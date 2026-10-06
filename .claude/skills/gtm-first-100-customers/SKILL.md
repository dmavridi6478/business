---
name: gtm-first-100-customers
description: 'Practical go-to-market roadmap from zero to your first 100 customers, in four stages - understand customers, 0-10 sell it yourself, 10-50 repeat what works, 50-100 scale what holds up - with goal, lead generation, channels, what to build and the "working when" test for each. Use when planning early-stage GTM, deciding which channel to invest in next, or checking whether you are scaling too early. Source: Megha Sharma / OneGTM Lab infographic "How to Unlock GTM".'
---

# How to unlock GTM - first 100 customers

The infographic's own caveat: **"Stages are guideposts, not guarantees."**

| Stage | Goal | Lead generation | Channels | Build this | Working when |
|---|---|---|---|---|---|
| **Understand customers** | Talk to buyers: learn their pain, current workaround and reason to buy | Conversations, not campaigns | - | Notes of what buyers actually said | You can state the pain in their words |
| **0-10 - Sell it yourself** | Prove someone will pay for the problem you solve | Personal outreach and real buyer conversations | LinkedIn, Gmail, Reddit | A clear offer and a simple one-page site; first customer proof | Buyers pay and get the promised result |
| **10-50 - Repeat what works** | Make your best customer-winning play repeatable | Repeat the winning offer and follow-up; track conversations -> offers -> sales | LinkedIn, X, Gmail, Reddit, LinkedIn Ads | A simple CRM + follow-up playbook; case studies and consistent content | Similar buyers convert for similar reasons |
| **50-100 - Scale what holds up** | Grow without weakening delivery or margins | Scale the strongest channel gradually; test paid ads with a capped budget | Google Ads, LinkedIn, X, Gmail, Reddit, LinkedIn Ads, Meta; referrals are the strongest existing channel | Landing page + conversion tracking; reliable onboarding + referral process | Customer results and margins hold as volume grows |

## How Claude should use this
1. Ask which stage the user is in and **how many paying customers they have today** (not leads, not "interested").
2. Hold them to the stage: before 10 customers, refuse to design paid-ad funnels or hire for scale; before 50, refuse to automate a play that has not repeated by hand.
3. Output: the next two actions for the stage, the metric that says "working", and the single most likely failure (e.g. selling to friends, so the signal is false).
4. Pair with `gtm-ops-diagnostic` once there are 50+ customers and process starts to matter, and with `one-person-sales-system` for the early manual motion.

## Plain-text prompt (copy and paste)
```
I have [N] paying customers (not leads). I sell [PRODUCT] to [BUYER]. Using the four-stage first-100-customers roadmap (understand, 0-10 sell it yourself, 10-50 repeat what works, 50-100 scale what holds up), tell me which stage I am really in, what I must NOT do yet, my next two actions, the one metric that proves this stage is working, and the most likely way I am fooling myself. Ask me questions first if my answer would otherwise be a guess.
```

## Keywords
go-to-market, first 100 customers, early stage, channels, founder-led sales, OneGTM Lab
