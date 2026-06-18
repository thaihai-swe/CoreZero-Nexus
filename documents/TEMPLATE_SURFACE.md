# Shipped Template Surface

This document defines the installed surface that adopters receive from `kit/`.

## Package Rules

- Canonical source of truth: `kit/manifest.json`
- `overwrite` = kit-managed content replaced on upgrade
- `copyIfMissing` = seeded adopter-owned content
- `preserve` = adopter state never rewritten by the installer

## Installed Surface

| Path | Posture | Notes |
|---|---|---|
| `AGENTS.md` | `copyIfMissing` | Runtime router |
| `INDEX.md` | `copyIfMissing` | Root routing index |
| `HARNESS_CARD.md` | `copyIfMissing` | Harness summary |
| `docs/README.md` | `overwrite` | Installed start page |
| `docs/index.html` | `overwrite` | HTML start page |
| `docs/guides/onboarding.md` | `overwrite` | Required first-run guide |
| `docs/policies/code-design.md` | `overwrite` | Shipped design policy |
| `docs/project/*` | `copyIfMissing` | Adopter-owned project docs |
| `docs/generated/*` | `copyIfMissing` | Seeded placeholders |
| `memories/repo/*` | `copyIfMissing` | Durable repo memory |
| `memories/domain/*` | `copyIfMissing` | Domain pack templates |
| `skills/_shared/*` | `overwrite` | Shared skill references |
| `skills/starter-init/**` | `overwrite` | Shipped v2 core |
| `skills/spec-research/**` | `overwrite` | Shipped v2 core |
| `skills/spec-requirements/**` | `overwrite` | Shipped v2 core |
| `skills/spec-plan/**` | `overwrite` | Shipped v2 core |
| `skills/spec-implement/**` | `overwrite` | Shipped v2 core |
| `skills/harness-verify/**` | `overwrite` | Shipped v2 core |
| `skills/context-session/**` | `overwrite` | Shipped v2 core |
| `skills/context-memory/**` | `overwrite` | Shipped v2 core |
| `skills/context-status/**` | `overwrite` | Governance bundle |
| `skills/harness-maintain/**` | `overwrite` | Governance bundle |
| `skills/spec-adr/**` | `overwrite` | Governance bundle |
| `skills/code-review/**` | `overwrite` | Core quality gate |
| `skills/technical-docs/**` | `overwrite` | Docs authoring bundle |
| `skills/codebase-documenter/**` | `overwrite` | Docs authoring bundle |
| `skills/visualize/**` | `overwrite` | Specialist visualization bundle |
| `skills/README.md` | `overwrite` | Shipped skills index |
| `rules/README.md` | `overwrite` | Rules index |
| `rules/python.md` | `overwrite` | Python guidance |
| `rules/security.md` | `overwrite` | Security guidance |
| `scripts/install.sh` | `overwrite` | Package installer |
| `scripts/generate-dashboard.py` | `overwrite` | Optional dashboard helper |
| `artifacts/` | `preserve` | Adopter feature state |

## Not In The Installed Surface

- `documents/`
- `page-document/`
- root repo workflows and maintainer scripts

If a future skill stays in the repo but out of the installed surface, mark it `source-only` anywhere that mixed shipped/non-shipped command lists appear.

## Ownership

| Area | Owner |
|---|---|
| shipped package behavior | `kit/skills/*/SKILL.md` and `kit/manifest.json` |
| installer semantics | `kit/scripts/install.sh` |
| maintainer explanation | `documents/` |
| public landing pages | `page-document/` |
