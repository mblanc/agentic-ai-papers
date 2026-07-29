---
title: Harness Engineering
category: harness-engineering
status: draft
updated: 2026-07-28
---

## What it is

A harness is the code around a model that decides what it stores, retrieves,
sees, and is allowed to do — the agent loop, tool definitions, permissions,
memory, and control flow, as distinct from the model weights themselves.
Harness engineering is the discipline of designing and improving that layer
deliberately, on the premise that harness quality is often a bigger lever on
agent performance than model choice.

## State of the art

The load-bearing claim for this whole category, stated most concretely: a
production trends report finds harness configuration alone can swing
benchmark results by 5+ points {{url:https://resources.anthropic.com/hubfs/2026%20Agentic%20Coding%20Trends%20Report.pdf}}
(see [[coding-agents]]), and LangChain's own playbook for Nemotron 3 Ultra
demonstrates it directly — near-frontier performance from tuning the system
prompt, tool descriptions, and middleware, not the weights
{{url:https://blog.langchain.com/tuning-the-harness-not-the-model-a-nemotron-3-ultra-playbook}}.
Anthropic's own guidance for harness design is to lean on what the model
already does well and strip out harness assumptions as the model gets more
capable, reserving explicit constraints for security, cost, and UX
{{url:https://claude.com/blog/harnessing-claudes-intelligence}}.

**The dominant emerging trend is harnesses that improve themselves**, and the
entries here converge on a strikingly similar loop across independent teams:
mine failures from execution traces, propose a targeted harness change, and
accept it only if it survives held-out evaluation. Self-Harness runs exactly
this three-stage loop (Weakness Mining → Harness Proposal → Proposal
Validation) with no human engineer and no stronger external agent, lifting
held-out pass rates 15-21 points across three different base model families
{{arxiv:2606.09498}}. Meta-Harness generalizes the same idea to harness code
broadly, not just prompts, using an agentic proposer with filesystem access to
every prior candidate's traces, improving a state-of-the-art context-
management baseline by 7.7 points at 4x fewer tokens
{{arxiv:2603.28052}}. RHO (Retrospective Harness Optimization) pushes this
further — it improves the harness with *no ground-truth labels or validation
set at all*, learning purely from the agent's own past trajectories, and lifts
one reported SWE-Bench Pro run from 59% to 78%
{{gh:wbopan/retro-harness}}. Live-SWE-agent is the extreme version: an agent
that evolves its own scaffold *during* runtime while solving real problems,
starting from a bash-only baseline and reaching 77.4% on SWE-bench Verified
without test-time scaling, beating every existing software agent including
proprietary ones {{arxiv:2511.13646}}.

This has produced a small ecosystem of general-purpose harness optimizers as
products, not just papers: meta-agent {{gh:canvas-org/meta-agent}}, metaharness
{{gh:superagenticai/metaharness}}, auto-harness {{gh:neosigmaai/auto-harness}},
and harness-evolver {{gh:raphaelchristi/harness-evolver}} all implement some
version of propose-evaluate-keep against a fixed base model.

## Origin

Multi-Agent Collaboration is an early instance of naming the problems this
whole category exists to solve — looping issues, security risk, scalability,
and evaluation difficulty — while surveying Auto-GPT, BabyAGI, and Gorilla as
the first widely-used harnesses {{arxiv:2306.03314}}.

## Open problems

Harness design is still model-specific, and that's a scaling problem, not a
one-time cost: Self-Harness's own framing is that effective harness design is
inherently tied to a particular model's behavior, and as models proliferate
and rapidly evolve, hand-engineering a harness per model scales poorly
{{arxiv:2606.09498}} — which is precisely the argument for the self-improving
approaches above, but also means there's no single "correct" harness to
converge on, only ones fit to a specific model at a specific time.

*Editorial note:* the harness-engineering ecosystem visible in this corpus
consists overwhelmingly of small, fast-moving GitHub projects rather than
peer-reviewed work — treat tool-specific performance claims (e.g. token
reduction percentages) as vendor-reported unless independently verified. One
entry could not be summarized this pass (a 404'd blog post,
`NEEDS-SOURCE` in the corpus).

## See also

- [[context-engineering]]
- [[coding-agents]]
- [[observability-and-ops]]
