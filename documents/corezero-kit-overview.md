# CoreZero Development Kit: The Autonomous SDLC

The CoreZero Development Kit is not just a collection of prompts; it is a **highly-disciplined, artifact-driven Operating System for AI Agents**.

Standard AI coding tools suffer from "Context Collapse"—as a project grows, the AI hallucinates, loses track of constraints, overwrites working code, and gets stuck in infinite retry loops trying to fix failing tests.

CoreZero solves this by replacing conversational coding with a strict **Autonomous Software Development Lifecycle (SDLC)**. The agent is bound by mechanical gates, traceability audits, circuit breakers, and a sophisticated memory hierarchy.

---

## 1. The Core Differentiators: Why the Kit is Powerful

### A. The Circuit Breaker & Telemetry System
The kit prevents "vibe coding" and infinite retry loops. Every time an agent fails a mechanical test during implementation, the failure is logged to `memories/repo/harness-telemetry.md` as an Observation (`OBS-NNN`).
If an agent fails **two consecutive times** on the same task, the **Circuit Breaker trips**. The agent is mechanically locked out of the `Implementing` phase and forced to route back to `/spec-plan` to rethink its architectural approach. It cannot blindly guess its way to a passing test.

### B. 100% Traceability Audits
Hallucinations and dropped requirements are eliminated mechanically. Before a feature can be marked `Done`, the `/harness-verify` skill runs a traceability audit (`traceability-audit.sh`).
- Every Acceptance Criterion in `spec.md` must map to a Task in `tasks.md`.
- Every Task must have a recorded passing terminal command proving it works.
- If there is a single requirement without proof, the build fails.

### C. The Three-Track Memory System
Instead of dumping the entire codebase into the AI's context window (which destroys attention span), the kit uses a tiered memory system to maintain Minimum Viable Context (MVC):
1. **Instruction Tier (`core-policies.md`):** The absolute, unbending constitutional laws of the repo (e.g., "Do not use Tailwind").
2. **Auto Tier (`harness-telemetry`):** The mechanical log of what approaches failed and why, preventing future agents from attempting known-bad solutions.
3. **Extracted Tier (`learned-heuristics.md`):** Durable architectural lessons (e.g., "We use `sqlite:///:memory:` for tests") extracted by `/context-memory` at the end of every feature session.

### D. Subagent Parallelization
The kit supports horizontal scaling. During the Planning phase (`/spec-plan`), the agent identifies independent, non-blocking components and flags them with `[P]`. During Implementation, the master agent can spawn isolated Subagents to build these components in parallel, merging them securely via mechanical gates.

---

## 2. The Core Delivery Loop (Feature Lifecycle)

Every feature moves sequentially through this strict pipeline. An agent cannot proceed to the next phase without producing a validated Markdown artifact.

1. **`/spec-research`**: *Investigation.* Used for brownfield repos or complex bugs. Maps the current undocumented behavior before deciding what to build.
2. **`/spec-requirements`**: *Definition.* The AI interviews the user to resolve ambiguity. Outputs `spec.md` with strict, binary pass/fail Acceptance Criteria.
3. **`/spec-plan`**: *Architecture.* Converts the spec into `plan.md` (Technical Design) and `tasks.md` (A strict checklist of 2-hour implementation slices).
4. **`/spec-implement`**: *Execution.* The AI writes code, but is strictly bound by `tasks.md`. It must run pre-flight baselines, write code, run post-flight tests, and log telemetry for any failures.
5. **`/harness-verify`**: *Auditing.* The AI audits its own work. Runs mechanical gates (`gate-runner.sh`), verifies traceability, checks security boundaries, and outputs `review.md`.

---

## 3. Governance & Self-Healing Skills

The kit doesn't just build code; it maintains its own health and architectural integrity.

*   **/spec-adr**: Pauses the delivery loop to document Architecture Decision Records (ADRs) when facing contested technical choices (e.g., "PostgreSQL vs MongoDB").
*   **/context-session**: Handles the boundaries of conversations (`START`, `CHECKPOINT`, `END`). Manages `handoff.md` so that work can be transferred seamlessly across days, contexts, or different agents without losing a beat.
*   **/context-memory**: The long-term learning mechanism. Extracts lessons at the end of a session and updates the agent's global knowledge base.
*   **/context-compact**: Automatically detects when a memory file or log grows too large and safely summarizes it in-place, preventing token saturation while retaining 100% of the normative intent.
*   **/code-review**: Evaluates code health, complexity, naming, and style against Google's Engineering Practices.
*   **/ponytail**: Forces the "lazy senior developer" mindset: aggressively preventing over-engineering and demanding standard library usage over custom abstractions.
*   **/harness-maintain**: The Meta-Skill. Evaluates the health of the AI kit itself. By reading telemetry failure logs, this skill rewrites the agent's own rules, indexes, and heuristics to improve future autonomous performance.

---

## 4. Documentation & Observability

*   **/technical-docs**: Generates scoped developer guides specifically for a newly shipped feature.
*   **/codebase-documenter**: Generates broad, multi-file documentation for human onboarding (architecture, component relationships, deployment guides).
*   **/visualize**: Generates Mermaid diagrams and SVGs to visualize complex data flows or state machines.
*   **/context-status**: The AI Project Manager. Scans all active feature logs and generates a high-level HTML dashboard reporting on progress, blockers, and next steps across the entire repository.
*   **/spec-testing-scenario**: Drafts an optional, user-invoked manual testing scenarios guide covering happy paths and edge cases for a feature.

---

## Summary of the Flow
1. Start with **`/starter-init`**.
2. Jump into the feature loop (**`/spec-research`** ➔ **`/spec-requirements`** ➔ **`/spec-plan`** ➔ **`/spec-implement`** ➔ **`/harness-verify`**).
3. If things get complicated, branch out into **`/spec-adr`**, **`/code-review`**, or **`/spec-testing-scenario`**.
4. When the feature ships, document it with **`/technical-docs`**.
5. Wrap up every day using the Context Governance commands (**`/context-memory`** ➔ **`/context-session END`**).


## Summary
The CoreZero Kit transforms an LLM from a "glorified autocomplete" into an **autonomous engineering team**. By wrapping the agent in mechanical gates, strict traceability, and durable memory, it ensures that complex software can be scaled infinitely without the typical AI degradation loop.
