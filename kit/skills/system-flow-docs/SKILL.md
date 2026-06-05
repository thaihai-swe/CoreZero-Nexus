---
name: system-flow-docs
description: Create system-level documentation explaining end-to-end flows, core workflows, actors, boundaries, and lifecycles via Markdown and Mermaid.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in any codebase.

---

# System Flow Docs


## Overview

Produce Markdown explaining how a system behaves end-to-end. Focuses on 2-5 high-value workflows, initiating actors, service boundaries, data handoffs, and state lifecycles.

## When to Use (vs. Others)

- **Use `/system-flow-docs`** for request paths, async event flows, transaction lifecycles, and backend orchestration logic.
- **Use `/api-endpoint-docs`** for HTTP route inputs, outputs, and JSON contract details.
- **Use `/codebase-documenter`** for developer setup, folders, and contributing guidelines.

## Read First

- Entry points (workers, cron, app routes).
- Orchestration (state machines, transaction layers, services).
- Storage and event boundaries (events, queues, schemas).
- References: `references/document-template.md`, `references/coverage-checklist.md`, `../_shared/doc-conventions.md`, and `../_shared/diagram-catalog.md`.

## Workflow

1. **Frame**: Define scope and boundaries.
2. **Trace Core Flows**: Trace request paths through entry points, validation, orchestration, external APIs, and persistence.
3. **Map Boundaries**: Identify initiating actors, owned components, and downstream interfaces.
4. **Visuals**: Embed a primary end-to-end flowchart or sequence diagram using shape rules in `../_shared/diagram-catalog.md`.
5. **Author**: Write the guide starting with overview and diagrams, then explain workflows and dependencies.
6. **Verify**: Check narrative against actual code control flows.

## Required Coverage

- Boundary and purpose mapping.
- Core workflows (2-5 paths).
- Components and interfaces.
- Primary end-to-end diagram.
- Failure/alternative path handling.

## Diagram Preferences

- **Primary**: Sequence diagram or flow chart for the main execution pipeline.
- **Supporting**: State diagram (lifecycles) or ERD (schemas).

## Stop Conditions

- Request asks for per-endpoint specs -> route to `/api-endpoint-docs`.
- Request asks for codebase onboarding -> route to `/codebase-documenter`.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "Document every edge flow." | 2-5 high-value flows beats exhausting edge cases. |
| "Add diagrams last." | Mapping diagrams during code tracing reveals hidden loops. |

## Red Flags

- Covers more than 5 workflows in a first pass.
- Missing a primary sequence/flow diagram.
- Written without tracing code paths.

## Verification

- [ ] Every flow claim verified against source files.
- [ ] Diagrams match the written narrative.
- [ ] Document structure complies with `../_shared/doc-conventions.md`.

## Core Rules

- Ground all system flows in actual code files. Do not describe speculative behavior.

## Output Rules

- Follow `../_shared/doc-conventions.md` guidelines.
- Save documentation to the specified output folder.
