---
name: cowork-sales-prompts-10
description: The 10 Claude Cowork prompts for sales reps (SalesDaily.co) in full plain text - account briefs from files, CRM hit list, inbox deals going dark, weekly pipeline report, prospect research, battle card, meeting prep, call-transcript deal intelligence, prospect list enrichment and QBR deck - with the inputs each needs and the connector it relies on. Use when a salesperson wants a copy-paste Cowork or Claude prompt for one of these tasks.
---

# 10 Claude Cowork prompts for sales (SalesDaily.co)

Fill each [bracket]. Prompts 4 and 7 are scheduling prompts: they create recurring work, so confirm the schedule and the folder before running.

1. Account brief (Google Drive). Needs: folder, account name.
```
Go through my Google Drive folder [folder name]. Pull every doc, email, and note related to [account name]. Build me a one-page account brief with: deal history, key stakeholders, open issues, and last 3 touchpoints.
```
2. CRM hit list (file). Needs: pipeline export.
```
Here's my pipeline export [file]. Score every deal by likelihood to close this quarter based on last activity date, deal stage, and deal size. Flag anything that's been stuck in the same stage for 14+ days. Save as a spreadsheet sorted by priority.
```
3. Deals going dark (Gmail). Needs: Gmail.
```
Check my Gmail for any prospect threads where I sent the last message and haven't gotten a reply in 7+ days. List them out with the contact name, company, what I last sent, and draft a follow-up for each one.
```
4. Weekly pipeline report (schedule). Needs: CRM export folder.
```
Schedule this: Every Friday at 4pm, pull my latest pipeline data from [CRM export folder], calculate week-over-week movement by stage, flag any deals that slipped or stalled, and save a one-page summary to my Desktop.
```
5. Prospect footprint (browser). Needs: prospect, company.
```
Use the browser to research [prospect name] at [company]. Check their LinkedIn activity, recent company press releases, job postings, and earnings calls. Save a one-page research brief to my Sales Prep folder.
```
6. Custom battle card (browser). Needs: competitor site, positioning doc folder.
```
Go to [competitor website] and pull their pricing page, features page, and latest case studies. Compare against our positioning doc in [folder]. Build a battle card with: where we win, where they win, objection responses, and talk tracks.
```
7. Meeting prep (calendar, schedule). Needs: Google Calendar, Drive.
```
Schedule this: Each morning at 7am, check my calendar for today's external meetings. For each one, look up the attendee's company, pull any related files from my Drive, and drop a 5-bullet prep doc on my Desktop before I start work.
```
8. Call recordings to deal intelligence. Needs: transcripts folder.
```
Here are my call transcripts from this week [folder]. For each call, extract: buyer's stated priorities, objections raised, competitors mentioned, next steps promised, and any budget or timeline signals. Save as one summary doc.
```
9. Clean and enrich prospect list (browser). Needs: leads spreadsheet.
```
Take this spreadsheet of leads [file]. Use the browser to verify each company's website, employee count, and industry. Remove any that are under 50 employees. Add a column with a personalized reason to reach out based on what you find. Save the updated file.
```
10. QBR deck from account folder. Needs: account folder.
```
Open my [account name] folder. Read through every doc, email thread, and note from the last 90 days. Build a QBR presentation with: executive summary, key wins, usage highlights, open risks, and a proposed plan for next quarter. Save as a PPTX to my Desktop.
```

## Connector map

Gmail (3), Google Drive (1, 7), Google Calendar (7) are connected in this account. Browser prompts (5, 6, 9) need Claude in Chrome, Cowork browser use, or TinyFish. Prompts that save to the Desktop need Cowork (desktop app), not a cloud session.

## Cautions

- Prompt 2's 14-day stuck rule and prompt 3's 7-day silence rule are the author's thresholds; adjust to your sales cycle.
- Prompt 9 deletes rows under 50 employees from a copy; keep the original file.
- Prompt 3 only drafts; never let it send follow-ups without reading them.
- Use `/cowork-sales-10 [number]` to print one prompt and list what to supply.
