# Batch 113 prompts (plain text; replace [brackets])

## 1. Customer personas from evidence (`/persona-from-evidence`) - @earchoe
Prompt 01: Analyse these customer statements [TEXT]. Cluster recurring needs, frustrations, desired outcomes, objections and buying triggers. Quote only short phrases that are actually present.
Prompt 02: Create 3 evidence-based customer profiles from the clusters. For each, show the evidence behind the profile and clearly mark anything that remains uncertain.
(Remove personal data you do not need before pasting. Keep "observed" and "inferred" separate.)

## 2. Five Claude Code prompt rewrites (`/sharpen-prompt`) - @awayfromlovable
1. [paste screenshot] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them
2. users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it
3. the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don't suppress the error
4. write a validateEmail function. example test cases: user@example.com is true, invalid is false, user@.com is false. run the tests after implementing
5. write a test for foo.py covering the edge case where the user is logged out. avoid mocks.

## 3. Build an agent in claude.ai without code - @oxana__ray
I want to build an AI agent. Ask me the right questions one by one to set it up. I'm new to this, so keep it simple and beginner-friendly.
Test prompt: Search for the latest AI news and give me a 3-point summary.

## 4. Reflective prompts 13-17 (`/life-prompt 13` ...) - @betterpromptsai (1-12 are in docs/batch-112-prompts.md)
13. I want to tap into my antifragile nature. Teach me how to use the power of chaos to forge mental resilience.
14. You are a social energy specialist. Design my complete social energy management system: which people drain me, which energize, how to recharge after draining interactions, and the optimal social diet for maintaining peak social energy.
15. You are an impromptu speaking specialist. Design the complete mental framework for speaking brilliantly on any topic without preparation: how to access deep knowledge, how to structure on the fly, and the confidence technique to never freeze.
16. Develop a nighttime productivity routine for a night owl writer, assuming a 2 am - 5 am work block, to maximize creative output while minimizing the risks of burnout.
17. (safer rewrite; the original asked for sensory deprivation and cold exposure) I want to build [skill/trait]. Using established learning science (spaced practice, deliberate practice, sleep, feedback), design a 7-day practice plan with daily 30-minute sessions. Do not include cold exposure or sensory deprivation. Note what is well supported by evidence and what is speculative.

## 5. Claude Code setup audit (`/ecosystem-audit`)
Audit this repository's Claude Code setup against four layers: memory (CLAUDE.md, rules), skills, subagents, hooks and permissions, MCP and plugins, automation. Return a table of layer, finding, severity and fix. Read only; make no changes.

## 6. Connector (run yourself, only after reading the vendor's terms; NOT added to .mcp.json)
claude mcp add --transport http Glasser https://api.glasser.ai/mcp   then /mcp -> Glasser -> Authenticate. Set a small balance cap first. See skill glasser-data-sources.
