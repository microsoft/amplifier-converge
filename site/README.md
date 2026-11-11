# Video website

The [video website](https://microsoft.github.io/amplifier-converge/) presents three independent introductions to the Converge methodology. Captions, transcripts, downloads, and a starting prompt are included.

The page and captions live here. Larger video and image files live in the GitHub release named in [media-manifest.json](media-manifest.json). The build checks each file's size and SHA-256 before including it in the site, so playback and downloads come from the same site as the page.

To build with Python 3 and an authenticated GitHub CLI:

```sh
python3 scripts/build-video-site.py
python3 -m http.server --directory _site 8000
```

Open `http://localhost:8000/`. A local copy of the release files can be used with `--media-dir PATH`. Choose a fresh `--output PATH` when an output directory already exists. Delete the generated output after previewing.

To update a video, upload its media to a new versioned release, update the manifest and matching captions, transcript, storyboard, and timings. Check each film's playback, scene jumps, captions, downloads, starting prompt, and mobile layout before merging. The Pages workflow builds pull requests and deploys changes from `main`; it can also be run manually.

Keep private review links and production notes out of the published files. The build publishes only the viewer, scripts, captions, and the listed media. Repository guidance remains authoritative for the methodology.
