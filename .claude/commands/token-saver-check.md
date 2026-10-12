---
description: Vet a Claude Code token-saving tool before installing it (what it changes, what it sees, how to test it)
argument-hint: <tool name or repo URL>
---

Use skill `token-saver-repos-top5`. Evaluate "$ARGUMENTS" from its README and source only. Answer: what it changes in my prompts or tool results; what it sends to third parties and whether it sits in the network path; how compression could drop a needed detail; whether it breaks prompt caching; one known-answer test I can run on a throwaway repo; and a verdict: adopt, trial, or skip. Quote the slide or README claim and mark it unverified. Install nothing.
