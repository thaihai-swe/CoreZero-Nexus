# CoreZero Nexus Constitution

Version: 1.1.0 | Last amended: 2026-06-04

## Purpose

This file stores the durable normative rules for maintaining the AI Agents Development Kit. Rules here are repo-wide, evidence-backed, and mandatory. Descriptive patterns and implementation facts belong in `memories/repo/project-knowledge-base.md`.

## Normative Rules

### CC-001 — Skill contracts are the single source of truth
`skills/*/SKILL.md` owns all workflow behavior. Do not duplicate full skill bodies elsewhere. When a skill contract changes, update relevant docs in the same wave.

### CC-002 — Completion requires fresh evidence
Do not mark kit work complete from a plausible diff alone. A passing verification command or observable side effect is required. Stale evidence is not evidence.

### CC-003 — Unknown stays unknown
When information is unavailable, agents MUST mark it explicitly as `[UNKNOWN]`. Never fill gaps with plausible-sounding guesses. This applies to all artifacts: specs, plans, reviews, and memory files.

### CC-004 — Permission boundaries must be explicit
Security-sensitive harness rules belong in `memories/repo/security-policy.md`. Do not scatter trust-boundary decisions across skill files or the knowledge base.

### CC-005 — Prefer surgical updates
Change only what is required by the stated task. No drive-by refactors, formatting churn, or unrelated cleanup. Touch only the files the task needs.

### CC-006 — Spec is the source of truth for feature behavior
The `spec.md` artifact defines what is being built and why. If implementation diverges from spec, one of them must be corrected before verification passes. Resolving divergence in chat history is not sufficient.

### CC-007 — Workflow and documentation must stay aligned
When a public command, artifact contract, or skill workflow changes, update `docs/`, `documents/`, and any generated references in the same change. Documentation drift is a real defect.

### CC-008 — Session handoff is mandatory for long work sessions
`context-session END` and `handoff.md` generation are required before closing any long kit work session. Chat history is volatile; handoff artifacts are the system of record.

### CC-009 — Memory promotion requires evidence at promotion time
Promote only what the repository or artifacts already support. Speculative rules and unverified observations do not belong in instruction-tier memory.

### CC-010 — Domain specs are descriptive; the constitution is normative
Domain specs (under `specs/`) describe current subsystem behavior. The constitution enforces repo-wide mandates. Do not put repo-wide rules in domain specs or project facts in the constitution.

## Release Guardrails

- Treat missing fixtures, missing docs, or stale command tables as real regressions.
- Any change to the public installed surface (`docs/`, `skills/`, `scripts/`) must be reflected in `manifest.json` and verified by a dry-run install before shipping.

## Amendment Rules

- Amend only when the rule is repo-wide, durable, and evidence-based.
- Prefer refining existing CC-* rules over adding new ones.
- Preserve stable CC-* identifiers across amendments.
- Version bump this file when any rule changes. Minor bump for refinements; major bump for new or removed rules.
- Route descriptive knowledge to `project-knowledge-base.md` instead.
