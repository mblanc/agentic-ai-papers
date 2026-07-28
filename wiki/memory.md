---
title: Agent Memory
category: memory
status: draft
updated: 2026-07-28
---

## What it is

Memory is what an agent retains *across* sessions or across a context reset —
distinct from [[context-engineering]], which curates what's active within a
single window. A memory system decides what gets written down, how it's
organized, and how it's found again later, often long after the interaction
that produced it.

## State of the art

There is no consensus architecture; three paradigms compete on genuinely
different bets about what makes retrieval reliable.

**Graph-structured memory** routes retrieval through relationships rather than
flat similarity. GAAMA avoids the "mega-hub" problem of entity-centric graphs
by routing through concept nodes instead, reaching 79.1% on LoCoMo-10
{{arxiv:2603.27910}}, while a more formally grounded approach models memory as
a versioned property graph under AGM belief-revision semantics, scoring 93.3%
on an implicit-constraint benchmark where the best prior baseline hit 45.7%
{{arxiv:2603.17244}}.

**Execution-state memory** argues semantic similarity is the wrong axis
entirely for long-horizon agentic tasks: MAGE stores a hierarchical state tree
keyed to what the agent *did*, not what it said, isolating flawed branches from
the active path and cutting tokens 55% while raising success 7.8-20.4pp
{{arxiv:2606.06090}}.

**Discrete fact objects** make the strongest empirical claim: benchmarked
against in-context memory, hash-addressed Knowledge Objects hit 100% accuracy
at every scale tested, while in-context memory's compaction destroys 60% of
facts and cascading compaction erodes 54% of project constraints — a failure
the authors show is architectural, not model-specific, replicating across four
frontier models {{arxiv:2603.17781}}.

Below the research layer, a set of production memory stores has converged on
similar shapes: Letta/MemGPT's core/archival/recall tiers established the
reference pattern {{gh:letta-ai/letta}}; mem0 {{gh:mem0ai/mem0}}, Zep
{{gh:getzep/zep}}, and cognee {{gh:topoteretes/cognee}} are the common
drop-in options; GitHub Copilot's cross-agent memory adds just-in-time
re-verification against code so shared memory doesn't drift as the codebase
changes {{url:https://github.blog/ai-and-ml/github-copilot/building-an-agentic-memory-system-for-github-copilot}}.

A direct structural comparison across chunks, triples, atomic facts, and
summaries found no single structure dominates — mixed structures were most
resilient to noise, and iterative retrieval consistently beat single-step or
reranked retrieval {{arxiv:2412.15266}}. Read this as license to not over-commit
to one memory shape early.

## Origin

Letta (MemGPT) is the reference point for treating agent memory as an
OS-style tiered system rather than a single vector store
{{gh:letta-ai/letta}}. The most current entry point into where the field is
heading is the survey organizing memory by substrate, cognitive mechanism, and
subject {{arxiv:2602.06052}}.

## Open problems

Memory is now an attack surface, not just an engineering convenience. Memory
poisoning attacks corrupt an agent's long-term memory through query-only
interactions, and realistic defenses require careful trust-threshold
calibration to avoid both under- and over-filtering
{{arxiv:2601.05504}}. RAG knowledge bases can be extracted wholesale by an
attacker who schedules non-redundant queries, reaching 66.8% corpus coverage in
1,000 queries {{arxiv:2601.15678}}. Governance is catching up but is still
mostly bespoke: MemArchitect treats decay, conflict resolution, and privacy as
explicit policy rather than passive storage {{arxiv:2603.18330}}, and MemTrust
proposes a hardware zero-trust architecture for memory shared across agents and
apps {{arxiv:2601.07004}} — neither is yet a settled default the way vector
retrieval was for RAG.

Separately, tool-memory conflict — an agent's parametric knowledge
contradicting what a tool just told it — is common on STEM tasks, and none of
the prompting- or RAG-based mitigations tested actually resolve it
{{arxiv:2601.09760}}. That's an open correctness problem, not just an
efficiency one.

## See also

- [[context-engineering]]
- [[safety-security-governance]]
- [[multi-agent]]
