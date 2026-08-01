---
title: Web, GUI, and Computer-Use Agents
category: web-gui-computer-use
status: draft
updated: 2026-08-01
---

## What it is

This covers agents that act on digital interfaces built for humans —
browsers, desktop screens, mobile apps — by perceiving and
clicking/typing rather than calling a structured API. Distinct from
[[embodied-and-robotics]], which acts in a physical or simulated world.

## State of the art

**The category splits into automation and testing, two different uses of
the same underlying capability.** For automation, Anthropic's computer-use
reference implementation shows the core pattern: a Dockerized Linux
desktop, an agent loop, and defined computer-use tools operating over
X11/VNC {{gh:anthropics/anthropic-quickstarts}}. browser-use generalizes
this to browsers specifically, letting an LLM click, type, and navigate
like a person across form-filling, extraction, and QA tasks across model
providers {{gh:browser-use/browser-use}}, and bux packages the same
capability as an always-on VPS service with persistent logged-in sessions
and a Telegram control channel, explicitly positioned against brittle
credential-stuffing {{gh:browser-use/bux}}.

For testing, the same navigation capability is turned toward finding
defects instead of completing tasks — a harder problem than it sounds,
because a GUI-navigating agent's default incentive is to finish the task,
not report anomalies along the way. GUITester names this precisely as
"Goal-Oriented Masking" (agents prioritize completing tasks over
reporting what they notice) and "Execution-Bias Attribution"
(misattributing real system bugs to agent error), and addresses both by
decoupling navigation from verification into separate modules, reaching
48.90% F1 (Pass@3) on a new benchmark against a 33.35% prior-baseline
{{arxiv:2601.04500}}. CovAgent applies a related agentic approach to a
narrower, harder problem in mobile: breaking past the roughly 30%
activity-coverage ceiling in Android testing by reasoning over decompiled
Smali code and the transition graph to infer *why* an activity is
unreachable, then generating instrumentation to satisfy the activation
condition directly — up to 179.7% more activity coverage than the
strongest prior baseline tested {{arxiv:2601.21253}}.

**Underneath both uses sits the grounding question: can a model actually
see and target the right screen element.** ShowUI is a lightweight (2B
parameter) vision-language-action model built for this, using a
UI-connected graph to drop redundant screenshot tokens and interleaving
vision/language/action, reaching 75.1% zero-shot screenshot grounding
while cutting roughly a third of visual tokens
{{url:https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html}}.
AGUVIS takes a related but distinct position on the same question: a pure
vision approach with no dependence on the accessibility tree at all
{{arxiv:2412.04454}} — an explicit bet that accessibility-tree parsing,
which is unreliable across real-world apps, isn't worth building around
even as a fallback.

**Training data for GUI agents is itself becoming an agentic problem
rather than a static-dataset one.** Learning with Challenges profiles a
mobile-GUI agent's own capability frontier — along trajectory length and
task goal difficulty — and generates training trajectories matched to
that frontier, improving performance 1.57x over prior data-generation
methods {{arxiv:2601.22781}}. This treats "what training data should this
agent see next" as an adaptive, agent-specific question, not a fixed
curriculum.

## Origin

WebGPT is the ancestor of this whole line: a browsing agent trained first
by imitation and then by preference optimization, which is also the
direct ancestor of today's "deep research" agents {{arxiv:2112.09332}}.
The RCI prompting approach is a distinct early lineage worth noting
separately: rather than any training at all, it has an agent recursively
critique and improve its own output to drive computer tasks from natural
language, reaching state-of-the-art on MiniWoB++ with a handful of
demonstrations per task instead of the tens of thousands of examples
supervised/RL approaches needed, and no task-specific reward function
{{openreview:M6OmjAZ4CX}}. WorkArena grounded the field in a harder,
more realistic benchmark shortly after — common knowledge-work tasks on a
real enterprise platform rather than a toy simulated site
{{arxiv:2403.07718}}, itself a step up from the earlier WebShop simulated
e-commerce benchmark {{arxiv:2207.01206}}.

## Open problems

75.1% zero-shot grounding accuracy
{{url:https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html}}
means roughly one in four targeting decisions is still wrong before any
downstream task logic even runs — visual grounding, not planning, remains
the binding constraint for many computer-use tasks. On the testing side,
correctly separating "the agent made a mistake" from "the app under test
is actually broken" is still an open, largely unsolved attribution
problem, by GUITester's own framing as one of two core blockers to
autonomous exploratory testing {{arxiv:2601.04500}}. And on mobile
specifically, even CovAgent's large relative gains still start from a
roughly 30% coverage floor {{arxiv:2601.21253}} — the underlying
reachability problem is mitigated, not solved.

## See also

- [[embodied-and-robotics]]
- [[coding-agents]]
- [[evaluation-and-benchmarks]]
