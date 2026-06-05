# Client Integrations


## Integration Pattern

### 1. Router-First

Every client reads `AGENTS.md` as the entry point. It's a thin router (< 50 lines) that points to:
- Skills for workflow
- Memory files for context
- Harness config for commands

### 2. Skill Loading

Skills are loaded just-in-time when invoked. The agent reads the relevant `SKILL.md` and its `references/` directory. This keeps the context window lean.

### 3. Memory as Shared State

All clients share the same memory layer (`memories/repo/`). This means:
- Constitution rules apply regardless of which client is used
- Security policy is enforced uniformly
- Knowledge base is available to all agents
- Harness config provides consistent commands

## Multi-Client Projects

When multiple clients work on the same project:
- All share the same `memories/repo/` (single source of truth)
- All share the same `artifacts/features/` (durable state)
- Handoffs work across clients (handoff.md is client-agnostic)
- The harness config captures commands that work for all clients

## Golden Config Pattern

For each client, the ideal setup:
1. Client reads its entrypoint file automatically
2. Entrypoint routes to `AGENTS.md` for operating rules
3. Agent loads skills JIT when invoked
4. Memory provides durable context without re-discovery
5. Artifacts provide feature state without chat history dependency
