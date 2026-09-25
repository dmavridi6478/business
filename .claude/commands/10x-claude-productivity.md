---
description: 10-step funnel to get 10X more done with Claude — model selection, prompting framework, Projects, Artifacts, Design, Research, Memory, Custom Skills, tool connections, and Claude Code mastery. Run with no args for the full framework, or name a step to go deep on it.
argument-hint: [model | prompting | projects | artifacts | design | research | memory | skills | tools | code] — or run with no args for the full framework
---

You are a Claude productivity coach. If no argument is given, present the full 10-step funnel and ask which step the user wants to go deeper on.

Source: @51ultron.com — "How to Get 10X More Done with Claude"

---

# 10X Claude Productivity Framework

**The 10-step funnel — from choosing the right model to deploying with Claude Code.**

---

## [1] Choose the Right Model

| Model | Best for |
|---|---|
| **Claude Sonnet** | Fast daily work — drafting, analysis, Q&A |
| **Claude Opus** | Deep reasoning — strategy, research synthesis, complex decisions |
| **Claude Code** | Software engineering — code, debugging, architecture |
| **Claude Research** | Multi-source web research with citations |

**Rule:** Match the model to the cognitive load of the task. Don't use Opus for a tweet.

---

## [2] Master Prompting

**The 6-part prompt formula:**

```
ROLE: You are a [EXPERT ROLE] with [SPECIFIC EXPERTISE].
GOAL: Your task is to [SPECIFIC OUTCOME].
CONTEXT: [BUSINESS / AUDIENCE / CONSTRAINTS / EXISTING DATA].
CONSTRAINTS: [LENGTH / TONE / FORMAT / WHAT TO AVOID].
OUTPUT FORMAT: [MARKDOWN TABLE / BULLET LIST / NUMBERED STEPS / JSON / PROSE].
SUCCESS CRITERIA: [HOW YOU WILL KNOW IT IS DONE].
```

**Prompt refinement loop:**
1. Run the prompt.
2. Identify what's missing or wrong.
3. Add one constraint or clarification.
4. Re-run.

---

## [3] Create Projects for Long-Term Memory

Projects give Claude persistent context across sessions.

**Recommended projects to set up:**

| Project | Purpose |
|---|---|
| **Learning** | Study notes, summaries, flashcards |
| **Research** | Ongoing investigations, source library |
| **Client Accounts** | One project per client with their brief, brand voice, history |
| **Business Ops** | SOPs, templates, internal comms |
| **Content Pipelines** | Drafts, calendars, repurposing queues |

---

## [4] Build with Artifacts

Artifacts are self-contained outputs Claude produces and stores.

| Artifact type | Use for |
|---|---|
| Documents | SOPs, reports, briefs |
| Dashboards | KPI views, competitive trackers |
| Websites | Landing pages, microsites |
| Apps | Calculators, tools, prototypes |
| Presentations | Decks, pitch materials |
| Checklists | Repeatable processes |

---

## [5] Design with Claude Design

Claude can produce visual-first deliverables.

- Pitch decks
- UI mockups
- Landing pages
- Visual reports
- Website designs
- Product concepts

**Prompt pattern:**
```
Design a [TYPE] for [AUDIENCE].
Brand: [COLOURS / FONTS / TONE].
Content: [KEY MESSAGES].
Format: [DIMENSIONS / SLIDES / SECTIONS].
```

---

## [6] Research Like a Pro

Claude Research can search the web, compare information, generate reports, and cite findings.

```
Research [TOPIC] and produce a structured report covering:
1. Current state of [TOPIC]
2. Key trends (last 12 months)
3. Top 5 sources (with citations)
4. Implications for [BUSINESS / AUDIENCE]

Format: Executive summary + detailed sections + source list.
```

---

## [7] Use Memory

Memory lets Claude remember your preferences across all sessions.

**What to save to memory:**
- Writing style and tone preferences
- Business context and brand voice
- Work constraints (budget, tools, team size)
- Personal goals and priorities
- Recurring workflow patterns

---

## [8] Create Custom Skills

Skills are reusable expertise packages you build once and use forever.

| Skill category | Examples |
|---|---|
| Content | LinkedIn post writer, carousel builder, email drafter |
| Marketing | Campaign brief, ICP definer, competitor analyser |
| Business | Board report, OKR planner, decision framework |
| Coding | PR reviewer, test writer, refactor guide |

**To create a skill:**
```
Turn this process into a reusable Claude skill:
Process: [DESCRIBE WHAT YOU DO REPEATEDLY]
Input: [WHAT GOES IN]
Output: [WHAT COMES OUT]
Format: SKILL.md file with frontmatter and step-by-step instructions.
```

---

## [9] Connect Your Tools

Claude integrates with your existing stack.

| Category | Tools |
|---|---|
| Docs / files | Google Workspace, Notion, Dropbox |
| Code | GitHub, VS Code (via Claude Code) |
| Comms | Slack, Gmail |
| Projects | Linear, Jira, ClickUp |
| CRMs | HubSpot, Salesforce |

---

## [10] Master Claude Code

**The full development loop:**

```
Idea → Architecture → Code → Test → Debug → Deploy
```

Key commands:
```bash
# Install
npm install -g @anthropic/claude-code

# Start in a project
cd your-project && claude

# Key slash commands
/review — code review the current file
/test — generate tests
/explain — explain the codebase
/fix — fix a failing test or bug
/commit — create a commit message
```

---

## Quick Reference Card

```
1. MODEL    → Sonnet (daily) | Opus (deep) | Code (dev) | Research (web)
2. PROMPT   → ROLE + GOAL + CONTEXT + CONSTRAINTS + FORMAT + SUCCESS
3. PROJECTS → Learning / Research / Clients / Ops / Content
4. ARTIFACTS → Docs / Dashboards / Sites / Apps / Decks / Checklists
5. DESIGN   → Pitches / UI / Landing pages / Visual reports
6. RESEARCH → Search + Compare + Report + Cite
7. MEMORY   → Style / Voice / Constraints / Goals / Patterns
8. SKILLS   → Content / Marketing / Business / Coding
9. TOOLS    → Google / GitHub / Slack / Notion / CRMs
10. CODE    → Idea → Arch → Code → Test → Debug → Deploy
```
