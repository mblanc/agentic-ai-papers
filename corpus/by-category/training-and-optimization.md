# training-and-optimization

24 entries.

## Timeline

23 dated entries, oldest first.

- [Self-Evolution Learning for Discriminative Language Model Pretraining](https://aclanthology.org/2023.findings-acl.254.pdf) · 2023
  - `acl:2023.findings-acl.254.pdf` · cited by 1: LJ
  - summary: Masks tokens by their informativeness rather than randomly, adding a Token-specific Label Smoothing step so masked-language pretraining focuses learning on under-explored tokens instead of uniformly random ones, improving 10 downstream tasks by 1.4-2.1 points on average across different pretrained models.

- [SELFEVOLVE: A Code Evolution Framework via Large Language Models](https://arxiv.org/pdf/2306.02907) · 2023-06
  - `arxiv:2306.02907` · cited by 1: LJ
  - summary: Two-step knowledge-provider then self-reflective-programmer pipeline.

- [Self-Evolved Diverse Data Sampling for Efficient Instruction Tuning](https://arxiv.org/pdf/2311.08182) · 2023-11
  - `arxiv:2311.08182` · cited by 1: LJ
  - summary: Self-evolving selection for label-efficient instruction tuning.

- [A Survey on Self-Evolution of Large Language Models](https://arxiv.org/pdf/2404.14387) · 2024-04
  - `arxiv:2404.14387` · cited by 1: LJ
  - summary: Four-phase framework; the entry point for this whole category.

- [Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy](https://arxiv.org/abs/2407.06813) · 2024-07
  - `arxiv:2407.06813` · cited by 1: LJ
  - summary: Strategic planning plus self-play evolution without human intervention.

- [Reinforcement Learning for Long-Horizon Interactive LLM Agents](https://arxiv.org/abs/2502.01600) · 2025-02
  - `arxiv:2502.01600` · cited by 1: ZJ
  - summary: TODO

- [ATLaS: Agent Tuning via Learning Critical Steps](https://arxiv.org/abs/2503.02197) · 2025-03
  - `arxiv:2503.02197` · cited by 1: LJ
  - summary: Tunes only on critical expert-trajectory steps, cutting cost.

- [Group-in-Group Policy Optimization for LLM Agent Training](https://arxiv.org/abs/2505.10978) · 2025-05
  - `arxiv:2505.10978` · cited by 1: ZJ
  - related: <https://github.com/langfengQ/verl-agent>
  - summary: TODO

- [SPA-RL: Reinforcing LLM Agents via Stepwise Progress Attribution](https://arxiv.org/abs/2505.20732) · 2025-05
  - `arxiv:2505.20732` · cited by 1: ZJ
  - related: <https://github.com/WangHanLinHenry/SPA-RL-Agent>
  - summary: TODO

- [Towards Efficient Online Tuning of VLM Agents via Counterfactual Soft Reinforcement Learning](https://arxiv.org/abs/2505.03792) · 2025-05
  - `arxiv:2505.03792` · cited by 1: ZJ
  - related: <https://github.com/langfengQ/CoSo>
  - summary: TODO

- [EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle](https://arxiv.org/abs/2510.16079) · 2025-10
  - `arxiv:2510.16079` · cited by 1: LJ
  - summary: Distills past runs into abstract principles that guide later decisions.

- [In-the-Flow Agentic System Optimization for Effective Planning and Tool Use](https://arxiv.org/abs/2510.05592) · 2025-10
  - `arxiv:2510.05592` · cited by 1: ZJ
  - summary: TODO

- [AgentDevel: Reframing Self-Evolving LLM Agents as Release Engineering](https://arxiv.org/pdf/2601.04620v1) · 2026-01
  - `arxiv:2601.04620` · cited by 1: VA
  - summary: Treats a self-evolving agent like a software release, with a critic that diagnoses failures from the outside and a gate that prioritizes non-regression over raw score, replacing unstable population search or in-agent self-refinement with a single auditable version line.

- [ArenaRL: Scaling RL for Open-Ended Agents via Tournament-based Relative Ranking](https://arxiv.org/pdf/2601.06487v2) · 2026-01
  - `arxiv:2601.06487` · cited by 1: VA
  - summary: Replaces pointwise reward scoring (which collapses subtle trajectory differences into noise) with intra-group tournament ranking for RL on open-ended agent tasks, matching full pairwise-comparison accuracy at linear instead of quadratic cost.

- [AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement](https://arxiv.org/pdf/2601.22758v1) · 2026-01
  - `arxiv:2601.22758` · cited by 1: VA
  - summary: Extracts reusable 'Experience Patterns' from an agent's task history as both specialized subagents (procedural knowledge) and skill snippets (static knowledge), with automatic pruning to stop the pattern repository degrading, beating hand-designed systems on TravelPlanner (27.1% vs 12.1%).

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

1 entries with no date derivable from their source (GitHub repos, blog posts, etc.).

- [AlphaFlow: autonomous discovery and optimization of multi-step chemistry using a self-driven fluidic lab guided by reinforcement learning](https://www.nature.com/articles/s41467-023-37139-y)
  - `url:https://nature.com/articles/s41467-023-37139-y` · cited by 1: LJ
  - summary: NEEDS-SOURCE
