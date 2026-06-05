# Domain Specs

This document explains how to use domain-level specs to make the kit work better on large codebases.

## Why Domain Specs Exist

Large repositories are hard for AI coding assistants because too much behavior is spread across too many files. Domain specs give the repository a stable, browsable description of how major areas of the system currently work.

They help agents:

- reason about one subsystem at a time
- avoid re-discovering the same behavior on every feature
- compare a proposed change against the current domain behavior
- work more safely when multiple teams change the same large codebase

## Relationship To Repository Memory

Use the layers like this:

- `constitution.md` - repository-wide rules and guardrails
- `project-knowledge-base.md` - durable cross-cutting patterns, boundaries, and watchouts
- domain specs - current behavior and responsibilities for a specific subsystem or business area

Domain specs are descriptive. They do not replace the constitution and should not contain repository-wide mandates.

## Recommended Location

Keep the routed baseline in this file. When a repository grows large enough to need deeper per-domain detail, link out to a dedicated top-level `specs/` directory such as:

```text
specs/
  auth/spec.md
  billing/spec.md
  notifications/spec.md
```

Keep `memories/repo/domain-specs.md` as the stable entrypoint and index for domain behavior even when detailed specs move into `specs/`.

## What Belongs In A Domain Spec

A strong domain spec should capture:

- the purpose of the domain
- major responsibilities and boundaries
- important user-visible behavior
- key data or state transitions
- integration boundaries and contracts
- protected existing behavior
- major risks or watchouts specific to the domain
- links to relevant code, tests, and feature artifacts

## What Does Not Belong In A Domain Spec

Do not put these here:

- repo-wide rules already owned by `constitution.md`
- general patterns better kept in `project-knowledge-base.md`
- feature-specific plans or one-off implementation notes
- speculative future architecture that is not yet true

## How Agents Should Use Domain Specs

For large-codebase work:

1. Read `constitution.md`
2. Read `project-knowledge-base.md`
3. Read the domain spec for the affected subsystem, if one exists
4. Read the current feature artifacts under `artifacts/features/<slug>/`

If no domain spec exists yet, use `/spec-research` to establish current-state facts and promote durable domain knowledge when it proves stable.

## How Domain Specs Relate To Feature Artifacts

Think of domain specs as the current-state baseline for a subsystem.

Think of feature artifacts as the proposed change against that baseline.

For brownfield changes, a useful pattern is:

1. `/spec-research` to understand current behavior
2. update or create the relevant domain spec if the finding is durable
3. create `spec.md`, `plan.md`, and `tasks.md` for the specific feature
4. use `/harness-verify` to verify the delivered change against both the feature artifacts and the current domain behavior

## Suggested Structure For A Domain Spec

```markdown
# Domain Spec: [Domain Name]

## Overview

## Responsibilities

## Boundaries

## Current Behavior

## Key Flows

## Integrations

## Protected Behavior

## Domain Watchouts

## References
```

## Large-Codebase Guidance

Use domain specs when:

- the repository has multiple major subsystems
- a feature touches an area with complex existing behavior
- multiple teams or sessions work in parallel
- agents repeatedly need the same subsystem context

Do not require them for every small repository. Add them where they reduce ambiguity and repeated discovery.
