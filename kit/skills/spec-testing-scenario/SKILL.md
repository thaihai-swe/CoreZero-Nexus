---
id: skill-spec-testing-scenario
name: spec-testing-scenario
description: "Draft a manual testing scenario guide for a feature. Fully optional and user-invoked — run it whenever you want structured test coverage documented before or after implementation."
tags: ['spec', 'testing', 'scenarios', 'manual-testing']
triggers: ['testing scenario', 'test scenarios', 'test guide', 'manual test', 'testing-scenarios']
next_skill: 'spec-implement'
---
# Spec Testing Scenario

## Overview

Use this skill to produce `testing-scenarios.md` — a structured, human-readable guide covering happy paths, edge cases, failure paths, regression checks, and sign-off for a feature. This skill is **fully optional**. No other skill auto-triggers it. Run it whenever structured test documentation adds value for your team.

Typical invocation points:
- After `/spec-plan` (before implementation begins, to clarify what will be tested)
- After `/spec-implement` (to document what was actually built)
- Standalone at any time during the feature lifecycle

## I/O Hand-off Protocol

- Reads: `artifacts/features/<slug>/spec.md`, `artifacts/features/<slug>/plan.md`
- Writes: `artifacts/features/<slug>/testing-scenarios.md`
- Next Skill: `/spec-implement` (if pre-implementation) or as directed.

## Workflow

1. **Locate the feature**: Identify `<slug>` from context or ask the user. Confirm `spec.md` and `plan.md` exist.
2. **Read inputs**: Load `spec.md` to extract all `AC-*` acceptance criteria. Load `plan.md` to understand the technical scope and component boundaries.
3. **Derive scenarios**: For each `AC-*` item:
   - Draft one or more happy-path scenarios that prove the AC is met.
   - Identify likely edge cases and failure paths (invalid input, boundary values, error states).
   - Flag any regression risk areas from `plan.md` (e.g., touched shared components).
4. **Populate the template**: Use `references/testing-scenarios-template.md` as the document structure. Fill every section — do not leave placeholder text in required fields. Leave optional fields blank rather than inventing content.
5. **Write output**: Save to `artifacts/features/<slug>/testing-scenarios.md`.
6. **Summary**: Report to the user: number of scenarios drafted, ACs covered, and any ACs that had no testable surface (escalate those).

## Core Rules

- **AC traceability required**: Every `AC-*` in `spec.md` must appear in the Scenario Matrix, linked to at least one scenario. No orphan ACs.
- **No invented facts**: If an AC is ambiguous, write the scenario with a `[CLARIFY]` marker — do not fabricate expected results.
- **Scope discipline**: Only test what is in `spec.md`. Do not add out-of-scope scenarios without noting them as `[OUT OF SCOPE — Optional]`.
- **Optionality respected**: This skill produces a document. It does not gate, block, or modify any other artifact. Skipping it is always valid.
