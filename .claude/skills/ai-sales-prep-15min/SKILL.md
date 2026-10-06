---
name: ai-sales-prep-15min
description: 'A 15-minute AI sales-call preparation system in six steps - account snapshot, likely pain points, stakeholder map, discovery plan, objection prep, final call brief - each with what to feed the AI, what to ask for and the output you want, plus the best input pack and four rules. Use before any sales, discovery or renewal call to walk in with sharper context and better questions. Source: SalesDaily.co "AI Sales Prep" infographic.'
---

# AI sales prep - 15 minutes

**Four rules (from the source):** feed AI source material, not vague prompts; ask for outputs in sales format, not essays; use AI to synthesise, diagnose and draft - not to invent facts; verify names, numbers and claims before the call.

**Best input pack:** recent company news; website and product pages; attendee profiles as text; the past email thread; CRM notes and deal stage; call transcript or notes; case studies or proof points.

| # | Step | Feed the AI | Ask for | Output you want |
|---|---|---|---|---|
| 1 | Account snapshot | Company site and product pages, recent news, the buyer's profile text, latest earnings notes if public | Summarise what changed recently, what the company likely cares about now, and 3 possible business priorities | A 1-page account brief: priorities, trigger events, likely initiatives, 3 tailored opening angles |
| 2 | Likely pain points | Role title, team structure, company size, industry, growth stage, known challenges | The 5 most likely pain points for this buyer right now; separate strategic pain from day-to-day execution pain | A prioritised pain list: symptoms, impact, and how each would show up in conversation |
| 3 | Stakeholder map | Org-chart clues, titles of people involved, job descriptions, who joined the last call, buying-committee hints | Map likely stakeholders, what each probably cares about, and what objections each may raise | A mini map: priorities, likely influence level, messaging angle per person |
| 4 | Discovery plan | Current deal stage, past emails, call notes, MEDDICC fields, pain hypotheses, open questions | 10 sharp discovery questions, 3 hypotheses to test, 3 red flags to watch for | A call-ready plan in sequence: opener, diagnosis, impact, decision process, next step |
| 5 | Objection prep | Your value drivers, proof points, competitor context, pricing model, case studies, common objections | Concise responses for price, timing, no-priority, competitor and "send me something" | Talk tracks with follow-up questions, proof points, and when to push vs when to slow down |
| 6 | Final call brief | Everything above plus meeting goal, meeting type, attendee list, desired next step | A final brief to review in 2 minutes before the call | Account summary, buyer goals, likely pain, discovery questions, objection prep, recommended next step |

## Procedure for Claude
Run steps 1-6 in order, asking for inputs not provided. Mark every statement `[from input]` or `[hypothesis]`. Never fill a gap with a plausible fact. If the user gives a company name only, say that step 1 will be hypotheses until real sources are supplied, and offer to fetch public pages with the repo's research tools. Command: `/call-prep`.

## Plain-text prompt (copy and paste)
```
You are my sales-call prep analyst. Meeting: [GOAL, TYPE, ATTENDEES, DESIRED NEXT STEP]. Material below: [PASTE: company news, website text, attendee profiles, email thread, CRM notes, case studies]. Do six things in order and label each: (1) account snapshot - what changed, what they care about, 3 business priorities, 3 opening angles; (2) the 5 most likely pain points, strategic vs day-to-day, with symptoms and impact; (3) stakeholder map with priorities, likely influence and a messaging angle each; (4) a discovery plan - 10 questions, 3 hypotheses to test, 3 red flags; (5) objection talk tracks for price, timing, no-priority, competitor and "send me something"; (6) a final brief I can read in 2 minutes. Use only my material. Tag each claim [from input] or [hypothesis]. List anything I must verify before the call.
```

## Keywords
sales prep, call preparation, discovery, MEDDICC, objection handling, SalesDaily
