# Task Breakdown

## Metadata

- Feature name:
- Related spec / plan / design:
- Owner:
- Last updated:

## Rules

- Keep tasks proportional to delivery profile; Tiny stays compact.
- Each task small, testable, and traceable to REQ/AC/plan.
- Mark `[P]` only when truly independent (no write/contract conflicts); state ownership boundary.
- Prefer explicit file/module targets when known.
- First unblocked task must be executable from this file alone.
- Task states: `Not Started` | `In Progress` | `Blocked` | `Done` | `Deferred`.
- Behavior-changing tasks: name the failing proof/test expected before the fix (TDD: RED → GREEN).
- Don't finalize until REQ → AC → TASK → validation coverage is complete.

## Task Block Format

Every task uses this canonical block. Repeat per task; assign sequential `TASK-NNN` IDs grouped under phases.

```
- [ ] TASK-NNN
  Status: Not Started                # Not Started | In Progress | Blocked | Done | Deferred
  Routing: AFK                       # AFK = unsupervised mechanical | HITL = human checkpoint required
  Summary:
  Outcome enabled:                   # link to user scenario or outcome when relevant
  Plan reference:                    # plan phase or task this came from
  Linked requirement(s):             # REQ-XXX
  Linked acceptance criteria:        # AC-XXX
  Ownership boundary:                # required if [P]
  Affected file(s) or module(s):
  Depends on:                        # other TASK-IDs
  Can run in parallel:               # yes/no; if yes, also fill Ownership boundary
  Proving command or proof:          # exact command, test, scenario, or log
  Validation evidence:               # filled after run; passing output or pointer
  Session note:                      # blockers, progress, HITL checkpoint description
```

`[ ]` toggles to `[X]` when `Status: Done`. Implementation agent must keep checkbox and Status aligned.

## Phases

Default scaffold — adjust phase count and goals to the plan.

### Phase 1: Foundations
Goal:
Completion criteria:
- [ ] CC-001
Tasks:
- [ ] TASK-001 …  (use the block above)

### Phase 2: Core Implementation
Goal:
Completion criteria:
- [ ] CC-002
Tasks:
- [ ] TASK-… …

### Phase 3: Validation And Closeout
Goal:
Completion criteria:
- [ ] CC-003
Tasks:
- [ ] TASK-… …

## Notes Per Task

Add `### TASK-NNN` subsections only when notes exceed the inline `Session note` field.

## Completion Notes

- What was delivered:
- What was deferred:
- What needs follow-up:

## Resume Notes

- Current phase:
- Next recommended task:
- Active blocker:
- Last validation evidence added:
- Exact next command or proof to run:
