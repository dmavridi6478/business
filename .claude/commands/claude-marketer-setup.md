---
description: Draft the four-step Claude setup for a marketer (custom instructions with banned words, one Project per function, three reusable templates, a least-privilege connector plan)
argument-hint: [your role, brand and audience, tone, the tools you use]
---

Use the `claude-marketer-setup-4-steps` skill.

Input: $ARGUMENTS

1. If my role, audience, tone or tools are missing, ask once. Do not invent a brand.
2. Write the custom-instructions block: who I am, who I serve, tone rules with two examples of how I do sound, and a banned-words list of at most fifteen words with a reason for each.
3. Propose the Projects (Content, Email, Research or others for my role): the files to upload to each, what to leave out, and a naming and dating rule.
4. Write three reusable templates for my most repeated tasks: input fields, the prompt, the output format, and how to review it.
5. Give a connector plan: which to connect first, read-only scope, what each could read or send, and what needs my security team's approval.
6. End with a two-week measurement plan (time per task before and after) and what I should not automate.
