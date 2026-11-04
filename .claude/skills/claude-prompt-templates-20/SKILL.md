---
name: claude-prompt-templates-20
description: Twenty copy-paste Claude prompt templates for everyday work (meeting notes to action items, email tone, difficult conversations, executive summary, job description, agenda, data interpretation, feedback, brainstorming, slide outline, policy explainer, competitive analysis, interview questions, status update, objections, document simplifier, decision framework, onboarding, cold outreach, retrospective), each with bracketed placeholders and a built-in output structure, mapped to the matching existing command. Use when someone wants a ready prompt for a common work task or asks which prompt to use. Source Mindstream infographic "20 Claude Prompt Templates" (Batch 115).
---

# 20 Claude prompt templates

Source: Mindstream infographic "20 Claude Prompt Templates" (a newsletter graphic with a lighthouse illustration). Prompts transcribed from the image; fill the [brackets] and paste. Several tasks already have a command here, so the table shows the nearest one; use the template when you want the exact wording.

What makes them work (the pattern in all 20): a named input in brackets, a fixed output structure, one constraint on length or tone, and one "flag what could go wrong" instruction. Reuse that pattern for your own.

| # | Template | Nearest existing command |
|---|---|---|
| 1 | Meeting Notes to Action Items | /action-plan-from-notes, /meeting |
| 2 | Email Tone Adjuster | /toneformal, /tonecasual, /shorten |
| 3 | Difficult Conversation Prep | /ceo-email-tough-feedback, /reflect-on-situation |
| 4 | Executive Summary Generator | /summary, /role-specific-summary |
| 5 | Job Description Writer | /job-post-builder (small-business plugin) |
| 6 | Meeting Agenda Builder | /meeting |
| 7 | Data Interpretation | /data:analyze (data plugin), data-storytelling |
| 8 | Feedback Softener | /ceo-email-tough-feedback |
| 9 | Brainstorm Expander | /brainstorm, /expand |
| 10 | Slide Outline Builder | `pptx-slide-specification` and `pptx` skills |
| 11 | Policy or Process Explainer | /simplify-explain, /sop |
| 12 | Competitive Analysis Starter | /competitor-benchmark-scorecard, /compare |
| 13 | Interview Question Generator | /interview |
| 14 | Status Update Writer | /status, /standup-notes, /weekly |
| 15 | Objection Handling Script | /objection |
| 16 | Document Simplifier | /simplify-explain, /plain-human |
| 17 | Decision Framework | /proscons, /decision-matrix |
| 18 | Onboarding Doc Creator | /onboard |
| 19 | Cold Outreach Message | /colddm, /sales-email |
| 20 | Post-Project Retrospective | /premortem (inverse), /reflect-then-revise |

### 1. Meeting Notes to Action Items

```
Here are my raw meeting notes: [paste notes]. Turn these into a clean summary with three sections: Decisions Made (with a one-line reason for each), Action Items (owner, deadline, and priority level), and Open Questions (flag which ones are blocking progress). Keep the tone neutral and skip anything that was just small talk or tangential.
```

### 2. Email Tone Adjuster

```
Rewrite this email to sound more [professional/warm/concise/assertive]: [paste email]. Keep the core message and any specific facts or numbers exactly the same. Shorten it if it feels padded, and flag if any part of the original might come across poorly to the recipient given the tone I'm asking for.
```

### 3. Difficult Conversation Prep

```
I need to talk to a colleague about [situation]. Give me an opening line that's direct but not accusatory, two likely ways they could respond (one defensive, one receptive), and a suggested reply for each. Also tell me one thing I should avoid saying, based on how this kind of conversation usually goes wrong.
```

### 4. Executive Summary Generator

```
Summarize this document in one paragraph for a busy executive who has 30 seconds to read it: [paste document]. Lead with the single most important takeaway, then the supporting point, then any decision or action needed from them. Avoid background context they don't need.
```

### 5. Job Description Writer

```
Write a job description for a [role title] at a [company type/size]. Include a short intro paragraph about the role's impact on the team, a list of core responsibilities in order of importance, required skills separated from nice-to-haves, and a note on who this role reports to. Match the tone to [company culture, e.g. startup/corporate/nonprofit].
```

