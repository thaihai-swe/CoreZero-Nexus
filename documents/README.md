# CoreZero Maintainer Documentation & Overview

The CoreZero developer kit is an engineering harness built to provide strict, spec-anchored, and test-validated AI coding agent workflows. It prevents common AI agent failure modes—such as context window amnesia, code bloat ("AI slop"), spec drift, and silent regressions—by structuring the workspace and enforcing strict progression gates.

Maintainer entrypoint for the CoreZero source repository.

## Start Here

CoreZero now has two explicit products:

- `kit/` — the installable adopter package
- `documents/` plus `page-document/` — maintainer and public explainer surfaces

When changing shipped behavior, start in `kit/`. When changing explanation, release notes, or site copy, work in `documents/` and `page-document/`.

## Maintainer Reading Order

1. [architecture.md](architecture.md) — repo architecture and boundaries
2. [TEMPLATE_SURFACE.md](TEMPLATE_SURFACE.md) — exact shipped surface and ownership
3. [INSTALL.md](INSTALL.md) — install, upgrade, and validation flow
4. [skills-guide.md](skills-guide.md) — shipped commands and any future `source-only` markers
5. [releasing.md](releasing.md) — release, version-sync, and Pages checklist

## Source Of Truth

The repo follows this truth order:

1. `kit/manifest.json` for shipped surface
2. `kit/skills/*/SKILL.md` for workflow behavior
3. `documents/` for maintainer explanation
4. generated files only as derived placeholders

## Current Packaging Position

The installed package ships the full command surface:

- shipped commands:
  - `/starter-init`
  - `/spec-research`
  - `/spec-requirements`
  - `/spec-plan`
  - `/spec-implement`
  - `/harness-verify`
  - `/context-session`
  - `/context-memory`
  - `/context-status`
  - `/harness-maintain`
  - `/spec-adr`
  - `/code-review`
  - `/technical-docs`
  - `/codebase-documenter`
  - `/visualize`
- the `source-only` marker is reserved for future skills that remain in the repo but stay out of `kit/manifest.json`

## Validation

For packaging changes, at minimum run the installer flow locally:

```bash
bash scripts/install.sh /tmp/corezero-check --dry-run
```

## System Overview

### 1. The 5-Layer Architecture Model

CoreZero operates across five distinct layers that separate concerns and maintain a minimal, high-signal context window:

```text
┌─────────────────────────────────────────────┐
│  1. Entrypoint Layer (AGENTS.md)            │  Thin task router -> points to skills
├─────────────────────────────────────────────┤
│  2. Skill Layer (skills/*/SKILL.md)         │  17 skills across 4 groups (Lifecycle, Context & Memory, Quality & Docs, Visualization)
├─────────────────────────────────────────────┤
│  3. Harness Layer (ETCLOVG Taxonomy)        │  Rules, validation commands, and session control
├─────────────────────────────────────────────┤
│  4. Artifact Layer (artifacts/features/)    │  Per-feature durable development state
├─────────────────────────────────────────────┤
│  5. Memory Layer (memories/repo/ & domain/) │  Durable cross-session knowledge & domain constraints
└─────────────────────────────────────────────┘
```

1. **Entrypoint Layer ([`AGENTS.md`](../kit/AGENTS.md)):** A minimal, high-level router (< 50 lines) that tells the agent where to find instructions for specific tasks, avoiding loading heavy skill configurations until needed.
2. **Skill Layer ([`skills/`](../kit/skills/)):** Compressed, token-efficient contracts (`SKILL.md`) that detail workflows, core rules, warning red flags, stop conditions, and outputs for specific tasks.
3. **Harness Layer ([`harness-config.md`](../kit/memories/repo/harness-config.md)):** The environment configuration structured around the 7-pillar **ETCLOVG** taxonomy, declaring verification command lists, paths, and live session limits/status.
4. **Artifact Layer (`artifacts/features/<slug>/`):** The isolated scratchpad for the active feature. It contains the feature status, locked specifications, task checkboxes, verification logs, and session progress trackers.
5. **Memory Layer ([`memories/`](../kit/memories/)):** Separated into:
    - **`repo/`** ([Durable repository-wide memory](../kit/memories/repo/)): constitution, heuristics, knowledge base, security policies.
    - **`domain/`** ([Adopter-owned domain-specific templates](../kit/memories/domain/)): glossary, boundaries, patterns, and canonical specifications.

