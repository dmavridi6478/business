---
name: earchoe-idea-validation
description: The @earchoe "AI Product Validation Before You Build" workflow - Context -> Structure -> Check, the inputs to write down first, two copy-ready prompts (10 assumptions labelled by impact and uncertainty; 5 cheap validation tests with what to measure), the human-check rule and the save-the-validation-map routine. Use before building a product, feature or offer, to expose assumptions and design tests, not to "prove demand".
---

# AI product validation before you build (9-slide carousel, series 08)
Core claim: AI cannot prove demand. It can expose assumptions, define tests and organise evidence. Do not start with a clever prompt; start with the outcome, the inputs and the quality check.

## Inputs (slide 3)
Write down: the problem, target user, proposed solution, alternative solutions, and what you currently believe.

## Prompt 01 - build the first pass
```
Act as a skeptical product researcher. For [IDEA], identify the 10 assumptions that must be true for this to work. Label each by impact and uncertainty.
```
## Prompt 02 - turn it into a deliverable
```
Turn the highest-risk assumptions into 5 cheap validation tests. For each test, state what I should measure and what result would increase or decrease confidence.
```
Each: replace every [BRACKET], attach the source or context, read the output before using it.

## Rules
- Do not ask whether the idea is "good". Ask which assumptions are dangerous and what evidence could test them. AI accelerates; you own the decision, the facts and the final output.
- Loop: idea -> assumptions -> tests -> evidence -> next decision. Then A find assumptions, B design tests, C review evidence, D repeat.
- Save the map: keep the original input, the prompt that worked, your own quality check before acting, and turn the finished workflow into a reusable template.

Related: `pressure-test-idea`, `saas-idea-validator`, `assumptions-and-gaps`. Run with `/validate-idea`.
