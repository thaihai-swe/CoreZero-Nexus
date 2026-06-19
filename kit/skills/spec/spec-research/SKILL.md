---
name: spec-research
description: Investigate an unknown problem space or bug and produce an analysis artifact.
compatibility: Designed for AI coding agents.
---

# Kit Research

## Overview
Investigate system behaviors and produce `artifacts/features/<slug>/analysis.md`. Use this for debugging, failure tracing, and mapping brownfield code before writing a spec or plan.

## I/O Hand-off Protocol
- **Reads**: `artifacts/features/<slug>/status.md`, codebase files.
- **Writes**: `artifacts/features/<slug>/analysis.md`, `artifacts/features/<slug>/status.md`.
- **Next Skill**: `/spec-requirements` or `/spec-plan`.

## Workflow
1. **Initialize State**: Update the `## Current State` section of `artifacts/features/<slug>/status.md` to set phase to `Researching`.
1.5 **Domain Pack Scan**: For each installed pack listed in `MASTER_INDEX.md` `## By Domain Packs`, read `memories/domain/<name>/glossary.md` frontmatter `triggers:`. If any trigger keyword appears in the user's task description or proposal, note the matched pack name in `status.md` under `## Loaded Domain Packs`. Load that pack's `glossary.md` now. Do this before conducting research.
2. **Reproduce**: For bugs, recreate the failure first.
3. **Map**: Map target files, trace dependencies, and identify boundaries.
4. **Document**: Write findings, risks, and next steps in `artifacts/features/<slug>/analysis.md`.
5. **Handoff**: Set `artifacts/features/<slug>/status.md` to `Research Complete`. Route to `/spec-requirements` if scope is clear, or `/spec-plan` if a formal plan is needed first.

## Core Rules
- **Fact-Focused**: Separate observed facts from inferences. Prove hypotheses with code evidence.
- **Scope Limit**: Write analysis only. Do NOT write code or plans yet.
- **Strict I/O**: Do not create custom artifacts outside of the designated files.
