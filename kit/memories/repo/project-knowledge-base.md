# CoreZero Nexus Project Knowledge Base

## Repository Overview

- This repository is an artifact-first kit for Harness Engineering and spec-driven AI development.
- Core workflow logic lives in `skills/*/SKILL.md`.
- Reusable scaffolds live beside each skill under `references/`.
- Adopter-facing documentation lives under `docs/`.
- Maintainer-facing documentation lives under `documents/`.
- Generated references live under `docs/generated/`.
- Bootstrap and maintenance scripts live under `scripts/`.

## Key Architectural Boundaries

### 1. Shipped Template Copy Posture
The installer script (`scripts/install.sh`) handles files using three distinct postures specified in `manifest.json`:
- **`overwrite`**: Core kit tools and guides (e.g. `skills/**`, `rules/**`, `docs/README.md`, `docs/ADOPTION_GUIDE.md`) that are refreshed on every upgrade to keep the automation framework up to date.
- **`copyIfMissing`**: Starter template files and memory baselines (e.g., `AGENTS.md`, `constitution.md`, `project-knowledge-base.md`). If the adopter project has customized these, the installer respects their edits and does not overwrite them.
- **`preserve`**: Feature-specific state folders (`artifacts/features/`, local settings). These are completely owned by the adopter project and are never touched by the installer.

### 2. Adaptive Rigor Selection Logic
Features execute under one of three delivery profiles defined in `skills/_shared/rigor-profiles.md`:
- **`Tiny`**: Small, low-risk, reversible edits. Can bypass separate `design.md`, `proposal.md`, or `requirements-review.md` files (inlining verification/readiness into status/spec instead).
- **`Standard`**: The default feature delivery profile. Normal spec, plan, and task list. `design.md` is only authored if technical ambiguity remains.
- **`Complex`**: Risk-heavy or cross-cutting work. Mandates detailed `design.md`, subagent-driven stress-testing, adversarial planning, and phased rollouts.
*Watchout:* Any work touching authentication (`auth`), databases (`data_model`), security-policy files, public API contracts, or the harness configuration itself forces a promotion to `Complex`.

### 3. The Memory Governance Loop
Repository memory is tiered to prevent context bloat:
- **Instruction Tier** (Static rules & facts): Constitution, PKB, and Security Policy. Loaded regularly based on active intent triggers in `memories/repo/INDEX.md`.
- **Auto Tier** (Execution telemetry): `observability-log.md`. Tracks harness, model, or spec failures. Triaged by `/context-memory` to promote key lessons to the instruction tier.
- **Extracted Tier** (Local lessons): `session-extracts.md`. Generated at session END. Candidates are kept local to features until triage merges them upstream.

### 4. Gated Integration vs. Standalone Review Distinction
The `code-review` skill is dual-purpose:
- **Standalone PR Mode**: Executed for human reviewers. Uses standard LGTM-with-comments, 1-day SLAs, and collaborative discussion.
- **Gated Integration Mode**: Executed programmatically by `/harness-verify`. It is a single-turn, automated blocking pass. The reviewer agent must immediately write its findings to `review.md` and fail loud if any acceptance criteria are unsatisfied.

## Common Installation & Bootstrap Watchouts

- **Baseline Testing**: `/starter-init` checks whether the target repository is greenfield or brownfield. It requires running the canonical baseline test or compile check. If none exists, the adopter must document the best available proof surface before autonomous feature work can proceed.
- **Drift in Routers**: `AGENTS.md` must stay under 50 lines for its router portion to prevent context window saturation. Standard operating guidelines should remain in `constitution.md` and only be linked from `AGENTS.md`.

## Feature Lifecycle Handoff Patterns

- The first feature starts with `/spec-requirements` or `/spec-research`. `/context-session` is the session-boundary skill only after a feature slug and `status.md` already exist, and it still closes long work sessions with `handoff.md` and `progress.md`.
- Mismatches between handoff claims and actual disk state at session start must be routed to `/harness-maintain assess` to repair the state before delivery work commences.
