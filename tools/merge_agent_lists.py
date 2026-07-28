#!/usr/bin/env python3
"""
merge_agent_lists.py — build a canonical, deduplicated, classified link corpus
from curated agentic-AI "awesome" lists.

Why a script and not a hand-written list: the seven seed repos hold roughly
2,000-3,000 links. Dedup is an identity problem (same arXiv paper appears as
/abs/, /pdf/, a DOI, and a project page), and that is mechanical. Curation is
the part that needs judgement, so this script gets you to a clean, provenance-
tagged corpus and leaves the summaries to a separate pass.

Usage:
    pip install requests
    python merge_agent_lists.py --out ./corpus
    python merge_agent_lists.py --out ./corpus --format jsonl

Outputs (in --out):
    corpus.jsonl          one record per canonical entity
    by-category/*.md      per-category markdown, ready for review
    report.md             dedup + overlap statistics
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass, field, asdict
from pathlib import Path
from urllib.parse import urlsplit, urlunsplit

try:
    import requests
except ImportError:
    sys.exit("pip install requests")


# --------------------------------------------------------------------------
# Sources. `tier` and `era` are editorial judgements about how much weight to
# give each source, not facts from the repos. Adjust them to taste.
# --------------------------------------------------------------------------

SOURCES = [
    dict(
        key="harness",
        repo="ai-boost/awesome-harness-engineering",
        branch="main",
        path="README.md",
        kind="mixed",          # vendor eng blogs + 2026 arXiv + tools
        era="2026",
        tier=1,
    ),
    dict(
        key="voltagent",
        repo="VoltAgent/awesome-ai-agent-papers",
        branch="main",
        path="README.md",
        kind="papers",
        era="2024-2026",
        tier=1,
    ),
    dict(
        key="luojunyu",
        repo="luo-junyu/awesome-agent-papers",
        branch="main",
        path="README.md",
        kind="papers",
        era="2024-2026",
        tier=1,
    ),
    dict(
        key="kyrolabs",
        repo="kyrolabs/awesome-agents",
        branch="main",
        path="README.md",
        kind="tools",
        era="2023-2026",
        tier=2,
    ),
    dict(
        key="zjunlp",
        repo="zjunlp/LLMAgentPapers",
        branch="main",
        path="README.md",
        kind="papers",
        era="2023-2024",
        tier=2,
    ),
    dict(
        key="berkeley",
        repo="arvindcr4/awesome-agents",
        branch="main",
        path="README.md",
        kind="course",         # Berkeley LLM-Agents MOOC reading list
        era="2024-2025",
        tier=2,
    ),
    dict(
        key="xi-survey",
        repo="WooooDyy/LLM-Agent-Paper-List",
        branch="main",
        path="README.md",
        kind="papers",
        era="2022-2024",       # companion to the 2023 SCIS survey; largely frozen
        tier=3,
    ),
]

RAW = "https://raw.githubusercontent.com/{repo}/{branch}/{path}"


# --------------------------------------------------------------------------
# Canonical identity
# --------------------------------------------------------------------------

ARXIV_PATTERNS = [
    re.compile(r"arxiv\.org/(?:abs|pdf)/(\d{4}\.\d{4,5})", re.I),
    re.compile(r"doi\.org/10\.48550/arxiv\.(\d{4}\.\d{4,5})", re.I),
    re.compile(r"arxiv\.org/html/(\d{4}\.\d{4,5})", re.I),
]
GITHUB_REPO = re.compile(r"github\.com/([A-Za-z0-9._-]+)/([A-Za-z0-9._-]+)", re.I)
ACL = re.compile(r"aclanthology\.org/([A-Za-z0-9.-]+?)/?$", re.I)
OPENREVIEW = re.compile(r"openreview\.net/(?:forum|pdf)\?id=([A-Za-z0-9_-]+)", re.I)

# Not content: badges, chrome, anchors, images.
SKIP_HOSTS = {
    "camo.githubusercontent.com",
    "img.shields.io",
    "shields.io",
    "star-history.com",
    "api.star-history.com",
    "awesome.re",
    "opengraph.githubassets.com",
    "creativecommons.org",
    "mirrors.creativecommons.org",
}
SKIP_URL_SUBSTRINGS = (
    "/stargazers", "/network/members", "/commits/", "/issues", "/pulls",
    "/graphs/contributors", "/blob/main/LICENSE", "/blob/main/CONTRIBUTING",
    "docs.github.com/site-policy", "github.com/login", "github.com/signup",
    "github.com/features", "github.com/solutions", "github.com/resources",
    "github.com/enterprise", "github.com/pricing", "github.com/security/advanced",
    "github.com/topics/", "github.com/trending", "github.com/collections",
    "githubstatus.com", "zdoc.app",
)
IMAGE_EXT = (".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp")

# Paper lists commonly write one item as:
#   - **Title.** *Authors.* [[paper](url)] [[code](url)] [[project page](url)]
# Those trailing links are satellites of the item, not separate entries. Left
# untreated they inflate the corpus and get misclassified, because their anchor
# text carries no topical signal.
SATELLITE_TEXT = {
    "paper", "papers", "pdf", "code", "codes", "project page", "project",
    "page", "dataset", "datasets", "data", "demo", "model", "models",
    "benchmark", "blog", "website", "site", "docs", "doc", "video",
    "slides", "poster", "homepage", "link", "arxiv", "github", "hf",
    "huggingface", "leaderboard", "codes and platform", "data viewer",
    "platform and implementations", "tutorial", "here",
}


def is_satellite(text: str) -> bool:
    return text.strip().strip(".:").lower() in SATELLITE_TEXT


def canonical_id(url: str) -> tuple[str, str]:
    """Return (id, id_type). Same paper via /abs/, /pdf/ or DOI collapses to one id."""
    u = url.strip()
    for pat in ARXIV_PATTERNS:
        m = pat.search(u)
        if m:
            return f"arxiv:{m.group(1)}", "arxiv"
    m = OPENREVIEW.search(u)
    if m:
        return f"openreview:{m.group(1)}", "openreview"
    m = GITHUB_REPO.search(u)
    if m:
        owner, repo = m.group(1), m.group(2)
        repo = re.sub(r"\.git$", "", repo)
        # A deep link into a repo still identifies that repo.
        return f"gh:{owner.lower()}/{repo.lower()}", "github"
    m = ACL.search(u)
    if m:
        return f"acl:{m.group(1)}", "acl"
    return f"url:{normalize_url(u)}", "web"


def normalize_url(url: str) -> str:
    s = urlsplit(url.strip())
    host = s.netloc.lower().removeprefix("www.")
    path = s.path.rstrip("/") or "/"
    # drop tracking / session query params entirely for identity purposes
    return urlunsplit(("https", host, path, "", ""))


def is_content_link(url: str, text: str) -> bool:
    if not url.startswith("http"):
        return False
    host = urlsplit(url).netloc.lower()
    if host in SKIP_HOSTS:
        return False
    if any(s in url for s in SKIP_URL_SUBSTRINGS):
        return False
    if url.lower().endswith(IMAGE_EXT):
        return False
    if not text.strip():
        return False
    return True


# --------------------------------------------------------------------------
# Taxonomy. Ordered — first rule that matches wins, so put the specific
# categories above the general ones.
# --------------------------------------------------------------------------

TAXONOMY: list[tuple[str, list[str]]] = [
    ("harness-engineering", [
        r"\bharness\b", r"agent loop", r"scaffold", r"agent.?computer interface",
    ]),
    ("context-engineering", [
        r"context engineering", r"compact", r"context window", r"prompt compress",
        r"context rot", r"\bcontext manage", r"token reduc", r"prompt cach",
        r"context prun", r"\bclaude\.md\b", r"agents\.md",
    ]),
    ("memory", [
        r"\bmemory\b", r"\bmemgpt\b", r"\bletta\b", r"\bmem0\b", r"\bzep\b",
        r"long.?term memor", r"episodic", r"knowledge graph", r"\brecall\b",
    ]),
    ("tool-use-and-protocols", [
        r"tool use", r"tool.?using", r"function call", r"\btool design\b",
        r"\bmcp\b", r"model context protocol", r"\ba2a\b", r"agent.?to.?agent",
        r"toolformer", r"toolllm", r"\bapi\b.*agent", r"\bskills?\b",
        r"structured output", r"\btool learning\b",
    ]),
    ("planning-and-reasoning", [
        r"\bplan(?:ning|ner)?\b", r"reason", r"chain.?of.?thought", r"\bcot\b",
        r"tree of thought", r"\breact\b", r"task decompos", r"\bmcts\b",
        r"tree search", r"self.?refine", r"self.?correct", r"reflexion",
        r"long.?horizon", r"\bself.?consistency\b",
    ]),
    ("multi-agent", [
        r"multi.?agent", r"\bswarm\b", r"orchestrat", r"\bdebate\b",
        r"\bcollaborat", r"\bcooperat", r"role.?play", r"\bcrew\b", r"\bsubagent",
        r"\bautogen\b", r"\bcamel\b", r"agent society", r"\bhandoff",
    ]),
    ("evaluation-and-benchmarks", [
        r"\beval", r"benchmark", r"\bbench\b", r"swe.?bench", r"webarena",
        r"\bagentbench\b", r"\bosworld\b", r"\bgaia\b", r"llm.?as.?a?.?judge",
        r"\btau.?bench", r"\bverif", r"\bci gate", r"\btest",
    ]),
    ("safety-security-governance", [
        r"\bsafety\b", r"\bsecurity\b", r"prompt injection", r"\bjailbreak\b",
        r"\bguardrail", r"\bsandbox", r"permission", r"\bauthoriz", r"\bauthent",
        r"\bowasp\b", r"red.?team", r"\bgovernan", r"\bpolicy\b", r"least privilege",
        r"\battack\b", r"\bpoison", r"\baudit\b", r"\balign",
    ]),
    ("observability-and-ops", [
        r"observab", r"\btracing\b", r"\btelemetry\b", r"\bmonitor",
        r"\bdebug", r"\bcost\b", r"\blatency\b", r"\bphoenix\b", r"\bopentelemetry\b",
        r"\blangsmith\b", r"\bdeploy", r"\bproduction\b", r"\bsre\b", r"\bincident\b",
    ]),
    ("coding-agents", [
        r"\bcoding agent", r"software engineer", r"\bswe.?agent\b", r"code gener",
        r"\baider\b", r"\bcline\b", r"\bopenhands\b", r"\bopendevin\b", r"\bcodex\b",
        r"\bclaude code\b", r"\bcopilot\b", r"pull request", r"\brepo",
        r"\bprogram repair\b", r"\bopencode\b", r"\bplandex\b",
    ]),
    ("web-gui-computer-use", [
        r"\bweb agent", r"\bbrowser", r"\bgui\b", r"computer.?use", r"\bwebshop\b",
        r"mind2web", r"\bplaywright\b", r"\bselenium\b", r"screen", r"\bmobile\b",
        r"\bandroid\b", r"\bios\b", r"\bnavigat",
    ]),
    ("rag-and-retrieval", [
        r"\brag\b", r"retrieval", r"\bvector\b", r"\bembedding", r"\bsearch\b",
        r"\bindex", r"\bgrounding\b", r"\bhipporag\b", r"deep research",
    ]),
    ("training-and-optimization", [
        r"\bfine.?tun", r"\brl\b", r"reinforcement", r"\bdpo\b", r"\bppo\b",
        r"\bdistill", r"agent tuning", r"\btraject", r"\bgepa\b", r"\bdspy\b",
        r"prompt optim", r"self.?evolv", r"\bcurricul",
    ]),
    ("embodied-and-robotics", [
        r"\bembodied\b", r"\brobot", r"\bmanipulat", r"\bminecraft\b",
        r"\bvoyager\b", r"\bsim.?to.?real\b", r"\baffordance", r"\bnavigation\b",
    ]),
    ("frameworks-and-sdks", [
        r"\bframework\b", r"\bsdk\b", r"\blibrary\b", r"\blangchain\b",
        r"\blanggraph\b", r"\bllamaindex\b", r"\bhaystack\b", r"\bsemantic kernel\b",
        r"\bmastra\b", r"\bpydantic\b", r"\bsmolagents\b", r"\bagno\b",
        r"\bstrands\b", r"\bagent development kit\b", r"\badk\b",
    ]),
    ("surveys-and-foundations", [
        r"\bsurvey\b", r"\bposition paper\b", r"\breview\b", r"\btaxonomy\b",
        r"\bfoundation", r"\bwhat is an? ai agent\b", r"\boverview\b",
    ]),
    ("simulation-and-social", [
        r"\bsimulat", r"generative agent", r"\bsocial\b", r"\bpersona",
        r"\bpersonality\b", r"\bsociety\b", r"\bgame\b", r"\bwerewolf\b",
    ]),
    ("domain-applications", [
        r"\bmedic", r"\bhealth", r"\bclinical\b", r"\blegal\b", r"\bfinanc",
        r"\bchemistry\b", r"\bbiolog", r"\bscientific discovery\b",
        r"\btheorem\b", r"\bmath", r"\beducation\b", r"\brecommend",
    ]),
]

FALLBACK = "unsorted"


# Categories broad enough that a more specific match elsewhere should win.
GENERIC = {"surveys-and-foundations", "frameworks-and-sdks", "domain-applications"}

SECTION_WEIGHT = 2.0   # a section header is deliberate curation
TEXT_WEIGHT = 1.0
SPECIFIC_BONUS = 1.5   # non-generic categories outrank generic ones on a tie


def classify(text: str, section_path: str, url: str) -> tuple[str, list[str]]:
    """Return (primary_category, all_matching_categories) by weighted score.

    Section headers are the strongest signal, but not absolute: an item titled
    "Harness Engineering" filed under a "Foundations" heading is a harness
    document first. Scoring both fields and preferring specific categories over
    broad ones handles that, where first-match-wins does not.
    """
    hay_section = section_path.lower()
    hay_text = f"{text} || {url}".lower()

    scores: dict[str, float] = {}
    for idx, (cat, pats) in enumerate(TAXONOMY):
        score = 0.0
        if any(re.search(p, hay_section) for p in pats):
            score += SECTION_WEIGHT
        if any(re.search(p, hay_text) for p in pats):
            score += TEXT_WEIGHT
        if score == 0.0:
            continue
        if cat not in GENERIC:
            score += SPECIFIC_BONUS
        # earlier taxonomy position = more specific; small nudge to break ties
        score += (len(TAXONOMY) - idx) * 0.01
        scores[cat] = score

    if not scores:
        return FALLBACK, []
    ranked = sorted(scores, key=lambda c: -scores[c])
    return ranked[0], ranked


# --------------------------------------------------------------------------
# Parsing
# --------------------------------------------------------------------------

MD_LINK = re.compile(r"\[([^\]\[]*(?:\[[^\]]*\][^\]\[]*)*)\]\((\s*<?)([^)\s]+?)(>?\s*(?:\"[^\"]*\")?)\)")
HEADING = re.compile(r"^(#{1,6})\s+(.*?)\s*#*$")
DATE_PREFIX = re.compile(r"\[(\d{4}[/-]\d{2})\]")
BOLD_RUN = re.compile(r"\*\*(.+?)\*\*", re.S)
IMG_LINK = re.compile(r"!\[")


@dataclass
class Occurrence:
    source: str
    section_path: str
    text: str
    raw_url: str
    related: list[str] = field(default_factory=list)
    date: str = ""


@dataclass
class Entry:
    cid: str
    id_type: str
    url: str
    titles: list[str] = field(default_factory=list)
    occurrences: list[Occurrence] = field(default_factory=list)
    category: str = FALLBACK
    categories: list[str] = field(default_factory=list)

    @property
    def sources(self) -> list[str]:
        return sorted({o.source for o in self.occurrences})

    @property
    def date(self) -> str:
        ds = sorted(d for d in (o.date for o in self.occurrences) if d)
        return ds[0] if ds else ""

    @property
    def related(self) -> list[str]:
        seen: list[str] = []
        for o in self.occurrences:
            for r in o.related:
                if r not in seen and r != self.url:
                    seen.append(r)
        return seen

    @property
    def best_title(self) -> str:
        # longest title text is usually the most descriptive
        return max(self.titles, key=len) if self.titles else self.url


def strip_badges(line: str) -> str:
    """Remove markdown images (badges) so their alt text is not mistaken for a title."""
    out, depth, i = [], 0, 0
    while i < len(line):
        if line.startswith("![", i):
            # skip the image construct including its (…) target
            j = line.find("](", i)
            if j == -1:
                break
            k, depth = j + 2, 1
            while k < len(line) and depth:
                if line[k] == "(":
                    depth += 1
                elif line[k] == ")":
                    depth -= 1
                k += 1
            i = k
            continue
        out.append(line[i])
        i += 1
    return "".join(out)


def clean_text(t: str) -> str:
    t = re.sub(r"\*\*|__|\*|`", "", t)
    t = re.sub(r"\s+", " ", t)
    return t.strip()


def parse_markdown(md: str, source_key: str) -> list[Occurrence]:
    occurrences: list[Occurrence] = []
    stack: list[str] = []
    in_code = False

    for line in md.splitlines():
        if line.lstrip().startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue

        h = HEADING.match(line)
        if h:
            level, title = len(h.group(1)), clean_text(h.group(2))
            stack = stack[: level - 1]
            while len(stack) < level - 1:
                stack.append("")
            stack.append(title)
            continue

        line = strip_badges(line)
        section_path = " > ".join(s for s in stack if s)

        found = [
            (clean_text(m.group(1)), m.group(3).strip("<>"), m.start())
            for m in MD_LINK.finditer(line)
        ]
        found = [(t, u, p) for t, u, p in found if is_content_link(u, t)]
        if not found:
            continue

        # Prose before the first link is the item title in paper-list style:
        #   - [2023/10] **Title.** *Authors.* [[paper](url)] [[code](url)]
        head = line[: found[0][2]]
        date = ""
        dm = DATE_PREFIX.search(head)
        if dm:
            date = dm.group(1).replace("-", "/")
            head = head[dm.end():]
        # The bold run is the title; the italic run after it is the author list.
        bm = BOLD_RUN.search(head)
        prose = clean_text(bm.group(1)) if bm else clean_text(head)
        prose = re.sub(r"^[\s\-*+]*", "", prose).rstrip(".,;:—-[( ")

        primaries = [(t, u) for t, u, _ in found if not is_satellite(t)]
        if primaries:
            title, url = primaries[0]
            related = [u for _, u, _ in found if u != url]
        else:
            # every link is a satellite: pick the paper/pdf one as the anchor
            pref = next(
                (u for t, u, _ in found
                 if t.strip().strip(".:").lower() in {"paper", "pdf", "arxiv"}),
                found[0][1],
            )
            title, url = (prose or found[0][0]), pref
            related = [u for _, u, _ in found if u != pref]

        if prose and len(prose) > len(title):
            title = prose

        occurrences.append(
            Occurrence(source_key, section_path, title, url, related, date)
        )

    return occurrences


# --------------------------------------------------------------------------
# Driver
# --------------------------------------------------------------------------

def fetch(src: dict, timeout: int = 30) -> str | None:
    url = RAW.format(**src)
    try:
        r = requests.get(url, timeout=timeout)
        r.raise_for_status()
        return r.text
    except Exception as exc:                     # noqa: BLE001
        print(f"  !! {src['key']}: {exc}", file=sys.stderr)
        return None


def build(sources: list[dict]) -> dict[str, Entry]:
    entries: dict[str, Entry] = {}
    for src in sources:
        print(f"-> {src['repo']}")
        md = fetch(src)
        if md is None:
            continue
        occs = parse_markdown(md, src["key"])
        print(f"   {len(occs)} candidate links")
        for occ in occs:
            cid, id_type = canonical_id(occ.raw_url)
            e = entries.get(cid)
            if e is None:
                e = Entry(cid=cid, id_type=id_type, url=occ.raw_url)
                entries[cid] = e
            e.occurrences.append(occ)
            if occ.text not in e.titles:
                e.titles.append(occ.text)

    for e in entries.values():
        section_blob = " ; ".join(o.section_path for o in e.occurrences)
        title_blob = " ; ".join(e.titles)
        e.category, e.categories = classify(title_blob, section_blob, e.url)
    return entries


def write_outputs(entries: dict[str, Entry], out: Path, fmt: str) -> None:
    out.mkdir(parents=True, exist_ok=True)
    (out / "by-category").mkdir(exist_ok=True)

    with (out / "corpus.jsonl").open("w", encoding="utf-8") as fh:
        for e in sorted(entries.values(), key=lambda x: (x.category, x.best_title.lower())):
            rec = dict(
                id=e.cid, id_type=e.id_type, url=e.url, title=e.best_title,
                category=e.category, categories=e.categories,
                sources=e.sources, n_sources=len(e.sources), related=e.related,
                date=e.date,
                occurrences=[asdict(o) for o in e.occurrences],
            )
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")

    by_cat: dict[str, list[Entry]] = defaultdict(list)
    for e in entries.values():
        by_cat[e.category].append(e)

    for cat, items in sorted(by_cat.items()):
        # Links cited by more sources first — cross-list agreement is the
        # cheapest available proxy for canonical status.
        items.sort(key=lambda x: (-len(x.sources), x.best_title.lower()))
        lines = [f"# {cat}", "", f"{len(items)} entries.", ""]
        for e in items:
            when = f" · {e.date}" if e.date else ""
            lines.append(f"- [{e.best_title}]({e.url}){when}")
            lines.append(f"  - `{e.cid}` · cited by {len(e.sources)}: {', '.join(e.sources)}")
            if e.related:
                lines.append("  - related: " + " ".join(f"<{r}>" for r in e.related[:4]))
            lines.append("  - summary: TODO")
            lines.append("")
        (out / "by-category" / f"{cat}.md").write_text("\n".join(lines), encoding="utf-8")

    # report
    per_source = defaultdict(int)
    shared = defaultdict(int)
    for e in entries.values():
        for s in e.sources:
            per_source[s] += 1
        shared[len(e.sources)] += 1

    # Title-collision report. Two dissimilar titles under one canonical id means
    # one of the source lists has a wrong link — silently merging would delete a
    # real entry. Found in practice: a paper list pointing FireAct at Voyager's
    # arXiv ID. Report, never auto-merge.
    collisions = []
    for e in entries.values():
        if len(e.titles) < 2:
            continue
        norm = [re.sub(r"[^a-z0-9 ]", "", t.lower()) for t in e.titles]
        base = set(norm[0].split())
        for other in norm[1:]:
            words = set(other.split())
            if not base or not words:
                continue
            jaccard = len(base & words) / len(base | words)
            if jaccard < 0.34:
                collisions.append((e.cid, e.titles, e.sources))
                break

    rep = ["# Dedup report", "", f"Canonical entries: **{len(entries)}**", "",
           "## Entries per source", ""]
    for k, v in sorted(per_source.items(), key=lambda kv: -kv[1]):
        rep.append(f"- `{k}`: {v}")
    if collisions:
        rep += ["", f"## ⚠ Title collisions ({len(collisions)}) — likely wrong links", "",
                "One canonical id, two unrelated titles. Check the source before trusting either.", ""]
        for cid, titles, srcs in collisions:
            rep.append(f"- `{cid}` ({', '.join(srcs)})")
            for t in titles:
                rep.append(f"  - {t}")
    rep += ["", "## Cross-source overlap", "",
            "| cited by N sources | entries |", "| --- | --- |"]
    for n in sorted(shared):
        rep.append(f"| {n} | {shared[n]} |")
    rep += ["", "## Category sizes", "", "| category | entries |", "| --- | --- |"]
    for cat, items in sorted(by_cat.items(), key=lambda kv: -len(kv[1])):
        rep.append(f"| {cat} | {len(items)} |")
    (out / "report.md").write_text("\n".join(rep), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", type=Path, default=Path("./corpus"))
    ap.add_argument("--format", default="jsonl", choices=["jsonl"])
    ap.add_argument("--only", nargs="*", help="restrict to these source keys")
    ap.add_argument("--max-tier", type=int, default=3)
    args = ap.parse_args()

    srcs = [s for s in SOURCES if s["tier"] <= args.max_tier]
    if args.only:
        srcs = [s for s in srcs if s["key"] in args.only]

    entries = build(srcs)
    write_outputs(entries, args.out, args.format)
    print(f"\n{len(entries)} canonical entries -> {args.out}")
    print(f"see {args.out / 'report.md'}")


if __name__ == "__main__":
    main()
