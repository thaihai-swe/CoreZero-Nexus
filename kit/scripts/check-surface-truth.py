#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


MARKDOWN_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)]+)\)")
IMAGE_LINK_RE = re.compile(r"!\[[^\]]*\]\(([^)]+)\)")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Validate that the documented CoreZero surface points at real files."
    )
    parser.add_argument(
        "--mode",
        choices=("source-repo", "installed"),
        required=True,
        help="Validation rules for the source repository or an installed downstream repo.",
    )
    parser.add_argument(
        "--root",
        default=".",
        help="Repository root to validate.",
    )
    return parser.parse_args()


def is_external(target: str) -> bool:
    return (
        target.startswith("#")
        or "://" in target
        or target.startswith("mailto:")
        or target.startswith("app://")
    )


def link_targets(text: str) -> list[str]:
    targets = []
    for pattern in (MARKDOWN_LINK_RE, IMAGE_LINK_RE):
        for match in pattern.finditer(text):
            target = match.group(1).strip()
            if target.startswith("<") and target.endswith(">"):
                target = target[1:-1]
            if not is_external(target):
                targets.append(target.split("#", 1)[0])
    return targets


def markdown_files(root: Path, mode: str) -> list[Path]:
    if mode == "source-repo":
        candidates = [
            root / "README.md",
            root / "documents",
            root / "kit" / "docs",
            root / "kit" / "memories",
            root / "kit" / "AGENTS.md",
            root / "kit" / "HARNESS_CARD.md",
        ]
    else:
        candidates = [
            root / "AGENTS.md",
            root / "HARNESS_CARD.md",
            root / "docs",
            root / "memories",
        ]

    files: list[Path] = []
    for candidate in candidates:
        if candidate.is_file():
            files.append(candidate)
        elif candidate.is_dir():
            files.extend(sorted(candidate.rglob("*.md")))
    return files


def validate_links(files: list[Path], repo_root: Path) -> list[str]:
    errors: list[str] = []
    for path in files:
        text = path.read_text(encoding="utf-8")
        for target in link_targets(text):
            resolved = (path.parent / target).resolve()
            try:
                resolved.relative_to(repo_root.resolve())
            except ValueError:
                errors.append(f"{path}: link escapes repo root -> {target}")
                continue
            if not resolved.exists():
                errors.append(f"{path}: missing link target -> {target}")
    return errors


def validate_router(root: Path) -> list[str]:
    agents = root / "AGENTS.md"
    if not agents.exists():
        return [f"{agents}: missing router"]
    line_count = len(agents.read_text(encoding="utf-8").splitlines())
    if line_count > 50:
        return [f"{agents}: router too long ({line_count} lines, limit 50)"]
    return []


def validate_source_specific(root: Path) -> list[str]:
    errors: list[str] = []
    manifest = root / "kit" / "manifest.json"
    if not manifest.exists():
        errors.append(f"{manifest}: missing manifest")
    root_workflow = root / ".github" / "workflows" / "harness-check.yml"
    kit_workflow = root / "kit" / ".github" / "workflows" / "harness-check.yml"
    if root_workflow.exists() and kit_workflow.exists():
        if root_workflow.read_text(encoding="utf-8") != kit_workflow.read_text(
            encoding="utf-8"
        ):
            errors.append(
                f"{kit_workflow}: shipped workflow drifted from source workflow"
            )
    return errors


def validate_installed_specific(root: Path) -> list[str]:
    required = [
        root / "AGENTS.md",
        root / "HARNESS_CARD.md",
        root / "docs" / "README.md",
        root / "docs" / "ADOPTION_GUIDE.md",
        root / "docs" / "INSTALL.md",
        root / "docs" / "code-design.md",
        root / "scripts" / "install.sh",
        root / "scripts" / "doctor.sh",
        root / "scripts" / "check-surface-truth.py",
    ]
    return [f"{path}: missing required installed file" for path in required if not path.exists()]


def main() -> int:
    args = parse_args()
    root = Path(args.root).resolve()
    files = markdown_files(root, args.mode)

    errors = validate_links(files, root)
    errors.extend(validate_router(root / "kit" if args.mode == "source-repo" else root))

    if args.mode == "source-repo":
        errors.extend(validate_source_specific(root))
    else:
        errors.extend(validate_installed_specific(root))

    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1

    print(f"Surface truth check passed for {args.mode}: {root}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
