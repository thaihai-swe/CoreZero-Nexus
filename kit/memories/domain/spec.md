# Example Domain — Canonical Spec

*This file is the single source of truth for the `example` domain's behavior.
Replace this scaffold with your actual domain rules. Brownfield refactors that
touch this domain MUST add a `## Delta` section to their feature `spec.md` (see
`skills/spec-requirements/references/delta-spec-operations.md`) instead of
restating these rules.*

## Status

- **Owner:**
- **Created:** YYYY-MM-DD
- **Last merged delta:** none yet
- **Active features touching this domain:** none

## Scope

What this domain owns:

- (Replace with the responsibilities canonical to this domain.)

What this domain does **not** own (cross-reference the domain that does):

-

## Functional Requirements

*Each requirement is canonical for this domain. Features that change a
requirement file a `MODIFIED Requirement` delta; features that retire one
file a `REMOVED Requirement` delta. Renumber only on merge.*

### REQ-001

- Requirement:
- Why it matters:
- Validation surface:
- First introduced by feature:

*(Add REQ-002, REQ-003, ... as the domain grows. Numbering is stable across
deltas — never re-pack IDs after a `REMOVED` merge; mark the slot
`Retired in <feature-slug> on <date>` and skip it.)*

## Non-Functional Requirements

- NFR-001 Performance:
- NFR-002 Reliability:
- NFR-003 Security or Privacy:

## Acceptance Criteria

- [ ] AC-001 Linked REQ:
  - Validation method:
  - Proof target:
  - Test path:

*(Acceptance criteria here describe the domain's *current* contract. Per-feature
ACs live in feature `spec.md`; only ACs that survive a feature's lifecycle and
become permanent contract get merged here.)*

## Delta History

*Append a one-line entry per merged feature delta. Most recent first. The full
delta block stays in the feature's archived `spec.md`.*

| Date | Feature slug | Net effect (brief) |
|---|---|---|
| YYYY-MM-DD | example-feature | Added REQ-001 and AC-001 |
