---
name: spec-implement
description: Execute implementation work task-by-task. Uses the approved spec, plan, and task list to drive code changes with strict status tracking and validation.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in spec-driven repositories that use memories/repo/ and artifacts/features/<slug>/.

---

# Kit Implement


## Overview

Use this skill to perform the coding work. Follow `tasks.md`, execute one approved task at a time, and keep task state and proof honest. Answers: can I complete the selected task and prove it without inventing new scope?

## Read First

- `status.md`, `tasks.md`, `plan.md`, `spec.md` in `artifacts/features/<slug>/`.
- `memories/repo/constitution.md` (code standards) and `security-policy.md` (security design).
- `memories/repo/harness-config.md` (canonical build/test/lint commands).
- Touched files and interfaces.
- References: `references/design-standards.md`, `references/implementation-standards.md`, and `../_shared/rigor-profiles.md`.

## When to Use

- Execute tasks from `tasks.md` in order.
- Track task states (`Pending`, `In Progress`, `Done`).
- Implement features/fixes satisfying the spec/plan.

## Workflow

1. **Initialization**: Update `status.md` phase to `Implementing`.
2. **Select Task**: Choose the first unblocked task ID (e.g., `T-01`) from `tasks.md`. Declare the target task before coding.
3. **Pre-Flight Baseline**: Read the task requirements. **Run the task's validation/proving command once in the terminal before editing** to establish a baseline. If files don't exist, create skeleton files first.
4. **Status Update**: Mark the task `In Progress` in `tasks.md`.
5. **Coding**: Implement code and tests within the task boundary. Follow `rules/` and templates.
6. **Proof Policy**: Satisfy planned proof surfaces. If the plan mandates tests, implement them.
7. **Validation**: Re-run the validation command to verify passes.
8. **Logging & Close**: Add validation evidence (e.g. test outputs) to `tasks.md`. Mark task `Done`. Update `progress.md` with session notes.
9. **Next Step**: If tasks remain, continue `/spec-implement`. If complete, hand off to `/harness-verify`. If issues arise (scope break, planning gaps), stop and route to `/spec-plan`.

## Stop Conditions

- `spec.md`, `plan.md`, or `tasks.md` is missing.
- Unresolved dependencies or design contradictions.

## Preconditions

- **Required Phase**: `Plan Approved` in `status.md`.
- **Phase sets**: `Implementing` (ongoing). Completion is set by `/harness-verify`.

## Core Rules

- **No "Vibe Coding"**: Stick strictly to task scopes.
- **Exact Task ID**: Work and log using explicit task IDs (e.g. `T-01`).
- **Baseline Proving**: Always execute the proving command *before* editing files.
- **Decision Provenance**: If you make a non-trivial execution decision mid-flight (e.g., swapping a library, deviating from `plan.md`), you MUST append a `## Decision Record` block to `progress.md` detailing the choice, reason, and spec alignment *before* writing the code.
- **No Swallowing Errors**: Follow backend/frontend coding policies.
- **Stop at Scope Breaks**: If a requirement is missing or contradictory, return to `/spec-plan` rather than work-around coding.

## Common Rationalizations

| Rationalization | Reality |
|---|---|
| "The task is vague, I'll fill it in." | Silent scope-filling creates drift. Return to planning. |
| "I'll update tasks on completion." | State must reflect reality mid-session. |
| "Skip tests now, let verify handle it." | Implementation owns writing the tests if required by the plan. |

## Red Flags

- No baseline proving command executed before file edits.
- Task marked `Done` while verification is still failing.
- Changing locked decisions from `spec.md` without re-spec'ing.

## Verification

- [ ] Code edits strictly bounded by the selected task.
- [ ] Proving commands run and outputs recorded in `tasks.md`.
- [ ] Coding contract constraints and decisions followed.

## Output Rules

- Modify only target source code, tests, `tasks.md`, `progress.md`, and `status.md`.
- Do not bypass verification checks.
