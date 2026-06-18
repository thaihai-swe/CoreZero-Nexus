---
name: context-session
description: Manage the start/end of a coding session.
compatibility: Designed for AI coding agents.
---

# Context Session

## Overview
Used to bootstrap context at the start of a session or summarize at the end.

## I/O Hand-off Protocol
- **Reads**: `memories/repo/harness-telemetry.md`
- **Writes**: `memories/repo/harness-telemetry.md`

## Workflow
1. **Prune Telemetry**: If ending a session or if `memories/repo/harness-telemetry.md` exceeds 500 lines, compress older closed tasks and log entries into a summarized historical record while keeping the active state verbose.
