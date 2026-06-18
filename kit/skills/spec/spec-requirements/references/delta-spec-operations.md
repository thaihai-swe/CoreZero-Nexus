# Delta Spec Operations

How feature `## Delta` sections in `spec.md` merge into a canonical domain spec at `memories/domain/spec.md`. The delta workflow is opt-in — features that do not touch a tracked domain skip it entirely.

## When the delta workflow applies

- The feature is brownfield (`## Current Context` is filled).
- The feature's `Impacted boundaries` overlap a domain pack listed in `memories/repo/INDEX.md` `## By Domain Packs`.
- A canonical spec exists (or will be created) at `memories/domain/spec.md`.

If any of those is false, leave the spec's `## Delta` section empty and skip the merge step. The feature's own `## Functional Requirements` remain the only requirements record.

Profile gating:

| Profile | Delta section | Merge step |
|---|---|---|
| Tiny | Skipped. | No. |
| Standard | Optional. Required only if the brownfield risk rating is `High` and the impacted domain has a canonical spec. | Run only when the section is filled. |
| Complex | Required when impacted boundaries overlap a tracked domain. | Required when section is filled. |

## Delta operation rules

Three operations are allowed: `ADDED`, `MODIFIED`, `REMOVED`. Anything else is rejected by `/harness-verify` post-ship sync before the merge runs.

### ADDED

- A `REQ-NNN` introduced by this feature that did not exist in the canonical spec.
- The full REQ block (Requirement, Why it matters, Impacted users or scenarios, Related success criteria, Priority, Acceptance notes, Validation surface) must be inlined under `### ADDED Requirements` — the merge appends it verbatim to the canonical spec.
- Reusing a `REQ-NNN` that already exists in the canonical spec is a conflict. Renumber to the next free ID for that domain (the merge step does not auto-renumber).

### MODIFIED

- An existing `REQ-NNN` whose text, priority, or validation surface changes.
- The entry MUST show both `Before:` (quoted canonical text) and `After:` (new text). A MODIFIED entry without a before/after is rejected.
- The merge step replaces the canonical text with the new text and stamps a comment `<!-- modified by feature <slug> on <ISO date> -->` directly under the REQ heading.
- Modifying a REQ-ID that does not exist in the canonical spec is a conflict — promote it to ADDED instead.

### REMOVED

- An existing `REQ-NNN` that no longer applies after this feature ships.
- Each REMOVED entry must name `Reason:` and `Migration / compensating behavior:`. Silent removal is rejected.
- The merge step does **not** delete the canonical REQ. It marks the canonical entry with `Status: Removed by feature <slug> on <ISO date>` at the head of the REQ block and moves the block to a `## Removed Requirements (history)` section at the bottom of the canonical spec, preserving auditability.

## Conflict detection

Before merging, the post-ship sync runs three checks. Any failure stops the merge with a clear error and routes back to `/spec-requirements`:

1. **ID collision.** An ADDED entry uses a `REQ-NNN` that already exists in the canonical spec.
2. **Missing target.** A MODIFIED or REMOVED entry references a `REQ-NNN` not present in the canonical spec.
3. **Concurrent edit.** The canonical spec's last-merged ISO date is later than this feature's `## Current Context` was authored, AND the impacted REQ-IDs were touched by the intervening merge. The fix is manual: re-anchor the delta against the current canonical text, then re-run sync.

If the canonical spec does not yet exist (first feature for this domain), the merge step creates it from `kit/skills/spec-requirements/references/spec-template.md` skeleton, fills `Feature name: <domain> canonical spec`, and inlines all ADDED entries. MODIFIED and REMOVED are not legal in a creation merge.

## Merge procedure (executed by post-ship sync)

1. Read the feature spec's `## Delta` section. If empty, skip.
2. Resolve `Target domain spec`. If the file does not exist, treat as creation merge (ADDED only).
3. Run conflict detection (above). On any conflict, stop and emit a `delta-merge-blocked` finding.
4. Apply ADDED entries first (append under `## Functional Requirements`).
5. Apply MODIFIED entries next (in-place text replacement plus modification stamp).
6. Apply REMOVED entries last (move to `## Removed Requirements (history)` with status stamp).
7. Append a one-line entry to the canonical spec's footer: `Last merged: feature <slug> on <ISO date> — added: <count>, modified: <count>, removed: <count>`.
8. Record the merge in `artifacts/features/<slug>/session-extracts.md` under the existing `## Post-Ship Sync — <ISO date>` heading: `Domain spec merged: memories/domain/spec.md (added: N, modified: N, removed: N)`.

## What the merge does NOT do

- It does not change the feature's own `spec.md`. The feature record is immutable after `Done`.
- It does not promote REQs or ACs into `memories/repo/core-policies.md` — that path stays under `/context-memory` heuristic-promotion.
- It does not auto-renumber colliding REQ-IDs. Renumbering is a human-readable concern; auto-renumbering would silently re-anchor proof references.

## Rejection signals

Reject the delta and stop the merge when any of these are true:

- A MODIFIED entry omits `Before:` or `After:`.
- A REMOVED entry omits `Reason:` or `Migration / compensating behavior:`.
- The `## Delta` section is filled but the spec's `## Current Context` is empty (delta requires brownfield context).
- The target domain spec path does not match `memories/domain/spec.md`.
- More than one `Target domain spec` is named in the section. Split into two features instead.

Each rejection routes back to `/spec-requirements` with the specific reason. The feature's `Done` status is not affected — the merge is post-ship hygiene, not a verification gate.
