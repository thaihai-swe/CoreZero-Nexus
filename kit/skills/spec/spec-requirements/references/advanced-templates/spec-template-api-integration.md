# Spec Template: API Integration

<!-- Use this template when the feature involves building, consuming, or integrating with APIs (REST, GraphQL, gRPC, webhooks). Extends the standard spec template with integration-specific sections. -->

## Problem Statement

## Target Users

## Integration Architecture

### API Overview

| Endpoint | Method | Purpose | Auth | Rate Limit |
|----------|--------|---------|------|------------|
| | | | | |

### Request/Response Contracts

#### [Endpoint Name]

**Request:**
```json
{
}
```

**Response (success):**
```json
{
}
```

**Response (error):**
```json
{
}
```

### Authentication & Authorization

- Auth method: [API Key | OAuth2 | JWT | mTLS | None]
- Token refresh strategy:
- Secret storage:
- Scope/permissions required:

### Dependencies

| External Service | Purpose | SLA | Fallback |
|-----------------|---------|-----|----------|
| | | | |

## Scenarios

### S1: [Happy path — successful API call]

### S2: [Timeout — external service is slow]

### S3: [Rate limited — 429 response]

### S4: [Auth failure — expired or invalid credentials]

### S5: [Breaking change — upstream schema changes]

## Requirements

- **REQ-1:** 
- **REQ-2:** 

## Acceptance Criteria

- **AC-1 (REQ-1):** Proof:
- **AC-2 (REQ-2):** Proof:

## Integration-Specific Constraints

### Resilience

| Pattern | Implementation | Config |
|---------|---------------|--------|
| Retry | | Max attempts:, Backoff: |
| Circuit breaker | | Threshold:, Recovery: |
| Timeout | | Connect:, Read: |
| Fallback | | Strategy: |

### Versioning & Compatibility

- API version strategy: [URL path | Header | Query param]
- Breaking change handling:
- Deprecation policy:

### Data Mapping

| External Field | Internal Field | Transform | Validation |
|---------------|---------------|-----------|------------|
| | | | |

### Webhook Handling (if applicable)

- Endpoint:
- Signature verification:
- Idempotency key:
- Retry expectations from sender:

## Verification Surface

- Unit tests: (mock external calls)
- Integration tests: (real or sandbox calls)
- Contract tests: (schema validation)
- Resilience tests: (timeout, retry, circuit breaker)

## Gray-Area Decisions

## Scope

### In Scope

### Out of Scope

### Non-Goals
