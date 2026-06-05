# Agent Router

Read this file first. Use it as a router, not a full handbook.

## Priority Rules

- Start with the answer, action, blocker, or decision.
- Correct false premises before continuing.
- Mark missing information as `[UNKNOWN]`.
- Touch only the requested scope.
- Preserve current behavior unless the user asks to change it.
- Do not claim success without fresh evidence from the real path.

## Load Order

1. Read `HARNESS_CARD.md`.
2. Read `memories/repo/INDEX.md`, then `constitution.md`, `harness-config.md`, and `security-policy.md`.
3. Load only the by-intent memory groups that match the task.
4. Open the active skill under `skills/<name>/SKILL.md`.

## Core Workflow

- `/starter-init` for bootstrap
- `/spec-research` for brownfield discovery
- `/spec-requirements` -> `/spec-plan` -> `/spec-implement` for feature delivery
- `/context-session` for session resume, checkpoint, and handoff after a feature slug exists
- `/harness-verify` for proof and closeout
- `/harness-maintain` or `scripts/doctor.sh` for harness repair

## Canonical Surfaces

- `docs/README.md`
- `docs/code-design.md`
- `memories/repo/constitution.md`
- `memories/repo/harness-config.md`
- `memories/repo/security-policy.md`

If a command, artifact name, or path changes, update the skill contract, installed docs, maintainer docs, and generated references in the same change.
