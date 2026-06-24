#!/usr/bin/env python3
import argparse
import os
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
_PARENT = str(_SCRIPT_DIR.parent)
if _PARENT not in sys.path:
    sys.path.insert(0, _PARENT)

from core.context_engine import ContextEngine


def main():
    parser = argparse.ArgumentParser(description="CoreZero Context Loader: Enforces Minimum Viable Context (MVC).")
    parser.add_argument("filepath", help="Path to the markdown file to load")
    parser.add_argument("--mode", choices=["full", "summary", "partial"], default="full",
                        help="Load mode")
    parser.add_argument("--intent", default="", help="Intent keywords for scoring")
    parser.add_argument("--budget", type=int, default=0, help="Token budget")
    args = parser.parse_args()

    if not os.path.exists(args.filepath):
        print(f"Error: File '{args.filepath}' does not exist.", file=sys.stderr)
        sys.exit(1)

    engine = ContextEngine(root="", intent=args.intent, budget=args.budget, mode=args.mode)
    engine.process_file(args.filepath)


if __name__ == "__main__":
    main()
