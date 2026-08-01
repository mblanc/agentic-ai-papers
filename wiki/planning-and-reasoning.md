---
title: Planning and Reasoning
category: planning-and-reasoning
status: draft
updated: 2026-08-01
---

## What it is

Reasoning is working through a problem step by step; planning is choosing a
sequence of actions toward a goal, often over a horizon long enough that
early choices foreclose later options. Most agent harnesses conflate the two
by prompting one model to do both. This category's central finding is that
the conflation is not free: a model can reason well locally and still plan
badly, and the corpus tracks four largely separate lines of work that try to
close that gap — interleaved reasoning-and-acting, tree/MCTS search over
candidate actions, self-critique and iterative refinement, and explicit
task decomposition into planner/executor roles.

## State of the art

**Step-wise reasoning is not planning, and the corpus now has a direct
argument for why.** A model doing plain chain-of-thought effectively runs a
locally-greedy policy: fine over short horizons, but it commits early to
choices it cannot walk back once delayed consequences arrive. FLARE adds
explicit lookahead and value propagation on top of a single model, and with
that addition an 8B LLaMA outperforms GPT-4o doing standard step-by-step
reasoning on long-horizon tasks — the paper states the qualitative result
plainly but its abstract does not give the margin as a number
{{arxiv:2601.22311}}. This is the organizing claim for the category: better
reasoning does not automatically buy better planning.

**ReAct is still the structural default.** Interleaving a Thought, an
Action, and an Observation in a loop remains the pattern nearly every agent
harness in this corpus builds on or reacts against {{arxiv:2210.03629}}. Two
lines extend it toward deliberate search: Tree of Thoughts explores multiple
reasoning branches with lookahead and backtracking instead of committing to
one chain {{arxiv:2305.10601}}, and RAP repurposes the LLM as both world
model and reasoning agent under Monte Carlo Tree Search {{arxiv:2305.14992}}.
LATS folds environment feedback directly into the MCTS signal over full
agent trajectories, not just token sequences {{arxiv:2310.04406}}. That
lineage continues into 2026: SYMPHONY runs MCTS planning across a pool of
*heterogeneous* LLM agents to diversify search branches, beating single-agent
MCTS baselines even with consumer-hardware open models {{arxiv:2601.22623}},
and ProAct trains on environment-grounded lookahead trajectories with
Monte-Carlo rollouts added to the policy gradient specifically to fight
compounding simulation error, letting a 4B model beat open-source baselines
on 2048 and Sokoban {{arxiv:2602.05327}}.

**Self-refinement's evidence is genuinely mixed, not a clean success story.**
Reflexion has an agent critique its own failed attempt in natural language
and retry {{arxiv:2303.11366}}, and Self-Refine has one model generate,
critique, and revise its own output in a loop {{arxiv:2303.17651}}. But a
direct study finds LLMs cannot self-correct reasoning *without* external
feedback — intrinsic self-correction often degrades accuracy rather than
improving it {{arxiv:2310.01798}}, which directly complicates the Reflexion/
Self-Refine story rather than confirming it. Where self-critique does show
gains, they come from adding structure the model can't fabricate on its own:
Devil's Advocate adds anticipatory reflection before acting plus post-action
and post-completion checks, for a 3.5-point WebArena success-rate gain and a
45% cut in trial-and-error revisions {{arxiv:2405.16334}}; CRITIC grounds
self-correction in tool-interactive critiquing rather than pure introspection
{{openreview:Sx038qxjek}}.

**Multi-agent coordination produces some of the largest, best-quantified
gains in the category, on the same benchmark.** In multi-agent travel
planning, a shared notebook for structured information sharing cuts
hallucinated-detail errors by 18%, and adding an orchestrator agent cuts
errors a further 13.5% within focused sub-areas; combined, they lift
TravelPlanner pass rate from a 7.5% single-agent baseline to 25%
{{arxiv:2508.12981}}. PMC gets to a comparable place by a different route —
decomposing constraint-heavy planning into a hierarchy of subordinate tasks
across a zero-shot multi-agent pipeline — reaching 42.68% on TravelPlanner
against GPT-4's 2.92%, and, notably, with only an 8B model as the planning
core {{acl:2025.coling-main.672}}. Both results point the same direction:
TravelPlanner's famously low baseline success rates {{arxiv:2402.01622}} are
much more a coordination-and-decomposition problem than a raw-capability one.

