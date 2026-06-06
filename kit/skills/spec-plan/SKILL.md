---
name: spec-plan
description: Design the technical solution and sequence execution. Handles architectural design, implementation planning, task breakdown, and automated traceability from requirements to tasks.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in spec-driven repositories that use memories/repo/ and artifacts/features/<slug>/.

---

# Kit Plan


## Overview

Converts an approved spec into a concrete execution strategy. Creates `plan.md`, `tasks.md`, and optionally `design.md` in `artifacts/features/<slug>/`. It answers: how will we build this safely, and what task does implementation start with?

## Read First

- `artifacts/features/<slug>/status.md` (must be `Spec Approved`)
- `spec.md` and `requirements-review.md`
- `memories/repo/constitution.md` (design constraints) and `security-policy.md` (threat boundaries)
- `memories/repo/harness-config.md` (verification commands)
- References: `references/design-template.md`, `references/plan-template.md`, `references/tasks-template.md`, `../_shared/rigor-profiles.md`, and `../_shared/status-phases.md`.

## When to Use

- Translate an approved `spec.md` into execution tasks.
- Map requirements and acceptance criteria to task steps.
- Resolve technical ambiguity or design trade-offs.

## Workflow

1. **Initialization**: Update `status.md` phase to `Planning`.
2. **Profile Load**: Load active rigor profile.
3. **Rigor Triage**: Set planning depth per profile:
   - `Tiny`: Lean `plan.md` with inlined tasks (3 or fewer). No `design.md`.
   - `Standard`: Full `plan.md` with: (a) impacted files list, (b) explicit execution order, (c) rollback strategy, (d) mechanical verification gate commands. `tasks.md` required. `design.md` only when technical ambiguity remains after reading `spec.md`.
   - `Complex`: Full design (`design.md`), dependency tracking, and phased rollout. Diagram via `/visualize` is optional if it involves boundaries.
4. **Load Decisions**: Import locked decisions from `spec.md` as constraints.
5. **Design (Profile-Driven)**: Build `design.md` to resolve technical tradeoffs.
   - `Complex` profile: Required.
   - `Standard` profile: Only when technical ambiguity remains after reading `spec.md`.
   - `Tiny` profile: Skipped. The profile determines this, not agent judgment.
6. **Plan Authoring**: Write `plan.md` defining impacted areas, execution order, rollback steps, and verification strategies.
   **Rollback strategy (required)**: `plan.md` must include a `## Rollback Strategy` section with:
   - Rollback command or steps (must be executable)
   - Scope of change affected
   - Estimated recovery time
   If the change is irreversible by design (e.g., schema migration), document that explicitly and add a compensating forward-fix procedure.
7. **Mechanical Gate**: Add a `## Mechanical Verification Gate` section with runnable test/lint bash commands.
8. **Task Decomposition**: Create `tasks.md` with unique task IDs (`T-01`), clear targets, and specific proof validations.
   Each task in `tasks.md` must include a `depends_on: [T-XX, T-XX]` field (empty `[]` for tasks with no dependencies). The "first unblocked task" in `/spec-implement` is defined as: the lowest-numbered task whose `depends_on` list is either empty or entirely `Done`.
9. **Traceability**: Verify `REQ -> AC -> TASK -> validation` mappings are complete.
10. **Handoff**: Set `status.md` to `Plan Approved` and name `/spec-implement` as the next core command.

## Stop Conditions

- `status.md` phase is not `Spec Approved` or `spec.md` is missing.
- Preconditions fail. (Route back to `/spec-requirements`).

## Preconditions

- **Required Phase**: `Spec Approved` in `status.md`.
- **Required Artifacts**: `spec.md`, `requirements-review.md` (must be `ready`).

## Core Rules

- **Verifiable Task Increments**: Break work into low-risk tasks that can be proven independently.
- **Rigor Proportionality**: Do not wrap minor changes in complex design ceremony.
- **No Spec Re-opening**: Stick to the approved requirements.
- **Validation-First**: Every task must end with a clear proving command.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "The developer will figure out approach." | Planning must remove core approach and sequencing ambiguity. |
| "Add test details during coding." | Validation design belongs in the plan. |
| "List 'Fix Bug X' as one task." | Decompose vague tasks: Reproduce -> Instrument -> Fix -> Verify. |

## Red Flags

- Plan is a vague brainstorm without structured execution steps.
- Implementation tasks lack concrete validation/proving commands.
- `design.md` created out of habit for trivial changes.

## Verification

- [ ] Every requirement/AC maps to a task and validation proof.
- [ ] First unblocked task is immediately executable from `tasks.md`.
- [ ] Planning depth matches the active profile.
- [ ] Mechanical gate commands are validated and runnable.

## Output Rules

- Update only: `design.md`, `plan.md`, `tasks.md`, `status.md`.
- Do not modify `spec.md`. Do not write code.
