# Batch 111 — prompts in plain text (copy and paste)

Replace every [BRACKET]. Slash commands: `.claude/commands/`; skills: `.claude/skills/`.

## 0. AUDIT - find the work to hand off (`/audit-week`)
Task: [your business in one line]
Context: [paste a normal week: calendar + sent folder]
Constraints: [hours you have, tools you use]
01 Map the real week: list every recurring task in the context, not the ones I say I do; group by area; for each give how often, how long, and what triggers it.
02 Score the judgment: for each task name what a stranger would need to do it well (my voice, my prices, a client's history, or my taste); if files can carry it, it can be handed off.
03 Sort into three piles: KEEP needs my judgment or my face; DRAFT: you prepare, I approve; RUN: you do it, I spot-check weekly; when unsure, pick DRAFT.
04 Price the time: put hours per week on every DRAFT and RUN task; rank by hours back, then by how much I dread it; the top of the list is where we start.
05 Name the inputs: for the top three, list the exact files, folders or exports you would need to read; flag anything that only lives in my head.
06 Verify, deliver, stop: return one table and the top three; mark every number that is an estimate; no advice beyond the list; then stop.

## 1. BUILD — turn one job into a skill (`/build-skill-from-job`)
Task: [the #1 job from your audit]
Context: [the files it needs + 3 past examples done well]
Constraints: [what never gets sent without me]
01 Outcome before steps: write what "done" looks like for this job in one sentence a client would recognise. Then write the check that proves it.
02 Read before writing: open every file in the context. Pull out the rules I follow without saying them: tone, length, prices, exceptions, who gets special treatment. List them back to me first.
03 Write the skill: one folder, one SKILL.md. Trigger, inputs, numbered steps in plain words, where the output lands. One job only. If a step needs "and", split it into two.
04 Test it on the past: run the skill on the three examples. Put your output next to what I actually did. Fix the step that caused each difference, then run it again.
05 Build the guardrail: add the check that catches a bad result before I see it: wrong price, wrong name, wrong tone, a promise I never made.
06 Deliver, stop: return the SKILL.md, the before/after tests side by side, and the one thing you are least sure about. Then stop.

## 2. RUN — put the skills on a schedule (`/run-skill-schedule`)
Task: [the skills you built]
Context: [your week: when you work, when you review]
Constraints: [drafts only until a skill runs clean 2 weeks]
01 One calendar: place every skill on a weekly schedule: daily, weekly, monthly. Nothing runs at a time I can't review what it made.
02 One inbox for output: every draft lands in one folder, named by date and job. I review in one sitting, not all day. Nothing sends itself.
03 Log every run: after each run, append one line to RUNLOG.md: date, skill, what it made, what failed, what I changed before using it.
04 Learn from my edits: every Friday, read the week's log and my edits. Propose one change per skill. Show me the diff before you apply it.
05 Promote or retire: two clean weeks: a skill moves from DRAFT to RUN. Rewritten by me three weeks running: it gets rebuilt or retired.
06 Report, stop: Monday, one paragraph: hours saved, what broke, what's next. Check the scheduler actually fired. Then stop.

## 3. Research brief, pass 1 and 2 (`/research-brief`)
P1: Turn these sources into a structured research brief on [TOPIC]. Separate established facts, source claims, disagreements and unanswered questions. Cite each important claim to its source.
P2: Now convert the brief into a one-page decision memo for [AUDIENCE]. Include: what we know, what we do not know, implications, options and the next 3 questions worth researching.

## 4. SOP builder, pass 1 and 2 (`/sop-from-process`)
P1: Turn this process description [PROCESS] into an SOP. Include purpose, trigger, prerequisites, numbered steps, decision points, quality checks and completion criteria. Do not invent steps.
P2: Now identify where a new person is most likely to make a mistake. Add short warnings and examples without changing the underlying process.

## 5. Nine-platform posting (`/blotato-post`; needs paid Blotato + OAuth)
Here's today's carousel and reel. Turn them into posts for all 9 platforms, each in its native format. Schedule for [DAY] [TIME]. Show me drafts first. Do not schedule anything until I say yes.

## 6. Connector commands
Claude Code: claude mcp add --transport http Blotato https://mcp.blotato.com/mcp   then /mcp -> Blotato -> Authenticate
Plugins (the slides say claude-plugins-official; in Claude Code 2.1.296 the built-in marketplace is anthropic-plugin-directory): /plugin install modern-web-guidance@anthropic-plugin-directory ; /plugin install browser-use@anthropic-plugin-directory ; /plugin install lovable@anthropic-plugin-directory
Slide-only extras not installed: paypal@..., hyperframes@... (check the marketplace name the same way).

## 7. Quick audits
SEO: Use seo-agents-100-and-tools-45. For [SITE URL] and goal [GOAL], run a baseline and pick the 3-5 agents and tools I need first, with input and output for each.
Maturity: Use limitless-marketing-maturity. Here is my team: [DESCRIBE]. Stage it with evidence and name the blocker.
ABM: Use full-funnel-os. Audit this program: [DESCRIBE]. Score the 5 parts 0-3.
BD week: Use bd-week-four-time-blocks. Plan my week around [CALENDAR]; name the 3 people for Give Something and the 1 for the Relationship Ladder.
