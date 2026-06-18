# CLAUDE.md

## What this repo is

CoreZero Nexus has two explicit products:

- `kit/` — the installable adopter package
- `documents/` plus `page-document/` — maintainer and public explainer surfaces

This repo is not a normal application. There is no root app build, test runner, or deploy step. The important verification here is package truth: docs, installer behavior, shipped file inventory, and release automation must agree.

Read `AGENTS.md` first. Then skim `kit/HARNESS_CARD.md` for the active rigor profile and known limits of the shipped package.

## Surface boundaries

- **`kit/`** is the shipped surface. `kit/manifest.json` is the source of truth for what adopters actually receive.
- **`documents/`** is maintainer-only documentation about the kit itself. It never ships downstream.
- **`page-document/`** is the lightweight public site surface used by GitHub Pages.

The root `AGENTS.md` is repo-specific and points into `kit/` for shipped policy surfaces. `kit/AGENTS.md` is the runtime router that gets installed into adopter repositories.

## Common commands

```bash
# Install or dry-run the shipped package
bash scripts/install.sh /path/to/target
bash scripts/install.sh /path/to/target --dry-run

```

## Invariants

1. Every shipped `kit/skills/<name>/` directory except `_shared` must contain `SKILL.md`.
2. Every manifest entry must resolve to a real shipped file or a valid template source.
3. Shipped docs must not link to missing shipped files.
4. Root docs, maintainer docs, shipped docs, and installer output must describe the same installed v2 surface.

## Working rules

- Make behavior changes in `kit/` when the change should ship.
- Make explanatory changes in `documents/` and `page-document/` when the change is maintainer-facing or public-site-facing.
- Treat `kit/docs/generated/*` as placeholders until they are refreshed.
- When changing installer behavior, think through both local execution and curl-piped clone execution.
