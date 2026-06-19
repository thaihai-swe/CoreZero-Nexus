---
name: harness-verify
description: Run the verification suite and check for regressions.
compatibility: Designed for AI coding agents.
---

# Harness Verify

## Overview
Validates that the implemented feature works and didn't break existing behavior.

## I/O Hand-off Protocol
- **Reads**: `artifacts/features/<slug>/tasks.md`, `artifacts/features/<slug>/spec.md`
- **Writes**: `artifacts/features/<slug>/status.md`, `memories/repo/harness-telemetry.md`
- **Next Skill**: `/context-memory` (to log lessons learned) or done.

## Workflow
1. Run `bash kit/scripts/harness/gate-runner.sh` to mechanically verify the workspace. Do not guess commands.
2. **AC Traceability Check** — for each AC in `spec.md`:
   1. Identify the task ID (`T-NN`) in `tasks.md` whose proof validation covers that AC.
   2. Confirm that task is marked `Done`.
   3. Confirm the gate runner in Step 1 passed.
   If any AC has no corresponding `Done` task, or the gate failed, block and route back to `/spec-implement` with a list of unresolved ACs.
3. If passes, update the `## Current State` section of `artifacts/features/<slug>/status.md` to `Verified`.
4. **If fails**: Increment a failure counter in `harness-telemetry.md`. If failures < 2, route back to `/spec-implement`. If failures >= 2 on the same task, route to `/spec-plan` to rethink the approach or trigger `/code-review` for intervention.
