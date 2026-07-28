---
title: Frameworks and SDKs
category: frameworks-and-sdks
status: draft
updated: 2026-07-28
---

## What it is

General-purpose libraries and SDKs for building agents — the layer that
provides orchestration, tool-calling plumbing, and composition primitives, as
opposed to a single-purpose harness built for one task. Overlaps with
[[harness-engineering]] where a framework's opinions become a specific
product's execution loop.

## State of the art

There's no consensus architecture, and the disagreement is informative rather
than a gap to be closed. LangChain remains the dominant, broadly-adopted
option, standardizing model access and tool integration with built-in
monitoring {{gh:langchain-ai/langchain}}. smolagents takes the opposite bet —
minimal code-writing agents in very few lines, explicitly trading
comprehensiveness for simplicity {{gh:huggingface/smolagents}}. AgentForge
argues the cost of frameworks like LangChain is architectural rigidity and
complexity, and reports 62% less development time from a composable-skill,
declarative-YAML alternative {{arxiv:2601.13383}} — a claim worth reading as
one team's benchmark, not a settled comparison.

A more foundational critique comes from outside the "which framework" debate
entirely: Agentic Design Patterns argues most framework taxonomies are
convenience-based rather than grounded in systems theory, and derives 12
reusable patterns from decomposing an agent into five interacting subsystems
(reasoning, perception, action, learning, communication), demonstrating the
approach by identifying structural gaps in ReAct itself {{arxiv:2601.19752}}.

Domain-specific frameworks are also emerging rather than everything
converging on one general tool: InfiAgent externalizes state to a file-centric
workspace specifically to keep long-horizon reasoning context bounded
{{arxiv:2601.03204}}, and OS-Symphony is purpose-built for computer-use agents,
pairing milestone-driven reflection memory with live tutorial synthesis for
unseen applications {{arxiv:2601.07779}}.

## Origin

LangChain is the earliest and most widely adopted framework in this space, and
the one most later frameworks position themselves against, whether by
composing on it (Open SWE, see [[coding-agents]]) or explicitly rejecting its
complexity (AgentForge, smolagents) {{gh:langchain-ai/langchain}}.

## Open problems

Project Ariadne's finding cuts across every framework in this category, not
just one: chain-of-thought traces can be "Reasoning Theater" — an agent
reaches the same conclusion regardless of contradictory internal logic, with
violation density up to 0.77 in factual and scientific domains
{{arxiv:2601.02314}}. Any framework whose observability or debugging story
leans on inspecting the reasoning trace is, per this finding, potentially
inspecting a rationalization rather than the actual decision process — a
problem no framework here currently claims to solve.

## See also

- [[harness-engineering]]
- [[multi-agent]]
- [[planning-and-reasoning]]
