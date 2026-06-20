# Context Engineering

## Purpose

Defines how the kit assembles, budgets, compacts, and evicts context during long-running work. Context is the agent's working memory — too little and it forgets, too much and it loses focus.

---

## The Minimum Viable Context (MVC) Principle (Rule CC-011)

To prevent cognitive drift, context window saturation, and high execution costs, the kit enforces the **Minimum Viable Context (MVC)** principle (**Rule CC-011**).

The core directive of MVC is: **Only load the minimal, high-signal context required to execute the active task.**

Never dump full files, large directories, or entire database schemas into the agent's context window. Instead, follow progressive JIT (Just-In-Time) loading and enforce strict, aggressive compaction and eviction of stale data.

---

## The Three-Track Memory Model

To structure workspace information efficiently, the kit divides memory into three distinct operational tracks:

```mermaid
flowchart TD
    %% Three-Track Memory Model

    subgraph Track1["1. Native Stack (Ephemeral Runtime)"]
        NS1["Router (AGENTS.md)"]
        NS2["JIT Code Content (T5)"]
        NS3["Transient Logs (T6)"]
    end

    subgraph Track2["2. Cross-Session Tools (Durable Local Repo)"]
        CS1["MASTER_INDEX.md (Router Index)"]
        CS2["Repo Memories (memories/repo/)"]
        CS3["Feature Artifacts (status/plan/tasks)"]
    end

    subgraph Track3["3. Team Sharing (Domain & Exporter Surface)"]
        TS1["Domain Packs (memories/domain/)"]
        TS2["Adopter-facing APIs & Docs"]
    end

    Track1 -->|evicted/summarized into| Track2
    Track2 -->|triage & promote lessons to| Track3
```

1. **Native Stack (Ephemeral Runtime):**
   - **What**: The direct, live token context loaded into the LLM during the active session. This includes the entrypoint router (`AGENTS.md`), JIT-loaded target code files, and transient execution outputs (Tiers 1, 5, and 6).
   - **Lifespan**: Volatile. Evicted and summarized aggressively within the session.

2. **Cross-Session Tools (Durable Local Repository):**
   - **What**: Git-tracked markdown files that store local feature state and repository-wide memories (Tiers 2, 3, and 4). Includes feature plans, tasks, progress logs, `learned-heuristics.md`, and `harness-telemetry.md`.
   - **Lifespan**: Persistent across sessions, versioned via Git.

3. **Team Sharing (Domain & Exporter Surface):**
   - **What**: Shared knowledge domain templates, boundaries, glossaries (`memories/domain/`), and system references that propagate to other developers and peer agent sessions.
   - **Lifespan**: Extremely durable, highly curated.

---

## Context Tiers

The kit assembles context across 6 tiers, from highest signal to lowest. Each tier has its own load rule.

```mermaid
flowchart TB
    %% 6-Tier Context Assembly — highest signal to lowest

    T1["Tier 1 — Router<br/>AGENTS.md + MASTER_INDEX.md"]:::t1
    T2["Tier 2 — Repo Memory (Always)<br/>constitution + security + harness-config"]:::t2
    T3["Tier 3 — Repo Memory (By Intent)<br/>Knowledge / Learned / Domain Packs / Debug groups"]:::t3
    T4["Tier 4 — Feature Artifacts<br/>status / spec / plan / tasks / handoff"]:::t4
    T5["Tier 5 — Raw Code<br/>only files for the immediate task (JIT)"]:::t5
    T6["Tier 6 — Transient Logs<br/>command output, traces (summarize + evict)"]:::t6

    T1 -->|every session| T2
    T2 -->|every session| T3
    T3 -->|before editing| T4
    T4 -->|just-in-time| T5
    T5 -->|only when proving| T6

    T6 -.->|compaction: summarize + evict| T4
    T5 -.->|evict after task| T4

    LOAD["Load Rules:<br/>Tier 1-2 always · Tier 3 by intent<br/>Tier 4 before edit · Tier 5 JIT · Tier 6 on demand"]:::note

    classDef t1 fill:#1e3a8a,stroke:#1e40af,color:#fff
    classDef t2 fill:#3b82f6,stroke:#1d4ed8,color:#fff
    classDef t3 fill:#6366f1,stroke:#4f46e5,color:#fff
    classDef t4 fill:#8b5cf6,stroke:#6d28d9,color:#fff
    classDef t5 fill:#a78bfa,stroke:#7c3aed,color:#fff
    classDef t6 fill:#c4b5fd,stroke:#8b5cf6,color:#1e1b4b
    classDef note fill:#f7f7f5,stroke:#e0e0e0,color:#111
```

