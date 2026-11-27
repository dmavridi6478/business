---
name: claude-sales-prep-10
description: Ten sales-prep prompts for B2B sellers (company intelligence, buyer intelligence, call opener, discovery questions, objection simulator, competitor battlecard, buying-signal detector, cost-of-inaction calculator, deal advancement coach, pre-call and follow-up agent) quoted verbatim, with the guardrails the graphic leaves out (verified facts versus hypotheses, source rules, invented-number checks, approval before any send or CRM write). Use when preparing for a sales call or deal review with Claude connected to CRM, email and calendar.
---

# Claude for sales prep: 10 prompts

Source: an infographic by Alan Ruchtein, "Claude for Sales Prep: 10 Claude skills every B2B seller must install" (Batch 123). Its premise: connect Claude to your CRM, email, calendar and research tools through MCP, save each prompt as a skill, and let Claude do the prep. Quoted verbatim below; replace the [brackets]. These are saved prompts, not a packaged SKILL.md bundle: paste them into a Project, a command or a skill of your own.

| # | Skill | Prompt (verbatim) |
|---|---|---|
| 1 | Company intelligence | Research [company] using its website, CRM records and connected research tools. Give me a 60-second briefing with: business model, target customers, 3 strategic priorities, recent changes/news, 5 commercial insights with sources and how to use them on a call. |
| 2 | Buyer intelligence | Find [prospect] at [company]. Review their role, previous emails, CRM notes and recent public activity. Give me: 3 likely KPIs they own, 3 role-specific pains, 2 buying signals, 1 personalized opening question. Separate verified facts from hypotheses. |
| 3 | Call opener builder | Check my calendar, CRM and previous email threads for [company]. Write a 30-second opener using: relevant context, reason for meeting, clear agenda, permission question. Keep it natural, confident and conversational. |
| 4 | Discovery architect | Analyze [company]'s CRM record and business context. Identify missing information and give me 7 discovery questions in priority order, covering: pain, impact, urgency, decision process, budget. For each question: include a follow-up and the buying signal to listen for. |
| 5 | Objection simulator | Review our product docs, past objections and lost-deal notes. Predict the 5 most relevant objections for [prospect]. For each one give me: likely root concern, 20-second response, supporting proof (case study, data, etc.), 1 question to advance the conversation. |
| 6 | Competitor battlecard | Compare [our product] vs [competitor] using verified product information, pricing and CRM win/loss notes. Give me: 3 meaningful differentiators, 2 weaknesses we should acknowledge, 3 questions to expose gaps, 1 positioning statement for this prospect. |
| 7 | Buying signal detector | Research [company] for funding, hiring, leadership changes, product launches and technology changes from the last 90 days. Give me the 5 strongest signals, and for each: why it matters, likely pain or opportunity, 1 discovery question to use on the call. |
| 8 | Cost of inaction calculator | Use [company]'s context, current process and our ROI benchmarks. Estimate the cost of keeping their current approach. Give me: conservative, base and aggressive scenarios, clear assumptions, estimated wasted hours, financial impact and missed revenue, 3 questions to validate the numbers live on a call. |
| 9 | Deal advancement coach | Review [company]'s opportunity, recent meetings, emails and CRM activity. Give me: missing stakeholders, unresolved objections, decision risks, stalled commitments, the highest-impact next action, a mutual next-step proposal, a ready-to-send email to secure it. |
| 10 | Pre-call and follow-up agent | Review tomorrow's calendar and match each meeting to its CRM record and email history. Create a 60-second brief for each call (context, risks, 3 key questions). After the call, extract decisions, commitments and owners from my notes. Draft a personalized follow-up email and proposed CRM updates for my approval. |

## Guardrails the graphic leaves out

1. **Facts versus hypotheses.** Only prompt 2 asks for the split. Add it to all ten: every claim gets a label (verified in CRM, verified on a named public page, or hypothesis) and a source. No source, no claim.
2. **Invented numbers.** Prompt 8 will produce confident figures from thin context. Treat the base case as a conversation starter: every input must be the customer's own number (confirmed on the call) or a named benchmark of yours. Never show the model's estimate to the customer as their cost.
3. **Competitor claims.** Prompt 6 is only as good as the "verified product information". Paste your own current pricing and the competitor's public pages; do not let the model fill gaps from memory. Pricing and features change.
4. **Predicted objections are guesses.** Prompt 5 should cite the lost-deal notes it used. If none were supplied, say so and mark the objections as hypotheses.
5. **Approval before anything leaves.** Prompts 3, 9 and 10 draft messages and CRM changes. Keep them as drafts for your approval; a model should not send email or write to the CRM on its own.
6. **Least privilege.** Connect read-only first (calendar, one mailbox label, CRM read). Add write access only after the first two weeks of drafts have been accurate, and with a manager's agreement. Meeting notes and emails contain personal data: check your company's policy and the regional rules on processing it.
7. **Prompt injection.** Websites, inbound emails and shared documents are untrusted input. Tell the model to treat them as data, never as instructions.
8. **The time claim is not measured.** Time one prep by hand and with the prompt before you quote hours saved.

## Overlap in this library
`sales:account-research`, `sales:call-prep`, `sales:handle-objection`, `sales:competitive-intelligence`, `sales:deal-advance-gap`, `sales:call-summary` (plugin skills) cover similar ground; `perplexity-sales-research-10`, `claude-cowork-sales-prompts-10`, `claude-sales-prompts-20`, `buying-signals-6`, `signal-sourcer` and `mutual-action-plan-builder` are neighbours. This skill adds the ten prompts as printed plus the guardrails; use whichever fits your connected tools.

Run with `/sales-prep <1-10 or "all"> <company or prospect>`.
