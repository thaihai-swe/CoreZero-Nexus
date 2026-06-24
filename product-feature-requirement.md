# CoreZero — Product Feature Requirements

> The document you present to users. It describes what CoreZero is, the problems it solves, and the full feature catalog shipped in the installable kit.

---

## 1. What CoreZero Is

**CoreZero** is a spec-anchored AI software delivery harness. It is installed into any repository via a single command (`bash scripts/install.sh /path/to/repo`) and turns an AI coding agent into a disciplined, evidence-backed delivery system that:

- **Locks specs before code** — no implementation starts until requirements are testable.
- **Plans every task** — target files, edit specs, and verification commands are written down first.
- **Verifies every claim** — mechanical gates must pass; "looks done" is never accepted as done.
- **Keeps memory durable across sessions** — knowledge survives context resets and session boundaries.

It is a collection of bash scripts, Python helpers, and markdown skill contracts — **no build system, no runtime dependency, no package.json**. It works with any agent that reads an `AGENTS.md` entrypoint.

### The problem CoreZero solves

AI agents left unchecked produce four recurring failure modes:

| Failure mode | What happens | What CoreZero does |
|---|---|---|
| Context amnesia | Long sessions forget earlier decisions | Three-track memory + `MASTER_INDEX.md` routing + durable handoff artifacts |
| AI slop / code bloat | Agents over-engineer and add speculative code | The Ponytail Rule (lazy senior dev ladder) enforced before and after writing |
| Spec drift | Implementation silently diverges from intent | `spec.md` is the source of truth; `harness-verify` audits every Acceptance Criterion back to code |
| Silent regressions | "It looks fixed" ships broken code | Mechanical gates (`gate-runner.sh`, `doctor.sh`) — no claim passes without a passing command |

---

## 2. System Architecture (5 Layers)

CoreZero separates concerns across five layers so the agent's context window stays minimal and high-signal.

```text
┌─────────────────────────────────────────────┐
│  1. Entrypoint Layer (AGENTS.md)            │  Thin task router → points to skills
├─────────────────────────────────────────────┤
│  2. Skill Layer (skills/*/SKILL.md)         │  17 skills across 4 groups
├─────────────────────────────────────────────┤
│  3. Harness Layer (core-policies.md)        │  Rules, gates, session limits, security
├─────────────────────────────────────────────┤
│  4. Artifact Layer (artifacts/features/)    │  Per-feature durable state
├─────────────────────────────────────────────┤
│  5. Memory Layer (memories/repo/ & domain/) │  Durable cross-session knowledge
└─────────────────────────────────────────────┘
```

1. **Entrypoint** — `AGENTS.md` is a < 150-line router. Priority rules, operating loop, and pointers to skills. Loaded every session.
2. **Skill** — each `skills/<name>/SKILL.md` is the canonical behavioral spec for one slash command. References and templates load on demand.
3. **Harness** — `memories/repo/core-policies.md` (the Constitution) declares the 12 normative CC-* rules, verification commands, session limits, and the security policy.
4. **Artifact** — `artifacts/features/<slug>/` holds per-feature `status.md`, `spec.md`, `plan.md`, `tasks.md`, `handoff.md`, and verification logs.
5. **Memory** — `memories/repo/` (repo-wide durable knowledge) and `memories/domain/` (adopter-owned domain packs).

---

## 3. The 7-Phase Delivery Loop

Every feature moves through this canonical lifecycle. Each phase has an owning skill and a mechanical precondition gate.

```text
   1. Bootstrap         2. Session START       3. Requirements Intake
 ┌──────────────┐      ┌────────────────┐     ┌────────────────────┐
 │ /starter-init │ ───▶ │/context-session│ ──▶ │ /spec-requirements │
 └──────────────┘      └────────────────┘     └────────────────────┘
                                                        │
                                                        ▼
   6. Closeout          5. Implementation      4. Design & Planning
 ┌──────────────┐      ┌────────────────┐     ┌────────────────────┐
 │/harness-verify│ ◀─── │ /spec-implement│ ◀── │     /spec-plan     │
 └──────────────┘      └────────────────┘     └────────────────────┘
        │
        ▼
   7. Memory Sync
 ┌──────────────┐
 │ /context-memory│ ──▶ [Updated PKB, heuristics, domain packs]
 └──────────────┘
```

