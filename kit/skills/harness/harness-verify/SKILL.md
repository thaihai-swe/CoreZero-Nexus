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
1. Run lint, typecheck, and test commands.
2. Verify all ACs from `spec.md` are satisfied.
3. If passes, update the `## Current State` section of `artifacts/features/<slug>/status.md` to `Verified`.
4. **If fails**: Increment a failure counter in `harness-telemetry.md`. If failures < 2, route back to `/spec-implement`. If failures >= 2 on the same task, route to `/spec-plan` to rethink the approach or trigger `/code-review` for intervention.
