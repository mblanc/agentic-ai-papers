# Seed corpus: taxonomy, source tiering, and dedup notes

Working notes for the wiki backfill. Read alongside `merge_agent_lists.py`.

---

## 1. The seven sources are not one corpus

I read four of the seven end-to-end. They split into three generations that
should **not** be merged into a single flat list, because they answer different
questions and age at very different rates.

| source | kind | items (approx) | currency | tier |
| --- | --- | --- | --- | --- |
| `ai-boost/awesome-harness-engineering` | vendor eng blogs + 2026 arXiv + tools | 250+ | actively maintained, heavily 2026 | **1** |
| `VoltAgent/awesome-ai-agent-papers` | papers, numbered sections | ~400 (not yet read) | recent | **1** |
| `luo-junyu/awesome-agent-papers` | papers | ~500 (not yet read) | recent | **1** |
| `kyrolabs/awesome-agents` | open-source tools only | ~135 | actively maintained | 2 |
| `zjunlp/LLMAgentPapers` | papers | ~500 (not yet read) | 2023–2024 leaning | 2 |
| `arvindcr4/awesome-agents` | Berkeley MOOC reading list | ~90 | Jan 2026, course-bound | 2 |
| `WooooDyy/LLM-Agent-Paper-List` | papers, survey companion | ~350 | **largely frozen** | 3 |

### Findings worth acting on

**`arvindcr4/awesome-agents` is not a fork of `kyrolabs/awesome-agents`.** The
identical repo name is a coincidence. It is a reading list curated strictly from
UC Berkeley's LLM Agents MOOC (Fall 2024 / Spring 2025 / Fall 2025), 2 stars,
4 commits. Its value is different in kind: it is a *syllabus*, so its ordering
encodes pedagogical dependency, and it is the only source with lecture videos and
a theorem-proving/formal-methods cluster. Keep it, but treat it as curriculum
scaffolding rather than SOTA.

**`WooooDyy/LLM-Agent-Paper-List` is a historical artifact.** It is the companion
to the Sept 2023 SCIS survey. Its newest substantive entries are mid-2024, the
README still advertises "coming soon: add one-sentence intro to each paper," and
its taxonomy (brain / perception / action, agent society, personality) is a 2023
framing. For a SOTA wiki this is **provenance, not state of the art** — excellent
for the canonical-origins pages (ReAct, Reflexion, ToT, Generative Agents,
Voyager, CoT), near-useless for anything about harnesses, MCP, compaction, or
subagents. Tier it down; do not let its 350 papers dominate category counts.

**`ai-boost/awesome-harness-engineering` is the closest match to what you're
building.** It is the only source organized around *engineering problems* rather
than research areas, and its section list is almost exactly your stated wiki
topics: agent loop, planning, context delivery & compaction, tool design,
skills & MCP, permissions & authorization, memory & state, task runners,
verification & CI, observability, debugging, human-in-the-loop. It also mixes
first-party vendor engineering posts with 2026 arXiv, which is the blend a
practitioner wiki needs. Consider making its section structure the spine of the
wiki and treating the paper lists as evidence you attach to those pages.

**Expected overlap is lower than you'd think.** These lists differ by artifact
type (papers vs. tools vs. blogs) and by generation. Real overlap concentrates in
a thin canon — ReAct, Reflexion, ToT, Voyager, Generative Agents, MemGPT,
SWE-agent, AutoGen, MetaGPT, WebArena, SWE-bench, OSWorld, Toolformer, DSPy —
which is exactly the set worth surfacing first. `n_sources >= 3` in the pipeline
output is a usable proxy for "canonical."

---

## 2. Dedup is an identity problem, not a string-matching one

The same paper appears across these lists in at least five shapes:

```
https://arxiv.org/abs/2210.03629
https://arxiv.org/pdf/2210.03629.pdf
https://arxiv.org/pdf/2210.03629v2
https://doi.org/10.48550/arXiv.2210.03629
https://react-lm.github.io/            <- project page, different entity
```

So dedup keys on a **canonical id**, not a URL:

| id form | example | rule |
| --- | --- | --- |
| `arxiv:2210.03629` | ReAct | strip `abs`/`pdf`/`html`, version suffix, `.pdf`; fold the `10.48550` DOI form |
| `gh:owner/repo` | `gh:letta-ai/letta` | lowercase; deep links collapse to the repo |
| `openreview:<id>` | forum/pdf `?id=` | |
| `acl:<id>` | aclanthology | |
| `url:<normalized>` | vendor blogs | https, drop `www.`, drop query, strip trailing `/` |

Three traps the script handles, each of which silently corrupts the corpus if
missed:

1. **Badge links.** Every `[![Stars](shields.io/...)](.../stargazers)` is a
   markdown link. Left in, they roughly double the corpus and add a fake
   `gh:owner/repo` entry pointing at `/stargazers`.
2. **Satellite links.** Paper lists write one item as
   `**Title.** *Authors.* [[paper](…)] [[code](…)] [[dataset](…)]`. Treated
   naively, one paper becomes three entries and the code repo gets classified
   from the anchor text `code`, which carries no topical signal. The script
   groups per list item: one primary entry, the rest as `related`.
