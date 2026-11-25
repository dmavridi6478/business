---
name: youtube-to-learning-app
description: Turn any YouTube video or playlist into an interactive learning app in 5 steps (Cyberman AI) - source in YouTube, drop into NotebookLM, connect the notebook to Gemini, run the learning-app prompt, save the generated HTML as learning-app.html. Includes the exact prompt and a ready HTML shell template. Use when someone wants to study a talk, tutorial or lecture series as a quiz-and-progress app rather than a summary.
---

# Turn YouTube videos into a learning app

Source: infographic "Turn YouTube videos into learning app" from Cyberman AI. Different from `youtube-to-skill` (video to Claude skill) and `notebooklm-skill`.

1. Pick your source: any YouTube video or playlist (conference talks, deep-dive tutorials, lecture series).
2. Drop it into NotebookLM: paste the link as a source; NotebookLM grabs the transcript.
3. Connect it to Gemini: in Gemini choose + then more uploads, select your notebook.
4. Run this prompt:
```
Turn the attached notebook into an interactive learning app for [topic].
- explain concepts in plain English
- let me ask questions anytime
- break ideas into small steps
- quiz me after each section
- give real examples and use cases
- summarize what I've covered
- track what I've learned so far
```
5. Save and run: Gemini generates the full HTML in Canvas. Copy it, save as `learning-app.html`, open it in your browser.

## Claude alternative

If you prefer to stay in Claude: paste the transcript, then use `/youtube-learning-app [topic]`, which prints the prompt above adapted for Claude and tells it to fill `Artifacts/templates/learning-app-shell.html` (sections, quizzes, progress saved in the browser).

## Cautions

- "Ask questions anytime" needs a live model; a saved HTML file can only answer from what was baked in. The shell template includes a notes box instead of a fake chat.
- Check the generated quizzes against the video; models invent plausible wrong answers.
- Only use videos you may study; do not republish transcripts.
