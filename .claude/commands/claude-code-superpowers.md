---
description: Give Claude Code dangerous superpowers — enable dynamic workflows, set effort to ultracode, and configure persistent goal conditions
argument-hint: ["workflows", "ultracode", "goal <condition>", "goal clear", "all" to apply all three]
---

You are a Claude Code power-user configurator. Based on "$ARGUMENTS", explain, apply, or chain the three dangerous superpowers that transform Claude Code from a code assistant into a workflow orchestration engine.

*Superpowers: Dynamic Workflows → Effort Ultracode → Goal Conditions*

---

## SUPERPOWER 1 — DYNAMIC WORKFLOWS

**What it does:** Unlocks Claude Code's multi-agent workflow engine. Instead of linear task execution, Claude plans, delegates, and orchestrates sub-tasks across sessions.

**How to enable:**
```
/config
→ Tab: Config
→ Search: "dy"
→ Dynamic workflows: true
→ Dynamic workflow size: large (aim for maximum orchestration)
```

**What changes:**
- Claude builds a plan before acting, not after
- Large workflow size = Claude can schedule more parallel sub-tasks
- Claude becomes an orchestrator, not just an executor

**Key rule:** Enable this once and leave it on. It's not per-task — it changes how every session thinks.

**Prompt:**
"I've enabled dynamic workflows on large. Analyze this project: [description]. Build me a dynamic workflow plan: what are the 5 main sub-tasks, which can run in parallel, and what's the critical path to completion? Output as a workflow dependency map."

---

## SUPERPOWER 2 — EFFORT ULTRACODE

**What it does:** Sets Claude's effort level to maximum for this session. Unlocks deeper reasoning, longer planning chains, and workflow orchestration on top of dynamic workflows.

**How to enable:**
```
/effort ultracode
```

**What it sets:**
- Effort level: `ultracode` (this session only — resets on new session)
- Workflow orchestration: active
- Claude plans more steps before executing, validates outputs more rigorously

**When to use:** Before any complex multi-file refactor, architecture decision, large feature build, or anything where you want Claude to think before touching code.

**Important:** This is session-scoped. You must re-run `/effort ultracode` at the start of each session where you want maximum effort.

**Prompt:**
"I've set effort to ultracode. Before writing any code, I want a full architecture brief: [describe the feature/system]. Give me: (1) the component map — every file that will be created or modified, (2) the sequence — what gets built in what order and why, (3) the risk surface — which parts could break existing functionality, (4) the test plan. Only then begin."

---

## SUPERPOWER 3 — GOAL CONDITIONS

**What it does:** Sets a persistent goal that Claude works toward across tasks. Claude will check every output against the goal condition and keep iterating until it's met or you clear it.

**How to use:**
```
/goal <condition>       → set a persistent goal Claude works toward
/goal clear             → remove the active goal
```

**Examples:**
```
/goal all tests pass and no TypeScript errors
/goal the dashboard loads in under 2 seconds on mobile
/goal the API returns correct data for all edge cases in the test suite
/goal the PR passes CI and has no lint warnings
```

**What changes:**
- Claude doesn't stop when it thinks it's done — it stops when the condition is met
- Claude self-evaluates against the goal after every action
- Use `clear` to remove the goal once the condition is satisfied

**Key rule:** Make the goal a verifiable condition, not a vague aspiration. "All tests pass" is a goal. "Make it better" is not.

**Prompt:**
"Set goal: [your verifiable condition]. Now work toward it. Before each action, state: (1) what the current state is relative to the goal, (2) what action will close the gap, (3) what you'll check to confirm it worked. Don't stop until the goal condition is met."

---

## FULL SUPERPOWER STACK (run in sequence)

```
Step 1: /config → Dynamic workflows: true → Dynamic workflow size: large
Step 2: /effort ultracode
Step 3: /goal [your verifiable success condition]
Step 4: Describe your task — Claude now plans, orchestrates, and iterates until done
```

**Power user setup:**
These three work together. Dynamic workflows gives Claude the architecture to plan in parallel. Ultracode gives Claude the reasoning depth to plan well. Goal conditions gives Claude the persistence to not stop until it's right.

**Combined prompt:**
"Stack is configured: dynamic workflows on large, effort ultracode, goal: [condition]. Here's the project: [description]. Build a full execution plan before touching any code. Plan should cover: (1) all sub-tasks and their dependencies, (2) which run in parallel, (3) what the goal condition verification looks like, (4) what a rollback looks like if something breaks. Confirm the plan with me before executing."

---

## REFERENCE — SLASH COMMANDS CHEAT SHEET

| Command | What it does | Scope |
|---------|-------------|-------|
| `/config` | Open settings panel | Persistent |
| `/effort ultracode` | Set max effort + workflow orchestration | Session only |
| `/effort ult` | Short form of ultracode | Session only |
| `/goal <condition>` | Set persistent success condition | Until cleared |
| `/goal clear` | Remove active goal | Immediate |
| `/mcp` | Manage MCP server connections | Persistent |

**Key rule:** `/effort ultracode` resets on session close. `/config` dynamic workflow settings persist. `/goal` persists until explicitly cleared.
