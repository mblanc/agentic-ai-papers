---
title: Training and Optimization for Agents
category: training-and-optimization
status: draft
updated: 2026-08-01
---

## What it is

This covers making an agent better at its job by changing its weights or its
prompts through a training-style loop — reinforcement learning on
trajectories, self-evolution over a deployment lifetime, fine-tuning
strategy, model merging, and prompt/program optimization — as opposed to
one-off scaffolding changes. It excludes the verification and detection
methods that catch a bad trajectory at runtime without touching training,
which live in [[evaluation-and-benchmarks]].

## State of the art

**Self-evolution — agents that improve from their own execution history
without a human curating new data — is the dominant recent direction, and the
entries split sharply on how much structure to put around the improvement
loop.** At one end, EvolveR distills past runs into abstract guiding
principles that steer later decisions {{arxiv:2510.16079}}, and AutoRefine
extracts reusable "Experience Patterns" in two forms — specialized subagents
for procedural knowledge, skill snippets for static knowledge — with active
pruning so the pattern repository doesn't degrade as it grows, beating
hand-designed baselines on TravelPlanner 27.1% to 12.1%
{{arxiv:2601.22758}}. At the other end, AgentDevel explicitly rejects
population-based search and in-agent self-refinement as unstable and
hard to audit, instead treating the agent like a software release: an
external critic diagnoses failures without touching agent internals, and a
gate prioritizes non-regression over raw score gains {{arxiv:2601.04620}}.
Between these, "Towards AGI" escalates through three distinct strategies —
curriculum learning, RL, genetic algorithms — chosen by failure severity,
finding each suited to a different difficulty band rather than one dominating
{{arxiv:2601.11658}}. No More Stale Feedback adds a third axis to this
picture: it jointly evolves the policy *and* its own natural-language critic
in a synchronized loop, arguing a static offline critic goes stale as the
policy improves past it {{arxiv:2601.06794}}.

**On the RL side, credit assignment and reward design get the most
attention.** GiGPO does hierarchical grouping for credit assignment across
long horizons {{arxiv:2505.10978}}, and SPA-RL attributes final trajectory
reward back to intermediate steps as stepwise progress rather than leaving
credit assignment to whatever the RL algorithm figures out on its own
{{arxiv:2505.20732}}. A distinct methodological problem gets named directly:
pointwise reward scoring on open-ended tasks suffers "discrimination
collapse," where a reward model can't tell subtly-different trajectories
apart; ArenaRL's fix is intra-group tournament ranking instead of scalar
scoring, matching full pairwise-comparison accuracy at linear rather than
quadratic cost {{arxiv:2601.06487}}. A second question — which training
examples belong in RL versus SFT — gets a dynamics-aware answer from PRISM:
route by gradient concentration, since high-conflict data needs RL's
structural adaptation while diffuse-update data is better served by SFT's
consolidation, cutting compute up to 3.22x over hybrid baselines
{{arxiv:2601.07224}}.

**Test-time adaptation without any gradient step is now a competitive
option, not just a cheap fallback.** JitRL retrieves similar past
trajectories to estimate action advantages and modulates output logits
directly — shown to be the exact closed-form solution to the KL-constrained
policy objective — and reports beating full fine-tuning methods like WebRL
at over 30x lower monetary cost {{arxiv:2601.18510}}. ARM pushes the same
no-gradient idea to a different problem, merging several
environment-specialist agents into one generalist by transplanting neurons
along role-specific activation patterns, beating both prior merge methods and
the original specialists without any retraining {{arxiv:2601.07309}}.

**Prompt/program optimization for multi-stage pipelines has its own
scaling problem, separate from single-prompt tuning.** Global textual-gradient
backpropagation through a compound LLM pipeline explodes or vanishes as depth
grows, the same way numeric gradients do; Textual Equilibrium Propagation
replaces it with local, equilibrium-propagation-style prompt refinement,
beating TextGrad on both accuracy and efficiency with the gap widening as
pipelines get deeper {{arxiv:2601.21064}}.

**Environment scarcity for agent RL is being addressed by synthesis rather
than hand-authoring.** EnvScaler auto-generates tool-interactive training
environments at scale — 191 environment skeletons and roughly 7,000 validated
task scenarios via a skeleton-builder/scenario-generator pipeline — and using
them to SFT+RL Qwen3 models gives a solid boost on multi-turn, multi-tool
benchmarks without the hallucination risk of LLM-simulated sandboxes
{{arxiv:2601.05808}}. OpenTinker addresses the adjacent infrastructure
problem: running many LoRA-backed policies over shared compute by treating
adapters as live, mutable policy state rather than static checkpoints, so
SFT, RL, and multi-turn training can share one base model while keeping each
adapter's gradients isolated {{arxiv:2601.07376}}.

## Origin

ATLaS is the clearest lineage marker for "train less, but train the right
part": tuning only on critical steps of expert trajectories rather than the
whole sequence, to cut cost without cutting effectiveness
{{arxiv:2503.02197}}. Self-Rewarding Language Models is the origin point for
using the model itself as its own preference-data source: the model acts as
LLM-as-judge to generate its own DPO training signal, and three rounds of
that loop on Llama 2 70B beat Claude 2, Gemini Pro, and GPT-4 (0613) on
AlpacaEval 2.0 while also sharpening the model's own judging ability
{{arxiv:2401.10020}} — CREAM later shows this loop stalls after a few
iterations because reward bias accumulates when the same model is both
policy and judge, and fixes it by regularizing on how consistent a response's
reward is across iterations {{openreview:Vf6RDObyEF}}. SELFEVOLVE's two-step
knowledge-provider/self-reflective-programmer pipeline is an early instance
of a pattern later generalized across domains: separate the step that
recalls or generates relevant knowledge from the step that critiques and
revises the output {{arxiv:2306.02907}}. WizardLM's Evol-Instruct — using an
LLM to rewrite simple instructions into progressively harder ones instead of
hand-authoring complex training data — is the origin point for
synthetic-data self-evolution specifically, with the resulting fine-tune
beating ChatGPT on human-judged high-complexity instructions
{{arxiv:2304.12244}}.

## Open problems

**Generalization doesn't track the intuitive notion of environment
realism.** A cross-domain study found the simpler, more abstract Sokoban
transferred better to SciWorld than the more "realistic" ALFWorld did, and
that SFT warmup actually *reduces* generalization to new domains even though
it prevents catastrophic forgetting — only step-by-step thinking during RL
reliably preserved it {{arxiv:2601.18217}}. That's a genuinely
counterintuitive result with no settled explanation yet, and it directly
complicates the EnvScaler-style bet that more, more-realistic environments
are the fix for agent RL {{arxiv:2601.05808}}.

**Self-evolving agents create a verification problem that training alone
doesn't solve** — something has to catch a malformed or off-task plan before
it executes. Trajectory Guard and TrajAD both attack this as a real-time
detection problem rather than a training one: a Siamese autoencoder reaching
0.88-0.94 F1 at 32ms, 17-27x faster than an LLM-judge baseline
{{arxiv:2601.00516}}, and a runtime verifier built specifically to localize
the error precisely enough to support rollback-and-retry rather than just
flagging failure {{arxiv:2602.06443}}. As self-evolution methods mature, this
verification layer looks increasingly load-bearing, not optional — and it
sits adjacent to, but outside, this page's scope; see
[[evaluation-and-benchmarks]].

## See also

- [[planning-and-reasoning]]
- [[evaluation-and-benchmarks]]
- [[multi-agent]]
