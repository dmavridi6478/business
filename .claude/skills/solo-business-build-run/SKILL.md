---
name: solo-business-build-run
description: The AUDIT (File 01), BUILD (File 02) and RUN (File 03) copy-ready prompts from @your.aimentor's solo-business series - turn one repeated job into a tested SKILL.md, then put the finished skills on a weekly schedule with a run log and Friday learning loop. Use when someone wants to convert a recurring task into a skill, test it against past examples, or schedule and review skills. Use AUDIT first to find which job to hand off; `audit-my-workflow-for-skills` is the longer repo-native version.
---

# Solo business: BUILD then RUN

All three prompts say "Sonnet 5.5 + Opus 5.5; send the image to Claude; works in the app or Claude Code". Replace every [BRACKET].

## AUDIT_PROMPT.md - find the work to hand off (File 01; cover slide: "3 Solo Business Copy-Ready Prompts For Claude", @your.aimentor)
```
Task: [your business in one line]
Context: [paste a normal week: calendar + sent folder]
Constraints: [hours you have, tools you use]

## 01 / Map the real week
List every recurring task in the context, not the ones I say I do. Group by area. For each give how often, how long, and what triggers it.
## 02 / Score the judgment
For each task name what a stranger would need to do it well: my voice, my prices, a client's history, or my taste. If files can carry it, it can be handed off.
## 03 / Sort into three piles
KEEP needs my judgment or my face. DRAFT: you prepare, I approve. RUN: you do it, I spot-check weekly. When unsure, pick DRAFT.
## 04 / Price the time
Put hours per week on every DRAFT and RUN task. Rank by hours back, then by how much I dread it. The top of the list is where we start.
## 05 / Name the inputs
For the top three, list the exact files, folders or exports you would need to read. Flag anything that only lives in my head.
## 06 / Verify, deliver, stop
Return one table and the top three. Mark every number that is an estimate. No advice beyond the list. Then stop.
```
The top job from AUDIT is the Task for BUILD.

## BUILD_PROMPT.md - turn one job into a skill
```
Task: [the #1 job from File 01]
Context: [the files it needs + 3 past examples done well]
Constraints: [what never gets sent without me]

## 01 / Outcome before steps
Write what "done" looks like for this job in one sentence a client would recognise. Then write the check that proves it.
## 02 / Read before writing
Open every file in the context. Pull out the rules I follow without saying them: tone, length, prices, exceptions, who gets special treatment. List them back to me first.
## 03 / Write the skill
One folder, one SKILL.md. Trigger, inputs, numbered steps in plain words, where the output lands. One job only. If a step needs "and", split it into two.
## 04 / Test it on the past
Run the skill on the three examples. Put your output next to what I actually did. Fix the step that caused each difference, then run it again.
## 05 / Build the guardrail
Add the check that catches a bad result before I see it: wrong price, wrong name, wrong tone, a promise I never made.
## 06 / Deliver, stop
Return the SKILL.md, the before/after tests side by side, and the one thing you are least sure about. Then stop.
```

## RUN_PROMPT.md - put it on a schedule
```
Task: [the skills you built in File 02]
Context: [your week: when you work, when you review]
Constraints: [drafts only until a skill runs clean 2 weeks]

## 01 / One calendar
Place every skill on a weekly schedule: daily, weekly, monthly. Nothing runs at a time I can't review what it made.
## 02 / One inbox for output
Every draft lands in one folder, named by date and job. I review in one sitting, not all day. Nothing sends itself.
## 03 / Log every run
After each run, append one line to RUNLOG.md: date, skill, what it made, what failed, what I changed before using it.
## 04 / Learn from my edits
Every Friday, read the week's log and my edits. Propose one change per skill. Show me the diff before you apply it.
## 05 / Promote or retire
Two clean weeks: a skill moves from DRAFT to RUN. Rewritten by me three weeks running: it gets rebuilt or retired.
## 06 / Report, stop
Monday, one paragraph: hours saved, what broke, what's next. Check the scheduler actually fired. Then stop.
```

## How to run it here
`/audit-week`, `/build-skill-from-job` and `/run-skill-schedule`. Schedule with the harness (routines / `/loop`), not by hand; "drafts only" stays on until a skill has two clean weeks. Related: `audit-my-workflow-for-skills`, `oneoff-to-reusable-pipeline`, `scheduled-routine`, `sop-builder`.
