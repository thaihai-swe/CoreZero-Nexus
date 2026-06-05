# Governance

<!-- Defines approval workflows, ownership, and decision-making processes for teams using the kit. Commands like /spec-requirements and /harness-verify reference this to enforce review requirements. -->

## Approval Gates

<!-- Who must approve before work proceeds to the next phase? -->

| Phase Transition | Approver | Method | SLA |
|-----------------|----------|--------|-----|
| Spec → Plan | | | |
| Plan → Implement | | | |
| Implement → Verify | | | |
| Verify → Done | | | |
| ADR → Accepted | | | |

## Spec Ownership

<!-- Who owns which domain? The owner is responsible for spec quality and approval. -->

| Domain / Area | Owner | Backup | Notes |
|---------------|-------|--------|-------|
| | | | |

## Risk Classification

<!-- How to classify feature risk. Higher risk = more ceremony. -->

| Risk Level | Criteria | Required Ceremony |
|------------|----------|-------------------|
| Low | Reversible, isolated, no auth/data/billing impact | Tiny profile, self-approve |
| Medium | Touches shared state, moderate blast radius | Standard profile, peer review |
| High | Auth, payments, data migration, cross-service | Complex profile, senior review |
| Critical | Security, compliance, production data, irreversible | Complex + ADR + explicit sign-off |

## Review Workflows

### Spec Review

- **Reviewer:** 
- **Criteria:** Readiness score ≥ 19/30, no dimension scored 1
- **Turnaround:** 
- **Escalation:** If not reviewed within SLA, escalate to:

### Code Review

- **Reviewer:** 
- **Criteria:** Passes mechanical gate, alignment audit clean
- **Required for:** [All changes | Medium+ risk | High+ risk]
- **Turnaround:** 

### ADR Review

- **Reviewer:** 
- **Criteria:** At least 2 options evaluated, consequences documented
- **Required for:** All architecture decisions
- **Turnaround:** 

## Change History Requirements

<!-- What must be recorded when artifacts change? -->

- Spec changes after lock: Require re-approval and version bump
- Plan changes after approval: Document reason in progress.md
- Constitution amendments: Require version bump and evidence
- Security policy changes: Require explicit sign-off

## Escalation Paths

<!-- When to escalate and to whom. -->

| Situation | Escalate To | Method |
|-----------|-------------|--------|
| Blocked > 24h | | |
| Scope disagreement | | |
| Security concern | | |
| Spec contradiction | | |
| Harness failure (repeated) | | |

## Role-Based Access

<!-- What can each role do within the kit workflow? -->

| Role | Can Approve Specs | Can Approve Plans | Can Merge | Can Amend Constitution |
|------|-------------------|-------------------|-----------|----------------------|
| | | | | |

## Audit Trail

<!-- What gets recorded for compliance and traceability. -->

- All phase transitions recorded in `status.md`
- All approvals recorded in `progress.md`
- All decisions recorded in ADRs or spec gray-area sections
- All harness failures recorded in `observability-log.md`
- All memory promotions include evidence and source
