---
description: Spec a small single-purpose web app with the MVP spec prompt, then produce the milestone build plan, with the four-question check
argument-hint: [user type] [problem] [input] [output]
---

Use the skill `micro-app-prompts-earchoe`. Input: "$ARGUMENTS".

1. Read `.claude/skills/micro-app-prompts-earchoe/SKILL.md`. If user type, problem, input or output is missing, ask for it in one short question instead of guessing.
2. Run Prompt 1 with the user's values: design the smallest useful version and list screens, user flow, data needed, validation rules, error states and success state. Add nothing the core workflow does not need.
3. Run Prompt 2: turn the spec into a build plan in small milestones, test the core workflow after each, keep the UI simple, mobile-friendly and accessible, and say what to test after each step. Name the builder the user will use.
4. Finish with the second-pass check: what was assumed, what is missing, an attack on the plan's own claims, and which facts, figures and prices need human verification.
5. Flag any personal data the app would collect. Do not build or deploy anything unless the user asks.