### 2. 6-Tier Context Assembly & Smart Routing

To conserve context window budget and prevent AI hallucination, the kit structures context into six tiers and loads them progressively:

```text
      [Tier 1: Router] (AGENTS.md + MASTER_INDEX.md)
             │ (loaded every session)
             ▼
      [Tier 2: Repo Memory (Always)] (constitution + security-policy + harness-config)
             │ (loaded every session)
             ▼
 [Tier 3: Repo Memory (By Intent)] (Knowledge / Learned / Debug groups via MASTER_INDEX.md)
              │ (loaded based on task trigger keywords)
             ▼
      [Tier 4: Feature Artifacts] (status.md, spec.md, plan.md, tasks.md, handoff.md)
             │ (loaded before editing or verifying)
             ▼
      [Tier 5: JIT Raw Code] (files targeted for immediate modification)
             │ (loaded just-in-time)
             ▼
      [Tier 6: Transient Logs] (command output, test outputs, grep searches)
               (summarized and evicted immediately to avoid bloating)
```

- **Trigger Loading (Tier 3):** Under [`MASTER_INDEX.md`](../kit/MASTER_INDEX.md), files in Tier 3 are loaded selectively based on query triggers defined in [`MASTER_INDEX.md`](../kit/MASTER_INDEX.md):
    - **Knowledge:** Loads [`project-knowledge-base.md`](../kit/memories/repo/project-knowledge-base.md), architecture, and indexes when keywords like `architecture`, `pattern`, `stack`, or `domain` are matched.
    - **Learned:** Loads [`learned-heuristics.md`](../kit/memories/repo/learned-heuristics.md) when keywords like `heuristic`, `recurring`, or `lesson` are matched.
    - **Debug:** Loads [`harness-telemetry.md`](../kit/memories/repo/harness-telemetry.md) when keywords like `debug`, `failure`, or `root cause` are matched.

- **Confidence-Scored Loading:** If ≤ 2 keywords match, a partial-load is executed (loading only index/header files for context awareness). High-confidence matches (3+ keywords) trigger a full-load of all group files.

### 3. End-to-End Workflow Lifecycle

A complete feature delivery lifecycle follows a structured chronological sequence of commands and phases:

```text
       1. Bootstrap           2. Session START        3. Requirements Intake
     ┌──────────────┐        ┌────────────────┐       ┌────────────────────┐
     │ /starter-init│ ──────>│/context-session│ ─────>│ /spec-requirements │
     └──────────────┘        └────────────────┘       └────────────────────┘
                                                                 │
                                                                 ▼
       6. Closeout            5. Implementation       4. Design & Planning
     ┌──────────────┐        ┌────────────────┐       ┌────────────────────┐
     │/harness-verify│<──────│ /spec-implement│<───── │     /spec-plan     │
     └──────────────┘        └────────────────┘       └────────────────────┘
            │
            ▼
       7. Memory Sync
     ┌────────────────┐
     │ /context-memory│ ──────> [Updated constitution, PKB & Heuristics]
     └────────────────┘
```

#### Phase 1: Repository Bootstrapping ([`/starter-init`](../kit/skills/starter-init/SKILL.md))
- Initializes the environment, parses dependencies, and registers targets.
- **Gitignore Injection:** Excludes ephemeral generated artifacts and telemetry (`core-zero/generated/*`, `memories/repo/harness-telemetry.md`) from version control.
- **Greenfield Mode:** Prefills standard templates and triggers.
- **Brownfield Mode (Phase A - Archaeology):** Runs a deep static sweep to identify code debt, dependency graphs, and records risk area notes into `memories/repo/project-knowledge-base.md`.

