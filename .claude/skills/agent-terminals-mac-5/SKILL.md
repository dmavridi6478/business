---
name: agent-terminals-mac-5
description: The @henryxagi "Your AI agents need a better terminal - 5 Mac apps worth a look" series - MXterm (a pane per agent with live status), Wave (open-source terminal with file previews and a browser), Tabby (modern terminal), Vesta (native terminal on libghostty for parallel coding agents) and Calyx (run and supervise coding agents in parallel) - with what each does, what the slides show, what is unverified (no repo links or licences on the slides), and a checklist for choosing a terminal to run several coding agents at once. Use when picking a terminal or multi-agent workspace for Claude Code, Codex or Gemini CLI on a Mac.
---

# Terminals for running coding agents (5 Mac apps)

The slides show app icons and mock-ups only: no repositories, licences or install commands, so every row below needs checking before you install. Not installed in the cloud session.

| App | Tagline (slide) | What the screenshot shows | Notes |
|---|---|---|---|
| MXterm | "A pane for every agent, with a live status" | workspaces on the left; panes running Claude Code, Codex and Gemini CLI plus a shell; per-agent status; SSH and machines section; v1.1.55 | find the official repo or site; confirm it is not a lookalike |
| Wave | "Open-source terminal with file previews and a browser" | terminal, file preview and web panes side by side; widget bar | Wave Terminal (wavetermdev/waveterm, Apache-2.0 per its README as I recall; verify); macOS, Linux, Windows |
| Tabby | "A terminal for a more modern age" | tabs and split panes, config in YAML, SSH and serial | Tabby (formerly Terminus); open source; Electron |
| Vesta | "Native terminal for running coding agents in parallel" | native macOS app (Swift/AppKit) on libghostty; a multiplexer daemon so sessions survive quitting; control socket to open, split, send keys, capture, notify; Lua plugins; reads your Ghostty config; v0.1.10 | very new (0.1.x): expect rough edges |
| Calyx | "Run and supervise coding agents in parallel" | tabs, groups and a "Changes" view | minimal screenshot: verify features |

## Choosing (my checklist)
1. Do sessions survive an app quit or SSH drop (a multiplexer like tmux or Vesta's daemon)?
2. Can you see which agent is waiting for approval? (status, notifications)
3. Per-pane working directory and git worktree, so two agents never edit the same checkout (`using-git-worktrees`, `dmux-workflows`).
4. A review surface for each agent's diff before merge.
5. Source, licence, update channel, and what it can do with your keys: a terminal sees everything you type.
6. Cost of staying on tmux plus a good prompt: for many people that is enough.

## Cautions
Run several agents only with permission rules (`claude-automation-stack-3-tiers`); parallel agents multiply token cost and merge conflicts. Unknown "AI terminals" can log keystrokes: prefer open source you can read, and install from the official release page. Related: `herdr`, `dmux-workflows`, `orca-cli`, `claude-devfleet`, `replace-so-oss-repos-10-oct` (Emdash, Jean). Command: `/agent-terminal-pick`.
