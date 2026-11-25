---
name: linux-server-hardening-guide
description: How to use the imthenachoman "How To Secure A Linux Server" guide safely - what the guide covers (firewalls, SSH hardening, intrusion detection and more, with sections from Introduction through Before You Start), a safe working method (test machine, snapshot, second session, one change at a time, rollback) and a verification checklist. Use when someone wants to harden a VPS or home server, plans a hardening session, or wants a review plan for a server they run.
---

# Securing a Linux server: working method for the guide

Source: a @sitetusk card for `imthenachoman/How-To-Secure-A-Linux-Server`, described as a free, step-by-step guide covering firewalls, SSH hardening, intrusion detection and other practical measures. The card shows only the table of contents start: Introduction (guide objective, why secure your server, why yet another guide, other guides, to do), Guide Overview (about, the author's use case, editing configuration files, contributing), Before You Start (identify your principles, pick a Linux distribution). Licence: CC BY-SA 4.0. The guide itself calls itself evolving and written for the author's use case.

I have not read the guide's chapters for this skill. What follows is general safe practice, not a summary of the guide; follow the guide's own commands for your distribution.

## Method
1. Decide what the server is for and what you must protect (the guide starts the same way: identify your principles).
2. Work on a test machine or a fresh VPS first, never first on production.
3. Take a snapshot or backup before the session.
4. Keep a second SSH session open while changing SSH or firewall settings, and test a new login in a third before closing anything.
5. Change one thing at a time; write down the command, why, and how to undo it.
6. Use the guide for your distribution and version; settings differ.
7. Re-check after updates; hardening drifts.

## Verification checklist (adapt after reading the guide)
- Can you still log in with the intended key, and is password login off if you intended that?
- Which ports listen, and does the firewall allow only those you intend?
- Are automatic security updates configured as you decided?
- Do logs show failed logins, and does someone read them?
- Is there a tested restore from backup?

## Boundaries
- This repository does not run hardening commands on any server. `/harden-server` produces a plan and checklist only.
- A hardened server is not a secure organisation: credentials, backups and patching matter as much.
- If the server holds personal data, record the measures you took; they may be needed for GDPR accountability.