**Governed and cost-aware planning are emerging as distinct concerns from
planning quality itself.** POLARIS treats back-office automation as typed
plan synthesis: a planner proposes type-checked plan graphs, execution is
gated by validators and compiled policy guardrails, and the system reaches
0.81 micro-F1 on SROIE while producing full audit trails
{{arxiv:2601.11816}}. On the cost side, BudgetThinker has a model track its
own remaining reasoning-token budget via inserted control tokens, trained
with a length-aware RL reward {{arxiv:2508.17196}}, and SemanticALLI caches
structured intermediate reasoning artifacts rather than final responses,
lifting cache hit rate from 38.7% to 83.1% and bypassing thousands of
redundant LLM calls {{arxiv:2601.16286}}. DPSDP applies dynamic-programming
policy search to multi-agent reflection specifically, provably matching any
in-distribution policy and lifting MATH 500 first-turn accuracy from 58.2%
to 63.2% via five rounds of refinement with majority voting
{{arxiv:2506.08379}}.

**Task decomposition into explicit planner/executor roles is a recurring,
independently-reinvented architecture.** TPTU frames task planning and tool
usage as two capabilities an agent needs jointly {{arxiv:2308.03427}},
extended by TPTU-v2 with an API retriever and fine-tuned planner for
real commercial-scale deployments {{arxiv:2311.11315}}. Plan-and-Act
specializes planner and executor as independent components rather than one
prompted model doing both, reaching 57.58% on WebArena-Lite and 81.36% on
WebVoyager {{arxiv:2503.09572}}. Task-Decoupled Planning takes the same
split further into a dependency graph, so a failure triggers localized
replanning of the affected branch instead of cascading through the whole
plan {{arxiv:2601.07577}}.

## Origin

The category's roots are in grounding free-form LLM output against what an
embodied agent can actually do. Language Models as Zero-Shot Planners
projects plans onto admissible actions rather than trusting free text
{{arxiv:2201.07207}}, and Inner Monologue closes the loop by feeding
environment feedback back in as language {{arxiv:2207.05608}}. ReAct is the
point where "reasoning" and "acting" stopped being separate prompted calls
and became one interleaved loop {{arxiv:2210.03629}}. STaR is the origin
point for the self-improvement thread that Reflexion and its successors
build on: bootstrap reasoning from a handful of rationales plus
rationale-free data, then retrain on the successful chains
{{openreview:_3ELRdg2sgI}}.

## Open problems

**The self-correction disagreement above is unresolved, not settled by
volume of papers on one side.** Whether critique-and-revise helps or hurts
appears to depend on whether the feedback is externally grounded (tool
output, execution results) or purely the model's own introspection — the
corpus has strong papers on both sides and no entry reconciles them.

**Failure modes are now being catalogued rather than anecdotally reported.**
A 48,000-scenario study of cloud root-cause-analysis agents under both ReAct
and Plan-and-Execute derives a 16-category failure taxonomy, including
stalled, biased, and confused reasoning patterns {{arxiv:2601.22208}}. Alice
in Wonderland shows GPT-4, Claude 3 Opus, and other frontier models collapse
on simple grade-school word problems, with wildly inconsistent accuracy
across trivial rephrasings and confident wrong explanations that neither
chain-of-thought nor self-reevaluation fixes {{arxiv:2406.02061}}. Separately,
temporal awareness turns out to be orthogonal to reasoning ability —
deadlines have to be explicitly injected into context, a model doesn't infer
urgency from reasoning alone {{arxiv:2601.13206}}.

**Planning and web-use agents are a live security target through a channel
that isn't retrieval.** UReCoM manipulates a *benign user* into relaying
adversarial content inside their own request, bypassing prompt-injection
defenses better than five standard attack baselines — because agents
validate explicit malicious instructions far more reliably than adversarial
content embedded in otherwise-legitimate user text, a design flaw the
authors find across 12 commercial agents {{arxiv:2601.10758}}. See
[[safety-security-governance]] for the broader threat landscape.

*Editorial note:* several entries in this category remain `NEEDS-SOURCE` in
the corpus — pages behind IEEE/ACM, Wiley, or Nature paywalls, and
OpenReview pages that block automated fetches. They're omitted here rather
than summarized from title alone; check
`corpus/by-category/planning-and-reasoning.md` for the list.

## See also

- [[multi-agent]]
- [[safety-security-governance]]
- [[training-and-optimization]]
- [[surveys-and-foundations]]
- [[embodied-and-robotics]]
