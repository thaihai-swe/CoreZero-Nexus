# Codemap

> Generated reference. Refresh when the installed surface changes materially.

## Top-Level Map

| Path | Responsibility | Notes |
| :--- | :--- | :--- |
| `AGENTS.md` | Thin router for load order and workflow entry | Keep under 50 lines |
| `HARNESS_CARD.md` | Harness summary and known limits | Read before non-trivial work |
| `docs/` | Installed operating docs | Includes `README.md`, `ADOPTION_GUIDE.md`, `INSTALL.md`, policy docs, generated refs, and `architecture.md` |
| `memories/repo/` | Durable rules, commands, and knowledge | `INDEX.md` routes memory loading |
| `skills/` | Canonical workflow contracts | Public commands map to these skill folders |
| `scripts/` | Install, repair, and validation helpers | Includes `install.sh`, `doctor.sh`, `check-surface-truth.py` |
| `.github/workflows/` | Consistency automation | `harness-check.yml` |

## Key Entrypoints

- Path: `docs/README.md`
  Purpose: first stop after install
  Watchouts: must only reference installed files

- Path: `scripts/install.sh`
  Purpose: manifest-driven installer
  Watchouts: must preserve adopter-owned seeded files

- Path: `scripts/doctor.sh`
  Purpose: repair and drift-check entrypoint
  Watchouts: runs structural checks, not feature verification
