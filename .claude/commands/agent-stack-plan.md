---
description: Plan an AI agent's stack from the seven building blocks (browser control, memory, research skills, diagrams, security, orchestration, context) with licence limits, using the agent-stack-architect agent
argument-hint: [what the agent must do, where it runs, who uses it]
---

Use the skill `agent-repos-licence-ledger` and the agent `agent-stack-architect`. Input: "$ARGUMENTS".

1. Read `.claude/skills/agent-repos-licence-ledger/SKILL.md`.
2. Run the agent with the goal. It chooses the blocks the agent actually needs (not all seven), names the repo for each, and states each licence limit.
3. Save the plan to `docs/agent-stack-plan-YYYY-MM-DD.md` with sections: goal, blocks chosen and rejected with reasons, licence limits, risks, first read-only prototype.
4. Install nothing and run nothing; ask before any step that does.
