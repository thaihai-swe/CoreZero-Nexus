# Multi-Agent Coordination Protocol

## Purpose

When multiple agents work on the same project simultaneously, they share the `memories/repo/` memory layer but operate on isolated feature slugs. This protocol prevents two agents from accidentally working on the same slug, defines how to merge partial work, and sets status reporting conventions for cross-agent visibility.

---

## Core Principle: One Agent Per Slug

Each feature slug in `artifacts/features/<slug>/` is owned by at most one active agent at a time. Ownership is established by a `claim.md` file. This is the lock primitive — it is git-tracked, auditable, and requires no external infrastructure.

---

## 1. Claiming a Feature Slug

Before starting any work on a feature, an agent **must** create or verify ownership of the slug's `claim.md`:

### Claim File Format

**Path:** `artifacts/features/<slug>/claim.md`

```markdown
# Claim: <slug>

- Agent ID: <describe yourself — e.g., "Claude Sonnet 3.5 session, terminal 1" or "Gemini CLI, user @alice">
- Claimed at: <ISO 8601 timestamp>
- Claimed by: <user or automated pipeline context>
- Expires at: <claimed-at + 4 hours, or "manual release only">
- Status: Active

## Scope
<One paragraph describing what this agent is doing with this slug — e.g., "Implementing TASK-03 and TASK-04 from tasks.md for the payment-webhook feature.">
```

### Claim Rules

1. **Read before claiming**: Before writing `claim.md`, read the directory to check if it already exists.
2. **Check for stale claims**: If `claim.md` exists and the `Expires at` timestamp has passed, the claim is stale and can be superseded. Write a new `claim.md` with a `## Supersedes` section referencing the old claim.
3. **Do not claim if active**: If an active claim exists (not expired, status = Active), stop and report `BLOCKED: feature <slug> is claimed by another agent`. Do not proceed.
4. **Claim scope is narrow**: Only claim the specific tasks you intend to work on. Do not claim the entire feature to block others.

---

## 2. Working Under a Claim

Once claimed:

- Write to `tasks.md` only for the tasks listed in your claim scope.
- Do not modify `spec.md` unless your claim explicitly covers spec amendments.
- Do not modify `plan.md` unless your claim covers plan revisions.
- Update `status.md` to reflect your current sub-task progress.
- Checkpoint your session via `/context-session CHECKPOINT` at natural pause points.

---

## 3. Releasing a Claim

When your work is complete or interrupted:

Update `claim.md` status to `Released`:

```markdown
- Status: Released
- Released at: <ISO 8601 timestamp>
- Release reason: Work complete | Session interrupted | Blocked on dependency

## Release Notes
<What was accomplished. What tasks are Done. What remains open for the next agent.>
```

This is mandatory. An unreleased claim blocks other agents unnecessarily.

---

## 4. Partial-Work Merge

When two agents worked on different tasks within the same slug (e.g., one on TASK-01 and one on TASK-02) and both need to merge their state:

### Merge Procedure

1. **Designate a merge agent**: One agent takes responsibility for merging. Declare this in `claim.md` as `Status: Merging`.
2. **Review both `tasks.md` edits**: Each agent's completed tasks should have their own proof evidence. Merge both sets into a unified `tasks.md` with all evidence preserved.
3. **Conflict resolution priority**:
   - For `tasks.md`: Preserve all completed tasks from both agents. Mark any conflicting tasks as `Needs Review` and surface them to the user.
   - For `status.md`: Set phase to the lowest completed phase (do not advance status past what both agents have verified).
   - For `spec.md`: Never merge spec changes without user confirmation. Surface conflicts as `[CONFLICT: Agent A said X, Agent B said Y]`.
4. **Re-run verify**: After merging, the merge agent must run `/harness-verify` from scratch. Partial evidence from isolated agents is not accepted as final verification proof.
5. **Release the merge claim** after the verify pass.

---

## 5. Multi-Agent Status Reporting

`/context-status` reports cross-feature visibility. In multi-agent environments, the claim file is the source of truth for who owns what.

When reporting status in a multi-agent context, each agent must end its session summary with one of:

| Status Code | Meaning |
|---|---|
| `DONE` | Work complete, claim released, verify passed |
| `DONE_WITH_CONCERNS` | Work complete but outstanding issues documented in `session-extracts.md` |
| `BLOCKED` | Cannot proceed — specify the blocker (slug claimed, dependency missing, spec conflict) |
| `NEEDS_CONTEXT` | Cannot proceed without additional information from user or another agent |
| `CHECKPOINT` | Work paused, claim held, ready to resume |

These status codes appear in `status.md` under a `## Agent Status` section and are picked up by `/context-status`.

---

## 6. Shared Memory Rules in Multi-Agent Environments

Multiple agents read and write to `memories/repo/` — this is intentional. Rules for shared memory:

- **Read freely**: Any agent may read any memory file at any time.
- **Append only for logs**: `observability-log.md` and `session-extracts.md` are append-only. Never overwrite an existing entry.
- **Propose before amending instruction-tier memory**: An agent must not directly edit `constitution.md`, `security-policy.md`, or `project-knowledge-base.md` during feature work. Proposals go through `/context-memory` Extraction Triage after the feature ships.
- **`INDEX.md` is read-only during feature work**: Only `/harness-maintain` and `/context-memory` Post-Ship Sync have write authority over `INDEX.md`.

---

## 7. Anti-Patterns

| Anti-Pattern | Risk | Correct Approach |
|---|---|---|
| Claiming a slug without reading existing claim.md | Two agents work on same tasks simultaneously | Always read the claim file before claiming |
| Holding a claim after work is done | Blocks other agents indefinitely | Release the claim immediately on completion or interruption |
| Merging without re-running verify | Accepts unverified evidence | Always re-run harness-verify after a merge |
| Writing to spec.md from two agents | Unresolvable spec conflicts | One agent owns spec authorship per feature; surface conflicts to user |
| Editing constitution.md during feature work | Race conditions on shared normative rules | Queue proposals through context-memory triage post-ship |
