# End-to-End Tutorial

This tutorial explains the full CoreZero skill flow from install to closeout. It covers all 16 shipped skills, their modes, and whether each skill is required, conditional, optional, or maintenance-only.

CoreZero has one required feature-delivery spine. The other skills are supporting branches for session continuity, memory health, governance, documentation, diagrams, and harness repair.

---

## 1. Full Skill System

### Required-vs-Optional Legend

| Label | Meaning |
|---|---|
| Required once per repo | Run during initial adopter setup. |
| Required per feature | Run for every feature that moves through the delivery lifecycle. |
| Conditional | Run when the stated condition applies. |
| Optional helper | Use when it improves clarity, documentation, review depth, or operator visibility. |
| Maintenance-only | Use when maintaining or repairing the harness itself. |

### Five Skill Bands

```mermaid
flowchart TD
    Install[Install kit] --> Starter["/starter-init<br/>Required once per repo"]

    Starter --> Intake{"Feature behavior known?"}
    Intake -->|"No, brownfield, unknown, or Complex"| Research["/spec-research<br/>Conditional"]
    Intake -->|"Yes"| Requirements["/spec-requirements<br/>Required per feature"]
    Research --> Requirements

    Requirements --> ADR{"Architecture decision needed?"}
    ADR -->|"Yes"| SpecADR["/spec-adr<br/>Conditional"]
    ADR -->|"No"| Plan["/spec-plan<br/>Required per feature"]
    SpecADR --> Plan

    Plan --> Implement["/spec-implement<br/>Required per feature"]
    Implement --> Verify["/harness-verify<br/>Required per feature"]
    Verify --> Memory["/context-memory<br/>Conditional post-ship sync"]
    Verify --> Done[Done]
    Memory --> Done

    subgraph SessionMemory["Session + Memory"]
        SessionStart["/context-session START"]
        SessionCheckpoint["/context-session CHECKPOINT"]
        SessionEnd["/context-session END"]
        Compact["/context-compact"]
    end

    subgraph Governance["Governance + Verification"]
        Status["/context-status"]
        Maintain["/harness-maintain"]
        Review["/code-review"]
    end

    subgraph DocsViz["Docs + Visualization"]
        TechDocs["/technical-docs"]
        CodebaseDocs["/codebase-documenter"]
        Visualize["/visualize"]
    end

    SessionStart -. "resume existing feature" .-> Requirements
    Implement -. "pause" .-> SessionCheckpoint
    Done -. "long-session closeout" .-> SessionEnd
    Verify -. "review branch" .-> Review
    Requirements -. "system structure affected" .-> Visualize
    Plan -. "docs needed" .-> TechDocs
    Done -. "repo docs needed" .-> CodebaseDocs
    Done -. "status view" .-> Status
    Verify -. "harness changed or drift found" .-> Maintain
    Memory -. "oversized memory" .-> Compact
```

### Required Feature Path

The normal delivery spine is:

```text
/starter-init
/spec-research      # required when behavior is unknown, brownfield, or Complex
/spec-requirements
/spec-plan
/spec-implement
/harness-verify
```

The support skills are real shipped skills, but they are not all mandatory for every feature. Their use depends on risk, feature profile, session length, documentation needs, and whether the harness itself is changing.

---

## 2. Command Matrix

