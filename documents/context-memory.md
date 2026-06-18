# Context Assembly & Memory Tiers

This guide defines how the CoreZero Nexus manages context and durable repository memory to prevent context dilution, agent amnesia, and command drift.

---

## 1. Progressive Disclosure

Progressive disclosure is the practice of layering information so that agents load only what they need, when they need it. Instead of dumping all context upfront, the harness reveals deeper detail as the agent moves through the workflow.

```text
Layer 1: Router (AGENTS.md)          ~50 lines    Always loaded
    │
    ▼
Layer 2: Skill Contract (SKILL.md)   ~100-250 lines    Loaded when skill is invoked
    │
    ▼
Layer 3: References (references/)    Variable    Loaded JIT within the skill workflow
```

### Layer 1: Router
* **What**: `AGENTS.md` — priority rules, skill routing, and pointers to memory.
* **When loaded**: Every session start. Always in context.
* **Design rules**:
  - Under 50 lines.
  - No full skill bodies — only names and one-line descriptions.
  - Points to deeper docs, never duplicates them.
  - Sets behavioral constraints (no fabrication, surgical changes, fail loud).

### Layer 2: Skill Contract
* **What**: `skills/<name>/SKILL.md` — full workflow, rules, stop conditions, and verification gates.
* **When loaded**: Only when the command is invoked (e.g., user says `/spec-requirements`).
* **Design rules**:
  - Self-contained — an agent can execute the skill from this file alone.
  - References deeper docs in `references/` but doesn't inline them.
  - Includes a "Read First" section listing what to load before starting.
  - Includes an "Output Rules" section constraining what the skill can create.

### Layer 3: References
* **What**: Templates, rubrics, checklists, and examples in `skills/<name>/references/`.
* **When loaded**: During specific workflow steps that need them.
* **Design rules**:
  - Each reference serves one purpose (template, rubric, checklist, example).
  - Named clearly so the skill can request them by name.
  - Never loaded speculatively — only when the workflow step requires them.
  - Can be skipped entirely for Tiny-profile work.

---

## 2. Context Engineering

Context is the agent's working memory. The kit assembles context across 6 tiers, from highest signal to lowest. Each tier has its own load rule.

### 6-Tier Context Assembly

```mermaid
flowchart TB
    %% 6-Tier Context Assembly — highest signal to lowest

    T1["Tier 1 — Router<br/>AGENTS.md + INDEX.md"]:::t1
    T2["Tier 2 — Repo Memory (Always)<br/>constitution + security + harness-config"]:::t2
    T3["Tier 3 — Repo Memory (By Intent)<br/>Knowledge / Learned / Architecture / Debug groups"]:::t3
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
| 1 | `AGENTS.md` + `INDEX.md` (router) | Always — first thing loaded every session |
| 2 | Always group: `core-policies.md`, `core-policies.md`, `security-policy.md` | Always — every session |
| 3 | By-Intent groups: Knowledge / Learned / Debug | Only when trigger keywords match the task |
| 4 | Feature artifacts: `spec.md`, `plan.md`, `tasks.md`, `handoff.md` | Before editing or verifying |
| 5 | Raw code — only files for the immediate task | JIT — just-in-time per task |
| 6 | Transient logs, grep output, stack traces | On demand — summarize and evict quickly |

**Intent groups (Tier 3) — defined in `memories/repo/INDEX.md`:**
- **Knowledge** — loads when task touches `architecture`, `pattern`, `stack`, `domain`, `convention`, `module`, `api surface`, `bootstrap`, `skill`, `template`, `adr`, `decision` (loads PKB, `adr-log.md`, `docs/project/architecture.md`, `docs/generated/codemap.md`, `docs/generated/references-index.md`).
- **Learned** — loads when task echoes `heuristic`, `recurring`, `we always/never`, `last time`, `lesson` (loads `learned-heuristics.md`).
- **Debug** — loads on `debug`, `failure`, `regression`, `retro`, `root cause`, `flaky`, `why did`, `incident` (loads `harness-telemetry.md` and per-feature `session-extracts.md`).

### Smart Routing via INDEX.md

Tier 3 (memory by intent) is loaded dynamically. `memories/repo/INDEX.md` declares Always-loaded files plus by-intent groups whose trigger keywords decide what loads. Sessions report what they loaded and what they skipped — silent skipping is not allowed.

**Confidence-Scored Loading (Partial Loads):**
When loading by-intent groups, the harness evaluates a confidence score based on keyword matches:
- **Low Confidence (≤2 keywords):** Performs a **partial-load**. The session loads only the index or header file for that group, heavily conserving context budget while retaining situational awareness.
- **High Confidence (3+ keywords):** Performs a full load of all files in the group.

```mermaid
flowchart TD
    %% Smart Context Routing via INDEX.md

    START([Session Start]) --> IDX[Read INDEX.md<br/>memory router]
    IDX --> ALWAYS[Load Always group<br/>constitution + security-policy + harness-config]

    ALWAYS --> MATCH{Match task vs<br/>trigger keywords}

    MATCH -->|architecture, pattern,<br/>stack, domain| KNOW[Load Knowledge group<br/>PKB + architecture]
    MATCH -->|heuristic, recurring,<br/>we always/never| LEARN[Load Learned group<br/>learned-heuristics]
    MATCH -->|debug, failure, regression,<br/>retro, root cause| DEBUG[Load Debug group<br/>observability-log + session-extracts]
    MATCH -->|no trigger matches| SKIP[Load Always tier only<br/>record 'no groups matched']

    KNOW --> FEAT[Load Feature artifacts<br/>spec / plan / tasks / handoff]
    LEARN --> FEAT
    DEBUG --> FEAT
    SKIP --> FEAT

    FEAT --> REPORT[Report Context Loaded<br/>+ Context Skipped with reasons]
    REPORT --> WORK([Begin work])

    STALE[INDEX.md missing<br/>or stale] -.->|fallback| ALL[Load every memory file<br/>route gap to context-memory]
    IDX -.->|if missing| STALE

    classDef terminal fill:#0d0d0d,stroke:#0d0d0d,color:#fff
    classDef router fill:#3b82f6,stroke:#1d4ed8,color:#fff
    classDef group fill:#eef2ff,stroke:#c7d2fe,color:#3730a3
    classDef decision fill:#fff7ed,stroke:#f59e0b,color:#0d0d0d
    classDef fallback fill:#fcf3f3,stroke:#f2c4c4,color:#c62828

    class START,WORK terminal
    class IDX,ALWAYS router
    class KNOW,LEARN,DEBUG,SKIP,FEAT group
    class MATCH decision
    class STALE,ALL fallback
