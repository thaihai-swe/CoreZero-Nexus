# System Specification Template

Use this template when the request is cross-cutting — it spans multiple features, defines a repo-wide policy, or establishes a technical standard that downstream feature specs must anchor to.

Output path: `docs/system-specs/<name>.md`

---

## Metadata

- System spec name:
- Slug:
- Owner:
- Status: Draft | In Review | Approved | Superseded
- Last updated:
- Affected features:

## Problem Statement

What cross-cutting problem or policy gap does this spec address? Why does it need to be resolved at the system level rather than inside a single feature spec?

## Desired Outcomes

- Outcome 1:
- Outcome 2:

## Scope

### In Scope

- Item 1:

### Out Of Scope

- Item 1:

### Non-Goals

- Non-goal 1:

## Affected Features And Boundaries

| Feature / Area | Impact | Must Comply By |
|---|---|---|
| | | |

## Policy Decisions

Record the cross-cutting decisions this spec locks. These become constraints that downstream feature specs must respect.

| ID | Decision | Rationale | Locked |
|---|---|---|---|
| POL-001 | | | Yes / Pending |

## Migration Impact

- What existing behavior must change:
- What existing behavior must be preserved:
- Migration sequencing (which features change first):
- Rollback posture if migration fails:

## Downstream Spec Anchoring

List the feature specs that must reference this system spec and the specific sections they must comply with.

| Feature Spec | Section to anchor | Compliance check |
|---|---|---|
| | | |

## Acceptance Criteria

- [ ] AC-001: All affected features have updated their specs to reference this system spec
- [ ] AC-002: Policy decisions are reflected in `memories/repo/constitution.md` or `security-policy.md` as appropriate
- [ ] AC-003: Migration sequencing is documented and agreed

## Open Questions

- Q-001 Question:
  Type: Blocking | Non-blocking
  Owner:
  Next step:

## Notes

Supporting context, links, or references.
