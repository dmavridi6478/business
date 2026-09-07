---
description: Turn "build me a portfolio" into a real Claude Code brief — purpose, content, design, stack, function, constraints (@futurewithai.dev)
argument-hint: [who the site is for] [what you do]
---

"Build me a portfolio" is not a good prompt. Before writing any code, fill in this 6-part brief with the user — ask for whichever fields aren't given in "$ARGUMENTS" rather than inventing them — then hand the completed brief to Claude Code as the actual build instruction.

## The 6 fields

1. **Purpose** — who is the site for? (recruiters, clients, collaborators — be specific)
2. **Content** — what should appear? (sections, real projects/experience — never invent achievements, metrics, or employers not supplied)
3. **Design** — what should it feel like? (don't just say "modern" — define the actual visual system: typography, spacing, color, grid, borders, motion)
4. **Stack** — what should it use? (framework, styling, minimal dependencies, responsive, production-ready)
5. **Function** — what needs to work? (forms, auth, CMS, payments — only what's actually needed; more tools ≠ better website)
6. **Constraints** — what should it avoid? (generic AI gradients, excessive glassmorphism, random floating cards, huge rounded containers, stock illustrations, unnecessary animations — aim for no AI-slop design)

## Template to fill in and hand to Claude Code

```
• Purpose: [who is it for]
• Content: [what to include]
• Design: [look & feel]
• Stack: [tech to use]
• Function: [what to build]
• Constraints: [what to avoid]
```

## Worked example

```
• PURPOSE
  Build a modern personal portfolio for a Computer Engineering and
  Mathematics student interested in AI, software and hardware.

• GOAL
  The site should quickly show who I am, what I build, and make it
  easy for recruiters or collaborators to explore my work.

• SECTIONS
  Create Hero, About, Experience, Projects, Skills and Contact
  sections.

• TECH
  Use Next.js, TypeScript and Tailwind. Keep MINIMAL DEPENDENCIES.
  Make it RESPONSIVE and production-ready.

• DESIGN
  Minimal, technical and premium. Strong typography, whitespace,
  STRONG TYPOGRAPHY, RESTRAINED MOTION and clear hierarchy.

• AVOID
  Generic AI gradients, excessive glassmorphism, random floating
  cards, huge rounded containers, stock illustrations and
  unnecessary animations. Aim for NO AI-SLOP DESIGN.
```

## After the first build

Don't accept version 1. Run this loop before calling it done:

```
Launch it locally. Inspect desktop and mobile. Find visual or
functional problems. Fix them before showing me the final result.
```

Check specifically for: spacing, overflow, typography, mobile
responsiveness, interactions, hierarchy, and generic-looking
("templated") sections. If real materials exist (resume, headshot,
project descriptions, logo, bio), feed them to Claude Code and instruct
it to replace every placeholder using only the supplied materials — do
not invent projects, employers, metrics, or accomplishments.