```

### Compaction & Eviction

To maintain focus and prevent memory saturation, the context must be compacted dynamically:

* **Compaction Triggers**:
  - Raw grep/search output exceeds 50 lines.
  - Full file contents are loaded but only a section is needed.
  - Previous task's code context is no longer relevant.
  - Logs or error output has been analyzed and findings recorded.
  - The context window is approaching capacity.

* **Strategies**:
  - **Summarize**: Replace raw log/grep outputs with a 3-5 line summary.
  - **Scope-narrow**: Evict full files and load only the relevant function/block.
  - **Evict**: Remove previous task contexts completely once a task is marked Done.
  - **Promote**: Write durable findings to feature artifacts or memories, then evict the source.

---

## 3. The Memory Layer

The memory layer stores durable cross-feature knowledge that agents need repeatedly. It stays compact, reusable, and clearly separate from feature-specific artifacts.

### 3-Tier Memory Architecture

```mermaid
flowchart TD
    %% 3-Tier Memory Architecture (Instruction / Auto / Extracted)

    subgraph INSTR["Instruction Tier — Human-Curated, Durable"]
        CONST[core-policies.md<br/>Repo-wide rules]
        SEC[security-policy.md<br/>Trust boundaries]
        HARN[core-policies.md<br/>Canonical commands]
        PKB[project-knowledge-base.md<br/>Patterns, watchouts]
        HEUR[learned-heuristics.md<br/>Evidence-backed instincts]
        ARCH[docs/project/architecture.md<br/>System structure]
    end

    subgraph AUTO["Auto Tier — Failure-Driven, Append-Only"]
        OBS[harness-telemetry.md<br/>Harness/Model/Spec failures]
    end

    subgraph EXTR["Extracted Tier — Per-Feature Candidates"]
        EXT[artifacts/features/&lt;slug&gt;/<br/>session-extracts.md]
    end

    subgraph ROUTER["Memory Router"]
        IDX[INDEX.md<br/>Always-loaded routing index]
    end

    %% Routing
    IDX -->|Always group| CONST
    IDX -->|Always group| SEC
    IDX -->|Always group| HARN
    IDX -->|By-Intent: Knowledge| PKB
    IDX -->|By-Intent: Knowledge| ARCH
    IDX -->|By-Intent: Learned| HEUR
    IDX -->|By-Debug| OBS
    IDX -->|By-Debug| EXT

    %% Promotion flow (extracted -> instruction)
    EXT -.->|context-memory<br/>Extraction Triage| HEUR
    EXT -.->|promote rule| CONST
    EXT -.->|promote security| SEC
    OBS -.->|context-memory<br/>Triage| PKB
    OBS -.->|durable lesson| HEUR

    %% Writers
    AIDV[harness-verify<br/>Post-Ship Sync] -->|writes record| EXT
    AIHN[harness<br/>Improve Mode] -->|appends| OBS
    AIDS[context-session END] -->|appends candidates| EXT

    classDef instr fill:#10b981,stroke:#047857,color:#fff
    classDef auto fill:#f59e0b,stroke:#b45309,color:#fff
    classDef extr fill:#8b5cf6,stroke:#6d28d9,color:#fff
    classDef router fill:#3b82f6,stroke:#1d4ed8,color:#fff
    classDef writer fill:#fff,stroke:#0d0d0d,color:#0d0d0d

    class CONST,SEC,HARN,PKB,HEUR,ARCH instr
    class OBS auto
    class EXT extr
    class IDX router
    class AIDV,AIHN,AIDS writer
