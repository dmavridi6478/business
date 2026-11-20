---
description: Run one of the 10 dream-job application prompts (1 decode JD, 2 tailor CV, 3 bullets, 4 cover letter, 5 role-fit, 6 ATS, 7 questions, 8 STAR, 9 recruiter review, 10 full pack)
argument-hint: <1-10> [paste the JD, CV or background after, or attach files]
---

Use the skill `dream-job-10-prompts`. Arguments: "$ARGUMENTS". The first word is the prompt number.

1. Read `.claude/skills/dream-job-10-prompts/SKILL.md` and take that prompt exactly as written.
2. Collect the missing inputs (JD, CV, background, cover letter) in one short message; accept pasted text or attached files (use the `pdf-to-markdown` skill for PDFs).
3. Run it. Never add skills, employers, titles or numbers the user did not give; use [ADD METRIC] and ask.
4. For prompt 9 give the verdict first (shortlist / maybe / reject), then reasons, then the three quickest fixes.
