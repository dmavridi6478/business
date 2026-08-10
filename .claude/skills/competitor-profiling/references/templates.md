# Competitor Profile & Summary Templates

*Authored directly for this repo — the parent skill's Output Format section pointed here, but no source content shipped with the install. This fills that gap with the same templates the parent skill describes inline, extracted here as standalone copy-paste files.*

## Individual profile template

Save as `competitor-profiles/[competitor-name].md`:

```markdown
# [Competitor Name] — Competitor Profile

**URL**: [website]
**Generated**: [date]
**Depth**: [quick scan / deep profile]

---

## At a Glance

| Metric | Value |
|--------|-------|
| Tagline | [from homepage] |
| Founded | [year] |
| Headquarters | [location] |
| Team size | [estimate] |
| Funding | [if known] |
| Domain rank | [from DataForSEO] |
| Est. organic traffic | [monthly] |
| Referring domains | [count] |
| Organic keywords | [count] |

---

## Positioning & Messaging

**Primary value proposition**: [headline + subheadline from homepage]

**Target audience**: [who they're speaking to, based on copy analysis]

**Positioning angle**: [how they position — e.g., "simplicity-first," "enterprise-grade," "all-in-one"]

**Key messaging themes**:
- [theme 1 — with source page]
- [theme 2]
- [theme 3]

---

## Product & Features

### Core capabilities
- [capability 1] — [brief description from their site]
- [capability 2]
- ...

### Notable differentiators
- [what they emphasize as unique]

### Integrations
- [count] integrations
- Key: [list top 5-10]

### Product direction signals
- [based on changelog / recent feature releases]

---

## Pricing

| Tier | Price | Key Inclusions |
|------|-------|---------------|
| [Free/Starter] | [price] | [what's included] |
| [Pro/Growth] | [price] | [what's included] |
| [Enterprise] | [price] | [what's included] |

**Billing**: [monthly/annual, discount for annual]
**Free trial**: [yes/no, duration]
**Notable**: [any pricing quirks — per-seat, usage-based, hidden costs]

---

## Customers & Social Proof

**Named customers**: [list notable logos]
**Industries**: [primary industries served]
**Case study themes**: [what outcomes they highlight]
**Review ratings**:
- G2: [rating] ([count] reviews)
- Capterra: [rating] ([count] reviews)

---

## SEO & Content Strategy

**Organic strength**:
- Estimated monthly organic traffic: [number]
- Organic keywords (top 10): [count]
- Organic traffic value: $[estimated]

**Top organic pages** (by estimated traffic):
1. [page URL] — [keyword] — [est. traffic]
2. [page URL] — [keyword] — [est. traffic]
3. [page URL] — [keyword] — [est. traffic]

**Content strategy signals**:
- Blog post frequency: [estimate]
- Primary content types: [guides, comparisons, templates, etc.]
- Content focus areas: [topics they invest in]

**Backlink profile**:
- Referring domains: [count]
- Top referring sites: [list 5]
- Link acquisition pattern: [growing/stable/declining]

---

## Strengths & Weaknesses

### Strengths
- [strength 1 — with evidence source]
- [strength 2]
- [strength 3]

### Weaknesses
- [weakness 1 — with evidence source]
- [weakness 2]
- [weakness 3]

---

## Competitive Implications for [Your Product]

**Where they're strong vs. us**: [areas where this competitor has an advantage]

**Where we're strong vs. them**: [areas where you have an advantage]

**Opportunities**: [gaps in their offering or positioning we can exploit]

**Threats**: [areas where they're improving or gaining ground]

---

## Raw Data Sources

- Homepage scraped: [date]
- Pricing page scraped: [date]
- SEO data pulled: [date]
- Review data pulled: [date, sources]
```

## Summary document template

Save as `competitor-profiles/_summary.md`, after all individual profiles are complete:

```markdown
# Competitive Landscape Summary

**Generated**: [date]
**Competitors profiled**: [list]

---

## 1. Competitor Landscape Overview

[One paragraph summarizing the competitive field — how crowded it is,
what the dominant positioning axes are, where the real fight is happening]

---

## 2. Comparison Table

| Metric | [Competitor A] | [Competitor B] | [Competitor C] | You |
|---|---|---|---|---|
| Founded | | | | |
| Pricing (entry tier) | | | | |
| Est. organic traffic | | | | |
| Domain rank | | | | |
| G2 rating | | | | |
| Positioning angle | | | | |

---

## 3. Positioning Map

[Plot each competitor on two relevant axes — e.g. simple↔complex,
cheap↔premium, self-serve↔enterprise-sales. Describe the map in words
or generate it as an actual chart via the dataviz skill if a visual
artifact is wanted.]

---

## 4. Key Takeaways

1. [Strategic observation 1]
2. [Strategic observation 2]
3. [Strategic observation 3]

---

## 5. Gaps and Opportunities

- [Where the market is underserved — a positioning angle, price point,
  or feature set nobody's covering well]
- [Repeat for each identified gap]
```

## Using these templates

- Fill every bracketed field from sourced data (scrape or DataForSEO response) saved in `raw/` — never fill a field from memory or assumption. Leave it as `[unknown]` rather than guessing.
- Keep the summary document's comparison table columns identical across a full competitive set — inconsistent metrics between competitors defeats the table's purpose.
