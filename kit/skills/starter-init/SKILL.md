---
name: starter-init
description: Initialize a project for harnessed agentic development. Detects repo type (greenfield / brownfield) and automatically runs an archaeology sweep (Phase A) before bootstrap (Phase B) when the repo has existing code, tests, CI, or history. Single entry point for all repo types.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in harness-engineered repositories that use memories/repo/ and artifacts/features/<slug>/.

---

# Kit Init


## Overview

Establishes the repository baseline for the harness before feature work begins. Detects repo type, runs a read-only archaeology pass for brownfield repositories (Phase A), then configures the harness and fills seeded memory files for all repo types (Phase B).

## Read First

- Root-level entrypoint files (`AGENTS.md`, `CLAUDE.md`, etc., if they exist)
- `memories/repo/harness-config.md` (if exists)
- `memories/repo/constitution.md` and `memories/repo/security-policy.md` (if they exist)
- `memories/repo/project-knowledge-base.md` and `memories/repo/learned-heuristics.md` (if they exist)

## When to Use

- Bootstrapping any repository for agentic workflows — greenfield or brownfield.
- Re-initializing a repository after major architectural changes or baseline drift.

## Workflow

### Phase A — Archaeology (brownfield repos only)

Skip Phase A entirely for greenfield repos. Activate when the repo has existing code, tests, CI pipelines, or meaningful git history. If `memories/repo/brownfield/brownfield-map.md` already exists from a prior run, skip Phase A and proceed directly to Phase B.

   **Re-run guard**: To re-run Phase A on a repo where `brownfield-map.md` already exists, the user must type exactly: `CONFIRM re-run Phase A`. Do not accept paraphrase. If not confirmed, skip Phase A and proceed directly to Phase B.

**A1. Scope Declaration**: Confirm the repo is non-trivial (has existing code, tests, or history). If the repo is greenfield (no meaningful content), skip to Phase B.

**A2. Subagent Read-Only Sweep**: Delegate a broad read-only exploration to subagents. Each subagent produces a summary report; raw output stays isolated. Subagents explore:
   - Source tree structure (top-level directories, file counts by type)
   - Test coverage indicators (test directories, CI config, coverage reports)
   - Security-sensitive paths (auth, payments, secrets loading, external API calls)
   - Entry points and public interfaces (routes, exported modules, CLI entrypoints)
   - High-fan-in modules (files imported by many others — high blast radius)

**A3. Brownfield Map**: Produce `memories/repo/brownfield/brownfield-map.md` using the template at `references/brownfield-map-template.md`. Classify each identified area by severity: `low` | `medium` | `high` | `critical`. Record: area name, severity, description, risky paths, implicit contracts, recommended action.

**A4. Dependency Graph**: Produce `memories/repo/brownfield/dependency-graph.md` using the template at `references/dependency-graph-template.md`. Map module-to-module dependencies. Flag modules with fan-in >= 5 as `risk_flag: true`.

**A5. HARNESS_CARD.md Annotation**: If `HARNESS_CARD.md` exists, update the `## Known Limits` section with brownfield-specific caveats found during the sweep (e.g., "Auth middleware has no test coverage", "Payment handler has 8 dependents — blast radius is high").

**A6. Heuristics Seeding**: Append 3–5 repo-specific watchouts to `memories/repo/learned-heuristics.md` (create the file if absent). Each watchout must be: evidence-backed (cite a file or pattern found), actionable, and specific to this codebase.

---

### Phase B — Bootstrap (all repos)

**B1. Context Load**: Identify tech stack, test runners, linters, and CI pipelines.

**B2. Repo Type Detection**: Determine if the repo is greenfield or brownfield. Record in `HARNESS_CARD.md` and `memories/repo/project-knowledge-base.md`:
   - **Greenfield**: New or near-empty repo. Phase A was skipped.
   - **Brownfield**: Has existing code, tests, CI, or history. Phase A must be complete before Phase B continues. Activate Brownfield Mode (see [references/brownfield-mode.md](references/brownfield-mode.md)).

