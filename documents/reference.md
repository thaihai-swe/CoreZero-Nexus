# Technical Reference

This reference catalog details the public commands, feature artifact schemas, repository memory files, and configuration templates in the CoreZero.

---

## 1. Command Reference Table

| Command                  | Subsystem       | Customer Value / Purpose                                                                                                                                                        | Key Artifacts                                                            |
| ------------------------ | --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| `/starter-init`          | Project Starter | Configures verification baselines; sweeps legacy code (Phase A) automatically on brownfield repos                                                                               | `core-policies.md`, `project-knowledge-base.md`, `learned-heuristics.md` |
| `/context-session`       | Context         | Minimizes token costs and prevents LLM context fatigue                                                                                                                          | `handoff.md`, `session-extracts.md`                                      |
| `/context-status`        | Context         | Monitors feature progression and flags implementation blockers                                                                                                                  | `progress.md`                                                            |
| `/context-memory`        | Context         | Updates shared conventions so the agent gets smarter over time                                                                                                                  | `core-policies.md`, `learned-heuristics.md`                              |
| `/spec-research`         | SDD             | Investigates codebase boundaries before specifying requirements                                                                                                                 | `analysis.md`                                                            |
| `/spec-requirements`     | SDD             | Locks down Socratic specifications and acceptance criteria                                                                                                                      | `spec.md`, `proposal.md`                                                 |
| `/spec-adr`              | SDD             | Documents structural decisions and alternatives formally                                                                                                                        | `adr-NNN.md`, `adr-log.md`                                               |
| `/spec-plan`             | SDD             | Maps designs to micro-tasks with dedicated proof commands                                                                                                                       | `plan.md`, `tasks.md`                                                    |
| `/spec-implement`        | SDD             | Implements code surgically task-by-task with pre-change proofs                                                                                                                  | Touches target source files                                              |
| `/harness-verify`        | Harness         | Performs mechanical build gates and spec alignment audits                                                                                                                       | `review.md`                                                              |
| `/harness-maintain`      | Harness         | Evaluates and improves harness rules based on logged errors                                                                                                                     | `harness-telemetry.md`                                                   |
| `/code-review`           | Specialist      | Audits code health against Google's Engineering Practices                                                                                                                       | Integrated reviews in `review.md`                                        |
| `/ponytail`              | Specialist      | Enforces the laziest effective solution — checks for over-engineering, trims bloat, maximises platform-native features. Supports lite / full (default) / ultra intensity levels | (no artifacts — advisory mode)                                           |
| `/context-compact`       | Context         | Compact oversized memory files (thresholds: 100-line early warning, 200-line breach, 3200-line hard cap). Preserves all normative identifiers with pre/post safety protocol     | Compacted target file under `core-zero/memories/` or `artifacts/`        |
| `/visualize`             | Specialist      | Generates visual SVG/Mermaid flowcharts and class diagrams                                                                                                                      | `.svg`, `.mermaid`                                                       |
| `/codebase-documenter`   | Specialist      | Compiles complete technical onboarding guides for new teams                                                                                                                     | `README.md`, `CONTRIBUTING.md`                                           |
| `/technical-docs`        | Specialist      | Compiles API contracts (`--mode api`) and/or system flows (`--mode flow`/`both`)                                                                                                | `api-docs.md`, `flows.md`, `technical-docs.md`                           |
| `/spec-testing-scenario` | SDD             | Drafts manual testing scenarios guide (optional)                                                                                                                                | `testing-scenarios.md`                                                   |

---

## 2. Feature Artifact Schemas (`artifacts/features/<slug>/`)

| File                     | Public Owner                           | Purpose                               |
| ------------------------ | -------------------------------------- | ------------------------------------- |
| `status.md`              | Multiple                               | Phase tracking, delivery profile      |
| `analysis.md`            | `/spec-research`                       | Investigation findings                |
| `proposal.md`            | `/spec-requirements`                   | High-level alignment                  |
| `spec.md`                | `/spec-requirements`                   | Locked requirements + AC              |
| `requirements-review.md` | `/spec-requirements`                   | Conditional readiness gate            |
| `plan.md`                | `/spec-plan`                           | Technical design + execution strategy |
| `tasks.md`               | `/spec-plan` / `/spec-implement`       | Task breakdown + evidence             |
| `review.md`              | `/harness-verify`                      | Verification verdict                  |
| `testing-scenarios.md`   | `/spec-testing-scenario`               | Manual test guide (optional)          |
| `progress.md`            | `/context-session`                     | Session log                           |
| `handoff.md`             | `/context-session`                     | Continuity artifact                   |
| `session-extracts.md`    | `/context-session` / `/harness-verify` | Extracted-tier memory candidates      |
| `harness-assessment.md`  | `/harness-maintain`                    | Harness evaluation                    |
| `eval-report.md`         | `/harness-maintain`                    | Evaluator findings                    |
| `adr-*.md`               | `/spec-adr`                            | Architecture decisions                |

