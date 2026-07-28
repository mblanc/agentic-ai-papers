#!/usr/bin/env python3
"""
import_curated.py — convert docs/CORPUS-curated.md into corpus/curated.jsonl.

The curated file holds ~784 hand-written summaries. Those are the one thing the
pipeline cannot reproduce, so they become *seed* rather than something to
regenerate: after this runs, merge_agent_lists.py --seed corpus/curated.jsonl
keeps every existing summary and only fills in what's genuinely new.

Run once at migration, then again whenever the curated file is edited by hand.

    python tools/import_curated.py --in docs/CORPUS-curated.md --out corpus/curated.jsonl
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

PROVENANCE = {"HE", "KY", "XI", "BK", "VA", "ZJ", "LJ"}

# Mirrors merge_agent_lists.canonical_id — keep the two in sync or dedup breaks.
ARXIV = [
    re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.I),
    re.compile(r"doi\.org/10\.48550/arxiv\.(\d{4}\.\d{4,5})", re.I),
    re.compile(r"arxiv\.org/html/(\d{4}\.\d{4,5})", re.I),
]
GITHUB = re.compile(r"github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)", re.I)
OPENREVIEW = re.compile(r"openreview\.net/(?:forum|pdf)\?id=([A-Za-z0-9_-]+)", re.I)
ACL = re.compile(r"aclanthology\.org/([A-Za-z0-9.-]+?)/?$", re.I)

H1 = re.compile(r"^#\s+(\d+)\.\s+(.*?)\s*$")
H2 = re.compile(r"^##\s+(.*?)\s*$")
# - [Title](url) — summary text `HE` `XI` *(optional note)*
ENTRY = re.compile(r"^-\s+\[(?P<title>[^\]]+)\]\((?P<url>https?://[^)\s]+)\)(?P<rest>.*)$")
CODES = re.compile(r"`(" + "|".join(PROVENANCE) + r")`")
# Provenance lives in a trailing run of codes, optionally followed by an italic
# note. Matching codes anywhere breaks summaries that mention a code inline
# (e.g. "`ZJ`'s newest entry"), which silently emptied one entry on first run.
TRAILING = re.compile(
    r"(?P<body>.*?)(?P<codes>(?:\s*`(?:" + "|".join(PROVENANCE) + r")`)+)"
    r"(?P<note>\s*\*\([^)]*\)\*)?\s*$"
)


def canonical_id(url: str) -> tuple[str, str]:
    for pat in ARXIV:
        m = pat.search(url)
        if m:
            return f"arxiv:{m.group(1)}", "arxiv"
    m = OPENREVIEW.search(url)
    if m:
        return f"openreview:{m.group(1)}", "openreview"
    m = GITHUB.search(url)
    if m:
        repo = re.sub(r"\.git$", "", m.group(2))
        return f"gh:{m.group(1).lower()}/{repo.lower()}", "github"
    m = ACL.search(url)
    if m:
        return f"acl:{m.group(1)}", "acl"
    return f"url:{normalize_url(url)}", "web"


TRACKING = re.compile(r"^(utm_\w+|ref|referrer|fbclid|gclid|mc_cid|mc_eid|source|hsLang)$", re.I)


def normalize_url(url: str) -> str:
    """Drop tracking params but KEEP identity-bearing ones.

    Blanket query-stripping is wrong: youtube.com/watch?v=A and ?v=B are
    different videos and collapsed to one canonical id on the first real run.
    """
    s = urlsplit(url.strip())
    host = s.netloc.lower().removeprefix("www.")
    kept = [
        kv for kv in s.query.split("&")
        if kv and not TRACKING.match(kv.split("=", 1)[0])
    ]
    return urlunsplit(("https", host, s.path.rstrip("/") or "/", "&".join(sorted(kept)), ""))


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def parse(md: str) -> tuple[list[dict], list[str]]:
    entries: list[dict] = []
    warnings: list[str] = []
    category = "unsorted"
    subsection = ""

    for n, line in enumerate(md.splitlines(), 1):
        h1 = H1.match(line)
        if h1:
            # "# 3. Memory" -> memory ; keep the canonical slug used by the pipeline
            category = slug(h1.group(2))
            subsection = ""
            continue
        if line.startswith("# "):          # non-numbered heading, e.g. "# Canonical..."
            continue
        h2 = H2.match(line)
        if h2:
            subsection = h2.group(1)
            continue

        m = ENTRY.match(line)
        if not m:
            continue

        title = m.group("title").strip()
        url = m.group("url").strip()
        rest = m.group("rest")

        tm = TRAILING.match(rest)
        if tm:
            sources = CODES.findall(tm.group("codes"))
            body = tm.group("body")
        else:
            sources = []
            body = re.sub(r"\*\([^)]*\)\*\s*$", "", rest)
        if not sources:
            warnings.append(f"line {n}: no provenance — {title[:60]}")
        summary = body.lstrip(" —-–").strip().rstrip("·").strip()

        if not summary:
            warnings.append(f"line {n}: no summary — {title[:60]}")

        cid, id_type = canonical_id(url)
        entries.append(
            dict(
                id=cid,
                id_type=id_type,
                url=url,
                title=title,
                summary=summary or "TODO",
                category=category,
                subsection=subsection,
                sources=sorted(set(sources)),
                origin="curated",
            )
        )
    return entries, warnings


def merge_duplicates(entries: list[dict]) -> tuple[list[dict], list[tuple]]:
    """Same id appearing under two categories is an intentional cross-listing.
    Keep the first, record the others, and flag genuine title collisions."""
    out: dict[str, dict] = {}
    collisions: list[tuple] = []
    for e in entries:
        prev = out.get(e["id"])
        if prev is None:
            e["also_in"] = []
            out[e["id"]] = e
            continue
        a = set(re.sub(r"[^a-z0-9 ]", "", prev["title"].lower()).split())
        b = set(re.sub(r"[^a-z0-9 ]", "", e["title"].lower()).split())
        if a and b and len(a & b) / len(a | b) < 0.34:
            collisions.append((e["id"], prev["title"], e["title"]))
        else:
            if e["category"] != prev["category"]:
                prev["also_in"].append(e["category"])
            prev["sources"] = sorted(set(prev["sources"]) | set(e["sources"]))
    return list(out.values()), collisions


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--in", dest="src", type=Path, default=Path("docs/CORPUS-curated.md"))
    ap.add_argument("--out", dest="dst", type=Path, default=Path("corpus/curated.jsonl"))
    args = ap.parse_args()

    if not args.src.exists():
        print(f"missing {args.src}", file=sys.stderr)
        return 1

    entries, warnings = parse(args.src.read_text(encoding="utf-8"))
    merged, collisions = merge_duplicates(entries)

    args.dst.parent.mkdir(parents=True, exist_ok=True)
    with args.dst.open("w", encoding="utf-8") as fh:
        for e in sorted(merged, key=lambda x: (x["category"], x["title"].lower())):
            fh.write(json.dumps(e, ensure_ascii=False) + "\n")

    cats = Counter(e["category"] for e in merged)
    srcs = Counter(s for e in merged for s in e["sources"])
    with_summary = sum(1 for e in merged if e["summary"] != "TODO")

    print(f"parsed   {len(entries)} entry lines")
    print(f"unique   {len(merged)} canonical ids")
    print(f"summaries {with_summary} ({with_summary / max(len(merged), 1):.0%}) preserved")
    print(f"wrote    {args.dst}")
    print(f"\ncategories ({len(cats)}):")
    for c, k in cats.most_common():
        print(f"  {k:4d}  {c}")
    print(f"\nprovenance: {dict(srcs.most_common())}")
    if collisions:
        print(f"\n⚠ {len(collisions)} title collision(s) — resolve before ingest:")
        for cid, a, b in collisions:
            print(f"  {cid}\n    {a}\n    {b}")
    if warnings:
        print(f"\n{len(warnings)} warning(s):")
        for w in warnings[:15]:
            print(f"  {w}")
        if len(warnings) > 15:
            print(f"  … and {len(warnings) - 15} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
