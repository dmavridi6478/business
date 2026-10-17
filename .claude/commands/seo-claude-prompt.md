---
description: Run one of the 10 SEO Claude prompts (keyword research, content brief, SERP analysis, internal linking, meta data, content upgrade, FAQ schema, competitor gap, repurposing, monthly report) with the inputs you give
argument-hint: "[prompt number 1-10] [keyword, ICP or pasted text]"
---

Use the skill `claude-seo-10-prompts`.

Input: $ARGUMENTS

If no prompt number from 1 to 10 was given, list the ten names and ask which to run. Otherwise take the prompt with that number from the skill and:
1. List the [brackets] it needs. If any needed input (keyword, ICP, pasted posts, SERP text, data) is missing, ask for exactly those in one short question; do not make them up.
2. Run the prompt on the inputs given. Where it asks for difficulty or volume, label the figure an estimate and say which tool would verify it.
3. For prompts 03, 04, 06 and 08, work only from the text or URLs I pasted; never invent competitor content.
4. Output the result in a table or list I can paste, then one line on the next prompt that would follow in the workflow.
