---
name: work-message-prompts-5
description: 'Five slash-style prompts for messages people hate writing at work - /followup (polite nudge), /badnews (calm problem update), /credit (document your contribution), /disagree (challenge without tension), /clarify (turn a vague request into 3 questions). Use when the user needs to write a difficult workplace message or email. Source: @faithflow_prayer carousel. Drafts only; never send.'
---

# Messages you hate writing - 5 prompts

Copied from the carousel (ChatGPT in the source; they work the same in Claude). Replace the bracket with the real message and context.

| Command | Goal | Prompt |
|---|---|---|
| `/followup` | Get a reply without sounding pushy | Write a polite follow-up to this unanswered message. Briefly restate what I need, explain why it matters now, and end with one clear question. Keep it under 80 words: [paste message and context] |
| `/badnews` | Share a problem without causing panic | Turn these facts into a calm update. State what happened, the impact, what is being done, and when the next update will come. Do not blame anyone or hide the risk: [paste facts] |
| `/credit` | Protect your contribution without sounding petty | Write a professional message that clearly documents my contribution, thanks the team, and connects my role to the outcome without sounding defensive or possessive: [paste contribution and context] |
| `/disagree` | Challenge an idea without creating tension | Write a respectful response that acknowledges this idea, explains my concern using facts, and proposes a practical alternative. Make me sound collaborative, not defensive: [paste idea and concern] |
| `/clarify` | Ask for clarity without looking confused | Turn this vague request into 3 concise questions that clarify the expected outcome, priority, deadline, and who will make the final decision: [paste request] |

## Rules
- Use only facts the user gives. `/badnews` must not minimise the impact; if a fact is missing, ask once.
- Output is a draft with 2 tone variants (direct, warm). Never send, post or email it.
- Greek requests: write in Greek, keep names and product terms as written, no capital-letter Greek words or accents on capitals.
- `/credit` carries a risk the carousel skips: the message can read as self-promotion. Offer the shorter, team-first version too.

Command: `/work-message <followup|badnews|credit|disagree|clarify>`.

## Keywords
follow-up email, bad news, credit, disagree, clarify, workplace communication, tone
