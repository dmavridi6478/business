# Tests for the 50 b2b-sales skills

Two layers, both repeatable.

1. **Structure** (`python3 -I scripts/check_b2b_sales_skills.py`): frontmatter, section order, step counts, numbering 1 to 50, stage counts 7/8/7/7/6/8/7, cross-references.
2. **Behaviour** (`scripts/check_b2b_sales_outputs.py`): each skill is run by Claude on a fictional deal pack (`fixtures/`), one case per skill plus six negative cases (`cases.json`), writing `results/<id>.md`. The script then checks, without an LLM: the skill's output headings in order; that no number appears that is not in the inputs, small, a year or a plan duration, unless tagged `[calc]` or `[assumption]`; that quotes are exact excerpts (cases flagged `quotes`); the draft label (cases flagged `draft`); and the expected pattern in negative cases.

How to run a case: give a fresh Claude the skill's `SKILL.md`, `b2b-sales-standard`, the case's input files and its `request`, and ask it to write the output to `results/<id>.md`. Do not give it the checker.

What this does not prove: that the advice would win a deal. The fixtures are fictional and one scenario; a script cannot judge quality; the number check allows plan durations; an LLM wrote the outputs under test, so a pass shows the skill's rules are followable, not that they are sufficient. Cases marked "manual review" also need a human read.
