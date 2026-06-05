---
name: starter-init
description: Initialize a project for harnessed agentic development by reconciling and filling the installer-seeded surface, validating repo state, and establishing repo-specific baselines before feature work begins.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in harness-engineered repositories that use memories/repo/ and artifacts/features/<slug>/.

---

# Kit Init


## Overview

Establishes the repository baseline for the harness before feature work begins. It scans the repo, determines if greenfield or brownfield, interviews for defaults in `harness-config.md`, tests repository health, reconciles the installer-seeded files, and hands off to `/context-session`.

## Read First

- Root-level entrypoint files (`AGENTS.md`, `CLAUDE.md`, etc., if they exist)
- `memories/repo/harness-config.md` (if exists)
- `memories/repo/constitution.md` and `memories/repo/security-policy.md` (if they exist)
- `memories/repo/project-knowledge-base.md` and `memories/repo/learned-heuristics.md` (if they exist)

## When to Use

- Bootstrapping a new repository for agentic workflows.
- Re-initializing a repository after major architectural changes or baseline drift.

## Workflow

1. **Context Load**: Identify tech stack, test runners, linters, and CI pipelines.
2. **Greenfield vs Brownfield vs Vibe-Coded**: Detect repository type:
   - **Greenfield**: New or near-empty repo. Run standard init flow.
   - **Brownfield**: Has existing code, tests, CI, or history. Activate Brownfield Mode (see [references/brownfield-mode.md](references/brownfield-mode.md)).
   - **Vibe-Coded**: Has code but lacks tests, CI, documented architecture, and consistent conventions (3+ vibe-coded indicators). Activate Vibe-Coded Mode (see [references/vibecoded-mode.md](references/vibecoded-mode.md)). Requires explicit user acknowledgment before proceeding to feature work.
3. **Repo-Config Interview**: Capture tracker mode, artifact paths, verification commands, and compaction triggers in `memories/repo/harness-config.md`.
4. **Repo Readiness Check**: Run canonical tests/lint/build baseline checks. If tests do not exist, document the best available proof surface.
5. **Installer Surface Check**: Confirm the installer-seeded files exist (`AGENTS.md`, `HARNESS_CARD.md`, `memories/repo/*`, seeded `docs/*.md`, `docs/generated/*`). If the surface is incomplete, stop and route to `bash scripts/doctor.sh` or re-run `install.sh`.
6. **Required Bootstrap**: Reconcile the existing entrypoints and update `memories/repo/harness-config.md`.
7. **Template Pre-Fill**: Fill only the seeded `docs/*.md` files and `docs/architecture.md` from code evidence (Tier 1) or user feedback (Tier 2), marking judgment fields with `[USER REVIEW NEEDED]`.
8. **Memory Fill**: Populate the seeded memory files (`constitution.md`, `security-policy.md`, `learned-heuristics.md`, `project-knowledge-base.md`) with repository-specific content.
9. **Optional Enrichment**: Update the seeded `docs/generated/codemap.md` and `docs/generated/references-index.md` for non-trivial repositories.
10. **Failure Log Bootstrap**: Fill the seeded `memories/repo/observability-log.md` baseline if it is still template-empty.
10. **Handoff**: State readiness status, name any gaps, and instruct user to run `/context-session`.

## Stop Conditions

- Repository build or test state is broken. Require user intervention first.
- Required configurations cannot be determined.
- Installer-seeded harness files are missing or the install surface is incomplete.
- Vibe-Coded Mode: security flags include hardcoded production credentials — halt before proceeding.
- Vibe-Coded Mode: user does not acknowledge the baseline report — do not create feature artifacts.

## Preconditions

- **Precondition Check**: `install.sh` has already seeded the harness surface. `starter-init` fills and reconciles those files; it is not a replacement for the installer.
- **Phase sets**: Creates progress logs; lifecycle begins with `/spec-requirements` or `/spec-research`.

## Core Rules

- **Router Entrypoint**: Keep one canonical router body. In the kit source, `AGENTS.md` is the canonical shipped router; downstream init seeds from that source instead of maintaining a forked duplicate template.
- **No Shadow Installer**: Do not create new harness files during init that `install.sh` was responsible for seeding. If a seeded file is missing, stop and repair the install surface instead of silently creating it.
- **Evidence-Extraction**: Extract PKB rules from code, do not invent them.
- **Config First**: Always define commands and folders in `harness-config.md` before proceeding.
- **Security Baseline**: Formulate trust boundaries in `security-policy.md` during bootstrap.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "Put all rules in AGENTS.md." | Giant entrypoints exhaust context window. Use it as a router. |
| "Fix broken baseline tests later." | Establish a clean, working build baseline first. |
| "Let the agent guess test commands." | Guessing creates drift. Document exact mechanical commands. |
| "Init can just create missing harness files." | Missing seeded files mean the install surface is broken. Repair the install first. |
| "I'll create the first feature logs now." | Init is only for repository setup, not feature execution. |

## Red Flags

- No baseline proof run or configured.
- A seeded harness file is missing and init keeps going anyway.
- `harness-config.md` or `security-policy.md` are missing/empty.
- Feature-local files (`progress.md`, `tasks.md`) created during init.

## Verification

- [ ] `AGENTS.md` and `HARNESS_CARD.md` set up.
- [ ] Installer-seeded harness files are present before any fill-in work starts.
- [ ] `memories/repo/harness-config.md` captures all commands and defaults.
- [ ] Memory seed files (`constitution.md`, `security-policy.md`, `learned-heuristics.md`, `project-knowledge-base.md`) populated.
- [ ] Baseline build/test checks pass.

## Output Rules

- Can update seeded installer files: `AGENTS.md`, `HARNESS_CARD.md`, `memories/repo/harness-config.md`, `memories/repo/constitution.md`, `memories/repo/security-policy.md`, `memories/repo/learned-heuristics.md`, `memories/repo/project-knowledge-base.md`, `memories/repo/observability-log.md`, `docs/architecture.md`, `docs/generated/codemap.md`, `docs/generated/references-index.md`, and the seeded project-policy docs under `docs/*.md`.
- Cannot create missing harness surface files that `install.sh` was supposed to seed; stop and repair the install surface instead.
- Cannot create: `spec.md`, `plan.md`, `tasks.md`, `design.md`.

## References

- [references/init-checklist.md](references/init-checklist.md)
- [../../AGENTS.md](../../AGENTS.md)
- [references/harness-config-template.md](references/harness-config-template.md)
- [../_shared/rigor-profiles.md](../_shared/rigor-profiles.md)
- [references/harness-card-template.md](references/harness-card-template.md)
- [references/brownfield-mode.md](references/brownfield-mode.md)
- [references/vibecoded-mode.md](references/vibecoded-mode.md)
- [references/template-prefill.md](references/template-prefill.md)
- [../context-memory/references/architecture-template.md](../context-memory/references/architecture-template.md)
- [../context-memory/references/security-policy-template.md](../context-memory/references/security-policy-template.md)
- [../context-memory/references/learned-heuristics-template.md](../context-memory/references/learned-heuristics-template.md)
- [../context-memory/references/observability-log-template.md](../context-memory/references/observability-log-template.md)
- [../harness-maintain/references/codemap-template.md](../harness-maintain/references/codemap-template.md)
- [../harness-maintain/references/references-index-template.md](../harness-maintain/references/references-index-template.md)
