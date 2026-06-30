# Task Breakdown

## Metadata
- Feature name:
- Feature slug:
- Date:
- Status:

## Heuristic Citations

*Optional. Cite any LH-* IDs applied in the design or execution of these tasks.*
- LH-NNN: <brief description>

## Task Block Format

Every task uses this canonical block. Repeat per task; assign sequential `TASK-NNN` IDs grouped under phases.

```
- [ ] TASK-NNN-<Mark `[P]` only when truly independent>
  Status: Not Started                # Not Started | In Progress | Blocked | Done | Deferred
  Routing: AFK                       # AFK = unsupervised mechanical | HITL = human checkpoint required
  Summary:
  Outcome enabled:                   # link to user scenario or outcome when relevant
  Plan reference:                    # plan phase or task this came from
  Linked requirement(s):             # REQ-XXX
  Linked acceptance criteria:        # AC-XXX
  User story:                        # US-XXX (P1|P2|P3) — empty for Setup/Foundational/
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

*(Repeat the phase block below for each phase defined in the plan: Setup, Foundational, Story P1, Story P2, Polish, etc.)*

### Phase N: [Phase Name]
Goal:
Story ID:                                # US-XXX (if applicable)
Priority:                                # P1|P2|P3 (if applicable)
Acceptance criteria covered:             # AC-XXX, AC-XXX
Independent proof:                       # exact command(s) that pass once this phase ships
Completion criteria:
- [ ] CC-NNN [Criterion description]
Tasks:
- [ ] TASK-NNN [Task summary]

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
