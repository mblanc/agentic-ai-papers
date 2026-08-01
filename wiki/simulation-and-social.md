---
title: Simulation and Social Agents
category: simulation-and-social
status: draft
updated: 2026-08-01
---

## What it is

This category covers LLM agents used to model human-like individuals and
societies rather than to complete a task: giving agents personas, memory, and
motivation, then observing what emerges when many of them interact — social
norms, competition, conformity, trust, or believable daily behavior. It spans
both the simulations themselves (towns, epidemics, markets, social networks)
and the underlying question of whether an LLM playing a persona is doing
anything psychologically real.

## State of the art

**Generative Agents remains the reference architecture.** Twenty-five agents
populate a Sims-style sandbox town, each driven by a memory stream, periodic
reflection, and planning that turns raw observations into believable
behavior over simulated days {{arxiv:2304.03442}}. Later work argues the
piece doing the real work in that architecture is summarization, not memory
retrieval itself, and that architecture choices there deserve more scrutiny
than they get {{arxiv:2305.01253}}. CitySim scales the same idea to city
level, using a recursive value-driven planner plus beliefs, goals, and
spatial memory to align individual and aggregate behavior with real urban
data {{arxiv:2506.21805}}.

**Whether these agents actually stand in for humans is still contested, and
the evidence cuts both ways.** On the positive side: GPT-4 agents in
behavioral-economics Trust Games track how humans actually play, including
trust biases and how trust shifts under pressure {{arxiv:2402.04559}}; the
"Turing Experiment" framework replicates classic economics and psychology
studies by simulating a representative sample rather than one persona
{{url:https://proceedings.mlr.press/v202/aher23a/aher23a.pdf}}; and after
collecting 1,100 people's biased responses to decision scenarios, GPT-4/GPT-5
reproduce those individual-level cognitive biases with notable precision —
though the two model generations don't match human behavior equally well
{{arxiv:2602.05597}}. On the negative side, the same aher23a paper that
validated replication also found a "hyper-accuracy distortion" in GPT-family
models, and a computational-social-science benchmark across 13 LLMs and 25
tasks found they still trail fine-tuned classifiers, useful mainly as
annotators rather than standalone {{acl:2024.cl-1.8}}. Persona assignment
also has a documented safety cost: giving ChatGPT a persona increases its
toxicity up to 6x across more than 500,000 generations, with some groups
targeted 3x more than others regardless of which persona was assigned
{{arxiv:2304.05335}}.

**Multi-agent societies reproduce real social dynamics, for better and
worse.** CompeteAI's virtual town of competing restaurant and customer
agents produces emergent strategies that line up with established market and
sociological theory {{arxiv:2310.17512}}. Werewolf games elicit emergent
deception and trust with no fine-tuning required
{{arxiv:2309.04658}}. Emergence of Social Norms gives an architecture for how
norms get created, spread, and complied with inside a generative-agent
society {{arxiv:2403.08251}}. But agents are also manipulable the way humans
are: Asch-style conformity experiments show LLM agents that are near-perfect
in isolation become manipulable under simulated group pressure, which the
authors frame as a genuine multi-agent security risk rather than just a
curiosity {{arxiv:2601.05384}}. At larger scale, a 70,000+-agent social
network shows measurable gender homophily and bias emerging without being
programmed in {{arxiv:2602.02606}}.

**Domain-specific simulations are moving from proof-of-concept to
production-shaped systems.** Epidemic Modeling with Generative Agents has
agents reason about their own protective behavior and produces resulting
epidemic curves {{arxiv:2307.04986}}. Macroeconomic agent-based modeling
replaces hand-coded behavioral rules with LLM agents that perceive, remember,
and reflect on market conditions, producing more realistic consumption
decisions and emergent phenomena {{acl:2024.acl-long.829}}. On the
recommendation side, generative-agent user simulators initialized from real
datasets are used to probe whether agents faithfully reproduce real user
behavior, including filter bubbles {{arxiv:2310.10108}}.

## Origin

The line between "agent with a persona" and "agent as evidence about the
model's own capacities" runs through the Theory of Mind literature: running
false-belief tests on 11 LLMs found GPT-4 solved 75% of tasks — matching
six-year-old children in prior human studies — while older and smaller
models scored zero, suggesting Theory-of-Mind-like reasoning emerged as a
byproduct of scaling rather than being explicitly trained
{{arxiv:2302.02083}}. Role-Play with Large Language Models reframes the
whole persona phenomenon deliberately: apparent agent "traits" are role-play
outputs describable in folk-psychology terms, not evidence of real deception
or self-awareness {{arxiv:2305.16367}}. The broader risk landscape these
personas sit inside is mapped earliest and most comprehensively by the six
risk areas and 21 named risks in {{arxiv:2112.04359}}.

## Open problems

**The persona-realism gap is now named and partially fixed, not solved.**
Large-scale generative-agent social simulations suffer from a "Behavior-
Realism Gap" where personas drift from real expert or data-derived behavior;
PersonaEvolve, an LLM-driven persona optimizer, cuts distributional
divergence 84% versus baseline on an active-shooter crowd simulation and
generalizes to new scenarios — but 84% reduction is not elimination
{{acl:2025.emnlp-main.1562.pdf}}.

**Games remain a sharp probe of what LLM agents are actually good at
socially.** Repeated 2x2 games show LLM agents play self-interested games
like Prisoner's Dilemma well but flub pure-coordination games like Battle of
the Sexes, though GPT-4 improves markedly given opponent information and
"social chain-of-thought" prompting {{arxiv:2305.16867}} — a reminder that
apparent social competence is uneven across game structure, not a single
capability.

**Whether personality/psychometric probes (MBTI, Big Five-style traits) are
measuring anything real, versus a fingerprint of prompting and training
data, is unresolved.** MBTI-on-LLMs work frames the test as a rough-but-usable
behavioral fingerprint for model comparison despite MBTI's own weak
scientific standing {{arxiv:2307.16180}}; a separate psychometric-validity
study across 18 models finds personality outputs can pass validity checks
and be deliberately dialed toward a target profile, but is explicit that
this is strongest in larger, instruction-tuned models {{arxiv:2307.00184}} —
these are different claims (fingerprint-for-comparison vs. genuine,
controllable trait) that the field has not reconciled.

## See also

- [[multi-agent]]
- [[safety-security-governance]]
- [[domain-applications]]
- {{gh:minedojo/voyager}} — reference skill-library agent, adjacent tooling for agent societies in game worlds
