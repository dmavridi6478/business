---
name: event-planner
description: Turn one client event brief into a complete event plan with Claude - brief, timeline, budget with estimated vs actual vs remaining, vendor tracker, every communication (invite, reminder, vendor email, speaker brief, follow-up) and an hour-by-hour event-day runbook. Use when the user is planning a client event, conference, meetup, workshop, launch or party and wants one organised system instead of scattered prompts. Source SkillDrop AI "Planning a client event?" 10-slide carousel (Batch 99); slide 4 was not in the upload, so the timeline step is reconstructed from the surrounding slides.
---

# Event planner - one brief, one system, one event plan

Principle from the carousel: one process, not 20 disconnected prompts. Everything flows from a single **event brief**; each later deliverable reuses it.

## Step 1 - The event brief (slide 2)

Claude needs this context before it can build the full plan. Ask for any missing field, one question at a time:

| Field | Example |
|---|---|
| Event type | conference, meetup, workshop, launch |
| Goal | educate, launch, network, celebrate |
| Audience | who attends and what they need |
| Date | event date(s) and time |
| Location | venue, city or virtual |
| Guest count | expected attendees |
| Budget | total budget and any limits |
| Must-haves | non-negotiable elements |

Save the answers in `event-brief.md` in the working folder (or a Claude Project) so every later step reads the same file.

## Step 2 - Timeline (reconstructed)

From planning to post-event, working backwards from the date: venue and date locked, vendors booked, invitations out, reminders, final numbers, day-of, follow-up. One line per milestone with owner and due date.

## Step 3 - Budget (slide 5)

Table: category, estimated, actual, remaining, with a flag when remaining is negative. Default categories from the slide: venue, catering, staff, AV, decor, marketing, contingency. Keep a contingency line. Never invent a figure: use only numbers the user gave; mark unknown estimates `?`.

## Step 4 - Vendor system (slide 6)

Table: vendor, contact, quote, deadline, status (Confirmed / In Review / Not Started), next action. No more scattered emails and notes: one tracker.

## Step 5 - Communications (slide 7)

Written from the same brief: invite email, reminder (to registrants), vendor email (details and next steps), speaker brief (agenda, logistics, key details), follow-up (thank attendees, share next steps). Drafts only; the user sends.

## Step 6 - Event-day runbook (slide 8)

Hour by hour so everyone knows what happens next, for example: 08:00 setup, 09:30 staff briefing, 10:00 doors open, 10:30 session 1, 12:30 lunch, 15:00 wrap-up. Each row: time, task, owner, backup.

## Before and after (slide 9)

Notes everywhere -> one timeline. Missed tasks -> a tracked list. Scattered emails -> a vendor tracker. Budget confusion -> an itemised budget with remaining. All of it from one brief.

## Rules

- Prices, availability and vendor claims come from the user or the vendor's quote, not from Claude.
- Drafts only. Nothing is booked, paid or sent by Claude.
- If this is for a client, keep the brief and budget in the client's folder and mark the file with the client's name.
