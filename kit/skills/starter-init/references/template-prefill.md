## Template Pre-Fill Mode

The bootstrap script copies 8 fillable documents to `docs/` plus `docs/architecture.md` as a living doc. This skill pre-fills them so the user starts from evidence-based drafts instead of empty files. The goal is to reduce manual fill-in work, especially in brownfield repos where the answers already live in the code.

**Tier 1 — AI Pre-Fills From Code Evidence (user refines later):**

Read the repository and populate these from concrete evidence. Cite the source (file or config) where it adds confidence. Never invent values.

| Template | Pre-Fill From |
|---|---|
| `docs/TECH_STACK_REFERENCE.md` | `package.json`, `pyproject.toml`, `go.mod`, `Cargo.toml`, lockfiles, import statements, framework config |
| `docs/architecture.md` | Top-level folder layout, module boundaries, entry points, build/CI config |
| `docs/QUALITY_POLICY.md` | Linter/formatter config (`.eslintrc`, `ruff.toml`, etc.), test runner config, coverage thresholds |
| `docs/PROJECT_CONSTRAINTS.md` | CI/CD settings, runtime version pins, resource limits, declared compliance tooling |

**Tier 2 — AI Asks Clarifying Questions (user-owned context):**

These need product, business, or policy context that is not reliably inferable from code. Ask 2-4 focused questions per template, then fill what the user answers. Leave unanswered sections as `[USER REVIEW NEEDED]`.

| Template | Ask About |
|---|---|
| `docs/PRODUCT_SENSE.md` | Who the users are, the core problem, success metrics |
| `docs/GLOSSARY.md` | Domain terms with ambiguous or overloaded meaning |
| `docs/GOVERNANCE.md` | Who approves changes, required reviewers, release gates |
| `docs/RELIABILITY_POLICY.md` | SLOs, acceptable downtime, error-budget posture |

**Tier 3 — Left For Later (not pre-filled at init):**

- `docs/TECH_DEBT_REGISTER.md` — populated by `harness-verify` fallow pass during feature work

**Pre-Fill Rules:**

- **Brownfield:** Pre-fill Tier 1 aggressively from code. The repository is the system of record.
- **Greenfield:** Tier 1 evidence is thin. Fill what config exists, mark the rest `[USER REVIEW NEEDED]`.
- **No fabrication:** If a value is not in the code and the user has not stated it, mark it `[USER REVIEW NEEDED]`. Do not guess product vision, SLOs, or compliance requirements.
- **Idempotent:** If a template already has user content (not the original template body), do not overwrite it. Append observations under a clearly marked section instead.
- **Report:** After pre-fill, list which templates were filled, which need user review, and where `[USER REVIEW NEEDED]` markers remain.

