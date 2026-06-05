---
name: harness-maintain
description: Evaluate, construct, or repair an agent harness across six core subsystems (Instructions, State, Verification, Scope, Lifecycle, Security), including evaluation architecture and failure-driven improvement from observability findings.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in any codebase.

---

# Harness Maintain



## Overview

Meta-skill for harness engineering. It evaluates or repairs the harness environment itself. Four modes:
1. **Assess Mode**: Score the repository against the 6 harness subsystems.
2. **Create Mode**: Generate a harness from scratch for a new project.
3. **Improve Mode**: Apply fixes to a harness based on failure evidence or logs.
4. **Eval Mode**: Run split evaluator passes over a feature execution flow.

## Read First

- `AGENTS.md` and `memories/repo/harness-config.md`
- `memories/repo/constitution.md` and `memories/repo/security-policy.md`
- `memories/repo/project-knowledge-base.md` and `memories/repo/observability-log.md`
- `docs/generated/codemap.md` and `docs/generated/references-index.md`
- References in `skills/harness-maintain/references/`.

## When to Use

- Evolve the harness environment or evaluate failures.
- Bootstrap agent infrastructure for a new repository.
- Repair a failing subsystem triggered by observability logs or verification failures.

## Workflow

### Assess Mode
1. Read project structures, memory files, and feature artifacts.
2. Score (1-5) against the 6 subsystems (Instructions, State, Verification, Scope, Lifecycle, Security) using `references/assessment-rubric.md`.
3. Check `session-extracts.md` for active features. If pending candidates exceed 5, flag in the State score.
4. Generate `artifacts/features/<slug>/harness-assessment.md`.

### Create Mode
1. Run `starter-init` bootstrap.
2. Build `constitution.md`, `security-policy.md`, `project-knowledge-base.md`, and `learned-heuristics.md`.
3. Create `codemap.md` and `references-index.md` for non-trivial repositories.

### Improve Mode
1. Check failure reports or `observability-log.md`.
2. Classify: **Harness** (environment caused error), **Model** (poor execution), or **Spec** (contradictory contract).
3. If harness issue, design fix for one subsystem. Record in `observability-log.md` and `learned-heuristics.md`. Route rule changes to `/context-memory`.

### Eval Mode
1. Run evaluations per `references/eval-modes.md` (Mechanical, Alignment, Adversarial/Security, Continuity).
2. Write findings to `artifacts/features/<slug>/eval-report.md`. Route outcomes to owning skills.

## Stop Conditions

- Attempting to use this skill to write feature code. (This skill only writes infrastructure/docs).
- The failure is a feature defect with no harness lesson. Route to implementation instead.

## Core Rules

- **Subsystems First**: Limit analysis to the 6 subsystems.
- **Durable Fixes**: Address structural environment issues, not prompt wording.
- **Failure-Driven**: Investigate environment gaps before blaming model capabilities.
- **Security is Design**: FS, network, and secret boundaries are core harness requirements.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "I'll tell the agent to be careful in prompt." | Prompt instructions erode. Build mechanical gates or state logs instead. |
| "I'll write more feature tests." | This skill designs the harness (test gates), not the feature code. |
| "Assess the whole codebase." | Focus on harness infrastructure (docs, scripts, CI), not source logic. |

## Red Flags

- Fixes are text rules in `AGENTS.md` without mechanical enforcement.
- Security-sensitive flows lack documented permission structures.
- Observability logs are written but never triaged.

## Verification

- [ ] Assess covers all 6 subsystems with 1-5 scores.
- [ ] Subsystem fixes address a documented failure category.
- [ ] Evaluation findings are explicit.

## Output Rules

- Can create/update: `artifacts/features/<slug>/harness-assessment.md`, `artifacts/features/<slug>/eval-report.md`, `AGENTS.md`, `HARNESS_CARD.md`, `memories/repo/harness-config.md`, `memories/repo/observability-log.md`, `docs/generated/codemap.md`, `docs/generated/references-index.md`.
- Read-Only: `memories/repo/constitution.md`, `memories/repo/security-policy.md`, `memories/repo/project-knowledge-base.md`, `memories/repo/learned-heuristics.md` (route updates to `/context-memory`).
- Cannot create: `spec.md`, `plan.md`, `tasks.md`, feature code.
