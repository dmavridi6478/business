---
name: llm-council-5-advisors
description: LLM council: five advisors with different thinking styles (Contrarian, First Principles, Expansionist, Outsider, Executor) debate one question and return a verdict, so Claude does not just agree with your framing. Source: @aiemergence.
---

# The LLM council (@aiemergence)
Flow: **Question -> Debate -> Verdict.** Different roles surface different trade-offs before you commit.
| # | Advisor | Job |
|---|---|---|
| 1 | The Contrarian | Finds what will fail |
| 2 | The First Principles Thinker | Starts from the facts |
| 3 | The Expansionist | Finds what else is possible |
| 4 | The Outsider | Sees what you missed |
| 5 | The Executor | Turns it into a plan |

**The problem it fixes:** same model, different framing. "Should I launch this?" gets 5 reasons to ship; "Is this a bad idea?" gets 5 reasons to stop. Your framing controls the output, so ask the council neutrally.
**Worked example from the card:** "Should I build a $297 Claude Code course for beginners?" Outsider: you may be selling to people who need a smaller first win. Executor: test the offer with a small cohort before building. Verdict: test a small cohort before building the $297 course (smaller test, better evidence, lower risk).

**Run it:** state the decision neutrally with the real constraints; have each advisor answer in turn in 3-5 lines without seeing the others' conclusions; then a final pass that names agreements, the strongest disagreement, and one verdict with the cheapest next test. Use `/advisors`. For multi-model or agent-based variants see `council`, `council-multi-model`, `multi-agent-debate`. The author's full setup was offered via a comment keyword; it is not reproduced here.
