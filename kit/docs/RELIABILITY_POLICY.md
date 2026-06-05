# Reliability Policy

<!-- Defines operational reliability requirements for the project. /harness-verify and /spec-plan reference this when designing for production readiness. -->

## Service Level Objectives

| Service / Endpoint | Availability | Latency (p95) | Latency (p99) | Error Rate |
|-------------------|--------------|---------------|---------------|------------|
| | | | | |

## Error Budgets

| Service | Budget Period | Budget | Current Burn Rate | Action Threshold |
|---------|-------------|--------|-------------------|-----------------|
| | | | | |

<!-- When error budget is exhausted: freeze non-critical deployments, focus on reliability work. -->

## Observability Requirements

### Logging

- Log format:
- Required fields:
- Retention:
- Sensitive data handling:

### Metrics

| Metric | Type | Labels | Alert Threshold |
|--------|------|--------|-----------------|
| | | | |

### Tracing

- Tracing provider:
- Sampling rate:
- Required spans:
- Trace retention:

### Dashboards

| Dashboard | Purpose | Owner | URL |
|-----------|---------|-------|-----|
| | | | |

## Incident Response

### Severity Levels

| Level | Criteria | Response Time | Escalation |
|-------|----------|---------------|------------|
| SEV-1 | | | |
| SEV-2 | | | |
| SEV-3 | | | |

### On-Call

- Rotation:
- Escalation path:
- Runbook location:

### Post-Incident

- Blameless postmortem required for: [SEV-1 | SEV-1 + SEV-2]
- Postmortem template:
- Action item tracking:
- Review cadence:

## Disaster Recovery

- RPO (Recovery Point Objective):
- RTO (Recovery Time Objective):
- Backup strategy:
- Failover mechanism:
- DR test cadence:

## Capacity Planning

- Current headroom:
- Growth projection:
- Scaling strategy: [Horizontal | Vertical | Auto]
- Load test cadence:
