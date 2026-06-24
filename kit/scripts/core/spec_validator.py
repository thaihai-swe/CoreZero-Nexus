#!/usr/bin/env python3
import argparse
import json
import os
import re
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
_PARENT = str(_SCRIPT_DIR.parent)
if _PARENT not in sys.path:
    sys.path.insert(0, _PARENT)

from core._lib.yaml_reader import load as load_yaml


def load_schema(path):
    with open(path) as f:
        return json.load(f)


def validate_frontmatter(spec_path, schema, strict=False):
    try:
        text = Path(spec_path).read_text(encoding="utf-8")
    except FileNotFoundError:
        return [f"Spec file not found: {spec_path}"], {}
    lines = text.split("\n")
    meta = {}
    in_meta = False
    for line in lines:
        if line.strip().startswith("## Metadata"):
            in_meta = True
            continue
        if in_meta:
            if line.strip().startswith("## "):
                break
            if "- " in line:
                parts = line.split("- ", 1)[1] if "- " in line else ""
                if ":" in parts:
                    key, val = parts.split(":", 1)
                    meta[key.strip().lower().replace(" ", "_")] = val.strip()
    errors = []
    if "feature" not in meta:
        errors.append("Missing required field: feature")
    if "slug" not in meta:
        errors.append("Missing required field: slug")
    if "status" not in meta:
        errors.append("Missing required field: status")
    if strict and "profile" not in meta:
        errors.append("Missing required field: profile")
    return errors, meta


def validate_req_ac_linkage(spec_path):
    text = Path(spec_path).read_text(encoding="utf-8")
    errors = []
    req_pattern = re.compile(r"### (REQ-\d+)")
    ac_pattern = re.compile(r"AC-(\d+)")
    current_req = None
    reqs_without_ac = []
    for line in text.split("\n"):
        req_match = req_pattern.search(line)
        if req_match:
            current_req = req_match.group(1)
            continue
        if current_req and ac_pattern.search(line):
            current_req = None
    req_pattern_all = re.compile(r"\b(REQ-\d+)\b")
    seen_reqs = set(req_pattern_all.findall(text))
    for req in seen_reqs:
        req_block = _get_block(text, req)
        if req_block and not ac_pattern.search(req_block):
            reqs_without_ac.append(req)
    if reqs_without_ac:
        errors.append(f"Requirements missing AC mapping: {', '.join(reqs_without_ac)}")
    return errors


def validate_ac_has_command(spec_path):
    text = Path(spec_path).read_text(encoding="utf-8")
    errors = []
    ac_pattern = re.compile(r"\bAC-(\d+)\b")
    acs = set(ac_pattern.findall(text))
    for ac_id in sorted(acs):
        ac_block = _get_block(text, f"AC-{ac_id}")
        if ac_block and "Verification:" not in ac_block and "verification:" not in ac_block:
            errors.append(f"AC-{ac_id} has no verification command")
    return errors


def validate_nfr_coverage(spec_path):
    text = Path(spec_path).read_text(encoding="utf-8")
    nfr_pattern = re.compile(r"### (NFR-\d+)")
    nfrs = nfr_pattern.findall(text)
    return nfrs


def compute_readiness(spec_path):
    text = Path(spec_path).read_text(encoding="utf-8")
    score = 1
    lines = text.split("\n")
    req_count = len(re.findall(r"\bREQ-\d+\b", text))
    ac_count = len(re.findall(r"\bAC-\d+\b", text))
    nfr_count = len(re.findall(r"\bNFR-\d+\b", text))
    risk_count = len(re.findall(r"\bRISK-\d+\b", text))
    if req_count >= 3:
        score += 1
    if ac_count >= req_count:
        score += 1
    if nfr_count >= 1:
        score += 1
    if risk_count >= 1:
        score += 1
    return min(score, 5)


def check_staleness(spec_path):
    text = Path(spec_path).read_text(encoding="utf-8")
    if "[STALE]" in text:
        return True, "Spec contains [STALE] marker — phase reset recommended"
    return False, "No staleness detected"


def _get_block(text, marker):
    lines = text.split("\n")
    in_block = False
    block_lines = []
    for line in lines:
        if marker in line and not in_block:
            in_block = True
            block_lines.append(line)
            continue
        if in_block:
            if line.strip().startswith("### ") or line.strip().startswith("---"):
                break
            block_lines.append(line)
    return "\n".join(block_lines)


