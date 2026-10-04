---
description: Check an AI system against the 15 governance and trust concepts and the five-stage lifecycle, with evidence seen, claimed or missing for each
argument-hint: [the AI system or program to check] [lifecycle stage it is in]
---

Use the skill `ai-governance-15-concepts`. Input: "$ARGUMENTS".

1. Read `.claude/skills/ai-governance-15-concepts/SKILL.md`. Use `/ai-governance` for the six-layer audit; this command is the completeness check.
2. Ask at most 4 questions about the system if the input is thin. Never ask for credentials or personal data.
3. Score each of the 15 concepts: evidence seen / claimed only / missing, quoting the evidence asked for in the skill.
4. List the missing items by lifecycle stage (Design, Build, Deploy, Operate, Evolve) and name the three to fix first.
5. State that the 15 concepts are a list, not a compliance standard, and that no legal conclusion follows from a full score.