### Tier Reference

| Tier | Content | Load Strategy |
|------|---------|---------------|
| 1 | `AGENTS.md` + `MASTER_INDEX.md` (router) | Always — first thing loaded every session |
| 2 | Always group: `core-policies.md` | Always — every session |
| 3 | By-Intent groups: Knowledge / Learned / Domain Packs / Debug | Only when trigger keywords match the task |
| 4 | Feature artifacts: `spec.md`, `plan.md`, `tasks.md`, `handoff.md` | Before editing or verifying |
| 5 | Raw code — only files for the immediate task | JIT — just-in-time per task |
| 6 | Transient logs, grep output, stack traces | On demand — summarize and evict quickly |

**Intent groups (Tier 3) — defined in `memories/repo/MASTER_INDEX.md`:**
- **Knowledge** — loads when task touches `architecture`, `pattern`, `stack`, `domain`, `convention`, `module`, `api surface`, `bootstrap`, `skill`, `template`, `adr`, `decision` (loads PKB, `adr-log.md`, `docs/project/architecture.md`, `docs/generated/code-map.md`)
- **Learned** — loads when task echoes `heuristic`, `recurring`, `we always/never`, `last time`, `lesson` (loads `learned-heuristics.md`)
- **Domain Packs** — loads when domain-pack glossary triggers match the task (`memories/domain/`). Low-confidence matches load `glossary.md` only; high-confidence matches load the full pack.
- **Debug** — loads on `debug`, `failure`, `regression`, `retro`, `root cause`, `flaky`, `why did`, `incident` (loads `harness-telemetry.md` and per-feature `session-extracts.md`)

## Assembly Rules

- Load tiers in order (1 → 6)
- Never skip Tier 1-2
- Load Tier 3 only when the task crosses component boundaries
- Load Tier 4 scoped to the active feature slug
- Load Tier 5 minimally — only the files the current task touches
- Tier 6 is ephemeral — extract the signal, then evict the noise

---

## Smart Routing via MASTER_INDEX.md

Tier 3 (memory by intent) is no longer "load everything." `memories/repo/MASTER_INDEX.md` declares Always-loaded files plus by-intent groups whose trigger keywords decide what loads. Sessions report what they loaded and what they skipped — silent skipping is not allowed.

**Confidence-Scored Loading (Partial Loads):**
When loading by-intent groups, the harness evaluates a confidence score based on keyword matches:
- **Low Confidence (≤2 keywords):** Performs a **partial-load**. The session loads only the index or header file for that group, heavily conserving context budget while retaining situational awareness.
- **High Confidence (3+ keywords):** Performs a full load of all files in the group.

```mermaid
flowchart TD
    %% Smart Context Routing via MASTER_INDEX.md

    START([Session Start]) --> IDX[Read MASTER_INDEX.md<br/>memory router]
    IDX --> ALWAYS[Load Always group<br/>constitution + security-policy + harness-config]

    ALWAYS --> MATCH{Match task vs<br/>trigger keywords}

    MATCH -->|architecture, pattern,<br/>stack, domain| KNOW[Load Knowledge group<br/>PKB + architecture]
    MATCH -->|heuristic, recurring,<br/>we always/never| LEARN[Load Learned group<br/>learned-heuristics]
    MATCH -->|domain glossary triggers| DOMAIN[Load Domain Pack<br/>glossary only or full pack]
    MATCH -->|debug, failure, regression,<br/>retro, root cause| DEBUG[Load Debug group<br/>observability-log + session-extracts]
    MATCH -->|no trigger matches| SKIP[Load Always tier only<br/>record 'no groups matched']

    KNOW --> FEAT[Load Feature artifacts<br/>spec / plan / tasks / handoff]
    LEARN --> FEAT
    DOMAIN --> FEAT
    DEBUG --> FEAT
    SKIP --> FEAT

    FEAT --> REPORT[Report Context Loaded<br/>+ Context Skipped with reasons]
    REPORT --> WORK([Begin work])

    STALE[MASTER_INDEX.md missing<br/>or stale] -.->|fallback| ALL[Load every memory file<br/>route gap to context-memory]
    IDX -.->|if missing| STALE

    classDef terminal fill:#0d0d0d,stroke:#0d0d0d,color:#fff
    classDef router fill:#3b82f6,stroke:#1d4ed8,color:#fff
    classDef group fill:#eef2ff,stroke:#c7d2fe,color:#3730a3
    classDef decision fill:#fff7ed,stroke:#f59e0b,color:#0d0d0d
    classDef fallback fill:#fcf3f3,stroke:#f2c4c4,color:#c62828

    class START,WORK terminal
    class IDX,ALWAYS router
    class KNOW,LEARN,DOMAIN,DEBUG,SKIP,FEAT group
    class MATCH decision
    class STALE,ALL fallback
```

