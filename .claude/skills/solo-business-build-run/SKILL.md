---
name: solo-business-build-run
description: The BUILD (File 02) and RUN (File 03) copy-ready prompts from @your.aimentor's solo-business series - turn one repeated job into a tested SKILL.md, then put the finished skills on a weekly schedule with a run log and Friday learning loop. Use when someone wants to convert a recurring task into a skill, test it against past examples, or schedule and review skills. File 01 (audit/pick the #1 job) is covered by audit-my-workflow-for-skills.
---

# Solo business: BUILD then RUN

Both prompts say "Sonnet 5.5 + Opus 5.5; send the image to Claude; works in the app or Claude Code". Replace every [BRACKET].

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
`/build-skill-from-job` and `/run-skill-schedule`. Schedule with the harness (routines / `/loop`), not by hand; "drafts only" stays on until a skill has two clean weeks. Related: `audit-my-workflow-for-skills`, `oneoff-to-reusable-pipeline`, `scheduled-routine`, `sop-builder`.
