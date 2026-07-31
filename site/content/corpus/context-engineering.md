# context-engineering

35 entries.

## Timeline

11 dated entries, oldest first.

- [Active Context Compression: Autonomous Memory Management in LLM Agents](https://arxiv.org/abs/2601.07190) · 2026-01
  - `arxiv:2601.07190` · cited by 2: HE, VA
  - summary: A "Focus Agent" decides when to consolidate and prune; 22.7% token cut, no accuracy loss.

- [CEDAR: Context Engineering for Agentic Data Science](https://arxiv.org/pdf/2601.06606v1) · 2026-01
  - `arxiv:2601.06606` · cited by 1: VA
  - summary: Structures a data-science agent's context as interleaved plan-and-code blocks written by separate LLM agents and keeps raw data local, injecting only aggregate statistics, so Kaggle-style tasks stay within context limits.

- [Meta Context Engineering via Agentic Skill Evolution](https://arxiv.org/pdf/2601.21557v2) · 2026-01
  - `arxiv:2601.21557` · cited by 1: VA
  - summary: Replaces hand-crafted context-engineering harnesses with a bi-level loop: a meta-agent evolves the context-engineering skills while a base-agent applies them and optimizes context as editable files and code, averaging 16.9% over prior agentic methods.

- [SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents](https://arxiv.org/pdf/2601.16746v2) · 2026-01
  - `arxiv:2601.16746` · cited by 1: VA
  - summary: Prunes a coding agent's context with a 0.6B 'skimmer' model that keeps only the lines relevant to an explicit per-step goal, cutting 23-54% of tokens on SWE-Bench Verified while raising success rates.

- [A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces](https://arxiv.org/abs/2602.03442) · 2026-02
  - `arxiv:2602.03442` · cited by 1: HE
  - summary: Reframes retrieval as tool calls in the loop rather than pipeline-time injection.

- [CompactRAG: Reducing LLM Calls and Token Overhead in Multi-Hop Question Answering](https://arxiv.org/pdf/2602.05728v1) · 2026-02
  - `arxiv:2602.05728` · cited by 1: VA
  - summary: Offline atomic QA pairs resolve multi-hop in two LLM calls regardless of hops.

- [SPARC-RAG: Adaptive Sequential-Parallel Scaling with Context Management for Retrieval-Augmented Generation](https://arxiv.org/pdf/2602.00083v1) · 2026-02
  - `arxiv:2602.00083` · cited by 1: VA
  - summary: Sequential and parallel inference-time scaling under unified context management.

- [Structured Context Engineering for File-Native Agentic Systems](https://arxiv.org/pdf/2602.05447v1) · 2026-02
  - `arxiv:2602.05447` · cited by 1: VA
  - summary: A 9,649-run study of how to structure context for data-querying agents that finds file-based retrieval helps only frontier models, serialization format (YAML/JSON/Markdown/TOON) barely moves accuracy, and model capability dwarfs both, so context structure should track model tier rather than a universal best practice.

- [LLM Readiness Harness: Evaluation, Observability, and CI Gates for LLM/RAG Applications](https://arxiv.org/abs/2603.27355) · 2026-03
  - `arxiv:2603.27355` · cited by 1: HE
  - summary: Deployment-blocking eval gates and CI patterns for LLM/RAG apps.

- [ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context](https://arxiv.org/abs/2604.01599) · 2026-04
  - `arxiv:2604.01599` · cited by 1: HE
  - summary: Model learns to weight information importance across hierarchy levels.

- [Context Pruning for Coding Agents via Multi-Rubric Latent Reasoning](https://arxiv.org/abs/2605.15315) · 2026-05
  - `arxiv:2605.15315` · cited by 1: HE
  - summary: Splits relevance into semantic evidence and dependency support instead of one score.

## Tools & Undated

24 entries with no date derivable from their source (GitHub repos, blog posts, etc.).

- [Autonomous Context Compression](https://blog.langchain.com/autonomous-context-compression/)
  - `url:https://blog.langchain.com/autonomous-context-compression` · cited by 1: HE
  - summary: Moves compression from threshold-triggered to agent-triggered, avoiding mid-subtask corruption.

- [Awesome Context Engineering](https://github.com/Meirtz/Awesome-Context-Engineering)
  - `gh:meirtz/awesome-context-engineering` · cited by 1: HE
  - summary: A curated survey of context-engineering work spanning RAG, memory, agent protocols, and production patterns, tracking the shift from static prompting to dynamic per-request context assembly.

- [Claude Code Compaction: How Context Compression Works](https://okhlopkov.com/claude-code-compaction-explained/)
  - `url:https://okhlopkov.com/claude-code-compaction-explained` · cited by 1: HE
  - summary: What survives compaction and what silently doesn't; keep critical rules in the system prompt.

- [codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp)
  - `gh:deusdata/codebase-memory-mcp` · cited by 1: HE
  - summary: Tree-sitter AST knowledge graph over 66 languages, replacing grep/read cycles.

- [Compaction — Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/compaction)
  - `url:https://platform.claude.com/docs/en/build-with-claude/compaction` · cited by 1: HE
  - summary: Server-side summarization of older context; 84% token reduction on a 100-turn eval.

- [Context Engineering for Reliable AI Agents: Lessons from Building Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200/)
  - `url:https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200` · cited by 1: HE
  - summary: Replacing 100+ bespoke tools with a filesystem raised "Intent Met" from 45% to 75%.

- [context-mode](https://github.com/mksglu/context-mode)
  - `gh:mksglu/context-mode` · cited by 1: HE
  - summary: Sandboxes bulky tool output outside the window, retrieving fragments via BM25.

- [Context7](https://github.com/upstash/context7)
  - `gh:upstash/context7` · cited by 1: HE
  - summary: Injects version-specific library docs to stop hallucinated APIs from stale training data.

- [DESIGN.md](https://github.com/google-labs-code/design.md)
  - `gh:google-labs-code/design.md` · cited by 1: HE
  - summary: Machine-readable design tokens plus prose rationale so agents respect a design system.

- [dirac](https://github.com/dirac-run/dirac)
  - `gh:dirac-run/dirac` · cited by 1: HE
  - summary: Hash-anchored edits and AST manipulation for surgical context curation; 50–80% cost cut.

- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents)
  - `url:https://anthropic.com/engineering/effective-context-engineering-for-ai-agents` · cited by 1: HE
  - summary: Treats the whole context state as a finite curated resource, not prompt wording.

- [Harness Engineering](https://openai.com/index/harness-engineering/)
  - `url:https://openai.com/index/harness-engineering` · cited by 1: HE
  - summary: OpenAI's framing of harness design as a named discipline for agent-first development.

- [harness-experimental](https://github.com/hoangnb24/harness-experimental)
  - `gh:hoangnb24/harness-experimental` · cited by 1: HE
  - summary: Turns a repo into an agent-ready workspace via structured AGENTS/HARNESS/FEATURE_INTAKE files.

- [headroom](https://github.com/chopratejas/headroom)
  - `gh:chopratejas/headroom` · cited by 1: HE
  - summary: Compresses tool outputs, logs and RAG chunks before they hit context; 60–95% reduction.

- [LLMLingua](https://github.com/microsoft/LLMLingua)
  - `gh:microsoft/llmlingua` · cited by 1: HE
  - summary: Prompt compression up to 20×; v2 adds 3–6× speedup for latency-sensitive loops.

- [Making Agent-Friendly Pages with Content Negotiation](https://vercel.com/blog/making-agent-friendly-pages-with-content-negotiation)
  - `url:https://vercel.com/blog/making-agent-friendly-pages-with-content-negotiation` · cited by 1: HE
  - summary: Serve `text/markdown` to agents so boilerplate never enters context.

- [MinishLab/semble](https://github.com/MinishLab/semble)
  - `gh:minishlab/semble` · cited by 1: HE
  - summary: Natural-language code search replacing grep+read; ~98% token cut, CPU-only.

- [Mirage](https://github.com/strukto-ai/mirage)
  - `gh:strukto-ai/mirage` · cited by 1: HE
  - summary: Mounts S3, Slack, Gmail, GitHub and Redis as one virtual filesystem so agents use bash.

- [OpenViking](https://github.com/volcengine/OpenViking)
  - `gh:volcengine/openviking` · cited by 1: HE
  - summary: Context database unifying memory, resources and skills behind a filesystem paradigm.

- [OpenWiki](https://github.com/langchain-ai/openwiki)
  - `gh:langchain-ai/openwiki` · cited by 1: HE
  - summary: A CLI that generates and maintains a codebase or knowledge-base wiki formatted for agent consumption, so an agent reads a synthesized local doc set instead of re-deriving a repo's structure each session.

- [PRO-LONG](https://github.com/alexisfox7/PRO-LONG)
  - `gh:alexisfox7/pro-long` · cited by 1: HE
  - summary: Gives long-horizon agents memory by appending every observation and action to a structured log they search programmatically, reaching 97.4% on ARC-AGI-3 with far fewer tokens than specialized retrieval and arguing code-based recall can beat complex retrieval.

- [Prompt Caching — Claude API Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
  - `url:https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching` · cited by 1: HE
  - summary: Cache-breakpoint placement as the main cost lever in multi-turn sessions.

- [Token Savior](https://github.com/Mibayy/token-savior)
  - `gh:mibayy/token-savior` · cited by 1: HE
  - summary: Symbol-level codebase index so agents navigate by pointer; 77% fewer active tokens.

- [Trellis](https://github.com/mindfold-ai/Trellis)
  - `gh:mindfold-ai/trellis` · cited by 1: HE
  - summary: Progressive spec loading to replace monolithic CLAUDE.md, with cross-platform adapters.
