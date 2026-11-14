---
description: Turn a YouTube video or transcript into an interactive learning app (sections, quizzes, progress) using the learning-app HTML shell, or print the 5-step NotebookLM and Gemini route
argument-hint: [topic] [youtube url or pasted transcript]
---

Use the skill `youtube-to-learning-app`. Input: "$ARGUMENTS".

1. Read `.claude/skills/youtube-to-learning-app/SKILL.md`.
2. If the user wants the Gemini route, print the 5 steps and the prompt exactly.
3. Otherwise get the transcript (ask the user to paste it if it cannot be fetched), split it into 4 to 8 sections of small steps, and write 2 to 3 quiz questions per section with the correct answer and a one-line reason.
4. Copy `Artifacts/templates/learning-app-shell.html`, replace the `COURSE` object with the real content, save as `learning-app.html`, and say which claims came from the transcript and which are your additions.
