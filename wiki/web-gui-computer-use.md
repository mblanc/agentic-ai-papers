---
title: Web, GUI, and Computer-Use Agents
category: web-gui-computer-use
status: draft
updated: 2026-07-28
---

## What it is

This covers agents that act on digital interfaces built for humans — browsers,
desktop screens, and mobile apps — by seeing and clicking/typing rather than
calling a structured API. Distinct from [[embodied-and-robotics]], which acts
in a physical or simulated world.

## State of the art

The category splits into two genuinely different uses of the same underlying
capability. The first is **automation**: driving a real interface to get a
task done. Anthropic's computer-use reference implementation shows the core
pattern — a Dockerized desktop, an agent loop, and defined computer-use tools
over X11/VNC {{gh:anthropics/anthropic-quickstarts}}; browser-use generalizes
this to web browsers specifically, letting an LLM click, type, and navigate
like a person across form-filling, extraction, and QA tasks
{{gh:browser-use/browser-use}}, with bux packaging it as an always-on VPS
service with persistent logged-in sessions {{gh:browser-use/bux}}.

The second use is **testing**: turning the same navigation capability toward
finding defects rather than completing tasks. This is a harder problem than it
looks, because a GUI-navigating agent's default incentive is to complete the
task, not report anomalies along the way. GUITester names this precisely as
"Goal-Oriented Masking" and "Execution-Bias Attribution" (misattributing real
system bugs to agent error), and addresses both by decoupling navigation from
verification into separate modules, reaching 48.90% F1 against a 33.35%
baseline on a new benchmark built for the task {{arxiv:2601.04500}}. CovAgent
applies a related agentic approach to a narrower, harder problem — breaking
past the ~30% activity-coverage ceiling in Android testing by reasoning about
*why* an activity is unreachable from decompiled code, then generating
instrumentation to satisfy the activation condition directly
{{arxiv:2601.21253}}.

Underneath both uses sits the grounding question: can a model actually see and
target the right screen element. ShowUI is a lightweight (2B) vision-language-
action model purpose-built for this, using a UI-connected graph to drop
redundant screenshot tokens, and reaches 75.1% zero-shot screenshot grounding
{{url:https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html}}.

## Origin

WebGPT is the ancestor of this whole line: a browsing agent trained first by
imitation, then by preference optimization, which is also the direct ancestor
of today's "deep research" agents {{arxiv:2112.09332}}.

## Open problems

75.1% zero-shot grounding accuracy {{url:https://openaccess.thecvf.com/content/CVPR2025/html/Lin_ShowUI_One_Vision-Language-Action_Model_for_GUI_Visual_Agent_CVPR_2025_paper.html}}
means roughly one in four targeting decisions is still wrong before any
downstream task logic runs — visual grounding, not planning, remains the
binding constraint for many computer-use tasks. On the testing side,
correctly separating "the agent made a mistake" from "the app under test is
actually broken" is still an open, largely unsolved attribution problem, per
GUITester's own framing of it as one of two core blockers to autonomous
exploratory testing {{arxiv:2601.04500}}.

## See also

- [[embodied-and-robotics]]
- [[coding-agents]]
