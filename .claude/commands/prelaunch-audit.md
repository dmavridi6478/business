---
description: Audit a website before launch against the 20-point list: run the mechanical script first, then a model pass on what it could not decide
argument-hint: [paste of page HTML, or a file path, plus any Lighthouse report]
---

Use the skill `prelaunch-website-audit-20`. Input: "$ARGUMENTS".

1. Read `.claude/skills/prelaunch-website-audit-20/SKILL.md`.
2. If the input is a file path, run `python3 -I scripts/prelaunch_check.py <path>` first and keep its output. If the input is pasted code, save it to a scratch file outside this repo and run the script on that.
3. For every check the script marked CAN'T CHECK, decide it only if the pasted material allows it; otherwise keep CAN'T CHECK and say exactly what to paste or run (Lighthouse, `curl -I`, a crawl).
4. Output the 20 lines as PASS, FAIL or CAN'T CHECK, one line why, and the exact fix. Never guess.
5. End with the 5 fixes to do first. If a secret was found, say to rotate it and never repeat it in the output.
