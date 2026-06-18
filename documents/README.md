# Kit Documentation

Maintainer entrypoint for the CoreZero Nexus source repository.

## Start Here

CoreZero Nexus now has two explicit products:

- `kit/` — the installable adopter package
- `documents/` plus `page-document/` — maintainer and public explainer surfaces

When changing shipped behavior, start in `kit/`. When changing explanation, release notes, or site copy, work in `documents/` and `page-document/`.

## Maintainer Reading Order

1. [architecture.md](architecture.md) — repo architecture and boundaries
2. [TEMPLATE_SURFACE.md](TEMPLATE_SURFACE.md) — exact shipped surface and ownership
3. [INSTALL.md](INSTALL.md) — install, upgrade, and validation flow
4. [skills-guide.md](skills-guide.md) — shipped commands and any future `source-only` markers
5. [releasing.md](releasing.md) — release, version-sync, and Pages checklist

## Source Of Truth

The repo follows this truth order:

1. `kit/manifest.json` for shipped surface
2. `kit/skills/*/SKILL.md` for workflow behavior
3. `documents/` for maintainer explanation
4. generated files only as derived placeholders

## Current Packaging Position

The installed package ships the full command surface:

- shipped commands:
  - `/starter-init`
  - `/spec-research`
  - `/spec-requirements`
  - `/spec-plan`
  - `/spec-implement`
  - `/harness-verify`
  - `/context-session`
  - `/context-memory`
  - `/context-status`
  - `/harness-maintain`
  - `/spec-adr`
  - `/code-review`
  - `/technical-docs`
  - `/codebase-documenter`
  - `/visualize`
- the `source-only` marker is reserved for future skills that remain in the repo but stay out of `kit/manifest.json`

## Validation

For packaging changes, at minimum run the installer flow locally:

```bash
bash scripts/install.sh /tmp/corezero-check --dry-run
```
