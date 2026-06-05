---
name: context-memory
description: Create, maintain, and route durable repository memory. Manage INDEX.md (memory router), constitution.md, security-policy.md, learned-heuristics.md, project-knowledge-base.md, docs/architecture.md, decide where findings belong, and run the post-ship knowledge sync after harness-verify passes.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in spec-driven repositories that use memories/repo/ and artifacts/features/<slug>/.

---

# Kit Memory


## Overview

Use this skill to manage durable repository memory across eleven functions:

1. **Memory Router (INDEX.md)** - Maintain `memories/repo/INDEX.md`. Routes session loads, declares groups, and tracks watchlist.
2. **Constitution** - Repo-wide normative rules (CC-*).
3. **Security Policy** - Repo-wide permission, trust-boundary, and sandbox rules.
4. **Learned Heuristics** - Descriptive, evidence-backed instincts.
5. **Project Knowledge Base** - Durable descriptive facts, patterns, boundaries.
6. **Architecture Baseline** - Durable system structure, boundaries, and integration seams.
7. **AI Coding Contract Synthesis** - Turn stack and conventions into coding rules.
8. **Project-Level Continuity** - Preserve durable multi-feature context.
9. **Memory Promotion** - Route findings to the right destination.
10. **Extraction Triage** - Classify candidates from session extracts and observability log.
11. **Post-Ship Sync (Knowledge Sweep)** - Run post-ship knowledge sweep after verification passes.

This is an advanced helper path. Feature work stays in the 6-step core flow and reaches this skill only when routed for sync, promotion, or repair.

## Memory Tiers

| Tier | Files | Who writes | Durability | Triage |
|---|---|---|---|---|
| **Instruction** | `constitution.md`, `security-policy.md`, `learned-heuristics.md`, `project-knowledge-base.md`, `harness-config.md`, `domain-specs.md`, `adr-log.md`, `docs/architecture.md` | Humans + `context-memory` | Durable | Direct edit, evidence-required |
| **Auto** | `observability-log.md` | `harness-maintain` Improve Mode, `harness-verify` | Append-only | Reviewed for promotion |
| **Extracted** | `artifacts/features/<slug>/session-extracts.md` | `context-session END` | Per-feature | Reviewed in Extraction Triage |

## Read First

- `memories/repo/INDEX.md` (memory router)
- `memories/repo/constitution.md`
- `memories/repo/security-policy.md` (if it exists)
- `memories/repo/learned-heuristics.md` (if it exists)
- `memories/repo/project-knowledge-base.md`
- `docs/architecture.md` (if it exists)
- feature artifacts, review outputs, and repo code paths

## When to Use

Use this skill to:
- **Create/maintain `INDEX.md`**: Bootstrap memory router, add groups/watchlist.
- **Run post-ship sync**: Sweeps and updates memory files in `INDEX.md`.
- **Maintain Instruction files**: Edit constitution, security-policy, heuristics, PKB, and architecture baseline.
- **Triage extracts**: Process `session-extracts.md` and `observability-log.md` candidates (promote, defer, or discard).
- **Synthesize Coding Contract**: Build rule-sets from stack evidence.

Do not use for:
- Writing feature-specific artifacts (`spec.md`, `plan.md`, `tasks.md`).
- Temporary findings or speculative future design.
- Post-implementation code review (use `harness-verify`).

## Workflow

### Memory Promotion & File Management
1. **Identify the finding** and its source.
2. **Classify and Route**:
   - **Normative repo rule** -> `constitution.md`
   - **Security/sandbox rule** -> `security-policy.md`
   - **Descriptive repeated instinct** -> `learned-heuristics.md`
   - **Durable fact/pattern** -> `project-knowledge-base.md`
   - **Structural architecture map** -> `docs/architecture.md`
   - **Feature-local** -> Keep in feature artifacts.
