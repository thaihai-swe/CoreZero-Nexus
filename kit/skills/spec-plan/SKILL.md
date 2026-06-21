---
name: spec-plan
description: Design the technical solution and sequence execution. Handles architectural design, implementation planning, task breakdown, and automated traceability from requirements to tasks.
---

# Kit Plan

## Overview
Converts an approved spec into a concrete execution strategy. Always produces `design.md` first, then `plan.md` and `tasks.md` in `artifacts/features/<slug>/`. Tasks are derived from the design, not the other way around. It answers: how will we build this safely, and what task does implementation start with?

## I/O Hand-off Protocol
- **Reads**: `artifacts/features/<slug>/spec.md`, `memories/repo/harness-telemetry.md`, `kit/docs/rules/ponytail.md`.
- **Writes**: `artifacts/features/<slug>/design.md`, `artifacts/features/<slug>/plan.md`, `artifacts/features/<slug>/tasks.md`, `artifacts/features/<slug>/status.md`.
- **Next Skill**: `/spec-implement`

## Workflow
1. **Initialize State**: Update the `## Current Phase` section of `artifacts/features/<slug>/status.md` to set phase to `Planning`.
2. **Design First**: You MUST write `artifacts/features/<slug>/design.md` using `references/design-template.md` before breaking down any tasks. Read the `## Complexity` from `status.md` and choose depth:
   - **Simple**: fill only the Lightweight section of the template.
   - **Moderate**: fill the Comprehensive section.
   - **Complex**: fill the Comprehensive section. If uncertainties remain, halt and invoke `/spec-research`.
   If the design reveals a contested decision with ≥2 viable approaches and material tradeoffs (e.g., build vs. buy, sync vs. async, new dependency vs. in-house), STOP. Invoke `/spec-adr` to record the decision before proceeding. Do not silently pick an approach.
   Once `design.md` is written, write `artifacts/features/<slug>/plan.md` using `references/plan-template.md` deriving the execution approach directly from the design. The plan must pass the **Architectural Gates** (see Core Rules) and conform to `ponytail.md` guidelines or explicitly document justified exceptions in a "Complexity Tracking" section.
3. **Task Breakdown**: Create `artifacts/features/<slug>/tasks.md` using `references/tasks-template.md` by breaking down the technical approach from `design.md`. Each task MUST be traceable to a design decision or component defined in `design.md`. Use unique task IDs (`T-01`), clear targets, and specific proof validations. Mark independent, non-blocking tasks with `[P]` to indicate safe parallel execution zones.
4. **Traceability**: Verify every requirement in `artifacts/features/<slug>/spec.md` maps to a task in `artifacts/features/<slug>/tasks.md`.
5. **Readiness & Handoff**: Run a completeness check using `references/definition-of-ready.md` to ensure the plan and tasks meet all preconditions. Set `artifacts/features/<slug>/status.md` to `Plan Approved` and route to `/spec-implement`.

## Core Rules
- **Hierarchical Detail Management**: Keep `plan.md` high-level and readable. Do NOT dump raw code or algorithms into the plan; extract those to separate implementation detail files if necessary.
- **Architectural Gates**:
  - **Simplicity Gate**: No speculative future-proofing. Build only what satisfies the exact requirements.
  - **Anti-Abstraction Gate**: Use framework features directly. Avoid creating custom wrappers or premature abstractions.
- **Verifiable Task Increments**: Break work into low-risk tasks that can be proven independently.
- **No Spec Re-opening**: Stick to the approved requirements.
- **Spec Amendment Protocol**: If `spec.md` is amended after `plan.md` has been approved, the agent MUST:
  1. Add a `[STALE — spec amended <date>]` header to the top of `plan.md` and `tasks.md`.
  2. Set `status.md` phase back to `Planning`.
  3. Re-run Steps 2–4 (Design, Task Breakdown, Traceability) before any implementation task resumes.
  Implementation MUST NOT continue against a stale plan.
- **Context Eviction**: After drafting the plan, you MUST summarize any raw architectural logs and evict them from your context window before handing off to `/spec-implement`.
