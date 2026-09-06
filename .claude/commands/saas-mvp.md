Run the `saas-mvp-24h` skill to guide a 4-phase build from idea to live SaaS product.

If "$ARGUMENTS" contains a product idea or description, use it as the starting context for Phase 1. If no arguments are provided, ask the user for their product idea and target user before proceeding.

Steps:
1. First, invoke the `saas-idea-validator` skill on the stated idea. If it surfaces a critical flaw (no real problem, no identifiable customer, existing dominant incumbent with no moat), surface the finding and ask whether to proceed anyway — don't auto-abort, but don't proceed silently.
2. If the idea passes (or the user chooses to proceed), run all 4 phases of `saas-mvp-24h` in sequence: Plan → Design → Build → Deploy+Distribute.
3. At each phase transition, output the deliverable for that phase (scope doc, design brief, build order, launch checklist) before moving to the next. Don't skip to code without a written plan.
4. Surface the copy-paste prompts for Claude, Cursor, and post-launch distribution from the skill at the appropriate phase — the user should be able to take the output of each phase and use it directly in the relevant tool.
