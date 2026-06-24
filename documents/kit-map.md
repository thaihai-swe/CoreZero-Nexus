# CoreZero Kit Map

This guide explains what the kit is, how its folders fit together, and which commands belong to the normal delivery path.

## What The Kit Is

CoreZero is an installable AI software delivery framework. It is copied into an adopter repository so agents have a shared operating model for context loading, requirements, planning, implementation, verification, and durable memory.

The kit is not a single application. It is a repo-local harness made of instructions, skills, memory files, docs, and helper scripts.

## The Kit Layers

### Core Delivery

Use this path for normal feature work:

`/starter-init` -> `/spec-research` or `/spec-requirements` -> `/spec-plan` -> `/spec-implement` -> `/code-review` -> `/harness-verify`

- `/starter-init` prepares the adopter repo for harnessed work.
- `/spec-research` maps unknown or brownfield behavior before requirements are locked.
- `/spec-requirements` defines the feature contract.
- `/spec-plan` turns the contract into a design and task sequence.
- `/spec-implement` performs the planned implementation.
- `/code-review` performs an adversarial or constructive code review against policies and spec.
- `/harness-verify` proves the work against the spec, plan, and available checks.
- `/ponytail` modifies agent behavior to force the simplest, laziest working solution.

### Session And Memory

Use this layer to keep long-running work coherent:

- `/context-session START` resumes an existing feature slug by loading routed memory, prior handoff, progress, and current feature artifacts.
- `/context-session CHECKPOINT` records a pause point while the work is still in progress.
- `/context-session END` closes a long session by producing handoff/progress context and candidate memory extracts.
- `/context-memory` triages session extracts and promotes only evidence-backed lessons into durable memory.
- `/context-compact` compresses oversized memory files when context is getting too heavy.

`context-session END` is mentioned often because closing work cleanly is what prevents chat history from becoming the only source of truth. It is not the only context-session mode.

### Governance

Use this layer to understand or repair the harness itself:

- `/context-status` reports feature status, blockers, claims, and next recommended commands.
- `/harness-maintain` evaluates or repairs the harness, indexes, generated references, and observability loops.
- `/spec-adr` records non-obvious architecture decisions.

### Documentation And Visualization

Use this layer when the repo needs durable explanation:

- `/technical-docs` writes feature-scoped API or workflow documentation.
- `/codebase-documenter` writes broader codebase documentation.
- `/visualize` creates Mermaid or SVG diagrams when a picture is clearer than prose.

## What Each Folder Means

| Folder | Owner | Purpose |
|---|---|---|
| `skills/` | Kit-managed | Slash-command contracts and references. |
| `scripts/` | Kit-managed | Installer, context loader, template renderer, engine layer (`core/`: context engine, harness engine, spec validator, template engine), verification harness (`harness/`: gate runner, telemetry, phase gates, readiness, traceability). |
| `docs/rules/` | Kit-managed | Language and security rules. |
| `docs/policies/` | Kit-managed | Cross-cutting code design and architectural policies. |
| `docs/project/` | Adopter-owned seed | Project facts the adopter fills in and maintains. |
| `docs/generated/` | Adopter-owned seed | Generated dashboard output (`dashboard.html`). |
| `memories/repo/` | Adopter-owned seed | Durable memory, policies, heuristics, and telemetry. |
| `memories/domain/` | Adopter-owned seed | Domain pack templates to replace with project-specific knowledge. |
| `artifacts/features/` | Adopter-owned state | Per-feature specs, plans, tasks, status, reviews, handoffs. |

## Install Ownership Rules

The manifest divides files into three behaviors:

- `overwrite`: kit-managed files. Re-running the installer upgrades them.
- `copyIfMissing`: adopter-owned seeds. The installer creates them once and then preserves local edits.
- `preserve`: adopter state directories that upgrades must not overwrite.

When in doubt, check `manifest.json` before editing a file as part of a kit upgrade.

## Which Command Should I Use?

| Situation | Command |
|---|---|
| Installing the kit into a repo | `scripts/install.sh <target_dir>` |
| First time in an adopter repo | `/starter-init` |
| Need to understand existing behavior first | `/spec-research` |
| Ready to define a feature | `/spec-requirements` |
| Requirements are approved | `/spec-plan` |
| Plan and tasks are ready | `/spec-implement` |
| Ready to review completed code | `/code-review` |
| Work appears complete | `/harness-verify` |
| Resuming an existing feature | `/context-session START` |
| Pausing but not done | `/context-session CHECKPOINT` |
| Ending a long session | `/context-session END` |
| Memory files are too large | `/context-compact` |
| Need project-wide status | `/context-status` |
| Need to repair or evaluate the harness | `/harness-maintain` |
| Need to document an architectural decision | `/spec-adr` |
| Need the simplest, laziest working solution | `/ponytail` |
| Need durable API or flow docs | `/technical-docs` |
| Need broader repo documentation | `/codebase-documenter` |
| Need a diagram | `/visualize` |

## Common Confusions

- The core delivery path does not include every skill. It includes the minimum commands required to ship a feature safely.
- `/context-session` is not a feature-start command. Use it after a feature slug and `status.md` already exist.
- `/context-memory` is not a general note-taking command. It promotes evidence-backed lessons after verification or session close.
- Generated files are not current truth until regenerated in the adopter repo.