---

## 3. Memory Files (`core-zero/memories/repo/`)

The memory layer is structured in a **3-Tier Memory Architecture**:
- **Instruction tier** (human-curated): constitution, learned-heuristics, project-knowledge-base, and `core-zero/project/architecture.md`.
- **Auto tier** (agent-written): harness-telemetry.
- **Extracted tier** (per-feature candidates): session-extracts.

| File                                                                                    | Public Owner                        | Type        | Tier        | Lifecycle                                                  |
| --------------------------------------------------------------------------------------- | ----------------------------------- | ----------- | ----------- | ---------------------------------------------------------- |
| [`MASTER_INDEX.md`](../kit/MASTER_INDEX.md)                                             | `/starter-init` / `/context-memory` | Router      | N/A         | Created at init, declares Always/By-Intent/By-Debug groups |
| [`core-policies.md`](../kit/core-zero/memories/repo/core-policies.md)                   | `/starter-init` / `/context-memory` | Normative   | Instruction | Created at init                                            |
| [`learned-heuristics.md`](../kit/core-zero/memories/repo/learned-heuristics.md)         | `/context-memory`                   | Descriptive | Instruction | Created at init                                            |
| [`project-knowledge-base.md`](../kit/core-zero/memories/repo/project-knowledge-base.md) | `/context-memory`                   | Descriptive | Instruction | Created at init                                            |
| [`harness-telemetry.md`](../kit/core-zero/memories/repo/harness-telemetry.md)           | `/harness-maintain`                 | Operational | Auto        | Created at init, written by Improve Mode                   |
| [`adr-log.md`](../kit/core-zero/memories/repo/adr-log.md)                               | `/spec-adr`                         | Registry    | Instruction | Lazy-created on first ADR                                  |

---

## 4. Shipped Adopter-Owned Docs (`core-zero/project/`)

These docs are copied to adopter repositories for customization (`copyIfMissing`):

| File                                                                                | Purpose                                                       | Primary Public Consumers                 |
| ----------------------------------------------------------------------------------- | ------------------------------------------------------------- | ---------------------------------------- |
| [`project/architecture.md`](../kit/core-zero/project/architecture.md)               | System structure, component boundaries                        | `/spec-research`, `/spec-plan`           |
| [`project/code-map.md`](../kit/core-zero/project/code-map.md)                       | Codebase map, module index                                    | `/spec-research`, `/spec-implement`      |
| [`project/agent-capabilities.md`](../kit/core-zero/project/agent-capabilities.md)   | Agent capability inventory                                    | `/harness-maintain`, `/starter-init`     |
| [`project/code-intelligence.md`](../kit/core-zero/project/code-intelligence.md)     | Code intelligence provider config + capability intent mapping | `/starter-init`, all CI-consuming skills |
| [`project/product-sense.md`](../kit/core-zero/project/product-sense.md)             | Product vision, users, metrics                                | `/spec-requirements`, `/spec-research`   |
| [`project/project-constraints.md`](../kit/core-zero/project/project-constraints.md) | Budgets, compliance, security                                 | `/spec-requirements`, `/harness-verify`  |
| [`project/glossary.md`](../kit/core-zero/project/glossary.md)                       | Shared vocabulary                                             | `/spec-requirements`, `/spec-implement`  |
| [`project/tech-stack.md`](../kit/core-zero/project/tech-stack.md)                   | Dependencies, APIs, tools                                     | `/spec-research`, `/spec-plan`           |

### Shipped Config (`overwrite`)

| File                                                                          | Purpose                          | Consumers                     |
| ----------------------------------------------------------------------------- | -------------------------------- | ----------------------------- |
| [`project/harness-config.yaml`](../kit/core-zero/project/harness-config.yaml) | Phase precondition configuration | `harness.py`, `phase-gate.sh` |
| [`project/spec-schema.json`](../kit/core-zero/project/spec-schema.json)       | Spec validation JSON schema      | —                             |
| [`project/adr/index.md`](../kit/core-zero/project/adr/index.md)               | ADR log registry                 | `/spec-adr`                   |
| [`project/adr/0001-example.md`](../kit/core-zero/project/adr/0001-example.md) | Example ADR template             | `/spec-adr`                   |

---

## 5. Kit-Managed Policy Doc

| File                                                                  | Purpose                          | Primary Public Consumers                           |
| --------------------------------------------------------------------- | -------------------------------- | -------------------------------------------------- |
| [`policies/code-design.md`](../kit/core-zero/policies/code-design.md) | Normative coding-policy guidance | `/spec-plan`, `/spec-implement`, `/harness-verify` |

---

## 6. Provenance & Heritage

The `/visualize` command (`skills/visualize/`) is adapted from the upstream repository [`yizhiyanhua-ai/fireworks-tech-graph`](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) and upgraded to support polished SVG template generation, text/border styling configurations, and automated Mermaid diagram syntax validation.
