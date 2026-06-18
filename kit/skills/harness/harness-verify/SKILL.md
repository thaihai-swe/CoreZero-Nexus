---
name: harness-verify
description: Run the verification suite and check for regressions.
compatibility: Designed for AI coding agents.
---

# Harness Verify

## Overview
Validates that the implemented feature works and didn't break existing behavior.

## I/O Hand-off Protocol
- **Reads**: `docs/generated/tasks.md`, `docs/project/requirements.md`
- **Writes**: `memories/repo/harness-telemetry.md`
- **Next Skill**: `/context-memory` (to log lessons learned) or done.

## Workflow
1. Run lint, typecheck, and test commands.
2. Verify all ACs from requirements are satisfied.
3. If passes, update the `## Current State` section of `memories/repo/harness-telemetry.md` to `Verified`.
4. If fails, route back to `/spec-implement`.
