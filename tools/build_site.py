#!/usr/bin/env python3
"""
build_site.py — sync wiki/ and corpus/by-category/ into site/content/ for Quartz.

wiki/*.md and corpus/*.jsonl are the sources of truth; site/content/ is a
generated mirror, rebuilt from scratch every run. Never hand-edit anything
under site/content/ — edit wiki/*.md or re-run merge_agent_lists.py instead.

The one transform this does: wiki pages cite corpus entries as {{id}}
(e.g. {{arxiv:2210.03629}}), which is this project's own syntax, not
something Quartz or Obsidian understands. This rewrites every {{id}} into a
real markdown link to that entry's source URL, using corpus.jsonl as the
id -> url lookup. [[wiki-links]] need no transform; Quartz resolves those
natively as long as both pages live under content/.

    python tools/build_site.py
"""

from __future__ import annotations

import json
import re
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI_SRC = ROOT / "wiki"
CORPUS_SRC = ROOT / "corpus" / "by-category"
CORPUS_JSONL = ROOT / "corpus" / "corpus.jsonl"
SITE_CONTENT = ROOT / "site" / "content"

CITATION = re.compile(r"\{\{(arxiv:[^}]+|gh:[^}]+|url:[^}]+|acl:[^}]+|openreview:[^}]+)\}\}")


def load_url_map() -> dict[str, str]:
    m: dict[str, str] = {}
    for line in CORPUS_JSONL.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        rec = json.loads(line)
        if rec.get("id") and rec.get("url"):
            m[rec["id"]] = rec["url"]
    return m


def rewrite_citations(text: str, url_map: dict[str, str]) -> str:
    def repl(m: re.Match) -> str:
        cid = m.group(1)
        url = url_map.get(cid)
        if url is None:
            # validate_corpus.py already guarantees every citation in a
            # non-template page resolves, so this should not happen; fail
            # loudly rather than silently emit a dead link.
            print(f"  !! no url for citation {{{{{cid}}}}}", file=sys.stderr)
            return m.group(0)
        return f"[{cid}]({url})"

    return CITATION.sub(repl, text)


def sync_wiki(url_map: dict[str, str]) -> int:
    dest = SITE_CONTENT / "wiki"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    n = 0
    for src in sorted(WIKI_SRC.glob("*.md")):
        if src.name.startswith("_"):
            continue  # templates aren't pages
        text = src.read_text(encoding="utf-8")
        text = rewrite_citations(text, url_map)
        (dest / src.name).write_text(text, encoding="utf-8")
        n += 1
    return n


def sync_corpus() -> int:
    dest = SITE_CONTENT / "corpus"
    if dest.exists():
        shutil.rmtree(dest)
    dest.mkdir(parents=True)
    n = 0
    for src in sorted(CORPUS_SRC.glob("*.md")):
        shutil.copy2(src, dest / src.name)
        n += 1
    index = dest / "index.md"
    index.write_text(
        "---\ntitle: Corpus\n---\n\n"
        "Generated, per-category reference lists of every corpus entry. "
        "This is the raw bibliography the wiki pages cite as evidence — "
        "browse it directly for entries not yet written up in a wiki page.\n",
        encoding="utf-8",
    )
    return n


def write_root_index() -> None:
    index = SITE_CONTENT / "index.md"
    index.write_text(
        "---\ntitle: Agentic AI Wiki\n---\n\n"
        "A wiki of state-of-the-art and best practices in agentic AI.\n\n"
        "- [[wiki/index|Wiki]] — hand-written topic pages, evidence-linked to the corpus\n"
        "- [[corpus/index|Corpus]] — the full categorized reference list\n",
        encoding="utf-8",
    )
    wiki_index = SITE_CONTENT / "wiki" / "index.md"
    if not wiki_index.exists():
        wiki_index.write_text(
            "---\ntitle: Wiki\n---\n\nTopic pages, one per category.\n",
            encoding="utf-8",
        )


def main() -> int:
    if not CORPUS_JSONL.exists():
        print(f"!! {CORPUS_JSONL} not found — run merge_agent_lists.py first", file=sys.stderr)
        return 1
    url_map = load_url_map()
    n_wiki = sync_wiki(url_map)
    n_corpus = sync_corpus()
    write_root_index()
    print(f"synced {n_wiki} wiki pages, {n_corpus} corpus category pages -> site/content/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
