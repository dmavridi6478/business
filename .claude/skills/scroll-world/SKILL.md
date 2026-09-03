---
name: scroll-world
description: Turn any brand into an immersive, scrollable 3D website. Use this skill when the user asks to build a 3D brand site, immersive scrollable experience, parallax brand showcase, or runs /scroll-world. Generates production-grade Three.js / CSS 3D transform HTML that "moves" as the user scrolls, with floating elements, depth, and cinematic feel.
---

# Scroll World — Immersive 3D Brand Website Generator

You turn a brand (name + description + optional colors/assets) into a complete, self-contained HTML file that feels like a 3D world the user scrolls through. Clients pay premium rates for this kind of experience.

## What to Build

A single HTML file with:
- **CSS 3D transforms + scroll-driven animations** — elements rotate, float, and parallax as the user scrolls
- **Three.js particle background or floating geometry** (load from cdnjs)
- **Sections**: Hero → About/Story → Featured Work/Products → Contact CTA
- **Typography**: Bold, distinctive display font from Google Fonts paired with refined body
- **Color**: Dark by default unless brand specifies otherwise; rich, cinematic palette
- **Interactions**: Hover glows, subtle tilt on mouse move (vanilla JS), smooth scroll with IntersectionObserver reveals
- **Performance**: All assets inlined or CDN; no external dependencies beyond cdnjs + Google Fonts

## Process

1. Ask (or infer from context): brand name, tagline, primary color, industry/vibe, any featured work/products
2. Choose a bold aesthetic direction: floating islands, deep-space, brutalist geometry, liquid glass, etc.
3. Build the complete HTML. The scroll must feel physical — elements have weight and depth.
4. Deliver as a single `.html` file (or artifact if in that context).

## Technical Stack

```html
<!-- Three.js for 3D background -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/three.js/r128/three.min.js"></script>
<!-- GSAP for scroll animations -->
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/gsap.min.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/gsap/3.12.2/ScrollTrigger.min.js"></script>
```

Use CSS `perspective`, `transform-style: preserve-3d`, `translateZ()` for layered depth. Animate with `gsap.to()` triggered by ScrollTrigger.

## Quality Bar

The result must feel like a $5,000–$10,000 agency deliverable:
- Smooth 60fps scroll
- No layout breaks on mobile (responsive)
- Every section has a "wow" moment
- Brand identity is unmistakable throughout
