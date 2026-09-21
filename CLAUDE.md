# App project: Workspace Training Portal

@README.md

You are working inside an **App project** (Spec, Code, Tests). Real people will use this
and keep using it. The code is the deliverable, not a means to one.

## The three layers

**1. Spec (the agreement)**
- `Spec.md` at the root: who uses it, what problem it solves, what it must do, and what
  it will not do
- Written before code. Updated when the shape of the app changes
- If a request would change the spec, say so and get it agreed rather than quietly
  widening the scope

**2. Code (the product)**, in `src/`
- Structured so someone else can find their way around it
- This code is maintained, not regenerated. It will be read, changed and extended by
  people who were not here when it was written
- Clarity beats cleverness every time. The reader is a busy engineer with a live site to
  get back to

**3. Tests (the safety net)**, in `tests/`
- Cover anything with logic in it: anything that calculates, decides, parses or transforms
- The point is not a coverage figure. The point is that a change can be made confidently
  six months from now
- A bug that reaches a user gets a failing test before it gets a fix, so it cannot come back

**Why it matters:** in an Automation project the local code is disposable tooling and the
output lives elsewhere. Here it is the opposite. The repo is the thing. Nothing here is
throwaway except `.tmp/`. Do not carry automation habits into this project.

## Design system

If the app has a user interface, use the `io-design-365` skill. Internal tools look like
our other work. Use `io-design-web` only if this app is public facing or sits alongside
the public website. Product interfaces (IO-CORE, IO-BASE, IO Pulse) are covered by
neither: ask before styling anything. Read the skill in place; never copy it into the project.

## How to operate

1. **Agree the spec before writing code.** Get `Spec.md` down first, even briefly. If any
   of it is unclear, ask. Building the wrong thing well is the expensive failure here.
2. **Keep it runnable at all times.** Small increments that leave the app working. Do not
   leave it half-migrated between two approaches. If something has to be broken for a
   while, say so up front.
3. **Someone else must be able to run this.** The README covers install, configure, run
   and test. `.env.example` lists every variable with a description and no real values.
   Assume the reader is one of the engineers and has never seen the project.
4. **Ask before adding dependencies.** Every dependency is something someone has to
   maintain and understand. Prefer the standard library. When one earns its place, say
   what it is for before adding it.
5. **Secrets live in `.env`, nowhere else.** No credentials, keys, tokens, site details or
   customer data in source, tests, fixtures or commit messages. Test data is invented,
   never copied from a live system.
6. **Refactor deliberately.** Improving code you are already in is fine. Restructuring the
   project, renaming widely, or changing an approach across the codebase needs a check
   with the owner first.
7. **Record decisions that were not obvious** in `docs/decisions.md`, with the reason in
   a couple of lines.

Pitch explanations to the owner's technical background, recorded in 
`01 Context\About Me.md`. Explain the software side properly; do not assume.

## Folders

```
README.md            Install, configure, run, test. Written for someone new. The owner reads the top.
CLAUDE.md            This file.
Spec.md              What it does, who for, what it will not do.
src/                 The application. The deliverable.
tests/               Tests for anything with logic.
docs/decisions.md    Non-obvious choices and why.
.env                 Secrets and configuration. Never anywhere else.
.env.example         Every variable, described, no real values.
.claude/launch.json  Optional. How to start the app for the browser preview.
.tmp/                Disposable. The only disposable thing here.
```

## Bottom line

You are building something people will rely on and come back to. Agree the spec, keep it
running, keep it testable, keep it explicable to someone who was not here. Leave it better
documented than you found it.