| Skill | Required? | Modes | Use when | Primary artifacts |
|---|---|---|---|---|
| [`/starter-init`](../kit/skills/starter-init/SKILL.md) | Required once per repo | Greenfield path, brownfield path | First setup after installation | `docs/`, `memories/`, `.gitignore`, project memory seeds |
| [`/spec-research`](../kit/skills/spec-research/SKILL.md) | Conditional | Research analysis | Behavior is unknown, repo is brownfield, or root cause is unclear | `artifacts/features/<slug>/analysis.md`, `status.md` |
| [`/spec-requirements`](../kit/skills/spec-requirements/SKILL.md) | Required per feature | Requirements authoring | Define what must be built and how it will be accepted | `spec.md`, `status.md` |
| [`/spec-plan`](../kit/skills/spec-plan/SKILL.md) | Required per feature | Planning | Convert approved requirements into design and tasks | `plan.md`, `tasks.md`, `status.md` |
| [`/spec-implement`](../kit/skills/spec-implement/SKILL.md) | Required per feature | Task execution | Implement approved tasks one at a time | Source changes, `tasks.md`, `status.md`, telemetry on failures |
| [`/harness-verify`](../kit/skills/harness-verify/SKILL.md) | Required per feature | Verification | Prove implementation against tasks and spec | `status.md`, verification output, `harness-telemetry.md` |
| [`/context-session`](../kit/skills/context-session/SKILL.md) | Conditional | `START`, `CHECKPOINT`, `END` | Resume, pause, or close long feature sessions | `progress.md`, `handoff.md`, `session-extracts.md`, optional `claim.md` |
| [`/context-memory`](../kit/skills/context-memory/SKILL.md) | Conditional | Regular update, `--audit` | Promote evidence-backed lessons or audit memory health | `memories/repo/*`, `memory-audit.md` |
| [`/context-compact`](../kit/skills/context-compact/SKILL.md) | Conditional | Target-file compaction | Memory files are oversized or context is too heavy | Compacted target under `memories/repo/` |
| [`/context-status`](../kit/skills/context-status/SKILL.md) | Optional helper | Status/dashboard sync | Need project-wide feature visibility or next commands | Status report, `docs/generated/dashboard.html` |
| [`/harness-maintain`](../kit/skills/harness-maintain/SKILL.md) | Maintenance-only | `assess`, `create`, `improve`, `eval`, `doctor` | Harness indexes, generated references, or governance loops need repair | `docs/generated/codemap.md`, eval reports |
| [`/spec-adr`](../kit/skills/spec-adr/SKILL.md) | Conditional | ADR capture | A non-obvious technical decision is locked | ADR entry, `docs/project/architecture.md`, `memories/repo/adr-log.md` where applicable |
| [`/code-review`](../kit/skills/code-review/SKILL.md) | Optional helper | Review | Manual review is requested or verification calls for deeper review | Review findings, usually feature-scoped |
| [`/ponytail`](../kit/skills/ponytail/SKILL.md) | Optional helper | `lite`, `full` (default), `ultra` | Simplicity check — enforce YAGNI, trim bloat, prefer platform-native features | Advisory — no artifacts |
| [`/technical-docs`](../kit/skills/technical-docs/SKILL.md) | Optional helper | `--mode api`, `--mode flow`, `--mode both` | Need grounded API docs or end-to-end flow docs | API docs, flow docs, technical narratives |
| [`/codebase-documenter`](../kit/skills/codebase-documenter/SKILL.md) | Optional helper | Codebase documentation | Need broader repo onboarding or architecture documentation | README-style guides, architecture docs, setup docs |
| [`/visualize`](../kit/skills/visualize/SKILL.md) | Optional helper, conditional for complex structure work | SVG, Mermaid, optional Mermaid render with `mmdc` | A diagram clarifies architecture, flow, sequence, state, ER, or agent/memory structure | `.svg`, `.mmd`, validated diagram artifacts |

---

## 3. Ceremony Scaling — How Much Rigor Runs

The agent scales ceremony based on the risk, scope, and complexity of each feature. There is no separate rigor-profiles configuration file — the agent detects the appropriate level by reading the task, the repo state, and the spec.

| Scale | What runs |
|---|---|
| Tiny | Minimal requirements, lean plan, implementation, and focused verification. Usually skips `/spec-research`, `/spec-adr`, and `/visualize` unless explicitly requested. |
| Standard | Normal feature flow. Research runs if the codebase is unfamiliar. ADRs and diagrams are optional and used when they clarify real decisions or boundaries. |
| Complex | Strongest ceremony. Research is required, ADRs are required for locked technical choices, diagrams are required when system structure changes, verification is deeper, and harness changes require `/harness-maintain eval`. |

The canonical feature phases are defined in [`kit/skills/_shared/status-phases.md`](../kit/skills/_shared/status-phases.md). Core phases move forward through `Researching`, `Spec Approved`, `Plan Approved`, `Implementing`, `Verifying`, and `Done`. Optional states such as `ADR In Progress` and `Blocked` should not hide the underlying core phase.

---

## 4. Phase-By-Phase Tutorial

### Phase 0: Install

Install the kit into a target repository:

```bash
bash kit/scripts/install.sh /path/to/target-repo
```

The installer uses [`kit/manifest.json`](../kit/manifest.json) to decide which files are kit-managed, which files are adopter-owned seeds, and which state directories are preserved during upgrades.

