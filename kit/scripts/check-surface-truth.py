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
    if line_count > 250:
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
    errors.extend(validate_lifecycle_contract(root, mode="source-repo"))
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
        root / "scripts" / "parse-observability.py",
        root / "scripts" / "generate-dashboard.py",
    ]
    errors = [
        f"{path}: missing required installed file" for path in required if not path.exists()
    ]
    errors.extend(validate_lifecycle_contract(root, mode="installed"))
    return errors


def ordered_contains(text: str, snippets: list[str]) -> bool:
    position = -1
    for snippet in snippets:
        position = text.find(snippet, position + 1)
        if position == -1:
            return False
    return True


def validate_lifecycle_contract(root: Path, mode: str) -> list[str]:
    if mode == "source-repo":
        base = root / "kit"
        docs = {
            "install": base / "docs" / "INSTALL.md",
            "adoption": base / "docs" / "ADOPTION_GUIDE.md",
            "readme": base / "docs" / "README.md",
            "starter": base / "skills" / "starter-init" / "SKILL.md",
            "session": base / "skills" / "context-session" / "SKILL.md",
            "session_flow": base
            / "skills"
            / "context-session"
            / "references"
            / "session-start-flow.md",
            "requirements": base / "skills" / "spec-requirements" / "SKILL.md",
            "research": base / "skills" / "spec-research" / "SKILL.md",
        }
    else:
        docs = {
            "install": root / "docs" / "INSTALL.md",
            "adoption": root / "docs" / "ADOPTION_GUIDE.md",
            "readme": root / "docs" / "README.md",
            "starter": root / "skills" / "starter-init" / "SKILL.md",
            "session": root / "skills" / "context-session" / "SKILL.md",
            "session_flow": root
            / "skills"
            / "context-session"
            / "references"
            / "session-start-flow.md",
            "requirements": root / "skills" / "spec-requirements" / "SKILL.md",
            "research": root / "skills" / "spec-research" / "SKILL.md",
        }

    errors: list[str] = []
    missing = [str(path) for path in docs.values() if not path.exists()]
    if missing:
        return [f"{path}: missing lifecycle contract surface" for path in missing]

    install_text = docs["install"].read_text(encoding="utf-8")
    adoption_text = docs["adoption"].read_text(encoding="utf-8")
    readme_text = docs["readme"].read_text(encoding="utf-8")
    starter_text = docs["starter"].read_text(encoding="utf-8")
    session_text = docs["session"].read_text(encoding="utf-8")
    session_flow_text = docs["session_flow"].read_text(encoding="utf-8")
    requirements_text = docs["requirements"].read_text(encoding="utf-8")
    research_text = docs["research"].read_text(encoding="utf-8")

    if "Run `/context-session`" in install_text or "Open work with /context-session" in install_text:
        errors.append(f"{docs['install']}: advertises /context-session before first-feature creation")
    if not ordered_contains(
        adoption_text,
        ["Run `/starter-init`", "/spec-requirements", "/spec-plan", "/spec-implement", "/harness-verify"],
    ):
        errors.append(f"{docs['adoption']}: greenfield flow is missing the spec-first delivery order")
    if "Run `/context-session`" in adoption_text.split("## Brownfield Adoption", 1)[0]:
        errors.append(f"{docs['adoption']}: greenfield flow still routes directly to /context-session")
    if "/context-session` only after the feature slug already exists" not in readme_text:
        errors.append(f"{docs['readme']}: does not state that /context-session requires an existing feature slug")
    if "Creates progress logs" in starter_text:
        errors.append(f"{docs['starter']}: starter-init still claims ownership of progress logs")
    if "instruct user to run `/context-session`" in starter_text:
        errors.append(f"{docs['starter']}: starter-init still hands off the first feature to /context-session")
    if "status.md does not exist yet" not in session_text:
        errors.append(f"{docs['session']}: context-session is missing the explicit no-status stop condition")
    if "/spec-requirements" not in session_flow_text or "/spec-research" not in session_flow_text:
        errors.append(f"{docs['session_flow']}: missing explicit reroute guidance for first-feature bootstrap")
    if "Create `status.md` if missing" not in requirements_text:
        errors.append(f"{docs['requirements']}: requirements no longer owns first status.md creation")
    if "Create `status.md` if missing" not in research_text:
        errors.append(f"{docs['research']}: research no longer owns first status.md creation")
    return errors


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
