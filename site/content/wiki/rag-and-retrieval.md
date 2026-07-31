---
title: RAG and Retrieval
category: rag-and-retrieval
status: draft
updated: 2026-07-28
---

## What it is

Retrieval-Augmented Generation couples an LLM with an external knowledge
source at inference time, fetching relevant passages, entities, or graph
structure to ground a response instead of relying only on parametric
knowledge. This page covers retrieval as a component; agent-side use of
retrieved memory over time is [[memory]].

## State of the art

The field is shifting from single-shot vector lookup to *agentic* retrieval —
routing, reflecting, and iterating rather than fetching once and generating.
JADE frames retrieval planning and execution as a cooperative team optimizing
jointly [arxiv:2601.21916](https://arxiv.org/pdf/2601.21916v1), ProRAG uses MCTS step-level rewards to locate
exactly where multi-hop reasoning goes wrong [arxiv:2601.21912](https://arxiv.org/pdf/2601.21912v1), and L-RAG
skips retrieval entirely when model uncertainty is already low
[arxiv:2601.06551](https://arxiv.org/pdf/2601.06551v1). But this isn't a one-directional story: a diagnostic
study specifically asks when iterative retrieval *beats* gold-standard
evidence in scientific multi-hop QA, and when it doesn't
[arxiv:2601.19827](https://arxiv.org/pdf/2601.19827v2) — the honest state of the art is "iterative retrieval
helps, situationally," not "iterative retrieval always wins."

Graph-structured retrieval is a second major thread: Deep GraphRAG
balances global and local hierarchical retrieval with beam-search reranking
[arxiv:2601.11144](https://arxiv.org/pdf/2601.11144v3), and CIRAG preserves multiple evidence chains rather than
collapsing to one at each hop [arxiv:2601.06799](https://arxiv.org/pdf/2601.06799v1).

Privacy and access control have become first-class RAG concerns rather than
an afterthought. A systematization of RAG privacy risk finds current
mitigations are still immature relative to the threat surface
[arxiv:2601.03979](https://arxiv.org/pdf/2601.03979v1). SD-RAG enforces disclosure controls during retrieval
itself, before the model ever sees sensitive passages, so it stays resilient
even to prompt injection targeting the generator
[arxiv:2601.11199](https://arxiv.org/pdf/2601.11199v1), and a distance-preserving encryption scheme lets an
untrusted cloud host the vector store while still computing similarity, at a
fraction of the cost of homomorphic encryption [arxiv:2601.12331](https://arxiv.org/pdf/2601.12331v1).

## Origin

WebCPM recorded 125,954 real human web-search actions to train models on
*interactive* retrieval rather than static corpus lookup [acl:2023.acl-long.499](https://aclanthology.org/2023.acl-long.499/)
— an early instance of retrieval as an agentic loop rather than a preprocessing
step. ToolkenGPT sits at a related origin point, representing external
resources (tools, in this case) as embeddings a frozen LLM can invoke directly,
the same move graph- and tool-retrieval systems now make for knowledge
[url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html](https://proceedings.neurips.cc/paper_files/paper/2023/hash/8fd1a81c882cd45f64958da6284f4a3f-Abstract-Conference.html).

## Open problems

Privacy mitigations for RAG are behind the attack surface, per the SoK's own
assessment of maturity [arxiv:2601.03979](https://arxiv.org/pdf/2601.03979v1) — this isn't solved, just
inventoried. There's also no settled guidance on *when* agentic retrieval
(routing, iteration, reflection) is worth its added latency and cost over
plain retrieval, since the evidence cuts both ways depending on task structure
[arxiv:2601.19827](https://arxiv.org/pdf/2601.19827v2). Enterprise-scale deployments face a harder-to-formalize
problem too: balancing relevance, coverage, and redundancy under a strict
token budget, which is where structure-aware context construction starts to
overlap directly with [[context-engineering]] [arxiv:2601.10681](https://arxiv.org/pdf/2601.10681v1).

## See also

- [[context-engineering]]
- [[memory]]
- [[safety-security-governance]]
