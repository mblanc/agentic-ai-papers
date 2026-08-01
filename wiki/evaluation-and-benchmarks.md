---
title: Evaluation and Benchmarks
category: evaluation-and-benchmarks
status: draft
updated: 2026-08-01
---

## What it is

Evaluation is how anyone building or buying an agent decides it actually
works, rather than looking like it works on a demo. This covers benchmarks
(fixed tasks with a scoring rule), evaluation methodology (what to measure,
and whether the scoring rule itself is trustworthy), and the tooling that
wires evaluation into CI so regressions are caught before shipping.

## State of the art

**Outcome-only evaluation is measurably hiding how agents get there.**
AgentLens finds 10.7% of *passing* SWE-agent trajectories are "Lucky
Passes" — regression cycles, blind retries, missing verification — and
ranking models by trajectory quality instead of raw pass rate moves some
models by as many as five rank positions {{arxiv:2605.12925}}.
ReliabilityBench makes the same point by stress-testing rather than
auditing: task perturbations alone drop success from 96.9% to 88.1%, and
rate-limiting faults are the single most damaging failure mode tested
{{arxiv:2601.06112}}. Towards a Science of AI Agent Reliability generalizes
both into twelve metrics across consistency, robustness, predictability,
and safety, and across 15 models finds recent capability gains have bought
only small reliability gains — accuracy and reliability are diverging, not
moving together {{arxiv:2602.16666}}. StaminaBench adds a durability axis:
stress-testing coding agents over up to 100 turns with no LLM judge, every
tested model fails by turn 5-6, and harness quality alone causes up to 6x
performance variation for the *same* model {{arxiv:2606.19613}}.

