# training-and-optimization

16 entries.

- [AgentDevel: Reframing Self-Evolving LLM Agents as Release Engineering](https://arxiv.org/pdf/2601.04620v1)
  - `arxiv:2601.04620` · cited by 1: VA
  - summary: Treats a self-evolving agent like a software release, with a critic that diagnoses failures from the outside and a gate that prioritizes non-regression over raw score, replacing unstable population search or in-agent self-refinement with a single auditable version line.

- [AlphaFlow: autonomous discovery and optimization of multi-step chemistry using a self-driven fluidic lab guided by reinforcement learning](https://www.nature.com/articles/s41467-023-37139-y)
  - `url:https://nature.com/articles/s41467-023-37139-y` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [ArenaRL: Scaling RL for Open-Ended Agents via Tournament-based Relative Ranking](https://arxiv.org/pdf/2601.06487v2)
  - `arxiv:2601.06487` · cited by 1: VA
  - summary: Replaces pointwise reward scoring (which collapses subtle trajectory differences into noise) with intra-group tournament ranking for RL on open-ended agent tasks, matching full pairwise-comparison accuracy at linear instead of quadratic cost.

- [ATLaS: Agent Tuning via Learning Critical Steps](https://arxiv.org/abs/2503.02197)
  - `arxiv:2503.02197` · cited by 1: LJ
  - summary: Tunes only on critical expert-trajectory steps, cutting cost.

- [AutoRefine: From Trajectories to Reusable Expertise for Continual LLM Agent Refinement](https://arxiv.org/pdf/2601.22758v1)
  - `arxiv:2601.22758` · cited by 1: VA
  - summary: Extracts reusable 'Experience Patterns' from an agent's task history as both specialized subagents (procedural knowledge) and skill snippets (static knowledge), with automatic pruning to stop the pattern repository degrading, beating hand-designed systems on TravelPlanner (27.1% vs 12.1%).

- [EvolveR: Self-Evolving LLM Agents through an Experience-Driven Lifecycle](https://arxiv.org/abs/2510.16079)
  - `arxiv:2510.16079` · cited by 1: LJ
  - summary: Distills past runs into abstract principles that guide later decisions.

- [JitRL: Just-In-Time Reinforcement Learning for Continual Learning in LLM Agents Without Gradient Updates](https://arxiv.org/pdf/2601.18510v1)
  - `arxiv:2601.18510` · cited by 1: VA
  - summary: Adapts a deployed LLM agent at test time with no gradient updates by retrieving similar past trajectories to estimate action advantages and directly modulating output logits, proven to be the closed-form solution of KL-constrained policy optimization, beating full fine-tuning at 30x lower cost.

- [OpenTinker: Separating Concerns in Agentic Reinforcement Learning](https://arxiv.org/pdf/2601.07376v1)
  - `arxiv:2601.07376` · cited by 1: VA
  - summary: An infrastructure for running many LoRA-backed agent policies over shared compute, treating adapters as live policy states (not static artifacts) so SFT, RL, rollout, and multi-turn training can share a base model while keeping each adapter's checkpoints and gradients isolated.

- [Paying Less Generalization Tax: A Cross-Domain Generalization Study of RL Training for LLM Agents](https://arxiv.org/pdf/2601.18217v1)
  - `arxiv:2601.18217` · cited by 1: VA
  - summary: Finds environment realism matters less for cross-domain agent generalization than state richness and planning complexity (Sokoban transfers better than the more realistic ALFWorld), and that step-by-step thinking during RL preserves generalization better than SFT warmup alone.

- [PRISM: Disentangling SFT and RL Data via Gradient Concentration](https://arxiv.org/pdf/2601.07224v1)
  - `arxiv:2601.07224` · cited by 1: VA
  - summary: Routes each training example to SFT or RL based on how much it conflicts with the model's existing knowledge (measured via gradient concentration), since consolidation and structural adaptation need different training regimes, cutting compute up to 3.22x over hybrid baselines.

- [Richelieu: Self-Evolving LLM-Based Agents for AI Diplomacy](https://arxiv.org/abs/2407.06813)
  - `arxiv:2407.06813` · cited by 1: LJ
  - summary: Strategic planning plus self-play evolution without human intervention.

- [Self-Evolved Diverse Data Sampling for Efficient Instruction Tuning](https://arxiv.org/pdf/2311.08182)
  - `arxiv:2311.08182` · cited by 1: LJ
  - summary: Self-evolving selection for label-efficient instruction tuning.

- [SELFEVOLVE: A Code Evolution Framework via Large Language Models](https://arxiv.org/pdf/2306.02907)
  - `arxiv:2306.02907` · cited by 1: LJ
  - summary: Two-step knowledge-provider then self-reflective-programmer pipeline.

- [Towards AGI A Pragmatic Approach Towards Self Evolving Agent](https://arxiv.org/pdf/2601.11658v1)
  - `arxiv:2601.11658` · cited by 1: VA
  - summary: A hierarchical multi-agent framework where a stuck agent escalates to synthesizing new tools, then to full evolution via curriculum learning, RL, or genetic algorithms depending on failure severity, with each evolution strategy suited to a different difficulty regime.

- [TrajAD: Trajectory Anomaly Detection for Trustworthy LLM Agents](https://arxiv.org/pdf/2602.06443v1)
  - `arxiv:2602.06443` · cited by 1: VA
  - summary: Runtime verifier locating trajectory errors for precise rollback-and-retry.

- [Trajectory Guard: A Lightweight, Sequence-Aware Model for Real-Time Anomaly Detection in Agentic AI](https://arxiv.org/pdf/2601.00516v1)
  - `arxiv:2601.00516` · cited by 1: VA
  - summary: A Siamese recurrent autoencoder that jointly detects 'wrong plan for the task' and 'malformed plan structure' in agent trajectories via contrastive plus reconstruction loss, hitting 0.88-0.94 F1 at 32ms latency, 17-27x faster than an LLM-judge baseline.
