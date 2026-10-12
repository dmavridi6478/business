---
name: claude-automation-stack-3-tiers
description: The @techsupportzone "run Claude Code on autopilot" series - the three automation tiers (Tier 1 /loop and CronCreate, Tier 2 Desktop scheduled tasks, Tier 3 cloud routines with schedule, API and GitHub-event triggers), pairing /loop with /goal, and permission rules or Auto Mode so it does not babysit you - with what each tier survives, its limits, example routines, guardrails and the slide claims that are unverified. Use when choosing how to schedule or trigger recurring Claude Code work, setting up a routine, or deciding what to auto-approve.
---

# Claude Code automation stack (3 tiers)

Source: nine @techsupportzone slides. Numbers and dates are the slides' own; check the Claude Code docs before relying on limits.

| Tier | Mechanism | Survives restart | Needs laptop awake | Limits (slide) | Use for |
|---|---|---|---|---|---|
| 1 | `/loop`, `CronCreate`, `CronList`, `CronDelete` | no (dies with the terminal) | yes | session-scoped, up to 50 tasks, auto-expire after 7 days | quick checks while you work |
| 2 | Desktop app > Schedule > New task | yes | yes (a sleeping laptop skips the run; turn on "Keep computer awake") | macOS and Windows only; Linux uses `/loop` or system cron | daily briefs, local files |
| 3 | Cloud routines (claude.ai/code/routines or `/schedule`) | yes | no | Anthropic-hosted; slide says released 14 Apr 2026, all paid plans, research preview | anything that must run with the laptop off |

## Tier 1: `/loop`
`/loop 10m check the deployment status`. Plain English works too: "every weekday at 7am, summarize overnight commits", "every hour, check for new support tickets", "at 6:30pm today, post a status update to Slack".
**Pair with `/goal`.** Loops alone let Claude do 20 of 50 tasks and call the rest handled. `/loop 5m process the support queue /goal don't stop until the queue is empty`. An evaluator checks after each turn: "done" clears the goal, "not done" starts the next turn. Good for: fix flaky tests until zero fail, drain a queue, chase a bug until one theory holds.

## Tier 2: Desktop scheduled tasks
Fields: name, instructions, schedule (for example every day 8:30 AM), time zone, model, notify. Every run starts fresh (no leftover context); permissions are locked per task. Example "Daily research brief": search the web for the top AI news from the past 24 hours, summarise the 5 most important items with sources and key takeaways.

## Tier 3: Cloud routines
A routine = one self-contained prompt (specific, no follow-up questions) + repos + connectors (Slack, GitHub, Linear, Drive) + permissions + a trigger.
Triggers: **Schedule** (cron), **GitHub event** (PR opened or merged, release published, issue opened, optional filter), **API** (POST to a per-routine URL with a bearer token; regenerate or delete the token from the routine; the slide's `rt_live_...` URL is an example, not a real endpoint).
Examples: CI fails -> routine investigates and opens a fix PR; PagerDuty alert -> triage and post to Slack; PR opened -> first-pass review comment; issue created -> labels and linked code; release published -> changelog.
Three that pay for themselves: morning briefing (overnight issues, classify severity, post to Slack), PR review pass (flag security and style issues before a human opens it), doc-drift detection (docs not updated with code, open a fix PR). "Comb the backlog": top Linear issue, attempt a fix, open a draft PR, weekly Monday 09:00.
**Default safety:** routines can only push to branches starting `claude/`, so a bad routine cannot touch `main`. Keep that default.

## Permissions that do not babysit you
Default asks before every action. Set rules: always allow reading files, running tests, `git status`; never allow force-push, delete-everything, editing `.env`. Or use Auto Mode (slide: "Anthropic found users approve 93% of prompts anyway", pings you on the risky ~7%; Max/Team/Enterprise/API, not Pro yet; prompt-injection scanning and audit trail). Rule of thumb: cheap to undo = auto-approve; expensive to undo = never.

## Guardrails (my additions)
1. A routine that can send, spend or delete needs an approval step; in this repo outbound actions go through `os-approval`.
2. Write the routine prompt as if the reader has no memory: repo, goal, definition of done, what not to touch.
3. Start every new routine read-only for a week; read the run logs before widening access.
4. The 93% figure is a vendor statistic about prompt approvals, not evidence that auto-approval is safe for your repo.
5. Longest interval that still catches the problem; each run costs tokens.

Related: `claude-code-4-loops`, `scheduled-routine`, `/automation-tier`, `autonomous-loops`, `night-shift-workflow`.
