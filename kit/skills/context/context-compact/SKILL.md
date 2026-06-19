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
1. **Analyze**: Read the target memory file and identify redundant information, overly verbose explanations, and deprecated rules. Run the **Pre-compaction snapshot** protocol first.
2. **Compress**: Rewrite the file using the following techniques:
   - Convert lengthy paragraphs to concise bullet points.
   - Combine duplicate or overlapping rules into a single constraint.
   - Remove obsolete gotchas that are no longer relevant to the current architecture.
3. **Verify Integrity**: Perform the **Post-compaction verification** protocol to ensure no normative rules (CC-* identifiers) or critical architectural constraints were lost during compression.
4. **Update**: Overwrite the original file with the leaner, compacted version.

## Core Rules
- **No Data Loss**: Compaction means reducing word count, not deleting active constraints.
- **Safety Protocol is Mandatory**: Never compact without backing up and running CC-* identifier verification.
- **Aggressive Brevity**: Aim for a 50% reduction in line count.
- **Header Preservation**: Do not remove primary `##` headers; only compress the content underneath them.

## Safety Protocol (MUST run before and after every compaction)

**Pre-compaction snapshot:**
1. Copy the target file to `<filename>.bak` in the same directory.
2. Record all CC-* identifiers present: `grep "CC-[0-9]" <file> | sort`.

**Post-compaction verification:**
3. Record all CC-* identifiers in the compacted file.
4. Diff the two lists. If any CC-* identifier is missing from the compacted version, ABORT — restore from `.bak` and report which identifiers were lost.
5. Print line counts: before and after. If reduction is less than 20%, the file was not oversized — do not compact.
6. Only delete `.bak` after the user confirms the compacted file is acceptable.