3. **Constitution Updates**: Use stable CC-* identifiers, maintain semantic versioning, and avoid overlapping rules.
4. **Security Policy**: Define permissions, safe vs confirm actions, network/fs/secret boundaries, and prompt-injection handling.
5. **Learned Heuristics**: Record repeated, evidence-backed execution heuristics (trigger, heuristic, evidence, recurrence count, semantic links, confidence). If you find a matching heuristic, increment its `recurrence-count`. If `recurrence-count` hits 3 or more, automatically draft a CC-* promotion proposal.
6. **Project Knowledge Base**: Integrate findings into descriptive sections, avoiding duplicates. Ensure every new entry uses markdown links (Semantic Knowledge Graph) to connect to relevant `docs/architecture.md` components or domain specs.
7. **Architecture Baseline**: Map component structure, runtime boundaries, data flow, and external integrations in `docs/architecture.md`.
8. **AI Coding Contract**: Synthesize stack conventions into normative rules (`constitution.md`) and descriptive examples (`project-knowledge-base.md`).
9. **Post-Ship Sync**: Sweeps memory files in `INDEX.md`. `Tiny` profile sweeps `learned-heuristics.md`; `Standard` and above run full sweeps. Follow [references/post-ship-sync.md](references/post-ship-sync.md).
10. **Extraction Triage**: Classify candidates from `session-extracts.md` and `observability-log.md`. Follow [references/extraction-triage.md](references/extraction-triage.md).

## Stop Conditions

- Finding is speculative or lacks repository evidence.
- The content is feature-local.
- Proposed coding rules cannot be justified by repo patterns.

## Core Rules

- **Normative vs. Descriptive**: Rules go in Constitution/Security Policy; facts go in Knowledge Base/Heuristics.
- **Structure**: Structural maps belong in `docs/architecture.md`, not PKB.
- **Durable Only**: Do not save session residue or diary logs.
- **Surgical Amendments**: Refine existing rules instead of adding duplicates. Use semantic versioning for Constitution.
- **Evidence-First**: Promote only what is supported by repository evidence.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "I'll save everything to the knowledge base." | Knowledge base is for durable, reusable patterns, not session residue. |
| "I don't need to update INDEX.md for new files." | INDEX.md routes sessions. Unlisted files are invisible to future sessions. |
| "Post-ship sync is busywork." | Every memory file must be reviewed with a one-line reason if untouched. |
| "I'll promote now and evidence later." | Evidence is required at promotion time. |
| "Both files can hold this rule." | Duplication across constitution and knowledge base creates drift. |

## Red Flags

- Architecture maps buried in PKB.
- Descriptive notes written as rules or normative language in descriptive files.
- Rules overlap existing CC-* items.
- Feature-local notes or temporary workarounds promoted as durable memory.
- Coding contract duplicates rules in both constitution and knowledge base.

## Verification

- [ ] Normative rules in constitution/security-policy; descriptive facts in heuristics/PKB.
- [ ] Durable structures mapped in `docs/architecture.md`.
- [ ] Stable identifiers and semantic version bumps are coherent.
- [ ] No placeholders; duplicate sections merged.
- [ ] Memory is grounded in repository evidence.

## Output Standard

Memory files must contain durable, evidence-grounded repo knowledge, separating normative rules from descriptive facts, and using stable identifiers.

## Output Rules

- Update only: `memories/repo/constitution.md`, `memories/repo/security-policy.md`, `memories/repo/learned-heuristics.md`, `memories/repo/project-knowledge-base.md`, `memories/repo/harness-config.md`, `memories/repo/domain-specs.md`, `docs/architecture.md`, `memories/repo/INDEX.md`, `memories/repo/observability-log.md`, or `memories/repo/adr-log.md`.
- Route findings to the owning skill with a short reason.
- Preserve heading structure and identifier stability.

## References

- [references/index-template.md](references/index-template.md)
- [references/constitution-template.md](references/constitution-template.md)
- [references/security-policy-template.md](references/security-policy-template.md)
- [references/learned-heuristics-template.md](references/learned-heuristics-template.md)
- [references/project-knowledge-base-template.md](references/project-knowledge-base-template.md)
- [references/architecture-template.md](references/architecture-template.md)
- [references/pkb-tech-stack-template.md](references/pkb-tech-stack-template.md)
- [references/pkb-conventions-template.md](references/pkb-conventions-template.md)
- [references/decision-template.md](references/decision-template.md)
- [references/observability-log-template.md](references/observability-log-template.md)
- [references/post-ship-sync.md](references/post-ship-sync.md)
- [references/extraction-triage.md](references/extraction-triage.md)
- [../context-session/references/session-extracts-template.md](../context-session/references/session-extracts-template.md)
- [references/adr-log-template.md](references/adr-log-template.md)
