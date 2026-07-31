---
title: Surveys and Foundations
category: surveys-and-foundations
status: draft
updated: 2026-07-28
---

## What it is

This category holds the field's survey papers, foundation-model papers, and
position papers — the entries that map a subfield rather than propose one new
technique. It's the right place to start when a topic elsewhere in the wiki
needs broader context than a single paper provides.

## State of the art

For LLM-based agents generally, two surveys are treated as the canonical
starting points here: a unified construction framework covering the field
broadly [arxiv:2308.11432](https://arxiv.org/abs/2308.11432), and the paper that traces "agent" from its
philosophical origins through to a brain/perception/action framework, then
into single-agent, multi-agent, and human-agent cooperation
[arxiv:2309.07864](https://arxiv.org/abs/2309.07864). A more recent methodology-centered pass links
architectural choices directly to collaboration mechanisms and evolutionary
pathways rather than treating them as separate topics
[arxiv:2503.21460](https://arxiv.org/abs/2503.21460).

Several entries name the categories other wiki pages build on. "On the
Opportunities and Risks of Foundation Models" is the paper that named the
category itself, identifying emergence and homogenization as the two central
dynamics to track [arxiv:2108.07258](https://arxiv.org/abs/2108.07258). Self-evolving agents — covered in
depth in [[training-and-optimization]] — have their own entry point via a
four-phase framework [arxiv:2404.14387](https://arxiv.org/pdf/2404.14387), and agent memory (see [[memory]])
via a design-and-evaluation survey [arxiv:2404.13501](https://arxiv.org/abs/2404.13501). Planning
(see [[planning-and-reasoning]]) gets its first systematic taxonomy here
[arxiv:2402.02716](https://arxiv.org/abs/2402.02716), and evaluation methodology
(see [[evaluation-and-benchmarks]]) a two-dimensional taxonomy plus
enterprise-specific challenges [arxiv:2507.21504](https://arxiv.org/abs/2507.21504).

Domain-specific surveys extend the same pattern into narrower fields: LLM
agents for scientific discovery differ from general-purpose agents in ways a
dedicated survey works through [arxiv:2503.24047](https://arxiv.org/abs/2503.24047), and materials science
[arxiv:2506.20743](https://arxiv.org/abs/2506.20743) and broader scientific-LLM development
[arxiv:2508.21148](https://arxiv.org/abs/2508.21148) each get their own data-centric treatment. Vision-language
models [arxiv:2501.02189](https://arxiv.org/pdf/2501.02189) and multimodal agents [arxiv:2402.15116](https://arxiv.org/abs/2402.15116) cover
the non-text-only frontier.

## Origin

LLaMA is the foundation-model release that made "train state-of-the-art models
on public data alone" credible at scale — LLaMA-13B beat GPT-3 (175B parameters)
on most benchmarks, and the weights were released to researchers, which is a
large part of why an open agent ecosystem exists to survey at all
[url:https://ai.meta.com/research/publications/llama-open-and-efficient-foundation-language-models](https://ai.meta.com/research/publications/llama-open-and-efficient-foundation-language-models/).

## Open problems

Alignment work here splits into outer alignment (specifying the right
objective) and inner alignment (getting the model to actually pursue it), and
the survey covering both is explicit that neither is solved, just better
categorized [arxiv:2309.15025](https://arxiv.org/abs/2309.15025). Security surveys are similarly inventory-
stage rather than solution-stage: a combined taxonomy across security,
privacy, and ethics threats in LLM-based agents exists
[arxiv:2411.09523](https://arxiv.org/pdf/2411.09523?), but as with the RAG privacy work covered in
[[rag-and-retrieval]], cataloguing a risk is not the same as having a mature
defense against it.

*Editorial note:* three entries in this category could not be summarized this
pass — sources were login-walled or returned an unreadable binary — and remain
marked `NEEDS-SOURCE` in the corpus rather than guessed. That's a corpus gap,
not a claim they're unimportant; check `corpus/by-category/surveys-and-foundations.md`
before assuming this page's coverage is exhaustive.

## See also

- [[training-and-optimization]]
- [[memory]]
- [[planning-and-reasoning]]
- [[evaluation-and-benchmarks]]
