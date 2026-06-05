# Post-Ship Sync (Knowledge Sweep)

Invoked automatically by `harness-verify` when a feature's verdict is `Pass`. The sweep is the self-improving step: every shipped feature must either update the knowledge base or explicitly justify why each file was left alone.

The mode is gated by the active rigor profile:

- **Tiny:** sweep only `learned-heuristics.md`. Update if the session produced a repeated, evidence-backed instinct. Otherwise record "no heuristic learned" and stop.
- **Standard / Complex:** full sweep across every memory file listed in `INDEX.md`.

Procedure (Standard and above):

1. **Read `INDEX.md`** to enumerate the current memory file set. If `INDEX.md` is missing, create it from `references/index-template.md` before continuing.
2. **Read the feature artifacts**: `spec.md`, `plan.md`, `review.md`, `session-extracts.md`, and any `adr-*.md` files under `artifacts/features/<slug>/`.
3. **For each memory file in `INDEX.md`**, decide one of:
   - **Update** — apply the diff (route through the matching skill section: constitution, security policy, learned heuristics, PKB, architecture, observability log).
   - **Untouched, with reason** — name the file and give a one-line reason it was not changed (e.g., "no normative rule emerged", "no new architectural boundary", "all candidates already deferred").
4. **Run promotion-threshold check**: for each updated file, compare against the thresholds in `harness-config.md` (lines, distinct subtopics, artifact references). If a file crosses a threshold, add it to the `## Promotion Watchlist` section in `INDEX.md` and write a one-paragraph promotion proposal to `artifacts/features/<slug>/promotions.md`. Promotion itself requires user approval — never split a file unprompted.
5. **Write the sweep record** to `artifacts/features/<slug>/session-extracts.md` under a new heading `## Post-Ship Sync — <ISO date>`. The record must list every memory file from `INDEX.md` with one of:
   - `Updated: <one-line summary of the change> -> <file>`
   - `Untouched: <one-line reason>`
6. **Verify** before reporting back to `harness-verify`:
   - Every file in `INDEX.md` appears exactly once in the sweep record.
   - No file is marked `Updated` without a corresponding diff in the same session.
   - No file is marked `Untouched` without a concrete reason — generic reasons such as "nothing changed" do not count.
   - Promotion watchlist additions have a corresponding proposal under `artifacts/features/<slug>/promotions.md`.

**Stop Conditions**:

- The verify verdict is not `Pass` — the sweep does not run on failed verifications.
- The session-extracts already contain a sweep record for this feature with the same date — re-running requires user confirmation.
- A required input (`review.md`, `INDEX.md`) is missing — repair before sweeping.

**Anti-patterns**:

- "Skipped — no updates needed" without enumerating files. Reject.
- Updating PKB or constitution to capture feature-local context. Route to feature artifacts instead.
- Promoting on the strength of one feature's signal. Heuristics still need repetition.
- Auto-splitting a memory file because it hit a threshold. Threshold breach opens a proposal, not an action.
