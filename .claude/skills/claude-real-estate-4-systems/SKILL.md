---
name: claude-real-estate-4-systems
description: Four Claude Project systems for a real estate agent - AI lead generation, organic marketing, AI SDR follow-up, and AI appointment setting - each as ten build steps (create a Claude Project, paste the main prompt, connect data or calendar, add research and scoring, connect n8n and the CRM, alert on hot leads, feed results back), with the guardrails the cards omit (fair housing, consent for automated messages, data protection, human approval). Use when a realtor or property business wants to automate lead handling, content or booking with Claude, or asks how to score and follow up leads. Source @usamaakrm "Claude for Real Estate Part 5: 4 AI Systems" (Batch 116). Steps were read from images; tool names are as shown, not verified.
---

# Claude for real estate: 4 AI systems

Source: @usamaakrm, "4 AI systems every Realtor needs today" (Part 5 of a series). Each system is a **Claude Project** (the "brain") with a main prompt, connected data, and an automation layer. The card ends with a pitch to hire the author to set them up; nothing on it is a result, price or case study.

**Verification status:** step lists were read from the infographic; tool names (PropStream, BatchLeads, Google Sheets, n8n, HubSpot, Twenty CRM, Higgsfield, cal.com, Telegram, Slack) are as shown and were not checked. No performance numbers were given.

## 1. AI Lead Generation System

| # | Step | Detail from the card |
|---|---|---|
| 1 | Create a Claude Project | Name it for the system; it is the brain |
| 2 | Add the main prompt | Find and analyse listings; research homeowners, buyers, investors, FSBOs, expired listings; check property and lead info; score 0-100; explain why a lead is good or bad; recommend the next action; send only qualified leads to the CRM. Bands: 80-100 hot, 60-79 warm, below 60 cold |
| 3 | Connect your lead data | Sources named: PropStream, BatchLeads, Google Sheets, CRM. Fields: name, phone, email, property, listing status, property value, equity, days on market |
| 4 | Add a research agent | Who owns it, is it FSBO, did the listing expire, are they an investor, any strong selling signals |
| 5 | Add a lead scorer | Score, priority, why qualified, best next action |
| 6 | Connect n8n | n8n does the automation, Claude does the thinking |
| 7 | Connect your CRM | HubSpot or Twenty CRM; write name, phone, email, lead type, score, notes |
| 8 | Add a hot-lead alert | Score 80 or above triggers Telegram, Slack or email |
| 9 | Give Claude the results | Feed back no reply, appointment set, deal won or closed so scoring improves |

## 2. Organic Marketing AI System

1 Create a Claude Project. 2 Add the main prompt (a content team for Instagram, TikTok, Threads, X, Facebook, LinkedIn). 3 Build a content research agent (audience problems, trending topics, competitors, FAQs and objections, 30 content ideas a month). 4 Build the content team (researcher, strategist, hook writer, script writer, copywriter, repurposer). 5 Create AI influencers (Higgsfield: consistent character, same face, different scenes). 6 Claude writes video scripts (hook, 30-60 second script, call to action). 7 Higgsfield creates the videos. 8 Repurpose one video everywhere. 9 Build the daily content machine. 10 Turn content into leads (comment keyword, DM, book a call).

## 3. AI SDR and Follow-Up System

1 Create a Claude Project. 2 Add the main prompt (contact new leads, ask simple qualifying questions, understand needs, follow up automatically, handle common objections, book qualified leads; never sound robotic). 3 Connect your leads (CRM, Google Sheets, lead form; name, phone, email, lead type, property, source). 4 Claude qualifies the lead (buy or sell, area, timeline, budget, already working with an agent). 5 Claude scores the lead (hot, warm, cold). 6 Create the follow-up sequence (day 1, 2, 4, 7, 14). 7 Personalise every message. 8 Handle replies (interested, not ready, not interested, qualified). 9 Book the meeting. 10 Update the CRM.

## 4. AI Appointment and Sales System

1 Create a Claude Project. 2 Add the main prompt (understand the lead, qualify, recommend the right appointment, book, handle simple objections, confirm, remind). 3 Connect the calendar (Google Calendar, cal.com). 4 Choose the right appointment (seller listing consultation, buyer consultation, property viewing, investor call). 5 Qualify before booking. 6 Offer available times. 7 Book automatically. 8 Send confirmation. 9 Send reminders (24 hours and 2 hours before). 10 Help the agent sell (a pre-meeting brief: who they are, what they want, budget, timeline, likely objection).

## Guardrails the cards omit (apply before any step runs)

- **Fair housing and discrimination:** lead scoring on property and household data can encode protected characteristics through proxies. Score only on declared intent, property facts and engagement; never on neighbourhood demographics, names, age or family status. Have counsel review the scoring prompt.
- **Consent and anti-spam:** automated texts, calls and emails to leads need consent and an opt-out. Rules differ by country and state (for example US telemarketing and text rules, EU/UK GDPR and e-privacy). Buying lists (expired, FSBO, absentee owners) carries extra risk.
- **Data protection:** property-owner data is personal data. Know the source, keep only what you need, and do not paste whole lead lists into a chat.
- **Human approval:** drafts only until you approve. A robot-sounding or wrong message goes out under your licence and name.
- **Accuracy:** an AI scorer is a guess. Track hot-lead outcomes for a quarter before trusting scores.
- **Platform rules:** auto-DMs and AI influencers can breach platform terms; AI-generated people need clear disclosure where required.

## How to use
Pick one system, not four. Start with 3 (follow-up) or 4 (booking): they need no scraped data. Use `/real-estate-system <system and your market>`. Related: `gtm-plays-12`, `cold-email`, `ai-entrepreneur-os`, `n8n-workflow-patterns`.
