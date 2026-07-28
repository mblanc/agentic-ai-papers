---
title: Training and Optimization for Agents
category: training-and-optimization
status: draft
updated: 2026-07-28
---

## What it is

This covers making an agent better at its job through training or tuning —
reinforcement learning on trajectories, self-evolution over deployment
lifetime, fine-tuning strategy, and the reward/data-allocation choices that
shape all of these — as opposed to prompting or scaffolding changes that leave
weights untouched.

## State of the art

The dominant recent direction is self-evolution: agents that improve from
their own execution history without a human curating new training data. But
the entries here split sharply on *how much structure* to put around that
improvement loop, and that split is the real story.

At one end, EvolveR distills past runs into abstract guiding principles
{{arxiv:2510.16079}} and AutoRefine extracts dual-form "Experience Patterns" —
specialized subagents for procedural knowledge, skill snippets for static
knowledge — with active pruning so the pattern repository doesn't degrade as
it grows, beating hand-designed baselines on TravelPlanner (27.1% vs 12.1%)
{{arxiv:2601.22758}}. At the other end, AgentDevel explicitly rejects
population-based search and in-agent self-refinement as unstable and
hard-to-audit, instead treating the agent as a software release: an external
critic diagnoses failures without touching agent internals, and a gate
prioritizes non-regression as the primary objective over raw score gains
{{arxiv:2601.04620}}. Between these, "Towards AGI" escalates through three
distinct evolution strategies (curriculum learning, RL, genetic algorithms)
depending on failure severity, finding each suited to a different difficulty
band rather than one dominating {{arxiv:2601.11658}}.

On the RL side specifically, a real methodological problem gets named and
addressed: pointwise reward scoring on open-ended tasks suffers "discrimination
collapse", where a reward model can't tell subtly-different trajectories
apart, and the fix is intra-group tournament ranking instead of scalar scoring
{{arxiv:2601.06487}}. A second RL-vs-SFT question — which examples belong in
which training regime — gets a dynamics-aware answer: route by gradient
concentration, since high-conflict data needs RL's structural adaptation while
diffuse-update data is better served by SFT's consolidation
{{arxiv:2601.07224}}.

Test-time adaptation without any gradient step at all is now a competitive
option, not just a cheap fallback: JitRL retrieves similar past trajectories to
estimate action advantages and modulates output logits directly, proven to be
the exact closed-form solution to the KL-constrained policy objective, and
outperforms full fine-tuning methods at over 30x lower cost
{{arxiv:2601.18510}}.

## Origin

ATLaS is the clearest lineage marker for "train less, but train the right
part": tuning only on critical steps of expert trajectories rather than the
whole sequence, to cut cost without cutting effectiveness
{{arxiv:2503.02197}}. SELFEVOLVE's two-step knowledge-provider /
self-reflective-programmer pipeline is an early instance of the pattern later
generalized across domains: separate the step that recalls or generates
relevant knowledge from the step that critiques and revises the output
{{arxiv:2306.02907}}.

## Open problems

Generalization doesn't track the intuitive notion of environment realism: a
cross-domain study found the simpler, more abstract Sokoban transferred better
to SciWorld than the more "realistic" ALFWorld did, and that SFT warmup
actually *reduces* generalization to new domains even though it prevents
catastrophic forgetting — only step-by-step thinking during RL reliably
preserved it {{arxiv:2601.18217}}. That's a genuinely counterintuitive result
with no settled explanation yet.

Separately, self-evolving agents create a verification problem that training
alone doesn't solve: something has to catch a malformed or off-task plan
before it executes. Trajectory Guard and TrajAD both attack this as a
real-time detection problem rather than a training one — a Siamese
autoencoder reaching 0.88-0.94 F1 at 32ms, far faster than an LLM-judge
baseline {{arxiv:2601.00516}}, and a runtime verifier built specifically to
locate the error precisely enough to support rollback-and-retry rather than
just flagging failure {{arxiv:2602.06443}}. As self-evolution methods mature,
this verification layer looks increasingly load-bearing, not optional.

## See also

- [[planning-and-reasoning]]
- [[evaluation-and-benchmarks]]
- [[multi-agent]]
