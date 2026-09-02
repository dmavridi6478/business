---
name: email-drafter
description: Multi-mode email drafting system covering cold outreach, follow-ups, and negotiation emails — each with its own tone, structure, and psychological framework. Use when the user needs to write any professional email and wants Claude to apply the right approach for the situation rather than produce generic copy. Distinct from outreach-copywriting (which focuses on high-volume cold sequences); this skill covers the full spectrum of professional email scenarios including negotiation and relationship maintenance. Source: @ai_slacker "25 Powerful AI Skills, Agents & Automations You Can Build Today."
---

# Email Drafter

Source: @ai_slacker "25 Powerful AI Skills, Agents & Automations You Can Build Today" (Beginner Tier, #3).

> Multi-mode prompt system that writes cold outreach, follow-ups, and negotiations on demand.

## The 3 modes

### Mode 1 — Cold Outreach
**Goal**: Start a conversation with someone who doesn't know you.
**Framework**: Problem → Credibility → Ask → Easy Yes
**Tone**: Direct, brief, no fluff. Under 100 words body.

```
Write a cold outreach email.

I am: [YOUR ROLE / COMPANY / WHAT YOU DO]
I'm reaching out to: [RECIPIENT ROLE / COMPANY]
My goal: [BOOK A CALL / GET FEEDBACK / PITCH A PARTNERSHIP / etc.]
The problem I can solve for them: [ONE SENTENCE]
My credibility signal: [RESULT, CLIENT, OR PROOF POINT — if any]
Preferred CTA: [SCHEDULE A 15-MIN CALL / REPLY WITH INTEREST / VISIT THIS LINK]

Rules:
- Subject line: under 8 words, curiosity-driven, no spam words
- Body: under 100 words
- One CTA only — no options, no "let me know if you're interested"
- Do not use "I hope this finds you well" or any filler opener
- Open with something specific to them, not about me
```

---

### Mode 2 — Follow-Up
**Goal**: Re-engage someone who didn't respond, without being annoying.
**Framework**: Reference → Value add → Frictionless ask
**Tone**: Light, confident, not apologetic.

```
Write a follow-up email.

Context: [I sent a cold email / proposal / had a call] on [DATE/TIMEFRAME]
They didn't respond / said they'd get back to me but didn't.
Original ask: [WHAT I ORIGINALLY WANTED]
New angle or value-add I can offer: [IF ANY — or leave blank]
Tone: [LIGHT / PROFESSIONAL / URGENT]
This is follow-up #: [1 / 2 / 3]

Rules:
- Reference the original email briefly, don't resend it
- Add a new angle or piece of value if this is follow-up #2 or #3
- Keep it shorter than the original
- Give them an easy exit if they're not interested — this preserves goodwill
- Never open with "Just checking in" or "Following up on my previous email"
```

---

### Mode 3 — Negotiation
**Goal**: Reach better terms on price, scope, timeline, or conditions.
**Framework**: Anchor → Justify → Alternative → Hold
**Tone**: Collaborative, not confrontational.

```
Write a negotiation email.

What I'm negotiating: [PRICE / SCOPE / TIMELINE / CONTRACT TERMS / etc.]
Current offer/situation: [WHAT THEY'VE PROPOSED OR WHAT'S ON THE TABLE]
My desired outcome: [WHAT I WANT INSTEAD]
My justification: [WHY MY POSITION IS REASONABLE — data, market rates, value delivered]
My fallback / alternative: [WHAT I'LL DO IF THEY DON'T BUDGE]
Relationship status: [NEW PROSPECT / EXISTING CLIENT / VENDOR I RELY ON]

Rules:
- Never open by accepting their terms and then asking for changes
- Acknowledge their position before stating mine
- Give one concrete counter-proposal — not a range
- Leave a clear path for them to say yes without losing face
- Close with a question that moves the conversation forward, not a statement
```

---

## Related skills

- **outreach-copywriting**: High-volume cold sequence design (Mode 1 at scale)
- **outreach-strategy**: Which channel and message type to use before writing
- **new-client-system**: Cold email is one node in the full client acquisition system
- **sales-enablement**: Negotiation email pairs with proposal and pitch deck layer
