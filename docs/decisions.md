# Decisions

_Non-obvious choices and why they were made. A couple of lines each. Six months on,
nobody remembers why, and without the note someone unpicks it._

| Date | Decision | Reason | Alternative considered |
|---|---|---|---|
| 2026-09-21 | Moved from a Claude Artifact prototype to a real App project, single static HTML/CSS/JS file in `src\index.html` | Artifacts are private, sandboxed, and not what "hosted externally, URL-driven" means. Nick confirmed this should be a real, published site | Keeping it as an Artifact indefinitely — rejected, doesn't match the stated long-term goal |
| 2026-09-21 | Square corners throughout, not the rounded corners the reference site (bms-engineer-academy) uses | Nick: "if the io design says square corners go with that" — `io-design-365` is explicit on this | Matching the reference site's rounded corners exactly — rejected |
| 2026-09-21 | Navigation uses plain JavaScript view-switching, not URL hash routing | The Claude Artifact version's hash-based links didn't work reliably inside the artifact viewer's iframe. Switching to in-memory routing fixed it | Kept for this App version too, for consistency — worth revisiting once actually hosted, since real URL routing (e.g. `/modules/01-welcome`) would be possible and preferable on GitHub Pages |
| 2026-09-21 | Separate new GitHub repo, not a new section inside bms-engineer-academy | Nick's explicit choice | A shared repo with the BMS Academy site — rejected |
| 2026-09-21 | Real narration audio via `edge-tts`, voice `en-GB-RyanNeural`, generated to `src\audio\*.mp3` | Same free, no-API-key tool and voice already used and approved on bms-engineer-academy — Nick asked VS Code/Claude directly which TTS it used there and got this answer | Browser built-in `speechSynthesis` (kept only as a fallback if a file fails to load) — rejected as the primary, sounded robotic |
| 2026-09-21 | GitHub Pages deploys via a GitHub Actions workflow (`.github\workflows\deploy.yml`) that publishes `src\` directly, rather than classic branch-based Pages | Classic GitHub Pages only serves the repo root or a `/docs` folder, which would have meant duplicating `src\` into `docs\` on every change. Actions-based Pages can publish any folder directly | Moving the app into a `docs\` folder at repo root instead of `src\` — rejected, breaks the App project's own `src\` convention for no real benefit |
