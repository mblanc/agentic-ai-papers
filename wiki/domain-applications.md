---
title: Domain Applications
category: domain-applications
status: draft
updated: 2026-08-01
---

## What it is

This category collects agents built for a specific external domain — medicine,
science, mathematics, chemistry, business, recommendation, education — rather
than for agentic infrastructure in general. The entries share a pattern more
than a topic: an LLM wrapped with domain tools, a domain-specific evaluation
metric, and (increasingly) an explicit accounting of where the agent still
needs a human checkpoint. The category spans enough ground that it's read as
clusters, not one narrative.

## State of the art

**Autonomous science is the most active cluster, and the honest entries in it
report failure rates alongside successes.** Agent Laboratory runs an LLM
through literature review, experimentation, and report writing end to end,
and with human feedback at each stage matches prior autonomous-research
quality at an 84% lower cost {{arxiv:2501.04227}}. AI Scientist runs the same
kind of pipeline — idea generation, experiments, full paper draft with
citations — aiming at fully automated discovery {{gh:sakanaai/ai-scientist}}.
But a case study running four end-to-end attempts at fully autonomous ML
research with six chained agents found three failed outright, documenting
recurring failure modes including implementation drift, context degradation,
and false success claims {{arxiv:2601.03315}} — a direct counterweight to
the more optimistic cost/quality framing elsewhere in the cluster. Agon
runs roughly 444 cycles of automated research under a "machine scales, human
steers" design and reports its own failures in a severity-tagged taxonomy
rather than hiding them {{arxiv:2606.24177}}. aiXiv adds the missing
publication layer: an open-access venue where human and AI scientists submit,
review, and revise proposals through a multi-agent pipeline
{{arxiv:2508.15126}}. R-LAM takes the opposite approach to open-ended
autonomy — constraining action execution with structured schemas,
deterministic policies, and provenance tracking so workflows stay auditable
and replayable {{arxiv:2601.09749}}, echoed by AUTOBUS's use of a symbolic
reasoning engine to check LLM-translated business logic against a knowledge
graph before execution {{arxiv:2601.15599}}.

**Medicine and biology show the same optimism/caution split.** Agent
Hospital simulates a full hospital of LLM patients, nurses, and doctors, so
doctor-agents evolve by treating tens of thousands of simulated cases without
labeled data, then beat prior medical agents on USMLE-style MedQA
{{arxiv:2405.02957}}. CRISPR-GPT pairs an LLM with domain tools to walk a
researcher through an entire gene-editing workflow, and its authors
explicitly address the ethics of automating that capability
{{arxiv:2404.18021}}. In drug discovery, a multi-agent pipeline (Principal
Researcher, Database, Medicinal Chemist, Ranking, Critic) that logs
provenance for every decision improved predicted AKT1 binding affinity by
31% over single-agent or unguided runs — though single-agent output scored
better on drug-likeness, a real tradeoff the paper doesn't paper over
{{arxiv:2508.03444}}. The Virtual Lab of AI agents produced experimentally
validated SARS-CoV-2 nanobodies, one of the few entries here with a wet-lab
result rather than a benchmark score {{url:https://nature.com/articles/s41586-025-09442-9}}.
Against this, a commentary on self-driving chemistry labs argues current lab
agents can't reliably judge when their own results are wrong, and that
plan-make-measure-analyze loops still need explicit human-expert checkpoints
{{url:https://doi.org/10.1038/s43588-025-00769-x}} — the same caution shows
up for mental-health chatbots, where mining 120 Reddit threads about Replika
found real upside (on-demand, judgment-free support) alongside unsolicited
sexual/violent content reaching minors and memory resets erasing context,
concluding these agents aren't ready for unsupervised long-term use
{{url:https://pmc.ncbi.nlm.nih.gov/articles/PMC10785945}}.

**Formal mathematics is the most benchmark-driven cluster and the most
mature.** The lineage runs from translating informal math into formal
statements {{arxiv:2205.12615}}, through informal proofs guiding formal
provers {{arxiv:2210.12283}}, to LeanDojo's retrieval-augmented, fully open
Lean toolkit {{arxiv:2306.15626}}. COPRA adds in-context proof search with
error feedback {{arxiv:2310.04353}}; Lean-STaR interleaves informal reasoning
with formal proof steps {{arxiv:2407.10040}}; ImProver rewrites existing
proofs against a user-chosen metric rather than only generating new ones
{{arxiv:2410.04753}}; miniCTX moves the benchmark to long-context,
real-repository settings instead of isolated lemmas {{arxiv:2408.03350}}.
AlphaProof reports IMO silver-medal-level performance combining
reinforcement learning with formal mathematics
{{url:https://deepmind.google/discover/blog/ai-solves-imo-problems-at-silver-medal-level}}.
OptimAI applies the same chained formulator/planner/coder/critic pattern to
optimization rather than proof search, hitting 88.1% accuracy on NLP4LP and
82.3% on Optibench, roughly halving prior methods' error rate
{{arxiv:2504.16918}}.

**Recommendation and business agents wrap existing systems rather than
replacing them.** Recommender AI Agent wraps a traditional recommender model
as a tool behind an LLM "brain" with memory, planning, and reflection, adding
a natural-language interface to an ID-based system rather than replacing its
core {{arxiv:2308.16505}}. A dynamic recommender-system simulator goes
further, having simulated likes, reviews, and purchases actually update item
state and spawn merchant-agent replies, reproducing emergent effects like
brand loyalty that static offline testbeds can't capture
{{acl:2025.emnlp-main.956}}. SuperAgent answers e-commerce questions by
mining public product pages and user content instead of proprietary chat
logs {{acl:P17-4017}}.

## Origin

Autoformalization — translating natural-language mathematics into checkable
formal statements — is the foundational move that the whole theorem-proving
cluster builds on {{arxiv:2205.12615}}; everything from LeanDojo to ImProver
assumes some version of that translation step already works well enough to
build on.

## Open problems

**Cost and reproducibility of "autonomous research" claims are still being
argued over inside the category itself, not settled by it.** The 84%
cost-reduction figure for Agent Laboratory {{arxiv:2501.04227}} and the
three-of-four outright failure rate reported for autonomous ML research
{{arxiv:2601.03315}} are both about the same class of system and are hard to
reconcile without knowing what "success" was scoped to mean in each case —
this page treats that as an open tension rather than picking a winner.

**Human-checkpoint design is emerging as its own sub-problem**, distinct from
raw capability. R-LAM {{arxiv:2601.09749}}, AUTOBUS {{arxiv:2601.15599}}, and
the self-driving-lab commentary {{url:https://doi.org/10.1038/s43588-025-00769-x}}
each propose a different mechanism — schemas/provenance, symbolic
verification, and explicit human sign-off gates respectively — for the same
underlying problem: none of them yet argue their mechanism generalizes
outside its own domain.

**Domain-specific evaluation is still borrowed, not built.** Medical agents
lean on MedQA/USMLE-style scoring {{arxiv:2405.02957}}, math agents on formal
proof-checking, and drug-discovery agents on predicted (not measured)
binding affinity {{arxiv:2508.03444}} — proxies with different levels of
ground-truth reliability that this category does not yet have a shared
standard for comparing across.

## See also

- [[simulation-and-social]]
- [[multi-agent]]
- [[evaluation-and-benchmarks]]
- [[safety-security-governance]]
