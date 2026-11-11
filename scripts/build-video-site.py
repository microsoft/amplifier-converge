#!/usr/bin/env python3
"""Assemble the static video site from checked, versioned release assets."""

import argparse
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import tempfile


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "site"


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

    files = [SOURCE / "index.html", SOURCE / "scripts-and-storyboards.md"]
    files += sorted(SOURCE.glob("film-*.vtt")) + sorted(SOURCE.glob("film-*.srt"))
    for path in files:
        text = path.read_text()
        if re.search(r"\.ts\.net|chatgpt\.com/space|/home/|localhost|127\.0\.0\.1", text):
            raise SystemExit(f"Private review reference in {path.name}")
    available = {p.name for p in files} | {a["name"] for a in manifest["assets"]}
    html = (SOURCE / "index.html").read_text()
    refs = re.findall(r'(?:href|src)="([^"]+)"', html)
    films = json.loads(html.split("const films=", 1)[1].split(";const player=", 1)[0])
    for film in films:
        refs.extend(film[key] for key in ("poster", "mp4", "webm", "vtt"))
    for ref in refs:
        if not ref.startswith(("https://", "#")) and ref not in available:
            raise SystemExit(f"Missing site file: {ref}")

    output.mkdir(parents=True)
    for path in files:
        shutil.copy2(path, output / path.name)
    for asset in manifest["assets"]:
        shutil.copy2(media / asset["name"], output / asset["name"])
    (output / ".nojekyll").touch()
    print(f"Built {len(files) + len(manifest['assets'])} files in {output}")


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
