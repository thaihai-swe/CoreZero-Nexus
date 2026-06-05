# Project Knowledge Base

## Purpose

Describe what stable repository knowledge this file stores and how agents should use it alongside `memories/repo/constitution.md`.

This file is not general documentation. It is durable agent memory.

When durable system structure becomes too large for this file, summarize it here and point to `docs/architecture.md`.

Use it to store:

- stable repository facts
- reusable implementation patterns
- decision heuristics that apply across many features
- durable brownfield watchouts
- durable project-level continuity notes that matter across multiple features

Do not use it for:

- feature-specific analysis
- temporary implementation notes
- one-off debugging sessions
- speculative future design with no repository basis

## How Agents Use This File

- Read before writing `spec.md`, `plan.md`, or `tasks.md`.
- Apply only when relevant to the current task.
- If a fact here conflicts with `memories/repo/constitution.md`, the constitution wins.

## Source Of Truth Map

- Domain or concern:
  Source of truth:
  Why it matters:

## Stable Invariants

Facts/constraints expected to hold across many features.

- Invariant:
  Why it matters:
  Confidence: High | Medium | Low
  Provenance: Observed in repo | Team convention

## AI Coding Contract

Descriptive side of the coding contract. Normative mandates → `constitution.md`.

### Tech Stack Snapshot

- Language/runtime + version:
- Primary frameworks/libraries:
- Storage/infrastructure:
- Validation/tooling:

### Naming And File Conventions

- Files and directories:
- Variables/functions:
- Types/classes/interfaces:
- Constants/config keys:

### Implementation Patterns

- Architectural pattern (use when):
- Error-handling pattern (use when):
- Validation/testing pattern (use when):
- Async/concurrency pattern (use when):

### AI-Followable Rules

- Rule:
  Why it exists:
  Applies to:
  Example or reference:

## Decision Heuristics

Repeatable rules for picking among implementation options.

- Heuristic:
  Use when:
  Avoid when:
  Why it helps:

## Known Good Patterns

Reference implementations worth copying.

- Pattern:
  Use when:
  Reference:
  Notes:

## Anti-Patterns And Forbidden Moves

- Anti-pattern:
  Why harmful:
  Safer alternative:

## Boundaries And Ownership

Concise — full structural maps belong in `docs/architecture.md`.

- Boundary:
  Owned by:
  Why it matters:
  Integration note:
  Related architecture section:

## Shared Dependencies And Infrastructure

- Dependency or platform:
  Why it matters:
  Watchout:

## Project Continuity

Cross-feature context durable enough to matter beyond one artifact set, not normative enough for the constitution.

- Active priority:
  Why it matters across features:
  Confidence:
  Provenance:

- Repo-wide watchout:
  Why it matters across features:
  Confidence:
  Provenance:

## Project Dictionary / Shared Language

Capture the project-specific vocabulary to ensure the agent uses the same language as the domain experts and code. This prevents naming collisions and reduces token usage by establishing a common ground.

- **Term:** [The exact term used in code/docs]
  - **Definition:** [What it means in this project]
  - **Context/Usage:** [Where it appears, e.g., "Used in auth middleware", "Refers to the DynamoDB partition key"]
  - **Aliases:** [Other names this might be called by users or in old code]

## Maintenance Metadata

- Last major refresh:
- Triggers a refresh:
- Doesn't belong here:

## Promotion Rules

- Belongs here:
- Stays in feature artifacts (`artifacts/features/<slug>/`):
- Goes to `constitution.md` instead:
- When durable enough to promote:
- How to record confidence/provenance with partial evidence:
