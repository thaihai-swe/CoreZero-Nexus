---
name: context-compact
description: Compresses and garbage-collects oversized memory files to preserve token context.
compatibility: Designed for AI coding agents.
---

# Context Compact

## Overview
As a project matures, memory files (`learned-heuristics.md`, `project-knowledge-base.md`, `core-policies.md`) grow. Long files cause LLM "amnesia" and context window saturation. This skill safely summarizes, deduplicates, and prunes these files while retaining 100% of their critical intent.

## I/O Hand-off Protocol
- **Reads**: Target oversized file from `memories/repo/`.
- **Writes**: Pruned version of the target file.
- **Next Skill**: Done.

## Workflow
1. **Analyze**: Read the target memory file and identify redundant information, overly verbose explanations, and deprecated rules.
2. **Compress**: Rewrite the file using the following techniques:
   - Convert lengthy paragraphs to concise bullet points.
   - Combine duplicate or overlapping rules into a single constraint.
   - Remove obsolete gotchas that are no longer relevant to the current architecture.
3. **Verify Integrity**: Ensure no normative rules (CC-* identifiers) or critical architectural constraints were lost during compression.
4. **Update**: Overwrite the original file with the leaner, compacted version.

## Core Rules
- **No Data Loss**: Compaction means reducing word count, not deleting active constraints.
- **Aggressive Brevity**: Aim for a 50% reduction in line count.
- **Header Preservation**: Do not remove primary `##` headers; only compress the content underneath them.
