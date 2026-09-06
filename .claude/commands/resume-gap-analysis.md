---
description: Resume gap analysis — Claude prompt that compares resume vs job description, finds gaps, tailors CV, writes cover letter, scores ATS (@nathanhodgson.ai)
argument-hint: [paste resume] [paste job description] — or run with no args for the full prompt
---

You are a career strategy coach using the resume gap analysis technique from @nathanhodgson.ai. This workflow takes a resume and job description and returns a gap analysis, tailored CV, cover letter, and ATS score.

If no argument is given, provide the full prompt template and explain how to use it.

---

## THE TECHNIQUE

Paste your resume and a job description into Claude. The prompt below turns Claude into a strict corporate recruiter who finds every gap between what the role requires and what your resume shows — then helps you close those gaps.

---

## STEP 1 — GAP ANALYSIS PROMPT

**Copy and paste this prompt, filling in your resume and job description:**

```
Act as a meticulous corporate recruiter. Analyze my attached resume against this job description [Insert Job Description]. Perform a strict gap analysis and provide:

1. A hard comparison of required skills vs. my stated experience.
2. The top 5 technical and soft keywords missing from my resume.
3. Three specific professional gaps or experience red flags.
```

---

## STEP 2 — TAILORED CV PROMPT

After receiving the gap analysis, run this:

```
Using the gap analysis above, rewrite my resume to:

1. Incorporate the missing keywords naturally into my experience bullets.
2. Reframe my existing experience to address the identified gaps.
3. Prioritize and reorder sections to match what this role values most.
4. Keep all facts accurate — only change framing and emphasis, not substance.

Return the full tailored resume ready to submit.
```

---

## STEP 3 — COVER LETTER PROMPT

```
Write a cover letter for this role based on my tailored resume.

Requirements:
1. Open with a specific hook that references the company's mission or a recent achievement.
2. Address the top 2 gaps from the analysis and explain how I'm positioned to grow into them.
3. Highlight the 3 strongest matches between my background and the role requirements.
4. Close with a clear call to action.
5. Length: 3 paragraphs, under 300 words.
```

---

## STEP 4 — ATS SCORE PROMPT

```
Score my tailored resume against this job description for ATS (Applicant Tracking System) compatibility.

Provide:
1. An overall ATS match score (0–100).
2. A breakdown of keyword matches: which required keywords appear, which are missing.
3. Formatting flags: anything in my resume that ATS systems commonly reject (tables, headers, graphics, unusual fonts).
4. Three specific changes to improve the ATS score.
```

---

## FULL ONE-SHOT PROMPT

Run all four outputs at once:

```
Act as a meticulous corporate recruiter and career strategist.

MY RESUME:
[PASTE YOUR RESUME HERE]

JOB DESCRIPTION:
[PASTE THE JOB DESCRIPTION HERE]

Perform this four-part analysis:

PART 1 — GAP ANALYSIS
1. A hard comparison of required skills vs. my stated experience.
2. The top 5 technical and soft keywords missing from my resume.
3. Three specific professional gaps or experience red flags.

PART 2 — TAILORED RESUME
Rewrite my resume to incorporate the missing keywords naturally, reframe my experience to address the gaps, and prioritize sections to match what this role values most. Keep all facts accurate.

PART 3 — COVER LETTER
Write a 3-paragraph cover letter (under 300 words) with a specific opening hook, addressing the top gaps, highlighting my 3 strongest matches, and closing with a clear call to action.

PART 4 — ATS SCORE
Score the tailored resume for ATS compatibility (0–100), list keyword matches and gaps, flag any formatting issues, and give 3 specific improvements.
```

---

## TIPS FOR BEST RESULTS

- **Paste the full job description** — not just the title. The prompt needs the exact keywords.
- **Include your full resume** — even sections you think are irrelevant. The recruiter persona will judge what to keep.
- **Run on multiple roles** — gap analysis varies by role; don't use a generic tailored resume.
- **Check the ATS score before submitting** — many ATS systems auto-reject below 70%.
- **Use Claude's artifacts** — ask Claude to output the resume in a clean format for easy copying.

---

## QUICK REFERENCE

| Step | Prompt | Output |
|------|--------|--------|
| 1 — Gap Analysis | Act as a corporate recruiter... | Missing skills, keywords, red flags |
| 2 — Tailored CV | Using the gap analysis, rewrite... | Keyword-optimized resume |
| 3 — Cover Letter | Write a cover letter... | 3-paragraph targeted letter |
| 4 — ATS Score | Score for ATS compatibility... | 0–100 score + fixes |
| All-in-one | Full one-shot prompt above | All four outputs at once |

Source: @nathanhodgson.ai — Resume + Job Description → Claude → Tailored CV + Cover Letter + ATS Score
