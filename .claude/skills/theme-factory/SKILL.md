---
name: theme-factory
description: Toolkit for styling artifacts with a theme. These artifacts can be slides, docs, reportings, HTML landing pages, etc. There are 10 pre-set themes with colors/fonts that you can apply to any artifact that has been creating, or can generate a new theme on-the-fly.
license: Complete terms in LICENSE.txt
---


# Theme Factory Skill

This skill provides a curated collection of professional font and color themes themes, each with carefully selected color palettes and font pairings. Once a theme is chosen, it can be applied to any artifact.

## Purpose

To apply consistent, professional styling to presentation slide decks, use this skill. Each theme includes:
- A cohesive color palette with hex codes
- Complementary font pairings for headers and body text
- A distinct visual identity suitable for different contexts and audiences

## Usage Instructions

To apply styling to a slide deck or other artifact:

1. **Show the theme showcase**: Display the `theme-showcase.pdf` file to allow users to see all available themes visually. Do not make any modifications to it; simply show the file for viewing.
2. **Ask for their choice**: Ask which theme to apply to the deck
3. **Wait for selection**: Get explicit confirmation about the chosen theme
4. **Apply the theme**: Once a theme has been chosen, apply the selected theme's colors and fonts to the deck/artifact

## Themes Available

The following 17 themes are available (1–10 showcased in `theme-showcase.pdf`; 11–17 added from uploaded reference images, previewed by the matching templates in `design-templates`):

1. **Ocean Depths** - Professional and calming maritime theme
2. **Sunset Boulevard** - Warm and vibrant sunset colors
3. **Forest Canopy** - Natural and grounded earth tones
4. **Modern Minimalist** - Clean and contemporary grayscale
5. **Golden Hour** - Rich and warm autumnal palette
6. **Arctic Frost** - Cool and crisp winter-inspired theme
7. **Desert Rose** - Soft and sophisticated dusty tones
8. **Tech Innovation** - Bold and modern tech aesthetic
9. **Botanical Garden** - Fresh and organic garden colors
10. **Midnight Galaxy** - Dramatic and cosmic deep tones
11. **Warm Creator Carousel** - Cream canvas, cocoa-to-peach gradient headlines, numbered badges (template: `numbered-workflow-carousel.html`, `carousel-cover-dark.html`)
12. **Governed Infographic** - Cream editorial page, heavy black headline, colour-coded layer bands (template: `layered-framework-infographic.html`)
13. **Peach Stack** - Cream-to-peach gradient, tinted 3D slabs stacked as a pyramid (template: `stacked-layer-pyramid.html`)
14. **Concentric Rainbow** - Pastel concentric rings, white label pills, heavy headline (template: `concentric-rings-framework.html`)
15. **Adaptive Pink** - Grey "traditional" vs pink/lilac "new way" columns, numbered pink/violet badges (template: `two-column-shift-comparison.html`)
16. **Prosp Dark Grid** - Charcoal org-chart grid, cyan/orange outlined job cards, orange CTA bar
17. **Workflow Grid Sunset** - Peach-to-coral gradient, dense pastel-tinted icon-tile grid for 50-100 items, orange/pink headline (template: `workflow-grid-catalog.html`)

## Theme Details

Each theme is defined in the `themes/` directory with complete specifications including:
- Cohesive color palette with hex codes
- Complementary font pairings for headers and body text
- Distinct visual identity suitable for different contexts and audiences

## Application Process

After a preferred theme is selected:
1. Read the corresponding theme file from the `themes/` directory
2. Apply the specified colors and fonts consistently throughout the deck
3. Ensure proper contrast and readability
4. Maintain the theme's visual identity across all slides

## Create your Own Theme
To handle cases where none of the existing themes work for an artifact, create a custom theme. Based on provided inputs, generate a new theme similar to the ones above. Give the theme a similar name describing what the font/color combinations represent. Use any basic description provided to choose appropriate colors/fonts. After generating the theme, show it for review and verification. Following that, apply the theme as described above.

## Related skills in this repo

- **frontend-design**, **premium-html-presentation**, **canvas-design**, **pptx**: Apply a theme from here as the starting palette/typography for any of these instead of picking colors from scratch.
- **product-marketing-context**: When the artifact needs the user's *own* brand rather than one of these preset themes, pull colors/voice from there instead (see the caveat on `brand-guidelines`, which is Anthropic-specific, not a generic brand tool).
- **design-token-extractor**: When matching a specific external reference rather than picking a preset, extract real tokens from it instead.
- **brandkit-generator**: A preset theme here can seed the starting palette/typography for a brand direction before it's refined into a full brand board.
