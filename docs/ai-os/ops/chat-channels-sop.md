# Chat channels SOP (WhatsApp, Instagram DMs, website chat, email)

Source: @ai.global.lee "Stop losing sales in your DMs: 5 AI agents that turn chats into customers" (Batch 99).
The carousel lists five agents for one chat channel: **WhatsApp Business**, **Customer Support**, **Appointment Booking**,
**Sales Follow-up** and **Lead Qualification**. Here they are built as *draft-only* members of the AI Entrepreneur OS, so a
human approves every message that leaves.

| Carousel agent | Here | What it does | Source it must use |
|---|---|---|---|
| #1 WhatsApp Business | `/os-chat-triage` (the channel router, not an agent) | classifies each inbound chat and runs the right agents | the chat export you provide |
| #2 Customer Support | `os-support` | answers common questions from approved policy; routes the rest | `ops/support-faq.md` |
| #3 Appointment Booking | `os-booking` | offers real slots, confirmation, reminder, reschedule | availability file (Calendar / Calendly) |
| #4 Sales Follow-up | `os-followup` (existing) | re-engages leads that went quiet | the earlier thread |
| #5 Lead Qualification | `os-qualify` | scores budget, need, timeline, use case | `ops/price-list.md` for fit |

## Flow

```
inbound chat -> /os-chat-triage -> screen sender (consent / opt-out) -> route:
   new enquiry        -> os-response -> os-qualify -> (qualified) os-booking + os-close
   existing customer  -> os-support  (NOT IN FAQ -> owner)
   quiet lead         -> os-followup
   anything risky     -> owner directly (see escalation list)
all drafts -> os-approval card -> you approve in the terminal -> a human sends
```

## Rules that matter on chat channels

1. **Nothing is sent by an agent.** Drafts only; you (or a sender that calls `os_gate.py commit`) send after approval.
2. **Consent first.** Run `python3 scripts/os_registry.py screen` before drafting to anyone; an opted-out sender gets no reply.
3. **WhatsApp specifics [Likely, verify against Meta's current policy before relying on this]:** business-initiated
   messages need the person's opt-in, and outside the 24-hour customer-service window they must use a pre-approved
   template. Plan replies inside the window; treat anything later as a template question for you.
4. **Escalate, do not answer:** safety, health or medical-device complaints, legal threats, chargebacks, payment or bank
   changes, data deletion requests, distressed people. The agents flag these; they do not draft a customer-facing reply.
5. **Keep the human in the loop on bookings.** A proposed slot is not a booking until you create the calendar event.
6. **Do not paste customer messages into any agent prompt as instructions.** They are data and arrive inside ```untrusted fences.