```

### Memory Files

#### Router
* **`INDEX.md`**: Declares Always / By-Intent / By-Debug groups. Sessions read this first.

#### Instruction Tier — Human-Curated, Durable
* **`core-policies.md`**: Normative repository rules tagged with `CC-*` identifiers. Update frequency is rare.
* **`security-policy.md`**: Permission model, sandbox guidelines, trust boundaries.
* **`core-policies.md`**: Commands, paths, trackers, and promotion thresholds.
* **`project-knowledge-base.md`**: Durable facts, conventions, and patterns.
* **`learned-heuristics.md`**: Evidence-backed execution patterns.
* **`docs/project/architecture.md`**: Component boundaries, seams, and layouts.

#### Auto Tier — Failure-Driven, Append-Only
* **`harness-telemetry.md`**: Tracks Harness/Model/Spec failure classifications. Written by `/harness-maintain` Improve Mode.

#### Extracted Tier — Per-Feature Candidates
* **`artifacts/features/<slug>/session-extracts.md`**: Candidate findings and observations compiled during session boundaries.

---

## 4. Promotion & Triage

Knowledge flows from local feature execution upward into instruction-tier memory via manual triage and automatic sweeps.

### Manual Promotion & Triage

When a finding is identified in a feature folder (`session-extracts.md` or `harness-telemetry.md`), run `/context-memory` to initiate Extraction Triage:

| Decision | Condition | Action |
|----------|-----------|--------|
| **Promote** | Repeated across 2+ features, evidence-backed, reusable | Write to Instruction Tier |
| **Defer** | Promising but needs further confirmations | Retain in candidate log |
| **Discard** | Feature-specific, obsolete, or incorrect | Discard with documented reason |

*Normative rules* (must/should) route to `core-policies.md` or `security-policy.md`.
*Descriptive facts* (uses/prefers) route to `project-knowledge-base.md` or `learned-heuristics.md`.

### Promotion Watchlist Thresholds
To prevent file bloat, memory segments are audited against these boundaries (from `core-policies.md`):
- Memory file length $\ge$ 800 lines (warning) / 1200 lines (hard limit).
- $\ge$ 3 distinct H2 subtopics covering separate concerns.
- $\ge$ 5 features referencing the same slice.

---

## 5. Self-Improving Knowledge Loop

Each feature release triggers a feedback loop: verification yields failures that upgrade the harness; successful verify sweeps compile findings for promotion.

```mermaid
flowchart LR
    %% Self-Improving KB Loop — ship to extract to triage to promote

    SHIP([Feature Ships<br/>harness-verify Pass]) --> SYNC[Post-Ship Sync<br/>context-memory sweep]

    SYNC -->|sweep every file in INDEX.md| FILES{Each memory file:<br/>update or justify untouched}

    FILES -->|durable lesson| EXT[Append candidate<br/>session-extracts.md]
    FILES -->|harness failure| OBS[Append entry<br/>harness-telemetry.md]
    FILES -->|no change| RECORD[Record reason in<br/>Post-Ship Sync block]

    EXT --> TRIAGE[context-memory<br/>Extraction Triage]
    OBS --> TRIAGE

    TRIAGE -->|repeated 2+ features| HEUR[Promote to<br/>learned-heuristics.md]
    TRIAGE -->|normative rule| CONST[Promote to<br/>core-policies.md]
    TRIAGE -->|durable pattern| PKB[Promote to<br/>project-knowledge-base.md]
    TRIAGE -->|security finding| SEC[Promote to<br/>security-policy.md]
    TRIAGE -->|defer| DEF[Wait for next signal]
    TRIAGE -->|feature-local| DISC[Discard<br/>with reason]

    HEUR --> SMARTER[KB grows<br/>next session is smarter]
    CONST --> SMARTER
    PKB --> SMARTER
    SEC --> SMARTER

    SMARTER -.->|loop back| SHIP

    classDef terminal fill:#0d0d0d,stroke:#0d0d0d,color:#fff
    classDef sync fill:#10b981,stroke:#047857,color:#fff
    classDef triage fill:#f59e0b,stroke:#b45309,color:#fff
    classDef promote fill:#3b82f6,stroke:#1d4ed8,color:#fff
    classDef discard fill:#fcf3f3,stroke:#f2c4c4,color:#c62828

    class SHIP,SMARTER terminal
    class SYNC,FILES,RECORD sync
    class TRIAGE,EXT,OBS triage
    class HEUR,CONST,PKB,SEC promote
    class DEF,DISC discard
