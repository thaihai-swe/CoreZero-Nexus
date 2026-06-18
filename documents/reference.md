# Technical Reference

This reference catalog details the public commands, feature artifact schemas, repository memory files, and configuration templates in the CoreZero Nexus.

---

## 1. Command Reference Table

| Command | Subsystem | Customer Value / Purpose | Key Artifacts |
|---|---|---|---|
| `/starter-init` | Project Starter | Configures verification baselines; sweeps legacy code (Phase A) automatically on brownfield repos | `core-policies.md`, `HARNESS_CARD.md`, `brownfield-map.md`, `dependency-graph.md` |
| `/context-session` | Context | Minimizes token costs and prevents LLM context fatigue | `handoff.md`, `session-extracts.md` |
| `/context-status` | Context | Monitors feature progression and flags implementation blockers | `progress.md` |
| `/context-memory` | Context | Updates shared conventions so the agent gets smarter over time | `core-policies.md`, `learned-heuristics.md` |
| `/spec-research` | SDD | Investigates codebase boundaries before specifying requirements | `analysis.md` |
| `/spec-requirements`| SDD | Locks down Socratic specifications and acceptance criteria | `spec.md`, `proposal.md` |
| `/spec-adr` | SDD | Documents structural decisions and alternatives formally | `adr-NNN.md`, `adr-log.md` |
| `/spec-plan` | SDD | Maps designs to micro-tasks with dedicated proof commands | `plan.md`, `tasks.md` |
| `/spec-implement` | SDD | Implements code surgically task-by-task with pre-change proofs | Touches target source files |
| `/harness-verify` | Harness | Performs mechanical build gates and spec alignment audits | `review.md`, `testing-scenarios.md` |
| `/harness-maintain` | Harness | Evaluates and improves harness rules based on logged errors | `harness-telemetry.md` |
| `/code-review` | Specialist | Audits code health against Google's Engineering Practices | Integrated reviews in `review.md` |
| `/visualize` | Specialist | Generates visual SVG/Mermaid flowcharts and class diagrams | `.svg`, `.mermaid` |
| `/codebase-documenter`| Specialist | Compiles complete technical onboarding guides for new teams | `README.md`, `CONTRIBUTING.md` |
| `/technical-docs` | Specialist | Compiles API contracts (`--mode api`) and/or system flows (`--mode flow`/`both`) | `api-docs.md`, `flows.md`, `technical-docs.md` |

---

## 2. Feature Artifact Schemas (`artifacts/features/<slug>/`)

| File | Public Owner | Purpose |
|------|-------------|---------|
| `status.md` | Multiple | Phase tracking, delivery profile |
| `analysis.md` | `/spec-research` | Investigation findings |
| `proposal.md` | `/spec-requirements` | High-level alignment |
| `spec.md` | `/spec-requirements` | Locked requirements + AC |
| `requirements-review.md` | `/spec-requirements` | Readiness gate |
| `design.md` | `/spec-plan` | Technical design when needed |
| `plan.md` | `/spec-plan` | Execution strategy + mechanical gate |
| `tasks.md` | `/spec-plan` / `/spec-implement` | Task breakdown + evidence |
| `review.md` | `/harness-verify` | Verification verdict |
| `testing-scenarios.md` | `/harness-verify` | Manual test guide |
| `progress.md` | `/context-session` | Session log |
| `handoff.md` | `/context-session` | Continuity artifact |
| `session-extracts.md` | `/context-session` / `/harness-verify` | Extracted-tier memory candidates |
| `harness-assessment.md` | `/harness-maintain` | Harness evaluation |
| `eval-report.md` | `/harness-maintain` | Evaluator findings |
| `adr-*.md` | `/spec-adr` | Architecture decisions |

---

## 3. Memory Files (`memories/repo/`)

The memory layer is structured in a **3-Tier Memory Architecture**:
- **Instruction tier** (human-curated): constitution, security-policy, learned-heuristics, project-knowledge-base, harness-config, and `docs/project/architecture.md`.
- **Auto tier** (agent-written): observability-log.
- **Extracted tier** (per-feature candidates): session-extracts.

| File | Public Owner | Type | Tier | Lifecycle |
|------|-------------|------|------|-----------|
| [`INDEX.md`](../kit/memories/repo/INDEX.md) | `/starter-init` / `/context-memory` | Router | N/A | Created at init, declares Always/By-Intent/By-Debug groups |
| [`core-policies.md`](../kit/memories/repo/core-policies.md) | `/context-memory` | Normative | Instruction | Created at init |
| [`security-policy.md`](../kit/memories/repo/security-policy.md) | `/context-memory` | Normative | Instruction | Created at init |
| [`learned-heuristics.md`](../kit/memories/repo/learned-heuristics.md) | `/context-memory` | Descriptive | Instruction | Created at init |
| [`project-knowledge-base.md`](../kit/memories/repo/project-knowledge-base.md) | `/context-memory` | Descriptive | Instruction | Created at init |
| [`core-policies.md`](../kit/memories/repo/core-policies.md) | `/starter-init` | Operational | Instruction | Created at init |
| [`harness-telemetry.md`](../kit/memories/repo/harness-telemetry.md) | `/harness-maintain` | Operational | Auto | Created at init, written by Improve Mode |
| [`adr-log.md`](../kit/memories/repo/adr-log.md) | `/spec-adr` | Registry | Instruction | Lazy-created on first ADR |

---

## 4. Shipped Adopter-Owned Docs (`docs/project/*.md`)

These docs are copied to adopter repositories for customization:

| File | Purpose | Primary Public Consumers |
|------|---------|--------------------------|
| [`project/product-sense.md`](../kit/docs/project/product-sense.md) | Product vision, users, metrics | `/spec-requirements`, `/spec-research` |
| [`project/project-constraints.md`](../kit/docs/project/project-constraints.md) | Budgets, compliance, security | `/spec-requirements`, `/harness-verify` |
| [`project/glossary.md`](../kit/docs/project/glossary.md) | Shared vocabulary | `/spec-requirements`, `/spec-implement` |
| [`project/tech-stack-reference.md`](../kit/docs/project/tech-stack-reference.md) | Dependencies, APIs, tools | `/spec-research`, `/spec-plan` |

---

## 5. Kit-Managed Policy Doc

| File | Purpose | Primary Public Consumers |
|------|---------|--------------------------|
| [`policies/code-design.md`](../kit/docs/policies/code-design.md) | Normative coding-policy guidance | `/spec-plan`, `/spec-implement`, `/harness-verify` |

---

## 6. Provenance & Heritage

The `/visualize` command (`skills/visualize/`) is adapted from the upstream repository [`yizhiyanhua-ai/fireworks-tech-graph`](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) and upgraded to support polished SVG template generation, text/border styling configurations, and automated Mermaid diagram syntax validation.
