---
name: claude-cowork-20-prompts
description: The "20 Claude Cowork prompts" graphic by Jonathan Parsons transcribed in full as fill-in-the-bracket prompts (morning briefing, folder cleanup, report draft, contract comparison, meeting prep, newsletter, expenses, slides, email follow-ups, research synthesis, duplicates, status update, job applications, scheduled report, onboarding pack, Excel cleaning, social batch, CRM update, PDF summaries, end-of-day plan) with safety notes for file and connector access. Use with Claude Cowork or any agent with folder access.
---

# 20 Claude Cowork prompts (Jonathan Parsons graphic)

Source: one infographic with twenty colour-coded prompt cards, transcribed in full below. Replace every [bracket]. Cowork prompts act on real files and connected accounts, so apply the safety notes at the end. Run one with `/cowork-prompt <1-20>`.

1. **Morning briefing**
   Check my [Google Calendar / Outlook calendar], unread emails in [Gmail / Outlook], and [Slack / Teams] mentions from the last 12 hours. Summarize everything I need to know before my first meeting at [TIME]. Keep it under 200 words and flag anything that needs a reply today.
2. **Folder cleanup and file organization**
   Go into the folder at [FOLDER PATH]. Rename all files using the format [DATE - TOPIC - FILE TYPE]. Group them into subfolders by [category, month, client name, or project]. List what you moved and ask me before deleting anything.
3. **Report draft from source files**
   Read all [PDF / Word / text] files in [FOLDER PATH]. These are [research notes / meeting transcripts / raw data]. Produce a structured report with the following sections: [Executive Summary, Key Findings, Recommendations]. Save it as a Word document named [FILE NAME] in [OUTPUT FOLDER PATH].
4. **Contract or proposal comparison table**
   Open the [2 / 3 / 4] PDF files in [FOLDER PATH]. These are [contracts / vendor proposals / project bids]. Compare them across the following criteria: [price, scope of work, payment terms, renewal clause, cancellation policy]. Produce a comparison table in Excel and save it to [OUTPUT FOLDER PATH].
5. **Meeting preparation brief**
   My meeting with [NAME / TEAM / COMPANY] is at [TIME] on [DATE]. It is about [TOPIC]. Pull any relevant files from [FOLDER PATH], check my recent emails with [CONTACT NAME or EMAIL] using the Gmail connector, and write a one-page prep brief covering background context, open questions, and my talking points.
6. **Weekly newsletter or internal update**
   Read the files in [FOLDER PATH] from the past [7 days / two weeks]. These cover [project updates / team activity / campaign performance]. Draft a [weekly newsletter / internal update email] addressed to [AUDIENCE]. Use a clear structure with a summary at the top, bullet points per section, and a next steps section at the end. Save as a Word document.
7. **Expense and receipt processing**
   Open all image and PDF files in [FOLDER PATH]. These are expense receipts from [MONTH]. Extract the merchant name, date, amount, and category for each one. Compile everything into an Excel spreadsheet with a total row and save it as [FILE NAME] in [OUTPUT FOLDER PATH].
8. **PowerPoint presentation from notes**
   Read the file [FILE NAME] in [FOLDER PATH]. This contains [raw notes / a document outline / research]. Turn it into a [10 / 15 / 20]-slide presentation covering [TOPIC]. Each slide should have a headline, three to five bullet points, and a speaker note. Save it as a .pptx file named [FILE NAME] in [OUTPUT FOLDER PATH].
9. **Email follow-up drafts**
   Read the email thread I have saved in [FILE PATH] or pull my last [3 / 5] emails with [CONTACT NAME] using the Gmail connector. Draft a follow-up email that [references our last conversation / summarizes what was agreed / asks for a status update]. Keep it under 150 words, professional in tone, and ready to send.
10. **Research synthesis from multiple sources**
   Use web search to find the [5 / 10] most relevant and recent articles on [TOPIC] from the past [30 / 90] days. Summarize each one in two to three sentences. Then write a 400-word synthesis that pulls out the key trends, disagreements, and open questions. Save the output as a Word document in [FOLDER PATH].
