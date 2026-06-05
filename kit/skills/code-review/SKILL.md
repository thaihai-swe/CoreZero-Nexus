---
name: code-review
description: Perform code review following Google's Engineering Practices. Evaluates code health, design, functionality, complexity, testing, naming, and style.
compatibility: Designed for agents reviewing code changes or PRs.

---

# Code Review Skill


## Overview

Use this skill to perform code reviews based on Google's Engineering Practices. The goal is to ensure the overall code health of the codebase improves over time. Usually invoked as a helper from `harness-verify`.

## Read First

- PR description and diff
- `memories/repo/constitution.md` (code standards, naming, principles)
- Style guides under `rules/`
- `memories/repo/security-policy.md` (security boundaries and sensitive paths)

## When to Use

- Assigned to review a new PR or CL.
- Evaluating quality, maintainability, and correctness of proposed changes before merge.

## Execution Modes: Standalone vs. Gated Integration

| Dimension | Standalone PR Review Mode | Gated Integration Mode (via `/harness-verify`) |
|---|---|---|
| **Trigger** | Assigned to review a new PR or CL | Automatically invoked at step 8 of `/harness-verify` |
| **Audience** | Human developers | Execution engine / automated verifiers |
| **Outcome** | PR Approval / Request Changes | Written directly to `review.md` |
| **Scope** | Complete PR diff + adjacent callers | Touch files & task boundaries (`tasks.md`) only |
| **Ceremony** | Mentorship, explanations, nit tags | Fails loud on AC/gate failures |

### Gated Integration Mode Contract
When called from `/harness-verify`:
- **Scope**: Restrict review strictly to touched files and specific task boundaries.
- **Outcome**: Produce a structured response (verdict, mandatory findings, options, compliments) and return to `/harness-verify` to write to `review.md`.

## The Standard of Code Review

Favor approving any CL that improves overall code health, even if imperfect.
- **No Perfectionism**: Do not block progress for minor polish.
- **No Degradation**: Do not approve changes that worsen code health (except in true emergencies).
- **Feature Fit**: Reject features that do not belong in the system.
- **Mentoring**: Share knowledge. Mark non-mandatory comments with `Nit:` or `Optional:`.

## Speed of Reviews

- Optimize for team velocity: respond within 1 business day.
- Approve with comments (LGTM with comments) for minor or optional items.

## Workflow

1. **Broad View**: Check if the change makes sense overall. If not, reject immediately.
2. **Main Parts**: Inspect core files first. Provide design feedback immediately.
3. **The Rest**: Look through the remaining changes and tests.

## What to Look For

1. **Design**: Check integration, interfaces, and architecture.
2. **Functionality**: Verify behavior and edge cases. Check for races/deadlocks.
3. **Complexity**: Call out over-engineering. Solve today's problems, not speculative future ones.
4. **Tests**: Verify test design and assertion correctness.
5. **Naming & Style**: Clear naming; follow style guides (`rules/`) or preserve local consistency.
6. **Comments & Docs**: Verify comments explain *why*, not *what*. Update relevant documentation.

## Writing Comments & Handling Pushback

- **Courtesy**: Focus comments on the code, never on the developer.
- **Severity**: Differentiate suggestions (`Nit:`, `Optional:`, `FYI:`) from mandatory fixes.
- **Pushback**: Resolve disagreements with technical facts. Do not accept "will fix in later PR" for new complexity; require fix now. Pre-existing issues get a TODO + bug ticket.

## Stop Conditions

- PR description is missing or too vague.
- Modifies security-sensitive paths without explicit security evidence (escalate).
- CL is pure documentation/comment changes (run lightweight pass).

## Core Rules

- **Technical Facts Over Opinions**: Prefer the author's approach if multiple valid options exist.
- **Understand Every Line**: Read and comprehend every modified line.

## Rationalization vs. Reality

| Rationalization | Reality |
|---|---|
| "They'll clean it up in a follow-up." | Deferred cleanup rarely happens. Require fixes to new complexity now. |
| "This is too long to read." | Reading every line is mandatory. Split oversized CLs. |
| "Tests pass, so design is fine." | Passing tests do not validate design quality. |

## Red Flags

- Lack of explanation of *why* the change exists.
- New complexity introduced without tests.
- Modifying security-sensitive paths without explicit safety proof.

## Verification

- [ ] Every file in the diff was read.
- [ ] Mandatory comments are explicitly distinguished from optional ones.
- [ ] Security-policy sensitive paths checked.
- [ ] Explicit review outcome (LGTM / Request Changes / Reject) provided.

## Output Rules

- Produce structured response: overall verdict, mandatory changes, optional suggestions, positive callouts.
- Do not modify repo files directly. Write outcome to `artifacts/features/<slug>/review.md` when integration mode is active.
