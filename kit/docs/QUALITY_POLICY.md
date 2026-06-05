# Quality Policy

<!-- Defines code quality standards, review processes, and tech debt management. /harness-verify and /spec-plan reference this for gate checks and design constraints. -->

## Code Quality Gates

### Automated Gates (Must Pass)

| Gate | Tool | Threshold | Blocking |
|------|------|-----------|----------|
| Tests | | 100% pass | Yes |
| Lint | | 0 errors | Yes |
| Type check | | 0 errors | Yes |
| Coverage | | ≥ X% | |
| Bundle size | | ≤ X KB | |
| Security scan | | 0 critical/high | |

### Manual Gates (Required Review)

| Gate | Reviewer | Criteria | Required For |
|------|----------|----------|--------------|
| Code review | | | |
| Design review | | | |
| Security review | | | |
| Accessibility review | | | |

## Review Standards

### Code Review Checklist

- [ ] Changes match the spec and plan
- [ ] No unrelated changes included
- [ ] Tests cover new behavior
- [ ] Error handling is appropriate
- [ ] No security vulnerabilities introduced
- [ ] Performance impact considered
- [ ] Naming is clear and consistent with glossary
- [ ] No dead code or commented-out blocks

### Review Turnaround

| Priority | SLA | Escalation |
|----------|-----|------------|
| Critical (blocking deploy) | | |
| Normal | | |
| Low (refactoring, docs) | | |

## Testing Standards

### Test Pyramid

| Level | Purpose | Speed | Coverage Target |
|-------|---------|-------|-----------------|
| Unit | Isolated logic | Fast | |
| Integration | Component interaction | Medium | |
| E2E | User journeys | Slow | |
| Contract | API compatibility | Fast | |

### Testing Requirements by Risk

| Risk Level | Unit | Integration | E2E | Manual |
|------------|------|-------------|-----|--------|
| Low | Required | Optional | No | No |
| Medium | Required | Required | Optional | No |
| High | Required | Required | Required | Required |
| Critical | Required | Required | Required | Required + sign-off |

## Tech Debt Management

### Classification

| Category | Description | Example |
|----------|-------------|---------|
| Deliberate | Conscious tradeoff with plan to fix | "Ship without caching, add in v2" |
| Accidental | Discovered after the fact | "This abstraction doesn't scale" |
| Bit rot | Gradual degradation | "Dependencies 2 major versions behind" |
| Environmental | External changes | "API deprecated, migration needed" |

### Debt Threshold

- Maximum open critical debt items:
- Maximum age for high-severity debt:
- Debt review cadence:
- Debt budget per sprint/cycle: [% of capacity]

### Debt Tracking

All tech debt is tracked in [TECH_DEBT_REGISTER.md](TECH_DEBT_REGISTER.md).

## Documentation Standards

- Public APIs: Must have usage examples
- Complex logic: Must have inline explanation of WHY
- Architecture changes: Must have ADR
- New features: Must have spec + plan artifacts
