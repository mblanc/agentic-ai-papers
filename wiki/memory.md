---
title: Agent Memory
category: memory
status: draft
updated: 2026-08-01
---

## What it is

Memory is what an agent retains *across* sessions or across a context reset —
distinct from [[context-engineering]], which curates what's active within a
single window. A memory system decides what gets written down, how it's
structured, when it's forgotten, and how it's found again later, often long
after the interaction that produced it. The corpus splits roughly into
research proposing new memory architectures, production stores implementing
some version of them, and a fast-growing security literature treating memory
as something an attacker can poison, steal, or manipulate.

## State of the art

There is no consensus architecture. Four structural bets compete on what
makes long-horizon recall reliable, and the corpus's own comparisons suggest
the answer is "it depends on the failure mode you're defending against," not
a single winner.

**Graph-structured memory** routes retrieval through relationships instead of
flat similarity. GAAMA avoids the "mega-hub" problem of entity-centric graphs
by routing through concept nodes instead, reaching 79.1% mean reward on
LoCoMo-10 — a 4.2-point improvement over the strongest tuned-RAG baseline
tested {{arxiv:2603.27910}}. A more formally grounded approach models memory
as a versioned property graph under AGM belief-revision semantics, scoring
93.3% judge accuracy on an implicit-constraint benchmark (LoCoMo-Plus) where
the best published baseline, Gemini 2.5 Pro, hit 45.7% — though the paper
also reports an independent reproduction by the benchmark's own authors
landing in the mid-80s, a gap worth treating as a caution on how sensitive
this class of result is to eval setup {{arxiv:2603.17244}}. MAGMA runs four
orthogonal graphs (semantic, temporal, causal, entity) with policy-guided
traversal rather than committing to one edge type {{arxiv:2601.03236}}, and a
separate survey catalogues extraction, storage, retrieval and temporal
evolution across this whole graph-memory family {{arxiv:2602.05665}}.

**Execution-state memory** argues semantic similarity is the wrong axis for
long-horizon agentic tasks in the first place. MAGE stores a hierarchical
state tree keyed to what the agent *did*, not what it said, isolating flawed
branches from the active path — 55.1% fewer tokens and 7.8–20.4pp higher
success on the MemoryArena benchmark {{arxiv:2606.06090}}. E-mem keeps
uncompressed context in per-assistant stores and reconstructs episodes on
demand instead of compressing destructively {{arxiv:2601.21714}}, and Amory
builds coherent narrative episodes from fragments while semanticizing
peripheral facts offline, a middle path between raw logs and lossy summaries
{{arxiv:2601.06282}}.

**Discrete fact objects make the strongest empirical claim against
in-context memory.** Benchmarked directly, hash-addressed Knowledge Objects
hit 100% accuracy from 10 to 7,000 facts and 78.9% on multi-hop reasoning
(vs. 31.6% for in-context memory), at 252x lower cost — while in-context
memory's compaction destroys about 60% of facts and cascading compaction
erodes 54% of project constraints, a failure the authors show is
architectural, replicating across four frontier models, not a
model-specific quirk {{arxiv:2603.17781}}. RET-LLM made an earlier, simpler
version of this bet — facts as explicit subject-predicate-object triplets in
a read-write store — and reported it handles date-sensitive recall
noticeably better than the model's own parametric memory
{{arxiv:2305.14322}}.

**A direct structural comparison found no single memory shape dominates.**
Across chunks, triples, atomic facts, and summaries, mixed structures were
most resilient to noise, and iterative retrieval consistently beat
single-step or reranked retrieval regardless of which representation backed
it {{arxiv:2412.15266}}. Read this as license to not over-commit to one
memory shape early — the graph/execution-state/fact-object split above is a
menu, not a hierarchy.

**Learned memory management is displacing hand-written heuristics for what
to keep.** Memory-R1 trains two agents with RL to actively manage and use
external memory rather than following fixed write/prune rules
{{arxiv:2508.19828}}; AtomMem decomposes memory into CRUD-style atomic
operations and learns the policy via SFT+RL {{arxiv:2601.08323}}; ProcMEM
learns reusable procedural (step-by-step) memory from experience via
non-parametric PPO, avoiding retraining to acquire a new skill
{{arxiv:2602.01869}}.

