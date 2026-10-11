---
description: Turn one repeated job into a tested SKILL.md using the BUILD prompt (outcome, read, write, test on the past, guardrail)
argument-hint: <the job, the files it needs, 3 past examples, what never goes out without you>
---

Use skill `solo-business-build-run` (BUILD_PROMPT). Task/Context/Constraints from "$ARGUMENTS"; ask once for anything missing. Run steps 01-06 in order, show the before/after tests side by side, name the one thing you are least sure about, then stop. Save the skill to `.claude/skills/<job>/SKILL.md` only after the user approves it.
