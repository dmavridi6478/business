---
description: Give me one of the 20 everyday Claude prompt templates (meeting notes, email tone, difficult conversation, status update, retrospective and more) filled in with my details, or show the list
argument-hint: [template name or number, plus your details; empty = list]
---

Use the `claude-prompt-templates-20` skill.

Input: $ARGUMENTS

If the input is empty, list the 20 templates with their nearest existing command. Otherwise pick the matching template, fill the brackets from my details (ask once for anything essential that is missing), and run it. Keep the output structure the template specifies. Flag any fact, number or quote I should verify before using the result.
