# Claude Cookbooks — Developer Recipe Library

Copy-paste code snippets and Jupyter notebooks for building with the Claude API. Covers capabilities, tool use, multimodal, evals, agent patterns, extended thinking, cost optimization, managed agents, and the Claude Agent SDK.

**Source:** `anthropics/claude-cookbooks` (public)
**Local clone:** `/home/user/anthropics/claude-cookbooks`
**API key required:** yes — set `ANTHROPIC_API_KEY`

---

## Directory map

| Directory | Contents |
|-----------|---------|
| `capabilities/` | Classification, RAG, summarization |
| `tool_use/` | Tool-use basics, customer-service agent, calculator, SQL |
| `multimodal/` | Vision, charts/graphs, forms, sub-agents |
| `evals/` | Agentic search eval harness |
| `extended_thinking/` | Extended thinking; extended thinking + tool use |
| `cost_optimization/` | Cost optimization checklist; Pareto-optimal agent config |
| `patterns/` | Agent patterns |
| `claude_agent_sdk/` | Agent SDK walkthroughs (00–08 + hosted agent, session browser, SRE agent, vulnerability detection agent, etc.) |
| `managed_agents/` | Managed Agents (CMA): cap spend, human-in-the-loop, orchestrate issue→PR, subagent observability, skills from a repo, MongoDB, Sentry, Slack, and more |
| `observability/` | Observability patterns |
| `finetuning/` | Fine-tuning recipes |
| `skills/` | Custom skills authoring (`CLAUDE.md`, `skill_utils.py`, `notebooks/`) |
| `third_party/` | Pinecone RAG, Voyage AI embeddings, Wikipedia search |
| `misc/` | JSON mode, moderation filter, prompt caching, PDF upload, building evals, web-page reading |
| `images/` | Image handling |
| `tool_evaluation/` | Tool evaluation |

---

## Claude Agent SDK notebooks (`claude_agent_sdk/`)

| Notebook | What it teaches |
|----------|----------------|
| `00_The_one_liner_research_agent.ipynb` | Minimal agent loop in one line |
| `01_The_chief_of_staff_agent.ipynb` | Multi-tool orchestration |
| `02_The_observability_agent.ipynb` | Tracing and logging agent runs |
| `03_The_site_reliability_agent.ipynb` | SRE on-call pattern |
| `04_migrating_from_openai_agents_sdk.ipynb` | Migration guide from OpenAI Agents SDK |
| `05_Building_a_session_browser.ipynb` | Persistent session management |
| `06_The_vulnerability_detection_agent.ipynb` | Security scanning agent |
| `07_Hosting_the_agent.ipynb` | Deploying a hosted agent |
| `08_Dynamic_workflows.ipynb` | Runtime-composed agent workflows |

---

## Managed Agents notebooks (`managed_agents/`)

| Notebook | Pattern |
|----------|---------|
| `CMA_cap_session_spend.ipynb` | Budget gating |
| `CMA_gate_human_in_the_loop.ipynb` | Human approval before irreversible actions |
| `CMA_orchestrate_issue_to_pr.ipynb` | Issue → PR automation |
| `CMA_watch_subagents_live.ipynb` | Live subagent observability |
| `CMA_use_skills_from_a_repo.ipynb` | Loading skills dynamically |
| `CMA_iterate_fix_failing_tests.ipynb` | Agentic test-fix loop |
| `CMA_plan_big_execute_small.ipynb` | Plan-then-execute decomposition |
| `CMA_verify_with_outcome_grader.ipynb` | LLM-as-judge outcome grading |
| `CMA_prompt_versioning_and_rollback.ipynb` | Prompt version management |
| `CMA_with_mongodb_atlas.ipynb` | MongoDB Atlas integration |

---

## Quick-start snippets

### Messages API

```python
import anthropic
client = anthropic.Anthropic()
message = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Hello!"}]
)
print(message.content[0].text)
```

### Tool use

```python
tools = [{
    "name": "get_weather",
    "description": "Get current weather",
    "input_schema": {
        "type": "object",
        "properties": {"location": {"type": "string"}},
        "required": ["location"]
    }
}]
response = client.messages.create(
    model="claude-haiku-4-5-20251001",
    max_tokens=1024,
    tools=tools,
    messages=[{"role": "user", "content": "What's the weather in London?"}]
)
```

### Extended thinking

```python
response = client.messages.create(
    model="claude-opus-5",
    max_tokens=16000,
    thinking={"type": "enabled", "budget_tokens": 10000},
    messages=[{"role": "user", "content": "Solve this step by step..."}]
)
```

---

## Prompts

### Find the right notebook for a task

```
Search /home/user/anthropics/claude-cookbooks for notebooks covering [topic].
List matching files with a one-line description of what each demonstrates.
```

### Run a cookbook notebook

```
Open /home/user/anthropics/claude-cookbooks/[directory]/[notebook].ipynb.
Walk through it step by step, explain what each cell does, and run it.
```

### Build an eval harness from the cookbook pattern

```
Use /home/user/anthropics/claude-cookbooks/misc/building_evals.ipynb as a reference.
Build an eval harness for [task description].
Produce: dataset of 20 test cases, a grading rubric, and a score report.
```

### Build a cost-optimized agent

```
Use /home/user/anthropics/claude-cookbooks/cost_optimization/cost_optimization.ipynb.
Apply the checklist to [agent description].
Measure pass rate and cost per task; find the Pareto-optimal model + prompt config.
```

### Author a custom skill

```
Read /home/user/anthropics/claude-cookbooks/skills/CLAUDE.md and skill_utils.py.
Create a new skill for [capability] following the cookbook pattern.
```
