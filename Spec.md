# Spec: Workspace Training Portal

_Written before code. Updated when the shape of the app changes. If a request would
change this, say so and get it agreed rather than quietly widening the scope._

## Who uses it

IO Controls staff getting set up with, or already using, their own AIS-OS Workspace —
any role: Admin, Supervisor, Engineer, Manager.

## What problem it solves

The training content (setup steps, folder structure, the six reference modules) needs to
live somewhere outside any one person's Claude setup: a shared, URL-addressable site
people can open whenever a question comes up, not files bundled inside each person's own
workspace copy. Modelled directly on the existing
[BMS Engineer Academy](https://geekneeus.github.io/bms-engineer-academy/) site.

## What it must do

- Present the setup steps, folder structure and six training modules, navigable without
  a page reload
- Track per-visitor progress (which modules are marked complete) locally in the browser
- Let a visitor read each module as a slide deck as well as plain text
- Read a module aloud (currently the browser's own built-in voice — see Open questions)
- Work as a static site with no backend: plain HTML, CSS and JavaScript, deployable to
  GitHub Pages

## What it will not do

- Store or sync progress across devices or people — that would need real shared state,
  which this project does not have
- Replace the AIS-OS Training Programme knowledge base in Nick's own workspace, which
  stays the maintained source of the module content
- Cover anything specific to one BMS product, customer site, or the smart BMS building
  enablement product

## How it is run

A static site. Locally, serve `src/` with any static file server (see README). Once
published, GitHub Pages serves it directly.

## Design system

`io-design-365` — this is internal IO Controls material, even though it is hosted outside
the company's own systems. Sentence case, IO Pink `#E61368` / IO Grey `#333333`, square
corners throughout (confirmed with Nick 2026-09-21 — no rounded corners despite the
reference site using them).

## Open questions

- Repo not yet created. Agreed with Nick: a separate new repo from bms-engineer-academy,
  not a section within it. Name and visibility (public/private) not yet decided.

## Resolved

- **Audio.** Same approach as bms-engineer-academy: `edge-tts` (free, open-source, no API
  key — taps Microsoft Edge's neural voices), voice `en-GB-RyanNeural`, matching the voice
  already chosen for the BMS Academy site. Real `.mp3` files generated per module into
  `src\audio\`, played with a normal `<audio>` element. Falls back to the browser's own
  built-in voice only if a file fails to load.
