# training-and-optimization

36 entries.

## Timeline

30 dated entries, oldest first.

- [Self-Evolution Learning for Discriminative Language Model Pretraining](https://aclanthology.org/2023.findings-acl.254.pdf) · 2023
  - `acl:2023.findings-acl.254.pdf` · cited by 1: LJ
  - summary: Masks tokens by their informativeness rather than randomly, adding a Token-specific Label Smoothing step so masked-language pretraining focuses learning on under-explored tokens instead of uniformly random ones, improving 10 downstream tasks by 1.4-2.1 points on average across different pretrained models.

- [WizardLM: Empowering Large Language Models to Follow Complex Instructions](https://arxiv.org/abs/2304.12244) · 2023-04
  - `arxiv:2304.12244` · cited by 1: ZJ
  - summary: Uses an LLM (Evol-Instruct) to automatically rewrite simple instructions into progressively harder ones instead of hand-authoring complex training data, and the resulting fine-tuned model beats ChatGPT on human-judged high-complexity instructions.

- [SELFEVOLVE: A Code Evolution Framework via Large Language Models](https://arxiv.org/pdf/2306.02907) · 2023-06
  - `arxiv:2306.02907` · cited by 1: LJ
  - summary: Two-step knowledge-provider then self-reflective-programmer pipeline.

- [Motif: Intrinsic Motivation from Artificial Intelligence Feedback](https://arxiv.org/pdf/2310.00166) · 2023-10
  - `arxiv:2310.00166` · cited by 1: LJ
  - summary: Motif turns an LLM's preferences over pairs of game-state captions into an intrinsic RL reward without the LLM ever touching the environment, and on NetHack, chasing that reward alone beats an agent trained to directly maximize score.

- [Self-Evolved Diverse Data Sampling for Efficient Instruction Tuning](https://arxiv.org/pdf/2311.08182) · 2023-11
  - `arxiv:2311.08182` · cited by 1: LJ
  - summary: Self-evolving selection for label-efficient instruction tuning.

- [Self-Rewarding Language Models](https://arxiv.org/pdf/2401.10020) · 2024-01
  - `arxiv:2401.10020` · cited by 1: LJ
  - summary: Self-Rewarding Language Models use the model itself as an LLM-as-judge to generate its own DPO training signal, and three rounds of this loop on Llama 2 70B beats Claude 2, Gemini Pro, and GPT-4 0613 on AlpacaEval 2.0 while also sharpening the model's own judging ability.

- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/pdf/2404.14387) · 2024-04
  - `arxiv:2404.14387` · cited by 1: LJ
  - summary: Four-phase framework; the entry point for this whole category.

- [Interactive Evolution: A Neural-Symbolic Self-Training Framework For Large Language Models](https://arxiv.org/abs/2406.11736) · 2024-06
  - `arxiv:2406.11736` · cited by 1: ZJ
  - summary: Self-training loop where feedback from the task environment filters an LLM's own generated symbolic-reasoning trajectories, letting it improve on neural-symbolic tasks without relying on scarce human-annotated symbolic data.

- [Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy](https://arxiv.org/abs/2407.06813) · 2024-07
  - `arxiv:2407.06813` · cited by 1: LJ
  - summary: Strategic planning plus self-play evolution without human intervention.

- [Reinforcement Learning for Long-Horizon Interactive LLM Agents](https://arxiv.org/abs/2502.01600) · 2025-02
  - `arxiv:2502.01600` · cited by 1: ZJ
  - summary: RL directly on long-horizon interactive tasks.

- [ATLaS: Agent Tuning via Learning Critical Steps](https://arxiv.org/abs/2503.02197) · 2025-03
  - `arxiv:2503.02197` · cited by 1: LJ
  - summary: Tunes only on critical expert-trajectory steps, cutting cost.

- [Group-in-Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2505.10978) · 2025-05
  - `arxiv:2505.10978` · cited by 1: ZJ
  - related: <https://github.com/langfengQ/verl-agent>
  - summary: GiGPO: hierarchical grouping for credit assignment in agent RL.

- [SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution](https://arxiv.org/abs/2505.20732) · 2025-05
  - `arxiv:2505.20732` · cited by 1: ZJ
  - related: <https://github.com/WangHanLinHenry/SPA-RL-Agent>
  - summary: Attributes final reward to intermediate steps as progress.

- [Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning](https://arxiv.org/abs/2505.03792) · 2025-05
  - `arxiv:2505.03792` · cited by 1: ZJ
  - related: <https://github.com/langfengQ/CoSo>
  - summary: Fixes RL exploration for VLM agents by using counterfactual reasoning to figure out which tokens in a generated action actually matter causally, then focusing exploration there instead of treating every token equally — improves sample efficiency and performance on Android control, card games, and embodied tasks.

- [EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle](https://arxiv.org/abs/2510.16079) · 2025-10
  - `arxiv:2510.16079` · cited by 1: LJ
  - summary: Distills past runs into abstract principles that guide later decisions.

- [In-the-Flow Agentic System Optimization for Effective Planning and Tool Use](https://arxiv.org/abs/2510.05592) · 2025-10
  - `arxiv:2510.05592` · cited by 1: ZJ
  - summary: Optimizes planning and tool use inside the running system.

- [AgentDevel: Reframing Self-Evolving LLM Agents as Release Engineering](https://arxiv.org/pdf/2601.04620v1) · 2026-01
  - `arxiv:2601.04620` · cited by 1: VA
  - summary: Treats a self-evolving agent like a software release, with a critic that diagnoses failures from the outside and a gate that prioritizes non-regression over raw score, replacing unstable population search or in-agent self-refinement with a single auditable version line.

- [ArenaRL: Scaling RL for Open-Ended Agents via Tournament-based Relative Ranking](https://arxiv.org/pdf/2601.06487v2) · 2026-01
  - `arxiv:2601.06487` · cited by 1: VA
  - summary: Replaces pointwise reward scoring (which collapses subtle trajectory differences into noise) with intra-group tournament ranking for RL on open-ended agent tasks, matching full pairwise-comparison accuracy at linear instead of quadratic cost.

- [ARM: Role-Conditioned Neuron Transplantation for Training-Free Generalist LLM Agent Merging](https://arxiv.org/pdf/2601.07309v1) · 2026-01
  - `arxiv:2601.07309` · cited by 1: VA
  - summary: ARM merges several environment-specialist LLM agents into one generalist by transplanting neurons based on role-specific activation patterns instead of retraining, beating both existing merge methods and the original specialists on cross-domain tasks without any gradient updates.

- [AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement](https://arxiv.org/pdf/2601.22758v1) · 2026-01
  - `arxiv:2601.22758` · cited by 1: VA
  - summary: Extracts reusable 'Experience Patterns' from an agent's task history as both specialized subagents (procedural knowledge) and skill snippets (static knowledge), with automatic pruning to stop the pattern repository degrading, beating hand-designed systems on TravelPlanner (27.1% vs 12.1%).

- [EnvScaler: Scaling Tool-Interactive Environments for LLM Agent via Programmatic Synthesis](https://arxiv.org/pdf/2601.05808v1) · 2026-01
  - `arxiv:2601.05808` · cited by 1: VA
  - summary: EnvScaler auto-generates training environments for tool-using agents at scale — 191 environment skeletons and ~7,000 validated task scenarios via its SkelBuilder/ScenGenerator pipeline — and using them to SFT+RL Qwen3 models gives a solid boost on multi-turn, multi-tool benchmarks without the hallucination and access problems of hand-built or LLM-simulated sandboxes.

- [JitRL: Just-In-Time Reinforcement Learning for Continual Learning in LLM Agents Without Gradient Updates](https://arxiv.org/pdf/2601.18510v1) · 2026-01
  - `arxiv:2601.18510` · cited by 1: VA
  - summary: Adapts a deployed LLM agent at test time with no gradient updates by retrieving similar past trajectories to estimate action advantages and directly modulating output logits, proven to be the closed-form solution of KL-constrained policy optimization, beating full fine-tuning at 30x lower cost.

- [No More Stale Feedback: Co-Evolving Critics for Open-World Agent Learning](https://arxiv.org/pdf/2601.06794v1) · 2026-01
  - `arxiv:2601.06794` · cited by 1: VA
  - summary: ECHO jointly evolves an RL agent's policy and its natural-language critic in a synchronized loop instead of using a static offline critic, using saturation-aware gain shaping to keep learning going past plateaus, yielding more stable training and better long-horizon success in open-world environments.

- [OpenTinker: Separating Concerns in Agentic Reinforcement Learning](https://arxiv.org/pdf/2601.07376v1) · 2026-01
  - `arxiv:2601.07376` · cited by 1: VA
  - summary: An infrastructure for running many LoRA-backed agent policies over shared compute, treating adapters as live policy states (not static artifacts) so SFT, RL, rollout, and multi-turn training can share a base model while keeping each adapter's checkpoints and gradients isolated.

- [Paying Less Generalization Tax: A Cross-Domain Generalization Study of RL Training for LLM Agents](https://arxiv.org/pdf/2601.18217v1) · 2026-01
  - `arxiv:2601.18217` · cited by 1: VA
  - summary: Finds environment realism matters less for cross-domain agent generalization than state richness and planning complexity (Sokoban transfers better than the more realistic ALFWorld), and that step-by-step thinking during RL preserves generalization better than SFT warmup alone.

- [PRISM: Disentangling SFT and RL Data via Gradient Concentration](https://arxiv.org/pdf/2601.07224v1) · 2026-01
  - `arxiv:2601.07224` · cited by 1: VA
  - summary: Routes each training example to SFT or RL based on how much it conflicts with the model's existing knowledge (measured via gradient concentration), since consolidation and structural adaptation need different training regimes, cutting compute up to 3.22x over hybrid baselines.

- [Textual Equilibrium Propagation for Deep Compound AI Systems](https://arxiv.org/pdf/2601.21064v2) · 2026-01
  - `arxiv:2601.21064` · cited by 1: VA
  - summary: TEP replaces global textual-gradient backprop through compound LLM pipelines, which explodes or vanishes with depth, with local equilibrium-propagation-style prompt refinement, beating TextGrad's accuracy and efficiency with gains that grow as the pipeline gets deeper.

- [Towards AGI A Pragmatic Approach Towards Self Evolving Agent](https://arxiv.org/pdf/2601.11658v1) · 2026-01
  - `arxiv:2601.11658` · cited by 1: VA
  - summary: A hierarchical multi-agent framework where a stuck agent escalates to synthesizing new tools, then to full evolution via curriculum learning, RL, or genetic algorithms depending on failure severity, with each evolution strategy suited to a different difficulty regime.

- [Trajectory Guard: A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI](https://arxiv.org/pdf/2601.00516v1) · 2026-01
  - `arxiv:2601.00516` · cited by 1: VA
  - summary: A Siamese recurrent autoencoder that jointly detects 'wrong plan for the task' and 'malformed plan structure' in agent trajectories via contrastive plus reconstruction loss, hitting 0.88-0.94 F1 at 32ms latency, 17-27x faster than an LLM-judge baseline.

- [TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents](https://arxiv.org/pdf/2602.06443v1) · 2026-02
  - `arxiv:2602.06443` · cited by 1: VA
  - summary: Runtime verifier locating trajectory errors for precise rollback-and-retry.

## Tools & Undated

6 entries with no date derivable from their source (GitHub repos, blog posts, etc.).

- [ADAS](https://github.com/ShengranHu/ADAS)
  - `gh:shengranhu/adas` · cited by 1: KY
  - summary: Runs a meta-agent that iteratively invents and codes new agent architectures in Python, then tests them, searching for designs that beat hand-built baselines on held-out agentic benchmarks (ICLR 2025).

- [AlphaFlow: autonomous discovery and optimization of multi-step chemistry using a self-driven fluidic lab guided by reinforcement learning](https://www.nature.com/articles/s41467-023-37139-y)
  - `url:https://nature.com/articles/s41467-023-37139-y` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [CollosalAI Chat](https://github.com/hpcaitech/ColossalAI/tree/main/applications/Chat)
  - `gh:hpcaitech/colossalai` · cited by 1: KY
  - summary: ColossalChat, the applications/Chat piece of ColossalAI, is an open reproduction of the ChatGPT RLHF pipeline - supervised fine-tuning, reward-model training and PPO - built on ColossalAI's distributed-training backend.

- [CREAM: Consistency Regularized Self-Rewarding Language Models](https://openreview.net/pdf?id=Vf6RDObyEF)
  - `openreview:Vf6RDObyEF` · cited by 1: LJ
  - summary: CREAM fixes the problem that self-rewarding LLMs (same model as both policy and judge) accumulate reward bias and stall after a few iterations, by regularizing training on how consistent a response's reward is across iterations so the model learns from the preference pairs it can actually trust.

- [Evolutionary optimization of model merging recipes](https://www.nature.com/articles/s42256-024-00975-8)
  - `url:https://nature.com/articles/s42256-024-00975-8` · cited by 1: LJ
  - summary: Evolves which layers and weights to merge from existing open models instead of hand-tuning the recipe, producing a Japanese math model that beats 70B-parameter baselines without any additional training.

- [LANGUAGE MODEL SELF-IMPROVEMENT BY REIN- FORCEMENT LEARNING CONTEMPLATION](https://openreview.net/pdf?id=38E4yUbrgr)
  - `openreview:38E4yUbrgr` · cited by 1: LJ
  - summary: SIRLC has an LLM play both student (generate an answer) and teacher (score it) on unlabeled questions, then trains the model with RL to raise its own evaluation scores — no external labels needed, since judging text turns out to be easier for the model than generating it.
