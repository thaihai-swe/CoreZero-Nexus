# Shipped Template Surface

This document defines the installed surface that adopters receive from `kit/`.

---

## Package Rules

- Canonical source of truth: `kit/manifest.json`
- `overwrite` = kit-managed content replaced on upgrade
- `copyIfMissing` = seeded adopter-owned content
- `preserve` = adopter state never rewritten by the installer

---

## Installed Surface

| Path | Posture | Notes |
|---|---|---|
| `AGENTS.md` | `copyIfMissing` | Canonical agent-agnostic runtime router |
| `INDEX.md` | `copyIfMissing` | Root routing index for memory files |
| `docs/README.md` | `overwrite` | Installed documentation start page |
| `docs/index.html` | `overwrite` | HTML documentation view |
| `docs/policies/code-design.md` | `overwrite` | Shipped code design quality policies |
| `docs/project/*` | `copyIfMissing` | Seeded adopter-owned project documentation |
| `docs/generated/*` | `copyIfMissing` | Seeded index placeholders (`codemap.md`, etc.) |
| `memories/repo/*` | `copyIfMissing` | Durable repository-wide configuration memories |
| `memories/domain/*` | `copyIfMissing` | Domain-specific pack templates |
| `skills/_shared/*` | `overwrite` | Shared skill resources and profiles |
| `skills/harness/starter-init/**` | `overwrite` | Environment bootstrap core skill |
| `skills/spec/spec-requirements/**` | `overwrite` | Socratic requirements intake core skill |
| `skills/spec/spec-plan/**` | `overwrite` | Feature implementation planning core skill |
| `skills/spec/spec-implement/**` | `overwrite` | Task coding execution core skill |
| `skills/harness/harness-verify/**` | `overwrite` | Mechanical verification core skill |
| `skills/context/context-session/**` | `overwrite` | Session boundary control core skill |
| `skills/context/context-memory/**` | `overwrite` | Post-ship memory promotion core skill |
| `skills/context/context-compact/**` | `overwrite` | Memory file compaction & GC core skill |
| `skills/context/context-status/**` | `overwrite` | Feature state reporting governance skill |
| `skills/harness/harness-maintain/**` | `overwrite` | Harness telemetry and index maintenance skill |
| `skills/spec/spec-adr/**` | `overwrite` | Architectural Decision Record manager skill |
| `skills/utilities/code-review/**` | `overwrite` | Quality and safety gate code review skill |
| `skills/utilities/technical-docs/**` | `overwrite` | API schema and technical docs generator skill |
| `skills/utilities/codebase-documenter/**` | `overwrite` | Orientation guide generator skill |
| `skills/utilities/visualize/**` | `overwrite` | Mermaid layout and architecture visualizer skill |
| `skills/README.md` | `overwrite` | Shipped skills index |
| `docs/rules/README.md` | `overwrite` | Rules index |
| `docs/rules/python.md` | `overwrite` | Python coding rules |
| `docs/rules/security.md` | `overwrite` | Security policies and guidance |
| `.gitignore` | `append` | Excludes generated outputs and local caches |
| `scripts/install.sh` | `overwrite` | Package installer |
| `scripts/harness/gate-runner.sh` | `overwrite` | Mechanical verification gate runner |
| `scripts/harness/telemetry-collector.sh` | `overwrite` | Gate execution telemetry log collector |
| `scripts/generate-dashboard.py` | `overwrite` | Adopter-facing dashboard generator |
| `artifacts/` | `preserve` | Adopter feature status and workspace state |

---

## Not In The Installed Surface

- `documents/`
- `page-document/`
- root repo workflows and maintainer scripts

If a future skill stays in the repo but out of the installed surface, mark it `source-only` anywhere that mixed shipped/non-shipped command lists appear.

---

## Ownership

| Area | Owner |
|---|---|
| shipped package behavior | `kit/skills/*/SKILL.md` and `kit/manifest.json` |
| installer semantics | `kit/scripts/install.sh` |
| maintainer explanation | `documents/` |
| public landing pages | `page-document/` |
