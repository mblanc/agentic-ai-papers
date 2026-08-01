---
title: Embodied and Robotics Agents
category: embodied-and-robotics
status: draft
updated: 2026-08-01
---

## What it is

Embodied agents ground an LLM, VLM, or learned policy in a physical or
simulated body — one that perceives an environment and acts within it,
rather than operating purely over text or a screen. This spans robot
manipulation, sim-to-real transfer, and open-ended game agents like
Minecraft's Voyager. Distinct from [[web-gui-computer-use]], which covers
agents acting on digital interfaces.

## State of the art

**LLM world knowledge supplies plans, not a trained-from-scratch policy.** A
large-enough pretrained LM can decompose "make breakfast" into "open fridge"
with zero task-specific training, provided a separate step maps each step
onto admissible actions {{url:https://proceedings.mlr.press/v162/huang22a.html}}.
The Interactive Agent Foundation Model pretrains one transformer jointly on
robotics trajectories, gameplay, video, and text so the same weights drive
an action-taking agent across robotics, gaming, and healthcare tasks
{{arxiv:2402.05929}}.

**Manipulation policies are converging on multi-task training from modest
demonstration counts.** RoboAgent trains one policy from 7,500
demonstrations using semantic augmentation and action chunking, evaluated
across 38 kitchen tasks, and generalizes to novel object-skill combinations
{{url:https://robopen.github.io/media/roboagent.pdf}}. SLAC instead pretrains
a latent action space in simulation before fine-tuning whole-body policies
with real-world RL {{url:https://cs.utexas.edu/~pstone/Papers/bib2html/b2hd-jiaheng_hu_2025.html}}.
NVIDIA pitches GR00T as a blueprint for generalist humanoid robotics
{{url:https://nvidia.com/en-us/robotics/groot-robot}} — vendor material, not
yet an independently benchmarked result in this corpus.

**Sim-to-real increasingly outsources tuning to an LLM.** Eureka has an LLM
write and evolve reward-function code that beats human-designed rewards on
dexterous manipulation {{url:https://eureka-research.github.io/}}; DrEureka
extends the same code-generation approach to domain-randomization configs
for transfer {{url:https://eureka-research.github.io/dr-eureka}}. That's not
the only route to superhuman control, though: GT Sophy beat champion human
drivers in Gran Turismo with model-free RL and no LLM in the loop at all
{{url:https://nature.com/articles/s41586-021-04357-7}}.

**Visual tracking under failure works by keeping a VLM idle until something
breaks.** It sits out during normal tracking and is invoked only on failure
detection, with a memory-augmented self-reflection loop learning from past
recoveries — lifting success rates 72% over RL-based trackers and 220% over
PID-based ones {{arxiv:2505.20718}}. VirtualEnv, an Unreal Engine 5 platform
for navigation and manipulation benchmarks, is infrastructure for testing
claims like this one rather than a method itself {{arxiv:2601.07553}}.

## Origin

Voyager originates the open-ended, Minecraft-style line of this category: a
GPT-4-driven agent that writes and stores executable code as skills, picks
its own goals via a novelty-seeking curriculum, and self-corrects on game
feedback with no human in the loop. It discovers 3.3x more unique items and
unlocks the wooden tech tier 15.3x faster than AutoGPT/ReAct/Reflexion
baselines, with skills that transfer to new worlds
{{url:https://voyager.minedojo.org/}}. The zero-shot planning result above is
the origin of the separate, non-Minecraft line grounding LLM plans in
executable actions {{url:https://proceedings.mlr.press/v162/huang22a.html}}.

## Open problems

A survey of 2,000+ papers argues the field's missing piece is spatial
intelligence — perceiving 3D structure and acting under physical
constraints, distinct from linking images to language — proposing a
three-axis taxonomy and six open challenges including hierarchical memory,
GNN-LLM integration, and world models {{arxiv:2602.01644}}. That tracks with
what the rest of this page shows empirically: every entry pairs
general-purpose LLM/VLM reasoning with an explicit grounding, fallback, or
simulation-pretraining mechanism — none claims an LLM acts embodied
unassisted.

*Editorial note:* this category is small (12 entries); treat "state of the
art" above as a curated sample, not a survey of the field.

## See also

- [[web-gui-computer-use]]
- [[planning-and-reasoning]]
- [[simulation-and-social]]
- [[training-and-optimization]]