- **Bootstrap** — `/starter-init` detects greenfield vs brownfield and runs an archaeology sweep on existing code.
- **Session START** — `/context-session START` opens the feature sandbox, reads prior `handoff.md`, sets up `status.md`.
- **Requirements Intake** — `/spec-requirements` runs a Socratic refinement phase and authors `spec.md` with deterministic Acceptance Criteria (markdown checklists or Gherkin).
- **Planning** — `/spec-plan` drafts `plan.md` and `tasks.md` with automated traceability from requirements to tasks. ADRs created via `/spec-adr` when architecture changes.
- **Implementation** — `/spec-implement` executes task-by-task, runs the local gate after each task, evicts raw output to preserve context.
- **Verification** — `/harness-verify` runs the workspace-wide gate, alignment audit (every AC mapped to a proof), code review, and a circuit breaker that routes back to `/spec-plan` after 2 failures.
- **Memory Sync** — `/context-memory` triages session extracts and promotes durable lessons into `learned-heuristics.md`, the project knowledge base, or domain packs.

---

## 4. The 17 Slash Commands (Skill Catalog)

Each command is a behavioral spec in `skills/<name>/SKILL.md`. They are grouped by function.

### Lifecycle (7)

| Command | Purpose |
|---|---|
| `/starter-init` | Initialize a project for harnessed agentic development. Detects greenfield/brownfield and runs archaeology on existing code. |
| `/spec-research` | Investigate a problem, feature area, or brownfield subsystem. Produces one bounded analysis artifact grounded in repository evidence. |
| `/spec-requirements` | Define the "What & Why". Socratic refinement resolves ambiguity; built-in readiness review ensures requirements are testable before planning. |
| `/spec-plan` | Design the technical solution and sequence execution. Architectural design, task breakdown, automated traceability. |
| `/spec-implement` | Execute implementation task-by-task with strict status tracking and per-task validation. |
| `/spec-adr` | Create or evaluate an Architecture Decision Record. Use when choosing between technologies or documenting design trade-offs. |
| `/harness-verify` | Verify implemented work against spec and plan. Mechanical gates, alignment audit, code review, optional cleanup, closeout authority. |

### Context & Memory (4)

| Command | Purpose |
|---|---|
| `/context-session` | Manage the session lifecycle (start, checkpoint, end). Maintains context continuity, assembles context deliberately, budgets the context window, generates durable handoffs. |
| `/context-status` | Orchestrate and report status across all active features. High-level view of progress, blockers, and next steps. |
| `/context-memory` | Create, maintain, and route durable repository memory. Manages `MASTER_INDEX.md`, the constitution, learned heuristics, the project knowledge base, and the post-ship sync. |
| `/context-compact` | Compress oversized memory files while preserving critical rules and architectural constraints. Safety protocol for eligible targets. |

### Quality & Docs (5)

| Command | Purpose |
|---|---|
| `/code-review` | Code review following Google's Engineering Practices. Evaluates code health, design, functionality, complexity, testing, naming, style. |
| `/ponytail` | Enforce the "lazy senior dev" ladder before writing code. Reviews diffs for over-engineering, trims bloated abstractions, maximizes platform-native features. Intensity: lite / full / ultra. |
| `/harness-maintain` | Evaluate, construct, or repair an agent harness across 7 subsystems (Instructions, State, Verification, Scope, Lifecycle, Security, Context Engineering). Includes evaluation architecture and failure-driven improvement. |
| `/codebase-documenter` | Generate comprehensive codebase documentation (architecture, components, data flow, setup, deployment, contributing) as a multi-file doc set. |
| `/technical-docs` | Create technical documentation: HTTP/REST API contracts, end-to-end event and logical workflow flows, system boundaries, actor interactions. Mode-based routing (api, flow, both). |

