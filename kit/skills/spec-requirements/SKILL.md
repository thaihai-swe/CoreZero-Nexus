---
name: spec-requirements

description: Define the "What & Why" of a feature. Handles specification authoring, Socratic refinement to resolve ambiguity, and a built-in readiness review to ensure requirements are testable and complete before planning.
---

# Kit Spec
## Routing Guide

- **Use `/spec-requirements`** to define requirements and acceptance criteria.
- **Use `/spec-research`** first if the problem space, bug root cause, or brownfield codebase state is unknown.
## Overview
Create or refine `status.md`, `proposal.md`, `spec.md`, and `requirements-review.md` in `artifacts/features/<slug>/`. This skill aligns the team on what is being built and how it will be verified.
## I/O Hand-off Protocol
- **Reads**: `artifacts/features/<slug>/analysis.md` (if exists), `artifacts/features/<slug>/status.md`, `memories/repo/adr-log.md`, domain packs.
- **Writes**: `artifacts/features/<slug>/spec.md`, `artifacts/features/<slug>/status.md`, `artifacts/features/<slug>/proposal.md`, `artifacts/features/<slug>/requirements-review.md`.
- **Next Skill**: `/spec-plan`

## When to Use

- Define a new feature, change request, or initiative.
- Refine existing specifications.
- Resolve ambiguity before design/planning.

## Workflow

1. **Initialization**: Create `status.md` if missing (from `references/status-template.md`). Set phase to `Spec'ing`. Load active rigor profile from `status.md` or fallback to `memories/repo/harness-config.md`.
2. **Intake & Routing**: Classify input type (`new_spec`, `spec_slice`, `change_request`, `new_initiative`, `maintenance`, `harness_improvement`) and risk flags in `status.md`. Determine lane (Tiny/Standard/Complex) per `references/intake.md`. Promote rigor profile if security/migration/auth/harness-maintain flags exist.
    - **System Spec Mode**: If the request is cross-cutting or system-wide, switch to System Spec Mode. Output target becomes `docs/system-specs/<name>.md`.
3. **Context Alignment**: 
    - **Domain Pack Scan**: Read `memories/domain/<name>/glossary.md` frontmatter `triggers:`. If matched, note in `status.md` and load that pack's `glossary.md`.
    - **Analysis Check**: Read `artifacts/features/<slug>/analysis.md` (if exists) and record open research questions.
    - **Domain Spec Check**: Read relevant domain specs (e.g., `memories/repo/domain-specs.md`).
    - **ADR Conflict Check**: Load `memories/repo/adr-log.md`. Verify the proposed spec does not contradict locked decisions. If a contradiction exists, insert `[ADR CONFLICT: ADR-NNN — <decision summary>]` and block Handoff.
4. **Clarification (Grilling Phase)**: Do NOT guess missing details. Engage in Socratic refinement using `[NEEDS CLARIFICATION: <specific question>]` tags. Ask batch clarifying questions with recommended answers (1-2 for Tiny, 3-5 for Standard, 5+ for Complex) per `references/grilling-waves.md`. If answers remain contradictory after 2 rounds, write `[UNRESOLVED: <description>]` and stop.
5. **Proposal & Scope Definition**: Draft `proposal.md` for `Standard`/`Complex` to align scope before spec'ing. (For `Tiny`, embed in the spec). Explicitly list `In Scope`, `Out Of Scope`, and `Non-Goals`.
6. **Spec Authoring**: Draft `spec.md` (`what` & `why`) using `references/spec-template.md`. Record key gray-area design/UX choices. Define testable, observable acceptance criteria (AC-*) using strict markdown checklists or Gherkin. Specify verification surfaces (unit, integration, manual check).
7. **Completeness Check**: Ensure NO `[NEEDS CLARIFICATION]`, `[UNRESOLVED]`, or `[ADR CONFLICT]` tags remain. For `Standard`/`Complex`, create and pass `requirements-review.md`.
8. **Handoff**: Update `status.md` phase to `Spec Approved` and route to `/spec-plan`.

## Core Rules
- **Anti-Hallucination**: Never invent plausible but unspecified business logic. Mark all unknowns explicitly.
- **What, not How**: Focus on requirements, not technical implementation.
- **Validation-Aware**: Every acceptance criterion must be testable.
- **Deterministic ACs**: ACs must be binary (pass/fail) and clearly mapped to a verification command or script.
