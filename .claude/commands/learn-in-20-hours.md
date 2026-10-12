---
description: Run the 6-prompt learning sequence (ladder, resources, 20-hour plan, cheat sheet, quiz, Feynman) on a topic
argument-hint: <topic> [hours per week]
---
Use the skill `claude-learn-100x-6-prompts`.

Topic and time: $ARGUMENTS

1. Ask me my current level and goal in one question.
2. Do prompt 4 (learning ladder), then prompt 5 (resources) and mark every resource you cannot be sure exists as "verify".
3. Do prompt 1 (20-hour plan in 10 sessions) using the resources.
4. Stop and ask me to start session 1. After each session I will ask for prompt 2 (cheat sheet), 3 (quiz) or 6 (Feynman).
5. Tag claims [Certain], [Likely] or [Guessing].
