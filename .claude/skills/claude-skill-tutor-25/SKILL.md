---
name: claude-skill-tutor-25
description: 'A set of 22 learn-any-skill prompts for Claude (30-day roadmap, teach me like a beginner, skill-level quiz, tutor mode, 80/20 curriculum, teach-it-back, 30-day challenge, expert interview, flashcards, 7-day crash course, 30-minute daily plan, strict coach mode) plus a recommended order. Use when the user wants to learn a skill, build a study plan, or be tutored by Claude. Source: "25 Claude Skill Tutorial Prompts" infographic (@wayaai.feeds).'
---

# Learn any skill with Claude - prompt set

The infographic is titled "25 prompts" but items 1, 24 and 25 are intro and closing text, so **22 usable prompts** exist. Several are cut off with "..." in the image; those are marked **(completed)** - the first words are the source's, the rest is mine.

| # | Name | Prompt |
|---|---|---|
| 2 | 30-day roadmap | Act as a world-class teacher. Create a 30-day roadmap to master [SKILL]. |
| 3 | Teach like a beginner | Teach me [TOPIC] as if I'm a complete beginner... **(completed)** ...Use plain words, one idea at a time, and check my understanding before moving on. |
| 4 | Skill-level analysis | Analyze my current skill level in [TOPIC]. Ask me 10 questions... **(completed)** ...one at a time, then tell me my level and the 3 gaps to close first. |
| 5 | Turn into a framework | Turn this topic into a step-by-step framework I can remember forever. |
| 6 | Ask before you proceed | Act as my private tutor. After every explanation, ask me a question... **(completed)** ...and do not continue until I answer. |
| 7 | Top 20 book lessons | Summarize the most important lessons from the top 20 books about [TOPIC]. (Verify the book list exists; models can invent titles.) |
| 8 | 80/20 curriculum | Create a beginner-to-advanced curriculum using the Pareto Principle. |
| 9 | Teach it back | Explain this concept, then ask me to teach it back to you. Evaluate me. |
| 10 | Visual mental model | Turn this complex topic into a visual mental model with analogies... **(completed)** ...and a simple diagram I can redraw from memory. |
| 11 | 30-day challenge | Create a practice challenge that gets progressively harder every day. |
| 12 | Expert interview | Act as an expert in [FIELD]. Interview me and help me think like a professional. |
| 13 | Beginner mistakes | What mistakes do beginners make when learning [SKILL]? Create a guide. |
| 14 | 50 real-world scenarios | Generate 50 real-world scenarios where I can apply this skill immediately. |
| 15 | Weekly review system | Design a weekly review system to track my progress and identify weaknesses. |
| 16 | Flashcards and quizzes | Create flashcards, quizzes, and memory techniques for this topic. |
| 17 | Real-world project | Simulate a real-world project that tests my understanding so far. |
| 18 | 7-day crash course | If I had only 7 days to learn this skill, what would you teach me? |
| 19 | Challenge assumptions | Challenge my assumptions about this topic and present opposing viewpoints. |
| 20 | Expert habits | Analyze experts in this field and extract the common habits that make them successful. |
| 21 | 30-minute daily plan | Create a learning schedule that fits into 30 minutes per day. |
| 22 | Stories and analogies | Transform this lesson into stories, analogies, and memorable examples. |
| 23 | Strict coach mode | Act as a strict coach. Hold me accountable and create consequences for missing goals. |

## Recommended order (my sequencing, not the source's)
Diagnose (4) -> roadmap (2, 8, 21) -> learn with checks (3, 6, 9, 16) -> apply (14, 17, 11) -> review (15, 19) -> accountability (23).

## Rules
- Ask the user for [SKILL], their level, hours per week and a deadline before starting. Never assume them.
- Claude cannot watch practice. Anything it grades (9, 17) is a self-report check; for physical or regulated skills use a human teacher.
- Prompt 23 "consequences" must be chosen by the user; do not impose any.

Command: `/learn-skill`. Agent: `learning-coach`.

## Keywords
learning plan, study, tutor, roadmap, flashcards, coaching, skill acquisition
