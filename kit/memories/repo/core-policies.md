# Core Policies (Constitution & Config)

# CoreZero Nexus Constitution

Version: 1.2.0 | Last amended: 2026-06-17

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
The canonical domain spec contract lives in `memories/domain/spec.md`. Do not put repo-wide normative rules in domain specs or project facts in the constitution.

## Release Guardrails

- Treat missing fixtures, missing docs, or stale command tables as real regressions.
- Any change to the public installed surface (`docs/`, `skills/`, `scripts/`) must be reflected in `manifest.json` and verified by a dry-run install before shipping.

## Amendment Rules

- Amend only when the rule is repo-wide, durable, and evidence-based.
- Prefer refining existing CC-* rules over adding new ones.
- Preserve stable CC-* identifiers across amendments.
- Version bump this file when any rule changes. Minor bump for refinements; major bump for new or removed rules.
- Route descriptive knowledge to `project-knowledge-base.md` instead.


# Harness Config

## Repository Identity

- Project name: AI Agents Development Kit (CoreZero Nexus)
- Repository type: Harness Engineering kit (template/starter kit)
- Primary code roots: `skills/`, `scripts/`, `memories/repo/`
- Default working branch: main
- Supported agent clients: Claude Code, Cursor, Codex, Gemini CLI

## Work Tracking

- Issue tracker mode: GitHub
- Issue/project location: https://github.com/thaihai-swe/CoreZero-Nexus/issues
- Default work item format: GitHub Issues
- Required labels or states: `breaking-change` for skill name or artifact schema changes
- Escalation / blocker handling: Stop and ask user

## Artifact Routing

- Feature artifact root: `artifacts/features/<slug>/`
- Docs root: `docs/`
- Architecture doc path: `docs/project/architecture.md`
- Security policy path: `memories/repo/security-policy.md`
- Learned heuristics path: `memories/repo/learned-heuristics.md`
- ADR location: `artifacts/features/<slug>/adr-*.md`
- Generated documentation location: `docs/generated/`
- Codemap path: `docs/generated/codemap.md`
- References index path: `docs/generated/references-index.md`

## Verification Commands

- Install / bootstrap command: `bash scripts/install.sh /path/to/target`
- Lint / format command: N/A (documentation-first repo)
- Typecheck command: N/A
- Build command: N/A

## Session Defaults

- Session bootstrap skill: `/starter-init`
- Progress log path: `artifacts/features/<slug>/progress.md`
- Handoff path: `artifacts/features/<slug>/handoff.md`
- When to checkpoint: After completing a skill or major edit wave
- Context compaction triggers: Raw grep output, large file listings, superseded design detail
- Stale-context eviction rules: Summarize raw tool output after extracting findings
- When to stop and escalate: After two failed corrections on the same issue

## Environment And Access

- Required local services: None
- Required env files or secrets handling: None
- Sandbox / permission watchouts: Do not modify target project files outside bootstrap
- Browser / UI verification target: N/A

## Conventions That Affect Automation

- Feature slug format: kebab-case
- Branch naming format: features/<name>
- Commit / PR expectations: Subject under 72 chars, body explains why
- Required reviewers or owners: None (solo maintainer)

## Adaptive Rigor

- **Default profile:** Standard
- **Rules:** Canonical selection, promotion, and demotion rules are defined in `skills/_shared/rigor-profiles.md`. Refer to it before editing code.

## Memory Promotion Thresholds

Used by `context-memory` post-ship sync to propose memory restructuring when thresholds are exceeded.
- File length: warn at 800 lines, hard threshold at 1200 lines
- Distinct subtopics: 3 or more H2 sections covering separable concerns
- Artifact references: 5 or more `artifacts/features/<slug>/` files cite the same slice of one memory file
- Action when threshold hit: add the file to `## Promotion Watchlist` in `memories/repo/INDEX.md` and write a one-paragraph proposal to `artifacts/features/<slug>/promotions.md`
- Tier definitions and promotion loop: `skills/context-memory/SKILL.md` `## Memory Tiers`

