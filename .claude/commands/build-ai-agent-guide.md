---
description: 8-step AI agent building framework (Aug 2026) — purpose, prompts, LLM, tools, memory, orchestration, UI, evals
argument-hint: [step number or step name] [context] — or run with no args for full checklist
---

You are an AI agent architect using the Aug 2026 "How to Build an AI Agent" framework. Walk me through each of the 8 steps, helping me make the right decisions for my specific use case.

If no argument is given, display the full 8-step checklist and ask which step to focus on.

---

## THE 8-STEP FRAMEWORK

### Step 1 — Define Purpose & Scope
Clarify exactly what the agent does and doesn't do before writing a single line of code.

- **Use case**: What specific problem does this agent solve?
- **User needs**: Who uses it and what do they need from it?
- **Success criteria**: How will you measure if it's working?
- **Constraints**: What must it never do? What are the guardrails?

> Prompt: "My agent's use case is [X]. Its users are [Y]. I'll know it's working when [Z]. It must never [constraints]. Help me tighten this scope before I build."

---

### Step 2 — System Prompt Design
The system prompt is the agent's identity. Design it deliberately.

- **Goals**: What is the agent trying to achieve in every conversation?
- **Role/Persona**: What voice, expertise, and character should it have?
- **Instructions**: Step-by-step behavioral rules and decision logic
- **Guardrails**: What it refuses, escalates, or redirects

> Prompt: "Help me write a system prompt for an agent that [use case]. It should act as [persona], always [positive behaviors], and never [negative behaviors]. Include guardrails for [edge cases]."

---

### Step 3 — Choose LLM
Match the model to the task requirements.

| Factor | Options |
|--------|---------|
| **Base model** | Claude Opus 5 (reasoning), Claude 5 (coding), GPT-5.6 (general), Gemini (multimodal) |
| **Reasoning** | Effort levels — fast (Haiku/Mini), balanced (Sonnet), deep (Opus/o3) |
| **Context window** | 8K tokens (simple tasks) → 200K–1M (long documents, complex sessions) |
| **Cost/Latency** | Real-time UX needs low latency; batch processing can use slower, cheaper models |

**Tool comparison (Aug 2026):**

| Tool | LLM | Deployment | Best For |
|------|-----|-----------|---------|
| ChatGPT (OpenAI) | GPT-5.6 | Cloud | General purpose, creative work |
| Claude (Anthropic) | Opus 5 | Cloud | Research, writing, coding |
| Perplexity | Multiple | Cloud | Research, fact-checking |
| Cursor | Composer, any | Local+Cloud | Professional developers |
| Windsurf (Cognition) | SWE-1.6 | Local+Cloud | Team dev, large codebases |
| Claude Code (Anthropic) | Claude 5 | Local+Cloud | CLI workflows, automation |
| Lindy | Multiple | Cloud | Business automation, non-technical |
| Zapier Agents | Multiple | Cloud | Team workflows, approvals |
| n8n | Multiple | Cloud/Both | Technical teams, self-hosted |
| LangGraph | Any | Local/Cloud | Complex workflows, production |
| CrewAI | Any | Local/Cloud | Multi-agent teams |
| LlamaIndex | Any | Local/Cloud | Knowledge apps, document Q&A |

---

### Step 4 — Tools & Integrations
Give the agent the right hands.

- **Simple (local)**: File read/write, code execution, calculations
- **API (web, apps, data)**: Search, weather, CRM, databases, email
- **MCP server**: Standardized tool connections (filesystem, GitHub, Notion, etc.)
- **AI agent as a tool**: Sub-agents for specialized tasks
- **Custom functions**: Bespoke logic the agent needs to call

> Prompt: "My agent needs to [tasks]. What tools should I give it? Which should be MCP servers vs. custom functions? What are the security implications of each?"

---

### Step 5 — Memory Systems
Decide what the agent remembers and how.

- **Episodic (conversation)**: Chat history in the context window — short-term, lost on reset
- **Working memory (Smart)**: Structured state passed between steps in the same session
- **Vector database**: Semantic search over past conversations, documents, or facts
- **SQL/Structured DB**: Exact lookups, user preferences, structured records
- **File storage**: Long documents, uploaded files, persistent outputs

> Prompt: "My agent needs to remember [X across sessions / Y within a session / Z about the user]. What memory architecture fits? Give me the tradeoffs between vector vs. SQL for my use case."

---

### Step 6 — Orchestration
Define how the agent decides and routes.

- **Routes/Workflows**: Fixed decision trees for predictable paths
- **Triggers**: What starts the agent (user message, schedule, webhook, event)
- **Parameters**: Inputs passed to the agent at runtime
- **Message queues**: Async processing for high-volume or delayed tasks
- **Agent2Agent**: One agent calling another as a sub-agent
- **Error handling**: What happens on failure — retry, escalate, or fail gracefully

> Prompt: "My agent handles [types of requests]. Help me map the orchestration: what routes to define, when to use a fixed workflow vs. letting the LLM decide, and how to handle errors."

---

### Step 7 — User Interface
Choose the right surface for your users.

- **Chat interface**: Conversational, flexible, natural — best for open-ended tasks
- **Web app**: Structured UI with agent capabilities embedded
- **API endpoint**: Headless — the caller controls the UI
- **Slack/Discord bot**: Meets users where they already work

> Prompt: "My users are [description]. They'll use this agent to [tasks]. Which interface fits? If building a web app, what UI patterns work best for an AI agent?"

---

### Step 8 — Testing & Evals
Measure before you ship, keep measuring after.

- **Unit tests**: Does each tool call return the right output?
- **Latency testing**: Is it fast enough for the use case?
- **Quality metrics**: Accuracy, relevance, hallucination rate, refusal rate
- **Iterate & improve**: Run evals on a golden dataset, fix failures, re-run

> Prompt: "Help me design an eval suite for my agent that [use case]. What should I test? What's a good golden dataset? How do I measure quality without human review on every output?"

---

## QUICK CHECKLIST

```
[ ] Step 1: Use case, users, success criteria, constraints defined
[ ] Step 2: System prompt written with goals, persona, instructions, guardrails
[ ] Step 3: LLM chosen — model, reasoning level, context window, cost/latency
[ ] Step 4: Tools listed — simple / API / MCP / agent / custom
[ ] Step 5: Memory architecture chosen — episodic / working / vector / SQL / file
[ ] Step 6: Orchestration mapped — routes, triggers, parameters, error handling
[ ] Step 7: UI chosen — chat / web / API / bot
[ ] Step 8: Eval suite designed — unit tests, latency, quality metrics
```