**B3. Repo-Config Interview**: Capture tracker mode, artifact paths, verification commands, and compaction triggers in `memories/repo/harness-config.md`. The interview MUST confirm and record `Default profile:` in `memories/repo/harness-config.md` → `## Adaptive Rigor` before proceeding. If the user does not specify, default to `Standard` and document it.

**B4. Installer Surface Check**: Confirm the installer-seeded files exist (`AGENTS.md`, `HARNESS_CARD.md`, `memories/repo/*`, seeded `docs/*.md`, `docs/generated/*`). If the surface is incomplete, stop and route to `bash scripts/doctor.sh` or re-run `install.sh`.

**B5. Repo Readiness Check**: Run canonical tests/lint/build baseline checks. If tests do not exist, document the best available proof surface.

**B6. Required Bootstrap**: Reconcile the existing entrypoints and update `memories/repo/harness-config.md`.
   **Re-init rule**: If `harness-config.md` already exists with non-default values, read it first. Preserve existing values; only update fields that are empty or clearly wrong. Prompt the user before overwriting any non-default configured value.

**B7. Template Pre-Fill**: Fill only the seeded `docs/*.md` files and `docs/architecture.md` from code evidence (Tier 1) or user feedback (Tier 2), marking judgment fields with `[USER REVIEW NEEDED]`.

**B8. Memory Fill**: Populate the seeded memory files (`constitution.md`, `security-policy.md`, `learned-heuristics.md`, `project-knowledge-base.md`) with repository-specific content and freshness metadata where the template expects it.

**B9. Optional Enrichment**: Update the seeded `docs/generated/codemap.md` and `docs/generated/references-index.md` for non-trivial repositories.

**B10. Failure Log Bootstrap**: Fill the seeded `memories/repo/observability-log.md` baseline if it is still template-empty.

**B11. Handoff**: State readiness status, name any gaps, and route the first feature to `/spec-requirements` or `/spec-research`.

## Stop Conditions

- Repository build or test state is broken. Require user intervention first.
- Required configurations cannot be determined.
- Installer-seeded harness files are missing or the install surface is incomplete.
- Brownfield repo detected but Phase A has not run and user has not approved a re-run.
- Phase A: subagent sweep finds active production credentials or secrets in tracked files — halt, surface the finding, and require user remediation before any feature work begins.
- Phase A: repository has no readable source files — cannot produce meaningful map; stop and report.

## Preconditions

- **Precondition Check**: `install.sh` has already seeded the harness surface. `starter-init` fills and reconciles those files; it is not a replacement for the installer.
- **Phase sets**: Repository bootstrap only; feature lifecycle begins with `/spec-requirements` or `/spec-research`.

## Core Rules

- **Router Entrypoint**: Keep one canonical router body. In the kit source, `AGENTS.md` is the canonical shipped router; downstream init seeds from that source instead of maintaining a forked duplicate template.
- **Phase A is Read-Only**: The subagent exploration phase MUST be read-only. No file modifications during the sweep.
- **Subagent Summaries Only**: Raw subagent output (file listings, grep output) never floods the main context. Only summary reports merge back.
- **Evidence-Backed Heuristics**: Every entry added to `learned-heuristics.md` must cite a specific file, pattern, or commit as its evidence. No invented watchouts.
- **One-Shot Archaeology**: Phase A runs once per repository. Re-running overwrites the prior brownfield map; require explicit user confirmation before a re-run on an existing map.
- **Profile Auto-Promotion**: Record in `brownfield-map.md` under `## Profile Rules`: any feature that touches a path rated `high` or `critical` MUST be promoted to `Complex` profile in its `status.md`. Enforced during `/spec-requirements`.
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
| "Run `/starter-init` for greenfield only; use the old two-skill sequence for brownfield." | `/starter-init` handles all repo types. Phase A runs automatically for brownfield repos. |
| "I'll create the first feature logs now." | Init is only for repository setup, not feature execution. |
| "I'll add heuristics from memory, not from the code." | Heuristics without code evidence are invented rules. They will be wrong and will mislead future agents. |

