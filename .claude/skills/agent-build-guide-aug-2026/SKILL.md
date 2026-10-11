---
name: agent-build-guide-aug-2026
description: The "How to Build an AI Agent" Aug 2026 infographic as a working procedure - eight steps (purpose and scope, system prompt, choose LLM, tools and integrations, memory, orchestration, user interface, testing and evals) and the product table (consumer agents, agentic coding tools, no-code builders, frameworks). Use when asked to design or build an agent; run it with /agent-blueprint. Table claims (model names, integration counts) come from the image and are unverified.
---

# 8 steps (each box on the image)
1. **Define purpose and scope** - use case, user needs, success criteria, constraints.
2. **System prompt design** - goals, role/persona, instructions, guardrails.
3. **Choose the LLM** - base model, reasoning effort, context window, cost/latency.
4. **Tools and integrations** - simple local tools, APIs (web, apps, data), MCP servers, an agent as a tool, custom functions.
5. **Memory** - episodic (conversation), working memory, vector DB, SQL/structured DB, file storage.
6. **Orchestration** - routes/workflows, triggers, parameters, message queues, agent-to-agent, error handling.
7. **User interface** - chat, web app, API endpoint, Slack/Discord bot.
8. **Testing and evals** - unit tests, latency tests, quality metrics, iterate and improve.
Order on the image runs 1->8 with 4<->5 and 6->7->8 as the lower rows. Build the eval (8) before you trust the loop.

# Product table (image, Aug 2026)
Consumer agents: ChatGPT (GPT-5.6), Claude (Opus 5; Projects, artifacts, Cowork, 1M context), Perplexity. Agentic coding: Cursor, Windsurf (Cognition, SWE-1.6), Claude Code (Claude 5; agent teams). No-code: Lindy (1,000+ integrations), Zapier Agents (9,000+ apps, human in the loop), n8n (500+ integrations, self-host, open source). Frameworks: LangGraph (graph flows, state, cycles), CrewAI (role-based, 40+ integrations), LlamaIndex (RAG-first).

# In this repo
Command `/agent-blueprint <use case>` runs steps 1-8 and outputs a one-page spec. Agent definition: `.claude/agents/agent-blueprint-designer.md`. See also `build-ai-agent-10-minutes`, `build-claude-agent-7-steps`, `agent-harness-construction`.
