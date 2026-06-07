# Kit Documentation

> **Who is this for?**
> — **Adopting the kit into a project?** → Go to [`docs/`](../kit/docs/README.md) instead.
> — **Maintaining or evolving the kit itself?** → You are in the right place. Start with the orientation list below.

This is the canonical maintainer documentation surface for the CoreZero Nexus source repository. All installer assets (skills, templates, and rules) are located under the [`kit/`](../kit/) directory in this source repository.

---

## The Core Value Proposition

Generative AI code generation is fast but often suffers from "AI slop," code bloat, context amnesia, and silent regressions. CoreZero Nexus addresses these challenges through four foundational pillars:

> [!IMPORTANT]
> **1. Spec-Driven Discipline**: No code is written until a granular specification (`spec.md`) is locked and mapped to concrete acceptance criteria (`AC-*`).
>
> **2. Continuous Verification**: Every code change is gated behind an automated mechanical verification commands loop (lints, builds, tests) to guarantee zero broken baselines.
>
> **3. Zero Amnesia Context**: Active sessions are checkpointed, compacted, and handed off seamlessly, ensuring the agent never "forgets" requirements in large codebases.
>
> **4. Durable Knowledge Compounding**: After every successful feature deployment, the kit sweeps session logs to update a central repository memory tier, making future agent runs progressively smarter.

---

## 1. Document Architecture & Navigation

The documentation set is organized into three tiers to allow maintainers to progress from high-level workflows to deep architectural specs.

### Tier 1: Core Guides
* **[skills-guide.md](skills-guide.md)** — The command taxonomy, guided learning flow, and internal lineages.
* **[packs.md](packs.md)** — Breakdown of the 4 core packs: Project Starter, Context Engineering, Spec-Driven Development, and Harness Engineering.
* **[end-to-end-tutorial.md](end-to-end-tutorial.md)** — Step-by-step developer tutorial walking through all 15 commands in a sample lifecycle.
* **[evaluation-report.md](evaluation-report.md)** — End-to-end evaluation report covering architecture, context management gaps, and template blueprints.
* **[INSTALL.md](INSTALL.md)** — Requirements, installation steps, upgrade mechanics, and rollback instructions.

### Tier 2: Technical & Context Systems
* **[context-memory.md](context-memory.md)** — The 6 context tiers, dynamic memory index routing, 3-tier memory model, compaction rules, and self-improving loop.
* **[HARNESS_ENGINEERING.md](HARNESS_ENGINEERING.md)** — Harness engineering core theory, the 6 subsystems, OpenAI advanced agent principles, and GC loops.
* **[architecture.md](architecture.md)** — File layer layouts, entrypoint routing, data flows, and skill structure.
* **[reference.md](reference.md)** — Quick lookup tables for commands, templates, feature artifacts, and memories.
* **[TEMPLATE_SURFACE.md](TEMPLATE_SURFACE.md)** — Breakdown of file categories, installer overwrite/preserve settings, and file ownership rules.

### Tier 3: Operations & Strategy
* **[adoption-strategies.md](adoption-strategies.md)** — Scale triaging (Tiny/Standard/Complex), Greenfield onboarding, and Brownfield reverse mapping.
* **[evals.md](evals.md)** — Split-mode verification gates (Mechanical, Alignment, Security, Continuity), spec scoring, and regression checks.
* **[integrations.md](integrations.md)** — Standard IDE and agent client routing configurations (Claude Code, Cursor, Gemini).
* **[releasing.md](releasing.md)** — Git tagging strategies, Conventional Commit auto-bumps, release branches, and versioning checklists.

---

## 2. Visual Diagrams

Mermaid diagram source files live under [`diagrams/`](diagrams/). See the [diagram directory map](diagrams/README.md) for individual files and validator details.