---

## Context Eviction & Telemetry Control

Raw console output, compiler errors, and test execution traces (Tier 6) are extremely token-dense and low-signal once analyzed. Retaining them in the active context window wastes token budget and accelerates model saturation, leading to hallucinations.

To prevent this, the `/spec-implement` workflow enforces **Mandatory Context Eviction**:
1. **Execute**: Run the mechanical validation gate via `gate-runner.sh`.
2. **Analyze**: Parse the success or failure output to identify the root cause or confirm completion.
3. **Summarize**: Record a 3-5 line high-level summary of the run in the active verification/task log (e.g. `tests passed` or `linter failed with syntax error in lines 12-14`).
4. **Evict**: Immediately remove the raw terminal stderr/stdout from the active context window. Do not keep the raw command dump in subsequent turns.
5. **Log Telemetry**: If the run failed, pipe the output to `telemetry-collector.sh` which appends it to `memories/repo/harness-telemetry.md` (removing it from the active session runtime).

---

## Compaction Triggers

Compact context when:
- `harness-telemetry.md` exceeds 500 lines or the session is ending
- Raw grep/search output exceeds 50 lines
- Full file contents are loaded but only a section is needed
- Previous task's code context is no longer relevant
- Logs or error output has been analyzed and findings recorded
- The context window is approaching capacity

---

## Compaction Strategies

| Strategy | When | How |
|----------|------|-----|
| **Summarize** | Large tool output analyzed | Replace raw output with 3-5 line summary |
| **Scope-narrow** | Full file loaded, only function needed | Drop to relevant section |
| **Evict** | Previous task context no longer needed | Remove entirely |
| **Promote** | Finding is durable | Write to memory/artifact, then evict source |

---

## Stale Context Rules

Context becomes stale when:
- The finding has been recorded in an artifact
- The task that needed it is marked Done
- A newer version of the information exists
- The raw data has been summarized

Stale context MUST be evicted — carrying it forward dilutes attention and wastes budget.

---

## Session Checkpoints

Checkpoint when:
- A task is completed (natural boundary)
- Context is getting large (approaching compaction triggers)
- Switching between skills (different context needs)
- Before a long-running operation

Checkpoint = update progress.md + apply compaction + verify context is lean.

---

## Anti-Patterns

| Anti-Pattern | Why It's Bad | Instead |
|--------------|-------------|---------|
| Loading entire design.md for a single task | Wastes context budget | Load only the relevant section |
| Keeping raw grep output after analysis | Noise dilutes signal | Summarize findings, evict raw output |
| Loading all feature artifacts at once | Most aren't needed for the current task | Load JIT based on task dependencies |
| Never checkpointing | Context grows until quality degrades | Checkpoint after each completed task |
| Relying on chat history for state | Chat is volatile and gets truncated | Use progress.md as system of record |

---

## Subagent-Driven Development

Broad work (multi-file search, codebase mapping, stress-testing) is delegated to subagents whose raw exploration stays isolated. Only summary reports merge back into the main context — keeping the main loop lean.

