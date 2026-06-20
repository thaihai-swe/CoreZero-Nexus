# Spec Template: Agentic System

<!-- Use this template when the feature involves multiple AI agents coordinating, delegating, or communicating. Extends the standard spec template with agent-specific sections. -->

## Problem Statement

## Target Users

## Agent Architecture

### Agents Involved

| Agent | Role | Capabilities | Boundaries |
|-------|------|-------------|------------|
| | | | |

### Communication Pattern

<!-- How do agents communicate? (Direct messaging, shared state, event-driven, orchestrator-worker, etc.) -->

### Delegation Model

<!-- Who delegates to whom? What are the delegation rules? -->

- **Orchestrator:** 
- **Workers:** 
- **Escalation path:** 

### Shared State

<!-- What state is shared between agents? Where does it live? Who owns it? -->

| State | Owner | Readers | Storage |
|-------|-------|---------|---------|
| | | | |

## Scenarios

### S1: [Happy path — agents coordinate successfully]

### S2: [Agent failure — one agent fails or times out]

### S3: [Conflict — agents produce contradictory outputs]

## Requirements

- **REQ-1:** 
- **REQ-2:** 

## Acceptance Criteria

- **AC-1 (REQ-1):** Proof:
- **AC-2 (REQ-2):** Proof:

## Agent-Specific Constraints

### Context Window Budget

| Agent | Max Context | Loading Strategy |
|-------|-------------|-----------------|
| | | |

### Permission Boundaries

| Agent | Can Do | Cannot Do | Requires Confirmation |
|-------|--------|-----------|----------------------|
| | | | |

### Failure Modes

| Failure | Detection | Recovery | Fallback |
|---------|-----------|----------|----------|
| Agent timeout | | | |
| Contradictory output | | | |
| Context overflow | | | |
| Hallucination | | | |

## Verification Surface

- Unit tests:
- Integration tests:
- Agent interaction tests:
- Failure injection tests:

## Gray-Area Decisions

## Scope

### In Scope

### Out of Scope

### Non-Goals
