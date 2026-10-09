# Wealth Lab 6-step variant — "Build an AI Agent in 10 Minutes"

Source: @the.wealth.lab carousel. "6 steps. No code. Every prompt ready to copy & paste."
Formula: **Context → Memory → Skills → Agents → Automation** — the move from "asking AI questions" to a reusable AI workflow.

Note: the source says "no code", but Steps 1 and 5–6 assume Claude Code or a scheduling surface. Steps 2–4 work in any Claude project.

## 1. Install Claude Code
Start with Claude Code — the agentic environment that lets Claude work across files, tools and multi-step workflows.
```
Help me set up Claude Code for my workflow. Check that it is installed correctly and explain the basic setup I need before we build my first AI agent.
```

## 2. Build its context
Give Claude a permanent briefing (CLAUDE.md = project briefing for environment, conventions and rules).
```
Help me build my CLAUDE.md from scratch. Ask me about my business, goals, audience, brand voice, banned words, output preferences, tools, and how I want you to work. Then create a clear, concise CLAUDE.md that can serve as my persistent project instructions.
```

## 3. Build its memory
Turn corrections, decisions and project knowledge into reusable files so the agent doesn't start from zero each session.
```
Design a simple memory system for my Claude Code projects. Whenever I give a correction, preference, important decision, or reusable piece of project knowledge, save it in an appropriate Markdown file. Create a central MEMORY.md index and organize the files so you can quickly find and reuse relevant information later.
```

## 4. Build a skill
Turn a repetitive workflow into a reusable capability (instructions + resources + scripts Claude loads when relevant).
```
Turn this workflow into a reusable Claude Skill: [DESCRIBE WORKFLOW]. Define its trigger, inputs, process, outputs, rules, and success criteria. Create the required SKILL.md structure and any supporting files needed. Make the skill reusable whenever this workflow is requested.
```

## 5. Build your agent team
```
Build an agent team for [DESCRIBE PROCESS]. Create specialized roles for research, analysis, execution, and quality control where appropriate. Give each agent a clear responsibility, required inputs, expected outputs, tools, and success criteria. Use subagents only when they add value, and have the main agent coordinate the workflow.
```
Guidance quoted on the slide: well-defined roles, clear completion criteria, and delegation where work can be isolated or run in parallel.

## 6. Put it on autopilot
```
Help me automate this workflow: [DESCRIBE WORKFLOW]. I want it to run [DAILY/WEEKLY/OTHER SCHEDULE]. Identify the appropriate Claude automation or scheduling method available to me, explain what permissions and integrations are required, and configure the workflow to deliver the finished output to [NOTION/GMAIL/DRIVE/OTHER DESTINATION].
```

## Repo mapping
- Step 2 → this repo's `CLAUDE.md`, `docs/about-me.md` · Step 3 → `MEMORY.md` pattern (see `context-save`, `memory-keeper` agent) · Step 4 → `/skill-create`, `skill-creator` · Step 5 → `/design-agent-team`, `team-builder` · Step 6 → `/schedule`, `scheduled-routine`, `/loop`.
- One-shot version of steps 4–6: `/workflow-to-agent`.
