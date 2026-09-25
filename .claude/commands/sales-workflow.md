---
description: Get a build sheet for one workflow from the 100-item sales-workflow-catalog, or list a stage's 10 workflows
argument-hint: [number 1-100, or workflow name, or a stage name] [platform: n8n | make]
---

Use the `sales-workflow-catalog` skill. Request: "$ARGUMENTS"

1. If blank, show the 10 stages and the build-order recommendation, and ask which workflow.
2. If a stage name is given, list its 10 workflows with the one-line job and ask which to build.
3. Look up the workflow by number or name. If it doesn't match one of the 100, say so — don't invent a workflow.
4. Produce a build sheet:
   - **Fit check**: one line — is this actually the highest-leverage thing to automate right now, given the skill's build-order.
   - **Tags**: note if it's marked **[data]** (needs a real export — ask for it, never invent) or **[send]** (needs a human-approval gate).
   - **Node map**: numbered table — # | node | platform module | input | output | error handling — expanding the skill's node sketch.
   - **Credentials**: every account/API key needed.
   - **Prompt** (if an LLM step is involved): a ready system prompt, grounded in real data only.
   - **Test plan**: a 5-record dry run before any live trigger.
   - **Hands off to**: the next workflow in sequence, if any.
5. If platform is Make, translate node names to Make modules; default to n8n.
