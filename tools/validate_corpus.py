#!/usr/bin/env python3
"""
validate_corpus.py — deterministic gate on corpus integrity.

Runs the checks that are cheap for a script and unreliable for a model:
schema, provenance, canonical-ID collisions, generated-file drift.

Exit 0 = clean, 1 = violations. Wire as a PostToolUse hook and/or CI step so it
runs whether or not the agent remembers to.

    python tools/validate_corpus.py
    python tools/validate_corpus.py --corpus corpus --wiki wiki
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

PROVENANCE = {"HE", "KY", "XI", "BK", "VA", "ZJ", "LJ"}
ID_PREFIXES = ("arxiv:", "gh:", "openreview:", "acl:", "url:")

# Phrases that indicate a summary was lifted from a source list's register
# rather than written for this corpus.
BANNED = [
    r"\bthis paper proposes\b",
    r"\bintroduces a novel framework\b",
    r"\bcutting-edge\b",
    r"\brevolutionary\b",
    r"\bstate-of-the-art results\b",
]


def fail(msg: str) -> None:
    print(f"  ✗ {msg}")


def check_jsonl(path: Path) -> list[str]:
    errs: list[str] = []
    if not path.exists():
        return [f"missing {path}"]

    by_id: dict[str, list[str]] = defaultdict(list)
    seen_ids: set[str] = set()

    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            rec = json.loads(line)
        except json.JSONDecodeError as exc:
            errs.append(f"{path}:{n} invalid JSON: {exc}")
            continue

        for field in ("id", "url", "title", "category", "sources"):
            if not rec.get(field):
                errs.append(f"{path}:{n} missing required field '{field}'")

        cid = rec.get("id", "")
        if cid and not cid.startswith(ID_PREFIXES):
            errs.append(f"{path}:{n} id '{cid}' has no recognized prefix")
        if cid in seen_ids:
            errs.append(f"{path}:{n} duplicate id '{cid}' — dedup did not run")
        seen_ids.add(cid)

        srcs = rec.get("sources") or []
        unknown = set(srcs) - {s.lower() for s in PROVENANCE} - PROVENANCE
        if unknown:
            errs.append(f"{path}:{n} unknown provenance {sorted(unknown)}")

        title = rec.get("title", "")
        if cid and title:
            by_id[cid].append(title)

        summary = rec.get("summary") or ""
        if summary and summary not in ("TODO", "NEEDS-SOURCE"):
            for pat in BANNED:
                if re.search(pat, summary, re.I):
                    errs.append(
                        f"{path}:{n} summary uses source-list register: /{pat}/"
                    )

    # Title collisions: one canonical id, two unrelated titles => wrong link
    # somewhere upstream. Never silently merge these.
    for cid, titles in by_id.items():
        uniq = list(dict.fromkeys(titles))
        if len(uniq) < 2:
            continue
        base = set(re.sub(r"[^a-z0-9 ]", "", uniq[0].lower()).split())
        for other in uniq[1:]:
            words = set(re.sub(r"[^a-z0-9 ]", "", other.lower()).split())
            if not base or not words:
                continue
            if len(base & words) / len(base | words) < 0.34:
                errs.append(
                    f"TITLE COLLISION on {cid}: {uniq[0]!r} vs {other!r} "
                    "— a source has a wrong link; resolve manually"
                )
                break
    return errs


def check_generated_not_edited(corpus: Path) -> list[str]:
    """by-category/*.md are build artifacts. A stray sentinel means someone edited one."""
    errs = []
    gen = corpus / "by-category"
    if not gen.exists():
        return errs
    for f in gen.glob("*.md"):
        head = f.read_text(encoding="utf-8")[:400]
        if "DO NOT EDIT" not in head.upper() and not head.lstrip().startswith("#"):
            errs.append(f"{f} does not look generated — was it hand-edited?")
    return errs


def check_wiki_links(wiki: Path, corpus: Path) -> list[str]:
    """Wiki pages cite corpus entries by canonical id; every citation must resolve."""
    errs: list[str] = []
    jsonl = corpus / "corpus.jsonl"
    if not wiki.exists() or not jsonl.exists():
        return errs
    known = {
        json.loads(l)["id"]
        for l in jsonl.read_text(encoding="utf-8").splitlines()
        if l.strip()
    }
    for page in wiki.rglob("*.md"):
        for cid in re.findall(r"\{\{(arxiv:[^}]+|gh:[^}]+)\}\}", page.read_text(encoding="utf-8")):
            if cid not in known:
                errs.append(f"{page} cites unknown entry {{{{{cid}}}}}")
    return errs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", type=Path, default=Path("corpus"))
    ap.add_argument("--wiki", type=Path, default=Path("wiki"))
    args = ap.parse_args()

    groups = {
        "corpus schema + dedup + collisions": check_jsonl(args.corpus / "corpus.jsonl"),
        "generated files untouched": check_generated_not_edited(args.corpus),
        "wiki citations resolve": check_wiki_links(args.wiki, args.corpus),
    }

    total = 0
    for name, errs in groups.items():
        if errs:
            print(f"[FAIL] {name}")
            for e in errs[:25]:
                fail(e)
            if len(errs) > 25:
                print(f"  … and {len(errs) - 25} more")
            total += len(errs)
        else:
            print(f"[ok]   {name}")

    print()
    if total:
        print(f"{total} violation(s).")
        return 1
    print("clean.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
