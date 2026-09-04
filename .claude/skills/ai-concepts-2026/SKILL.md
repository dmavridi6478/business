# 9 AI Concepts for 2026 — Reference & Architecture Guide

Master the 9 AI engineering concepts that separate builders from observers in 2026. Use this skill to explain, evaluate, or architect AI systems around each concept.

## The 9 Concepts

```
01 AGENTIC LOOPS      Plan → Act → Observe → Reflect → (repeat) + memory/feedback
02 MCP                Agent → MCP → [Gmail, GitHub, DB, Browser, Slack, Files]
03 SUBAGENTS          Orchestrator → [Research | Coding | Reviewer | Data] → Merged Result
04 AI GATEWAY         Apps A/B/C → Gateway (auth, routing, rate limit, cache, logs) → [OpenAI | Anthropic | Gemini | OSS]
05 INFERENCE ECON     Tokens In → Cache HIT (~10% cost) / MISS (full cost) → Output Tokens → Total Bill
06 EVALS              Test Cases → Model Output → Judge LLM/Rubric → PASS/FAIL → Metrics
07 GUARDRAILS         User Input → Input Filter → Model → Output Filter → Safe
08 OBSERVABILITY      Agent Workflow → [1][2][3][4] → Traces, Logs, Metrics → Dashboard
09 AGENT HARNESS      User/App → [Planner | Memory | Tools | State | Guardrails | Evals] → Models + External Tools → Trusted Output
```

---

## Concept Prompts

### 01 — Agentic Loops

```
Act as an AI systems architect. Design an agentic loop for [USE CASE]:

LOOP STRUCTURE:
- PLAN: What does the agent plan before acting? (goal decomposition, task ordering)
- ACT: What tools/APIs/actions does the agent execute?
- OBSERVE: What does the agent observe from each action? (output parsing, error handling)
- REFLECT: How does the agent evaluate success and decide next step?
- MEMORY: What short-term and long-term memory does it maintain?
- FEEDBACK: What signals trigger loop continuation vs. termination?

Produce: loop pseudocode, termination conditions, failure recovery strategy.
```

### 02 — MCP (Model Context Protocol)

```
Act as an MCP integration architect. Design the MCP server setup for [AI AGENT / USE CASE]:

MCP DESIGN:
- Which external tools/services does the agent need? (Gmail, GitHub, Database, Browser, Slack, Files, custom APIs)
- For each tool: what MCP server handles it?
- Authentication strategy per integration
- Tool call schema for each capability
- How does the agent decide which tool to invoke?
- Error handling when MCP call fails

Produce: MCP server list, tool definitions, authentication matrix.
```

### 03 — Subagents & Multi-Agent Systems

```
Act as a multi-agent systems architect. Design a subagent system for [TASK]:

ORCHESTRATOR DESIGN:
- What does the orchestrator agent control and decide?
- How does it decompose the task across subagents?

SUBAGENT DEFINITIONS:
For each subagent:
- Role and specialization
- Own tools available
- Own context scope (what it knows)
- Output format it returns to orchestrator

RESULT MERGING:
- How does the orchestrator merge/validate subagent outputs?
- Conflict resolution when subagents disagree
- Quality gate before final output

Produce: agent diagram, context isolation strategy, merge logic.
```

### 04 — AI Gateway

```
Act as an AI infrastructure architect. Design the AI Gateway layer for [ORGANIZATION/USE CASE]:

GATEWAY REQUIREMENTS:
- Which applications will route through the gateway?
- Which model providers are needed? (OpenAI, Anthropic, Gemini, Open Source)
- Routing logic: how does the gateway decide which model handles which request?

GATEWAY CAPABILITIES:
- Authentication: how are apps authenticated to the gateway?
- Rate limiting: per app, per user, per model?
- Caching: what responses are cached? What's the cache TTL?
- Logging: what is logged per request? (tokens, latency, model, cost, user)
- Fallback: if primary model is unavailable, what's the failover?

Produce: gateway architecture diagram, routing rules table, cost control strategy.
```

### 05 — Inference Economics

```
Act as an AI cost optimization engineer. Analyze inference economics for [USE CASE / WORKLOAD]:

COST DRIVERS:
- Input tokens per request (average and peak)
- Output tokens per request
- Model tier being used (frontier vs. mid-tier vs. small)
- Requests per day / month

CACHE ANALYSIS:
- What % of prompts are repeated or share a common prefix? (cache hit rate estimate)
- Prompt caching savings: cache hit = ~10% of full cost
- Which prompt sections are cacheable? (system prompt, few-shot examples, context)

OPTIMIZATION LEVERS:
1. Prompt compression: how many tokens can be removed without quality loss?
2. Model right-sizing: which requests can use a smaller/cheaper model?
3. Caching strategy: what prefix caching setup maximizes hit rate?
4. Batching: can requests be batched to reduce per-call overhead?

Produce: monthly cost estimate before/after optimization, top 3 levers ranked by savings.
```

### 06 — Evals

