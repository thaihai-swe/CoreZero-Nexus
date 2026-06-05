# Architecture

Living architecture doc for the installed CoreZero Nexus surface.

## System Snapshot

- Repository type: Adopter-facing harness package
- Primary runtime(s): Markdown, Bash, optional Python 3 for validation helpers
- Main entrypoints: `AGENTS.md`, `HARNESS_CARD.md`, `docs/README.md`, `scripts/install.sh`, `skills/*/SKILL.md`
- Deployment shape: Installed workflow layer inside a downstream repository
- Confidence: High

## Top-Level Components

| Component | Responsibility | Key Paths | Notes |
| --- | --- | --- | --- |
| Router and policy entrypoints | Load-order and operating defaults | `AGENTS.md`, `HARNESS_CARD.md`, `memories/repo/*` | Router stays thin; durable rules live in memory files |
| Installed docs | User-facing operating guidance | `docs/*.md`, `docs/generated/*`, `docs/system-specs/README.md` | Must match shipped files exactly |
| Skill contracts | Canonical workflow behavior | `skills/*/SKILL.md`, `skills/*/references/` | Behavioral source of truth |
| Maintenance scripts | Install, repair, and surface validation | `scripts/install.sh`, `scripts/doctor.sh`, `scripts/check-surface-truth.py` | Used for install, drift checks, and smoke tests |
| Verification workflow | Continuous consistency checks | `.github/workflows/harness-check.yml` | Same workflow contract as the source repository |

## Runtime Boundaries

- Boundary: Installed docs vs source-repo maintainer docs
  Owner: `docs/` in the installed repo; `documents/` in the source repo
  Crossing rule: installed docs must never depend on nonexistent local maintainer files

- Boundary: Skill behavior vs explanation surfaces
  Owner: `skills/*/SKILL.md`
  Crossing rule: when a command or artifact contract changes, update `skills/`, `docs/`, `documents/`, and generated references together

- Boundary: Kit-managed vs adopter-owned files
  Owner: `manifest.json` in the source repo
  Crossing rule: overwrite only kit-managed files; preserve adopter-owned seeded content and artifacts

## Safe Change Guidance

- High-risk areas: `scripts/install.sh`, `.github/workflows/harness-check.yml`, `docs/generated/*`, shipped path claims in `docs/*.md`
- Required proof: installer dry-run, install smoke test, and `scripts/check-surface-truth.py`
