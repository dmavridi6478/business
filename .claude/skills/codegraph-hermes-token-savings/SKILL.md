---
name: codegraph-hermes-token-savings
description: The @aiclawbots slides claiming the free CodeGraph tool cuts Hermes agent token usage by almost 70 percent, with the mechanism (a code knowledge graph the agent navigates), the illustrative numbers on the slides, why they are unproven, and a three-run test to measure your own saving.
---

# CodeGraph and Hermes token usage (@aiclawbots)

Source: nine slides in the upload ("This free tool can cut your Hermes token usage by almost 70%", "Comment HERMES and I'll send it to you for free"). The charts are labelled **"Illustrative"** on the slides themselves.

## The argument
1. On a large codebase, every new Hermes session may re-read the code to understand it. Slide figure: 52.4k tokens per session, three sessions = 157k, before a real question is asked.
2. Slide figure for context used before the first question: files 18.2k, functions 12.6k, dependencies 9.1k, relationships 7.4k = 47.3k tokens. Cost grows with codebase size (small, medium, large).
3. CodeGraph reads the code once and stores files, functions and their relationships as a knowledge graph. The agent follows the graph and pulls only what the task needs (example: "Fix the login bug" loads login.ts, validateUser() and getUser(), not 2,307 other files).
4. Slide result: 52.4k down to 15.7k tokens per session, "reductions close to 70% in some workflows". The slide wording is "CodeGraph claiming", so it is the tool's own claim.

## What is and is not known
- [Certain] The numbers on the slides are illustrations, not measurements.
- [Likely] The tool referred to is a code-indexing MCP such as `colbymchenry/codegraph` (MIT), already described in `dev-repos-to-clone`; the slides do not give the repo, so this is an inference.
- [Guessing] That the saving holds for your codebase. It depends on language, repo size and how your agent searches.
- "Comment HERMES for the free guide" is a lead magnet. Nothing was commented or requested.

## Measure it yourself (three runs each)
1. Pick one task you repeat, for example "explain how login works and add rate limiting".
2. Run it three times in fresh sessions without the index and record input and output tokens each time.
3. Index the repo, run the same task three times in fresh sessions, and record the same figures.
4. Compare medians, and also check answer quality: a smaller context that misses a file is not a saving.
5. Read the installer before running it; the codegraph README installs with a `curl | sh` line.