## Red Flags

- No baseline proof run or configured.
- A seeded harness file is missing and init keeps going anyway.
- Brownfield repo detected but Phase A has not run.
- `harness-config.md` or `security-policy.md` are missing/empty.
- Feature-local files (`progress.md`, `tasks.md`) created during init.
- Brownfield map produced without a real subagent sweep (fabricated from assumptions).
- Heuristics added to `learned-heuristics.md` without file citations.
- Phase A run on a greenfield repo (produces a meaningless empty map).

## Verification

- [ ] `AGENTS.md` and `HARNESS_CARD.md` set up.
- [ ] Installer-seeded harness files are present before any fill-in work starts.
- [ ] **Brownfield Phase A** (if applicable):
  - [ ] `memories/repo/brownfield/brownfield-map.md` exists and has at least one rated area.
  - [ ] `memories/repo/brownfield/dependency-graph.md` exists and lists module dependencies.
  - [ ] `memories/repo/learned-heuristics.md` has 3–5 new entries with file citations.
  - [ ] `HARNESS_CARD.md` Known Limits section updated with brownfield-specific caveats.
  - [ ] No raw grep output in main context — subagent summaries only.
- [ ] `memories/repo/harness-config.md` captures all commands and defaults.
- [ ] Memory seed files (`constitution.md`, `security-policy.md`, `learned-heuristics.md`, `project-knowledge-base.md`) populated.
- [ ] Baseline build/test checks pass.

## Output Rules

- Can update seeded installer files: `AGENTS.md`, `HARNESS_CARD.md`, `memories/repo/harness-config.md`, `memories/repo/constitution.md`, `memories/repo/security-policy.md`, `memories/repo/learned-heuristics.md`, `memories/repo/project-knowledge-base.md`, `memories/repo/observability-log.md`, `docs/architecture.md`, `docs/generated/codemap.md`, `docs/generated/references-index.md`, and the seeded project-policy docs under `docs/*.md`.
- Can create (brownfield Phase A only): `memories/repo/brownfield/brownfield-map.md`, `memories/repo/brownfield/dependency-graph.md`.
- Cannot create missing harness surface files that `install.sh` was supposed to seed; stop and repair the install surface instead.
- Cannot create: `spec.md`, `plan.md`, `tasks.md`, `design.md`.

`starter-init` creates and seeds memory files (`constitution.md`, `security-policy.md`, `learned-heuristics.md`, `project-knowledge-base.md`) at init time. It does not overwrite non-empty versions of these files on re-init. Ongoing updates are owned by `/context-memory`.

## References

- [references/init-checklist.md](references/init-checklist.md)
- [../../AGENTS.md](../../AGENTS.md)
- [references/harness-config-template.md](references/harness-config-template.md)
- [../_shared/rigor-profiles.md](../_shared/rigor-profiles.md)
- [references/harness-card-template.md](references/harness-card-template.md)
- [references/brownfield-mode.md](references/brownfield-mode.md)
- [references/brownfield-map-template.md](references/brownfield-map-template.md)
- [references/dependency-graph-template.md](references/dependency-graph-template.md)
- [references/template-prefill.md](references/template-prefill.md)
- [../context-memory/references/architecture-template.md](../context-memory/references/architecture-template.md)
- [../context-memory/references/security-policy-template.md](../context-memory/references/security-policy-template.md)
- [../context-memory/references/learned-heuristics-template.md](../context-memory/references/learned-heuristics-template.md)
- [../context-memory/references/observability-log-template.md](../context-memory/references/observability-log-template.md)
- [../harness-maintain/references/codemap-template.md](../harness-maintain/references/codemap-template.md)
- [../harness-maintain/references/references-index-template.md](../harness-maintain/references/references-index-template.md)
