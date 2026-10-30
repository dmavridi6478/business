---
description: Build a resume end to end using the resume-prompt-kit skill's 10 prompts — career positioning, intake, summary, experience, skills, certs, education, and an ATS proofread pass — then optionally tailor it and draft a cover letter for a named job.
argument-hint: [target role, industry, seniority, and — if tailoring — a job posting to paste]
---

Given what's described in "$ARGUMENTS" (ask the user for this if not provided — at minimum, target role, industry, and seniority level):

1. **Positioning** — apply `resume-prompt-kit` Prompt 1 to set the positioning statement and 5-7 themes to emphasize.
2. **Intake** — apply Prompt 2 to produce a fill-in checklist, then collect the actual background/achievements/work-history details from the user before continuing. Don't invent achievements or dates — ask.
3. **Summary** — apply Prompt 3 to draft 3 professional-summary variants.
4. **Experience** — apply Prompt 4 to turn the collected work history into ATS-friendly, quantified bullets per role.
5. **Skills** — apply Prompt 5. If the user has a specific job description already, use it now; otherwise skip the JD-matching and produce a general prioritized skills section from their background.
6. **Certifications** — apply Prompt 6 if the user has any to place.
7. **Education** — apply Prompt 7.
8. **Proofread** — apply Prompt 8 as a final ATS-safety and consistency pass over the assembled resume.

If "$ARGUMENTS" included a specific job posting (or the user provides one after step 8), continue:

9. **Tailor** — apply Prompt 9 against that posting.
10. **Cover letter** — apply Prompt 10 for that same posting.

Run a `humanizer` pass on the final summary, bullets, and cover letter before presenting them as finished — resume/cover-letter drafts are exactly where inflated AI phrasing shows up most.
