---
name: claude-code-mod-builder
description: 'Five-step workflow to find what you repeat in Claude Code and turn it into a small plugin ("mod"): audit your recent sessions, pick one repeat, build and test it, save it as a plugin, share it through a marketplace; with the five-question check and nine mod ideas (open-loops, sessions-band, mission-control, done-ping, secrets-guard, safe-delete, outbox, plain-reply, brand-theme). Use when the user wants to customise Claude Code or package a repeated workflow. Source: "How to Make a Claude Code Mod" infographic (@aisimplified23). Commands in it are unverified.'
---

# Claude Code mod builder

Source idea: **Skill -> MCP -> Mod.** A skill tells Claude how to do a job; MCP connects tools; a mod changes the app itself.

## Verification status (read first)
| Item in the infographic | Status |
|---|---|
| `/plugin enable cc-plugin-you-should-know@builtin` and "needs v2.1.287+ and usage-data sharing" | **Not verified.** I could not confirm this plugin or version. Check `/plugin` in your own Claude Code before trusting it. Turning on usage-data sharing is a privacy choice for the owner |
| `claude plugin marketplace add you/your-mod` | Matches the documented `claude plugin marketplace add` command; the repo name is a placeholder |
| "Your mod disappears when the chat closes - tell Claude: save this mod as a plugin" | Plausible, unverified |
Nothing here was run in the cloud session.

## The five steps
1. **Set up** - confirm plugins work in your version (`/plugin`).
2. **Run the audit** - Prompt 1 below.
3. **Build it** - pick one repeat; Prompt 2 pattern; test it.
4. **Keep it** - save as a plugin so it loads every session.
5. **Share it** - put the plugin in a GitHub repo; teammates add it with one marketplace command.

## Prompt 1 - the audit
```
Read my last 30 Claude Code sessions. Find what I ask for again and again. Suggest five mods that would fix it.
```
Privacy note: session history can hold secrets and client data. Run it only on your own machine, and read the suggestions before saving anything.

## Prompt 2 - example build (open-loops)
```
Build me a Claude Code mod called open-loops. Every time I send a prompt, list each thing I asked for in a panel beside the chat. Only tick an ask off when you give proof (a file path, a link or a sent message). Show "Open loops: N" in the bar under the chat, and add a /loops command that lists what's still open.
```
Reusable pattern: `Build me a Claude Code mod called <name>. <trigger>. <what it shows or does>. <proof or safety rule>. Add a /<command> that <list or toggle>.`

## Check before you build (5 yeses -> build, any no -> skip)
Do you ask for this every day? Can you see it without typing a command? Does it run by itself? Can you read it in one glance? Does it keep your keys hidden?

## Nine ideas from the source
open-loops (every ask until done), sessions-band (bar of other sessions), mission-control (plan as live progress bar), done-ping (ping when Claude finishes), secrets-guard (blocks key files, hides keys in output), safe-delete (deletes go to the Bin), outbox (holds every email until you say yes), plain-reply (flags hard-to-read replies), brand-theme (your colours).
Fit with this repo's rules: `outbox` and `secrets-guard` match the draft-only and no-secrets stance already enforced by hooks; check `.claude/settings.json` before adding overlapping ones.

Command: `/mod-builder`. Related: `claude-code-cheatsheet-2026`, `claude-code-tooling`, `claude-code-setup-plugin`.

## Keywords
Claude Code, plugin, mod, hooks, customisation, audit sessions, marketplace
