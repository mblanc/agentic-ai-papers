---
title: RAG and Retrieval
category: rag-and-retrieval
status: draft
updated: 2026-08-01
---

## What it is

Retrieval-Augmented Generation couples an LLM with an external knowledge
source at inference time — vector search, a knowledge graph, or live web
search — to ground a response instead of relying only on parametric memory.
This page covers retrieval as a system component: how to decide *whether* to
retrieve, *what* structure to retrieve over, and how to keep that retrieval
safe and efficient. Agent-side use of retrieved memory over time is
[[memory]]; token-budget tradeoffs once evidence is in the prompt are
[[context-engineering]].

## State of the art

**Retrieval is becoming a decision, not a default.** L-RAG skips retrieval
entirely when model uncertainty is already low, using an entropy-based lazy
trigger {{arxiv:2601.06551}}, and ACE has an orchestrator agent choose
per-step whether to retrieve new evidence or reason over what it already has,
cutting unnecessary retrieval while improving multi-hop QA accuracy
{{arxiv:2601.08747}}. Query complexity gets the same treatment on the other
side of the loop: an RL policy decides when to split a complex query into
sub-queries and fuse the results rather than always decomposing
{{arxiv:2601.21208}}. This isn't unconditionally good — a diagnostic study
asking specifically *when* iterative retrieval beats gold-standard evidence in
scientific multi-hop QA finds the advantage is situational, not universal
{{arxiv:2601.19827}}, so "retrieve less, retrieve smarter" is a real trend but
not yet a settled recipe.

**Process supervision is replacing outcome-only supervision for multi-hop
retrieval.** ProRAG uses MCTS step-level rewards to localize exactly where a
multi-hop reasoning chain goes wrong, rather than scoring only the final
answer {{arxiv:2601.21912}}, and JADE frames strategic planning and
operational execution as a jointly-optimized cooperative team instead of a
planner handing fixed instructions to a retriever {{arxiv:2601.21916}}.

**Graph-structured retrieval is a distinct, active thread**, motivated by
plain top-k vector search losing relational structure. Deep GraphRAG balances
global and local hierarchical retrieval with beam-search reranking
{{arxiv:2601.11144}}; CIRAG preserves multiple evidence chains across a
multi-hop query instead of collapsing to one path per hop, expanding
granularity from triples up to full passages {{arxiv:2601.06799}}; Relink
builds a query-specific evidence graph on the fly rather than trusting a
static pre-built one, filling gaps with latent relations mined from the
source corpus, and reports a 5.4-point EM and 5.2-point F1 gain over leading
GraphRAG baselines across five open-domain QA benchmarks
{{arxiv:2601.07192}}; FastInsight fuses graph reranking with
semantic-topological expansion {{arxiv:2601.18579}}; and Topo-RAG routes
narrative text and tabular content through separate retrievers rather than
one shared pipeline, for hybrid text-table documents {{arxiv:2601.10215}}.

**Reranking and evidence handling are splitting semantic match from factual
correctness.** DeepEra separates semantic similarity from logical relevance in
its reranker, on the premise that the most similar-sounding passage isn't
always the most useful one {{arxiv:2601.16478}}, and a related line makes
conflict between retrieved sources an explicit, observable step rather than
silently averaging over it {{arxiv:2601.06842}}.

**Privacy and access control are now first-class RAG concerns.** A
systematization of RAG privacy risk — extraction attacks, embedding leakage —
finds current mitigations still immature relative to the threat surface
{{arxiv:2601.03979}}. SD-RAG enforces disclosure controls during retrieval
itself, before sensitive passages ever reach the generator, which keeps it
resilient even to prompt injection targeting the model, and reports up to a
58-point gain on privacy score over baselines {{arxiv:2601.11199}}; a
distance-preserving encryption scheme lets an untrusted cloud host the vector
store while still computing similarity ranking, without reconstructing text
or queries, at a fraction of homomorphic encryption's cost
{{arxiv:2601.12331}}.

**Self-evolving deep-research agents are converging on constrained, not
free-form, self-modification.** EvoFSM makes a self-evolving deep-research
agent controllable by evolving an explicit finite state machine — separating
flow logic from per-state skills — instead of letting the agent rewrite
itself freely, curbing the instability that unconstrained optimization
produces, and reports 58% on DeepSearch {{arxiv:2601.09465}}. DIVERGE applies
reflection and memory refinement specifically to keep answers diverse on
open-ended information-seeking tasks, where a single best-guess answer is the
wrong target {{arxiv:2602.00238}}.

**Tool-form deep-research agents already ship as products, not just papers.**
GPT Researcher plans sub-questions, cross-checks sources in parallel, and
writes a cited report, with MCP support for custom data connectors
{{gh:assafelovic/gpt-researcher}}, and Stanford's STORM builds a full,
cited Wikipedia-style article by simulating multi-perspective interview
conversations before writing a single word, rather than a single
retrieve-then-generate pass {{arxiv:2402.14207}} {{gh:stanford-oval/storm}}.
OpenScholar performs retrieval-augmented synthesis specifically over
scientific literature {{arxiv:2411.14199}}, and Atom-Searcher supervises deep
research at a finer grain, rewarding individual atomic units of thought
rather than the final report alone {{arxiv:2508.12800}}.

## Origin

WebCPM recorded 125,954 real human web-search actions to train models on
*interactive* retrieval — issuing queries, reading results, deciding to search
again — rather than static single-pass corpus lookup; the resulting model's
answers matched or beat human-written ones in 32.5% of cases on its own
dataset {{acl:2023.acl-long.499}}. This is the earliest instance in the
corpus of retrieval framed as an agentic loop rather than a preprocessing
step, and it's the direct ancestor of today's routing/reflecting/iterating
systems.

## Open problems

Privacy mitigations for RAG are behind the attack surface by the SoK's own
assessment — inventoried, not solved {{arxiv:2601.03979}}. There's no settled
guidance yet on *when* agentic retrieval (routing, iteration, reflection) is
worth its added latency and cost over plain single-shot retrieval, since the
evidence on iterative retrieval cuts both ways depending on task structure
{{arxiv:2601.19827}}. At enterprise scale, a harder-to-formalize problem
shows up: balancing relevance, coverage, and redundancy under a strict token
budget, which is where structure-aware context construction overlaps
directly with [[context-engineering]] {{arxiv:2601.10681}} — Utilizing
Metadata compares prefix, suffix, unified-embedding, and late-fusion
strategies for injecting document metadata into that same budget
{{arxiv:2601.11863}}, without a clear universal winner among them.

## See also

- [[context-engineering]]
- [[memory]]
- [[safety-security-governance]]
