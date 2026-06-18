# CoreZero Nexus Overview & Core Workflow

The CoreZero Nexus developer kit is an engineering harness built to provide strict, spec-anchored, and test-validated AI coding agent workflows. It prevents common AI agent failure modes—such as context window amnesia, code bloat ("AI slop"), spec drift, and silent regressions—by structuring the workspace and enforcing strict progression gates.

---

## 1. The 5-Layer Architecture Model

CoreZero Nexus operates across five distinct layers that separate concerns and maintain a minimal, high-signal context window:

```text
┌─────────────────────────────────────────────┐
│  1. Entrypoint Layer (AGENTS.md)            │  Thin task router -> points to skills
├─────────────────────────────────────────────┤
│  2. Skill Layer (skills/*/SKILL.md)         │  11 core delivery + 4 specialist capability cards
├─────────────────────────────────────────────┤
│  3. Harness Layer (6 subsystems)            │  Rules, validation commands, and session control
├─────────────────────────────────────────────┤
│  4. Artifact Layer (artifacts/features/)    │  Per-feature durable development state
├─────────────────────────────────────────────┤
│  5. Memory Layer (memories/repo/ & domain/) │  Durable cross-session knowledge & domain constraints
└─────────────────────────────────────────────┘
```

1. **Entrypoint Layer ([`AGENTS.md`](../kit/AGENTS.md)):** A minimal, high-level router (< 50 lines) that tells the agent where to find instructions for specific tasks, avoiding loading heavy skill configurations until needed.
2. **Skill Layer ([`skills/`](../kit/skills/)):** Compressed, token-efficient contracts (`SKILL.md`) that detail workflows, core rules, warning red flags, stop conditions, and outputs for specific tasks.
3. **Harness Layer ([`core-policies.md`](../kit/memories/repo/core-policies.md) and [`HARNESS_CARD.md`](../kit/HARNESS_CARD.md)):** The environment configuration that declares verification command lists, paths, and live session limits/status.
4. **Artifact Layer (`artifacts/features/<slug>/`):** The isolated scratchpad for the active feature. It contains the feature status, locked specifications, task checkboxes, verification logs, and session progress trackers.
5. **Memory Layer ([`memories/`](../kit/memories/)):** Separated into:
    - **`repo/`** ([Durable repository-wide memory](../kit/memories/repo/)): constitution, heuristics, knowledge base, security policies.
    - **`domain/`** ([Adopter-owned domain-specific templates](../kit/memories/domain/)): glossary, boundaries, patterns, and canonical specifications.

---

## 2. 6-Tier Context Assembly & Smart Routing

To conserve context window budget and prevent AI hallucination, the kit structures context into six tiers and loads them progressively:

