# Technical Reference

This reference catalog details the public commands, feature artifact schemas, repository memory files, and configuration templates in the CoreZero Nexus.

---

## 1. Command Reference Table

| Command | Subsystem | Customer Value / Purpose | Key Artifacts |
|---|---|---|---|
| `/brownfield-init` | Project Starter | Sweeps legacy code to locate risks before changing it | `brownfield-map.md`, `dependency-graph.md` |
| `/starter-init` | Project Starter | Configures linter, build, and test verification baselines | `harness-config.md`, `HARNESS_CARD.md` |
| `/context-session` | Context | Minimizes token costs and prevents LLM context fatigue | `handoff.md`, `session-extracts.md` |
| `/context-status` | Context | Monitors feature progression and flags implementation blockers | `progress.md` |
| `/context-memory` | Context | Updates shared conventions so the agent gets smarter over time | `constitution.md`, `learned-heuristics.md` |
| `/spec-research` | SDD | Investigates codebase boundaries before specifying requirements | `analysis.md` |
| `/spec-requirements`| SDD | Locks down Socratic specifications and acceptance criteria | `spec.md`, `proposal.md` |
| `/spec-adr` | SDD | Documents structural decisions and alternatives formally | `adr-NNN.md`, `adr-log.md` |
| `/spec-plan` | SDD | Maps designs to micro-tasks with dedicated proof commands | `plan.md`, `tasks.md` |
| `/spec-implement` | SDD | Implements code surgically task-by-task with pre-change proofs | Touches target source files |
| `/harness-verify` | Harness | Performs mechanical build gates and spec alignment audits | `review.md`, `testing-scenarios.md` |
| `/harness-maintain` | Harness | Evaluates and improves harness rules based on logged errors | `observability-log.md` |
| `/code-review` | Specialist | Audits code health against Google's Engineering Practices | Integrated reviews in `review.md` |
| `/visualize` | Specialist | Generates visual SVG/Mermaid flowcharts and class diagrams | `.svg`, `.mermaid` |
| `/codebase-documenter`| Specialist | Compiles complete technical onboarding guides for new teams | `README.md`, `CONTRIBUTING.md` |
| `/system-flow-docs` | Specialist | Explains multi-component interactions and workflow paths | Workflow documentation logs |
| `/api-endpoint-docs` | Specialist | Generates exact, machine-readable HTTP contract specs | API contract documentation |

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
- **Instruction tier** (human-curated): constitution, security-policy, learned-heuristics, project-knowledge-base, domain-specs, harness-config, and `docs/architecture.md`.
- **Auto tier** (agent-written): observability-log.
- **Extracted tier** (per-feature candidates): session-extracts.

| File | Public Owner | Type | Tier | Lifecycle |
|------|-------------|------|------|-----------|
| [`INDEX.md`](../kit/memories/repo/INDEX.md) | `/starter-init` / `/context-memory` | Router | N/A | Created at init, declares Always/By-Intent/By-Debug groups |
| [`constitution.md`](../kit/memories/repo/constitution.md) | `/context-memory` | Normative | Instruction | Created at init |
| [`security-policy.md`](../kit/memories/repo/security-policy.md) | `/context-memory` | Normative | Instruction | Created at init |
| [`learned-heuristics.md`](../kit/memories/repo/learned-heuristics.md) | `/context-memory` | Descriptive | Instruction | Created at init |
| [`project-knowledge-base.md`](../kit/memories/repo/project-knowledge-base.md) | `/context-memory` | Descriptive | Instruction | Created at init |
| [`harness-config.md`](../kit/memories/repo/harness-config.md) | `/starter-init` | Operational | Instruction | Created at init |
| [`domain-specs.md`](../kit/memories/repo/domain-specs.md) | `/context-memory` | Descriptive | Instruction | Created at init |
| [`observability-log.md`](../kit/memories/repo/observability-log.md) | `/harness-maintain` | Operational | Auto | Created at init, written by Improve Mode |
| [`adr-log.md`](../kit/memories/repo/adr-log.md) | `/spec-adr` | Registry | Instruction | Lazy-created on first ADR |

---

## 4. Shipped Adopter-Owned Docs (`docs/*.md`)

These docs are copied to adopter repositories for customization:

| File | Purpose | Primary Public Consumers |
|------|---------|--------------------------|
| [`PRODUCT_SENSE.md`](../kit/docs/PRODUCT_SENSE.md) | Product vision, users, metrics | `/spec-requirements`, `/spec-research` |
| [`PROJECT_CONSTRAINTS.md`](../kit/docs/PROJECT_CONSTRAINTS.md) | Budgets, compliance, security | `/spec-requirements`, `/harness-verify` |
| [`GLOSSARY.md`](../kit/docs/GLOSSARY.md) | Shared vocabulary | `/spec-requirements`, `/spec-implement` |
| [`TECH_STACK_REFERENCE.md`](../kit/docs/TECH_STACK_REFERENCE.md) | Dependencies, APIs, tools | `/spec-research`, `/spec-plan` |
| [`GOVERNANCE.md`](../kit/docs/GOVERNANCE.md) | Approval gates, ownership | `/spec-requirements`, `/harness-verify` |
| [`RELIABILITY_POLICY.md`](../kit/docs/RELIABILITY_POLICY.md) | SLOs, incident response | `/harness-verify`, `/spec-plan` |
| [`QUALITY_POLICY.md`](../kit/docs/QUALITY_POLICY.md) | Quality gates, review standards | `/harness-verify`, `/spec-plan` |
| [`TECH_DEBT_REGISTER.md`](../kit/docs/TECH_DEBT_REGISTER.md) | Tracked debt items | `/harness-verify` |


---

## 5. Provenance & Heritage

The `/visualize` command (`skills/visualize/`) is adapted from the upstream repository [`yizhiyanhua-ai/fireworks-tech-graph`](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) and upgraded to support polished SVG template generation, text/border styling configurations, and automated Mermaid diagram syntax validation.