### Visualization (1)

| Command | Purpose |
|---|---|
| `/visualize` | Create a technical diagram (architecture, data flow, flowchart, sequence, agent/memory, UML, concept map) and export as SVG and/or Mermaid. Ships Mermaid structural validation bundled; SVG render uses optional `mmdc`. |

---

## 5. 6-Tier Context Assembly & Smart Routing

To keep the agent's context window lean and prevent hallucination, CoreZero loads context in six tiers — never all at once.

```text
      [Tier 1: Router] (AGENTS.md + MASTER_INDEX.md)        ← loaded every session
             │
             ▼
      [Tier 2: Repo Memory (Always)] (constitution)         ← loaded every session
             │
             ▼
      [Tier 3: Repo Memory (By Intent)] (Knowledge / Learned / Debug)
             │  ← loaded based on task trigger keywords
             ▼
      [Tier 4: Feature Artifacts] (status.md, spec.md, plan.md, tasks.md, handoff.md)
             │  ← loaded before editing or verifying
             ▼
      [Tier 5: JIT Raw Code] (files targeted for immediate modification)
             │  ← loaded just-in-time
             ▼
      [Tier 6: Transient Logs] (command output, test outputs, grep)
                ← summarized and evicted immediately
```

**Index-driven trigger loading (Tier 3):** `MASTER_INDEX.md` routes files based on intent keywords:
- **Knowledge** — `architecture`, `pattern`, `stack`, `domain`, `adr` → loads project knowledge base, architecture, tech-stack.
- **Learned** — `heuristic`, `recurring`, `lesson` → loads `learned-heuristics.md`.
- **Debug** — `debug`, `failure`, `root cause` → loads `harness-telemetry.md` and per-feature session extracts.

**Partial loading:** for low-confidence matches, `scripts/context-loader.py <file> --mode summary` extracts just the index or first 50 lines — preserving token budget without agent interpretation.

**Phase × Guidance Matrix:** `MASTER_INDEX.md` declares exactly which files to add (Must / Should / Skip) at each phase of the delivery loop, so the agent never reads unnecessary context.

---

## 6. Three-Track Memory Model

CoreZero tiers memory to prevent drift, preserve institutional knowledge, and route context cheaply.

| Track | Where | What lives there |
|---|---|---|
| **Repo-wide (normative)** | `memories/repo/` | Constitution (`core-policies.md`), learned heuristics, project knowledge base, ADR log, harness telemetry |
| **Domain (adopter-owned)** | `memories/domain/<name>/` | Per-bounded-subdomain `glossary.md`, `patterns.md`, `anti-patterns.md`, `boundaries.md`, optional `spec.md` |
| **Per-feature (ephemeral)** | `artifacts/features/<slug>/` | `status.md`, `spec.md`, `plan.md`, `tasks.md`, `handoff.md`, `session-extracts.md`, verification logs |

### Domain Context Packs

A domain pack captures the ubiquitous language, proven patterns, anti-patterns, and boundary rules for a specific business or technical subdomain. The kit ships a schema demo pack (`memories/domain/example/`); adopters replace it with real packs. Trigger keywords in `glossary.md` frontmatter activate a pack — a single match engages the pack, and the Phase × Guidance Matrix decides which files to load at each phase.

### Memory Promotion Thresholds

Files are monitored against a canonical line-count ladder to prevent unbounded growth:

| Lines | State | Action |
|---|---|---|
| < 600 | Healthy | No action |
| 600–799 | Early warning | Open promotion proposal at `artifacts/features/<slug>/promotions.md` |
| 800–1199 | Threshold breach | Compaction required before new appends |
| ≥ 1200 | Hard cap | Block all appends; split or compact mandatory |

