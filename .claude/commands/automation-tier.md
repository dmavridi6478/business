---
description: Pick the right Claude Code automation tier (loop, desktop task, cloud routine) for a recurring task and draft the prompt
argument-hint: <the recurring task and how often>
---

Use skill `claude-automation-stack-3-tiers`. For "$ARGUMENTS": say what must survive (terminal close, restart, laptop off), pick Tier 1, 2 or 3 and why, name the trigger (schedule, GitHub event, API), and write the self-contained routine prompt (repo, goal, definition of done, what not to touch). Add a `/goal` line if it must run until a condition holds. List the permissions it needs and mark anything that sends, spends or deletes as approval-required. Do not schedule anything; give me the prompt and the setup steps.
