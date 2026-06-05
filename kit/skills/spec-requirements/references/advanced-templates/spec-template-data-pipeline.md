# Spec Template: Data Pipeline

<!-- Use this template when the feature involves data ingestion, transformation, validation, or delivery. Extends the standard spec template with pipeline-specific sections. -->

## Problem Statement

## Target Users

## Pipeline Architecture

### Data Sources

| Source | Format | Volume | Frequency | Auth |
|--------|--------|--------|-----------|------|
| | | | | |

### Transformations

| Step | Input | Output | Logic | Error Handling |
|------|-------|--------|-------|----------------|
| | | | | |

### Data Destinations

| Destination | Format | Delivery | SLA | Retry Policy |
|-------------|--------|----------|-----|--------------|
| | | | | |

### Data Flow

```
[Source] → [Ingestion] → [Validation] → [Transform] → [Load] → [Destination]
```

## Data Quality Requirements

| Dimension | Requirement | Measurement | Threshold |
|-----------|-------------|-------------|-----------|
| Completeness | | | |
| Accuracy | | | |
| Timeliness | | | |
| Consistency | | | |
| Uniqueness | | | |

## Scenarios

### S1: [Happy path — full pipeline run]

### S2: [Partial failure — source unavailable]

### S3: [Data quality violation — invalid records]

### S4: [Backfill — reprocess historical data]

## Requirements

- **REQ-1:** 
- **REQ-2:** 

## Acceptance Criteria

- **AC-1 (REQ-1):** Proof:
- **AC-2 (REQ-2):** Proof:

## Pipeline-Specific Constraints

### Volume & Performance

- Expected daily volume:
- Peak throughput:
- Latency SLA (end-to-end):
- Batch window:

### Error Handling

| Error Type | Strategy | Alert | Recovery |
|------------|----------|-------|----------|
| Source unavailable | | | |
| Schema mismatch | | | |
| Validation failure | | | |
| Destination full | | | |

### Idempotency & Ordering

- Idempotent: [Yes/No — can the pipeline be safely re-run?]
- Ordering guarantee: [None / At-least-once / Exactly-once]
- Deduplication strategy:

### Monitoring & Observability

- Pipeline health metric:
- Data quality metric:
- Alerting threshold:
- Dashboard:

## Verification Surface

- Unit tests:
- Integration tests:
- Data quality tests:
- End-to-end pipeline test:
- Performance/load test:

## Gray-Area Decisions

## Scope

### In Scope

### Out of Scope

### Non-Goals
