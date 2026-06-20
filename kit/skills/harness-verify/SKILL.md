---
name: harness-verify
description: Verify implemented work against the spec and plan. Handles split verification modes, mechanical gates, implementation reviews (via the code-review skill), optional fallow-pass cleanup, manual testing guides, and final closeout authority.

---

# Harness Verify

## Overview
Use this skill to close the loop on a feature. It updates `status.md` to `Verifying`, runs mechanical gates, audits alignment and traceability, performs a security lens check, runs optional code-review or harness maintenance, executes fallow-pass cleanup, drafts testing scenarios, runs post-ship memory sync, and writes the final verdict in `review.md`.

## I/O Hand-off Protocol
- **Reads**: `artifacts/features/<slug>/tasks.md`, `artifacts/features/<slug>/spec.md`
- **Writes**: `artifacts/features/<slug>/status.md`, `memories/repo/harness-telemetry.md`
- **Next Skill**: `/context-memory` (to log lessons learned) or done.

## Workflow

1. **Initialization**: Update `artifacts/features/<slug>/status.md` phase to `Verifying`.
2. **Mechanical Gate Audit**: Run `bash kit/scripts/harness/gate-runner.sh` to mechanically verify the workspace. Do not guess commands. Write the results into `review.md`.
3. **Gate Failure Telemetry**: If the gate in Step 2 fails, increment a failure counter in `memories/repo/harness-telemetry.md`. If failures < 2, hand off to `/spec-implement`. If failures >= 2 on the same task, escalate to the user for a rethink or route to `/code-review`. Do not proceed.
4. **Clean-State Check**: Ensure no uncommitted changes or broken builds.
5. **Alignment Audit**: For each AC in `spec.md`, identify the task ID (`T-NN`) in `tasks.md` whose validation covers it.
   **Pass/Fail threshold**: Zero tolerance — every `AC-*` item in `spec.md` must map to at least one task with recorded validation evidence in `tasks.md`. A single AC with no implementation evidence = `Fail`. There is no partial pass.
6. **Security Lens**: Audit verified scope against `memories/repo/core-policies.md ## Security Policy`.
7. **Fallow Pass (Optional)**: Simplify touched files by removing dead code/unused imports.
   **Scope limit**: Applies only to files explicitly listed in this feature's `tasks.md` task targets. No structural refactors are allowed during this step. Re-run the mechanical gate after cleanup before proceeding.
8. **Helper Skills**:
   - **Code Review**: For substantial changes, invoke `/code-review` and merge findings into `review.md`.
   - **Harness Maintain**: Invoke `/harness-maintain` if changes touch the kit structure.
9. **Artifact Generation**: Write findings into `review.md`. Draft `testing-scenarios.md` using `references/testing-scenarios-template.md` (Required for `Complex`, optional for `Standard`).
10. **Finalization & Handoff**: Set verdict (`Pass`, `Pass with Follow-Up Debt`, or `Fail`). If passed, update `status.md` to `Done` and explicitly hand off to `/context-memory` for post-ship sync.

## Core Rules

- **Proof Must Match Plan**: Require verification on the planned proof surfaces.
- **Evidence over Confidence**: Review fresh, reproducible execution outputs.
- **Split Modes**: Perform mechanical, alignment, and security audits separately.
- **Drift Detection**: Mismatches between code and spec must fail verification.
- **Done Authority**: This skill is the sole authority for marking a feature `Done`.