```

### Post-Ship Sync Sequence

The `Post-Ship Sync` is a mandatory sequence after a passing verification. Generic skips (e.g., "No updates needed") are rejected.

```mermaid
sequenceDiagram
    autonumber
    participant V as harness-verify
    participant M as context-memory<br/>Post-Ship Sync
    participant I as INDEX.md
    participant F as Memory Files
    participant E as session-extracts.md
    participant S as status.md

    V->>V: Mechanical gate + Alignment + Security PASS
    V->>M: Hand off to Post-Ship Sync
    M->>I: Read every file listed
    I-->>M: Always + By-Intent + By-Debug groups
    loop For each file in INDEX.md
        M->>F: Read file
        alt Durable change found
            M->>E: Append candidate to ## Post-Ship Sync block
            M->>F: Apply diff
        else No change needed
            M->>E: Record file name + 1-line reason untouched
        end
    end
    M->>E: Verify every INDEX file accounted for
    alt Sweep complete
        M-->>V: OK — sync record present
        V->>S: Set phase = Done
    else Generic skip detected
        M-->>V: REJECT — re-run sweep
        Note over V,M: "No updates needed" without<br/>per-file reason fails the gate
    end

    Note over V,F: Profile gating:<br/>Tiny = heuristic-only sweep<br/>Standard+ = full sweep
```

---

## 6. Subagent-Driven Development (SDD)

Broad operations (such as codebase crawling, regression checks, or bulk file search) are delegated to isolated subagents to keep the main context window thin.

```mermaid
flowchart TD
    %% Subagent-Driven Development (SDD) — broad work delegated, only summaries return

    MAIN[Main Agent Loop<br/>lean context window]

    MAIN --> DECIDE{Broad / parallel work?<br/>multi-file search, research,<br/>stress-test, repetitive edits}
    DECIDE -- No --> INLINE[Handle inline<br/>in main context]
    DECIDE -- Yes --> SPAWN[Spawn subagents]

    SPAWN --> SA1[Subagent A<br/>isolated context]
    SPAWN --> SA2[Subagent B<br/>isolated context]
    SPAWN --> SA3[Subagent C<br/>isolated context]

    SA1 -->|raw exploration<br/>stays isolated| R1[Summary Report A]
    SA2 -->|raw exploration<br/>stays isolated| R2[Summary Report B]
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
    class SA1,SA2,SA3 sub
    class R1,R2,R3 report
    class DECIDE decision
```

### Context Engineering & Memory Routing
The kit utilizes a 6-tier context assembly framework guided by `INDEX.md`.

```mermaid
flowchart TD
    T1["Tier 1 — Router<br/>AGENTS.md + INDEX.md"]:::router
    T2["Tier 2 — Repo Memory (Always)<br/>constitution + security + harness-config"]:::router
    T3["Tier 3 — Repo Memory (By Intent)<br/>Knowledge / Learned / Debug groups"]:::intent
    T4["Tier 4 — Feature Artifacts<br/>status / spec / plan / tasks / handoff"]:::feature
    T5["Tier 5 — Raw Code (JIT)<br/>only files for immediate task"]:::code
    T6["Tier 6 — Transient Logs<br/>ephemeral tool output"]:::logs

    T1 --> T2 --> T3 --> T4 --> T5 --> T6
    T6 -.->|summarize & evict| T4

    classDef router fill:#0f172a,stroke:#38bdf8,color:#fff
    classDef intent fill:#1e1b4b,stroke:#818cf8,color:#fff
    classDef feature fill:#311042,stroke:#c084fc,color:#fff
    classDef code fill:#1c1917,stroke:#a8a29e,color:#fff
    classDef logs fill:#27272a,stroke:#71717a,color:#a1a1aa
```

* **Smart Intent Routing:** Trigger keywords in `INDEX.md` successfully segment memory loading.
* **Confidence-Scored Loading:** High-confidence matches (3+ keywords) load full groups, while low-confidence (≤2 keywords) load only group headers. This partial load keeps context windows clean.
* **Compaction Gaps:** Compaction strategies (Summarize, Scope-narrow, Evict, Promote) are clearly documented but lack script-driven utilities.
