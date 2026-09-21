# Workspace Training Portal

| | |
|---|---|
| Type | App |
| Status | Active |
| Started | 2026-09-21 |
| Last updated | 2026-09-21 |
| Owner | Nick Goddard |

## Purpose

A standalone, URL-addressable training site for IO Controls staff using their own AIS-OS
Workspace — setup steps, the folder structure, and six reference modules, each readable
as a page, a slide deck, or read aloud. Modelled on the existing
[BMS Engineer Academy](https://geekneeus.github.io/bms-engineer-academy/) site. Started
as a Claude Artifact prototype, moved here to become the real, hosted version.

## Who uses it and what it must do

See `Spec.md`. Agree it before writing code.

## Install

Nothing to install. It's plain HTML, CSS and JavaScript — no build step, no packages.

## Configure

No configuration needed. Narration audio uses `edge-tts`, a free, open-source tool with
no API key — `python -m pip install edge-tts` is the only setup step, and only needed if
you're regenerating the audio (see below), not to run the site itself.

## Run

Open `src\index.html` directly in a browser, or use the browser preview below so it
behaves the way it will once it's actually hosted.

## Regenerating narration audio

If a module's text changes, its audio should be regenerated to match:

```
python -m pip install edge-tts
python tools\generate_audio.py
```

This reads the `NARRATION` text straight out of `src\index.html` and rewrites every
`src\audio\*.mp3`, so the audio is always regenerated from the same file the page itself
uses — never edited separately by hand.

## Test

No automated tests yet — it's a static page with no calculations or data processing to
get wrong. Check it by clicking through it in a browser: every nav link, both audio and
slide buttons on each module, and the progress tracker.

## Browser preview

If this app has a page to look at, `.claude\launch.json` in this folder tells Claude Code
how to start it. Open this app's folder itself as the working folder to use the preview.
Shape of the file:

```json
{
  "version": "0.0.1",
  "configurations": [
    { "name": "site", "runtimeExecutable": "python", "runtimeArgs": ["tools/serve.py"], "port": 8080 }
  ]
}
```

## Folders

- `Spec.md`: what it does, who for, what it will not do
- `src\`: the application
- `tests\`: tests for anything with logic
- `docs\decisions.md`: choices that were not obvious, and why
- `.tmp\`: disposable

## Background

_Facts carried over from earlier work, with dates and sources._

## Open questions

_None yet._
