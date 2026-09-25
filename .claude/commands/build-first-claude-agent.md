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
