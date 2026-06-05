---
name: api-endpoint-docs
description: Create API endpoint documentation from route files, handlers, schemas, and OpenAPI definitions. Use when the system is an HTTP/REST API and the user wants per-endpoint contracts.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in any codebase.

---

# API Endpoint Docs

## Overview

Produce Markdown documentation detailing HTTP API endpoints: method, path, request/response payload shapes, authentication, sequence/data flows, and dependencies. Ground all facts in code.

## When to Use (vs. Others)

- **Use `/api-endpoint-docs`** for HTTP/REST per-endpoint contracts (inputs, outputs, status codes, rates).
- **Use `/system-flow-docs`** for end-to-end event/logical workflow narratives.
- **Use `/codebase-documenter`** for general repo onboarding (setup, project boundaries).

## Read First

- Router, handler, controller, and DTO/serializer files.
- Middleware, auth, and error-handler configurations.
- References: `references/document-template.md`, `references/coverage-checklist.md`, `../_shared/doc-conventions.md`, and `../_shared/diagram-catalog.md`.

## Workflow

1. **Scope**: Identify version prefix, host, and routes to document. Default to API reference structure.
2. **Trace Paths**: Map routes through middleware, validation, handler, service, and database layers.
3. **Capture Contract**: Extract authentication, inputs (query/headers/body), status codes, error shapes, and side effects.
4. **Shared Rules**: Document cross-cutting behaviors (pagination, rate limits, CORS) in a central section.
5. **Examples**: Provide representative request/response snippets (default to curl and JSON).
6. **Visuals**: Embed a sequence diagram for request flows. Map shapes per `../_shared/diagram-catalog.md`.
7. **Document & Verify**: Format logically. Re-read code to verify every route, parameter, and response matches.

## Required Coverage

- Endpoint summary table.
- Method, path, purpose, auth, input/output structures, and error types.
- Examples (requests/responses).
- Centralized auth/pagination rules.
- Sequence flow diagram.

## Diagram Preferences

- **Primary**: Sequence diagram mapping Client → Gateway → Middleware → Handler → Service → DB.
- Use readable labels; include code identifiers only for developer mapping.

## Output Rules & conventions

- Follow formatting guidelines in `../_shared/doc-conventions.md`.
- Group endpoints logically (by resource/feature, not source path).
- Do not invent hypothetical endpoints; document only what exists in source code.
