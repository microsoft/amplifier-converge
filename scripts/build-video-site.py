#!/usr/bin/env python3
"""Assemble the static video site from checked, versioned release assets."""

import argparse
import hashlib
from html import escape
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site"


def stamp(seconds):
    minutes, seconds = divmod(int(seconds), 60)
    return f"{minutes}:{seconds:02d}"


def transcript(film):
    """One Markdown value supplies both the download and clipboard."""
    parts = [f"# {film['title']}", "Converge methodology — video transcript",
             f"[Watch this video](https://microsoft.github.io/amplifier-converge/#film-{film['id']}) · "
             "[Read the methodology](https://github.com/microsoft/amplifier-converge)"]
    for scene in film["scenes"]:
        parts.extend([f"## {stamp(scene['start'])} — {scene['title']}", scene["narration"]])
    return "\n\n".join(parts) + "\n"


def film_html(film, markdown):
    fid = film["id"]
    sections = []
    for scene in film["scenes"]:
        sections.append(f'''<section>
          <h3><a class="timestamp" href="{escape(film['mp4'])}#t={scene['start']}" data-player="player-{fid}" data-seek="{scene['start']}" aria-label="Play {escape(scene['title'])} at {stamp(scene['start'])}">{stamp(scene['start'])}</a>{escape(scene['title'])}</h3>
          <p>{escape(scene['narration'])}</p>
        </section>''')
    return f'''<section class="film" id="film-{fid}" aria-labelledby="title-{fid}">
    <p class="eyebrow">{stamp(round(film['duration']))} · Converge methodology</p>
    <h2 id="title-{fid}">{escape(film['label'])}</h2>
    <p class="takeaway">{escape(film['takeaway'])}</p>
    <div class="viewer">
      <video id="player-{fid}" controls playsinline preload="none" poster="{escape(film['poster'])}" aria-label="{escape(film['title'])}">
        <source src="{escape(film['mp4'])}" type='video/mp4; codecs="avc1.640028, mp4a.40.2"'>
        <source src="{escape(film['webm'])}" type='video/webm; codecs="vp9, opus"'>
        <track kind="captions" label="English" srclang="en" src="{escape(film['vtt'])}" default>
        <a href="{escape(film['mp4'])}">Download this video</a>
      </video>
      <div class="video-footer">
        <span>Illustrated scenario · AI narration</span>
        <div class="video-downloads"><a href="{escape(film['mp4'])}" download>Download MP4</a><a href="{escape(film['vtt'])}" download>Captions</a></div>
      </div>
    </div>
    <div class="actions transcript-actions">
      <button type="button" data-copy="markdown-{fid}" data-status="copy-status-{fid}" data-success="Copied as Markdown." aria-label="Copy transcript for {escape(film['label'])} as Markdown">Copy transcript</button>
      <a class="button-link" href="film-{fid}-transcript.md" download>Download Markdown</a>
      <span id="copy-status-{fid}" class="copy-status" role="status"></span>
    </div>
    <textarea id="markdown-{fid}" class="copy-fallback" aria-label="Markdown transcript for {escape(film['label'])}" readonly hidden>{escape(markdown)}</textarea>
    <details class="transcript">
      <summary>Transcript &amp; bookmarks</summary>
      <div class="transcript-body">{''.join(sections)}</div>
    </details>
  </section>'''


def build(media, output, manifest):
    if output.exists():
        raise SystemExit(f"Output already exists; choose an empty destination: {output}")
    # Verify everything before creating output, including local preview inputs.
    for asset in manifest["assets"]:
        name = asset["name"]
        if Path(name).name != name or name in (".", ".."):
            raise SystemExit(f"Invalid asset name: {name}")
        path = media / name
        if path.stat().st_size != asset["bytes"]:
            raise SystemExit(f"Wrong size: {name}")
        if hashlib.sha256(path.read_bytes()).hexdigest() != asset["sha256"]:
            raise SystemExit(f"Wrong SHA-256: {name}")

    files = [SOURCE / "style.css", SOURCE / "viewer.js", SOURCE / "scripts-and-storyboards.md"]
    files += sorted(SOURCE.glob("film-*.vtt")) + sorted(SOURCE.glob("film-*.srt"))
    films = json.loads((SOURCE / "films.json").read_text())
    generated = {f"film-{film['id']}-transcript.md": transcript(film) for film in films}
    html = (SOURCE / "index.html").read_text()
    if html.count("<!-- FILMS -->") != 1:
        raise SystemExit("Expected one film insertion point in index.html")
    generated["index.html"] = html.replace("<!-- FILMS -->", "\n\n".join(
        film_html(film, generated[f"film-{film['id']}-transcript.md"]) for film in films))
    for name, text in [(p.name, p.read_text()) for p in files] + list(generated.items()):
        if re.search(r"\.ts\.net|chatgpt\.com/space|/home/|localhost|127\.0\.0\.1", text):
            raise SystemExit(f"Private review reference in {name}")
    available = {p.name for p in files} | set(generated) | {a["name"] for a in manifest["assets"]}
    html = generated["index.html"]
    refs = re.findall(r'(?:href|src)="([^"]+)"', html)
    for film in films:
        refs.extend(film[key] for key in ("poster", "mp4", "webm", "vtt"))
    for ref in refs:
        if not ref.startswith(("https://", "#")) and ref.split("#")[0] not in available:
            raise SystemExit(f"Missing site file: {ref}")

    output.mkdir(parents=True)
    for path in files:
        shutil.copy2(path, output / path.name)
    for name, text in generated.items():
        (output / name).write_text(text)
    for asset in manifest["assets"]:
        shutil.copy2(media / asset["name"], output / asset["name"])
    (output / ".nojekyll").touch()
    print(f"Built {len(files) + len(generated) + len(manifest['assets'])} files in {output}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--media-dir", type=Path, help="Use existing media instead of downloading")
    parser.add_argument("--output", type=Path, default=ROOT / "_site")
    args = parser.parse_args()
    manifest = json.loads((SOURCE / "media-manifest.json").read_text())
    if args.media_dir:
        build(args.media_dir, args.output, manifest)
    else:
        with tempfile.TemporaryDirectory(prefix="converge-site-media-") as folder:
            command = ["gh", "release", "download", manifest["release"],
                       "--repo", manifest["repository"], "--dir", folder]
            for asset in manifest["assets"]:
                command += ["--pattern", asset["name"]]
            subprocess.run(command, check=True)
            build(Path(folder), args.output, manifest)


if __name__ == "__main__":
    main()
