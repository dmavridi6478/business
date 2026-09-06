---
description: Convert a process into a reusable SOP with inputs, steps, checks, and outputs
argument-hint: [process or task to document]
---

Convert the process or task described in "$ARGUMENTS" into a standard operating procedure (SOP) structured for someone doing it for the first time:

**INPUTS** — what is needed before starting (data, access, prerequisites, tools)
**STEPS** — numbered sequence of actions; each step says who does what, with enough specificity that someone could follow it without asking
**QUALITY CHECKS** — what to verify at key points to confirm the step was done correctly before moving on
**OUTPUTS** — what a completed run produces and where it goes
**WHEN TO ESCALATE** — the conditions that mean something is wrong and shouldn't proceed

Write it for repeatability, not just description. If a step is ambiguous or varies by situation, name the variation and say how to handle each case. Flag any step that is currently manual but could realistically be automated.

If "$ARGUMENTS" is empty, ask what process to turn into an SOP before proceeding.

Source: @theusefulshift "20 Claude Commands That Feel Illegal" — Command 09 (sop).
