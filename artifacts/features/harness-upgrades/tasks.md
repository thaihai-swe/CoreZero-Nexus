# Task Breakdown

## Metadata

- Feature name: Harness Upgrades (Context, Provenance, Memory)
- Related spec / plan / design: `plan.md`
- Owner: Agent
- Last updated: 2026-06-05

## Rules

- Keep tasks proportional to delivery profile; Tiny stays compact.
- Each task small, testable, and traceable to REQ/AC/plan.
- Mark `[P]` only when truly independent (no write/contract conflicts); state ownership boundary.
- Prefer explicit file/module targets when known.
- First unblocked task must be executable from this file alone.
- Task states: `Not Started` | `In Progress` | `Blocked` | `Done` | `Deferred`.
- Behavior-changing tasks: name the failing proof/test expected before the fix (TDD: RED → GREEN).
- Don't finalize until REQ → AC → TASK → validation coverage is complete.

## Phases

### Phase 1: Context & Provenance
Goal: Enable partial context loading and enforce execution decision provenance.
Completion criteria:
- [ ] CC-001: INDEX.md and session skills updated to handle `partial-load`.
- [ ] CC-002: spec-implement skill enforces Decision Record blocks.

Tasks:
- [x] TASK-001
  Status: Done
  Routing: AFK
  Summary: Update INDEX.md to document the `partial-load` keyword modifier logic.
  Outcome enabled: Context Intelligence
  Plan reference: Phase 1
  Linked requirement(s): REQ-001
  Linked acceptance criteria: N/A
  Ownership boundary: 
  Affected file(s) or module(s): `kit/memories/repo/INDEX.md`
  Depends on: 
  Can run in parallel: yes
  Proving command or proof: Validate markdown formatting
  Validation evidence: 
  Session note: 

- [x] TASK-002
  Status: Done
  Routing: AFK
  Summary: Update context-session SKILL.md to parse and respect `partial-load` modifiers.
  Outcome enabled: Context Intelligence
  Plan reference: Phase 1
  Linked requirement(s): REQ-001
  Linked acceptance criteria: N/A
  Ownership boundary: 
  Affected file(s) or module(s): `kit/skills/context-session/SKILL.md`
  Depends on: TASK-001
  Can run in parallel: no
  Proving command or proof: Validate markdown formatting
  Validation evidence: 
  Session note: 

- [x] TASK-003
  Status: Done
  Routing: AFK
  Summary: Update spec-implement SKILL.md to require Decision Records in progress files for mid-flight execution decisions.
  Outcome enabled: Decision Provenance
  Plan reference: Phase 1
  Linked requirement(s): REQ-002
  Linked acceptance criteria: N/A
  Ownership boundary: 
  Affected file(s) or module(s): `kit/skills/spec-implement/SKILL.md`
  Depends on: 
  Can run in parallel: yes
  Proving command or proof: Validate markdown formatting
  Validation evidence: 
  Session note: 

### Phase 2: Memory Architecture
Goal: Enable semantic graph links and auto-promotions via recurrence counts.
Completion criteria:
- [ ] CC-003: learned-heuristics template includes recurrence-count.
- [ ] CC-004: context-memory skill enforces semantic graph links and count logic.

Tasks:
- [x] TASK-004
  Status: Done
  Routing: AFK
  Summary: Add `recurrence-count` and graph linking requirements to `learned-heuristics-template.md`.
  Outcome enabled: Cross-Feature Pattern Surfacing
  Plan reference: Phase 2
  Linked requirement(s): REQ-003, REQ-004
  Linked acceptance criteria: N/A
  Ownership boundary: 
  Affected file(s) or module(s): `kit/skills/context-memory/references/learned-heuristics-template.md`
  Depends on: 
  Can run in parallel: yes
  Proving command or proof: Validate markdown formatting
  Validation evidence: 
  Session note: 

- [x] TASK-005
  Status: Done
  Routing: AFK
  Summary: Update context-memory SKILL.md to instruct agents on incrementing recurrence-counts and enforcing semantic graph links.
  Outcome enabled: Semantic Memory Graph
  Plan reference: Phase 2
  Linked requirement(s): REQ-003, REQ-004
  Linked acceptance criteria: N/A
  Ownership boundary: 
  Affected file(s) or module(s): `kit/skills/context-memory/SKILL.md`
  Depends on: TASK-004
  Can run in parallel: no
  Proving command or proof: Validate markdown formatting
  Validation evidence: 
  Session note: 

## Completion Notes

- What was delivered: All 4 ecosystem harness upgrades (Confidence-Scored Loading, Decision Provenance Records, Cross-Feature Pattern Surfacing, Semantic Memory Knowledge Graph).
- What was deferred: None.
- What needs follow-up: Monitoring `INDEX.md` loading behavior in future sessions to ensure partial-loading reduces token bloat effectively.

## Resume Notes

- Current phase: Phase 1
- Next recommended task: TASK-001
- Active blocker: None
- Last validation evidence added: N/A
- Exact next command or proof to run: Read targets to prepare for updates.