After install, the adopter-facing entrypoints are:

- `AGENTS.md`
- `MASTER_INDEX.md`
- `docs/README.md`

### Phase 1: Bootstrap With `/starter-init`

Run:

```text
/starter-init
```

Required once per adopter repo. This prepares `docs/`, `memories/`, and baseline project memory. It has two practical paths:

- **Greenfield path:** bootstrap the harness and seed unknown project facts with `[UNKNOWN]`.
- **Brownfield path:** inspect existing code/tests/CI enough to record baseline proof surfaces and project-specific memory.

`/starter-init` does not implement product code. It prepares the repo so future feature work has stable instructions, memory, and verification commands.

### Phase 2: Feature Intake

Start a feature with either research or requirements:

```text
/spec-research
```

Use `/spec-research` when current behavior, root cause, or brownfield structure is unknown. It is required for Complex work and strongly recommended when the agent cannot safely define requirements from the user request alone.

```text
/spec-requirements
```

Use `/spec-requirements` when the desired behavior can be specified. This is required per feature. It creates or updates the feature slug under `artifacts/features/<slug>/` and locks testable acceptance criteria in `spec.md`.

### Phase 3: Context Session

Use `/context-session` only after the feature slug and `status.md` exist. It is not the command that creates a new feature.

| Mode | Use when | Output |
|---|---|---|
| `START` | Resuming an existing feature or beginning a new work session on an existing slug. | Readiness summary, routed context, current phase, blockers, next task. |
| `CHECKPOINT` | Pausing after meaningful progress while work remains active. | Updated `progress.md`, claim/status notes, next-step summary. |
| `END` | Closing a long session or preparing handoff to another session. | `handoff.md`, updated `progress.md`, candidate `session-extracts.md`. |

`/context-session END` is emphasized because it protects handoff state when chat history disappears. It is not the only context-session mode.

### Phase 4: Spec

Run:

```text
/spec-requirements
```

The spec phase answers “what and why,” not “how.” It should produce deterministic acceptance criteria. Unknowns must remain explicit as `[UNKNOWN]` or `[NEEDS CLARIFICATION]` until resolved.

Route back to `/spec-research` if the requirements depend on behavior that has not been observed.

### Phase 5: Plan

Run:

```text
/spec-plan
```

Planning is required after the spec is approved. It creates `plan.md` and `tasks.md`, maps acceptance criteria to implementation tasks, and defines proof commands for each task.

If a non-obvious architecture decision is locked during planning, branch to:

```text
/spec-adr
```

`/spec-adr` is conditional in Tiny and Standard work. It is required for each locked technical choice in Complex work.

### Phase 6: Implementation

Run:

```text
/spec-implement
```

Implementation is required per feature. It executes the approved tasks one at a time, keeps scope tied to `tasks.md`, and runs the mechanical gate through `kit/scripts/harness/gate-runner.sh` when appropriate.

If implementation reveals missing requirements or an unsafe design, do not improvise. Route back to `/spec-requirements` or `/spec-plan` and record the reason in `status.md`.

Use `/context-session CHECKPOINT` when a long implementation wave reaches a natural pause.

### Phase 7: Verification

Run:

```text
/harness-verify
```

Verification is required per feature. It checks mechanical proof, spec alignment, task evidence, and regressions according to the feature profile.

`/code-review` can be run manually, and verification may also call for review when quality, security, or design concerns need a focused audit:

```text
/code-review
```

If verification fails repeatedly on the same task or approach, route back to `/spec-plan` rather than looping on implementation.

### Phase 8: Memory Sync

After verification passes, use memory sync when there are durable lessons:

```text
/context-memory
```

This is conditional, evidence-based memory promotion. It should promote only observations supported by actual feature artifacts or verification results.

Use audit mode when the memory system itself needs inspection:

```text
/context-memory --audit
```

Use compaction when memory files are too large:

```text
/context-compact --file memories/repo/project-knowledge-base.md
```

`/context-compact` reduces memory size while preserving active constraints. It should not delete live rules just to make a file shorter.

### Phase 9: Status And Dashboard

Run:

```text
/context-status
```

Use this when you need cross-feature visibility, blocker awareness, or next-command guidance. It is optional for a single small feature, but valuable when multiple feature slugs or multiple agents are active.

The status surface reads feature artifacts and can refresh `docs/generated/dashboard.html`.

### Phase 10: Docs And Diagrams

