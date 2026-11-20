---
description: Plan a supervised coding-agent run using a Jev-style decision model (Foreman with Openjev or Jev), with tests before trusting it
argument-hint: [the coding task and what a wrong action would cost]
---

Use the skill `replace-so-repos-7-jev-edition`. Input: "$ARGUMENTS".

1. Read `.claude/skills/replace-so-repos-7-jev-edition/SKILL.md` and `.claude/skills/laya-jev-ultrafast/SKILL.md`.
2. Propose the worker, the supervisor questions (stuck, tests passing, requirements met, needs verification, needs a human) and the action each score maps to.
3. State the hardware or key each piece needs and what data leaves the machine.
4. Give 5 test cases to run in demo mode first and a rule for when a human must approve. Do not install or run anything.
