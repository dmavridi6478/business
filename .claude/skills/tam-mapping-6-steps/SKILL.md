---
name: tam-mapping-6-steps
description: Six-step TAM mapping playbook from CRM to first send (define the ICP from closed-won and closed-lost deals, build the full account list, split into segments, pick a path per segment, score and tier every account, find the right people at tier-one accounts) with a vendor-neutral method, data-provenance and outreach-law checks, and the claims that are vendor marketing. Use when mapping a total addressable market for outbound.
---

# The 6-step TAM mapping playbook

Source: an infographic by Michel Lieben, founder of ColdIQ (Batch 121), titled "From your CRM to the first send in 6 steps. ColdIQ orchestrates the data." It is a vendor graphic: the data-provider mix ("70% ColdIQ unlimited lookups at a flat price, 30% unified API waterfall across 28+ providers") describes the vendor's product and is not a method claim. The six steps are sound and vendor-neutral.

| Step | Graphic | Method (vendor-neutral) |
|---|---|---|
| 1 | Start in your CRM: closed-won and closed-lost deals define your ICP | Pull 12 to 24 months of won and lost deals; compare firmographics, buying triggers and cycle length; write the ICP as testable rules |
| 2 | Build the full account list | Combine one primary data source with fallback sources for gaps ("one provider misses, the next one answers"); de-duplicate against the CRM; record the source and date of every field |
| 3 | Split it into segments | Tag by region, industry and size (examples: UK Tech, DACH Tech, DACH Services, AUS Services) |
| 4 | Pick a path per segment | **A: blast first**, then enrich only repliers (cheap, fast, lower precision). **B: enrich first**, with signals and tech stack (costly, precise) |
| 5 | Score every account | **T1 priority**: every channel. **T2 volume**: cold email. **T3 nurture**: re-score quarterly |
| 6 | Find the right people | Decision makers at tier-1 accounts get the first send ("T1 x P1 = first send") |

## Checks the graphic leaves out
- **Closed-lost matters, and survivorship bias is real.** Your CRM only holds companies you already reached; the ICP from it may miss segments you never tried. Add a hypothesis test for one new segment.
- **Data quality.** Waterfall enrichment multiplies cost per provider and still returns stale or wrong data. Sample 50 records per segment and check them by hand before scoring.
- **Lawful outreach.** DACH, UK and EU rules on personal data and cold email are strict (for example UK and EU GDPR, and Germany's competition law on unsolicited email advertising). [Likely] B2B cold email is not free of consent rules in every country. Get legal advice per region, keep a suppression list, and give an easy opt-out.
- **Scoring is a model.** Define each tier by explicit rules or a documented score; review a sample of tier-1 and tier-3 accounts with sales each quarter.
- **Do not decide the path by tool.** Choose A or B per segment by deal value: enrich-first only pays where deals are large.

## Output of this skill
1. ICP rules from won and lost deals (with the sample size). 2. A TAM table: segment, account count, source, data age. 3. Path per segment with a cost per qualified account estimate. 4. Tier definitions and the count per tier. 5. A persona list for tier-1 accounts. 6. A first-send plan with legal review per region and a 30-day measurement (reply, meeting, cost per meeting).

Run with `/tam-map <ICP, regions, CRM export summary>`. Related: `build-and-fill-a-tam`, `gtm-engineer-skills` (command), `icp-builder`, `icp-score-and-route`, `lead-gen-route`, `list-architect`, `data-enrichment`, `signal-sourcer`, `trigger-based-outbound`, `gtm-api-stack`, `outbound-campaign-brief`.