```text
     [Tier 1: Router] (AGENTS.md + INDEX.md)
            │ (loaded every session)
            ▼
     [Tier 2: Repo Memory (Always)] (constitution + security-policy + harness-config)
            │ (loaded every session)
            ▼
     [Tier 3: Repo Memory (By Intent)] (Knowledge / Learned / Debug groups via memories/repo/INDEX.md)
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

- **INDEX-Driven Trigger Loading (Tier 3):** Under [`INDEX.md`](../kit/memories/repo/INDEX.md), files in Tier 3 are loaded selectively based on query triggers defined in [`memories/repo/INDEX.md`](../kit/memories/repo/INDEX.md):
    - **Knowledge:** Loads [`project-knowledge-base.md`](../kit/memories/repo/project-knowledge-base.md), architecture, and indexes when keywords like `architecture`, `pattern`, `stack`, or `domain` are matched.
    - **Learned:** Loads [`learned-heuristics.md`](../kit/memories/repo/learned-heuristics.md) when keywords like `heuristic`, `recurring`, or `lesson` are matched.
    - **Debug:** Loads [`harness-telemetry.md`](../kit/memories/repo/harness-telemetry.md) when keywords like `debug`, `failure`, or `root cause` are matched.

- **Confidence-Scored Loading:** If ≤ 2 keywords match, a partial-load is executed (loading only index/header files for context awareness). High-confidence matches (3+ keywords) trigger a full-load of all group files.

---

## 3. End-to-End Workflow Lifecycle

A complete feature delivery lifecycle follows a rigorous chronological sequence of commands and phases:

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

### Phase 1: Repository Bootstrapping ([`/starter-init`](../kit/skills/starter-init/SKILL.md))
- Initializes the environment, parses dependencies, and registers targets.
- **Gitignore Injection:** Excludes ephemeral generated artifacts and telemetry (`docs/generated/*`, `memories/repo/harness-telemetry.md`) from version control.
- **Greenfield Mode:** Prefills standard templates and triggers.
- **Brownfield Mode (Phase A - Archaeology):** Runs a deep static sweep to identify code debt, dependency graphs, and seeds legacy boundary rules into `memories/repo/brownfield/`.

### Phase 2: Session Initialization ([`/context-session START`](../kit/skills/context-session/SKILL.md))
- Initiates the feature sandbox under a specific slug (e.g. `feature-abc`).
- Sets up `status.md` and reads `handoff.md` from the previous session to ensure continuous execution.

### Phase 3: Specification Intake ([`/spec-requirements`](../kit/skills/spec-requirements/SKILL.md))
- Conducts a "Socratic Grilling" phase, asking the developer clarifying questions to avoid assumptions.
- Authors the canonical `spec.md` requiring strict deterministic Acceptance Criteria formatted as markdown checklists (`- [ ]`) or Gherkin (`Given/When/Then`) mapped to binary verification commands.

### Phase 4: Planning ([`/spec-plan`](../kit/skills/spec-plan/SKILL.md))
- Drafts Architectural Decision Records (ADRs) via `/spec-adr` if system architecture is modified.
- Generates `plan.md` (listing target files, code modification specifications, and verification commands).
- Populates `tasks.md` (a checklist of granular coding tasks paired with evidence-proving commands).

### Phase 5: Implementation ([`/spec-implement`](../kit/skills/spec-implement/SKILL.md))
- Agent executes modifications in targeted files.
- Coding standards in [`docs/rules/`](../kit/docs/rules/) (syntax, language-specific lints, and security standards) must be strictly adhered to.
- For every task item, the agent runs the localized proof command, records the outcome, and immediately evicts raw console logs to prevent context fatigue.

### Phase 6: Verification & Review ([`/harness-verify`](../kit/skills/harness-verify/SKILL.md))
- **Mechanical Gate:** Runs the workspace-wide check suite (linting, build verification, and test suites) to ensure zero broken baselines.
- **Circuit Breaker:** Tracks failure counts to prevent infinite loops; if an implementation fails verification >= 2 times, it routes back to `/spec-plan` or `/code-review`.
- **Alignment Audit:** Maps every single `AC-*` from `spec.md` to task proofs to verify full requirements implementation.
- **Code Review:** Checks code against safety guidelines and Google-standard coding policies.
- Promotes feature status to `Done` in `status.md`.

### Phase 7: Memory Promotion ([`/context-memory`](../kit/skills/context-memory/SKILL.md))
- Closes out the session via `/context-session END` which distills lesson candidates into `session-extracts.md`.
- Post-ship sync evaluates candidate lessons and promotes them to the durable instruction tier (`project-knowledge-base.md`, `learned-heuristics.md`, or domain packs under `memories/domain/`).

---

## 4. Operational & Specialist Skills

Nexus also contains specialist commands that run outside of the primary delivery loop to maintain the repository health:
- **`/harness-maintain`:** Updates generated indexes (`codemap.md` and `references-index.md`) and analyzes failures in `harness-telemetry.md` to suggest gate adjustments.
- **`/visualize`:** Parses Mermaid markup and renders high-fidelity SVG architectural diagrams or data-flow maps.
- **`/code-review`:** Performs manual-trigger code quality and security reviews.
- **`/technical-docs`:** Automatically generates API flowcharts, contracts, and schema documentation.
- **`/codebase-documenter`:** Refreshes adopter-facing orientation assets and README guides.
