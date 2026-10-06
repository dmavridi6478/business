---
description: 'Look up a named agent role in the roster (LinkedIn-100, GTM-200, Lead-Gen-100, Revenue-45) and route the task to the working department agent, or to the nearest existing os-* agent.'
argument-hint: '<catalog: linkedin|gtm|leadgen|revenue> <role name or number> [task]'
---

Arguments: "$ARGUMENTS"

1. Read `.claude/skills/roster-agents/catalogs.json`. Match the catalog (linkedin -> `linkedin-100`, gtm -> `gtm-200`, leadgen -> `leadgen-100`, revenue -> `revenue-45`) and the role (exact name, partial name, or position number). If several roles match, list them (max 5) and ask which; if none match, say so and name the nearest.
2. Route:
   - `gtm-200`: the entry's `agent` field is the subagent to run.
   - `linkedin-100`: use `linkedin-to-gtm-agent` for the department.
   - `leadgen-100` / `revenue-45`: use the matching `os-*` agent listed in `.claude/skills/roster-agents/SKILL.md` if one covers it; otherwise run the generic role prompt from that file.
3. Run that agent with: the role name, the user's task, and the instruction that the output is a draft saved under `data/agent-drafts/`.
4. Never send, post, connect or message anyone. Show the draft path and the `Not verified:` list. If the task needs the owner's proof or ICP and it is missing, ask one question before drafting.