**Below the research layer, production memory stores have converged on
similar tiered shapes.** Letta/MemGPT's core/archival/recall tiers
established the reference pattern for treating an agent's context window as
OS-style virtual memory {{gh:letta-ai/letta}}, an idea ClawVM extends by
making the *harness* manage that virtual memory directly — typed pages with
validated writeback at every lifecycle boundary, eliminating post-compaction
state loss at under 50 microseconds overhead per turn
{{arxiv:2604.10352}}. mem0 {{gh:mem0ai/mem0}}, Zep
{{gh:getzep/zep}}, and cognee's self-hosted knowledge-graph layer
{{gh:topoteretes/cognee}} are the common drop-in options. A distinct,
unfashionable-but-notable minority bet is on *not* building a specialized
memory system at all: LangChain's Agent Builder stores memory as plain files
the agent reads and edits, betting current models handle filesystems well
enough to skip dedicated tooling {{url:https://blog.langchain.com/how-we-built-agent-builders-memory-system}},
and claude-memory-compiler distills each Claude Code session into compiled
articles via hooks, again with no vector database in the loop
{{gh:coleam00/claude-memory-compiler}}. GitHub Copilot's cross-agent memory
splits the difference — it stores facts with citations to code locations and
re-verifies them just-in-time at recall, so shared memory doesn't silently
drift as the codebase changes underneath it
{{url:https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot}}.

## Origin

Cognitive Architectures for Language Agents (CoALA) is the field's most-cited
organizing framework, structuring an agent around modular memory, an action
space, and a decision procedure {{arxiv:2309.02427}}. Letta (MemGPT) is the
reference implementation for that idea as a shipped system rather than a
diagram {{gh:letta-ai/letta}}. RET-LLM and ChatDB are the earliest entries in
this corpus proposing memory as explicit structured storage — triplets and a
SQL database respectively — rather than an implicit property of a longer
context window {{arxiv:2305.14322}} {{arxiv:2306.03901}}. The most current
entry point into where the field is heading is a 2026 survey organizing
memory by substrate, cognitive mechanism, and subject
{{arxiv:2602.06052}}.

## Open problems

**Memory is now a named attack surface, not just an engineering
convenience.** Memory poisoning corrupts an agent's long-term store through
query-only interactions; on clinical-record agents the paper finds
pre-existing legitimate memories partly blunt the attack on their own, and
proposes trust-scored moderation plus decay-based sanitization as defenses
{{arxiv:2601.05504}}. RAG knowledge bases can be extracted wholesale:
RAGCrawler schedules non-redundant queries to reach 66.8% average corpus
coverage (up to 84.4%) within 1,000 queries, a 44.9% relative improvement
over the strongest prior baseline {{arxiv:2601.15678}}. The corresponding
defense seeds a GraphRAG knowledge graph with plausible-but-false
"adulterants" that only key-holders can filter, dropping a thief's accuracy
to 5.3% while legitimate queries stay 100% correct
{{arxiv:2601.00274}}. Governance is catching up but still mostly bespoke:
MemArchitect treats decay, conflict resolution, and privacy as explicit
policy rather than passive storage {{arxiv:2603.18330}}, and MemTrust
proposes a hardware zero-trust (TEE) architecture for memory shared across
agents and apps {{arxiv:2601.07004}} — neither is a settled default the way
vector retrieval became for RAG.

**Tool-memory conflict is a measured correctness gap, not just an efficiency
one.** When an agent's parametric knowledge contradicts what a tool just
told it, the conflict is common on STEM tasks, and none of the prompting- or
RAG-based mitigations tested actually resolve it {{arxiv:2601.09760}} — this
sits one level below the memory-architecture question entirely and none of
the architectures above claim to fix it.

**Forgetting is still mostly hand-tuned.** MemoryBank applies an
Ebbinghaus-inspired decay curve to stored conversation memory
{{arxiv:2305.10250}}; FadeMem generalizes this to adaptive exponential decay
with LLM-guided conflict resolution when two memories disagree
{{arxiv:2601.18642}}. Neither is validated against the graph or
execution-state architectures above under the same benchmark, so it's
unclear whether decay is a bolt-on or should be native to the memory
structure itself.

**Benchmarks are shifting from "can it retrieve" to "does it act."**
Mem2ActBench specifically tests whether agents *use* long-term memory
proactively rather than just answering when asked
{{arxiv:2601.19935}}, and RealMem stress-tests over 2,000 cross-session
dialogues with goals that evolve over time rather than staying fixed
{{arxiv:2601.06966}}. Older single-hop QA-style memory evals under-test both
axes.

## See also

- [[context-engineering]]
- [[safety-security-governance]]
- [[multi-agent]]
- {{gh:letta-ai/letta}} — reference stateful-agent memory architecture
- {{gh:mem0ai/mem0}} — lowest-integration drop-in memory layer