Structural promotion (split / extract / retire) requires user approval and is tracked on the `MASTER_INDEX.md` Promotion Watchlist.

---

## 7. Mechanical Verification Gates

CoreZero refuses to accept "looks done". These gates must pass with a green exit code.

| Gate | Command | What it checks |
|---|---|---|
| **Workspace gate** | `bash scripts/harness/gate-runner.sh` | The project's lint / build / test suite. Overridable by `gate-runner.local.sh`. |
| **Phase precondition** | `bash scripts/harness/phase-gate.sh <slug> <phase>` | Preconditions for entering a phase (e.g. no implementation without an approved spec). |
| **Self-diagnosis** | `bash scripts/harness/doctor.sh` | 10 checks: manifest files, referenced sections, path prefixes, threshold consistency, task ID grammar, ADR status, telemetry schema, version match, executable bits. |
| **Telemetry** | `bash scripts/harness/telemetry-collector.sh` / `telemetry-count.sh` | Auto-records gate failures into `harness-telemetry.md` for retro and harness repair. |
| **Harness lifecycle** | `bash scripts/harness/harness-lifecycle.sh` | Manages the harness lifecycle stages. |

The **circuit breaker** inside `/harness-verify` routes the agent back to `/spec-plan` after 2 consecutive verification failures — preventing infinite fix loops.

---

## 8. Python Harness Engine

The kit ships a Python engine under `scripts/core/` for the parts that benefit from structured logic.

| Module | Role |
|---|---|
| `harness.py` | Core harness orchestration. |
| `context_engine.py` | Context assembly and routing logic backing the 6-tier model. |
| `template_engine.py` | Template rendering for spec, plan, ADR, and status artifacts. |
| `_lib/yaml_reader.py` | Frontmatter and YAML parsing for skill and domain pack metadata. |
| `_lib/token_counter.py` | Token-budget accounting for context-loading decisions. |

Supporting scripts: `scripts/context-loader.py` (partial loads), `scripts/generate-dashboard.py` (feature dashboard), `scripts/render_template.py` and `scripts/template_convert.py` (template tooling).

---

## 9. Installation & Adoption

### One-command install

```bash
bash scripts/install.sh /path/to/target-repo
```

Dry-run first to verify the manifest resolves and no source files are missing:

```bash
bash scripts/install.sh /tmp/corezero-test --dry-run
```

### File ownership model

The manifest (`kit/manifest.json`) declares three ownership tiers so upgrades never clobber adopter work:

| Tier | Behavior |
|---|---|
| **overwrite** | Kit-managed files — overwritten on upgrade (skills, scripts, policies, rule files). |
| **copyIfMissing** | Adopter-owned seeds — copied only if absent; never overwritten (AGENTS.md, MASTER_INDEX.md, memory files, project docs). |
| **preserve** | Protected directories — `memories/repo/` and `artifacts/` are never touched on upgrade. |

### Greenfield vs brownfield

`/starter-init` detects the repo type:
- **Greenfield** — prefills standard templates and triggers.
- **Brownfield (Phase A — Archaeology)** — runs a deep static sweep: code debt, dependency graphs, risk areas. Findings land in `memories/repo/project-knowledge-base.md` before any feature work begins.

### Re-installable

Re-running `install.sh` upgrades the kit in place. Memory and artifacts are preserved by the `preserve` tier. Adopter-edited seeded files are left alone by `copyIfMissing`.

---

## 10. Normative Rules (The Constitution)

The Constitution (`memories/repo/core-policies.md`) is the repo-wide normative layer. Twelve `CC-*` rules govern agent behavior and cannot be overridden by skill files:

