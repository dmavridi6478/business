---
name: advisor-room-debate
description: A three-round advisor debate for one business decision (independent opinions, challenge, reconsider and vote) with role lenses instead of impersonating real people, a decision brief template, a scored verdict and dissent record, plus a review of the roast-room repository behind a "room of billionaire advisors" carousel (seats, setup, licence, age, cost) and the limits of simulated debate. Use before a big business decision when you want your lean tested rather than agreed with.
---

# The advisor room: three rounds, one verdict

Source: a ten-step TikTok-style carousel from usamaakrm, "How to turn Claude into a room of billionaire advisors" (Batch 125), built on the repository `nateherkai/roast-room`. Steps 1 to 7, 9 and 10 were in the images; step 8 was not.

## What the repository is (read on GitHub, 31 October 2026)
- "Seven AI advisors debate your business decision in Claude Code, live around a table", plus five more on call: a Chair recommends who sits on the council and you confirm. Each is "built from that person's public work".
- Default seats: Bezos (strategy and decisions), Paul Graham (product and startups), Alex Hormozi (offers, pricing, sales), Gary Vaynerchuk (marketing and attention), Dan Martell (people, hiring, founder time), Gino Wickman (operations and scaling), Warren Buffett (money and capital). On call: Naval Ravikant, Codie Sanchez, Leila Hormozi, Sara Blakely, Elon Musk. `/newroaster <name>` builds another.
- Needs Claude Code and Node.js 20 or newer. `git clone https://github.com/nateherkai/roast-room.git`, `cd roast-room`, `npm start`, open `http://localhost:4730`, run `claude` in the same folder, then `/roast-room <decision>`. Flags: `--quick` (four advisors, two rounds, uses far less of your plan), `--seats a,b`, `ask <seat> ...`. A scored verdict and PDF come out; the report lands in `sessions/`.
- **Figures:** 1,271 stars, 292 forks, 10 open issues, created 10 October 2026, one contributor with 9 commits, licence shown as "Other". Read the licence file before reuse.

## The carousel's ten steps, in my words
1 Open Claude. 2 Clone the repository and enter its folder. 3 Start the room (`npm start`) and open the local address. 4 Open Claude Code in the same folder. 5 Ask a real business question with your decision, options, budget, revenue, team size, deadline and goal. 6 Let Claude pick the advisors. 7 Watch the debate: round 1 each gives an opinion; round 2 they challenge each other's assumptions, risks and trade-offs; round 3 they reconsider and vote. 9 Add an expert with `/newroaster <name>`. 10 Use it before big decisions (pricing, hiring, new ideas, offers, marketing, investments, products, partnerships) and do not blindly follow the verdict; verify important facts.

## Disagreements, stated plainly
**I disagree with "billionaire advisors".** It is one model playing seven parts. The risk is false independence: the seats share the same blind spots, drift toward the same answer and flatter your lean. Treat the output as a structured set of arguments, not as seven opinions. The repository itself says it tests your lean rather than agreeing with it, which is the right design; check that it does.
**I disagree with putting real people's names on the output.** It is a simulation built from public work. It is not what those people think. Do not quote "Buffett says" or publish verdicts under their names; the carousel's own fine print says "simulated perspectives, not the real people or their endorsement". Use role lenses in your notes (money lens, strategy lens).
**The risk in running it:** you execute third-party code (a small Node web app) and send your numbers to the model provider through Claude Code. Read `package.json` and the commands before `npm start`, and do not paste data you cannot share.

## A tool-free version (what `/advisor-room` runs)
**Brief:** decision in one line; two or three options (including "do nothing"); numbers; limits; success measure and date; which way you lean and why (the council must test it).
**Lenses (pick four to seven):** strategy and reversibility; product and demand; offer, price and sales; marketing and attention; people and founder time; operations; money, cash and risk; leverage and ownership; buy versus build; leadership; brand; first-principles speed.
**Round 1, independent opinions:** each lens answers alone without seeing the others, in one paragraph with its recommendation and its confidence.
**Round 2, challenge:** each lens attacks the others' assumptions, risks and trade-offs; list claims that need a fact.
**Round 3, reconsider and vote:** each lens updates or holds, with a one-line reason and a vote (yes, maybe, no).
**Verdict:** a scored recommendation, the strongest dissent, the three facts to verify, a reversible first step and a date to review.

## When not to use it
Medical, legal or tax decisions; decisions about named individuals (hiring or firing someone); anything where the numbers are made up; irreversible commitments without checking facts. For those use a professional.

Overlap in this library: `advisory-board`, `multi-agent-debate`, `marketing-council`, `council`, `council-multi-model`, `agentic-council:*`, `16-minds:*`, `decision-partner`, `pressure-test-options`, `steelman-both-sides`, `premortem`. This skill is the three-round protocol plus the roast-room review.

Run with `/advisor-room <decision and options>`.
