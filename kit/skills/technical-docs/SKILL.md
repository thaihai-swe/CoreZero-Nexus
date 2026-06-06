---
name: technical-docs
description: Create technical documentation including HTTP/REST API contracts, end-to-end event and logical workflow flows, system boundaries, and actor interactions using Markdown and Mermaid diagrams. Supports mode-based routing (api, flow, both).
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in any codebase.
---

# Technical Docs

## Overview

Produce structured Markdown documentation explaining API contracts (endpoints, payloads, auth) and/or system workflows (end-to-end logic, actor boundaries, lifecycles). Ground all documentation strictly in source code.

## When to Use (vs. Others)

- **Use `/technical-docs --mode api`** for HTTP/REST API endpoints, query/body payloads, headers, status codes, and route-level auth.
- **Use `/technical-docs --mode flow`** for end-to-end workflow narratives, state machine lifecycles, and event-driven data flow.
- **Use `/technical-docs --mode both`** when the feature introduces both new API endpoints and complex system orchestration/event workflows.
- **Use `/codebase-documenter`** for developer setup, architecture layout, directory overviews, and contributing guides.

## Read First

- `memories/repo/constitution.md` and `memories/repo/project-knowledge-base.md`
- `../_shared/doc-conventions.md` (shared documentation rules and output standards)
- Routers, controllers, handler files, schema/DTO definitions, and OpenAPI specs (for `api` mode)
- Worker processes, queue subscribers, state transition modules, and orchestration scripts (for `flow` mode)
- References: `references/api-document-template.md`, `references/api-coverage-checklist.md`, `references/flow-document-template.md`, `references/flow-coverage-checklist.md`, and `../_shared/diagram-catalog.md`.

## Workflow

### Step 0: Mode Selection
Identify the active mode from the invocation parameters or feature context:
- `--mode api`: Document HTTP endpoint contracts.
- `--mode flow`: Document end-to-end system flows.
- `--mode both` (or unspecified feature flow touching both API and system changes): Run the `api` mode workflow, then the `flow` mode workflow, combining the output into a single unified technical document.

### Mode: api
1. **Scope & OpenAPI Read**: Identify base path, host, and version prefix. Read any OpenAPI/Swagger spec first as a baseline; reconcile any divergence with router and handler files.
2. **Trace Paths**: Trace routes through middleware, validators, handlers, and persistence layers.
3. **Capture Contract**: Extract inputs (query, headers, body schemas), success/failure status codes, error shapes, and route auth.
4. **Shared Conventions**: Document global behaviors (pagination, rate limits, CORS) in a central section.
5. **Examples**: Write syntactically valid request/response payloads (JSON and curl).
6. **Visuals**: Embed a sequence diagram using Mermaid sequence diagram syntax. For complex flows, invoke `/visualize` using standard shapes.
7. **Document & Verify**: Write to file following `references/api-document-template.md` and check against `references/api-coverage-checklist.md`.

### Mode: flow
1. **Frame & Discovery**: Define system boundaries, actors, entry points, and persistence layers.
2. **Trace Core Flows**: Trace request/event paths through entry points, validation, orchestration, and persistence.
   **Failure paths**: For each primary flow, identify the top 2 failure or alternative paths. Document them in a `## Failure Paths` section below the happy path.
3. **Map Boundaries**: Identify initiating actors, component edges, and external APIs.
4. **Visuals**: Embed a flowchart or sequence diagram using shape rules in `../_shared/diagram-catalog.md`.
5. **Author & Verify**: Write to file following `references/flow-document-template.md` and check against `references/flow-coverage-checklist.md`.

### Mode: both
1. Execute the `api` mode workflow.
2. Execute the `flow` mode workflow.
3. Combine the generated API contracts and flow narratives into a single unified technical document.

## Output Rules

- Follow formatting guidelines in `../_shared/doc-conventions.md`.
- Group endpoints/flows logically (by feature/resource, not source file layout).
- Ground all facts in code; do not speculate or invent hypothetical routes or behaviors.
- **Output location**: Follow canonical paths from `../_shared/doc-conventions.md → ## Output Locations`.
  - Feature-scoped:
    - `--mode api`: `artifacts/features/<slug>/api-docs.md`
    - `--mode flow`: `artifacts/features/<slug>/flows.md`
    - `--mode both`: `artifacts/features/<slug>/technical-docs.md`
  - Global / standalone:
    - `--mode api`: `docs/api/<version>.md`
    - `--mode flow`: `docs/flows/<name>.md`
    - `--mode both`: `docs/technical-docs/<name>.md`

## Stop Conditions

- Route files, handlers, schemas, or orchestration files are missing or unreadable.
- Request scope requires more than 5 distinct flows in a single document (flow mode) -> split into separate subsystem documents or scope down with the user.
- Fewer than 1 endpoint/flow can be traced on disk (no source code to ground facts in).

## Core Rules

- **Ground in Code**: Every endpoint signature, payload key, state transition, and file reference must exist in the codebase.
- **No Shadow Divergence**: If OpenAPI specs or legacy docs diverge from code, document the code behavior and flag the contradiction explicitly.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "I'll document how the API is supposed to work." | Documentation must match the current codebase implementation exactly. |
| "A single giant sequence diagram is best." | Keep diagrams under 20 nodes; use multiple diagrams or call `/visualize` for complex orchestrations. |

## Red Flags

- Inventing paths, enums, or behaviors not implemented in code.
- Sequence diagrams that do not trace actual execution paths.
- Missing failure paths for critical business workflows.

## Verification

Before finalizing, verify:
- [ ] Every documented route/flow is trace-verified against files on disk.
- [ ] Auth and payload schemas match active handlers/schemas.
- [ ] At least one request/response example is syntactically valid per endpoint.
- [ ] Diagrams match the written narrative exactly.
- [ ] Scope, audience, and system boundaries are explicitly stated.
