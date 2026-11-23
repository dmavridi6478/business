# Design DNA

Reverse-engineer any website's visual design — typography, color palette, layout patterns, and spacing — then replicate or adapt the style with precision.

Repo: `zanwei/design-dna`

## What it does

- Reverse-engineer designs from screenshots or URLs
- Replicate any UI style (typography, spacing, color)
- Extract curated color palettes
- Surface refined typography insights (font stack, weight, size scale)
- Deliver detailed layout analysis (grid, whitespace, hierarchy)

## Workflow

### Step 1 — Analyse a design

```
Analyse the design at [URL or describe the screenshot].

Extract and report:
1. Color palette — primary, secondary, accent, neutrals (hex values)
2. Typography — font families, weights used, size scale (px/rem), line heights
3. Layout — grid system, max-width, column count, gutter size
4. Spacing system — base unit, padding/margin patterns (4px / 8px / 16px scale?)
5. Component patterns — card style, button radius, shadow depth, border use
6. Overall visual mood — 3 adjectives
```

### Step 2 — Replicate the style

```
Using the Design DNA extracted above, recreate [component/page] in [React / HTML+CSS / Tailwind].
Match: color palette, font choices, spacing rhythm, border-radius, and shadow levels exactly.
Do not copy content — only clone the visual DNA.
```

### Step 3 — Adapt to my brand

```
I have this Design DNA: [paste Step 1 output].
My brand colors are: [hex values].
My font is: [font name].

Adapt the layout and component patterns to my brand while keeping the structural DNA intact.
Output: CSS variables + updated component code.
```

## Prompt

```
Act as a UI design analyst. Reverse-engineer the design of [site/screenshot].
Give me: color palette (hex), font stack, spacing scale, layout grid, and 3 reusable component patterns.
Format as a Design DNA card I can paste into future prompts.
```
