---
name: startup-investor-kit
description: Turn one startup idea into an investor kit - market analysis, competitor map, product spec, business model, pitch deck, product roadmap, investor pitch and a landing page - after a viability gate that refuses to polish a bad idea. A Claude-native equivalent of the "startup-architect" workflow shown in an @aiclawbots carousel (which ran on the Hermes agent); the carousel's repo could not be identified, so this skill does not depend on it. Use when someone has an idea in their notes and needs something structured enough to show people.
---

# Startup investor kit

**Source and honesty note.** The carousel (4 slides, @aiclawbots) says a free repo called "hermes-startup-architect" builds 8 files from an idea. I could not find a repo by that name; a different, unrelated project (`33hodl/hermes-startup`, MIT) turned up in search and I did not confirm it is the same. So this is a **from-scratch skill**, not an install of that repo. Its best idea is on slide 7: *"It can't turn a terrible idea into a great business ... nicely formatted, still a bad idea."* - hence the gate.

## Step 0 - Viability gate (do not skip)
Score the idea 0-2 on each; **if the total is below 6/10, stop and say why instead of producing the kit.**
1. A named buyer who has the problem now (not "everyone").
2. A painful, frequent problem with a current workaround they already pay for or suffer.
3. A way to reach 10 of those buyers this month without paid ads.
4. A believable reason this beats the workaround (not "AI-powered").
5. A price point and unit economics that can work at small scale.
Say which scores are evidence and which are guesses.

## Step 1 - Gather (ask, do not assume)
Idea in one sentence; who it is for; where they hang out; what they do today; any numbers the user really has; geography; constraints (time, money, skills).

## Step 2 - Produce 8 files in `data/investor-kit/<idea-slug>/`
| File | Contents |
|---|---|
| `market_analysis.md` | Bottom-up TAM/SAM/SOM (buyers x price x reach) with every input labelled `[user]`, `[sourced: URL]` or `[assumption]`; no top-down "1% of a $50B market" |
| `competitor_map.md` | Direct, indirect, and do-nothing alternatives; pricing; weakness; table; sources |
| `product_spec.md` | Problem, user stories, MVP scope vs later, non-goals |
| `business_model.md` | Revenue model, pricing, cost of delivery, break-even, 3 scenarios |
| `product_roadmap.md` | 30/60/90 days then 12 months; each step has a test that could fail |
| `pitch_deck.md` | Problem, Solution, Market, Revenue, Competition, Roadmap (+ Team, Ask) - one message per slide |
| `investor_pitch.md` | 2-minute spoken pitch + the 5 questions an investor will ask and honest answers |
| `landing_page.html` | Single-file page with headline, 3 benefits, proof placeholder, one call to action; no invented testimonials |

## Rules
- Every number carries its label. No invented customers, quotes or traction. Missing evidence -> `[NEEDS EVIDENCE]`.
- Prefer sources found with the repo's research tools (`/hyperresearch`) for the market and competitor files; say when you did not search.
- Financial projections are scenarios, not predictions; show the assumption that moves the answer most.
- Drafts only; nothing is sent to an investor.

Command: `/investor-kit`. To render the deck as slides use the `pptx` or `ai-canva-presentations` skills; the carousel's blueprint-grid look can be reused from `design-templates` > `repo-card-slide.html?theme=blueprint`.

## Plain-text prompt (copy and paste)
```
I want to build [IDEA IN ONE SENTENCE] for [BUYER]. First run a viability gate: score (0-2 each) named buyer, painful frequent problem with a current workaround, a way to reach 10 buyers this month without ads, a believable reason it beats the workaround, and workable unit economics. If the total is under 6/10, tell me why and stop. If it passes, research the market and competitors, then write: market_analysis, competitor_map, product_spec, business_model, product_roadmap, pitch_deck, investor_pitch and a one-file landing_page.html. Label every number [user], [sourced: URL] or [assumption]. Do not invent traction, customers or quotes.
```

## Keywords
investor kit, pitch deck, market analysis, TAM SAM SOM, startup idea validation, financial projections