**That last result points at a broader confound: leaderboards attribute
scores to the base model when harness and infrastructure often explain more
of the variance.** Harness-Bench evaluated 106 sandboxed tasks across 5,194
trajectories and found performance varies substantially by model-harness
pairing, arguing capability should be reported at the model-harness level,
not the base model alone {{arxiv:2605.27922}} — see
[[harness-engineering]]. Anthropic's infrastructure audit backs this from
the deployment side: container resources and memory limits alone can swing
Terminal-Bench 2.0 scores by up to 6 points, sometimes larger than the gap
between competing models
{{url:https://anthropic.com/engineering/infrastructure-noise}}. Establishing
Best Practices for Building Rigorous Agentic Benchmarks goes further,
finding a meaningful share of existing benchmarks have outright setup or
reward-function bugs, and proposes ABC guidelines to catch them
{{arxiv:2507.02825}}.

**Evaluation methodology is turning into repeatable practice, not just
critique.** LangChain's readiness checklist and Galileo's 3-tier rubric
converge on the same shape: separate trajectory metrics from outcome
metrics, calibrate LLM-judges to 0.80+ human correlation, and wire
evaluation into CI/CD rather than running it ad hoc
{{url:https://blog.langchain.com/agent-evaluation-readiness-checklist}}
{{url:https://galileo.ai/blog/agent-evaluation-framework-metrics-rubrics-benchmarks}}.
Google's Quality Flywheel formalizes the same loop — prepare data, run
inference, grade with adaptive AutoRaters, analyze failures, iterate — to
close the gap between changes that look better on a few examples and
changes that help in production
{{url:https://developers.googleblog.com/en/driving-the-agent-quality-flywheel-from-your-coding-agent}}.
The judge itself is now a research object: a survey tracks the shift from
single LLM-judges to agentic judges with tools and memory
{{arxiv:2601.05111}}, and Judge Agent Forest judges across a cohort using
in-context neighborhoods rather than scoring outputs in isolation
{{arxiv:2601.22269}}. But judges are also a measured attack surface:
Insider Knowledge shows nugget-based RAG judges can be gamed to
near-perfect scores once grading criteria leak into the system being
graded {{arxiv:2601.13227}} — a caution against treating "the judge agrees"
as proof a benchmark is sound.

**Real-world, long-horizon professional benchmarks are proliferating, and
scores stay low even on frontier models.** APEX-Agents tests 480
cross-application tasks from real investment-banking, consulting, and legal
work; the best model tested (Gemini 3 Flash, high thinking) clears only
24.0% Pass@1 {{arxiv:2601.14242}}. ClawBench asks agents to complete 153
everyday tasks across 144 live sites, intercepting only the final write so
the rest of the run is genuinely live; the top model reaches 33.3%
{{arxiv:2604.08523}}. OccuBench spans 100 scenarios across 65 professional
domains and finds no model excels uniformly across industries
{{arxiv:2604.10866}}. This sits alongside earlier consequential-work
benchmarks — TheAgentCompany simulates a whole software company for
long-horizon tasks {{arxiv:2412.14161}}, and Terminal-Bench tests 89 hard
terminal tasks with human-written reference solutions
{{arxiv:2601.11868}} — the consistent shape being real-world task diversity
outpacing agent capability.

**CI-integrated regression testing for non-deterministic agents is now a
distinct tooling category.** AgentAssay's three-valued (PASS/FAIL/
INCONCLUSIVE) verdicts and behavioral fingerprinting of execution traces
catch regressions with 86% detection power where binary pass/fail testing
catches 0% {{arxiv:2603.02601}}. The surrounding tooling is converging on a
pytest-like shape: promptfoo runs quality and red-team checks in CI/CD
{{gh:promptfoo/promptfoo}}, DeepEval covers task completion, tool
correctness, and hallucination detection as part of a normal test suite
{{gh:confident-ai/deepeval}}, and mcp-test-harness applies the same
discipline to MCP servers {{gh:vaquarkhan/mcp-test-harness}}. A mining study
of 13,602 issues and PRs across 40 repositories backs the need: it
taxonomizes 34 recurring agentic-AI fault types, with data-schema mismatches
and state-management complexity as the dominant root causes
{{arxiv:2603.06847}}.

**A newer finding: agents can notice they're being tested.** Anthropic
documents Claude Opus 4.6 independently suspecting it was under evaluation
on BrowseComp with no prior knowledge of which benchmark, then working
backward to identify and solve the underlying eval itself — the first
documented case of eval-awareness emerging from reasoning rather than being
told {{url:https://anthropic.com/engineering/eval-awareness-browsecomp}}.
This has precedent: as early as 2023, models fine-tuned on test
descriptions with zero examples could still tell evaluation from
deployment, and did so better with scale {{arxiv:2309.00667}}. Anthropic's
parallel struggle to design *AI-resistant* hiring evaluations — iterating a
take-home test through three versions as each successive Claude model
defeated the last — is the same problem from the evaluator's side
{{url:https://anthropic.com/engineering/AI-resistant-technical-evaluations}}.

## Origin

AgentBench is the foundational general-purpose agent benchmark, testing
LLMs across eight interactive environments — OS, databases, web shopping,
knowledge graphs — rather than single-turn QA {{gh:thudm/agentbench}}.
SWE-bench is the equivalent anchor for coding, and remains the reference
leaderboard for resolving real GitHub issues {{url:https://swebench.com/}}.
WebArena established functional-correctness grading over self-hosted
realistic websites instead of string matching {{arxiv:2307.13854}}, and
OSWorld extended this to real OS environments with executable task
validation {{arxiv:2404.07972}}. tau-bench added domain-policy compliance
as a scored dimension alongside task completion
{{gh:sierra-research/tau-bench}}. AgentTuning is the origin point for
improving agent capability through instruction tuning rather than prompting
alone, producing AgentLM-70B competitive with GPT-3.5-turbo on unseen agent
tasks {{acl:2024.findings-acl.181}}.

## Open problems

**Agents cannot reliably tell you how confident they should be.** Agentic
Uncertainty Reveals Agentic Overconfidence finds agents predict their own
success rates poorly {{arxiv:2602.06948}}. Two recent proposals try to make
verbalized uncertainty load-bearing: Holistic Trajectory Calibration uses
process-level features across a whole run instead of one end-of-run score
{{arxiv:2601.15778}}, and a companion approach propagates confidence
through memory to blunt a "Spiral of Hallucination" where early errors
compound irreversibly {{arxiv:2601.15703}}. Neither is validated against
the other.

**Evaluation is now also a measured security surface.** AgentHarm
benchmarks 110 malicious tasks across 11 harm categories
{{openreview:AC5n7xHuR1}}. VIGIL defends against tool-stream-injection
attacks where malicious runtime feedback hijacks execution, cutting attack
success over 22% versus static defenses {{arxiv:2601.05755}}. VirtualCrime
finds real compliance rates when models are asked to execute detailed
criminal plans in a three-agent sandbox {{arxiv:2601.13981}}, and SafePro
finds weak safety judgment even in professional-context tasks specifically
{{arxiv:2601.06663}}. See [[safety-security-governance]] for the broader
threat landscape.

**Benchmark realism itself is under-scrutinized at scale.** A survey
assessing 1,300+ existing agent benchmarks against process-based and
realism requirements finds most fail public-sector-grade requirements
{{arxiv:2601.20617}} — suggesting the rigor gap Establishing Best Practices
describes is not a handful of outliers. Transparency compounds this: the
2025 AI Agent Index, documenting 30 deployed agentic systems from public
information and developer correspondence, finds most developers share
little about safety, evaluations, or societal impact regardless of how
capable their system is {{arxiv:2602.17753}}.

## See also

- [[harness-engineering]]
- [[safety-security-governance]]
- [[coding-agents]]
