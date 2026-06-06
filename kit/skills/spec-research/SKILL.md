---
name: spec-research
description: Investigate a problem, feature area, bug, or brownfield subsystem and produce one bounded analysis artifact grounded in repository evidence. Use when root cause is unknown or current behavior must be mapped first.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in spec-driven repositories that use memories/repo/ and artifacts/features/<slug>/.

---

# Kit Research


## Routing Guide

- **Use `/spec-research`** to investigate unknown problem spaces, bug causes, or brownfield code states.
- **Use `/spec-requirements`** to define requirements and acceptance criteria.

## Overview

Investigate system behaviors and produce an analysis artifact (`artifacts/features/<slug>/analysis.md`). This skill covers debugging, failure tracing, root-cause discovery, and brownfield mapping before implementation work begins.

## Read First

- `artifacts/features/<slug>/status.md` (if exists)
- `memories/repo/constitution.md` and `memories/repo/security-policy.md`
- `memories/repo/project-knowledge-base.md`
- Related files/caller interfaces.
- References: `references/analysis-template.md` and `references/debugging-checklist.md`.

## When to Use

- Understand current behavior before writing a spec/plan.
- Diagnose and reproduce bugs.
- Map boundaries, dependencies, and stable patterns in brownfield paths.

## Workflow

0. **Claim Check**: Before touching any feature artifact, check `artifacts/features/<slug>/claim.md`.
   - If an active, non-expired claim exists from a different agent → stop. Report `BLOCKED: <agent-id> holds an active claim. Wait for release or expiry.`
   - If no claim exists or the existing claim is stale (expired timestamp or `Released` status) → create/update `claim.md` to establish ownership. Use the format from `../context-session/references/multi-agent-protocol.md`.
1. **Initialization**: Create `status.md` if missing (set phase to `Researching`).
2. **Profile Load**: Read the rigor profile from `artifacts/features/<slug>/status.md` → `## 🧭 Delivery Profile`. If not set, fall back to `memories/repo/harness-config.md` default. Run the Automated Profile Selection Routine from `../_shared/rigor-profiles.md` if the profile has not been set yet.
3. **Reproduce**: For bugs, recreate the failure with a script or concrete steps before investigating. Follow: Reproduce -> Hypothesize -> Instrument -> Observe.
   **Subagent-First Exploration (SFE):** Before reading large subsystems manually, delegate exploration to subagents. Assign each subagent a bounded area (e.g., a single module or service boundary). Return summary reports only to the main context.
4. **Brownfield Mapping**: Map target files, trace their dependencies, identify preserved behaviors, boundary contracts, reuse patterns, risks, and migration constraints. Document all findings in `analysis.md` using the Brownfield Readiness Artifact structure from `references/analysis-template.md`.
5. **Trace**: Follow the request path from symptoms to the first failing boundary.
6. **Document**: Write findings, risks, and next steps in `analysis.md`.
7. **Handoff**: Update `status.md` to `Research Complete`. Route based on research findings:
   - Research reveals scope and requirements are clear → `/spec-requirements`
   - Research reveals a contested technical choice that blocks requirements → `/spec-adr` first, then `/spec-requirements`
   - Research reveals brownfield complexity requiring a formal plan before spec → `/spec-plan` (exceptional; document rationale)
   - Research is inconclusive (evidence too sparse) → stop. Write `[INCONCLUSIVE]` in `analysis.md` and surface to user.

## Stop Conditions

- Evidence is insufficient to distinguish facts from guesswork.
- Bug cannot be reproduced after 3 distinct instrumentation attempts — write what was tried, mark `analysis.md` as `[UNREPRODUCIBLE]`, stop.
- The brownfield area has no tests and no readable source files — stop. Cannot produce a meaningful readiness artifact.
- Research reveals the issue is out of scope for the current feature slug — stop and surface to user.

## Preconditions

- **Precondition Check**: Investigation findings must route through `/spec-requirements` before modifying plans or code.
- **Phase sets**: `Researching` → `Research Complete`.

## Core Rules

- **Subagent-First Exploration (SFE)**: Delegate broad searching to a subagent; merge only their **Summary Report** to keep context lean.
- **Fact-Focused**: Separate observed facts from inferences. Prove hypotheses with repository evidence.
- **Scope Limit**: Write analysis only, do not write code or plans.
- **Preserved Behavior**: Clearly specify what behavior must remain unchanged during future changes.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "Fix it during research." | Research is for understanding root causes. Coding happens in implementation phase. |
| "I know this error already." | Assumptions lead to incorrect fixes. Verify every hunch with evidence. |
| "Entire repo search is too slow." | Targeted, exhaustive research prevents 'whack-a-mole' bugs. |

## Red Flags

- Analysis reads like a plan, design, or requirements spec.
- Root cause claims are made without supporting code/log evidence.
- Suggesting changes without stating the behavior to preserve.

## Verification

- [ ] Facts and inferences are clearly separated.
- [ ] Claims are backed by observed code evidence.
- [ ] Preserved behaviors and reuse patterns are explicitly named.

## Output Rules

- Update only `analysis.md` and `status.md`.
- Do not modify source code, `plan.md`, or `tasks.md`.
