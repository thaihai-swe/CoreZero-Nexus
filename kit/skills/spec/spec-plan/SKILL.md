---
name: spec-plan
description: Design the technical solution and sequence execution tasks.
compatibility: Designed for AI coding agents.
---

# Kit Plan

## Overview
Converts approved requirements into a concrete execution strategy. Answers: how will we build this safely, and what task does implementation start with?

## I/O Hand-off Protocol
- **Reads**: `docs/project/requirements.md`, `memories/repo/harness-telemetry.md`.
- **Writes**: `docs/generated/plan.md`, `docs/generated/tasks.md`, `memories/repo/harness-telemetry.md`.
- **Next Skill**: `/spec-implement`

## Workflow
1. **Initialize State**: Update the `## Current State` section of `memories/repo/harness-telemetry.md` to set phase to `Planning`.
2. **Design**: Write `docs/generated/plan.md` defining impacted areas, execution order, rollback steps, and verification strategies.
3. **Task Breakdown**: Create `docs/generated/tasks.md` with unique task IDs (`T-01`), clear targets, and specific proof validations.
4. **Traceability**: Verify every requirement in `docs/project/requirements.md` maps to a task in `docs/generated/tasks.md`.
5. **Handoff**: Set `memories/repo/harness-telemetry.md` to `Plan Approved` and route to `/spec-implement`.

## Core Rules
- **Verifiable Task Increments**: Break work into low-risk tasks that can be proven independently.
- **No Spec Re-opening**: Stick to the approved requirements.
