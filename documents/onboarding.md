# CoreZero Onboarding

Use this guide after installing the kit into an adopter repository.

## First 30 Minutes

1. Read `kit-map.md` to understand the command layers and ownership model.
2. Read `AGENTS.md` and `INDEX.md` at the repo root.
3. Fill in the adopter-owned project docs under `docs/project/` with known facts. Use `[UNKNOWN]` where the answer is not known yet.
4. Run `/starter-init` to bootstrap the repo-specific harness state.
5. Start the first feature with `/spec-requirements` when the goal is clear, or `/spec-research` when existing behavior needs investigation first.

## Normal Feature Flow

The core delivery path is:

`/starter-init` -> `/spec-research` or `/spec-requirements` -> `/spec-plan` -> `/spec-implement` -> `/harness-verify`

This path does not include every skill. It includes the minimum sequence for shipping a feature with a spec, plan, implementation proof, and verification pass.

## Session Flow

Use `/context-session` only after a feature slug and `artifacts/features/<slug>/status.md` already exist.

| Situation | Command |
|---|---|
| Resume an existing feature | `/context-session START` |
| Pause after meaningful progress | `/context-session CHECKPOINT` |
| Close a long session or prepare handoff | `/context-session END` |

`END` is emphasized because it creates durable handoff context before chat history disappears. It is not the only mode.

## Ownership During Upgrades

The installer treats files according to `manifest.json`:

- `overwrite` files are kit-managed and updated on each install.
- `copyIfMissing` files are adopter-owned seeds and are not overwritten after first install.
- `preserve` directories hold adopter state and must survive upgrades.

## Useful Follow-Up Commands

- `/context-status` shows active features, blockers, and recommended next commands.
- `/context-memory` promotes evidence-backed lessons after work is verified or a long session ends.
- `/harness-maintain` repairs stale indexes, generated references, or harness drift.
- `/technical-docs` and `/codebase-documenter` create durable documentation.
- `/visualize` creates diagrams when they materially improve clarity.

## Troubleshooting

- If a generated file looks stale, regenerate it with the owning skill instead of editing it by hand.
- If a feature has no `status.md`, start with `/spec-requirements` or `/spec-research`, not `/context-session`.
- If a session gets long or confusing, run `/context-session CHECKPOINT`; if context is saturated, run `/context-session END`.
- If installer validation fails, treat it as a kit packaging defect and repair the shipped source before distributing the kit.
