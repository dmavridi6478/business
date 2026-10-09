---
description: 5 UI design styles to recognize and generate (Glassmorphism, Neumorphism, Neobrutalism, Flat Design, Minimalism), with prompt-ready visual descriptions for each
argument-hint: [style name, or "all" for the full reference]
---

# 5 UI Design Styles You Should Know

Source: @designwithbyy, "5 UI Design Styles You Should Know." A visual-style reference (what each style looks like and when to reach for it), distinct from this repo's `design-templates` skill (ready-to-use copy-paste HTML/CSS layouts for specific content types like carousels, brand boards, pricing tables). Use this file to pick a style; use `design-templates` for the actual markup once you know which style you want.

## 1. Glassmorphism

Frosted-glass panels: translucent, blurred backgrounds behind foreground UI elements, subtle light borders, soft shadows for depth. Seen in: smart-home dashboards, account/settings menus over a blurred photo background, dark analytics cards with glowing accent numbers.

**Prompt to generate this style:**
```
Design a [DASHBOARD/CARD/MENU] in glassmorphism style: translucent frosted-
glass panels over a blurred background image, subtle white border at low
opacity, soft drop shadow, rounded corners. Use [LIGHT/DARK] mode with one
accent color for key numbers/CTAs.
```

## 2. Neumorphism

Soft, extruded/embossed surfaces that look pressed into or raised out of the same-color background — subtle dual-direction shadows (light + dark) instead of hard borders. Best for: settings toggles, media player controls, calendar pickers, low-contrast monochrome interfaces.

**Prompt to generate this style:**
```
Design a [SETTINGS PANEL/MEDIA CONTROLS/CALENDAR] in neumorphism style: same
background and element color throughout, soft embossed/pressed-in shadow
effect (light shadow top-left, dark shadow bottom-right) instead of borders,
rounded corners, minimal color — one accent color maximum for active states.
```

## 3. Neobrutalism

Loud, high-contrast, deliberately "undesigned": thick black borders, flat saturated colors (cyan, magenta, lime, yellow), hard drop shadows with no blur, bold sans-serif type, visible grid/window-chrome elements (fake minimize/close buttons). Best for: brand personality that wants to feel loud/confident rather than polished — book launches, indie SaaS, youth-brand apps.

**Prompt to generate this style:**
```
Design a [APP SCREEN/LANDING SECTION/PRODUCT CARD] in neobrutalism style:
thick solid black borders on every element, flat saturated color blocks
(pick 3-4 from cyan/magenta/lime/yellow/hot pink), hard-edged drop shadows
with zero blur, bold uppercase sans-serif headlines, no gradients, no soft
corners.
```

## 4. Flat Design

Clean, solid-color surfaces with no shadows, gradients, or textures — depth communicated through color contrast, spacing, and typography alone. Rounded pill-shaped buttons and toggles. Best for: fintech/crypto dashboards, transaction flows, anything needing to feel simple and trustworthy.

**Prompt to generate this style:**
```
Design a [DASHBOARD/TRANSACTION FLOW/FORM] in flat design style: solid flat
colors with no shadows or gradients, pill-shaped buttons and toggles,
generous whitespace, one saturated accent color against neutral
light/dark backgrounds, clear numeric hierarchy (large bold numbers for
key figures).
```

## 5. Minimalism

Maximum whitespace, restrained (often just black/white) palette, large confident typography as the primary visual element, few or no decorative elements. Best for: designer/agency portfolios, personal brand sites, editorial content.

**Prompt to generate this style:**
```
Design a [PORTFOLIO HOME/AGENCY LANDING/PROFILE PAGE] in minimalist style:
mostly white background, black text, one large bold typographic statement
as the hero element, no color accents beyond black/white/one neutral grey,
generous margins, a simple text-only nav, black-and-white photography if
any images are used.
```

## Picking one when you don't know which to use

```
I'm designing [WHAT YOU'RE BUILDING] for [BRAND/AUDIENCE]. Given these 5
styles — Glassmorphism, Neumorphism, Neobrutalism, Flat Design, Minimalism —
which one fits the brand personality I want ([DESCRIBE IN 1-2 WORDS: e.g.
"loud and confident" / "quiet and trustworthy" / "playful"])? Then generate
the design in that style.
```

Once you've picked a style, check `design-templates` for a ready-made layout (carousel, brand board, pricing table, etc.) to build the actual page in.
