# Example Domain — Boundary Rules

Defines what this domain owns, does not own, and how it integrates with adjacent domains.
Replace with your domain's actual boundaries.

## Owns

- The core business entities and their lifecycle rules
- State transition logic and validation
- Domain events emitted when state changes
- The domain interface contracts (ports)

## Does Not Own

- Persistence mechanics (SQL queries, ORM mappings) — owned by Infrastructure
- HTTP request/response shaping — owned by API/Transport layer
- Authentication and session management — owned by Auth domain
- Notification delivery (email, SMS, push) — owned by Notification domain

## Integration Contracts

| Produces | Consumed By | Contract |
|---|---|---|
| Domain events | Event bus | Immutable event schema, versioned |
| Domain objects | Application services | Via repository port interface |

## Change Rules

- Domain interfaces are stable contracts. Changes require an ADR.
- Domain events are append-only. New fields may be added; existing fields must not be removed.
- Cross-domain calls go through declared integration contracts only — never direct imports.
