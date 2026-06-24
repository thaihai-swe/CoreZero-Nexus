#!/usr/bin/env python3
import argparse
import os
import re
import sys
from pathlib import Path

_SCRIPT_DIR = Path(__file__).resolve().parent
_PARENT = str(_SCRIPT_DIR.parent)
if _PARENT not in sys.path:
    sys.path.insert(0, _PARENT)

from core._lib.token_counter import estimate_tokens, process_text
from core._lib.yaml_reader import load as load_yaml


def resolve_root(root_flag):
    if root_flag:
        p = Path(root_flag).resolve()
        if (p / "AGENTS.md").exists() and (p / "memories/repo").exists():
            return p
        if (p / "kit/AGENTS.md").exists():
            return p / "kit"
    for d in [Path.cwd()] + list(Path.cwd().parents):
        if (d / "AGENTS.md").exists() and (d / "memories/repo").exists():
            return d
        if (d / "kit/AGENTS.md").exists():
            return d / "kit"
    sys.exit("ERROR: Could not resolve repository root")


class Scorer:
    def __init__(self, intent_keywords):
        keywords = []
        for kw in intent_keywords:
            keywords.extend(kw.lower().replace(",", " ").split())
        self.keywords = [k for k in keywords if k]

    def score(self, filepath):
        if not self.keywords:
            return 50
        try:
            text = Path(filepath).read_text(encoding="utf-8").lower()
        except Exception:
            return 0
        score = 0
        for kw in self.keywords:
            count = text.count(kw)
            if count > 0:
                score += min(count * 10, 30)
        return min(score, 100)


class BudgetTracker:
    def __init__(self, warn=160000, hard=200000):
        self.warn = warn
        self.hard = hard
        self.total = 0
        self.loaded = []

    def check(self, filepath, tokens):
        new_total = self.total + tokens
        if new_total > self.hard:
            return False, f"BUDGET_HARD: Adding '{filepath}' ({tokens} tokens) would exceed hard cap {self.hard}"
        if new_total > self.warn:
            print(f"WARNING: Token budget at {new_total} (warn threshold: {self.warn})", file=sys.stderr)
        return True, None

    def add(self, filepath, tokens, score):
        self.loaded.append({"filepath": filepath, "tokens": tokens, "score": score})
        self.total += tokens

    def evict_to_budget(self):
        if self.total <= self.hard:
            return []
        evicted = []
        self.loaded.sort(key=lambda x: x["score"])
        while self.total > self.hard and self.loaded:
            item = self.loaded.pop(0)
            self.total -= item["tokens"]
            evicted.append(item["filepath"])
            print(f"EVICTED: {item['filepath']} (score={item['score']}, tokens={item['tokens']})", file=sys.stderr)
        return evicted


class Compressor:
    def __init__(self):
        self.id_pattern = re.compile(r"\b[A-Z]{2,6}-\d+\b")

    def compress(self, filepath):
        try:
            text = Path(filepath).read_text(encoding="utf-8")
        except Exception:
            return None, 0
        original_tokens = estimate_tokens(text)
        lines = text.split("\n")
        result = []
        seen_ids = set()
        for line in lines:
            stripped = line.strip()
            if not stripped:
                result.append(line)
                continue
            ids = self.id_pattern.findall(stripped)
            if ids:
                if any(i in seen_ids for i in ids):
                    continue
                seen_ids.update(ids)
            if stripped.startswith("## ") and "Changelog" in stripped:
                result.append(line)
                continue
            if stripped.startswith("- ") and len(stripped) < 80 and ":" not in stripped:
                result.append(line)
                continue
            if len(stripped) > 200:
                line = line[:200] + "..."
            result.append(line)
        compressed = "\n".join(result)
        compressed_tokens = estimate_tokens(compressed)
        if original_tokens > 0 and (original_tokens - compressed_tokens) / original_tokens < 0.1:
            return text, original_tokens
        return compressed, compressed_tokens


class ContextEngine:
    def __init__(self, root, intent="", budget=0, mode="full"):
        self.root = Path(root) if root else Path.cwd()
        self.intent = intent
        self.budget = budget
        self.mode = mode
        self.scorer = Scorer(intent.split(",") if intent else [])
        self.budget_tracker = BudgetTracker()
        self.compressor = Compressor()

    def process_file(self, filepath):
        fp = Path(filepath)
        if not fp.exists():
            print(f"ERROR: File not found: {fp}", file=sys.stderr)
            return
        score = self.scorer.score(str(fp))
        tokens = estimate_tokens(fp.read_text(encoding="utf-8"))
        ok, msg = self.budget_tracker.check(str(fp), tokens)
        if not ok:
            print(msg, file=sys.stderr)
            return
        self.budget_tracker.add(str(fp), tokens, score)
        if self.mode == "scored":
            print(f"[score={score}] {fp}")
            return
        if self.mode == "summary":
            text = fp.read_text(encoding="utf-8")
            result, _ = process_text(text, tokens, mode="summary")
            print(result)
        elif self.mode == "partial":
            text = fp.read_text(encoding="utf-8")
            result, _ = process_text(text, tokens, mode="partial")
            print(result)
        elif self.mode == "compress":
            result, _ = self.compressor.compress(str(fp))
            print(result)
        else:
            print(fp.read_text(encoding="utf-8"), end="")

    def run(self, files):
        for fp in files:
            self.process_file(fp)
        if self.budget > 0:
            self.budget_tracker.hard = self.budget
            evicted = self.budget_tracker.evict_to_budget()
            if evicted:
                print(f"Evicted {len(evicted)} files to meet budget", file=sys.stderr)


def main():
    parser = argparse.ArgumentParser(description="CoreZero Context Engine")
    parser.add_argument("--root", default="", help="Repository root")
    parser.add_argument("--intent", default="", help="Intent keywords for relevance scoring")
    parser.add_argument("--budget", type=int, default=0, help="Hard token budget")
    parser.add_argument("--mode", choices=["full", "summary", "partial", "scored", "compress"],
                        default="full", help="Load mode")
    parser.add_argument("files", nargs="+", help="Files to process")
    args = parser.parse_args()

    engine = ContextEngine(args.root, args.intent, args.budget, args.mode)
    engine.run(args.files)


if __name__ == "__main__":
    main()
