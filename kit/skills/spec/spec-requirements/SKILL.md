---
name: spec-requirements
description: Define the requirements and acceptance criteria for a feature.
compatibility: Designed for AI coding agents.
---

# Kit Spec

## Overview
Define the "What & Why" of a feature. Aligns the team on what is being built and how it will be verified.

## I/O Hand-off Protocol
- **Reads**: `docs/generated/analysis.md` (if exists), `memories/repo/harness-telemetry.md`.
- **Writes**: `docs/project/requirements.md`, `memories/repo/harness-telemetry.md`.
- **Next Skill**: `/spec-plan`

## Workflow
1. **Initialize State**: Update the `## Current State` section of `memories/repo/harness-telemetry.md` to set phase to `Spec'ing`.
2. **Clarify**: If there is ambiguity, ask the user clear questions.
3. **Authoring**: Draft `docs/project/requirements.md`. Define testable acceptance criteria (AC).
4. **Scope Cut**: Explicitly list In Scope, Out Of Scope, and Non-Goals.
5. **Handoff**: Update the `## Current State` section of `memories/repo/harness-telemetry.md` to `Spec Approved` and route to `/spec-plan`.

## Core Rules
- **Clarify, Don't Re-litigate**: Ask minimum high-signal questions.
- **What, not How**: Focus on requirements, not technical implementation.
- **Validation-Aware**: Every acceptance criterion must be testable.
