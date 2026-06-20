---
name: spec-adr
description: Create or evaluate an architecture decision record (ADR). Use when choosing between technologies, documenting design trade-offs, or reviewing system proposals. This skill ensures decisions are recorded with context, trade-offs, and long-term consequences.

---

# Kit ADR

## Overview
Record significant architectural decisions.
## When to Use
- **Technology Choices:** Choosing between Kafka vs SQS, React vs Angular, etc.
- **Design Trade-offs:** Documenting why a specific architectural pattern was chosen over another.
- **System Proposals:** Reviewing and refining new component designs.
- **Refactoring Decisions:** Documenting major structural changes and their rationale.
## I/O Hand-off Protocol
- **Reads**: Codebase context, `kit/docs/rules/ponytail.md`.
- **Writes**: `docs/project/architecture.md` (append ADR).
- **Next Skill**: Return to previous skill (e.g., `/spec-plan` or `/spec-implement`).

## Workflow
1. Identify the decision to be made.
2. Consider context, options, and consequences.
3. Append the decision to `docs/project/architecture.md` using `references/adr-template.md`.

## Core Rules
- **Comparative Analysis:** Always include at least two options with pros and cons.
- **Traceability:** Link ADRs to `spec.md` when writing during the spec phase. Link to `design.md` only when the planning phase has completed and `design.md` exists.
- **Immutability:** Once "Accepted," ADRs should be superseded or deprecated, not deleted or significantly altered.
- **Surgical Scope:** Focus on the architectural decision, not the implementation details.
