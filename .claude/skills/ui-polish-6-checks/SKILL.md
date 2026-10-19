---
name: ui-polish-6-checks
description: Six-check UI polish audit from the @ux_dose / Meya Lab Studio carousel 'Why your UI feels cheap and how to fix it' - heavy shadows, too many font sizes, random spacing, mixed icon sets, almost-aligned elements, shouting buttons and pricing - each with the before/after fix. Use when reviewing a landing page, pricing card, dashboard or screenshot that feels amateur. Run via /ui-polish. Complements ui-image-layout-5-tips (layout) and design-templates.
---

# UI polish - six checks

Source: @ux_dose carousel, 7 slides (slide 7 was not in the files, so only six checks are recorded; nothing is invented for it).

| # | Defect ("before") | Fix ("after") | Test you can run |
|---|---|---|---|
| 1 | Cheap cues: all-caps shouting labels, "!!", footnote asterisks, loud green and orange buttons | Plain label, one dark primary button, calm copy ("Start free trial") | Count colours of buttons on screen; more than one primary is a defect |
| 2 | Too many font sizes: eleven sizes on one page | A scale of five or six, e.g. Display 32, Title 24, Heading 18, Body 15, Small 13 | List every distinct font-size; more than six fails |
| 3 | Random spacing: 13px here, 22px there | A 4 or 8 point system (4, 8, 16, 24 ...) | Every margin and gap divisible by 4 |
| 4 | Heavy shadows: dark, blurry drop shadows look dated | Lighter, softer shadow, or a 1px border instead | Shadow opacity under about 12 percent, or border only |
| 5 | Mixed icon sets: outline next to filled, thick next to thin | One icon family, one stroke weight | All icons from one set at one stroke width |
| 6 | Almost-aligned: off by 2px feels worse than off by 20px | Snap to the same edge; check at 400 percent zoom | Overlay a vertical guide at zoom 400 |

## Procedure

1. Take the screenshot, URL or component the user gives. Do not redesign; audit.
2. Walk the six checks; for each give pass / fail, the evidence (what you counted) and the one-line fix.
3. Output a fix list ordered by effort (token changes first: type scale, spacing scale, shadow, icon set), then by component.
4. If CSS is in the repo, propose token values; apply only if asked.

House rules for deliverables: Aptos, body 11, title 32, heading 14, table content top and centre.