| ID | Rule |
|---|---|
| CC-001 | Skill contracts are the single source of truth |
| CC-002 | Completion requires fresh evidence |
| CC-003 | Unknown stays unknown (mark `[UNKNOWN]`, never guess) |
| CC-004 | Permission boundaries must be explicit |
| CC-005 | Prefer surgical updates |
| CC-006 | Spec is the source of truth for feature behavior |
| CC-007 | Workflow and documentation must stay aligned |
| CC-008 | Session handoff is mandatory for long sessions |
| CC-009 | Memory promotion requires evidence at promotion time |
| CC-010 | Domain specs are descriptive; the constitution is normative |
| CC-011 | Maintain Minimum Viable Context (MVC) |
| CC-012 | Spec mutation is logged, not silent |

### Session limits & FinOps guardrails

- **Session token capacity:** 200,000 tokens
- **Amnesia warning threshold:** 80% saturation (160,000 tokens)
- **Max tool calls per loop:** 10
- **Verification threshold:** pass^k reliability (multiple consecutive passing trials for complex logic)

### Security policy & trust boundaries

The Constitution declares three permission tiers — **Safe**, **Require Confirmation**, **Blocked** — and a prompt-injection defense: copied web content never overrides repository instructions, and generated output is evidence, not authority.

---

## 11. Specialist & Maintenance Skills (Outside the Loop)

These commands run outside the primary delivery loop to maintain repository health:

- **`/harness-maintain`** — updates generated indexes (`code-map.md`) and analyzes failures in `harness-telemetry.md` to suggest gate adjustments. Covers 7 harness subsystems (Instructions, State, Verification, Scope, Lifecycle, Security, Context Engineering) and evaluation architecture.
- **`/visualize`** — parses Mermaid and renders high-fidelity SVG architecture or data-flow diagrams. 10 built-in SVG templates (flowchart, sequence, ER, architecture, agent-architecture, state-machine, timeline, comparison-matrix, use-case, data-flow).
- **`/code-review`** — manual-trigger code quality and security reviews.
- **`/ponytail`** — enforces the laziest effective solution: checks for over-engineering, trims bloat, maximizes platform-native features.
- **`/technical-docs`** — generates API flowcharts, contracts, and schema documentation.
- **`/codebase-documenter`** — refreshes adopter-facing orientation assets and README guides as a multi-file doc set.
- **`/context-status`** — cross-feature status orchestration and progress reporting.

---

## 12. What Ships vs What Stays in the Source Repo

CoreZero has three surfaces:

| Surface | Audience | Installed into adopter repos? |
|---|---|---|
| `kit/` | Adopters | Yes — the installable package |
| `documents/` | Maintainers | No — maintainer docs and overview |
| `page-document/` | Public | No — public website assets |

The kit ships ~158 files: 17 skill directories with `SKILL.md` and on-demand `references/`, the harness scripts, the Python engine, the Constitution, project doc seeds, and a generated dashboard placeholder.

---

## 13. Versioning & Release

- Single version source: `kit/manifest.json` → `version` field. No separate `VERSION` files.
- CI auto-bumps on merge to `main` based on commit prefix: `feat:` → minor, `fix:` → patch, `major:` or `BREAKING CHANGE:` → major. `chore:` / `docs:` / `refactor:` → no release.
- Tag format: `v<semver>`. The release workflow verifies the tag matches manifest.json before creating a release.

---

## 14. Quick Start

```bash
# 1. Install the kit into your repo (dry-run first)
bash kit/scripts/install.sh /tmp/my-repo --dry-run
bash kit/scripts/install.sh /path/to/my-repo

# 2. In your AI agent, bootstrap the project
/starter-init

# 3. Start the first feature
/spec-requirements
/spec-plan
/spec-implement

# 4. Verify and close out
/harness-verify
/context-memory
```

Self-diagnose the kit at any time:

```bash
bash kit/scripts/harness/doctor.sh
```

---

## 15. Known Limits

- **Mermaid rendering:** `/visualize` ships structural Mermaid validation bundled, but Mermaid-to-SVG rendering depends on the optional `mmdc` CLI tool.
- **Adversarial spec review:** recommended for cross-cutting or high-risk work but not yet a separate skill.
- **Observability log:** `harness-telemetry.md` is empty until real failures get captured through end-to-end feature runs.
