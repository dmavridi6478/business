---
description: Plan a homelab alert setup (Uptime Kuma, ntfy, Beszel, Dozzle, What's Up Docker) for your services - plans only, installs nothing
argument-hint: [services to watch, where they run, how you want to be alerted]
---

Input: "$ARGUMENTS". If empty, ask what runs where and what should wake the user up.

Use `.claude/skills/oss-homelab-rust-agency-nov2026/SKILL.md` and `self-hosted-docker-stack`.

1. Split the need: is it up (Uptime Kuma), how loaded (Beszel), what is it saying (Dozzle), is it outdated (What's Up Docker), how do I get told (ntfy).
2. For ntfy: on the public server the topic name acts as a password. Propose a long random topic or self-hosting with access control and a token, and keep secrets out of messages. Uptime Kuma has a built-in ntfy provider (server URL, topic, optional token).
3. Give a minimal order of work and one test per step (stop a service on purpose, confirm the phone alert, then restore it).
4. Warn that the monitor itself needs to be watched from outside, and that log views can reveal secrets.
5. The "alert setup" slide had no steps in the files; do not claim to reproduce it.

Install and run nothing. End with `Not verified:`.
