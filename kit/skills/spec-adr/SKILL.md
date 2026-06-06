---
name: spec-adr
description: Create or evaluate an architecture decision record (ADR). Use when choosing between technologies, documenting design trade-offs, or reviewing system proposals. This skill ensures decisions are recorded with context, trade-offs, and long-term consequences.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in spec-driven repositories.

---

# Kit ADR



## Overview
This skill manages the creation, evaluation, and logging of Architecture Decision Records (ADRs). It ensures that technical decisions are not just made, but documented with their full context and trade-offs for future maintainers. It is a helper path for durable decision capture, not a default step in every feature flow.

**Non-Goals:**
- This is not a replacement for `spec-plan` (implementation strategy).
- This is not for recording meeting minutes or general project notes.

## When to Use
- **Technology Choices:** Choosing between Kafka vs SQS, React vs Angular, etc.
- **Design Trade-offs:** Documenting why a specific architectural pattern was chosen over another.
- **System Proposals:** Reviewing and refining new component designs.
- **Refactoring Decisions:** Documenting major structural changes and their rationale.

**Routing:**
- For implementation steps and task breakdown, use `/spec-plan`.
- For low-level code implementation, use `/spec-implement`.
- Use this skill when a core flow step encounters a real architecture trade-off that should outlive the feature.

## Read First
- `artifacts/features/<slug>/status.md`
- `artifacts/features/<slug>/adr-*.md`
- `memories/repo/adr-log.md`
- `skills/spec-adr/references/adr-template.md`
- `memories/repo/constitution.md` — ADRs must not contradict existing normative rules
- `memories/repo/security-policy.md` — ADRs touching auth, data, or network boundaries must reference security constraints

## Workflow
0. **Claim Check**: Check `artifacts/features/<slug>/claim.md`. Follow the same claim-check protocol as `spec-research` Step 0.
1. **Context Check:** Read `status.md` to identify the current phase and any blockers related to the decision.
2. **Profile Load**: Read the active rigor profile.
   - `Tiny` profile: Check if the decision is non-obvious. If obvious (only one viable option, no tradeoffs), skip the ADR — record a one-line note in `progress.md` and stop.
   - `Standard` profile: Proceed only for non-obvious technical choices.
   - `Complex` profile: Required for each locked technical choice. Proceed always.
3. **Gather Context:** Identify the problem, constraints, and forces at play.
4. **Identify Options:** List at least two viable alternatives.
5. **Comparative Analysis:** Evaluate each option against at minimum: Complexity, Cost, Scalability, Team Familiarity. Add domain-specific dimensions as relevant (e.g., Compliance, Latency, Vendor Lock-In, Reversibility). Do not restrict analysis to only the default four if the decision domain requires others.
6. **Draft ADR:** Use `adr-template.md` to document the decision, trade-offs, and consequences.
7. **Update Log:** Append the new ADR reference to `memories/repo/adr-log.md`.
8. **Finalization:** Update `status.md`. If this ADR was a blocker, mark it as resolved.

### Superseding an Existing ADR

When an accepted ADR needs to be replaced:
1. Draft the new ADR normally (steps 0–8).
2. In the new ADR's `## Status` field, write: `Accepted — supersedes ADR-NNN`.
3. In the old ADR's `## Status` field, write: `Superseded by ADR-MMM`.
4. Append both the new and updated old ADR references to `adr-log.md`.
Do not delete or alter the old ADR's decision or rationale — only update its status.

## Stop Conditions

- Required constraints (e.g., budget, RPS, deadline) are missing or ambiguous.
- No viable alternatives are considered (avoid "the only way" thinking).
- The decision requires input from a stakeholder who hasn't been consulted.

## Core Rules
- **Comparative Analysis:** Always include at least two options with pros and cons.
- **Traceability:** Link ADRs to `spec.md` when writing during the spec phase. Link to `design.md` only when the planning phase has completed and `design.md` exists.
- **Immutability:** Once "Accepted," ADRs should be superseded or deprecated, not deleted or significantly altered.
- **Surgical Scope:** Focus on the architectural decision, not the implementation details.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "It's too small for an ADR." | Small decisions compound into big technical debt. |
| "Everyone agreed in chat, no need to document." | Chat logs are not architectural history. New team members shouldn't have to search Slack to understand why a choice was made. |
| "I'll write the ADR after I'm done with the implementation." | Post-hoc documentation often omits the alternatives considered and the 'why' behind the chosen path. |

## Red Flags

- The ADR lacks a "Consequences" section (everything has a cost).
- "Team Familiarity" is the only reason for a decision.
- The "Context" section is too vague to understand the original problem.

## Verification

- Verify that at least two options were assessed.
- Ensure "Consequences" (both positive and negative) are explicitly listed.
- Confirm the ADR is added to the central `adr-log.md`.

## Output Rules

- Update or create `artifacts/features/<slug>/adr-[number].md`.
- Update `memories/repo/adr-log.md`.
- Do not modify `spec.md` or `plan.md` (only link to them).

**ADR Numbering**: Assign the ADR number by counting existing entries in `memories/repo/adr-log.md` and adding 1. Format: `adr-NNN.md` (zero-padded to 3 digits). Example: if `adr-log.md` has 4 entries, the next ADR is `adr-005.md`.

`spec-adr` is the **write owner** of `memories/repo/adr-log.md`. It is the only skill that appends entries. `/context-memory` reads `adr-log.md` for architecture drift detection but does not append entries.
