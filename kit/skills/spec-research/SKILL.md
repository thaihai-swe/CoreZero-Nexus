---
name: spec-research
description: Investigate a problem, feature area, bug, or brownfield subsystem and produce one bounded analysis artifact grounded in repository evidence. Use when root cause is unknown or current behavior must be mapped first.
---

# Kit Research

## Overview
Investigate system behaviors and produce `artifacts/features/<slug>/analysis.md`. Use this for debugging, failure tracing, and mapping brownfield code before writing a spec or plan.
## When to Use

- Understand current behavior before writing a spec/plan.
- Diagnose and reproduce bugs.
- Map boundaries, dependencies, and stable patterns in brownfield paths.
## I/O Hand-off Protocol
- **Reads**: `artifacts/features/<slug>/status.md`, codebase files, domain packs.
- **Writes**: `artifacts/features/<slug>/analysis.md`, `artifacts/features/<slug>/status.md`.
- **Next Skill**: `/spec-requirements`, `/spec-adr`, or `/spec-plan`.

## Workflow

1. **Initialization**: Create `status.md` if missing. Update the `## Current State` section to set phase to `Researching`. Load the rigor profile from `status.md` or fallback to `memories/repo/harness-config.md` default (use Automated Profile Selection from `../_shared/rigor-profiles.md` if not set).
2. **Context Alignment**: For each installed pack listed in `MASTER_INDEX.md`, read `memories/domain/<name>/glossary.md` frontmatter `triggers:`. If matched, note in `status.md` and load that pack's `glossary.md` before conducting research.
3. **Reproduce & Trace**: For bugs, recreate the failure with a script or concrete steps before investigating (Reproduce -> Hypothesize -> Instrument -> Observe). Follow the request path from symptoms to the first failing boundary.
   - **Subagent-First Exploration (SFE):** Before reading large subsystems manually, delegate exploration to subagents. Assign each subagent a bounded area and return summary reports to the main context.
4. **Brownfield Mapping**: Map target files, trace dependencies, identify preserved behaviors, boundary contracts, reuse patterns, risks, and migration constraints. 
5. **Document**: Write all findings, risks, and next steps in `artifacts/features/<slug>/analysis.md` using the Brownfield Readiness Artifact structure from `references/analysis-template.md` (or `references/brownfield-mapping-template.md`).
6. **Handoff**: Update `status.md` to `Research Complete`. Route based on findings:
   - Scope and requirements clear → `/spec-requirements`
   - Contested technical choice blocks requirements → `/spec-adr` first, then `/spec-requirements`
   - Brownfield complexity requires formal plan before spec → `/spec-plan` (document rationale)
   - Inconclusive (evidence too sparse) → stop. Write `[INCONCLUSIVE]` in `analysis.md` and surface to user.
## Core Rules
- **Fact-Focused**: Separate observed facts from inferences. Prove hypotheses with code evidence.
- **Scope Limit**: Write analysis only. Do NOT write code or plans yet.
- **Strict I/O**: Do not create custom artifacts outside of the designated files.
