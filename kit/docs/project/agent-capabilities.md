# Agent Capabilities

This file documents the capabilities the AI agent requires to operate this kit effectively.

## Required

| Capability | Used by |
|---|---|
| Shell execution | All skills — gate-runner, telemetry, scripts |
| File editing (read/write) | All skills — status.md, spec.md, code changes |
| Slash-command / skill invocation | All skills — routed via AGENTS.md |

## Recommended

| Capability | Used by |
|---|---|
| Subagent spawning | `starter-init` (Phase A archaeology sweep), `spec-research` (structural feature exploration) |

## Optional

| Capability | Used by |
|---|---|
| Python 3 | `visualize`, `scripts/context-loader.py`, `scripts/generate-dashboard.py` |
| `mmdc` (Mermaid CLI) | `visualize` — SVG diagram export |
