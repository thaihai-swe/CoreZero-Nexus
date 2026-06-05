# Tech Debt Register

<!-- Tracked debt items discovered during implementation or verification. /harness-verify fallow pass routes debt here. Review regularly to prevent accumulation. -->

## Purpose

Provide a single, visible registry of all known technical debt. Each item has an owner, severity, and resolution plan so debt doesn't silently accumulate.

## Active Debt

| ID | Title | Severity | Category | Owner | Discovered | Target Resolution | Status |
|----|-------|----------|----------|-------|------------|-------------------|--------|
| TD-001 | | [Critical \| High \| Medium \| Low] | [Deliberate \| Accidental \| Bit rot \| Environmental] | | YYYY-MM-DD | YYYY-MM-DD | [Open \| In Progress \| Resolved] |

## Entry Format

### TD-XXX: [Title]

- **Severity:** [Critical | High | Medium | Low]
- **Category:** [Deliberate | Accidental | Bit rot | Environmental]
- **Discovered:** YYYY-MM-DD
- **Source:** [Feature slug, verify fallow pass, code review, etc.]
- **Owner:** 
- **Description:** [What the debt is and why it exists]
- **Impact:** [What happens if we don't fix it]
- **Resolution Plan:** [How to fix it]
- **Target Date:** YYYY-MM-DD
- **Dependencies:** [What must happen first]
- **Status:** [Open | In Progress | Resolved]

## Resolved Debt

<!-- Move items here when resolved. Keep for historical reference. -->

| ID | Title | Resolved Date | Resolution |
|----|-------|---------------|------------|
| | | | |

## Metrics

- Total open items:
- Critical/High open:
- Average age (days):
- Resolution rate (items/month):
- Oldest unresolved:

## Review Cadence

- Weekly: Review Critical and High items
- Monthly: Review all open items, update metrics
- Quarterly: Assess debt budget and capacity allocation
