---
name: new-client-system
description: Build a complete client acquisition system — outreach strategies, follow-up sequences, sales pipeline structure, proposal templates, and onboarding SOPs — for a service business, agency, or freelancer. Use when the user is starting or scaling a client-based business and needs a systematic way to find, pitch, convert, and onboard clients rather than relying on random referrals. Source: @the.wealth.lab "6 Favorite Claude Skills That Automate Almost Anything."
---

# New Client System

Source: @the.wealth.lab "6 Favorite Claude Skills That Automate Almost Anything."

> Build outreach strategies, follow-up sequences, sales pipelines, proposals, and onboarding SOPs that turn cold leads into paying clients consistently.

## What this skill produces

A complete end-to-end client acquisition system for a service business:
- **Outreach strategy**: which channels, what message, what volume
- **Cold outreach templates**: DM, email, LinkedIn — platform-native, not copy-paste spam
- **Follow-up sequence**: timing, tone, and content for 3–5 touchpoints
- **Sales pipeline structure**: stages, criteria for moving a lead, how long before cutting bait
- **Proposal template**: structure and copy framework for a winning proposal
- **Onboarding SOP**: the first 7 days after a client signs — what happens, in what order, who does what

## The system structure

```
FIND → QUALIFY → OUTREACH → FOLLOW-UP → CLOSE → ONBOARD
```

| Stage | Goal | Output from this skill |
|---|---|---|
| Find | Identify right-fit leads | Lead criteria + sourcing channels |
| Qualify | Filter before wasting time | 3 qualifying questions |
| Outreach | Start a real conversation | Channel-specific templates |
| Follow-up | Stay visible without being annoying | 4-touch sequence with timing |
| Close | Convert the conversation | Proposal structure + call framework |
| Onboard | Deliver confidence from day one | 7-day onboarding SOP |

## Copy-paste prompt to use

```
You are a client acquisition strategist who helps service businesses, agencies, and freelancers build predictable systems for getting clients.

My service: [DESCRIBE WHAT YOU SELL AND WHO YOU SELL IT TO]
My ideal client: [JOB TITLE / COMPANY SIZE / INDUSTRY / SPECIFIC PAIN POINT]
Current situation: [HOW DO I GET CLIENTS NOW — referrals, ads, cold outreach, none?]
Price point: [ROUGH RANGE — e.g. $500/mo retainer, $3,000 project, etc.]
My bandwidth: [HOURS PER WEEK I CAN SPEND ON SALES]

Build me a complete new-client system:

1. Outreach strategy — which 2 channels to focus on and why (choose from: cold email, LinkedIn DMs, Instagram DMs, Reddit, community forums, warm referral asks, content-led inbound)
2. Lead criteria — 5 signals that tell me a prospect is worth reaching out to
3. Cold outreach templates for each channel — write the actual messages, not the structure
4. Follow-up sequence — 4 touchpoints with exact timing, tone, and what to say
5. Qualifying questions — 3 questions that tell me fast if someone is a real buyer
6. Proposal structure — section-by-section outline + the 1–2 paragraphs that win proposals
7. 7-day onboarding SOP — checklist of what happens after they sign, in order

Make it specific to my service and price point. Don't give me generic advice.
```

## Pairing with lead generation

This skill handles the system — pairing with `lead-scraper` gets the actual list of people to outreach:
1. Run `lead-scraper` to build the prospect list
2. Run `new-client-system` to build the outreach system
3. Combine: apply the system to the list

## Related skills

- **lead-scraper**: Find the actual leads this system targets
- **sales-enablement**: Proposal writing and pitch deck layer on top of this skill's close stage
- **content-repurposing-service**: Inbound content strategy feeds warm leads into this system
- **product-marketing-context**: Nail the positioning before writing outreach templates
- **the-leverage-stack-auditor**: Check whether client acquisition is a bottleneck vs. delivery capacity before investing in this system
- **n8n-agent-builder**: Automate the follow-up sequence and CRM updates with n8n workflows
