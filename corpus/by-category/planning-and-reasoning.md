# planning-and-reasoning

66 entries.

## Timeline

58 dated entries, oldest first.

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) · 2022-10
  - `arxiv:2210.03629` · cited by 1: HE
  - summary: Interleaves reasoning traces with actions in a Thought/Action/Observation loop; the structure nearly every agent harness still uses.

- [Describe, Explain, Plan and Select: Interactive Planning with LLMs Enables Open-World Multi-Task Agents](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6b8dfb8c0c12e6fafc6c256cb08a5ca7-Abstract-Conference.html) · 2023
  - `url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/6b8dfb8c0c12e6fafc6c256cb08a5ca7-Abstract-Conference.html` · cited by 1: LJ
  - summary: DEPS interleaves describing, explaining, planning, and a learnable goal-selector that reorders sub-goals by estimated completion difficulty, becoming the first zero-shot agent to robustly clear 70+ Minecraft tasks and nearly doubling prior performance.

- [Large Language Models are Better Reasoners with Self-Verification](https://aclanthology.org/2023.findings-emnlp.167.pdf) · 2023
  - `acl:2023.findings-emnlp.167.pdf` · cited by 1: LJ
  - summary: Backward verification over CoT conclusions.

- [Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](https://arxiv.org/pdf/2302.01560) · 2023-02
  - `arxiv:2302.01560` · cited by 1: LJ
  - summary: Interactive planning with goal selection for open-world multi-task agents.

- [Plan-and-Execute Agents](https://blog.langchain.com/plan-and-execute-agents/) · 2023-05
  - `url:https://blog.langchain.com/plan-and-execute-agents` · cited by 1: HE
  - summary: Separates one-shot planning from execution, replanning only when needed.

- [TPTU: Large Language Model-based AI Agents for Task Planning and Tool Usage](https://arxiv.org/abs/2308.03427) · 2023-08
  - `arxiv:2308.03427` · cited by 1: LJ
  - summary: Proposes a structured framework for LLM agents with one-step and sequential agent variants and evaluates multiple LLMs on task-planning-plus-tool-use, establishing the baseline TPTU-v2 later extends.

- [microsoft/TaskWeaver](https://github.com/microsoft/TaskWeaver) · 2023-09
  - `gh:microsoft/taskweaver` · cited by 1: HE
  - summary: Code-first planner/executor split with plugins for domain knowledge.

- [LATS: Language Agent Tree Search](https://arxiv.org/abs/2310.04406) · 2023-10
  - `arxiv:2310.04406` · cited by 1: HE
  - summary: MCTS over agent trajectories with environment feedback as the search signal.

- [TPTU-v2: Boosting Task Planning and Tool Usage of Large Language Model-based Agents in Real-world Systems](http://arxiv.org/abs/2311.11315) · 2023-11
  - `arxiv:2311.11315` · cited by 1: LJ
  - summary: Adds an API retriever (to fit within token limits), a fine-tuned planner, and an adaptive demo selector (for hard-to-distinguish APIs) on top of TPTU, validated on a real commercial system as well as an open academic benchmark.

- [Large Language Models lack essential metacognition for reliable medical reasoning](https://doi.org/10.1038/s41467-024-55628-6) · 2024
  - `url:https://doi.org/10.1038/s41467-024-55628-6` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [Refining Guideline Knowledge for Agent Planning Using Textgrad](https://www.computer.org/csdl/proceedings-article/ickg/2024/088200a102/24sKrMSCxr2) · 2024
  - `url:https://computer.org/csdl/proceedings-article/ickg/2024/088200a102/24sKrMSCxr2` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [Planning, Creation, Usage: Benchmarking LLMs for Comprehensive Tool Utilization in Real-World Complex Scenarios](https://arxiv.org/abs/2401.17167) · 2024-01
  - `arxiv:2401.17167` · cited by 1: LJ
  - summary: Planning, creation and usage across the whole tool pipeline without a fixed toolset.

- [Enhancing the General Agent Capabilities of Low-Parameter LLMs through Tuning and Multi-Branch Reasoning](https://arxiv.org/abs/2403.19962) · 2024-03
  - `arxiv:2403.19962` · cited by 1: LJ
  - summary: Shows supervised fine-tuning on GPT-4-constructed agent-specific data sharply cuts hallucination and formatting errors for 7B/13B open models used as agents, and that multi-path reasoning plus task decomposition further boosts their AgentBench performance.

- [KnowAgent: Knowledge-Augmented Planning for LLM-Based Agents](https://arxiv.org/pdf/2403.03101) · 2024-03
  - `arxiv:2403.03101` · cited by 1: LJ
  - summary: Action knowledge base plus self-learning to curb planning hallucination.

- [Perceive, Reflect, and Plan: Designing LLM Agent for Goal-Directed City Navigation without Instructions](http://arxiv.org/abs/2408.04168) · 2024-08
  - `arxiv:2408.04168` · cited by 1: LJ
  - summary: Fine-tunes a vision-language model to perceive landmark direction/distance for goal-directed city navigation with no explicit instructions, adding a memory-based reflection step and a planning stage that together fix the repeated-visit, short-sighted behavior of a bare react-on-observation baseline.

- [PlanCritic: Formal Planning with Human Feedback](https://arxiv.org/abs/2412.00300) · 2024-12
  - `arxiv:2412.00300` · cited by 1: LJ
  - summary: Uses an evolutionary algorithm plus a trained LSTM validator to repair imprecise LLM-generated PDDL goal specifications against the original natural-language intent, improving adherence over plans generated from a single LLM translation pass.

- [Planning with Multi-Constraints via Collaborative Language Agents](https://aclanthology.org/2025.coling-main.672/) · 2025
  - `acl:2025.coling-main.672` · cited by 1: LJ
  - summary: Decomposes constraint-heavy planning into a hierarchy of subordinate tasks across a zero-shot multi-agent pipeline, reaching 42.68% success on TravelPlanner versus GPT-4's 2.92%, and working even with an 8B model as the planning core.

- [Plan-and-Act: Improving Planning of Agents for Long-Horizon Tasks](https://arxiv.org/abs/2503.09572) · 2025-03
  - `arxiv:2503.09572` · cited by 1: HE
  - summary: Independent specialization of planner and executor; 57.58% WebArena-Lite, 81.36% WebVoyager.

- [SWEET-RL: Training Multi-Turn LLM Agents on Collaborative Reasoning Tasks](https://arxiv.org/abs/2503.15478) · 2025-03
  - `arxiv:2503.15478` · cited by 1: LJ
  - summary: Step-level rewards from a critic with training-time information; introduces ColBench.

- [DualRAG: A Dual-Process Approach to Integrate Reasoning and Retrieval for Multi-Hop Question Answering](https://arxiv.org/abs/2504.18243) · 2025-04
  - `arxiv:2504.18243` · cited by 1: LJ
  - summary: Couples reasoning and retrieval into two tightly interleaved processes for multi-hop QA (reasoning generates targeted queries, retrieval feeds structured knowledge back into reasoning), preserving both capabilities even after fine-tuning down to smaller models.

- [Agents of Change: Self-Evolving LLM Agents for Strategic Planning](https://arxiv.org/abs/2506.04651) · 2025-06
  - `arxiv:2506.04651` · cited by 1: LJ
  - summary: Uses Catan as a strategic benchmark for self-improving architectures.

- [Reinforcing Large Language Model Reasoning through Multi-Agent Reflection](https://arxiv.org/abs/2506.08379) · 2025-06
  - `arxiv:2506.08379` · cited by 1: LJ
  - summary: DPSDP applies dynamic-programming-based direct policy search to multi-agent reflection, provably matching any in-distribution policy's performance and lifting MATH 500 accuracy from 58.2% to 63.2% via five refinement rounds with majority voting.

- [Analyzing Information Sharing and Coordination in Multi-Agent Planning](https://arxiv.org/abs/2508.12981) · 2025-08
  - `arxiv:2508.12981` · cited by 1: LJ
  - summary: Finds that in multi-agent travel planning, a shared notebook cuts hallucinated-detail errors 18% and an orchestrator agent cuts further errors up to 13.5%; combined, they lift TravelPlanner pass rate from a 7.5% single-agent baseline to 25%.

- [BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens](https://arxiv.org/abs/2508.17196) · 2025-08
  - `arxiv:2508.17196` · cited by 1: LJ
  - summary: Inserts control tokens during inference so an LLM stays aware of its remaining reasoning-token budget, trained via SFT then curriculum RL with a length-aware reward, holding accuracy across tighter budgets better than baselines.

- [PVPO: Pre-Estimated Value-Based Policy Optimization for Agentic Reasoning](https://arxiv.org/abs/2508.21104) · 2025-08
  - `arxiv:2508.21104` · cited by 1: LJ
  - summary: Advantage reference anchor plus pre-sampling to cut rollout dependence.

- [SE-Agent: Self-Evolution Trajectory Optimization in Multi-Step Reasoning with LLM-Based Agents](https://arxiv.org/abs/2508.02085) · 2025-08
  - `arxiv:2508.02085` · cited by 1: LJ
  - summary: Revision, recombination and refinement to widen the search space across trajectories.

- [Think in Games: Learning to Reason in Games via Reinforcement Learning with Large Language Models](https://arxiv.org/abs/2508.21365) · 2025-08
  - `arxiv:2508.21365` · cited by 1: LJ
  - summary: Reformulates game-playing RL as language modeling so an LLM generates language-guided policies refined by online RL against environment feedback, closing the declarative-vs-procedural-knowledge gap at far lower data cost while still producing natural-language explanations for its decisions.

- [Effective Harnesses for Long-Running Agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents) · 2025-11
  - `url:https://anthropic.com/engineering/effective-harnesses-for-long-running-agents` · cited by 1: HE
  - summary: Initializer-then-worker handoff so progress survives across context windows.

- [A2RAG: Adaptive Agentic Graph Retrieval for Cost-Aware and Reliable Reasoning](https://arxiv.org/pdf/2601.21162v1) · 2026-01
  - `arxiv:2601.21162` · cited by 1: VA
  - summary: Verifies evidence sufficiency and escalates retrieval effort progressively.

- [Agentic Reasoning for Large Language Models](https://arxiv.org/pdf/2601.12538v1) · 2026-01
  - `arxiv:2601.12538` · cited by 1: VA
  - summary: A roadmap survey organizing agentic reasoning into three layers (foundational single-agent, self-evolving, and collective multi-agent) and two training modes (in-context orchestration vs RL/SFT post-training), spanning science, robotics, and math applications.

- [AT²PO: Agentic Turn-based Policy Optimization via Tree Search](https://arxiv.org/pdf/2601.04767v1) · 2026-01
  - `arxiv:2601.04767` · cited by 1: VA
  - summary: A turn-level tree-search RL framework that jointly does entropy-guided exploration and turn-wise credit assignment for multi-turn agentic tasks, improving up to 1.84 points over state-of-the-art across seven benchmarks.

- [Beyond Static Tools: Test-Time Tool Evolution for Scientific Reasoning](https://arxiv.org/pdf/2601.07641v1) · 2026-01
  - `arxiv:2601.07641` · cited by 1: VA
  - summary: Lets agents synthesize, verify, and evolve their own tools at inference time instead of drawing from a fixed library, which matters specifically in science where tools are sparse and incomplete; introduces the SciEvo benchmark (1,590 tasks, 925 evolved tools) to measure it.

- [Breaking Up with Normatively Monolithic Agency with GRACE: A Reason-Based Neuro-Symbolic Architecture for Safe and Ethical AI Alignment](https://arxiv.org/pdf/2601.10520v2) · 2026-01
  - `arxiv:2601.10520` · cited by 1: VA
  - summary: A neuro-symbolic architecture that separates moral reasoning (a deontic-logic Moral Module) from instrumental decision-making (a wrapped Decision-Making Module), with a Guard enforcing compliance, aiming to make agent alignment interpretable and contestable rather than baked into one opaque policy.

- [Choosing the Right Multi-Agent Architecture](https://blog.langchain.com/choosing-the-right-multi-agent-architecture/) · 2026-01
  - `url:https://blog.langchain.com/choosing-the-right-multi-agent-architecture` · cited by 1: HE
  - summary: Four patterns with data: subagents process 67% fewer tokens than skills multi-domain.

- [Collaborative Multi-Agent Test-Time Reinforcement Learning for Reasoning](https://arxiv.org/pdf/2601.09667v2) · 2026-01
  - `arxiv:2601.09667` · cited by 1: VA
  - summary: Injects structured textual experience at test time, no tuning.

- [Controlling Long-Horizon Behavior in Language Model Agents with Explicit State Dynamics](https://arxiv.org/pdf/2601.16087v1) · 2026-01
  - `arxiv:2601.16087` · cited by 1: VA
  - summary: Adds an external Valence-Arousal-Dominance affective state with first/second-order update rules to give a long-horizon dialogue agent temporal coherence, finding stateless agents drift while state persistence enables recovery, and second-order dynamics trade responsiveness for stability.

- [Lost in the Noise: How Reasoning Models Fail with Contextual Distractors](https://arxiv.org/pdf/2601.07226v1) · 2026-01
  - `arxiv:2601.07226` · cited by 1: VA
  - summary: Robustness across 11 tasks against several noise types.

- [LUMINA: Long-horizon Understanding for Multi-turn Interactive Agents](https://arxiv.org/pdf/2601.16649v1) · 2026-01
  - `arxiv:2601.16649` · cited by 1: VA
  - summary: Oracle counterfactuals measuring which capability actually mattered.

- [MARO: Learning Stronger Reasoning from Social Interaction](https://arxiv.org/pdf/2601.12323v2) · 2026-01
  - `arxiv:2601.12323` · cited by 1: VA
  - summary: Decomposes social-interaction outcomes into per-behaviour signals.

- [MAS-Orchestra: Understanding and Improving Multi-Agent Reasoning Through Holistic Orchestration and Controlled Benchmarks](https://arxiv.org/pdf/2601.14652v2) · 2026-01
  - `arxiv:2601.14652` · cited by 1: VA
  - summary: Orchestration as function-calling RL, with MASBENCH for controlled evaluation.

- [POLARIS: Typed Planning and Governed Execution for Agentic AI in Back-Office Automation](https://arxiv.org/pdf/2601.11816v1) · 2026-01
  - `arxiv:2601.11816` · cited by 1: VA
  - summary: A governed orchestration framework for back-office automation where a planner proposes type-checked plan DAGs, a rubric-guided module selects one compliant plan, and execution is gated by validators and compiled policy guardrails, reaching 0.81 micro-F1 on SROIE while preserving full audit trails.

- [Real-Time Deadlines Reveal Temporal Awareness Failures in LLM Strategic Reasoning](https://arxiv.org/abs/2601.13206) · 2026-01
  - `arxiv:2601.13206` · cited by 1: HE
  - summary: Temporal awareness is orthogonal to reasoning; deadlines must be injected into context.

- [SemanticALLI: Caching Reasoning, Not Just Responses, in Agentic Systems](https://arxiv.org/pdf/2601.16286v2) · 2026-01
  - `arxiv:2601.16286` · cited by 1: VA
  - summary: Caches intermediate reasoning structures, not just final responses, by decomposing an agentic pipeline into intent resolution and synthesis stages and treating each stage's output as a cacheable artifact, lifting cache hit rate from 38.7% to 83.1% and bypassing thousands of LLM calls.

- [Stalled, Biased, and Confused: Uncovering Reasoning Failures in LLMs for Cloud-Based Root Cause Analysis](https://arxiv.org/pdf/2601.22208v1) · 2026-01
  - `arxiv:2601.22208` · cited by 1: VA
  - summary: 48,000 scenarios producing a 16-failure taxonomy under ReAct and Plan-and-Execute.

- [SYMPHONY: Synergistic Multi-agent Planning with Heterogeneous Language Model Assembly](https://arxiv.org/pdf/2601.22623v1) · 2026-01
  - `arxiv:2601.22623` · cited by 1: VA
  - summary: Runs Monte Carlo Tree Search planning with a pool of heterogeneous LLM-based agents instead of one, using their differing reasoning patterns to diversify search branches, beating single-agent MCTS baselines even with consumer-hardware open models.

- [Task-Decoupled Planning for Long-Horizon Agents (TDP)](https://arxiv.org/abs/2601.07577) · 2026-01
  - `arxiv:2601.07577` · cited by 1: HE
  - summary: Dependency-graph decomposition enabling localized replanning without cascade.

- [TCAndon-Router: Adaptive Reasoning Router for Multi-Agent Collaboration](https://arxiv.org/pdf/2601.04544v1) · 2026-01
  - `arxiv:2601.04544` · cited by 1: VA
  - summary: A multi-agent router that generates a natural-language reasoning chain before predicting candidate expert agents, supporting dynamic onboarding of new agents and aggregating multiple agents' answers via a Refining Agent to reduce routing conflicts as the agent pool grows.

- [Think Locally, Explain Globally: Graph-Guided LLM Investigations via Local Reasoning and Belief Propagation](https://arxiv.org/pdf/2601.17915v2) · 2026-01
  - `arxiv:2601.17915` · cited by 1: VA
  - summary: Separates evidence-gathering from reasoning for open-ended investigations over large heterogeneous data: an LLM does bounded local lookups while a deterministic controller tracks state and propagates belief, cutting the exploration-order instability of ReAct-style agents and gaining 7x on entity-level consistency.

- [Too Helpful to Be Safe: User-Mediated Attacks on Planning and Web-Use Agents](https://arxiv.org/pdf/2601.10758v1) · 2026-01
  - `arxiv:2601.10758` · cited by 1: VA
  - summary: Introduces UReCoM, an attack where a benign user is manipulated into relaying adversarial content inside their own request, bypassing prompt-injection defenses because agents validate explicit malicious instructions far more reliably than adversarial entities embedded in legitimate-looking user text.

- [Why Reasoning Fails to Plan: A Planning-Centric Analysis of Long-Horizon Decision Making in LLM Agents](https://arxiv.org/pdf/2601.22311v1) · 2026-01
  - `arxiv:2601.22311` · cited by 1: VA
  - summary: Shows step-wise reasoning acts as a myopic greedy policy that fails on long horizons because early actions can't account for delayed consequences, then introduces FLARE (explicit lookahead and value propagation) which lets an 8B model with FLARE outperform GPT-4o doing plain step-by-step reasoning.

- [Agyn: A Multi-Agent System for Team-Based Autonomous Software Engineering](https://arxiv.org/abs/2602.01465) · 2026-02
  - `arxiv:2602.01465` · cited by 2: HE, VA
  - summary: Role-specialized agents with differing model sizes and tool access.

- [DyTopo: Dynamic Topology Routing for Multi-Agent Reasoning via Semantic Matching](https://arxiv.org/pdf/2602.06039v1) · 2026-02
  - `arxiv:2602.06039` · cited by 1: VA
  - summary: Rewires agent connections each reasoning round instead of fixed topology.

- [Multi-Agent Workflows Often Fail. Here's How to Engineer Ones That Don't.](https://github.blog/ai-and-ml/generative-ai/multi-agent-workflows-often-fail-heres-how-to-engineer-ones-that-dont/) · 2026-02
  - `url:https://github.blog/ai-and-ml/generative-ai/multi-agent-workflows-often-fail-heres-how-to-engineer-ones-that-dont` · cited by 1: HE
  - summary: Treat handoffs as distributed-system interfaces with typed schemas.

- [ROMA: Recursive Open Meta-Agent Framework for Long-Horizon Multi-Agent Systems](https://arxiv.org/pdf/2602.01848v1) · 2026-02
  - `arxiv:2602.01848` · cited by 1: VA
  - summary: Subtask trees running in parallel to exceed single-context limits.

- [Task-Adaptive Multi-Agent Orchestration (AdaptOrch)](https://arxiv.org/abs/2602.16873) · 2026-02
  - `arxiv:2602.16873` · cited by 1: HE
  - summary: Selects topology from the task dependency graph; 12–23% over model selection.

- [Building NVIDIA Nemotron 3 Agents for Reasoning, Multimodal RAG, Voice, and Safety](https://developer.nvidia.com/blog/building-nvidia-nemotron-3-agents-for-reasoning-multimodal-rag-voice-and-safety/) · 2026-03
  - `url:https://developer.nvidia.com/blog/building-nvidia-nemotron-3-agents-for-reasoning-multimodal-rag-voice-and-safety` · cited by 1: HE
  - summary: NVIDIA's Nemotron 3 Super is an open hybrid Mamba-Transformer mixture-of-experts model activating 12B parameters per pass with a 1M-token context, tuned for coding, math, and function-calling in multi-agent settings.

- [Harness Design for Long-Running Application Development](https://www.anthropic.com/engineering/harness-design-long-running-apps) · 2026-03
  - `url:https://anthropic.com/engineering/harness-design-long-running-apps` · cited by 1: HE
  - summary: Multi-session harness design; every component encodes an assumption that will expire.

- [DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) · 2026-04
  - `gh:esengine/deepseek-reasonix` · cited by 1: HE
  - summary: A DeepSeek-native terminal coding agent engineered around prefix-cache stability to keep token costs low, distributed as a single dependency-free static binary with config-driven, multi-model, plugin-extensible design.

## Tools & Undated

8 entries with no date derivable from their source (GitHub repos, blog posts, etc.).

- [Agent Planning with World Knowledge Model](https://openreview.net/pdf?id=j6kJSS9O6I)
  - `openreview:j6kJSS9O6I` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://openreview.net/pdf?id=Sx038qxjek)
  - `openreview:Sx038qxjek` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [Enhancing Robot Task Planning: Integrating Environmental Information and Feedback Insights through Large Language Models](https://ieeexplore.ieee.org/abstract/document/10661782)
  - `url:https://ieeexplore.ieee.org/abstract/document/10661782` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [Run Long-Horizon Tasks with Codex](https://developers.openai.com/blog/run-long-horizon-tasks-with-codex/)
  - `url:https://developers.openai.com/blog/run-long-horizon-tasks-with-codex` · cited by 1: HE
  - summary: Plan.md / Implement.md / Documentation.md as reusable harness artifacts.

- [SciAgents: Automating Scientific Discovery Through Bioinspired Multi-Agent Intelligent Graph Reasoning](https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/adma.202413523)
  - `url:https://advanced.onlinelibrary.wiley.com/doi/full/10.1002/adma.202413523` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [SMART-LLM: Smart Multi-Agent Robot Task Planning using Large Language Models](https://ieeexplore.ieee.org/abstract/document/10802322)
  - `url:https://ieeexplore.ieee.org/abstract/document/10802322` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [STaR: Self-Taught Reasoner Bootstrapping Reasoning With Reasoning](https://openreview.net/pdf?id=_3ELRdg2sgI)
  - `openreview:_3ELRdg2sgI` · cited by 1: LJ
  - summary: Bootstraps reasoning from a handful of rationales plus rationale-free data. The origin of the self-improvement line.

- [V-STaR: Training Verifiers for Self-Taught Reasoners](https://openreview.net/pdf?id=stmqBSW2dV)
  - `openreview:stmqBSW2dV` · cited by 1: LJ
  - summary: Trains a verifier on *both* correct and incorrect self-generated solutions.
