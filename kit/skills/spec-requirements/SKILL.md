---
name: spec-requirements
description: Define the "What & Why" of a feature. Handles specification authoring, Socratic refinement to resolve ambiguity, and a built-in readiness review to ensure requirements are testable and complete before planning.
compatibility: Designed for Claude, Codex, and other Agent Skills-compatible tools working in spec-driven repositories that use memories/repo/ and artifacts/features/<slug>/.

---

# Kit Spec


## Routing Guide

- **Use `/spec-requirements`** to define requirements and acceptance criteria.
- **Use `/spec-research`** first if the problem space, bug root cause, or brownfield codebase state is unknown.

## Overview

Create or refine `status.md`, `proposal.md`, `spec.md`, and `requirements-review.md` in `artifacts/features/<slug>/`. This skill aligns the team on what is being built and how it will be verified.

## Read First

- `memories/repo/constitution.md`
- `memories/repo/project-knowledge-base.md`
- `memories/repo/domain-specs.md` (if relevant)
- `artifacts/features/<slug>/analysis.md` (if it exists)
- References: `references/intake.md`, `references/status-template.md`, `references/proposal-template.md`, `references/spec-template.md`, `references/requirements-review-template.md`, and `../_shared/rigor-profiles.md`.

## When to Use

- Define a new feature, change request, or initiative.
- Refine existing specifications.
- Resolve ambiguity before design/planning.

## Workflow

0. **Claim Check**: Check `artifacts/features/<slug>/claim.md` before writing any artifact. Same protocol as `spec-research` Step 0.
1. **Initialization**: Create `status.md` if missing (from `references/status-template.md`). Set phase to `Spec'ing`.
2. **Profile Load**: Load active rigor profile from `status.md` (`## 🧭 Delivery Profile`) or fallback to `memories/repo/harness-config.md` default.
3. **Intake (Required)**: Classify input type (`new_spec`, `spec_slice`, `change_request`, `new_initiative`, `maintenance`, `harness_improvement`) and risk flags (`auth`, `authorization`, `data_model`, `provider`, `migration`, `cross_boundary`, `public_api`, `security`, `harness-maintain`, `none`) in `status.md`. Determine lane (Tiny/Standard/Complex) per rules in `references/intake.md`.
3a. **System Spec Mode Routing**: After Intake, check: is the request cross-cutting (affects multiple features) or system-wide (harness, auth, schema)? If yes → switch to System Spec Mode immediately. Output target becomes `docs/system-specs/<name>.md` instead of `artifacts/features/<slug>/spec.md`. All subsequent steps run in this mode. Do not continue into Step 4 in feature mode.
3b. **Analysis Check**: If `artifacts/features/<slug>/analysis.md` exists, read it before proceeding. Record any open research questions as explicit constraints in Step 4 (Domain Spec Check).
4. **Domain Spec Check**: Read relevant domain specs (e.g. `memories/repo/domain-specs.md`) to anchor feature behavior.
5. **Rigor Triage**: Promote profile to match intake lane decision. Set to `Complex` if security/migration/auth/harness-maintain flags exist.
6. **Grilling Phase**: Ask batch clarifying questions with recommended answers (1-2 for `Tiny`, 3-5 for `Standard`, 5+ for `Complex`). Do not ask what the codebase itself can answer.
   **Stop rule**: If after 2 grilling rounds the user's answers remain contradictory on a core requirement, stop. Write the contradictions to `spec.md` as `[UNRESOLVED: <description>]` items and surface to user. Do not proceed to Step 7 while core requirements are unresolved.
7. **Proposal**: Draft `proposal.md` for `Standard`/`Complex` to align scope before spec'ing. (For `Tiny`, embed in the spec).
8. **Gray-Area Decisions**: Record key design/UX/policy choices directly in `spec.md`.
9. **Scope Cut**: Explicitly list `In Scope`, `Out Of Scope`, and `Non-Goals`.
10. **Authoring**: Draft `spec.md` (`what` & `why`). Define scenarios and verify requirements.
11. **Acceptance Criteria**: Design testable, observable acceptance criteria (AC-*).
12. **Verification Surface**: Specify test methods (unit, integration, manual check).
13. **Self-Review**: Create `requirements-review.md` for `Standard`/`Complex`. Update `status.md` to `Spec Approved` and route to `/spec-plan`.

## System Spec Mode

Use when defining cross-cutting policies or standards spanning multiple features/harness changes.
- **Trigger**: Request affects multiple feature slugs or defines shared rules.
- **Output**: Write to `docs/system-specs/<name>.md` using `references/system-spec-template.md`. Do not create a feature directory.
- **Workflow**: Map policy decisions in `## Policy Decisions` table. Downstream specs must anchor to it. Route normative policy to `constitution.md` or `security-policy.md`.

## Stop Conditions

- Product ambiguity is too high to define outcomes.
- Grilling answers remain contradictory.

## Preconditions

- **Required Phase**: None or `Research Complete`. If `analysis.md` exists, read it first.
- **Phase sets**: `Spec'ing` → `Spec Approved`.

## Core Rules

- **Clarify, Don't Re-litigate**: Ask minimum high-signal questions, then stick to decisions.
- **What, not How**: Focus on requirements, not technical implementation.
- **Validation-Aware**: Every acceptance criterion must name its proof surface.
- **Brownfield Protection**: Explicitly state unchanged behavior to prevent regressions.
- **Spec-Anchored**: Requirements change requires returning to this skill first.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "Fill in product gaps later." | Leaks ambiguity into design and planning. |
| "A big umbrella spec is faster." | Oversized specs hide scope creep and weaken reviews. |
| "User prompt is clear enough." | Fuzzy requirements always benefit from targeted questions. |
| "Define How here to save time." | Prescribing design in specs creates early technical debt. |

## Red Flags

- Spec details design, tasks, or code.
- Criteria are not observable or lack verification methods.
- Spec keeps broadening instead of shipping smaller slices.
- `Tiny` work is treated with heavy ceremony without justification.

## Verification

- [ ] No placeholder text.
- [ ] Requirements are observable, non-contradictory, and testable.
- [ ] In/Out of Scope and Non-Goals are explicit.
- [ ] Rigor profile matches intake lane.
- [ ] Next command is `/spec-plan`.

## Output Rules

- Update only: `proposal.md`, `spec.md`, `requirements-review.md`, `status.md` (or `docs/system-specs/*`).
- Do not create: `design.md`, `plan.md`, `tasks.md`.
