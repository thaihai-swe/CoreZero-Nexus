# Kit Diagrams

Mermaid diagrams (`.mmd`) visualizing the CoreZero Nexus architecture, memory model, and workflows. Validate any diagram with:

```bash
python3 skills/visualize/scripts/validate_mermaid.py documents/diagrams/<file>.mmd
```

Render to SVG (requires `mmdc`):

```bash
python3 skills/visualize/scripts/render_mermaid.py documents/diagrams/<file>.mmd <out>.svg
```

Legacy `corezero-*` filenames may remain on some diagram files until a later rename pass. Their labels, captions, and public meanings follow the pack-based command vocabulary.

## Architecture & Memory

| Diagram | Shows |
|---|---|
| `corezero-context.mmd` | C4 system context — user, kit, LLM, git repo |
| `corezero-memory.mmd` | 3-tier memory (Instruction / Auto / Extracted) + `INDEX.md` router for `context-*` flows |
| `corezero-context-routing.mmd` | Smart context routing — INDEX.md intent-based group loading |
| `corezero-context-assembly.mmd` | 6-tier context assembly, highest to lowest signal |
| `corezero-mindmap.mmd` | Full kit structure mapped to Starter, Context, Spec, and Harness packs |
| `skills-repository-architecture.mmd` | Public pack grouping with advanced specialist tools |

## Workflow & Lifecycle

| Diagram | Shows |
|---|---|
| `corezero-full-flow.mmd` | Guided pack flow with advanced specialist branches |
| `corezero-dataflow.mmd` | Artifact flow: analysis → spec → plan → code → review → memory |
| `corezero-onboarding.mmd` | Greenfield vs Brownfield onboarding through `starter-init` (Phase A: archaeology, Phase B: bootstrap) |
| `corezero-rigor-profiles.mmd` | Adaptive rigor: Tiny / Standard / Complex |
| `corezero-harness-maintenance.mmd` | Flowchart of /harness-maintain Assess vs Improve modes |
| `skills-end-to-end-execution.mmd` | Sequence diagram of a harness run |
| `corezero-spec-lifecycle.mmd` | Spec flow: triage → grilling waves → readiness → locked |
| `corezero-verify-gate.mmd` | Harness verification gate: split modes to Done |
| `corezero-traceability.mmd` | REQ → AC → TASK → proof chain |
| `corezero-status-machine.mmd` | Feature status state machine + transitions |
| `corezero-greenfield-flow.mmd` | Greenfield flow: bootstrap → `starter-init` → ship first feature |
| `corezero-brownfield-flow.mmd` | Brownfield flow: archaeology → `starter-init` → research → ship first feature |
| `corezero-packs-taxonomy.mmd` | Mindmap catalog of all public commands mapped to the 4 Core Packs |
| `corezero-subagent-fanout.mmd` | SDD: delegate broad work, merge summaries only |

## Self-Improving Knowledge

| Diagram | Shows |
|---|---|
| `corezero-self-improving-kb.mmd` | ship → extract → triage → promote → KB grows loop |
| `corezero-post-ship-sync.mmd` | Sequence of the mandatory post-ship `context-memory` sweep |

## Maintenance

Refresh a diagram when the underlying system changes:
- Memory model changes → `corezero-memory.mmd`, `corezero-context-routing.mmd`
- Public command flow changes → `corezero-full-flow.mmd`
- Observability/Maintenance changes → `corezero-harness-maintenance.mmd`
- New memory file or tier → `corezero-memory.mmd`, `corezero-mindmap.mmd`
- Brownfield bootstrap changes → `corezero-onboarding.mmd`

After editing, re-run the validator on the changed file.
