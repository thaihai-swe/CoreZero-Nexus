# Codemap

> Generated reference. Refresh when top-level layout changes.
> Last refresh: 2026-06-05 (CoreZero Nexus v0.2.0).

## Top-Level Map

| Path | Responsibility | Notes |
| :--- | :--- | :--- |
| `skills/` | Canonical workflow contracts and templates | Public commands map to `starter-*`, `context-*`, `spec-*`, and `harness-*` skill folders |
| `docs/` | Adopter-facing installed documentation | Includes `INSTALL.md`, `ADOPTION_GUIDE.md`, templates, generated references, and `architecture.md` |
| `documents/` | Maintainer-facing product documentation | Source-repo only; not part of the default installed surface |
| `memories/repo/` | Durable repo memory | `INDEX.md` router plus policy, heuristics, and project knowledge |
| `scripts/` | Installer and consistency automation | `install.sh` plus repo-local checks |
| `artifacts/` | Per-feature process state | Status, specs, plans, review, and session extracts under `features/<slug>/` |
| `rules/` | Language and security standards | Python, TypeScript, and security guidance |
| `.github/workflows/` | CI and release workflows | `harness-check.yml`, `auto-bump.yml`, `release.yml` |

## Repo-Root Files

| Path | Responsibility |
| :--- | :--- |
| `manifest.json` | Installer source of truth for overwrite, copy-if-missing, preserve, and template seeding |
| `VERSION` | Plain-text semver stamp mirrored to `<target>/.corezero-version` after install |
| `AGENTS.md` | Top-level router for repo-specific operating rules |
| `HARNESS_CARD.md` | One-page harness summary for this source repository |
| `README.md` | Product overview and audience split between adopter and maintainer surfaces |

## Key Entrypoints

- Path: `README.md`
  Purpose: top-level product overview and audience split
  Watchouts: keep the adopter/maintainer boundary explicit

- Path: `docs/README.md`
  Purpose: adopter start page for the installed surface
  Watchouts: lead with tasks and the canonical public workflow, not maintainer internals

- Path: `documents/README.md`
  Purpose: maintainer start page for evolving the kit itself
  Watchouts: do not re-teach the adopter journey in parallel with `docs/`

- Path: `scripts/install.sh`
  Purpose: manifest-driven installer; idempotent, ships itself to targets, supports curl-pipe
  Watchouts: must stay aligned with `manifest.json`, `docs/INSTALL.md`, and `templateMap`

- Path: `manifest.json`
  Purpose: declarative package inventory consumed by the installer
  Watchouts: every shipped file, seeded template, and preserved path must be classified here exactly once

## Major Boundaries

- Boundary: Adopter docs vs maintainer docs
  Owner: `docs/` and `documents/`
  Safe change guidance: keep adopter navigation in `docs/`; keep source-repo explanation in `documents/`

- Boundary: Skill contracts vs explanation surfaces
  Owner: `skills/`, `docs/`, and `documents/`
  Safe change guidance: when command behavior changes, update the matching docs and checks in the same wave

- Boundary: Kit content vs downstream-owned content
  Owner: `manifest.json` `files.overwrite`, `files.copyIfMissing`, and `files.preserve`
  Safe change guidance: decide packaging ownership once and encode it in the manifest

## Hot Paths

- Flow: Installer changes
  Primary files: `scripts/install.sh`, `manifest.json`, `docs/INSTALL.md`, `docs/README.md`
  Verification notes: run installer dry-run and confirm the installed surface matches the documented boundary

- Flow: Public workflow contract changes
  Primary files: `skills/*/SKILL.md`, `docs/README.md`, `docs/ADOPTION_GUIDE.md`, `documents/workflow.md`, `documents/skills-guide.md`
  Verification notes: sweep for stale command names and outdated next-step guidance

- Flow: Generated reference changes
  Primary files: `docs/generated/codemap.md`, `docs/generated/references-index.md`, `HARNESS_CARD.md`, `memories/repo/project-knowledge-base.md`
  Verification notes: generated references must only claim repo facts that are present and supported

- Flow: Release
  Primary files: `VERSION`, `manifest.json`, `.github/workflows/release.yml`, `.github/workflows/auto-bump.yml`
  Verification notes: tag must match `VERSION`; release workflows must only ship the intended package surface
