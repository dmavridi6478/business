---
name: apple-design-audit
description: Reconstruction of the "Apple's design secrets for Claude" workflow from an @alex.carterr_ video (frames only, audio not read) - paste a website URL and ask Claude (Opus, high effort) to audit its design against Apple's design principles, then have it implement fixes and compare with a screenshot. The exact prompt on screen was cut off, so the prompt below is a reconstruction, not a quote. Use for design reviews via /apple-design-audit.
---

What the frames show: a Claude chat with `www.fitpass.com Audit this website's design using Apple...` (cut off), model Opus 5 / High; slides about Apple's Creator Studio, animation, "move it"; a result deck "Product Team Standup"; a Bash `npm run build` step with a successful build and 26 warnings; "design a modern app".
**Reconstructed prompt (verify and adapt; Apple's Human Interface Guidelines are public at developer.apple.com/design):**
```
[URL]. Audit this website's design using Apple's Human Interface Guidelines principles: clarity, deference, depth, hierarchy, consistency, typography, spacing, colour and contrast, motion and feedback, accessibility. For each principle give: what works, what breaks, evidence (element or screenshot), severity, and a concrete fix. Then list the 5 changes with the highest impact. Do not edit anything yet.
```
Follow-up pattern (from `claude-code-prompt-rewrites-5`): implement the top fixes, screenshot the result, compare with the original, list differences, fix them. Related: `design-review-audit`, `better-ui`, `accessibility-compliance`.
