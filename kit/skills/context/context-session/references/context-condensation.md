# Context Condensation Strategies

As a session progresses, the context window fills up with conversation history, tool outputs, and loaded files. To prevent context degradation, apply these strategies:

1.  **Summarize, Don't Repeat:** Instead of carrying forward the full output of a failing test, summarize it: "Test X fails on line 42 due to a null pointer exception in user auth."
2.  **Prune Exploration:** If a subagent or tool was used to search the codebase, extract the findings and discard the raw search results (grep output, file listings).
3.  **Just-In-Time (JIT) Loading:** If you are working on Task B, do not load the `design.md` sections for Task D. Load only what is immediately necessary.
4.  **Offload to Memory:** If you discover a durable fact about the codebase, write it to `project-knowledge-base.md` or `progress.md` so you don't have to keep it "in mind."
5.  **Signal vs. Noise:** When running commands, drop verbose boilerplate output and retain only the specific pass/fail signals and relevant error stack traces.
6.  **Evict By Tier:** Drop transient logs before raw code, raw code before unrelated feature artifacts, and unrelated artifacts before repo memory.
7.  **Preserve The Resume Surface:** Keep the current task, proof state, blockers, and active files even when aggressively compacting.

---

## Token Budgeting & Amnesia Warnings

1.  **Monitor Saturation:** Read the `Session Token Capacity` in `HARNESS_CARD.md`. Calculate your current token usage at each checkpoint.
2.  **Amnesia Warning (80% Saturation):** When the token count exceeds 80% of capacity (e.g., 160k out of 200k tokens), print: `[WARNING: Session Context Saturated at XX% (X/Y tokens). Amnesia risk is high. Re-initialize session to clear.]`.
3.  **Hard Reset Trigger:** If the token count remains above 80% after applying all condensation strategies, do not attempt further code changes in the current session. Run `/context-session END` to generate a handoff and progress log, then immediately start a new session conversation window to clear the context history.
