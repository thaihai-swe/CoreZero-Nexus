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
        self.words = []
        self.phrases = []
        if intent_keywords:
            raw = ",".join(intent_keywords)
            for part in raw.split(","):
                token = part.strip().lower()
                if not token:
                    continue
                if " " in token:
                    self.phrases.append(token)
                else:
                    self.words.append(re.escape(token))

    def score(self, filepath, base_score=0):
        if not self.words and not self.phrases:
            return 50 if base_score == 0 else base_score
        try:
            text = Path(filepath).read_text(encoding="utf-8").lower()
        except Exception:
            return base_score
        score = base_score
        for w in self.words:
            count = len(re.findall(r"\b" + w + r"\b", text))
            if count > 0:
                score += min(count * 10, 30)
        for phrase in self.phrases:
            count = text.count(phrase)
            if count > 0:
                score += min(count * 15, 40)
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


TIER_BOOST = {"Must": 40, "Should": 20, "Skip": 0}

PHASE_COLUMNS = {"spec": 1, "plan": 2, "implement": 3, "verify": 4}


def _path_for_source(source):
    source = source.strip().rstrip(")")
    if "(" in source:
        source = source[: source.index("(")].strip()
    if source.startswith("`") and source.endswith("`"):
        source = source[1:-1]
    source = source.strip()
    if source.startswith("docs/") or source.startswith("skills/") or source.startswith("scripts/"):
        return source
    if source.startswith("domain/"):
        return f"memories/{source}"
    if source in ("harness-telemetry.md",):
        return f"memories/repo/{source}"
    if source in ("session-extracts.md", "Prior `session-extracts.md`"):
        return None
    return f"memories/repo/{source}"


def parse_phase_matrix(text):
    """Return list of (source_pattern, spec_tier, plan_tier, implement_tier, verify_tier)."""
    rows = []
    # Find the Phase × Guidance Matrix section
    marker = "## 3. Phase × Guidance Matrix"
    idx = text.find(marker)
    if idx == -1:
        # Fallback: scan for "Phase × Guidance Matrix" anywhere
        idx = text.find("Phase × Guidance Matrix")
    if idx == -1:
        return rows
    # Scan forward from section header
    in_table = False
    for line in text[idx:].split("\n"):
        s = line.strip()
        if not in_table:
            if s.startswith("| `"):
                in_table = True
            else:
                continue
        if s and not s.startswith("|"):
            break
        if not s.startswith("|"):
            continue
        parts = [p.strip() for p in line.split("|")]
        if len(parts) < 6:
            continue
        source = parts[1]
        if source in ("Source", "---"):
            continue
        rows.append((source, parts[2], parts[3], parts[4], parts[5]))
    return rows


def resolve_route(root, phase):
    """Resolve Phase×Guidance Matrix for a given phase.
    Returns list of (resolved_path, tier).
    """
    root = Path(root)
    master = root / "MASTER_INDEX.md"
    if not master.exists():
        return []
    text = master.read_text(encoding="utf-8")
    rows = parse_phase_matrix(text)
    col = PHASE_COLUMNS.get(phase.lower())
    if col is None:
        return []
    results = []
    for source, *tiers in rows:
        tier = tiers[col - 1]
        if tier not in ("Must", "Should"):
            continue
        rel = _path_for_source(source)
        if rel is None:
            continue
        if "*" in rel:
            matches = sorted(root.glob(rel))
            for m in matches:
                results.append((str(m), tier))
        else:
            fp = root / rel
            if fp.exists():
                results.append((str(fp), tier))
    return results


class ContextEngine:
    def __init__(self, root, intent="", budget=0, mode="full"):
        self.root = resolve_root(root)
        self.intent = intent
        self.budget = budget
        self.mode = mode
        self.scorer = Scorer([intent] if intent else [])
        self.budget_tracker = BudgetTracker()
        self.compressor = Compressor()
        self.tier_map = {}

    def set_tier(self, filepath, tier):
        self.tier_map[str(Path(filepath).resolve())] = tier

    def load_tier_map(self, mapping):
        """Accept a dict of path->tier."""
        for path, tier in mapping.items():
            self.set_tier(path, tier)

    def _get_base_score(self, filepath):
        rel = str(Path(filepath).resolve())
        tier = self.tier_map.get(rel)
        return TIER_BOOST.get(tier, 0)

    def process_file(self, filepath):
        fp = Path(filepath)
        if not fp.exists():
            print(f"ERROR: File not found: {fp}", file=sys.stderr)
            return
        base = self._get_base_score(str(fp))
        score = self.scorer.score(str(fp), base_score=base)
        tokens = estimate_tokens(fp.read_text(encoding="utf-8"))
        ok, msg = self.budget_tracker.check(str(fp), tokens)
        if not ok:
            print(msg, file=sys.stderr)
            return
        self.budget_tracker.add(str(fp), tokens, score)
        if self.mode == "scored":
            tier_tag = f" [{self.tier_map.get(str(Path(filepath).resolve()), '?')}]" if self.tier_map else ""
            print(f"[score={score}]{tier_tag} {fp}")
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

    def run_route(self, phase, mode="full"):
        """Load files dictated by Phase×Guidance Matrix for the given phase."""
        if not self.root:
            return
        entries = resolve_route(self.root, phase)
        if not entries:
            print(f"No route entries for phase '{phase}'", file=sys.stderr)
            return
        # Collect unique paths (last tier wins for duplicates)
        unique = {}
        for fp, tier in entries:
            unique[fp] = tier
        for fp, tier in unique.items():
            self.set_tier(fp, tier)
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
    parser.add_argument("--route", default="",
                        help="Phase name to load files from Phase×Guidance Matrix (spec/plan/implement/verify)")
    parser.add_argument("files", nargs="*", help="Files to process")
    args = parser.parse_args()

    engine = ContextEngine(args.root, args.intent, args.budget, args.mode)
    if args.route:
        engine.run_route(args.route, args.mode)
    if args.files:
        engine.run(args.files)


if __name__ == "__main__":
    main()
