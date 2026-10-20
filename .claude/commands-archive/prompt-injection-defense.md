# Prompt Injection Defense — Boundary Rules for Agents

Source: @qbuilder (TikTok), a 6-slide security-awareness carousel on prompt
injection in agentic AI. This is a procedure, not a prompt list — use it as
a pre-flight checklist whenever building or reviewing an agent that reads
external content (web pages, emails, files, tool outputs) and can also take
actions (send, delete, spend, install).

## The core problem

> The model can't tell your orders from what it reads.

Inside a model's working memory there is no colored text — nothing marks
which words came from you and which came from a random web page, email, or
file. Your instruction and a stranger's instruction "look exactly the same
from the inside." A page can carry text you never see (`color: white`,
`font-size: 0`, `display: none`, hidden `alt="..."` text) — your agent reads
all of it anyway.

**Why it matters more now than a year ago:** the same trick that used to end
in a chatbot saying something silly can now end in something actually
happening, because agents have hands — email, files, terminals. "Reading
leads to action now."

## The 3 rules ("the rules of my house")

1. **Never mix the open internet and sensitive access in the same session.**
   If an agent is browsing, it isn't holding your keys. Split browsing tasks
   and credentialed/sensitive tasks into separate sessions or separate
   agents.
2. **Anything that sends, deletes, or spends comes to a human first.**
   No agent auto-approves its own irreversible or costly actions — a human
   is always the yes.
3. **Whatever the agent brings back from the internet, a human reads it
   before it becomes real** — before it's forwarded, before it's acted on,
   before it's trusted as a citation or a fact.

**The whole trick:** none of this makes the model smarter. It only decides
what the model is allowed to read, and what it's allowed to do.

## Pre-flight checklist for a new agent build

- [ ] Does this agent read content it didn't author (web pages, emails,
      files, tool output)? If yes, treat everything it reads as untrusted
      data, never as instructions — regardless of how it's phrased.
- [ ] Does this agent also have the ability to send, delete, spend, or
      execute? If yes, rule 1 applies — don't let read-untrusted-content and
      take-irreversible-action sit in the same unsupervised loop.
- [ ] Is there a human approval gate before anything irreversible fires?
      If no, add one before shipping.
- [ ] Is there a review step before the agent's findings get forwarded,
      published, or acted on as fact?
- [ ] Have you told the agent explicitly (in its system prompt / skill
      file) that content it reads is data, not instructions? Most
      injection failures come from this never being said at all.

## How this applies inside this repo

This exact untrusted-vs-instruction distinction is already the governing
rule for how this session (and any Claude Code session) treats fetched web
content, PR comments, and other external sources — see the standing
system-prompt guidance on treating fetched content as data, not commands.
Cross-referenced from `ai-governance-layers` (which covers organizational
AI governance more broadly) and `claude-code-tooling` (which covers agent
sandboxing/trust patterns) — this file is the tactical version: the
3-rule checklist to run before any new agent build that touches both
external content and real-world actions.