### 6. Meeting Agenda Builder

```
I have a meeting about [topic] with [attendees/roles] for [time length]. Build me an agenda with time allocations per segment, a clear goal stated for each segment, and a suggested owner to lead each part. End with a segment for next steps and owners.
```

### 7. Data Interpretation

```
Here's some data [paste data or describe it]. Identify the three most important takeaways, note anything that looks surprising or contradicts common assumptions, and list the follow-up questions I should be asking before presenting this to others.
```

### 8. Feedback Softener

```
I need to give feedback that [describe the feedback]. Rephrase it so it's honest and specific but doesn't come across as harsh. Structure it as what's working, what needs to change, and why the change matters. Keep it under 100 words.
```

### 9. Brainstorm Expander

```
I have an idea [describe idea]. Give me 10 variations or angles, ranging from safe and practical to bold and unconventional, and label which category each one falls into. For the three most promising ones, note what would need to be true for them to work.
```

### 10. Slide Outline Builder

```
I need to present on [topic] to [audience] for [time limit]. Give me a slide-by-slide outline with a one-line summary of what goes on each slide, a suggested visual or data point for each, and a note on where the audience is most likely to ask questions.
```

### 11. Policy or Process Explainer

```
Explain this internal policy or process in plain language, as if explaining it to someone new to the company: [paste policy]. Break it into what it is, why it exists, and what someone actually needs to do differently because of it. Flag any part that's commonly misunderstood.
```

### 12. Competitive Analysis Starter

```
I'm comparing [my product/service] to [competitor]. Build a comparison framework covering pricing, features, target audience, and positioning. For each category, note where we're clearly ahead, clearly behind, or roughly even, and suggest one angle we could lean into in messaging.
```

### 13. Interview Question Generator

```
I'm interviewing someone for a [role]. Give me 8 questions that go beyond the resume and test for [specific skill or trait]. For each question, include what a strong answer sounds like versus a weak one, so I know what to listen for.
```

### 14. Status Update Writer

```
Turn these bullet points into a weekly status update for my manager: [paste bullets]. Organize it by project, keep each project to two or three lines, note anything that's at risk or behind schedule, and end with a specific ask if I need something from them.
```

### 15. Objection Handling Script

```
I'm pitching [product/idea] and expect pushback like [objection]. Give me three ways to respond that address the concern directly without sounding defensive, ranging from a quick reassurance to a more detailed data-backed answer. Note which response fits best depending on how skeptical the person seems.
```

### 16. Document Simplifier

```
Simplify this so someone outside our industry could understand it: [paste text]. Cut jargon and replace it with plain language, keep all key facts intact, and add a one-sentence explanation for any term that can't be avoided.
```

### 17. Decision Framework

```
I'm trying to decide between [option A] and [option B] for [context]. Build a pros and cons comparison for each, weigh which factors matter most given [my priority, e.g. cost, speed, risk], and tell me what additional information would most change the decision.
```

### 18. Onboarding Doc Creator

```
Create a first-week onboarding checklist for a new [role] joining our team. Assume they know nothing about our internal tools yet. Organize it by day, include who they should meet and why, and flag anything that's easy to overlook in the first week.
```

### 19. Cold Outreach Message

```
Write a short, non-salesy outreach message to [type of person] about [reason for reaching out]. Keep it under 100 words, open with something specific to them rather than a generic line, and end with a low-pressure ask that's easy to say yes to.
```

### 20. Post-Project Retrospective

```
Here's what happened during [project name]: [describe what happened]. Structure a retrospective covering what went well, what didn't, and what to change next time. For each point, note whether it's a one-off issue or a pattern worth fixing at a process level.
```

## Notes
- Keep real names, figures and confidential text out of prompts unless your plan and your policy allow it.
- Check facts, numbers and quotes in the output before sending. Template 7 (data) and 12 (competitors) can produce confident but wrong claims.
- Overlap: `claude-20-prompts` (a different set of 20 by another author), `claude-power-prompts`, `claude-prompt-frameworks`.