```
Act as an AI evaluation engineer. Design an eval suite for [AI SYSTEM / USE CASE]:

EVAL DESIGN:
- What are the 3–5 core capabilities this system must have?
- For each capability: write 5 test cases (input → expected output or behavior)

JUDGE SETUP:
- Will you use an LLM-as-judge or a rubric-based scorer?
- If LLM judge: write the judge prompt with scoring criteria
- If rubric: define the rubric dimensions and weights

METRICS:
- Accuracy / task success rate
- Safety pass rate
- Latency at P50, P95
- Cost per correct answer

PASS/FAIL THRESHOLDS:
- What score defines "ship-ready"?
- What triggers a rollback?

Produce: eval matrix, judge prompt, CI integration recommendation.
```

### 07 — Guardrails

```
Act as an AI safety architect. Design the guardrail stack for [AI SYSTEM]:

INPUT GUARDRAILS (before model):
- PII detection: what personal data patterns to block or redact?
- Prompt injection defense: how to detect and neutralize injections?
- Topic restrictions: what inputs are out of scope?
- Rate limiting at user level

OUTPUT GUARDRAILS (after model):
- Jailbreak detection: patterns that indicate policy violation?
- Toxicity filtering: threshold and action (block / warn / redact)?
- Factual grounding: how to flag hallucinated or unverifiable claims?
- Brand safety: outputs that could embarrass the organization?

GUARDRAIL ARCHITECTURE:
- Synchronous (blocks response) vs. asynchronous (flags for review)?
- Layered: which checks run at input, which at output?
- Escalation: what happens on a guardrail trigger?

Produce: guardrail stack diagram, policy decision table, false positive mitigation strategy.
```

### 08 — Observability

```
Act as an AI observability architect. Design the observability stack for [AI AGENT / SYSTEM]:

WHAT TO TRACE:
- Each step in the agent workflow (numbered 1→N)
- Inputs and outputs at each step
- Tool calls made and their results
- Token counts and latency per step

LOGS:
- Structured log schema per request
- Error logging with context
- User session correlation

METRICS:
- Task success rate
- Average steps to completion
- Token cost per task
- Latency (total, per-step P50/P95)
- Tool call failure rate

DASHBOARD:
- What real-time views does the team need?
- Alerting rules (what triggers a PagerDuty/Slack alert?)
- Feedback loop: how do observations feed back into evals?

Produce: trace schema, metrics definitions, dashboard mockup description, alert thresholds.
```

### 09 — Agent Harness

```
Act as an agent harness architect. Design the complete agent harness for [USE CASE]:

The vendor ships the model. You own the loop. Design each layer:

PLANNER:
- How does the harness decompose the user's goal into executable steps?

MEMORY:
- Short-term: what stays in context during a session?
- Long-term: what is persisted across sessions? (vector DB, key-value, structured DB)

TOOLS:
- Full list of tools available to the agent
- Tool selection logic (how does the planner decide which tool to call?)

STATE:
- What state is tracked during execution? (current step, completed tasks, errors)
- State persistence strategy

GUARDRAILS:
- Input and output safety checks (see Concept 07)

EVALS:
- Inline quality checks during execution (see Concept 06)

EXTERNAL TOOLS → TRUSTED OUTPUT:
- How does the harness validate tool outputs before passing to model?
- How does it produce a final output the user can trust?

Produce: harness architecture diagram, layer-by-layer spec, handoff contracts between layers.
```

---

## Full System Audit

### Prompt — 9-Concept AI Architecture Review

```
Act as a senior AI systems architect. Review [AI SYSTEM / PROJECT] against the 9 foundational AI engineering concepts for 2026:

01 AGENTIC LOOPS: Does it implement Plan→Act→Observe→Reflect? Is the loop bounded? Does it have memory?
02 MCP: Does it use MCP for tool access? Which tools? Is the integration standard or bespoke?
03 SUBAGENTS: Are tasks decomposed across specialized subagents? Is context properly isolated?
04 AI GATEWAY: Is there a gateway for auth, routing, rate limiting, caching, and logging? Which providers?
05 INFERENCE ECONOMICS: Is caching implemented? Is model selection cost-optimized? What's the estimated monthly cost?
06 EVALS: Are there automated evals? LLM judge or rubric? CI integration?
07 GUARDRAILS: Are input AND output guardrails in place? What policies are enforced?
08 OBSERVABILITY: Are traces, logs, and metrics collected? Is there a dashboard? Alerting?
09 AGENT HARNESS: Is there a coherent harness managing planner, memory, tools, state, guardrails, and evals?

For each concept: score 0–3 (0=missing, 1=partial, 2=implemented, 3=best-in-class)
Flag the 3 lowest scores as priority gaps.
Produce a roadmap to close the top gap within 30 days.
```

---

## Concept Selection Guide

| You want to... | Use concept |
|----------------|-------------|
| Build an autonomous agent | 01 Agentic Loops + 09 Agent Harness |
| Connect to external tools | 02 MCP |
| Parallelize complex tasks | 03 Subagents |
| Manage multiple AI providers | 04 AI Gateway |
| Reduce AI API costs | 05 Inference Economics |
| Measure and improve quality | 06 Evals |
| Make the system safe | 07 Guardrails |
| Debug and monitor production | 08 Observability |
| Ship a production AI product | All 9 |
