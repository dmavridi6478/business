---
description: Explain one of the six ML algorithms through its key line, or run the checked numpy script that makes all six work
argument-hint: [linear | tree | forest | boosting | kmeans | network | run]
---

Use the skill `ml-six-key-lines`. Input: "$ARGUMENTS".

1. Read `.claude/skills/ml-six-key-lines/SKILL.md`.
2. For a named algorithm, explain its line in plain words, show the matching section of `scripts/ml_six_key_lines.py`, and state the caveat the video leaves out.
3. For `run`, execute `python3 scripts/ml_six_key_lines.py` (numpy required; if missing, say so and give `pip install numpy` for the user to run), and report the printed results as they are.
4. Do not claim the toy accuracy figures describe real-world performance.
