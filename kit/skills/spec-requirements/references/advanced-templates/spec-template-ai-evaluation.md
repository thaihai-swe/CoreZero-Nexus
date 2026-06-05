# Spec Template: AI Model Evaluation

<!-- Use this template when the feature involves evaluating, testing, or validating AI model behavior — including prompt engineering, model selection, fine-tuning validation, or safety testing. -->

## Problem Statement

## Target Users

## Evaluation Architecture

### Model Under Test

| Property | Value |
|----------|-------|
| Model | |
| Provider | |
| Version/Checkpoint | |
| Task type | |
| Input format | |
| Output format | |

### Evaluation Dimensions

| Dimension | Metric | Threshold | Priority |
|-----------|--------|-----------|----------|
| Accuracy | | | |
| Latency | | | |
| Cost | | | |
| Safety | | | |
| Consistency | | | |
| Hallucination rate | | | |

### Test Dataset

| Dataset | Size | Source | Coverage | Refresh Cadence |
|---------|------|--------|----------|-----------------|
| | | | | |

## Scenarios

### S1: [Happy path — model produces correct output]

### S2: [Edge case — ambiguous or adversarial input]

### S3: [Safety violation — harmful or biased output]

### S4: [Regression — model quality degrades after update]

### S5: [Cost overrun — token usage exceeds budget]

## Requirements

- **REQ-1:** 
- **REQ-2:** 

## Acceptance Criteria

- **AC-1 (REQ-1):** Proof:
- **AC-2 (REQ-2):** Proof:

## Evaluation-Specific Constraints

### Prompt/Input Specification

- System prompt:
- Input template:
- Few-shot examples: [count]
- Context window budget:

### Output Validation

| Check | Method | Threshold |
|-------|--------|-----------|
| Format compliance | | |
| Factual accuracy | | |
| Hallucination detection | | |
| Toxicity/safety | | |
| Consistency (same input → similar output) | | |

### Baseline & Regression

- Baseline model/version:
- Baseline scores:
- Regression threshold: [% degradation that triggers alert]
- A/B comparison method:

### Cost & Performance Budget

- Max tokens per request:
- Max cost per evaluation run:
- Max latency (p95):
- Batch size:

### Human Review

- Review sample rate: [% of outputs reviewed by humans]
- Review criteria:
- Escalation threshold:
- Reviewer qualifications:

## Verification Surface

- Automated eval suite:
- Human review queue:
- Regression tests:
- Safety/red-team tests:
- Cost monitoring:

## Gray-Area Decisions

## Scope

### In Scope

### Out of Scope

### Non-Goals
