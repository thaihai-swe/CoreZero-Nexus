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
4. **Validation**: Run the validation commands required by the task.
5. **Log & Close**: Mark task `Done` in `artifacts/features/<slug>/tasks.md`.
6. **Next Step**: If tasks remain, continue. If complete, route to `/harness-verify`.

## Core Rules
- **No "Vibe Coding"**: Stick strictly to task scopes.
- **Stop at Scope Breaks**: If a requirement is missing or contradictory, return to `/spec-plan` instead of doing work-around coding.
