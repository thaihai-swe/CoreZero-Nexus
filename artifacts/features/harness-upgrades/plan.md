# Implementation Plan

## Metadata

- Feature name: Harness Upgrades (Context, Provenance, Memory)
- Related spec: N/A (Harness self-improvement)
- Related requirements review: N/A
- Related design: N/A
- Owner: Agent
- Status: Draft
- Last updated: 2026-06-05

## Plan Summary

This plan outlines the updates to the kit's core harness skills and memory templates to implement four advanced ecosystem patterns: Confidence-Scored Context Loading, Decision Provenance Records, Cross-Feature Pattern Surfacing, and Semantic Memory Knowledge Graphs. Since this modifies the harness and agent instructions, it will be executed under the `Complex` rigor profile.

## Execution Context

- Delivery profile: Complex
- Locked spec decisions: Approved by user from the ecosystem comparison report.
- Relevant repository patterns for execution: Skill files own workflow logic, memory templates own schema.
- Unchanged behavior that must be preserved during delivery: Existing CC-* rules and indexing must not be deleted, only augmented.

## First Delivery Slice

- Smallest useful slice: Update `INDEX.md` and `context-session` to support `partial-load` confidence scoring.
- Why this slice goes first: It reduces token usage for all subsequent agent runs.
- What proof should exist when this slice is done: The routing logic in `INDEX.md` clearly documents partial loading rules.

## Technical Approach

- Chosen approach: Modify markdown schemas and skill instructional prompts.
- Architectural or integration shape: 
  - `INDEX.md`: Add partial-load logic.
  - `context-session`: Add parsing for partial-load.
  - `spec-implement`: Mandate Decision Record block in progress files.
  - `context-memory`: Add Semantic Link enforcement and recurrence count auto-promotions.
  - `learned-heuristics-template.md`: Update schema.

## Requirements And Constraints

- REQ-001: Confidence-Scored Loading
  - Implementation note: Modify `memories/repo/INDEX.md` and `skills/context-session/SKILL.md`.
- REQ-002: Decision Provenance Records
  - Implementation note: Modify `skills/spec-implement/SKILL.md` to require decision blocks.
- REQ-003: Cross-Feature Pattern Surfacing
  - Implementation note: Add `recurrence-count` to `skills/context-memory/references/learned-heuristics-template.md`.
- REQ-004: Semantic Memory Graph
  - Implementation note: Require markdown linking in `skills/context-memory/SKILL.md`.

## Impacted Areas

- Services or modules: `skills/context-session`, `skills/context-memory`, `skills/spec-implement`
- Documentation: `memories/repo/INDEX.md`, `skills/context-memory/references/learned-heuristics-template.md`

## Affected Files

- FILE-001 Path: `kit/memories/repo/INDEX.md`
  - Reason for change: Add partial load rule.
- FILE-002 Path: `kit/skills/context-session/SKILL.md`
  - Reason for change: Instruct session agent on handling partial loads.
- FILE-003 Path: `kit/skills/spec-implement/SKILL.md`
  - Reason for change: Add Decision Record enforcement.
- FILE-004 Path: `kit/skills/context-memory/references/learned-heuristics-template.md`
  - Reason for change: Add `recurrence-count` and semantic link fields.
- FILE-005 Path: `kit/skills/context-memory/SKILL.md`
  - Reason for change: Instruct memory agent to increment counts and enforce semantic graph links.

## Execution Phases

### Phase 1: Context & Provenance
- Goal: Enable partial context loading and enforce execution decision provenance.
- Completion criteria: `INDEX.md`, `context-session/SKILL.md`, and `spec-implement/SKILL.md` updated.

### Phase 2: Memory Architecture
- Goal: Enable semantic graph links and auto-promotions via recurrence counts.
- Completion criteria: `learned-heuristics-template.md` and `context-memory/SKILL.md` updated.

## Validation Strategy

- Manual verification: Read through modified skill files to ensure new instructions do not contradict existing workflow steps.

## Rollout Plan
- Immediate availability for new agent sessions. No backward compatibility issues since new schemas are additive.
