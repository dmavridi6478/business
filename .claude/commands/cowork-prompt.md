---
description: Run one of the 20 Claude Cowork prompts (morning briefing, folder cleanup, report draft, contract comparison, meeting prep and more) after asking for the folder, file and name inputs it needs
argument-hint: "[prompt number 1-20] [folder path and details]"
---

Use the skill `claude-cowork-20-prompts`.

Input: $ARGUMENTS

If no prompt number from 1 to 20 was given, list the twenty titles and ask which to run. Otherwise take that prompt and:
1. List its [brackets]. Ask in one short question for the folder path, file names and options I have not given; never invent paths or contacts.
2. Before changing or moving any file, show the plan (files affected, new names, destination) and wait for my yes. Never delete anything without asking.
3. For prompts that read email, calendar, Slack or a CRM, use read-only access and say which connector is used; never send or post.
4. Produce the output in the format named in the prompt (Word, Excel or .pptx) and tell me exactly where it was saved and what you assumed.