#### Phase 2: Session Initialization ([`/context-session START`](../kit/skills/context-session/SKILL.md))
- Initiates the feature sandbox under a specific slug (e.g. `feature-abc`).
- Sets up `status.md` and reads `handoff.md` from the previous session to ensure continuous execution.

#### Phase 3: Specification Intake ([`/spec-requirements`](../kit/skills/spec-requirements/SKILL.md))
- Conducts a Socratic evaluation phase, asking the developer clarifying questions to avoid assumptions.
- Authors the canonical `spec.md` requiring strict deterministic Acceptance Criteria formatted as markdown checklists (`- [ ]`) or Gherkin (`Given/When/Then`) mapped to binary verification commands.

#### Phase 4: Planning ([`/spec-plan`](../kit/skills/spec-plan/SKILL.md))
- Drafts Architectural Decision Records (ADRs) via `/spec-adr` if system architecture is modified.
- Generates `plan.md` (listing target files, code modification specifications, and verification commands).
- Populates `tasks.md` (a checklist of granular coding tasks paired with evidence-proving commands).

#### Phase 5: Implementation ([`/spec-implement`](../kit/skills/spec-implement/SKILL.md))
- Agent executes modifications in targeted files.
- Coding standards in [`core-zero/rules/`](../kit/core-zero/rules/) (syntax, language-specific lints, and security standards) must be strictly adhered to.
- For every task item, the agent runs the localized mechanical verification gate via `kit/scripts/harness/gate-runner.sh`.
- **Telemetry Collection:** If the gate fails, errors are piped to `kit/scripts/harness/telemetry-collector.sh` to update `harness-telemetry.md`.
- **Minimum Viable Context & Eviction:** The agent operates under strict Minimum Viable Context (MVC) guidelines, JIT-loading only targeted files, and evicts raw execution output from the active context window immediately after summarization.

#### Phase 6: Verification & Review ([`/harness-verify`](../kit/skills/harness-verify/SKILL.md))
- **Mechanical Gate:** Runs the workspace-wide check suite via `kit/scripts/harness/gate-runner.sh` (linting, build verification, and test suites) to ensure zero broken baselines.
- **Circuit Breaker:** Tracks failure counts to prevent infinite loops; if an implementation fails verification >= 2 times, it routes back to `/spec-plan` to rethink the approach.
- **Alignment Audit:** Maps every single `AC-*` from `spec.md` to task proofs to verify full requirements implementation.
- **Code Review:** Checks code against safety guidelines and Google-standard coding policies.
- Promotes feature status to `Done` in `status.md`.

#### Phase 7: Memory Promotion ([`/context-memory`](../kit/skills/context-memory/SKILL.md))
- Closes out the session via `/context-session END` which distills lesson candidates into `session-extracts.md`.
- Post-ship sync evaluates candidate lessons and promotes them to the durable instruction tier (`project-knowledge-base.md`, `learned-heuristics.md`, or domain packs under `memories/domain/`).

### 4. Operational & Specialist Skills

Nexus also contains specialist commands that run outside of the primary delivery loop to maintain the repository health:
- **`/harness-maintain`:** Updates generated indexes (`code-map.md`) and analyzes failures in `harness-telemetry.md` to suggest gate adjustments.
- **`/visualize`:** Parses Mermaid markup and renders high-fidelity SVG architectural diagrams or data-flow maps.
- **`/code-review`:** Performs manual-trigger code quality and security reviews.
- **`/ponytail`:** Enforces the laziest effective solution — checks for over-engineering, trims bloat, and maximises platform-native features. Intensity: lite / full (default) / ultra.
- **`/technical-docs`:** Automatically generates API flowcharts, contracts, and schema documentation.
- **`/codebase-documenter`:** Refreshes adopter-facing orientation assets and README guides.

`scripts/context-loader.py` provides `--mode summary` to extract the index or first 50 lines of any memory file, enforcing MVC without agent interpretation.
