---
description: Run one lesson from the Claude for Sales curriculum (1 to 8) as a prompt and checklist, without needing the course
argument-hint: "[lesson number 1-8]"
---

Use the skill `claude-for-sales-course-map`.

Lesson: $ARGUMENTS

If no lesson number from 1 to 8 was given, list the eight titles and ask which one. Then, for the chosen lesson:
1. State its promise from the skill in one line.
2. Ask me for the inputs it needs (my product, my buyer, a prospect or call text) in one short question; do not guess them.
3. Produce the output for that lesson: 01 a one-page brief on what AI changes in my sales process; 02 three personalised email drafts under 120 words each; 03 a prospect research sheet with the buying signal and source for each prospect; 04 a four-touch follow-up sequence with timing; 05 a table of the top objections with a reply and a question for each; 06 a lead capture, qualify and nurture flow with the consent rule for each step; 07 a call review (talk ratio, questions asked, objections, next step, one thing to change); 08 a 30-day plan by week.
4. Draft only: never send, post or message anyone, and mark every claim you cannot verify. Do not invent prospects, quotes or results.
