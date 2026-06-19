# Feature Specification

## Metadata

- Feature name:
- Feature slug:
- Owner:
- Status: Draft | In Review | Approved | In Progress | Done
- Last updated:
- Related knowledge artifact(s):

## Problem Statement

What problem are we solving, for whom, and why now?

## Desired Outcomes

- Outcome 1:

## Minimum Release Slice

- What ships in the first useful release:
- What can wait:

## Success Criteria

- SC-001:

## In Scope

- Item 1:

## Out Of Scope

- Item 1:

## Non-Goals

- Non-goal 1:

## Users And Stakeholders

- Primary users:
- Secondary stakeholders:

## User Stories And Key Scenarios

- US-001:

### Detailed Scenarios

- **Scenario 1 (Happy Path):**
  - **Given:**
  - **When:**
  - **Then:**
- **Scenario 2 (Edge Case):**
  - **Given:**
  - **When:**
  - **Then:**
- **Scenario 3 (Error State):**
  - **Given:**
  - **When:**
  - **Then:**

## Current Context

*Brownfield only. Leave blank for greenfield.*

- **Current behavior summary:**
- **Impacted boundaries:**
- **Preserved behavior:**
- **Brownfield risk rating:** Low | Medium | High
  - Low: isolated area, strong test coverage, no external dependents
  - Medium: shared module, partial coverage, or known fragile integrations
  - High: load-bearing path, weak coverage, external dependents, or migration required

## Delta

*Optional. Fill in only when this feature modifies a canonical domain spec at `memories/domain/spec.md`. Skip for greenfield features and for brownfield features that do not touch a tracked domain. Required for Complex brownfield features whose `Impacted boundaries` overlap a domain pack listed in `MASTER_INDEX.md`.*

The delta names what changes against the canonical spec — not what the feature does in total. A reader of the canonical spec plus this delta should see the post-merge target state.

- **Target domain spec:** `memories/domain/spec.md`
- **Domain pack triggers matched:** <list keywords from the pack's `glossary.md` frontmatter that this feature exercises>

### ADDED Requirements

*New REQ-IDs that did not exist in the canonical spec. Each entry must use the same `REQ-NNN` block format as `## Functional Requirements`.*

- REQ-NNN (ADDED):

### MODIFIED Requirements

*Existing REQ-IDs whose behavior, priority, or validation surface changes. Quote the canonical text being replaced and give the new text. The merge rule in `references/delta-spec-operations.md` rejects a MODIFIED entry that does not show a before/after.*

- REQ-NNN (MODIFIED):
  - Before: <quote from canonical spec>
  - After: <new text>
  - Reason:

### REMOVED Requirements

*Existing REQ-IDs that no longer apply after this feature ships. Removed requirements must name the migration or compensating behavior — silent removal is rejected.*

- REQ-NNN (REMOVED):
  - Reason:
  - Migration / compensating behavior:

The merge into `memories/domain/spec.md` happens during `/harness-verify` post-ship sync per `kit/skills/spec/spec-requirements/references/delta-spec-operations.md`. The feature's own `## Functional Requirements` section remains the source of truth for what was built; the delta exists so the canonical spec stays accurate after this feature lands.

## Gray-Area Decisions

- Locked decisions that shape this spec:
- Remaining decisions that still block approval:

## Dependencies And External Touchpoints

- DEP-001:

## Functional Requirements

### REQ-001

- Requirement:
- Why it matters:
- Impacted users or scenarios:
- Related success criteria:
- Priority: Must Have | Should Have | Could Have
- Acceptance notes:
- Validation surface:

*(Add REQ-002, REQ-003, ... as needed using the same fields.)*

## Non-Functional Requirements

- NFR-001 Performance:
- NFR-002 Reliability:
- NFR-003 Security or Privacy:
- NFR-004 Accessibility:
- NFR-005 Observability:
- NFR-006 Compliance:

## Constraints

- Technical:
- Business:
- Delivery:

## Assumptions

- ASM-001:

## Risks

- RISK-001 Risk / Mitigation:

## Open Questions

- Q-001 Question:
  - Type: Blocking | Non-blocking
  - Owner:
  - Next step:

## Acceptance Criteria

- [ ] AC-001 Linked REQ:
  - Linked scenario or success criteria:
  - Validation method:
  - Proof target:
  - Scenario (Given / When / Then):           # recommended for high-risk or user-visible behaviors
    - Given:
    - When:
    - Then:
  - Test path:                                 # file path or test name exercising the scenario above; matches Proof target

*(Add AC-002, AC-003, ... as needed. Each AC should have at least one scenario block when the behavior is user-visible, security-sensitive, or high-risk.)*

## Notes

Supporting context, links, or references.
