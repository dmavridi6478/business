---
description: Turn one repetitive workflow into a reusable skill, an agent team, and a scheduled automation in one pass (Wealth Lab steps 4–6)
argument-hint: [describe the workflow, e.g. "weekly competitor price check for surgical sutures"]
---

Workflow: "$ARGUMENTS"

Work in three stages. Confirm with me after each stage before starting the next.

**Stage 1 — Skill.** Turn this workflow into a reusable Claude Skill. Define its trigger, inputs, process, outputs, rules and success criteria. Create the SKILL.md structure (under `.claude/skills/<kebab-name>/`) and any supporting files. Make it reusable whenever this workflow is requested. Follow the `skill-creator` conventions and check first that no existing skill already covers it (search `.claude/skills`).

**Stage 2 — Agent team.** Only if the process has separable steps: build an agent team with specialised roles for research, analysis, execution and quality control where appropriate. Give each agent a clear responsibility, required inputs, expected outputs, tools and success criteria. Use subagents only when they add value; the main agent coordinates. Write agent definitions under `.claude/agents/`. If one agent is enough, say so and skip.

**Stage 3 — Autopilot.** Ask me for the schedule (daily/weekly/other) and the destination (Notion/Gmail/Drive/Slack/other). Identify the appropriate Claude scheduling method available here (`/schedule` routine, `/loop`, or Zapier/Notion automation), state which permissions and connectors are required and which are actually connected, then configure it. Keep any send/publish step behind human approval.
