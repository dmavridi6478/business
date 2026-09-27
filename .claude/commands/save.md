---
description: Store a useful chat result, workflow, or prompt for future reuse
argument-hint: [what to save, and optionally where]
---

Save "$ARGUMENTS" so it can be reused later, rather than letting it disappear at the end of this conversation:

- A reusable prompt or short recurring workflow → turn it into a slash command (see `/custom`).
- A multi-step procedure, framework, or reference worth loading into future sessions → save it as a skill under `.claude/skills/<name>/SKILL.md`.
- A one-off result (a draft, a generated report, research findings) with no reuse pattern → write it to a sensibly-named file in the repo (or the project's existing convention for that content type) instead of leaving it only in chat history.

Confirm the exact file path saved to once done.
