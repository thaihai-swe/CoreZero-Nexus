#!/usr/bin/env python3
import argparse
import json
import re
import sys
from pathlib import Path

# Regex to parse individual entries in the observability log
ENTRY_RE = re.compile(
    r"###\s+(OBS-\d+)\s+—\s+(.*?)\n(.*?)(?=\n###\s+OBS-|\n##\s+|\Z)",
    re.DOTALL
)

FIELD_RE = re.compile(
    r"-\s+(Date|Source|Class|Status|Promotion target):\s*(.*?)\n"
)

CONTENT_SECTION_RE = re.compile(
    r"\*\*(What happened|Why it matters|Proposed durable fix|Triage notes)\*\*\n(.*?)(?=\n\*\*|\Z)",
    re.DOTALL
)

def parse_args():
    parser = argparse.ArgumentParser(
        description="Parse and audit memories/repo/observability-log.md entries."
    )
    parser.add_argument(
        "--log-path",
        default="memories/repo/observability-log.md",
        help="Path to the observability log file"
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results as JSON"
    )
    parser.add_argument(
        "--check-only",
        action="store_true",
        help="Check syntax and structure without printing report"
    )
    parser.add_argument(
        "--test-mock",
        action="store_true",
        help="Run script against a mock entry dataset for validation"
    )
    return parser.parse_args()

def parse_log(file_content):
    entries = []
    for match in ENTRY_RE.finditer(file_content):
        obs_id = match.group(1).strip()
        summary = match.group(2).strip()
        body = match.group(3)

        fields = {}
        for f_match in FIELD_RE.finditer(body):
            fields[f_match.group(1).lower().replace(" ", "_")] = f_match.group(2).strip()

        content = {}
        for c_match in CONTENT_SECTION_RE.finditer(body):
            content[c_match.group(1).lower().replace(" ", "_")] = c_match.group(2).strip()

        entries.append({
            "id": obs_id,
            "summary": summary,
            "date": fields.get("date", "Unknown"),
            "source": fields.get("source", "Unknown"),
            "class": fields.get("class", "Unknown"),
            "status": fields.get("status", "open"),
            "promotion_target": fields.get("promotion_target", "none"),
            "what_happened": content.get("what_happened", ""),
            "why_it_matters": content.get("why_it_matters", ""),
            "proposed_durable_fix": content.get("proposed_durable_fix", ""),
            "triage_notes": content.get("triage_notes", "")
        })
    return entries

def generate_remediations(entries):
    remediations = []
    for entry in entries:
        if entry["status"] != "open":
            continue
        
        cls = entry["class"].lower()
        fix = entry["proposed_durable_fix"]
        
        remediation = {
            "id": entry["id"],
            "summary": entry["summary"],
            "class": entry["class"],
            "priority": "High" if cls == "harness" else "Medium",
            "action": ""
        }
        
        if "harness" in cls:
            remediation["action"] = f"Update harness-config.md or validation gates: {fix}"
        elif "model" in cls:
            remediation["action"] = f"Add normative rule to constitution.md or security-policy.md: {fix}"
        elif "spec" in cls:
            remediation["action"] = f"Add new Socratic grilling criteria to spec-requirements references: {fix}"
        else:
            remediation["action"] = f"Triage proposed fix: {fix}"
            
        remediations.append(remediation)
    return remediations

def get_mock_content():
    return """# Observability Log
## Entries
### OBS-001 — Agent bypasses verification commands
- Date: 2026-06-04
- Source: artifacts/features/test-slug/review.md
- Class: Harness
- Status: open
- Promotion target: harness-config.md

**What happened**
The agent encountered a failing test but explained it away instead of failing the gate.

**Why it matters**
Without strict mechanical constraints, agents will routinely check in broken logic.

**Proposed durable fix**
Enforce test passes by rejecting commits in pre-commit git hooks.

**Triage notes**
Pending verification.
"""

def main():
    args = parse_args()
    
    if args.test_mock:
        content = get_mock_content()
    else:
        path = Path(args.log_path)
        if not path.exists():
            # If default doesn't exist, search up or print empty list
            if args.json:
                print(json.dumps({"error": f"Log file not found at {path}"}))
                return 1
            print(f"Observability log file not found at {path}", file=sys.stderr)
            return 0
        content = path.read_text(encoding="utf-8")
        
    entries = parse_log(content)
    remediations = generate_remediations(entries)
    
    if args.check_only:
        # Validate entry formats
        invalid = [e["id"] for e in entries if e["class"] == "Unknown" or e["status"] not in ("open", "promoted", "retired")]
        if invalid:
            print(f"Validation failed for entries: {', '.join(invalid)}", file=sys.stderr)
            return 1
        print("Observability log validation passed.")
        return 0
        
    report = {
        "summary": {
            "total_entries": len(entries),
            "open_count": sum(1 for e in entries if e["status"] == "open"),
            "promoted_count": sum(1 for e in entries if e["status"] == "promoted"),
            "retired_count": sum(1 for e in entries if e["status"] == "retired"),
            "classes": {
                "harness": sum(1 for e in entries if e["class"].lower() == "harness"),
                "model": sum(1 for e in entries if e["class"].lower() == "model"),
                "spec": sum(1 for e in entries if e["class"].lower() == "spec")
            }
        },
        "open_remediations": remediations,
        "entries": entries
    }
    
    if args.json:
        print(json.dumps(report, indent=2))
    else:
        print("=== OBSERVABILITY LOG REPORT ===")
        print(f"Total Entries: {report['summary']['total_entries']}")
        print(f"Open: {report['summary']['open_count']} | Promoted: {report['summary']['promoted_count']} | Retired: {report['summary']['retired_count']}")
        print(f"Categories -> Harness: {report['summary']['classes']['harness']} | Model: {report['summary']['classes']['model']} | Spec: {report['summary']['classes']['spec']}")
        print("\n=== OPEN REMEDIATION TASKS ===")
        if not remediations:
            print("No open remediation tasks.")
        for rem in remediations:
            print(f"[{rem['priority']} Priority] {rem['id']}: {rem['summary']}")
            print(f"  Class: {rem['class']}")
            print(f"  Recommended Action: {rem['action']}\n")
            
    return 0

if __name__ == "__main__":
    sys.exit(main())
