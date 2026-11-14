---
description: Decide which rung of the LLM, RAG, agent, agentic ladder a task needs, and the limits to add at that rung
argument-hint: [describe the task and what a wrong answer would cost]
---

Use the skill `llm-rag-agent-agentic-ladder`. Input: "$ARGUMENTS".

1. Read `.claude/skills/llm-rag-agent-agentic-ladder/SKILL.md`.
2. Say which rung is the lowest that can pass the task (LLM, RAG, agent, agentic) and why, using the "enough when" column.
3. State what the next rung up would add in cost and risk, and why it is not needed, or what evidence would justify climbing.
4. List the limits for the chosen rung (retrieval quality checks for RAG; step, spend and permission caps for agents; a measured need for multi-agent coordination).
5. Name 3 to 5 test cases the user should run to confirm the choice. Do not build anything unless asked.