11. **Duplicate file detection and cleanup**
   Scan the folder at [FOLDER PATH] and identify any duplicate files based on file name similarity or identical file size. List all duplicates with their full paths, the date each was created, and which one appears to be the more recent or complete version. Ask me before deleting anything.
12. **Client or project status update**
   Read all files in [FOLDER PATH] related to [CLIENT NAME / PROJECT NAME]. These include [meeting notes / deliverables / email exports]. Produce a one-page status update covering: what has been completed, what is in progress, what is blocked, and what is due next. Save it as [FILE NAME] and format it as a Word document.
13. **Job application batch processing**
   I have [NUMBER] job description files saved in [FOLDER PATH]. My current resume is at [FILE PATH]. For each job description, compare it against my resume and write a tailored cover letter in my voice. Save each cover letter as a separate Word file named [COMPANY NAME - ROLE] in [OUTPUT FOLDER PATH].
14. **Scheduled recurring file report**
   Every [Monday morning / Friday at 5pm], go into [FOLDER PATH] and check for any new files added in the past [7 days]. List each file by name, size, and what it appears to contain based on the file name and first few lines. Send me a summary so I know what came in during the week.
15. **Onboarding document pack creation**
   Using the files in [FOLDER PATH] as source material, create an onboarding document pack for a new [ROLE NAME] joining [TEAM / COMPANY NAME]. The pack should include: a welcome overview, a glossary of key terms, a list of tools and access they will need, and a 30-day plan outline. Save everything as a single Word document named [FILE NAME].
16. **Data cleaning and formatting in Excel**
   Open the spreadsheet at [FILE PATH]. The data contains [describe the messy state: inconsistent date formats, missing values, duplicate rows, merged cells, etc.]. Clean it by [standardizing date formats to DD/MM/YYYY, removing duplicates, filling in blanks with N/A, etc.]. Add a summary row at bottom. Save cleaned version as [FILE NAME] in [OUTPUT FOLDER PATH].
17. **Social media or content batch drafting**
   Read the file at [FILE PATH]. This contains [a product brief / campaign notes / a topic list]. Using this as your source, write [10 / 15 / 20] LinkedIn post drafts on the topic of [TOPIC]. Each post should be between [150 and 200 words], start with a strong hook, and end with a question or call to action. Save all drafts in a single Word document.
18. **CRM or sales notes update (via connector)**
   Using the [Salesforce / HubSpot] connector, pull all deals I own that are in the [stage name] stage and have not been updated in the past [14 / 30] days. For each one, check my recent emails with that contact using the Gmail connector and write a one-sentence update on where things stand. Save a summary report to [FOLDER PATH].
19. **PDF to structured summary pipeline**
   Open all PDF files in [FOLDER PATH]. These are [research papers / legal documents / annual reports]. For each one, produce a structured summary with the following sections: Purpose, Key Findings or Terms, Action Items or Red Flags, and a Confidence Rating on how complete the document appears. Compile all summaries into a single Word document saved in [OUTPUT FOLDER PATH].
20. **End-of-day wrap-up and tomorrow's plan**
   At [TIME] each day, check what files were created or edited in [FOLDER PATH] today, pull my calendar for tomorrow using the [Google Calendar / Outlook] connector, and check for any unread emails or Slack messages flagged as urgent. Write a short end-of-day wrap-up covering what I got done today and a prioritized to-do list for tomorrow. Save it as a daily note in [NOTES FOLDER PATH].

## Safety notes
- **[Certain]** Prompts 2 and 11 move or delete files: keep the "ask me before deleting anything" line, work on a copy first, and never point them at a folder you cannot restore.
- **[Certain]** Prompts 5, 9, 18 and 20 read email, Slack, calendar or CRM through connectors and prompt 9 can end "ready to send"; keep every send manual and the connector read-only where possible.
- **[Likely]** Prompts 3, 7, 12 and 19 process documents with personal or confidential data; check your organisation's rules before pointing Claude at them.
- **[Likely]** Prompts 14 and 20 describe recurring runs; Claude Cowork scheduling depends on your plan and app, so confirm it is available before relying on it.
- Related: `claude-cowork-setup`, `cowork-marketing-20`, `claude-20-prompts`, `meeting-notes-processor`, `invoice-receipt-processor`.
