---
name: spec-plan
description: Design the technical solution and sequence execution. Handles architectural design, implementation planning, task breakdown, and automated traceability from requirements to tasks.
---

# Kit Plan

## Overview
Converts an approved spec into a concrete execution strategy. Produces `plan.md` (which explicitly defines the Technical Design first) and `tasks.md` in `artifacts/features/<slug>/`. Tasks are derived from the design portion of the plan. It answers: how will we build this safely, and what task does implementation start with?

## I/O Hand-off Protocol
- **Reads**: `artifacts/features/<slug>/spec.md`, `memories/repo/harness-telemetry.md`, `docs/rules/ponytail.md`.
- **Writes**: `artifacts/features/<slug>/plan.md`, `artifacts/features/<slug>/tasks.md`, `artifacts/features/<slug>/status.md`.
- **Next Skill**: `/spec-implement`

## Workflow
1. **Initialize State**: Update the `## Current Phase` section of `artifacts/features/<slug>/status.md` to set phase to `Planning`.
2. **Design First**: You MUST write `artifacts/features/<slug>/plan.md` using `references/plan-template.md`. You must complete **Part 1: Technical Design** before defining execution phases or tasks. Read the `## Complexity` from `status.md` and choose depth for the Technical Design section:
   - **Simple**: fill only the Lightweight Design section.
   - **Moderate**: fill the Comprehensive Design section.
   - **Complex**: fill the Comprehensive Design section. If uncertainties remain, halt and invoke `/spec-research`.
   If the design reveals a contested decision with ≥2 viable approaches and material tradeoffs (e.g., build vs. buy, sync vs. async, new dependency vs. in-house), STOP. Invoke `/spec-adr` to record the decision before proceeding. Do not silently pick an approach.
   The delivery strategy (Part 2 of the plan) must pass the **Architectural Gates** (see Core Rules) and conform to `ponytail.md` guidelines.
3. **Task Breakdown**: Create `artifacts/features/<slug>/tasks.md` using `references/tasks-template.md` by breaking down the technical approach from the `plan.md`. Each task MUST be traceable to a design decision or component defined in the Technical Design. Use unique task IDs (`TASK-001`), clear targets, and specific proof validations. Mark independent, non-blocking tasks with `[P]` to indicate safe parallel execution zones.
4. **Traceability**: Verify every requirement in `artifacts/features/<slug>/spec.md` maps to a task in `artifacts/features/<slug>/tasks.md`.
5. **Readiness & Handoff**: Run a completeness check using `references/definition-of-ready.md` to ensure the plan and tasks meet all preconditions. Run `bash scripts/harness/phase-gate.sh <slug> "Plan Approved"` to verify preconditions. If it fails, fix the root cause before proceeding. Set `artifacts/features/<slug>/status.md` to `Plan Approved` and route to `/spec-implement`.

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