3. **GitHub page chrome.** Fetching the rendered HTML page pulls in ~200 nav
   links (`/features`, `/pricing`, `/login`, site-policy…). The script reads
   `raw.githubusercontent.com` instead, and still filters defensively.

---

## 3. Canonical taxonomy

19 categories, ordered specific → general. Order matters: it is used to break
scoring ties, so a match on an earlier category wins.

| # | category | what belongs here |
| --- | --- | --- |
| 1 | `harness-engineering` | the scaffolding itself: agent loop, agent-computer interface, harness definitions |
| 2 | `context-engineering` | compaction, pruning, caching, context assembly, CLAUDE.md/AGENTS.md patterns |
| 3 | `memory` | short/long-term memory, consolidation, episodic stores, memory retrieval |
| 4 | `tool-use-and-protocols` | function calling, tool design, MCP, A2A, skills, structured output |
| 5 | `planning-and-reasoning` | CoT, ToT, ReAct, decomposition, tree search, self-correction, long-horizon |
| 6 | `multi-agent` | orchestration, topology, debate, handoffs, subagents, swarms |
| 7 | `evaluation-and-benchmarks` | evals, benchmarks, LLM-as-judge, verification, CI gates |
| 8 | `safety-security-governance` | prompt injection, sandboxing, permissions, authz, red-teaming, policy |
| 9 | `observability-and-ops` | tracing, telemetry, cost, latency, production/SRE, debugging |
| 10 | `coding-agents` | SWE agents, code generation, repo-level work, CLI/IDE agents |
| 11 | `web-gui-computer-use` | browser, GUI, computer-use, mobile, navigation |
| 12 | `rag-and-retrieval` | retrieval, vector search, grounding, deep research |
| 13 | `training-and-optimization` | fine-tuning, RL, DPO, trajectories, prompt/program optimization (DSPy, GEPA) |
| 14 | `embodied-and-robotics` | embodied agents, manipulation, sim-to-real, Minecraft |
| 15 | `frameworks-and-sdks` | LangChain/LangGraph, LlamaIndex, ADK, Mastra, smolagents… |
| 16 | `surveys-and-foundations` | surveys, position papers, taxonomies, definitional pieces |
| 17 | `simulation-and-social` | generative agents, society simulation, personas, games |
| 18 | `domain-applications` | medical, legal, finance, chemistry, math/theorem proving, education |
| 19 | `unsorted` | fallback — review this file first, it tells you where the rules are thin |

### Classification weighting

Pure first-match-on-section-header is wrong. An item titled *Harness
Engineering* sitting under a heading called *Foundations* is a harness document,
not a survey. So each category is scored:

```
section header match  +2.0     (deliberate curation by the list maintainer)
title/url match       +1.0
non-generic category  +1.5     (specific beats surveys/frameworks/domain)
taxonomy position     +0.01 × (N - index)
```

`surveys-and-foundations`, `frameworks-and-sdks` and `domain-applications` are
marked generic: they are real categories but broad enough that a specific match
anywhere should outrank them.

Every entry keeps its full `categories` list, not just the winner — many items
legitimately belong in three places, and a wiki wants them cross-linked rather
than filed once.

---

## 4. On the "short summary below each link"

Two reasons not to carry the source lists' own descriptions through:

- **They're copyrighted prose.** These READMEs are CC0 in two cases but not all,
  and either way a merged file of several thousand verbatim curator descriptions
  is a redistribution of their editorial work, not a new artifact.
- **They're inconsistent.** `awesome-harness-engineering` writes 60-word
  analytical annotations; `kyrolabs` writes 8-word taglines; `WooooDyy` has none
  for large stretches. Concatenating them gives an unusable mixed voice.

So the pipeline emits `summary: TODO` per entry and captures the *facts* —
canonical id, title, date, provenance, related links, section path the maintainer
filed it under. Generate summaries as a second pass in your own voice, at a
consistent length, from the abstract or repo README. That pass is also where the
Gemini/Vertex batch setup you already have for Pulse pays off: a few thousand
one-line summaries is a cheap batch job, and it keeps the wiki's voice uniform.

---

## 5. Suggested order of work

1. Run the pipeline over tier 1 only (`--max-tier 1`). Smaller corpus, highest
   currency, and it maps directly onto your wiki's topic pages.
2. Review `by-category/unsorted.md` and tighten the rules. Two or three passes
   gets the fallback bucket small.
3. Add tier 2, then tier 3 last — by then your category boundaries are stable, so
   the 350 older papers land as historical context instead of setting the shape.
4. Only then generate summaries. Ordering matters: summarizing before the
   taxonomy settles means re-summarizing.
5. Sort each category by `n_sources` descending. The top of each file is your
   canon and the natural first set of wiki pages to write.

## 6. Gaps these seven sources leave

Worth noting before you treat this as the whole backfill: the seven are
paper-and-tool heavy and thin on
**vendor primary documentation** (Anthropic/OpenAI/Google docs as opposed to
blog posts), **changelogs and release notes** (where the actual SOTA moves
week to week), and **failure/postmortem writeups**. Only
`awesome-harness-engineering` carries much of the third category. Your existing
feed list is likely the better source for those.
