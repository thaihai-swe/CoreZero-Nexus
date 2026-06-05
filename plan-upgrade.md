# `plan-upgrade.md` — Harness Lifecycle And Surface-Truth Remediation

## Summary

Replace the current implied lifecycle with one canonical contract:

`install.sh` seeds the harness surface, `/starter-init` reconciles only installer-seeded repo-level files, the **first feature starts with `/spec-requirements` or `/spec-research`**, `/context-session` is used only once a feature slug already exists, and `/harness-verify` remains the only closeout authority.

This plan should be written as a new root file `plan-upgrade.md`. It is a full remediation plan, not a narrow patch. It covers the end-to-end flow bug, the remaining `starter-init` drift, public surface truth, brownfield-strengthening work, acceptance testing, and repair-path hardening. It does **not** include the excluded items: measurable context operations, stronger multi-agent primitives, or reference packs.

## Important Public Contract Changes

- **First-feature command sequence changes**
  - Greenfield: `install.sh` -> `/starter-init` -> `/spec-requirements` -> `/spec-plan` -> `/spec-implement` -> `/harness-verify`
  - Brownfield: `install.sh` -> `/starter-init` -> `/spec-research` -> `/spec-requirements` -> `/spec-plan` -> `/spec-implement` -> `/harness-verify`
  - `/context-session` is no longer advertised as the immediate post-init command for a brand-new repo.

- **`/context-session` scope is narrowed and made explicit**
  - It remains the session boundary skill for `START`, `CHECKPOINT`, and `END`.
  - `START` requires an existing feature slug and `artifacts/features/<slug>/status.md`.
  - If no feature slug exists yet, the skill must stop and route to `/spec-requirements` or `/spec-research`, not self-bootstrap feature state.

- **`/starter-init` contract is locked**
  - It may update only installer-seeded repo-level files.
  - It must not create feature-local artifacts such as `status.md`, `progress.md`, `tasks.md`, `plan.md`, `spec.md`, or `handoff.md`.
  - Missing seeded files are install-surface failures and must route to `scripts/doctor.sh` or `install.sh`, never be silently recreated by init.

## Implementation Changes

### 1. Canonical lifecycle realignment

- Rewrite every adopter-facing flow surface to match the spec-first lifecycle:
  - installer next-step output
  - `kit/docs/INSTALL.md`
  - `kit/docs/README.md`
  - `kit/docs/ADOPTION_GUIDE.md`
  - root `README.md`
  - root `AGENTS.md` and `kit/AGENTS.md`
- Update durable memory and harness summaries so they no longer claim “every work session must open with `/context-session`” for the first feature.
- Change lifecycle wording everywhere from `init -> session -> verify` to a model that includes feature creation/spec entry before session management.

### 2. `starter-init` hardening

- Fix the remaining internal drift in `kit/skills/starter-init/SKILL.md`:
  - remove the `Creates progress logs` phase claim
  - change the handoff target from `/context-session` to `/spec-requirements` or `/spec-research`
  - fix duplicate workflow numbering
  - keep the “No Shadow Installer” rule as the central invariant
- Audit all `starter-init` references so none imply feature-local artifact creation.
- Remove or relocate leftover starter-owned progress scaffolding if it no longer belongs to init.
  - If the progress template is still needed, move ownership to the session skill or a shared reference owned by the actual writer.

### 3. `context-session` contract hardening

- Update `kit/skills/context-session/SKILL.md` and `references/session-start-flow.md` so the first line of the contract is “resume/manage an existing feature session.”
- Add an explicit stop condition for “no existing feature slug / no `status.md`.”
- Add routing guidance:
  - use `/spec-requirements` when requirements can be defined directly
  - use `/spec-research` when brownfield behavior or root cause is unknown
- Keep `CHECKPOINT` and `END` behavior unchanged except for any wording needed to align with the new lifecycle.

### 4. Surface-truth sweep and source-of-truth hardening

- Make `manifest.json` plus installer behavior the canonical shipped-surface contract.
- Reconcile all shipped docs, generated references, harness summaries, tutorials, and maintainer docs with the same lifecycle and file-ownership model.
- Sweep diagrams and tutorials that still show `/context-session` immediately after `/starter-init`.
- Add CI assertions that fail when:
  - adopter docs advertise a first-feature sequence that contradicts skill preconditions
  - `starter-init` claims ownership of feature-local artifacts
  - `context-session` is described as first-feature bootstrap
  - referenced shipped paths or commands are missing or renamed

### 5. Brownfield adoption strengthening

- Add a first-class brownfield readiness artifact to the brownfield path.
  - minimum sections: preserved behavior inventory, target subsystem boundaries, reuse patterns, risk register, baseline proof surface, migration constraints
- Route this artifact through `/spec-research`, not `/starter-init`.
- Update adopter docs so brownfield work is clearly “understand current behavior first, then spec.”
- Add one realistic brownfield walk-through example in maintainer docs that uses the same canonical flow.

### 6. Acceptance testing and doctor-mode strengthening

- Add or expand self-tests for:
  - dry-run install
  - fresh install
  - reinstall preservation
  - first-feature greenfield flow contract
  - first-feature brownfield flow contract
  - no missing-path or wrong-command references in shipped docs
- Add a golden-path acceptance test for:
  - greenfield: install -> init -> requirements -> plan -> implement -> verify
  - brownfield: install -> init -> research -> requirements -> plan -> implement -> verify
- Strengthen `scripts/doctor.sh` so it can diagnose lifecycle drift, not only missing files:
  - wrong next-step guidance
  - missing seeded surface
  - feature state started from the wrong skill
  - stale or contradictory adopter docs

### 7. Guardrails on future growth

- Do not add new public slash commands as part of this remediation.
- Do not expand `context-session` into first-feature bootstrap.
- Do not add new duplicated templates for router or lifecycle docs.
- Do not introduce new template families unless they are included in the same source-of-truth and CI drift checks as the existing shipped surface.

## Test Plan

- `python3 kit/scripts/check-surface-truth.py --mode source-repo --root .`
- `bash kit/scripts/test-install.sh`
- Compare installer next-step output against the canonical lifecycle and fail if `/context-session` appears before first-feature creation.
- Add a static contract test that checks:
  - `/starter-init` docs never claim feature-local artifact creation
  - `/context-session` requires existing `status.md`
  - `/spec-requirements` and `/spec-research` remain the first creators of feature `status.md`
- Validate one docs-only golden-path walkthrough for greenfield and one for brownfield to ensure the command sequence is internally consistent from install to completed first feature.

## Assumptions And Defaults

- This plan is intended to be written to a new root file: `plan-upgrade.md`.
- The remediation reuses the existing `harness-upgrades` intent but does not require reusing that feature slug for implementation tracking.
- No new public slash command will be introduced.
- `manifest.json` and installer behavior remain the canonical shipped-surface contract.
- `documents/` stays maintainer-only unless already explicitly shipped through the installer.
- The preferred fix is **spec-first routing**, not expanding `/context-session` into a bootstrap skill.
