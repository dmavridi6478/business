---
name: outreach-channels
description: Execute cold outbound across non-email channels — a LinkedIn connection/DM sequence bounded by a 2-DM max rule, a 6-part cold-call script framework, and AI-personalized video outreach (Tavus/HeyGen-style). Use when a campaign needs LinkedIn, phone, or video touches alongside or instead of cold email.
---

# Outreach Channels

Source: reviewed from a social post showing a "Claude Code outreach project" skill tree (`linkedin-sequence.md`, `cold-call-script.md`, `video-outreach.md`); no external repo existed to vendor, so this is written fresh for this repo, covering the same three concerns as one skill.

Reuses `outreach-strategy`'s persona/pain/offer framing and `outreach-copywriting`'s messaging discipline, adapted to each channel's constraints and etiquette. Runs after list-building; typically as a complement to cold email rather than the only channel.

## 1. LinkedIn sequence: 2-DM max rule

LinkedIn tolerates far less volume than email before a profile gets reported or restricted. Cap direct outreach at two DMs total per contact: one connection-request note (short, references the trigger, no pitch) and one follow-up DM after acceptance (the actual offer, still under LinkedIn's shorter effective attention span than email). Do not chain additional DMs after silence — that's where automation tools get accounts flagged. A LinkedIn touch inside a multi-channel sequence is one data point, not the whole campaign; let email carry the follow-up cadence instead.

## 2. Cold-call script: 6-part framework

1. **Pattern interrupt** — open with something other than "how are you doing today," which triggers an automatic "fine, busy" hang-up reflex.
2. **Permission-based opener** — ask for the specific amount of time being requested, not an open-ended "got a minute."
3. **Reason for the call, trigger-anchored** — same trigger used in written outreach, spoken concisely.
4. **One diagnostic question** — confirm the assumed pain actually applies before pitching anything.
5. **Value statement, conditional on the answer** — tailor to what was just said, not a memorized pitch.
6. **Close with a specific next step** — a concrete date/time ask, not "I'll follow up."

Script this as a framework with branches, not a word-for-word read — a call that sounds scripted loses the prospect immediately.

## 3. Video outreach: AI-personalized video

Tools like Tavus or HeyGen generate personalized video (often the sender's likeness, dynamically inserting the prospect's name/company/logo) at outbound scale. Use for higher-value accounts where the novelty and personalization justify the extra production step over plain text — not as a blanket replacement for email, since video requires the recipient to actively watch rather than skim. Keep videos short (under 60 seconds) and lead with the same trigger-based hook as the written first-touch, since the opening seconds determine whether it gets watched at all.

## Related skills in this repo

- **outreach-strategy** / **outreach-copywriting**: supply the persona, offer, and messaging discipline each channel adapts.
- **outreach-automation**: video generation and multi-channel sequencing are natural n8n-workflow candidates once the manual process is validated.
- **social-content** (marketingskills plugin): general social-channel content technique, distinct from this skill's specific outbound-sales use of LinkedIn.
