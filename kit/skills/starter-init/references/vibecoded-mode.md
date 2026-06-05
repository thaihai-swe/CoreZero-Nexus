## Vibe-Coded Mode

Activate when the repository has code but none of the following: organized test suite, CI/CD pipeline, documented architecture, or consistent conventions. Common symptoms: a single large file, no `README`, mixed patterns, no package manager lock files, no linter config.

> **Goal:** Enumerate reality, define the first verifiable proof surface, document all unknowns explicitly, and gate further work on explicit user acknowledgment — not on an idealized baseline that doesn't exist.

---

### Detection Checklist

The agent must check all of the following and record results before proceeding:

| Signal | Vibe-Coded Indicator |
|--------|----------------------|
| Test files (`*_test.*`, `test_*`, `*.spec.*`, `tests/`) | **None found** |
| Build / run script (`Makefile`, `package.json`, `pyproject.toml`, `Cargo.toml`) | **None or unconfigured** |
| Linter config (`.eslintrc`, `.flake8`, `ruff.toml`, `.rubocop.yml`) | **None found** |
| CI config (`.github/workflows/`, `.gitlab-ci.yml`, `Jenkinsfile`) | **None found** |
| Architecture docs (`README.md`, `docs/`, `ARCHITECTURE.md`) | **None or skeleton only** |
| Code style: consistent naming, file structure, import patterns | **Inconsistent or absent** |

If 3+ indicators are true → **Vibe-Coded Mode is active**.

If 1-2 indicators are true → evaluate as **Brownfield Mode** with a note about the missing coverage areas.

---

### Vibe-Coded Mode Steps

#### Step 1: Enumerate What Exists (No Judgment)

Produce a factual inventory — do not editorialize. Write findings to `memories/repo/project-knowledge-base.md` under `## Vibe-Coded Inventory`:

```
## Vibe-Coded Inventory

Recorded: <date>

### Entry Points
- List all files that appear to be entry points (e.g., main.py, index.js, app.rb)

### Data Surfaces
- List any files that touch databases, files on disk, or external APIs

### Dependencies
- List all external libraries found in imports or package files

### Unreachable / Dead Code
- Flag obvious dead code or commented-out blocks

### Code Style Observations
- Note: consistent/inconsistent naming, file structure, error handling patterns

### Known Unknowns
- List things the agent could not determine from reading the code
```

#### Step 2: Define the First Verifiable Proof Surface

Since there are no tests and no build script, the agent must define the **minimum viable proof surface** — the simplest command that proves the code does something measurable:

1. **Try to run the code**: Can `python main.py` or `node index.js` execute without error?
2. **If yes**: Record that command as the proof surface. Note its output.
3. **If no**: Document the error. Record it in `memories/repo/harness-config.md` under `## Known Baseline Errors`.
4. **If indeterminate** (e.g., the code appears to be a library with no entry point): Define a lint-only proof surface: `python -m py_compile *.py` or equivalent static check.

Document the proof surface in `memories/repo/harness-config.md`:

```
## Proof Surface (Vibe-Coded Baseline)
Command: <exact command>
Expected output: <what a passing run produces>
Acceptable failure mode: <what a partial-pass looks like>
Established: <date>
```

#### Step 3: Flag Security-Sensitive Surfaces

Before any feature work, scan for and flag in `memories/repo/security-policy.md`:

- Any hardcoded credentials, API keys, tokens, or passwords in the code
- Files that open sockets, make HTTP requests, or call external APIs
- Files that write to disk, environment variables, or system state
- Any exec/eval/subprocess calls with dynamic input

Record each finding as:

```
## Vibe-Coded Security Flags
- [HIGH] <file>:<line> — Hardcoded credential found
- [MEDIUM] <file> — External API call, unclear auth model
- [LOW] <file> — Dynamic input to shell command
```

Do NOT fix these findings during init. Flag and continue.

#### Step 4: Set Rigor Profile to Standard Minimum

Vibe-Coded repos must never use the Tiny profile for new features. Record in `memories/repo/harness-config.md`:

```
## Rigor Override
Default profile: Standard (minimum)
Rationale: Vibe-Coded baseline — no test suite, increased discipline required for all changes.
```

#### Step 5: Require User Acknowledgment

Before handing off to `/spec-requirements` or `/spec-research`, produce a **Vibe-Coded Baseline Report** and require explicit user acknowledgment:

```
## Vibe-Coded Baseline Report

Repository: <name>
Mode: Vibe-Coded (3+ vibe-coded indicators active)

### What Was Found
<inventory summary — 5-10 bullets>

### What Is Not Known
<unknown items — be explicit>

### Proof Surface
<the command defined in Step 2>

### Security Flags
<count and severity summary>

### Risks Before Feature Work
- No automated safety net — any change could silently break behavior
- No existing tests means the first feature must establish the baseline
- Security flags listed above require manual review before touching those files

### Required Acknowledgment
Before proceeding with feature work, confirm:
[ ] I have reviewed the Vibe-Coded inventory above
[ ] I accept that there are no automated tests yet — the first feature will establish them
[ ] I have read and acknowledged the security flags
[ ] I want to proceed with feature work using the Standard rigor minimum

Type "acknowledged" to continue.
```

Do NOT create feature artifacts (`spec.md`, `tasks.md`, etc.) until the user acknowledges.

---

### Vibe-Coded Mode Stop Conditions

- The agent cannot determine any valid entry point or proof surface — requires user clarification before continuing.
- Security flags include hardcoded production credentials — halt and require immediate remediation, do not proceed with feature work.
- The user declines to acknowledge — record the refusal and wait.

---

### After Acknowledgment: First Feature Obligation

The first feature delivered in a Vibe-Coded repository **must** include:

1. A test file that covers the changed behavior — this becomes the first regression anchor.
2. A `Makefile` or `package.json` script entry that runs the test (the canonical proof command).
3. An update to `memories/repo/harness-config.md` replacing the Vibe-Coded proof surface with the new automated command.

This is non-negotiable. `/harness-verify` will fail if no test exists for code that was changed in a Vibe-Coded repo.
