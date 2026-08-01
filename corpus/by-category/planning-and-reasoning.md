# planning-and-reasoning

144 entries.

## Timeline

132 dated entries, oldest first.

- [Language Models as Zero-Shot Planners: Extracting Actionable Knowledge for Embodied Agents](https://arxiv.org/abs/2201.07207) · 2022-01
  - `arxiv:2201.07207` · cited by 1: ZJ
  - summary: Grounds free-form plans by projecting onto admissible actions.

- [Inner Monologue: Embodied Reasoning through Planning with Language Models](https://arxiv.org/abs/2207.05608) · 2022-07
  - `arxiv:2207.05608` · cited by 1: ZJ
  - summary: Closes the loop by feeding environment feedback back as language.

- [Mind's Eye: Grounded Language Model Reasoning through Simulation](https://arxiv.org/abs/2210.05359) · 2022-10
  - `arxiv:2210.05359` · cited by 1: ZJ
  - summary: Runs a physics simulator (MuJoCo) on the question first and feeds the simulated outcome into the LLM's context before it reasons, letting a much smaller model match one 100x larger on physical-reasoning benchmarks.

- [ReAct: Synergizing Reasoning and Acting in Language Models](https://arxiv.org/abs/2210.03629) · 2022-10
  - `arxiv:2210.03629` · cited by 3: BK, HE, ZJ
  - summary: Interleaves reasoning traces with actions in a Thought/Action/Observation loop; the structure nearly every agent harness still uses.

- [SurCo: Learning Linear Surrogates For Combinatorial Nonlinear Optimization Problems](https://arxiv.org/abs/2210.12547) · 2022-10
  - `arxiv:2210.12547` · cited by 1: BK
  - summary: Learned linear surrogates for combinatorial nonlinear optimization.

- [Don’t Generate, Discriminate: A Proposal for Grounding Language Models to Real-World Environments](https://arxiv.org/abs/2212.09736) · 2022-12
  - `arxiv:2212.09736` · cited by 1: ZJ
  - summary: Instead of having the LLM generate plans directly, pairs it with a symbolic agent that enumerates valid candidate plans and has the LLM just score which is most plausible — a BERT-base model set up this way sets a new record on knowledge-base QA.

- [LLM-Planner: Few-Shot Grounded Planning for Embodied Agents with Large Language Models](https://arxiv.org/abs/2212.04088) · 2022-12
  - `arxiv:2212.04088` · cited by 1: ZJ
  - summary: Uses an LLM as a few-shot planner for embodied instruction-following that updates its plan against the live scene rather than sticking to one fixed generation, matching fully-trained ALFRED baselines while using under 0.5% of their training data.

- [Describe, Explain, Plan and Select: Interactive Planning with LLMs Enables Open-World Multi-Task Agents](https://proceedings.neurips.cc/paper_files/paper/2023/hash/6b8dfb8c0c12e6fafc6c256cb08a5ca7-Abstract-Conference.html) · 2023
  - `url:https://proceedings.neurips.cc/paper_files/paper/2023/hash/6b8dfb8c0c12e6fafc6c256cb08a5ca7-Abstract-Conference.html` · cited by 1: LJ
  - summary: DEPS interleaves describing, explaining, planning, and a learnable goal-selector that reorders sub-goals by estimated completion difficulty, becoming the first zero-shot agent to robustly clear 70+ Minecraft tasks and nearly doubling prior performance.

- [Large Language Models are Better Reasoners with Self-Verification](https://aclanthology.org/2023.findings-emnlp.167.pdf) · 2023
  - `acl:2023.findings-emnlp.167.pdf` · cited by 1: LJ
  - summary: Backward verification over CoT conclusions.

- [Do Embodied Agents Dream of Pixelated Sheep?: Embodied Decision Making using Language Guided World Modelling](https://arxiv.org/abs/2301.12050) · 2023-01
  - `arxiv:2301.12050` · cited by 1: ZJ
  - summary: Has an LLM hypothesize a subgoal sequence for a Minecraft crafting task, then has the agent execute, verify and correct that hypothesized world model against real experience, improving RL sample efficiency by an order of magnitude while staying robust to the LLM's mistakes.

- [Describe, Explain, Plan and Select: Interactive Planning with Large Language Models Enables Open-World Multi-Task Agents](https://arxiv.org/pdf/2302.01560) · 2023-02
  - `arxiv:2302.01560` · cited by 2: LJ, ZJ
  - summary: Interactive planning with goal selection for open-world multi-task agents.

- [Chat with the Environment: Interactive Multimodal Perception using Large Language Models](https://arxiv.org/abs/2303.08268) · 2023-03
  - `arxiv:2303.08268` · cited by 1: ZJ
  - summary: Gives a robot an LLM backbone that decides which sense to query — vision, sound, touch — before acting, so it can plan around partial observability instead of assuming it already has full state information.

- [PaLM-E: An embodied multimodal language model](https://arxiv.org/abs/2303.03378) · 2023-03
  - `arxiv:2303.03378` · cited by 1: ZJ
  - summary: Interleaves images, state and text into one embodied multimodal model.

- [Plan4MC: Skill Reinforcement Learning and Planning for Open-World Minecraft Tasks](https://arxiv.org/abs/2303.16563) · 2023-03
  - `arxiv:2303.16563` · cited by 1: ZJ
  - summary: Skill RL plus planning over a skill graph for Minecraft tasks.

- [Reflexion: Language Agents with Verbal Reinforcement Learning](https://arxiv.org/abs/2303.11366) · 2023-03
  - `arxiv:2303.11366` · cited by 1: ZJ
  - summary: Agent critiques its own failed attempt in natural language and retries, turning failure into a text-based learning signal.

- [Self-Refine: Iterative Refinement with Self-Feedback](https://arxiv.org/abs/2303.17651) · 2023-03
  - `arxiv:2303.17651` · cited by 1: ZJ
  - summary: Same model generates, critiques and revises its own output in a loop.

- [Teaching Large Language Models to Self-Debug](https://arxiv.org/abs/2304.05128) · 2023-04
  - `arxiv:2304.05128` · cited by 2: BK, ZJ
  - summary: Model explains and repairs its own code from execution results.

- [AdaPlanner: Adaptive Planning from Feedback with Language Models](https://arxiv.org/abs/2305.16653) · 2023-05
  - `arxiv:2305.16653` · cited by 1: ZJ
  - summary: Lets an LLM agent rewrite its own plan in place as environment feedback comes in, instead of committing to a static plan or replanning from scratch, beating baselines on ALFWorld and MiniWoB++ while using up to 600x fewer samples.

- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290) · 2023-05
  - `arxiv:2305.18290` · cited by 1: BK
  - summary: Preference learning without a separate reward model; now the default alignment recipe.

- [Ghost in the Minecraft: Generally Capable Agents for Open-World Environments via Large Language Models with Text-based Knowledge and Memory](https://arxiv.org/abs/2305.17144) · 2023-05
  - `arxiv:2305.17144` · cited by 1: ZJ
  - summary: Text knowledge and memory for open-world capability.

- [Knowledge-enhanced Agents for Interactive Text Games](https://arxiv.org/abs/2305.05091) · 2023-05
  - `arxiv:2305.05091` · cited by 1: ZJ
  - summary: Injects prior knowledge — memory of past correct actions and known object affordances — into both RL and LLM agents playing text-based games, comparing injection strategies like knowledge graphs versus input augmentation across ScienceWorld's ten tasks.

- [Language Models Meet World Models: Embodied Experiences Enhance Language Models](https://arxiv.org/abs/2305.10626.pdf) · 2023-05
  - `arxiv:2305.10626` · cited by 2: LJ, ZJ
  - summary: Finetunes an LLM on embodied experiences an agent gathers in a physical-world simulator, using EWC and LoRA to add object-permanence and planning without erasing general language ability, letting small models match ChatGPT on 18 tasks.

- [Plan, Eliminate, and Track -- Language Models are Good Teachers for Embodied Agents](https://arxiv.org/abs/2305.02412) · 2023-05
  - `arxiv:2305.02412` · cited by 1: ZJ
  - summary: Splits embodied task-following into three LLM-driven steps — break the goal into sub-tasks, mask out irrelevant objects from the observation, check off sub-tasks as done — for a 15% jump over prior state of the art on generalizing to human-phrased goals in AlfWorld.

- [Plan-and-Execute Agents](https://blog.langchain.com/plan-and-execute-agents/) · 2023-05
  - `url:https://blog.langchain.com/plan-and-execute-agents` · cited by 1: HE
  - summary: Separates one-shot planning from execution, replanning only when needed.

- [Plan-and-Solve Prompting: Improving Zero-Shot Chain-of-Thought Reasoning by Large Language Models](https://arxiv.org/abs/2305.04091) · 2023-05
  - `arxiv:2305.04091` · cited by 1: ZJ
  - summary: Fixes zero-shot chain-of-thought's habit of skipping steps by first prompting the model to write an explicit subtask plan and then execute it, beating Zero-shot-CoT across ten reasoning datasets and matching 8-shot CoT on math with no exemplars at all.

- [Reasoning with Language Model is Planning with World Model](https://arxiv.org/abs/2305.14992) · 2023-05
  - `arxiv:2305.14992` · cited by 1: ZJ
  - summary: RAP: repurposes the LLM as both world model and reasoning agent under MCTS.

- [SwiftSage: A Generative Agent with Fast and Slow Thinking for Complex Interactive Tasks](https://arxiv.org/abs/2305.17390) · 2023-05
  - `arxiv:2305.17390` · cited by 1: ZJ
  - summary: Fast intuitive module plus slow deliberate module for complex interactive tasks.

- [Tree of Thoughts: Deliberate Problem Solving with Large Language Models](https://arxiv.org/abs/2305.10601) · 2023-05
  - `arxiv:2305.10601` · cited by 1: ZJ
  - summary: Explores multiple reasoning branches with lookahead and backtracking instead of committing to one chain.

- [Voyager: An Open-Ended Embodied Agent with Large Language Models](https://arxiv.org/abs/2305.16291) · 2023-05
  - `arxiv:2305.16291` · cited by 1: ZJ
  - summary: Lifelong Minecraft agent that writes and stores executable skills, building a reusable skill library.

- [Enabling Intelligent Interactions between an Agent and an LLM: A Reinforcement Learning Approach](https://arxiv.org/abs/2306.03604) · 2023-06
  - `arxiv:2306.03604` · cited by 1: ZJ
  - summary: Trains a small RL policy to decide when an agent actually needs to pay for a query to an expensive LLM for new high-level instructions versus keep following its current plan, cutting interaction costs on MiniGrid and Habitat without hurting success rate.

- [RecAgent: A Novel Simulation Paradigm for Recommender Systems](https://arxiv.org/abs/2306.02552) · 2023-06
  - `arxiv:2306.02552` · cited by 1: ZJ
  - summary: User-behaviour simulation for recommender research.

- [A Real-World WebAgent with Planning, Long Context Understanding, and Program Synthesis](https://arxiv.org/abs/2307.12856) · 2023-07
  - `arxiv:2307.12856` · cited by 1: ZJ
  - summary: WebAgent: HTML summarization plus program synthesis on live sites.

- [Towards A Unified Agent with Foundation Models](https://arxiv.org/abs/2307.09668) · 2023-07
  - `arxiv:2307.09668` · cited by 1: ZJ
  - summary: Uses a language/vision-language model as the reasoning core of an RL agent — driving exploration, skill scheduling and reuse of offline data through one interface instead of separate bespoke algorithms — tested on a sparse-reward robotic stacking task.

- [ExpeL: LLM Agents Are Experiential Learners](https://arxiv.org/abs/2308.10144) · 2023-08
  - `arxiv:2308.10144` · cited by 1: ZJ
  - summary: Extracts cross-task insights from past trajectories without gradient updates.

- [Retroformer: Retrospective Large Language Agents with Policy Gradient Optimization](https://arxiv.org/abs/2308.02151) · 2023-08
  - `arxiv:2308.02151` · cited by 1: ZJ
  - summary: Trains a separate retrospective model with policy gradient to summarize why a language agent's past attempts failed and rewrite its prompt accordingly, so its plans keep improving across a task instead of staying static like plain verbal-feedback methods.

- [SelfCheck: Using LLMs to Zero-Shot Check Their Own Step-by-Step Reasoning](https://arxiv.org/abs/2308.00436) · 2023-08
  - `arxiv:2308.00436` · cited by 1: ZJ
  - summary: Model checks its own reasoning steps without external supervision.

- [TPTU: Large Language Model-based AI Agents for Task Planning and Tool Usage](https://arxiv.org/abs/2308.03427) · 2023-08
  - `arxiv:2308.03427` · cited by 1: LJ
  - summary: Proposes a structured framework for LLM agents with one-step and sequential agent variants and evaluates multiple LLMs on task-planning-plus-tool-use, establishing the baseline TPTU-v2 later extends.

- [Chain-of-Verification Reduces Hallucination in Large Language Models](https://arxiv.org/abs/2309.11495) · 2023-09
  - `arxiv:2309.11495` · cited by 1: BK
  - summary: Drafts, plans verification questions, answers them independently, then revises.

- [Large Language Models as Optimizers](https://arxiv.org/abs/2309.03409) · 2023-09
  - `arxiv:2309.03409` · cited by 1: BK
  - summary: OPRO: the model proposes successive solutions from an optimization trajectory.

- [Self-driven Grounding: Large Language Model Agents with Automatical Language-aligned Skill Learning](https://arxiv.org/abs/2309.01352) · 2023-09
  - `arxiv:2309.01352` · cited by 1: ZJ
  - summary: Has the LLM hypothesize subgoals for a task, verify them by trying them in the environment, then bank the verified ones as reusable skills — matches imitation-learning baselines on BabyAI's hardest tasks with far fewer demonstrations.

- [TaskWeaver](https://github.com/microsoft/TaskWeaver) · 2023-09
  - `gh:microsoft/taskweaver` · cited by 2: HE, KY
  - summary: Code-first planner/executor split with plugins for domain knowledge.

- [Large Language Models Cannot Self-Correct Reasoning Yet](https://arxiv.org/abs/2310.01798) · 2023-10
  - `arxiv:2310.01798` · cited by 1: BK
  - summary: Intrinsic self-correction without external feedback often degrades accuracy.

- [LATS: Language Agent Tree Search](https://arxiv.org/abs/2310.04406) · 2023-10
  - `arxiv:2310.04406` · cited by 1: HE
  - summary: MCTS over agent trajectories with environment feedback as the search signal.

- [LEO: An Embodied Generalist Agent in 3D World](https://arxiv.org/abs/2311.12871) · 2023-11
  - `arxiv:2311.12871` · cited by 1: ZJ
  - summary: LEO: single model across 3D perception, reasoning and action.

- [TPTU-v2: Boosting Task Planning and Tool Usage of Large Language Model-based Agents in Real-world Systems](http://arxiv.org/abs/2311.11315) · 2023-11
  - `arxiv:2311.11315` · cited by 1: LJ
  - summary: Adds an API retriever (to fit within token limits), a fine-tuned planner, and an adaptive demo selector (for hard-to-distinguish APIs) on top of TPTU, validated on a real commercial system as well as an open academic benchmark.

- [Chain of Code: Reasoning with a Language Model-Augmented Code Emulator](https://arxiv.org/abs/2312.04474) · 2023-12
  - `arxiv:2312.04474` · cited by 1: ZJ
  - summary: Interleaves real execution with an LM emulating unrunnable code.

- [ReST meets ReAct: Self-Improvement for Multi-Step Reasoning LLM Agent](https://arxiv.org/abs/2312.10003) · 2023-12
  - `arxiv:2312.10003` · cited by 1: ZJ
  - summary: Bootstraps a ReAct-style reason-and-act agent by iteratively fine-tuning it on its own past trajectories with AI feedback, distilling a small model that matches a much larger prompted one on multi-step QA with two orders of magnitude fewer parameters.

- [E2CL: Exploration-based Error Correction Learning for Embodied Agents](https://aclanthology.org/2024.findings-emnlp.448/) · 2024
  - `acl:2024.findings-emnlp.448` · cited by 1: ZJ
  - summary: Trains embodied agents to learn from their own exploration mistakes, using both teacher-guided and unsupervised exploration, so the agent gets better at catching and self-correcting infeasible actions rather than just imitating expert trajectories.

- [Iterative Translation Refinement with Large Language Models](https://aclanthology.org/2024.eamt-1.17.pdf) · 2024
  - `acl:2024.eamt-1.17.pdf` · cited by 1: LJ
  - summary: Iteratively re-prompting an LLM to critique and refine its own translation improves fluency and naturalness by human judgment even though string-matching metrics (which reward matching a fixed reference) go down, showing self-refinement only pays off when it's grounded in the source text and starts from a decent first draft.

- [Large Language Models lack essential metacognition for reliable medical reasoning](https://doi.org/10.1038/s41467-024-55628-6) · 2024
  - `url:https://doi.org/10.1038/s41467-024-55628-6` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [Refining Guideline Knowledge for Agent Planning Using Textgrad](https://www.computer.org/csdl/proceedings-article/ickg/2024/088200a102/24sKrMSCxr2) · 2024
  - `url:https://computer.org/csdl/proceedings-article/ickg/2024/088200a102/24sKrMSCxr2` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [AutoAct: Automatic Agent Learning from Scratch via Self-Planning](https://arxiv.org/abs/2401.05268) · 2024-01
  - `arxiv:2401.05268` · cited by 2: LJ, ZJ
  - summary: Synthesizes its own trajectories with no external supervision.

- [Planning, Creation, Usage: Benchmarking LLMs for Comprehensive Tool Utilization in Real-World Complex Scenarios](https://arxiv.org/abs/2401.17167) · 2024-01
  - `arxiv:2401.17167` · cited by 1: LJ
  - summary: Planning, creation and usage across the whole tool pipeline without a fixed toolset.

- [SeeClick: Harnessing GUI Grounding for Advanced Visual GUI Agents](https://arxiv.org/abs/2401.10935) · 2024-01
  - `arxiv:2401.10935` · cited by 1: ZJ
  - summary: Drives GUI agents purely from screenshots instead of parsed HTML or accessibility trees, pretraining specifically for grounding — locating the right element from an instruction — and shows grounding accuracy is what actually predicts downstream task success.

- [Self-Contrast: Better Reflection Through Inconsistent Solving Perspectives](https://arxiv.org/abs/2401.02009) · 2024-01
  - `arxiv:2401.02009` · cited by 1: ZJ
  - summary: Contrasts divergent solution attempts to locate real errors.

- [Agent-Pro: Learning to Evolve via Policy-Level Reflection and Optimization](https://arxiv.org/pdf/2402.17574) · 2024-02
  - `arxiv:2402.17574` · cited by 1: ZJ
  - summary: Reflects at policy level rather than per-action.

- [Beyond A\: Better Planning with Transformers via Search Dynamics Bootstrapping](https://arxiv.org/abs/2402.14083) · 2024-02
  - `arxiv:2402.14083` · cited by 1: BK
  - summary: Trains on search dynamics, not just solutions.

- [Chain-of-Thought Empowers Transformers to Solve Inherently Serial Problems](https://arxiv.org/abs/2402.12875) · 2024-02
  - `arxiv:2402.12875` · cited by 1: BK
  - summary: Theoretical account of why intermediate tokens add expressive power.

- [Chain-of-Thought Reasoning Without Prompting](https://arxiv.org/abs/2402.10200) · 2024-02
  - `arxiv:2402.10200` · cited by 1: BK
  - summary: Recovers CoT paths by decoding alternatives rather than prompting.

- [Empowering Large Language Model Agents through Action Learning](https://arxiv.org/abs/2402.15809) · 2024-02
  - `arxiv:2402.15809` · cited by 1: ZJ
  - summary: Lets an LLM agent write and revise its own action set as Python functions based on which actions failed during training, instead of being stuck with a fixed action space — a 32% jump over ReAct+Reflexion on AlfWorld.

- [OS-Copilot: Towards Generalist Computer Agents with Self-Improvement](https://arxiv.org/abs/2402.07456) · 2024-02
  - `arxiv:2402.07456` · cited by 1: ZJ
  - summary: Builds an agent that acts across an entire OS — web, terminal, files, third-party apps — instead of one app at a time, accumulating skills from past tasks and beating prior methods by 35% on the GAIA assistant benchmark.

- [Premise Order Matters in Reasoning with Large Language Models](https://arxiv.org/abs/2402.08939) · 2024-02
  - `arxiv:2402.08939` · cited by 1: BK
  - summary: Reordering premises alone changes accuracy substantially.

- [TravelPlanner: A Benchmark for Real-World Planning with Language Agents](https://arxiv.org/pdf/2402.01622.pdf) · 2024-02
  - `arxiv:2402.01622` · cited by 1: ZJ
  - summary: Real-world constrained planning; famously low success rates.

- [AutoGuide: Automated Generation and Selection of State-Aware Guidelines for Large Language Model Agents](https://arxiv.org/abs/2403.08978) · 2024-03
  - `arxiv:2403.08978` · cited by 1: ZJ
  - summary: Mines offline agent trajectories into short conditional guidelines ('in this state, do this') instead of raw few-shot demonstrations, so a web-navigation agent gets relevant guidance exactly when the situation calls for it.

- [Enhancing the General Agent Capabilities of Low-Parameter LLMs through Tuning and Multi-Branch Reasoning](https://arxiv.org/abs/2403.19962) · 2024-03
  - `arxiv:2403.19962` · cited by 1: LJ
  - summary: Shows supervised fine-tuning on GPT-4-constructed agent-specific data sharply cuts hallucination and formatting errors for 7B/13B open models used as agents, and that multi-path reasoning plus task decomposition further boosts their AgentBench performance.

- [SOTOPIA-π: Interactive Learning of Socially Intelligent Language Agents](https://arxiv.org/abs/2403.08715) · 2024-03
  - `arxiv:2403.08715` · cited by 1: ZJ
  - summary: Trains a 7B language agent's social skills via behavior cloning plus self-reinforcement on LLM-rated interaction data, closing the gap to a GPT-4-based agent on social-goal completion, while finding LLM judges overrate agents trained specifically against that same judging signal.

- [Iterative Reasoning Preference Optimization](https://arxiv.org/abs/2404.19733) · 2024-04
  - `arxiv:2404.19733` · cited by 1: BK
  - summary: Preference optimization over competing CoT candidates.

- [Agent Planning with World Knowledge Model](https://arxiv.org/abs/2405.14205) · 2024-05
  - `arxiv:2405.14205` · cited by 1: ZJ
  - summary: Parametric world-knowledge model guiding global and local planning.

- [Can Graph Learning Improve Planning in LLM-based Agents?](https://arxiv.org/abs/2405.19119) · 2024-05
  - `arxiv:2405.19119` · cited by 1: ZJ
  - summary: Treats task planning as choosing a path through a subtask-dependency graph, argues LLMs' attention and autoregressive bias makes them bad at that kind of graph decision, and swaps in a graph neural network to pick the path instead — the gain grows with graph size and beats prompt-only baselines even untrained.

- [Devil's Advocate: Anticipatory Reflection for LLM Agents](https://arxiv.org/abs/2405.16334) · 2024-05
  - `arxiv:2405.16334` · cited by 2: LJ, ZJ
  - summary: Gives an LLM agent three introspective interventions (anticipatory reflection before acting, post-action alignment checks, and post-completion review) in a zero-shot approach, raising WebArena success rate 3.5 points over prior zero-shot methods while cutting trial-and-error revisions 45%.

- [Faithful Logical Reasoning via Symbolic Chain-of-Thought](https://arxiv.org/abs/2405.18357) · 2024-05
  - `arxiv:2405.18357` · cited by 1: ZJ
  - summary: Has the LLM translate a logic problem into symbolic form, work out the solution step by step using formal deduction rules, then verify its own translation and reasoning chain — beats plain chain-of-thought on first-order-logic and constraint benchmarks.

- [Grokked Transformers are Implicit Reasoners: A Mechanistic Journey to the Edge of Generalization](https://arxiv.org/abs/2405.15071) · 2024-05
  - `arxiv:2405.15071` · cited by 1: BK
  - summary: Implicit reasoning emerges past grokking, with sharp generalization limits.

- [Intelligent Go-Explore: Standing on the Shoulders of Giant Foundation Models](https://arxiv.org/abs/2405.15143) · 2024-05
  - `arxiv:2405.15143` · cited by 1: ZJ
  - summary: Replaces Go-Explore's hand-coded 'is this state interesting' heuristics with a foundation model's judgment of novelty, succeeding on exploration tasks where Reflexion-style agents completely fail.

- [Alice in Wonderland：Simple Tasks Showing Complete Reasoning Breakdown in State-Of-the-Art Large Language Models](https://arxiv.org/abs/2406.02061) · 2024-06
  - `arxiv:2406.02061` · cited by 1: ZJ
  - summary: Shows GPT-4, Claude 3 Opus and other top models collapse on a simple grade-school word problem, with wildly inconsistent accuracy across trivial rephrasings and confident, plausible-sounding wrong explanations that chain-of-thought and self-reevaluation don't fix.

- [Symbolic Learning Enables Self-Evolving Agents](https://arxiv.org/abs/2406.18532v1) · 2024-06
  - `arxiv:2406.18532` · cited by 1: ZJ
  - summary: Agent-symbolic learning treating prompts and pipelines as learnable.

- [TextGrad: Automatic “Differentiation” via Text](https://arxiv.org/abs/2406.07496) · 2024-06
  - `arxiv:2406.07496` · cited by 1: ZJ
  - summary: Backpropagates natural-language feedback through compound systems.

- [Unpacking DPO and PPO: Disentangling Best Practices for Learning from Preference Feedback](https://arxiv.org/abs/2406.09279) · 2024-06
  - `arxiv:2406.09279` · cited by 1: BK
  - summary: Disentangles what actually drives preference-learning gains.

- [WorkArena++: Towards Compositional Planning and Reasoning-based Common Knowledge Work Tasks](https://arxiv.org/abs/2407.05291) · 2024-07
  - `arxiv:2407.05291` · cited by 1: BK
  - summary: Compositional planning and reasoning extension.

- [Perceive, Reflect, and Plan: Designing LLM Agent for Goal-Directed City Navigation without Instructions](http://arxiv.org/abs/2408.04168) · 2024-08
  - `arxiv:2408.04168` · cited by 1: LJ
  - summary: Fine-tunes a vision-language model to perceive landmark direction/distance for goal-directed city navigation with no explicit instructions, adding a memory-based reflection step and a planning stage that together fix the repeated-visit, short-sighted behavior of a bare react-on-observation baseline.

- [Composing Global Optimizers to Reasoning Tasks via Algebraic Objects in Neural Nets](https://arxiv.org/abs/2410.01779) · 2024-10
  - `arxiv:2410.01779` · cited by 1: BK
  - summary: Algebraic structure of solutions in small reasoning networks.

- [Dualformer: Controllable Fast and Slow Thinking by Learning with Randomized Reasoning Traces](https://arxiv.org/abs/2410.09918) · 2024-10
  - `arxiv:2410.09918` · cited by 1: BK
  - summary: Randomized reasoning traces yield a controllable fast/slow switch.

- [Is Your LLM Secretly a World Model of the Internet? Model-Based Planning for Web Agents](https://arxiv.org/abs/2411.06559) · 2024-11
  - `arxiv:2411.06559` · cited by 1: BK
  - summary: Model-based planning with an LLM world model for web agents.

- [PlanCritic: Formal Planning with Human Feedback](https://arxiv.org/abs/2412.00300) · 2024-12
  - `arxiv:2412.00300` · cited by 1: LJ
  - summary: Uses an evolutionary algorithm plus a trained LSTM validator to repair imprecise LLM-generated PDDL goal specifications against the original natural-language intent, improving adherence over plans generated from a single LLM translation pass.

- [KnowAgent: Knowledge-Augmented Planning for LLM-Based Agents](https://arxiv.org/pdf/2403.03101) · 2024/03
  - `arxiv:2403.03101` · cited by 2: LJ, ZJ
  - summary: Action knowledge base plus self-learning to curb planning hallucination.

- [Planning with Multi-Constraints via Collaborative Language Agents](https://aclanthology.org/2025.coling-main.672/) · 2025
  - `acl:2025.coling-main.672` · cited by 1: LJ
  - summary: Decomposes constraint-heavy planning into a hierarchy of subordinate tasks across a zero-shot multi-agent pipeline, reaching 42.68% success on TravelPlanner versus GPT-4's 2.92%, and working even with an 8B model as the planning core.

- [STeCa: Step-level Trajectory Calibration for LLM Agent Learning](https://arxiv.org/abs/2502.14276) · 2025-02
  - `arxiv:2502.14276` · cited by 2: LJ, ZJ
  - summary: Builds calibrated trajectories via step-level reward comparison and reflection.

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

- [4D-ARE: 4-Dimensional Attribution-Driven Agent Requirements Engineering](https://arxiv.org/pdf/2601.04556v1) · 2026-01
  - `arxiv:2601.04556` · cited by 1: VA
  - summary: 4D-ARE gives you a four-dimension framework (Results, Process, Support, Long-term, grounded in Pearl's causal hierarchy) for specifying what an agent should reason about at design time, not just how it reasons at runtime, because a ReAct agent that answers "why is completion rate 80%" with metrics instead of causes is missing a requirements layer, not a reasoning layer.

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

- [Can We Predict Before Executing Machine Learning Agents?](https://arxiv.org/pdf/2601.05930v1) · 2026-01
  - `arxiv:2601.05930` · cited by 1: VA
  - summary: FOREAGENT skips the expensive step of actually running ML experiments by having an LLM predict which candidate solution will work best from a data-analysis report first, hitting 61.5% prediction accuracy and, with a predict-then-verify loop, converging 6x faster while still beating execution-based baselines by 6%.

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

- [MAXS: Meta-Adaptive Exploration with LLM Agents](https://arxiv.org/pdf/2601.09259v1) · 2026-01
  - `arxiv:2601.09259` · cited by 1: VA
  - summary: MAXS adds a lookahead step to LLM agent tool-calling that scores candidate reasoning paths on consistency and trend before committing, then halts further rollouts once paths converge, beating baselines on both accuracy and inference cost across three models and five datasets.

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

- [ProAct: Agentic Lookahead in Interactive Environments](https://arxiv.org/pdf/2602.05327v1) · 2026-02
  - `arxiv:2602.05327` · cited by 1: VA
  - summary: ProAct trains agents on environment-grounded lookahead trajectories and adds Monte-Carlo rollouts to the policy gradient to fight compounding simulation errors in long-horizon planning, letting a 4B model beat all open-source baselines on 2048 and Sokoban and generalize to unseen environments.

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

- [Beyond Offline A/B Testing: Context-Aware Agent Simulation for Recommender System Evaluation](https://arxiv.org/abs/2604.09549) · 2026-04
  - `arxiv:2604.09549` · cited by 2: VA, ZJ
  - summary: Simulates believable recommender-system users by anchoring their interactions in generated daily-life scenarios (when/where/why they'd engage) and enforcing consistency between an agent's stated thoughts and its actions, showing recommender parameters tuned against the simulation improve real-world engagement.

- [DeepSeek-Reasonix](https://github.com/esengine/DeepSeek-Reasonix) · 2026-04
  - `gh:esengine/deepseek-reasonix` · cited by 1: HE
  - summary: A DeepSeek-native terminal coding agent engineered around prefix-cache stability to keep token costs low, distributed as a single dependency-free static binary with config-driven, multi-model, plugin-extensible design.

## Tools & Undated

12 entries with no date derivable from their source (GitHub repos, blog posts, etc.).

- [Agent Planning with World Knowledge Model](https://openreview.net/pdf?id=j6kJSS9O6I)
  - `openreview:j6kJSS9O6I` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [AutoAgents](https://github.com/AutoLLM/AutoAgents)
  - `gh:autollm/autoagents` · cited by 1: ZJ
  - related: <https://github.com/AntonOsika/gpt-engineer>
  - summary: Adds a planning stage in front of ReAct-style tool use, so the agent first decides which specialized sub-agents/tools a question needs before executing, aimed at improving multi-hop question answering over plain ReAct.

- [CRITIC: Large Language Models Can Self-Correct with Tool-Interactive Critiquing](https://openreview.net/pdf?id=Sx038qxjek)
  - `openreview:Sx038qxjek` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [Enhancing Robot Task Planning: Integrating Environmental Information and Feedback Insights through Large Language Models](https://ieeexplore.ieee.org/abstract/document/10661782)
  - `url:https://ieeexplore.ieee.org/abstract/document/10661782` · cited by 1: LJ
  - summary: NEEDS-SOURCE

- [Prompt4ReasoningPapers](https://github.com/zjunlp/Prompt4ReasoningPapers)
  - `gh:zjunlp/prompt4reasoningpapers` · cited by 1: ZJ
  - summary: A maintained paper list tracking LLM reasoning-via-prompting research — chain-of-thought variants, knowledge- and tool-augmented methods, plus benchmarks — worth bookmarking as a standing index rather than reading for a single result.

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

- [Tree Search for Language Model Agents](https://jykoh.com/search-agents)
  - `url:https://jykoh.com/search-agents` · cited by 1: BK
  - summary: Best-first tree search over real interactive web environments.

- [V-STaR: Training Verifiers for Self-Taught Reasoners](https://openreview.net/pdf?id=stmqBSW2dV)
  - `openreview:stmqBSW2dV` · cited by 1: LJ
  - summary: Trains a verifier on *both* correct and incorrect self-generated solutions.

- [XAgent](https://github.com/OpenBMB/XAgent)
  - `gh:openbmb/xagent` · cited by 1: KY
  - summary: Autonomous agent built around a dispatcher/planner/actor split so it can decompose complex, long-horizon tasks, refine its plan as it goes, and run tool calls in a sandboxed workspace.