def validate_traceability(spec_path, tasks_path):
    spec_text = Path(spec_path).read_text(encoding="utf-8")
    tasks_text = Path(tasks_path).read_text(encoding="utf-8")
    errors = []
    all_ac = set(re.findall(r"\b(AC-\d+)\b", spec_text))
    all_req = set(re.findall(r"\b(REQ-\d+)\b", spec_text))
    all_task = set(re.findall(r"\b(TASK-\d+)\b", tasks_text))
    unmapped_ac = [ac for ac in all_ac if ac not in tasks_text]
    unmapped_req = [req for req in all_req if req not in tasks_text]
    if unmapped_ac:
        errors.append(f"ACs not found in tasks.md: {', '.join(unmapped_ac)}")
    if unmapped_req:
        errors.append(f"REQs not found in tasks.md: {', '.join(unmapped_req)}")
    for task in all_task:
        block = _get_block(tasks_text, f"**{task}**")
        if block and not re.search(r"Proof:|Evidence:|Status:\s*(Done|Pass)", block):
            errors.append(f"{task} has no evidence/proof")
    return errors


def main():
    parser = argparse.ArgumentParser(description="CoreZero Spec Validator")
    parser.add_argument("--spec", required=True, help="Path to spec.md")
    parser.add_argument("--schema", default="", help="Path to spec-schema.json")
    parser.add_argument("--strict", action="store_true", help="Fail on missing optional fields")
    parser.add_argument("--traceability", action="store_true", help="Run traceability audit")
    parser.add_argument("--tasks", default="", help="Path to tasks.md (for traceability)")
    parser.add_argument("--readiness", action="store_true", help="Compute readiness score")
    parser.add_argument("--staleness", action="store_true", help="Check for stale markers")
    parser.add_argument("--validate-all", action="store_true", help="Validate all specs in project")
    parser.add_argument("--root", default="", help="Repository root")
    args = parser.parse_args()

    if args.validate_all:
        root = Path(args.root) if args.root else Path.cwd()
        spec_dir = root / "artifacts" / "features"
        if not spec_dir.exists():
            print("No features directory found")
            return
        total = 0
        errors = 0
        for feat_dir in spec_dir.iterdir():
            spec_file = feat_dir / "spec.md"
            if spec_file.exists():
                total += 1
                e, _ = validate_frontmatter(str(spec_file), None, args.strict)
                e2 = validate_req_ac_linkage(str(spec_file))
                if e or e2:
                    print(f"FAIL: {spec_file}")
                    for err in e + e2:
                        print(f"  {err}")
                    errors += 1
        print(f"Validated {total} specs, {errors} failures")
        if errors:
            sys.exit(1)
        return

    if not os.path.exists(args.spec):
        print(f"ERROR: Spec not found: {args.spec}", file=sys.stderr)
        sys.exit(1)

    all_errors = []

    schema = None
    if args.schema and os.path.exists(args.schema):
        schema = load_schema(args.schema)
    fm_errors, meta = validate_frontmatter(args.spec, schema, args.strict)
    all_errors.extend(fm_errors)

    linkage_errors = validate_req_ac_linkage(args.spec)
    all_errors.extend(linkage_errors)

    cmd_errors = validate_ac_has_command(args.spec)
    if args.strict:
        all_errors.extend(cmd_errors)

    if args.traceability:
        if not args.tasks or not os.path.exists(args.tasks):
            print("ERROR: --tasks required for --traceability", file=sys.stderr)
            sys.exit(1)
        trace_errors = validate_traceability(args.spec, args.tasks)
        all_errors.extend(trace_errors)

    if args.readiness:
        score = compute_readiness(args.spec)
        nfrs = validate_nfr_coverage(args.spec)
        print(f"Readiness score: {score}/5")
        print(f"Requirements: {len(re.findall(r'\\bREQ-\\d+\\b', Path(args.spec).read_text()))}")
        print(f"Acceptance criteria: {len(re.findall(r'\\bAC-\\d+\\b', Path(args.spec).read_text()))}")
        print(f"NFRs: {len(nfrs)}")
        print(f"Risks: {len(re.findall(r'\\bRISK-\\d+\\b', Path(args.spec).read_text()))}")

    if args.staleness:
        stale, msg = check_staleness(args.spec)
        print(msg)
        if stale:
            all_errors.append(msg)

    if all_errors:
        for e in all_errors:
            print(f"FAIL: {e}", file=sys.stderr)
        sys.exit(1)
    if not args.readiness and not args.staleness:
        print("PASS: spec validation passed")


if __name__ == "__main__":
    main()
