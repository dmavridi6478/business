---
name: claude-cowork-sales-prompts-10
description: Ten Claude Cowork prompts for sales reps (account briefs from Drive, CRM export hit list, deals going dark in Gmail, weekly pipeline report, prospect research, battle card, daily meeting prep, call transcripts to deal intelligence, prospect list enrichment, QBR deck) quoted verbatim, with the data-protection, consent and review checks the graphic omits. Use when setting up Cowork or another file-and-browser agent for sales work.
---

# 10 Claude Cowork prompts for sales reps

Source: a SalesDaily.co infographic, "10 Claude Cowork Prompts That Save Sales Reps 5+ Hours/Week" (Batch 120). Quoted verbatim; replace the [brackets]. The "5+ hours a week" claim is the graphic's and is not measured: time one task by hand and with the prompt before you believe it.

| # | Use case | Prompt (verbatim) | Check before you trust it |
|---|---|---|---|
| 1 | Auto-build account briefs from your files | Go through my Google Drive folder [folder name]. Pull every doc, email, and note related to [account name]. Build me a one-page account brief with: deal history, key stakeholders, open issues, and last 3 touchpoints. | Spot-check three facts against the source; each claim should name its file |
| 2 | Turn a messy CRM export into a prioritized hit list | Here's my pipeline export [file]. Score every deal by likelihood to close this quarter based on last activity date, deal stage, and deal size. Flag anything that's been stuck in the same stage for 14+ days. Save as a spreadsheet sorted by priority. | The score is a judgement, not a forecast: compare it with your own top 10 |
| 3 | Scan my inbox for deals going dark | Check my Gmail for any prospect threads where I sent the last message and haven't gotten a reply in 7+ days. List them out with the contact name, company, what I last sent, and draft a follow-up for each one. | Drafts only; you read and send. Never auto-send |
| 4 | Weekly pipeline report on autopilot | Schedule this: Every Friday at 4pm, pull my latest pipeline data from [CRM export folder], calculate week-over-week movement by stage, flag any deals that slipped or stalled, and save a one-page summary to my Desktop. | A scheduled task only runs while the computer and app are available; check the first two runs |
| 5 | Research a prospect's entire digital footprint | Use the browser to research [prospect name] at [company]. Check their LinkedIn activity, recent company press releases, job postings, and earnings calls. Save a one-page research brief to my Sales Prep folder. | Keep to public professional material; LinkedIn terms restrict automated access, so prefer press, talks and filings |
| 6 | Build a custom battle card from real competitor content | Go to [competitor website] and pull their pricing page, features page, and latest case studies. Compare against our positioning doc in [folder]. Build a battle card with: where we win, where they win, objection responses, and talk tracks. | Verify each competitor claim on its page and date it; do not state what you cannot support |
| 7 | Prep every meeting on my calendar | Schedule this: Each morning at 7am, check my calendar for today's external meetings. For each one, look up the attendee's company, pull any related files from my Drive, and drop a 5-bullet prep doc on my Desktop before I start work. | Confirm it did not open private files outside the account |
| 8 | Turn call recordings into deal intelligence | Here are my call transcripts from this week [folder]. For each call, extract: buyer's stated priorities, objections raised, competitors mentioned, next steps promised, and any budget or timeline signals. Save as one summary doc. | Recording consent and retention rules apply; quote, do not paraphrase budget numbers |
| 9 | Clean up and enrich my prospect list | Take this spreadsheet of leads [file]. Use the browser to verify each company's website, employee count, and industry. Remove any that are under 50 employees. Add a column with a personalized reason to reach out based on what you find. Save the updated file. | Keep the original; check the employee count source; the "reason" must come from a real finding |
| 10 | Generate a QBR deck from my account folder | Open my [account name] folder. Read through every doc, email thread, and note from the last 90 days. Build a QBR presentation with: executive summary, key wins, usage highlights, open risks, and a proposed plan for next quarter. Save as a PPTX to my Desktop. | Numbers and wins must tie to a source file; review before the customer sees it |

## Rules the graphic leaves out
- **Customer data.** These prompts feed customer emails, files and call transcripts to an AI service. Check your employer's policy, your contracts and data-protection law before using them, and use a work account that your company has approved.
- **Consent and recording.** Transcripts of calls need the participants' consent under the rules where they are; keep only what you need.
- **Outbound messages.** Prompts 3 and 9 produce outreach text. Check anti-spam and consent rules and keep a human in the send step.
- **Least access.** Point the agent at one folder, not your whole Drive or inbox, and review the permissions it asks for.
- **Test on a copy.** Run each prompt on a dummy account first, then compare the output with what you know.

## Related
`claude-sales-prompts-20`, `claude-sales-by-role`, `claude-cowork-setup`, `perplexity-sales-research-10`, `sales-workflow-catalog`, `pipeline-review`, `deal-velocity-engineer`, `mutual-action-plan-builder`, `cs-qbr`. Run one with `/cowork-sales-prompt <1-10> <details>`.
