---
name: harness-verify
description: Verify implemented work against the spec and plan. Handles split verification modes, mechanical gates, implementation reviews (via the code-review skill), optional fallow-pass cleanup, manual testing guides, and final closeout authority.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in spec-driven repositories that use memories/repo/ and artifacts/features/<slug>/.

---

# Kit Verify



## Overview

Use this skill to close the loop on a feature. It updates `status.md` to `Verifying`, runs mechanical gates, audits alignment and traceability, performs a security lens check, runs optional code-review or harness maintenance, executes fallow-pass cleanup, drafts testing scenarios, runs post-ship memory sync, and writes the final verdict in `review.md`.

## Read First

- `status.md`, `spec.md`, `plan.md`, `tasks.md`, and test/build output.
- `memories/repo/INDEX.md` (memory router)
- `memories/repo/constitution.md` and `memories/repo/security-policy.md`
- `memories/repo/harness-config.md` (canonical verification commands)
- References: `references/definition-of-done.md`, `references/review-template.md`, `../_shared/rigor-profiles.md`, and `../context-memory/references/post-ship-sync.md`.

## When to Use

- Review implementation against spec requirements.
- Audit traceability and detect spec drift.
- Perform behavior-neutral code cleanup (fallow pass).

## Workflow

1. **Initialization**: Update `status.md` to `Verifying`. Load active rigor profile.
2. **Mechanical Gate Audit**: Run the exact proof commands in `plan.md` (e.g. test, lint) and write results in `review.md`. If gate fails, stop.
3. **Clean-State Check**: Ensure no uncommitted changes or broken builds.
4. **Alignment Audit**: Map each `REQ-X` from `spec.md` to the implementation, flagging missing, ghost, or misaligned behaviors.
   **Pass/Fail threshold**: Zero tolerance — every `AC-*` item in `spec.md` must map to at least one task with recorded validation evidence in `tasks.md`. A single AC with no implementation evidence = `Fail`. There is no partial pass.
5. **Traceability & Baseline**: Verify `REQ -> AC -> TASK -> validation` trace and check if validation was run *prior* to implementation. (Required for `Complex`, optional for `Standard`).
6. **Security Lens**: Audit verified scope against `security-policy.md`.
7. **Helper Skills**:
   - **Code Review**: For substantial changes, invoke `/code-review` (passing touched files, ACs, tasks) and merge findings into `review.md`.
   - **Harness Maintain**: Invoke `/harness-maintain` if changes touch the harness.
8. **Optional Fallow Pass**: Simplify touched files by removing dead code/unused imports. Do not change behavior; re-run verification after cleanup.
   **Scope limit**: Fallow pass applies only to files explicitly listed in this feature's `tasks.md` task targets. No changes to adjacent or related files, even if they contain dead code. Re-run the mechanical gate after cleanup before writing the final verdict.
9. **Write Review**: Output findings by mode and cleanup details in `review.md`.
10. **Scenarios**: Draft `testing-scenarios.md` for human testing (Required for `Complex`, optional for `Standard`). Draft using `references/testing-scenarios-template.md`. Required for `Complex`; optional for `Standard`; skip for `Tiny` unless behavior is user-visible.
11. **Post-Ship Knowledge Sync**: Invoke `/context-memory` Post-Ship Sync (Standard/Complex profiles or when reusable knowledge is produced).
12. **Finalization**: Set verdict (`Pass`, `Pass with Follow-Up Debt`, or `Fail`). If passed and memory sync is done, update `status.md` to `Done`.

## Stop Conditions

- Proposed cleanup changes behavior or expands beyond the verified feature surface (fallow-pass scope creep).
- `plan.md` exists but has no `## Mechanical Verification Gate` section → stop. Route to `/spec-plan` to add the gate before verifying.
- Proof command exits non-zero after 2 distinct fix attempts → stop. Write findings to `review.md` with verdict `Fail`. Surface to user for resolution before retrying verification.
- Security audit (Step 6) finds a P0 violation (as defined in `security-policy.md`) → stop. Verdict is `Fail` regardless of other checks. No pass until the violation is resolved and re-verified.

## Preconditions

- **Required Phase**: `Implementing` in `status.md`.
- **Required Artifacts**: `spec.md`, `plan.md` (must have `## Mechanical Verification Gate`), `tasks.md`.
- **Phase sets**: `Verifying` → `Done` (on pass).

## Core Rules

- **Proof Must Match Plan**: Require verification on the planned proof surfaces.
- **Evidence over Confidence**: Review fresh, reproducible execution outputs.
- **Split Modes**: Perform mechanical, alignment, and security audits separately.
- **Drift Detection**: Mismatches between code and spec must fail verification.
- **Done Authority**: This skill is the sole authority for marking a feature `Done`.

## Verdict Definitions

- **Pass**: All ACs verified with executed evidence. No unresolved required findings.
- **Pass with Follow-Up Debt**: All ACs verified, but non-blocking quality issues exist (e.g., missing inline comments, non-critical dead code not in the fallow pass scope). Requires creating a debt entry in `docs/TECH_DEBT_REGISTER.md` before marking `Done`.
- **Fail**: One or more ACs not verified, a gate command fails, or a P0 security violation is found. `status.md` stays at `Verifying`. Route to the responsible phase skill.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "The diff looks correct." | Verification requires executed evidence, not plausibility. |
| "Tests pass, so we're good." | Passing tests do not validate design quality or alignment. |
| "I'll add the tests in a separate PR." | Missing planned proof is a verification failure. |
| "I'll clean up adjacent files." | Fallow pass is strictly surgical and limited to touched files. |

## Red Flags

- Verdict depends on confidence or code reading rather than test execution.
- Task status contradicts validation evidence.
- Fallow pass changes behavior or expands scope.

## Verification

- [ ] Every finding points to fresh, traceable evidence.
- [ ] Alignments, gates, and security parameters checked.
- [ ] Fallow pass verified as behavior-neutral.
- [ ] Verdict and final phase transition are explicit.

## Output Rules

- Update only: `review.md`, `testing-scenarios.md`, `status.md`.
- Do not rewrite `spec.md` or `plan.md` directly.
