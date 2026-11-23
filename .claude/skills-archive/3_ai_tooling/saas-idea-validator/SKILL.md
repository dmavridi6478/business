---
name: saas-idea-validator
description: Stress-test a SaaS, software, or digital-product idea against market reality — problem-solution fit, realistic market size, existing competition, moat, and a specific reason it might fail. Use this whenever the user describes a new product/software/app/tool idea and wants an honest assessment of whether it's viable — including phrases like "is this a good idea," "should I build this," "validate this idea," or "what do you think of this concept." This is a critical evaluation skill, not a brainstorming or encouragement skill — it should surface the strongest reasons the idea might NOT work, not just cheerlead it.
---

# SaaS Idea Validator

A skill for honest, critical evaluation of a product idea — the opposite of a pitch-deck cheerleading exercise. The most valuable output of this skill is often "here's the specific reason this fails," not a validation stamp.

## When to trigger

- "Is this a good idea for a SaaS/app/tool?" / "should I build this?" / "validate my idea"
- Any new product concept description where the person wants an honest read, not just brainstorming

## Workflow

### 1. Force specificity before evaluating
A vague idea can't be validated. Get: who exactly is the customer (not "businesses" — which businesses, what size, what role), what specific problem it solves, and what they do today instead (the real alternative is rarely "nothing" — it's usually a spreadsheet, a competitor, or a manual workaround). If the idea is vague, ask before proceeding rather than validating a fog.

### 2. Check problem-solution fit first, market size second
Order matters: an idea with no real painful problem behind it fails regardless of market size. Ask: is this a vitamin (nice to have) or a painkiller (actively costing the customer time/money/risk today)? Vitamins are much harder to sell, especially to businesses. Only after establishing real pain, assess market size (rough TAM/SAM, and — more usefully for an early idea — how many people you could realistically reach with a beachhead go-to-market).

### 3. Map the actual competitive landscape
Search for existing solutions before assuming there are none — "nobody else does this" is almost always wrong and usually means the searching wasn't done, not that the space is empty. If competitors exist, the real question is differentiation and defensibility, not existence. If genuinely nobody does this, ask why not — sometimes it's a real opportunity, sometimes it's a market that's been tried and failed for a specific reason worth surfacing.

### 4. Identify the moat honestly
Most SaaS ideas have a weak or no moat at launch (feature parity is copyable within months). Name what could become a moat (data network effects, switching costs, integration depth, brand/community, regulatory/compliance complexity) rather than assuming "we'll just execute better" is a moat — execution speed is an advantage, not a moat.

### 5. Name the specific failure mode
Every idea has a most-likely way it fails — distribution cost exceeds LTV, the buyer isn't the user (classic B2B split), the problem is real but not painful enough to pay for, a platform dependency risk, regulatory friction. Name the SPECIFIC one for this idea, not a generic "execution risk" disclaimer.

### 6. Give a genuine verdict, not a hedge
End with a clear read: proceed as-is / proceed with a specific pivot / kill it — and the one piece of evidence that would most change your mind. Refusing to take a position defeats the purpose of this skill.

## Quality bar

- At least one competitor or adjacent solution was actually searched for, not assumed away.
- The failure mode named is specific to this idea, not a generic risk disclaimer.
- The verdict is a real position, not both-sides hedging.
- Vitamin-vs-painkiller distinction is explicitly addressed.

## Output format
Conversational for a quick gut-check; structured markdown (Problem | Market | Competition | Moat | Most Likely Failure Mode | Verdict) for a formal validation writeup.

## Related skills in this repo

- **product-strategy-session**: Use that instead when the idea has passed an initial gut-check and needs a full multi-week positioning/discovery/roadmap process.
- **the-productize-yourself-blueprint**: Apply this validator's critical lens to the productized-service idea that blueprint produces, before committing to build it.
- **content-repurposing-service**: A concrete example service this skill's framework (problem-solution fit, competition, moat, failure mode) can be applied to.
