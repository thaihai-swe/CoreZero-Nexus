---
name: spec-requirements
description: Define the requirements and acceptance criteria for a feature.
compatibility: Designed for AI coding agents.
---

# Kit Spec

## Overview
Define the "What & Why" of a feature. Aligns the team on what is being built and how it will be verified.

## I/O Hand-off Protocol
- **Reads**: `artifacts/features/<slug>/analysis.md` (if exists), `artifacts/features/<slug>/status.md`.
- **Writes**: `artifacts/features/<slug>/spec.md`, `artifacts/features/<slug>/status.md`.
- **Next Skill**: `/spec-plan`

## Workflow
1. **Initialize State**: Update the `## Current State` section of `artifacts/features/<slug>/status.md` to set phase to `Spec'ing`.
1.5 **Domain Pack Scan**: For each installed pack listed in `MASTER_INDEX.md` `## By Domain Packs`, read `memories/domain/<name>/glossary.md` frontmatter `triggers:`. If any trigger keyword appears in the user's task description or proposal, note the matched pack name in `status.md` under `## Loaded Domain Packs`. Load that pack's `glossary.md` now. Do this before drafting the spec.
2. **Clarify**: Do NOT guess missing details. If there is ambiguity (e.g., auth method, data source), insert explicit `[NEEDS CLARIFICATION: <specific question>]` tags directly into the spec draft.
3. **Authoring**: Draft `artifacts/features/<slug>/spec.md` using `references/spec-template.md`. Define testable acceptance criteria (AC) using either strict markdown checklists (`- [ ]`) or Gherkin syntax (`Given/When/Then`).
4. **Scope Cut**: Explicitly list In Scope, Out Of Scope, and Non-Goals.
4.5 **ADR Conflict Check**: Load `memories/repo/adr-log.md`. For each locked ADR that intersects with the feature's domain or target files, verify the proposed spec does not contradict the locked decision. If a contradiction exists, insert `[ADR CONFLICT: ADR-NNN — <decision summary>]` into the spec draft and block Handoff until the conflict is resolved with the user.
5. **Completeness Check**: Ensure NO `[NEEDS CLARIFICATION]` tags or `[ADR CONFLICT]` blocks remain before proceeding. Ask the user to resolve any remaining tags.
6. **Handoff**: Update the `## Current State` section of `artifacts/features/<slug>/status.md` to `Spec Approved` and route to `/spec-plan`.

## Core Rules
- **Anti-Hallucination**: Never invent plausible but unspecified business logic. Mark all unknowns explicitly.
- **What, not How**: Focus on requirements, not technical implementation.
- **Validation-Aware**: Every acceptance criterion must be testable.
- **Deterministic ACs**: ACs must be binary (pass/fail) and clearly mapped to a verification command or script.
