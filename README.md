# CoreZero Nexus

CoreZero Nexus has two explicit products:

- `kit/` — the installable adopter package
- `documents/` plus `page-document/` — maintainer and public explainer surfaces

## Install The Kit

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/CoreZero-Nexus/main/scripts/install.sh \
  | bash -s -- /path/to/your/project
```

After install, start with [kit/docs/README.md](kit/docs/README.md) and [kit/docs/guides/onboarding.md](kit/docs/guides/onboarding.md).

## Shipped Commands

The installed package now ships the full workflow surface: core delivery, governance, docs authoring, and specialist visualization.

- `/starter-init`
- `/spec-research`
- `/spec-requirements`
- `/spec-plan`
- `/spec-implement`
- `/harness-verify`
- `/context-session`
- `/context-memory`
- `/context-status`
- `/context-compact`
- `/harness-maintain`
- `/spec-adr`
- `/code-review`
- `/technical-docs`
- `/codebase-documenter`
- `/visualize`

## What Gets Installed

The installed surface comes from `kit/` and includes:

- root entrypoints: `AGENTS.md`, `INDEX.md`, `HARNESS_CARD.md`
- first-read docs: `docs/README.md`, `docs/guides/onboarding.md`, `docs/policies/code-design.md`
- adopter-owned seeded docs under `docs/project/*`
- seeded placeholders under `docs/generated/*`
- shipped memories under `memories/repo/*` and `memories/domain/*`
- shipped skills under `skills/`, including docs authoring and visualization helpers
- shipped rules under `rules/`
- install and validation helpers under `scripts/`

Maintainer docs under `documents/` and site assets under `page-document/` do not get installed into adopter repositories.

## Source-Only Marker

`source-only` means an asset exists in this repo but is excluded from `kit/manifest.json` and the installer surface. No current shipped skill uses that marker.

## Choose Your Surface

- Adopting the kit into a project: [kit/docs/README.md](kit/docs/README.md)
- Maintaining the kit itself: [documents/README.md](documents/README.md)
- Exact shipped tree and ownership: [documents/TEMPLATE_SURFACE.md](documents/TEMPLATE_SURFACE.md)
