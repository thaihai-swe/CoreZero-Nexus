---
name: spec-implement
description: Execute implementation work task-by-task. Uses the approved spec, plan, and task list to drive code changes with strict status tracking and validation.

---

# Kit Implement

## Overview

Use this skill to perform the coding work. Follow `artifacts/features/<slug>/tasks.md` , execute one approved task at a time, and keep task state and proof honest. Answers: can I complete the selected task and prove it without inventing new scope?


## I/O Hand-off Protocol
- **Reads**: `artifacts/features/<slug>/plan.md`, `artifacts/features/<slug>/tasks.md`, `artifacts/features/<slug>/spec.md`, `memories/repo/harness-telemetry.md`.
- **Writes**: Source code, `artifacts/features/<slug>/tasks.md` (to mark tasks done), `artifacts/features/<slug>/status.md`, `memories/repo/harness-telemetry.md`, `artifacts/features/<slug>/progress.md`.
- **Next Skill**: `/harness-verify`

## Workflow

1. **Initialization**: Update `artifacts/features/<slug>/status.md` phase to `Implementing`.
2. **Resumption Check**: (If resuming mid-task) Read the last entry in `progress.md` to identify the interrupted task. Re-run the task's proving command from pre-flight. If the proving command now fails, treat the task as not started: reset its status to `Pending` and restart from Step 3.
3. **Select Task**: Choose the first unblocked task ID (e.g., `T-01`) from `artifacts/features/<slug>/tasks.md`. Declare the target task before coding.
4. **Status Update**: Mark the task `In Progress` in `tasks.md`.
5. **Pre-Flight Baseline**: Read the task requirements. **Run the task's validation/proving command once in the terminal before editing** to establish a baseline. If files don't exist, create skeleton files first.
6. **Coding & Provenance**: Implement code and tests within the task boundary. Follow `rules/` (including `ponytail.md` for simplicity) and guidelines in `references/implementation-standards.md`.
    - **Decision Provenance**: If implementation requires a design decision not covered in `spec.md` or `plan.md` (e.g., swapping a library), stop coding. Route to `/spec-adr` if architectural. For minor choices: append a `## Decision Record` block to `progress.md` (choice, reason) before writing code. Do not implement undocumented mid-flight decisions silently.
    - **Proof Policy**: Satisfy planned proof surfaces. If the plan mandates tests, implement them.
7. **Mechanical Validation**: Re-run the local task proof to verify passes. Then, run `bash kit/scripts/harness/gate-runner.sh` for all mechanical validation. If the gate fails, pipe the output into `bash kit/scripts/harness/telemetry-collector.sh` to log the failure, then resolve the root cause.
8. **Logging & Close**: Add validation evidence (e.g. test outputs) to `tasks.md`. Mark task `Done`. Update `progress.md` with session notes.
9. **Next Step**: If tasks remain, continue `/spec-implement`. If complete, hand off to `/harness-verify`. If issues arise (scope break, planning gaps), stop and route to `/spec-plan`.

## Core Rules
- **No "Vibe Coding"**: Stick strictly to task scopes.
- **Stop at Scope Breaks**: If a requirement is missing or contradictory, return to `/spec-plan` instead of doing work-around coding.
- **Ponytail Rule**: Maintain the lazy senior dev mindset. Never over-engineer. Use the standard library and native features before adding dependencies or custom code.
- **Minimum Viable Context (MVC)**: JIT-load only the specific files required for the current task. Do not load the entire codebase into context.
- **Context Eviction**: After running `gate-runner.sh`, you MUST summarize the raw terminal logs and evict the raw output from your context window to conserve token budget.
