# How to Build Your First Claude Agent (3-Level Guide)

Source: @usamaakrm (TikTok), a 3-part "Save skill → Autopilot → Run in the
cloud" carousel series. This is a genuine build-an-agent guide, reproduced
in full below with the exact commands.

## Level 1 of 3 — Save Your First Claude Skill
*Turn one boring weekly task into a permanent system.*

1. **Describe it once.** Claude writes the entire skill for you.
2. **Save it as `skill.md`.**
3. **Connect your tools.** Notion, Gmail, Drive.
4. **Test it. Fix it. Save it.** (run → fix → save loop)
5. **Trigger it from any chat.** e.g. `/reel`
6. **Input goes in. Finished work comes out.**
7. Create a skill once. Use it forever.

## Level 2 of 3 — Put Your Skill on Autopilot
*Run your skill on a timer. Let Claude handle the work.*

1. Your skill already works. Now give it a schedule.
2. Tell Cowork in plain English: *"Run my skill every Monday at 9 AM."*
3. Cowork asks a few questions: Which day? Which files? Done.
5. Same `skill.md` — no rebuilding, no rewriting.
6. Every week, it runs automatically.
7. Your results are waiting for review when you wake up.
8. One skill. Infinite repeats.

## Level 3 of 3 — Run It in the Cloud
*AI agent workflow: Input/Trigger → AI Agent → Tools & APIs → Process → Output/Delivered.*

1. Your skill works. Your schedule works. Now remove your laptop.
2. **Install Claude Code once:**
   ```bash
   npm install -g @anthropic-ai/claude-code
   ```
3. Drop in the same skill. No changes. No rewrites.
4. Tell it: *"Run my skill every morning at 7 AM."*
5. Claude Code handles the rest — APIs, files, agents.
6. Close your laptop. The work keeps moving.
7. Manage everything from your browser.

---

## Try it now

This exact 3-level path is directly executable in this environment. To
build your own first skill right now:

```
Help me turn [describe your repeating weekly task] into a Claude skill.
Interview me the way /skill-creator does, then write the skill.md file,
tell me which tools it needs connecting (Notion/Gmail/Drive/etc.), and
give me the exact trigger phrase to run it from a fresh chat.
```

For the scheduling step (Level 2/3, "run every Monday at 9 AM"), this
platform's own scheduling mechanism is a Routine (`create_trigger` /
`send_later` in Claude Code Remote sessions) rather than Claude Cowork
specifically — ask "schedule this skill to run every [day] at [time]" and
Claude Code will set up the equivalent using its own trigger tooling instead
of Cowork's.

## Worked example (@aisimplified23, "How to Build Your 1st AI Agent")

A second creator's carousel walks the same Cowork → connect tools →
Automations path through one concrete example instead of the abstract
3-level frame above — useful as a template to copy when scoping a real
first agent instead of a generic one:

1. **Open Claude, switch to Cowork.**
2. **Give it one role** — a single plain-English instruction, e.g. "Check
   my new leads and write a personal follow-up for each one." Keep it to
   one job, not several.
3. **Test it** — let it handle a few real leads first, read the output,
   and give plain feedback ("too long," "too salesy," "make it sound more
   like me") until it sounds right. This loop matters more than getting
   the instruction perfect on the first try.
4. **Give it your info** — the business specifics it needs to make output
   relevant (listings/services, service area, customer types, follow-up
   style), so messages aren't generic.
5. **Connect only the tools it needs** — e.g. a Google Sheet for the lead
   data and Gmail for sending, nothing broader than the job requires.
6. **Make it run daily** — once steps 2-5 work reliably by hand, add a
   schedule (Cowork's Automations, or this platform's own Routine per the
   note above) so it runs unattended, e.g. every morning at 9 AM.
7. **Review, don't rubber-stamp** — the daily run should hand back
   prepared output for a human to check and send, not send unsupervised
   by default, especially for anything customer-facing.

The pattern generalizes past lead follow-up to any recurring one-role task
with a small, well-scoped tool list: steps 2 and 5 (one job, minimum
necessary access) are what keeps the agent reliable as it scales from "a
few leads" to "every day, unattended."