```mermaid
flowchart TD
    %% Subagent-Driven Development (SDD) — broad work delegated, only summaries return

    MAIN[Main Agent Loop<br/>lean context window]

    MAIN --> DECIDE{Broad / parallel work?<br/>multi-file search, research,<br/>stress-test, repetitive edits}
    DECIDE -- No --> INLINE[Handle inline<br/>in main context]
    DECIDE -- Yes --> SPAWN[Spawn subagents]

    SPAWN --> SA1[Subagent A<br/>isolated context]
    SPAWNOW[Subagent B<br/>isolated context]
    SA3[Subagent C<br/>isolated context]

    SA1 -->|raw exploration<br/>stays isolated| R1[Summary Report A]
    SPAWNOW -->|raw exploration<br/>stays isolated| R2[Summary Report B]
    SA3 -->|raw exploration<br/>stays isolated| R3[Summary Report C]

    R1 --> MERGE[Merge ONLY summaries<br/>into main context]
    R2 --> MERGE
    R3 --> MERGE

    MERGE --> STATUS[Each subagent ends with:<br/>DONE / DONE_WITH_CONCERNS<br/>/ BLOCKED / NEEDS_CONTEXT]
    STATUS --> MAIN

    INLINE --> MAIN

    NOTE["Raw tool output never floods main loop.<br/>Main context stays lean and fast.<br/>BLOCKED / NEEDS_CONTEXT are never ignored."]:::note

    classDef main fill:#3b82f6,stroke:#1d4ed8,color:#fff
    classDef sub fill:#8b5cf6,stroke:#6d28d9,color:#fff
    classDef report fill:#a78bfa,stroke:#7c3aed,color:#fff
    classDef decision fill:#fff7ed,stroke:#f59e0b,color:#0d0d0d
    classDef note fill:#f7f7f5,stroke:#e0e0e0,color:#111

    class MAIN,MERGE,STATUS main
    class SA1,SPAWNOW,SA3 sub
    class R1,R2,R3 report
    class DECIDE decision
```

---

## Domain Packs

Domain packs extend the memory router with project-specific semantic context. Each pack captures the ubiquitous language, proven patterns, anti-patterns, and boundary rules for a specific business or technical domain.

### Where They Live

```
memories/domain/
├── glossary.md      — ubiquitous language + trigger keywords
├── patterns.md      — proven domain patterns
├── anti-patterns.md — failure modes to avoid
├── boundaries.md    — domain ownership and integration contracts

```

### How Loading Works

Domain packs use confidence-scored loading (same principle as Tier 3 intent groups):
- **3+ keyword matches** → full pack load (all files)
- **1–2 keyword matches** → partial load (glossary.md only)
- **0 matches** → pack skipped

Trigger keywords are declared in each pack's `glossary.md` frontmatter:
```yaml
domain: payments
triggers: [billing, invoice, charge, stripe, subscription, refund, payment]
```

### Authoring a Pack

1. Create `memories/domain/` with the required files.
2. Declare triggers in `glossary.md` frontmatter.
3. Register the pack in `memories/repo/MASTER_INDEX.md` under `## By Domain Packs`.
4. See `memories/domain/README.md` for the full schema.

### Lifecycle

Domain packs are **adopter-owned** memory — the kit seeds the schema but not the content. During `/context-memory` Post-Ship Sync, promote durable patterns from `session-extracts.md` into the appropriate domain pack file.

Brownfield artifacts under `memories/repo/project-knowledge-base.md ## Repository Overview` are separate from domain packs. As of the current kit revision, they are produced by `/starter-init` (Phase A) but are not yet auto-routed by `MASTER_INDEX.md`; sessions need to load them intentionally when relevant.

> **MVC Tool — `scripts/context-loader.py`**: Provides programmatic enforcement of the MVC rule. Run `python3 scripts/context-loader.py <file> --mode summary` to extract only the `## Index` section or first 50 lines of a memory file, preserving context budget without agent interpretation.

---

## Context Compaction & Claim Gaps

During the system-wide evaluation (detailed in [evaluation-report.md](evaluation-report.md)), several context-engineering gaps and corresponding recommendations were identified:

* **Workspace Claim Lock Contention**: The file-backed claim protocol manages multi-agent coordination but lacks automated collision resolution. To prevent distributed agent workspace blockages, claim files should be explicitly mapped to Git branch states rather than single absolute paths.
