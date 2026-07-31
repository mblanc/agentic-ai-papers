# context-engineering

35 entries.

## Timeline

30 dated entries, oldest first.

- [LLMLingua](https://github.com/microsoft/LLMLingua) · 2023-07
  - `gh:microsoft/llmlingua` · cited by 1: HE
  - summary: Prompt compression up to 20×; v2 adds 3–6× speedup for latency-sensitive loops.

- [Context7](https://github.com/upstash/context7) · 2025-03
  - `gh:upstash/context7` · cited by 1: HE
  - summary: Injects version-specific library docs to stop hallucinated APIs from stale training data.

- [Awesome Context Engineering](https://github.com/Meirtz/Awesome-Context-Engineering) · 2025-07
  - `gh:meirtz/awesome-context-engineering` · cited by 1: HE
  - summary: A curated survey of context-engineering work spanning RAG, memory, agent protocols, and production patterns, tracking the shift from static prompting to dynamic per-request context assembly.

- [Effective Context Engineering for AI Agents](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) · 2025-09
  - `url:https://anthropic.com/engineering/effective-context-engineering-for-ai-agents` · cited by 1: HE
  - summary: Treats the whole context state as a finite curated resource, not prompt wording.

- [Active Context Compression: Autonomous Memory Management in LLM Agents](https://arxiv.org/abs/2601.07190) · 2026-01
  - `arxiv:2601.07190` · cited by 2: HE, VA
  - summary: A "Focus Agent" decides when to consolidate and prune; 22.7% token cut, no accuracy loss.

- [CEDAR: Context Engineering for Agentic Data Science](https://arxiv.org/pdf/2601.06606v1) · 2026-01
  - `arxiv:2601.06606` · cited by 1: VA
  - summary: Structures a data-science agent's context as interleaved plan-and-code blocks written by separate LLM agents and keeps raw data local, injecting only aggregate statistics, so Kaggle-style tasks stay within context limits.

- [headroom](https://github.com/chopratejas/headroom) · 2026-01
  - `gh:chopratejas/headroom` · cited by 1: HE
  - summary: Compresses tool outputs, logs and RAG chunks before they hit context; 60–95% reduction.

- [Meta Context Engineering via Agentic Skill Evolution](https://arxiv.org/pdf/2601.21557v2) · 2026-01
  - `arxiv:2601.21557` · cited by 1: VA
  - summary: Replaces hand-crafted context-engineering harnesses with a bi-level loop: a meta-agent evolves the context-engineering skills while a base-agent applies them and optimizes context as editable files and code, averaging 16.9% over prior agentic methods.

- [OpenViking](https://github.com/volcengine/OpenViking) · 2026-01
  - `gh:volcengine/openviking` · cited by 1: HE
  - summary: Context database unifying memory, resources and skills behind a filesystem paradigm.

- [SWE-Pruner: Self-Adaptive Context Pruning for Coding Agents](https://arxiv.org/pdf/2601.16746v2) · 2026-01
  - `arxiv:2601.16746` · cited by 1: VA
  - summary: Prunes a coding agent's context with a 0.6B 'skimmer' model that keeps only the lines relevant to an explicit per-step goal, cutting 23-54% of tokens on SWE-Bench Verified while raising success rates.

- [Trellis](https://github.com/mindfold-ai/Trellis) · 2026-01
  - `gh:mindfold-ai/trellis` · cited by 1: HE
  - summary: Progressive spec loading to replace monolithic CLAUDE.md, with cross-platform adapters.

- [A-RAG: Scaling Agentic Retrieval-Augmented Generation via Hierarchical Retrieval Interfaces](https://arxiv.org/abs/2602.03442) · 2026-02
  - `arxiv:2602.03442` · cited by 1: HE
  - summary: Reframes retrieval as tool calls in the loop rather than pipeline-time injection.

- [codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) · 2026-02
  - `gh:deusdata/codebase-memory-mcp` · cited by 1: HE
  - summary: Tree-sitter AST knowledge graph over 66 languages, replacing grep/read cycles.

- [CompactRAG: Reducing LLM Calls and Token Overhead in Multi-Hop Question Answering](https://arxiv.org/pdf/2602.05728v1) · 2026-02
  - `arxiv:2602.05728` · cited by 1: VA
  - summary: Offline atomic QA pairs resolve multi-hop in two LLM calls regardless of hops.

- [context-mode](https://github.com/mksglu/context-mode) · 2026-02
  - `gh:mksglu/context-mode` · cited by 1: HE
  - summary: Sandboxes bulky tool output outside the window, retrieving fragments via BM25.

- [Making Agent-Friendly Pages with Content Negotiation](https://vercel.com/blog/making-agent-friendly-pages-with-content-negotiation) · 2026-02
  - `url:https://vercel.com/blog/making-agent-friendly-pages-with-content-negotiation` · cited by 1: HE
  - summary: Serve `text/markdown` to agents so boilerplate never enters context.

- [SPARC-RAG: Adaptive Sequential-Parallel Scaling with Context Management for Retrieval-Augmented Generation](https://arxiv.org/pdf/2602.00083v1) · 2026-02
  - `arxiv:2602.00083` · cited by 1: VA
  - summary: Sequential and parallel inference-time scaling under unified context management.

- [Structured Context Engineering for File-Native Agentic Systems](https://arxiv.org/pdf/2602.05447v1) · 2026-02
  - `arxiv:2602.05447` · cited by 1: VA
  - summary: A 9,649-run study of how to structure context for data-querying agents that finds file-based retrieval helps only frontier models, serialization format (YAML/JSON/Markdown/TOON) barely moves accuracy, and model capability dwarfs both, so context structure should track model tier rather than a universal best practice.

- [Autonomous Context Compression](https://blog.langchain.com/autonomous-context-compression/) · 2026-03
  - `url:https://blog.langchain.com/autonomous-context-compression` · cited by 1: HE
  - summary: Moves compression from threshold-triggered to agent-triggered, avoiding mid-subtask corruption.

- [LLM Readiness Harness: Evaluation, Observability, and CI Gates for LLM/RAG Applications](https://arxiv.org/abs/2603.27355) · 2026-03
  - `arxiv:2603.27355` · cited by 1: HE
  - summary: Deployment-blocking eval gates and CI patterns for LLM/RAG apps.

- [PRO-LONG](https://github.com/alexisfox7/PRO-LONG) · 2026-03
  - `gh:alexisfox7/pro-long` · cited by 1: HE
  - summary: Gives long-horizon agents memory by appending every observation and action to a structured log they search programmatically, reaching 97.4% on ARC-AGI-3 with far fewer tokens than specialized retrieval and arguing code-based recall can beat complex retrieval.

- [Token Savior](https://github.com/Mibayy/token-savior) · 2026-03
  - `gh:mibayy/token-savior` · cited by 1: HE
  - summary: Symbol-level codebase index so agents navigate by pointer; 77% fewer active tokens.

- [ByteRover: Agent-Native Memory Through LLM-Curated Hierarchical Context](https://arxiv.org/abs/2604.01599) · 2026-04
  - `arxiv:2604.01599` · cited by 1: HE
  - summary: Model learns to weight information importance across hierarchy levels.

- [DESIGN.md](https://github.com/google-labs-code/design.md) · 2026-04
  - `gh:google-labs-code/design.md` · cited by 1: HE
  - summary: Machine-readable design tokens plus prose rationale so agents respect a design system.

- [dirac](https://github.com/dirac-run/dirac) · 2026-04
  - `gh:dirac-run/dirac` · cited by 1: HE
  - summary: Hash-anchored edits and AST manipulation for surgical context curation; 50–80% cost cut.

- [MinishLab/semble](https://github.com/MinishLab/semble) · 2026-04
  - `gh:minishlab/semble` · cited by 1: HE
  - summary: Natural-language code search replacing grep+read; ~98% token cut, CPU-only.

- [Context Pruning for Coding Agents via Multi-Rubric Latent Reasoning](https://arxiv.org/abs/2605.15315) · 2026-05
  - `arxiv:2605.15315` · cited by 1: HE
  - summary: Splits relevance into semantic evidence and dependency support instead of one score.

- [harness-experimental](https://github.com/hoangnb24/harness-experimental) · 2026-05
  - `gh:hoangnb24/harness-experimental` · cited by 1: HE
  - summary: Turns a repo into an agent-ready workspace via structured AGENTS/HARNESS/FEATURE_INTAKE files.

- [Mirage](https://github.com/strukto-ai/mirage) · 2026-05
  - `gh:strukto-ai/mirage` · cited by 1: HE
  - summary: Mounts S3, Slack, Gmail, GitHub and Redis as one virtual filesystem so agents use bash.

- [OpenWiki](https://github.com/langchain-ai/openwiki) · 2026-06
  - `gh:langchain-ai/openwiki` · cited by 1: HE
  - summary: A CLI that generates and maintains a codebase or knowledge-base wiki formatted for agent consumption, so an agent reads a synthesized local doc set instead of re-deriving a repo's structure each session.

## Tools & Undated

5 entries with no date derivable from their source (GitHub repos, blog posts, etc.).

- [Claude Code Compaction: How Context Compression Works](https://okhlopkov.com/claude-code-compaction-explained/)
  - `url:https://okhlopkov.com/claude-code-compaction-explained` · cited by 1: HE
  - summary: What survives compaction and what silently doesn't; keep critical rules in the system prompt.

- [Compaction — Claude API Docs](https://platform.claude.com/docs/en/build-with-claude/compaction)
  - `url:https://platform.claude.com/docs/en/build-with-claude/compaction` · cited by 1: HE
  - summary: Server-side summarization of older context; 84% token reduction on a 100-turn eval.

- [Context Engineering for Reliable AI Agents: Lessons from Building Azure SRE Agent](https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200/)
  - `url:https://techcommunity.microsoft.com/blog/appsonazureblog/context-engineering-lessons-from-building-azure-sre-agent/4481200` · cited by 1: HE
  - summary: Replacing 100+ bespoke tools with a filesystem raised "Intent Met" from 45% to 75%.

- [Harness Engineering](https://openai.com/index/harness-engineering/)
  - `url:https://openai.com/index/harness-engineering` · cited by 1: HE
  - summary: OpenAI's framing of harness design as a named discipline for agent-first development.

- [Prompt Caching — Claude API Docs](https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching)
  - `url:https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching` · cited by 1: HE
  - summary: Cache-breakpoint placement as the main cost lever in multi-turn sessions.
