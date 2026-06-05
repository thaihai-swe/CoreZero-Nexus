# Architecture

Living architecture doc for the repository. Skills (`spec-plan`, `spec-research`, `context-memory`, `starter-init`) read it for boundaries, data flow, and safe-change guidance. Update as the system evolves.

## Purpose

Capture durable system structure so agents don't reinfer boundaries every session.

**Use for:** system decomposition, module/boundary ownership, integration seams, runtime/deployment shape, durable architectural decisions broader than one feature.

**Don't use for:** feature-local design, speculative future architecture, task lists, or restating every file.

---

## System Snapshot

- Repository type:           <!-- REST API monolith | microservices | monorepo | CLI | full-stack web app -->
- Primary runtime(s):        <!-- e.g. Node.js 20, Python 3.11 -->
- Main entrypoints:          <!-- e.g. src/index.ts, cmd/server/main.go -->
- Deployment shape:          <!-- e.g. Docker on AWS ECS, Vercel edge -->
- Confidence:                High | Medium | Low

---

## Top-Level Components

| Component | Responsibility | Key Paths | Depends On | Notes |
| --- | --- | --- | --- | --- |
|   |   |   |   |   |

> Example row: `Auth Service | Login, JWT, sessions | src/auth/ | Postgres, Redis | All routes pass through auth middleware`

---

## Runtime Boundaries

A boundary is a line code must not cross without an explicit contract (API call, queue, DB query).

- Boundary:
  Owner:
  Why it exists:
  Crossing rule:
  Evidence:

> Example: `API ↔ Database`, owner Backend, prevents direct DB access from frontend, only via repository layer in `src/db/`, evidence `src/db/index.ts` is sole DB import point.

---

## Data And Control Flow

Trace primary paths that cross boundaries.

- Flow:
  Starts at:
  Passes through:
  Ends at:
  Why it matters:

> Example: `User login` — `POST /auth/login` → `AuthService.validateCredentials` → `UserRepository.findByEmail` → `JWTService.sign` → JWT to client, refresh in Redis. All authenticated requests depend on this.

---

## External Integrations

| Integration | Purpose | Protocol | Auth Method | Failure/Latency Watchout |
| --- | --- | --- | --- | --- |
|   |   |   |   |   |

> Example row: `Stripe | Payments | HTTPS REST | API key (env STRIPE_SECRET_KEY) | Webhook delays up to 72h; verify event signatures`

---

## Runtime Environment

- Production:
- Staging:
- Local dev:
- CI/CD:

---

## Architectural Decisions

Key choices already made. Link to ADRs when they exist.

- Decision:
  Status:               <!-- Accepted | Superseded | Under Review -->
  Why:
  Evidence:
  Related artifact:

> Example: Use JWTs over server-side sessions — Accepted — mobile clients need stateless auth; horizontal scaling simpler — `artifacts/features/auth-system/adr-001.md`.

---

## Safe Change Guidance

### High-Risk Areas

- Area:
  Watch for:
  Validation needed:

### Safe Areas

- Area:
  Why isolated:

### Cross-Cutting Concerns

- Concern:
  Affects:

---

## Open Architecture Questions

Resolve via `spec-adr`.

- Question:
  Why unresolved:
  Best next source of truth:
