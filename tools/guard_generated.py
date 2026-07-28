#!/usr/bin/env python3
"""
guard_generated.py — PreToolUse hook. Blocks writes to generated files.

`corpus/by-category/*.md` are build artifacts. Editing one is always a mistake:
the change is silently destroyed on the next pipeline run, and in the meantime the
corpus and its views disagree. CLAUDE.md says not to, but CLAUDE.md is context,
not enforcement — a model can reason its way past it. A hook cannot be overridden.

Reads the tool-call payload on stdin, exits 2 to block.
"""

from __future__ import annotations

import json
import re
import sys

BLOCKED = [
    (re.compile(r"corpus/by-category/.*\.md$"), "generated view — edit the pipeline or the source entry, then rebuild"),
    (re.compile(r"corpus/report\.md$"), "generated report — rerun the pipeline"),
    (re.compile(r"corpus/corpus\.jsonl$"), "canonical store — write via the pipeline, not by hand"),
]


def main() -> int:
    try:
        payload = json.load(sys.stdin)
    except Exception:
        return 0  # never block on a malformed payload

    path = (
        payload.get("tool_input", {}).get("file_path")
        or payload.get("tool_input", {}).get("path")
        or ""
    )
    if not path:
        return 0

    for pat, why in BLOCKED:
        if pat.search(path):
            print(f"BLOCKED: {path} is a {why}.", file=sys.stderr)
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
