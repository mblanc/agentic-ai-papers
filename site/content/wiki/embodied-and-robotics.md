---
title: Embodied and Robotics Agents
category: embodied-and-robotics
status: draft
updated: 2026-07-28
---

## What it is

Embodied agents ground an LLM or VLM's reasoning in a physical or simulated
body — one that perceives an environment and acts within it, rather than
operating purely over text or a screen. This is distinct from
[[web-gui-computer-use]], which covers agents acting on digital interfaces.

## State of the art

The foundational move here is treating an LLM's world knowledge as a source of
*plans* that then need grounding in what's actually executable, not as
something an environment-specific policy has to be trained from scratch. A
large-enough pretrained LM can decompose "make breakfast" into "open fridge"
with no additional training, provided a separate step maps the resulting plan
onto admissible actions [url:https://proceedings.mlr.press/v162/huang22a.html](https://proceedings.mlr.press/v162/huang22a.html).
That grounding gap is closed further by fine-tuning on embodied experience
gathered inside a physical-world simulator — using elastic weight
consolidation plus LoRA to add object-permanence and planning skill without
erasing general language ability, enough for a 1.3B model to match ChatGPT on
several downstream tasks [arxiv:2305.10626](https://arxiv.org/abs/2305.10626.pdf).

More recent work pushes the same "reason, then fall back" pattern into visual
tracking: a vision-language model sits idle during normal tracking and is
invoked only on failure detection, with a memory-augmented self-reflection
loop letting it learn from past recoveries, boosting success rates 72-220%
over RL- and PID-based trackers [arxiv:2505.20718](https://arxiv.org/abs/2505.20718).

## Origin

The zero-shot planning result is the origin point for this whole line of work
— it's the first clean demonstration that an LLM's world knowledge transfers
to embodied action without task-specific training
[url:https://proceedings.mlr.press/v162/huang22a.html](https://proceedings.mlr.press/v162/huang22a.html).

## Open problems

*Editorial note, not a corpus finding:* this category is thin in the current
corpus (four entries), so treat "state of the art" above as a sample of what's
been curated, not a survey of the field. What the entries here do establish
concretely: general-purpose LLM/VLM reasoning still needs an explicit grounding
or fallback mechanism to be reliable in a physical loop — none of the papers
here claim an LLM can act embodied unassisted.

## See also

- [[web-gui-computer-use]]
- [[planning-and-reasoning]]
