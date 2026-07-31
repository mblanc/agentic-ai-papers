---
title: Planning and Reasoning
category: planning-and-reasoning
status: draft
updated: 2026-07-28
---

## What it is

Reasoning is how an agent works through a problem step by step; planning is
deciding a sequence of actions to reach a goal, often over a horizon long
enough that early choices constrain what's possible later. Both are usually
handled by prompting the same underlying model, but the entries here make the
case that they're not the same capability, and conflating them causes
specific, reproducible failures.

## State of the art

The sharpest recent finding in this category is a direct argument that
step-wise reasoning is not planning: reasoning induces a locally-greedy
policy that's fine over short horizons but systematically commits early to
choices it can't recover from once consequences arrive later. FLARE adds
explicit lookahead and value propagation to a single model and, with that
addition, an 8B LLaMA outperforms GPT-4o doing plain step-by-step reasoning on
long-horizon tasks [arxiv:2601.22311](https://arxiv.org/pdf/2601.22311v1). This is the load-bearing distinction
for the whole category — better reasoning does not automatically buy better
planning.

Multi-agent planning gets real gains from two mechanisms specifically:
structured information sharing and reflective coordination. A shared notebook
cut hallucinated-detail errors 18% in multi-agent travel planning, and adding
an orchestrator cut errors a further 13.5%, combining for a 25% pass rate
against a 7.5% single-agent baseline [arxiv:2508.12981](https://arxiv.org/abs/2508.12981). PMC gets to a
similar place by decomposing constraint-heavy planning into a hierarchy of
subordinate tasks, reaching 42.68% on TravelPlanner versus GPT-4's 2.92% —
and notably works with an 8B model as the planning core, not just frontier
models [acl:2025.coling-main.672](https://aclanthology.org/2025.coling-main.672/).

Governed, auditable planning is emerging as its own concern in enterprise
settings: POLARIS treats automation as typed plan synthesis, with a planner
proposing type-checked plan graphs and execution gated by validators and
compiled policy guardrails, producing full audit trails for finance-document
tasks [arxiv:2601.11816](https://arxiv.org/pdf/2601.11816v1).

Efficiency has its own thread, distinct from planning quality. BudgetThinker
lets a model track its own remaining reasoning-token budget via inserted
control tokens, trained with a length-aware RL reward
[arxiv:2508.17196](https://arxiv.org/abs/2508.17196), and SemanticALLI caches structured intermediate
reasoning artifacts rather than final responses, lifting cache hit rate from
38.7% to 83.1% and bypassing thousands of redundant LLM calls
[arxiv:2601.16286](https://arxiv.org/pdf/2601.16286v2).

## Origin

TPTU is the foundational framework distinguishing task planning from tool
usage as two capabilities an LLM-based agent needs jointly, evaluated with
one-step and sequential agent variants [arxiv:2308.03427](https://arxiv.org/abs/2308.03427), extended by
TPTU-v2 with an API retriever, a fine-tuned planner, and a demo selector for
hard-to-distinguish APIs at real commercial scale [arxiv:2311.11315](http://arxiv.org/abs/2311.11315). DEPS
(Describe, Explain, Plan and Select) is the origin point for interactive,
feedback-corrected planning in open-ended environments, becoming the first
zero-shot agent to robustly clear 70+ Minecraft tasks
[url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/6b8dfb8c0c12e6fafc6c256cb08a5ca7-Abstract-Conference.html](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6b8dfb8c0c12e6fafc6c256cb08a5ca7-Abstract-Conference.html).

## Open problems

Planning agents are a live security target through a channel that isn't
retrieval: UReCoM manipulates a *benign user* into relaying adversarial
content inside their own request, and this bypasses prompt-injection defenses
better than five standard attack baselines, because agents validate explicit
malicious instructions far more reliably than adversarial entities embedded in
otherwise-legitimate user text — a design flaw the authors find present across
12 commercial agents [arxiv:2601.10758](https://arxiv.org/pdf/2601.10758v1). See [[safety-security-governance]]
for the broader threat landscape.

*Editorial note:* 7 entries in this category could not be summarized this pass
— two OpenReview pages required login past a bot-check, two IEEE pages
returned bot-blocking errors, one Nature article is login-walled, one
Wiley article is paywalled, and one ACM/IEEE-adjacent page returned no
retrievable content. These remain `NEEDS-SOURCE` in the corpus rather than
guessed; check `corpus/by-category/planning-and-reasoning.md` for the list.

## See also

- [[surveys-and-foundations]]
- [[multi-agent]]
- [[safety-security-governance]]