Use these helpers when the work needs durable explanation:

```text
/technical-docs --mode api
/technical-docs --mode flow
/technical-docs --mode both
```

Use `/technical-docs` for API contracts, event flows, workflow traces, or a combined technical narrative.

```text
/codebase-documenter
```

Use `/codebase-documenter` for broader onboarding, architecture, setup, and repository documentation.

```text
/visualize
```

Use `/visualize` when a diagram clarifies architecture, data flow, sequence, state, ER, or agent/memory structure. Supported outputs are SVG and Mermaid. Mermaid-to-SVG rendering is optional and only available when `mmdc` is installed. Do not claim PlantUML, draw.io, PNG export, or interactive HTML output unless those capabilities are later added.

### Phase 11: Harness Maintenance

Run:

```text
/harness-maintain assess
/harness-maintain create
/harness-maintain improve
/harness-maintain eval
/harness-maintain doctor
```

Use `/harness-maintain` when maintaining the kit or repairing the harness, not as a routine feature step.

| Mode | Use when |
|---|---|
| `assess` | Evaluate harness quality, structure, and readiness. |
| `create` | Build missing harness structure from scratch. |
| `improve` | Use observed failures to improve harness rules, references, or checks. |
| `eval` | Run evaluator passes, especially after cross-cutting or harness changes. |
| `doctor` | Detect drift, broken references, stale generated files, or install/package issues. |

For Complex work that changes the harness itself, `/harness-maintain eval` is part of the verification expectation.

---

## 5. Which Skill Do I Use?

| Situation | Use |
|---|---|
| First setup after install | `/starter-init` |
| Existing behavior is unclear | `/spec-research` |
| You can define desired behavior now | `/spec-requirements` |
| Requirements are approved | `/spec-plan` |
| A technical decision needs a durable record | `/spec-adr` |
| Tasks are approved and ready | `/spec-implement` |
| Work appears complete | `/harness-verify` |
| You are resuming an existing feature | `/context-session START` |
| You are pausing mid-feature | `/context-session CHECKPOINT` |
| You are ending a long session | `/context-session END` |
| There are durable lessons to promote | `/context-memory` |
| Memory health needs inspection | `/context-memory --audit` |
| Memory files are oversized | `/context-compact` |
| You need active feature status | `/context-status` |
| You need an implementation review | `/code-review` |
| You need API or flow docs | `/technical-docs --mode api`, `--mode flow`, or `--mode both` |
| You need repo onboarding docs | `/codebase-documenter` |
| You need a diagram | `/visualize` |
| The harness itself needs repair or evaluation | `/harness-maintain` |

---

## 6. Practical End-To-End Example

For a Standard feature in a known codebase:

```text
/starter-init                         # once per repo
/spec-requirements                    # define ACs
/spec-plan                            # design and tasks
/spec-implement                       # execute tasks
/harness-verify                       # prove done
/context-memory                       # only if durable lessons exist
/context-session END                  # if the session was long or needs handoff
```

For a Complex brownfield feature:

```text
/starter-init                         # once per repo
/spec-research                        # required because behavior/risk is unknown
/spec-requirements                    # lock ACs
/spec-adr                             # required for locked technical choices
/visualize                            # required when system structure changes
/spec-plan                            # full design, plan, tasks
/context-session CHECKPOINT           # recommended during long work
/spec-implement                       # smaller verified slices
/harness-verify                       # deeper verification
/harness-maintain eval                # required if the harness itself changed
/context-memory                       # promote evidence-backed lessons
/context-session END                  # handoff and extracted candidates
```

For documentation-only support work:

```text
/technical-docs --mode flow
/codebase-documenter
/visualize
```

These documentation helpers are shipped by default, but they do not replace the core delivery path for behavior-changing feature work.

---

## 7. Ground Truth References

- Shipped skill index: [`kit/skills/README.md`](../kit/skills/README.md)
- Kit map: [`documents/kit-map.md`](kit-map.md)
- Status phases: [`kit/skills/_shared/status-phases.md`](../kit/skills/_shared/status-phases.md)
- Install manifest: [`kit/manifest.json`](../kit/manifest.json)
- Context loader script: [`kit/scripts/context-loader.py`](../kit/scripts/context-loader.py)

When this tutorial disagrees with a `SKILL.md` contract, the `SKILL.md` contract is the source of truth.
