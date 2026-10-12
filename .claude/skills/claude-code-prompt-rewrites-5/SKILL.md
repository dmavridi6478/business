---
name: claude-code-prompt-rewrites-5
description: Five before/after Claude Code prompt rewrites from an @awayfromlovable carousel ("rewritten by Anthropic", from Anthropic's own best-practices guide) - show it then check it (screenshot compare), describe the symptom (file, flow, failing test), fix the cause not the symptom, give it a test to pass, scope the task. Use when a coding prompt is vague, to sharpen it before sending, via /sharpen-prompt.
---

| # | You write | Better prompt | Principle |
|---|---|---|---|
| 1 | make the dashboard look better | [paste screenshot] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them | give it something to look at and a way to check itself |
| 2 | fix the login bug | users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it | describe the symptom, point at the place, ask for a reproducing test |
| 3 | the build is failing | the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don't suppress the error | paste the real error; forbid suppressing it |
| 4 | implement a function that validates email addresses | write a validateEmail function. example test cases: user@example.com is true, invalid is false, user@.com is false. run the tests after implementing | give it a test to pass and run it |
| 5 | add tests for foo.py | write a test for foo.py covering the edge case where the user is logged out. avoid mocks. | scope the task: one case, one constraint |
Pattern: say what is wrong, where to look, how to verify success, and what not to do. Use `/sharpen-prompt <your prompt>`.
