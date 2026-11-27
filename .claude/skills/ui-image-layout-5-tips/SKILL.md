---
name: ui-image-layout-5-tips
description: Five UI layout tips for placing images with text - split images into columns, put images outside the layout for an immersive feel, wrap text smartly, make some images lead the pack, and add dynamic sizes to a grid - each with the do and the don't. Use when designing article pages, galleries, cards or landing sections that mix images and text. Source @iqonicdesign / @ux_dose "5 Tips To Help You In UI Design" carousel (Batch 103). Cover slide plus 5 tip slides; all 6 were in the upload. Also holds the six "UI feels cheap" polish checks from the @ux_dose / Meya Lab Studio carousel (Batch 112): cue overload, font sizes, spacing, shadows, icon sets, alignment.
---

# 5 tips for images in UI layouts

| # | Tip | Do not | Do |
|---|---|---|---|
| 1 | Split images into columns | Wrap text around a single image so the text column gets narrow | Split the view into separate columns: image in one, text in the other |
| 2 | Put images outside the layout | Keep every image inside the text column | Let an image break out of the column (full bleed or beside it) for a more immersive page or article |
| 3 | Use text wrapping smartly | Interrupt the reading flow with the image mid-paragraph | Align images inside a paragraph to the top or right, so the eye keeps its line |
| 4 | Make images stand out | Show a screen of equal-sized images | With multiple images, make some lead the pack: one large hero, smaller supporting images |
| 5 | Add dynamic to the layout | Repeat a uniform grid (3 x 4 equal tiles) | Employ multiple columns and image sizes so scrolling is more interactive |

## Applying them
- Use CSS grid with named areas for tips 1 and 4, `float` or `shape-outside` only for tip 3, and a negative inline margin or `grid-column: 1 / -1` for tip 2.
- Keep one focal image per viewport; a "bento" or masonry grid (tip 5) is only worth it with at least 6 images.
- Check each layout at 400 px wide: columns should stack and the lead image should stay first.
- Template: `design-templates/templates/ui-tip-do-dont.html` reproduces the do/don't card format. Related skills: `responsive-design`, `visual-design-foundations`, `better-layout`.

## Six "feels cheap" polish checks (Batch 112, @ux_dose / Meya Lab Studio)

Source: 7-slide carousel; slide 7 was not in the files, so only six checks are recorded and none invented. Template: `design-templates/templates/ui-tip-before-after.html`. Related: `better-ui`, `make-interfaces-feel-better`.

| # | Defect ("before") | Fix ("after") | Test you can run |
|---|---|---|---|
| 1 | Cheap cues: all-caps shouting labels, "!!", footnote asterisks, loud green and orange buttons | Plain label, one dark primary button, calm copy ("Start free trial") | Count colours of buttons on screen; more than one primary is a defect |
| 2 | Too many font sizes: eleven sizes on one page | A scale of five or six, e.g. Display 32, Title 24, Heading 18, Body 15, Small 13 | List every distinct font-size; more than six fails |
| 3 | Random spacing: 13px here, 22px there | A 4 or 8 point system (4, 8, 16, 24 ...) | Every margin and gap divisible by 4 |
| 4 | Heavy shadows: dark, blurry drop shadows look dated | Lighter, softer shadow, or a 1px border instead | Shadow opacity under about 12 percent, or border only |
| 5 | Mixed icon sets: outline next to filled, thick next to thin | One icon family, one stroke weight | All icons from one set at one stroke width |
| 6 | Almost-aligned: off by 2px feels worse than off by 20px | Snap to the same edge; check at 400 percent zoom | Overlay a vertical guide at zoom 400 |

### Audit procedure

1. Take the screenshot, URL or component the user gives. Do not redesign; audit.
2. Walk the six checks; for each give pass / fail, the evidence (what you counted) and the one-line fix.
3. Output a fix list ordered by effort (token changes first: type scale, spacing scale, shadow, icon set), then by component.
4. If CSS is in the repo, propose token values; apply only if asked.
