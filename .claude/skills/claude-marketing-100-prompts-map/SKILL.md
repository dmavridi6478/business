---
name: claude-marketing-100-prompts-map
description: Map of the klaym.ai graphic "100 Claude Code Prompts for Marketing" (a README.md and folder tree of 10 categories, 5 prompt titles shown per category) with the 50 visible prompt titles, what each category is for, and what the graphic does not give you (the prompts themselves, which are behind a "comment MARKETING" gate). Includes how to build your own prompt library with the same folder structure. Use when planning a marketing prompt library or checking what is and is not in that giveaway.
---

# "100 Claude Code Prompts for Marketing" (klaym.ai): what is actually shown

Source: one graphic styled as a code editor: a `claude-marketing-prompts/` folder tree on the left (ten folders, each with `prompt-01.md` to `prompt-04.md` and "...") and a README on the right. The graphic shows **category names and five prompt titles per category (50 titles)**, not the prompts. The call to action is "COMMENT MARKETING FOR FREE ACCESS", a lead-capture mechanic. I did not receive the prompts and have not invented them. Note: the graphic says 100 prompts; only 50 titles are visible, so "100" is unverified.

| # | Folder | Visible titles |
|---|---|---|
| 01 | research | Market Research; Market Segmentation; Customer Research; Customer Interview Analysis; Voice-of-Customer Analysis |
| 02 | strategy | Marketing Strategy; 90-Day Marketing Planning; Go-to-Market Strategy; Channel Strategy; Campaign Strategy |
| 03 | positioning | Positioning Analysis; Positioning Development; Value Proposition; Messaging Architecture; Customer Pain to Solution Mapping |
| 04 | content | Content Strategy; Content Opportunity Discovery; Content Ideation; Content Calendar Creation; Content Brief Creation |
| 05 | seo-aeo | Keyword Research; Search Intent Analysis; Keyword Clustering; SERP Analysis (Supplied Data); Competitor Content Gaps |
| 06 | social-linkedin | Social Media Strategy; LinkedIn Strategy; Content Idea Generation (Social); Hook Development; LinkedIn Post Creation |
| 07 | email | Email Strategy; Newsletter Strategy; Newsletter Creation; Welcome Sequences; Lead Nurture Sequences |
| 08 | demand-generation | Demand Generation Strategy; Campaign Planning; Campaign Brief Creation; Paid Campaign Ideation; Webinar and Event Campaign Planning |
| 09 | conversion-cro | Landing Page Heuristic Review; Landing Page Copywriting; CRO Audit (Data-Supported); A/B Test Ideation; A/B Test Result Analysis |
| 10 | analytics | Marketing Performance Reporting; Channel Performance Analysis; Campaign Performance Rollup; Email Performance Analysis; Attribution Analysis (Supplied Data) |

Telling detail: several titles say "(Supplied Data)" or "(Data-Supported)". That is the right design: an LLM cannot see your SERP, analytics or attribution unless you paste the data, and it should say so rather than invent figures.

## Build your own library from this structure

1. Create `marketing-prompts/` with the ten folders and a `README.md` index.
2. For each title write one prompt with: role, task, required inputs you will paste, output format, and a "do not invent data; list what you could not check" line.
3. Use existing skills as the starting point instead of buying a list: `claude-marketing-8-frameworks`, `content-strategy`, `positioning`, `seo-audit`, `cold-email`, `cro`, `marketing-plan`, `/seo-prompts-10`, `/cowork-marketing-20`, `kpi-dashboard-design`.

## Not done

I did not request the giveaway, and nothing from it is in this repository.
