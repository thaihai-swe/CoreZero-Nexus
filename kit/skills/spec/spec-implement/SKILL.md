---
name: spec-implement
description: Execute implementation work task-by-task based on the plan.
compatibility: Designed for AI coding agents.
---

# Kit Implement

## Overview
Perform the coding work. Follow `artifacts/features/<slug>/tasks.md` and execute one approved task at a time.

## I/O Hand-off Protocol
- **Reads**: `artifacts/features/<slug>/plan.md`, `artifacts/features/<slug>/tasks.md`, `artifacts/features/<slug>/spec.md`, `memories/repo/harness-telemetry.md`.
- **Writes**: Source code, `artifacts/features/<slug>/tasks.md` (to mark tasks done), `artifacts/features/<slug>/status.md`, `memories/repo/harness-telemetry.md`.
- **Next Skill**: `/harness-verify`

## Workflow
1. **Initialize State**: Update the `## Current State` section of `artifacts/features/<slug>/status.md` to set phase to `Implementing`.
2. **Select Task**: Choose the first unblocked task ID from `artifacts/features/<slug>/tasks.md`.
3. **Coding**: Implement code and tests within the task boundary.
4. **Validation**: Run `bash kit/scripts/harness/gate-runner.sh` for all mechanical validation. If the gate fails, pipe the output into `bash kit/scripts/harness/telemetry-collector.sh` to log the failure, then resolve the root cause.
5. **Log & Close**: Mark task `Done` in `artifacts/features/<slug>/tasks.md`.
6. **Next Step**: If tasks remain, continue. If complete, route to `/harness-verify`.

## Core Rules
- **No "Vibe Coding"**: Stick strictly to task scopes.
- **Stop at Scope Breaks**: If a requirement is missing or contradictory, return to `/spec-plan` instead of doing work-around coding.
- **Minimum Viable Context (MVC)**: JIT-load only the specific files required for the current task. Do not load the entire codebase into context.
- **Context Eviction**: After running `gate-runner.sh`, you MUST summarize the raw terminal logs and evict the raw output from your context window to conserve token budget.
