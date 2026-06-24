# CoreZero

CoreZero has two explicit products:

- `kit/` — the installable adopter package
- `documents/` plus `page-document/` — maintainer and public explainer surfaces

## Purpose
| Area |Target State |
|------|---------------|--------------|
| **Harness Engineering**  | Configurable execution harness with lifecycle management |
| **Context Engineering**  | Dynamic context assembly, compression, relevance scoring |
| **Spec-Driven Development**  | Formal spec format, validation, traceability |
| **Templates**  | Composable template system with slots, conditions, chains |
| **Skills Library**  | Curated skill definitions with patterns |
| **Tooling**   | CLI, validators, generators |



## Install The Kit

```bash
curl -fsSL https://raw.githubusercontent.com/thaihai-swe/CoreZero-Nexus/main/kit/scripts/install.sh \
  | bash -s -- /path/to/your/project
```

After install, start with [kit/docs/index.html](kit/docs/index.html) and [documents/onboarding.md](documents/onboarding.md).

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
- `/ponytail`
- `/technical-docs`
- `/codebase-documenter`
- `/visualize`

## What Gets Installed

The installed surface comes from `kit/` and includes:

- root entrypoints: `AGENTS.md`, `MASTER_INDEX.md`
- first-read docs: `docs/index.html`, `docs/policies/code-design.md`
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

- Adopting the kit into a project: [kit/docs/index.html](kit/docs/index.html)
- Maintaining the kit itself: [documents/README.md](documents/README.md)
- Exact shipped tree and ownership: [documents/TEMPLATE_SURFACE.md](documents/TEMPLATE_SURFACE.md)
