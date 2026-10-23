# Batch 116 prompts (plain text, copy and paste)

Source material: 71 images (GitHub project cards, Claude real-estate systems, faceless-channel story, automation-skill cards, a personal-brand map). The cards contain no prompts to transcribe verbatim except the one real-estate lead-score rule, rebuilt below as our own wording.

## A. Real estate system planner (command: /real-estate-system)

```
/real-estate-system [which system: lead generation, organic marketing, SDR follow-up or appointment booking, and your market]
```

Plain version:

```
Use the claude-real-estate-4-systems skill. Plan the [system] for [my market and listing type]. List its ten steps, what I must provide at each, and what I already have in this stack. Write the main prompt for the Claude Project with a scoring rule that uses only declared intent, property facts and engagement (never neighbourhood demographics, names, age or family status). State the fair-housing, consent, data-protection and approval checks for my market, and the outcome I will track for a quarter. Draft only; do not contact leads, connect accounts or send anything.
```

## B. Find a faceless niche with a YouTube scan (reference: yt-faceless-channel/references/claude-youtube-scan.md)

```
Use the YouTube Data API v3 with my key to scan the last 10 days for faceless channels in [topic area]. Run about 16 searches, take each channel's last 10 uploads, and rank videos by views divided by that channel's average. Report the top channels, the traits they share (presenter, title style, length, upload frequency, footage type, subscriber size) and the three niches with the best ratio. Do not estimate income. Then list the platform-policy, licence and voice-consent checks I must pass before making a video.
```

## C. 60-second narration script (from the story's script step)

```
Write a 60-second documentary narration in the style of [niche]: a hook in the first sentence, short sentences, about 140 words. Use only facts I supply or that you flag as needing a source. Mark any claim I must verify. Do not imitate a real person's voice.
```

## D. Skill description tester (for the 8 automation skills)

```
Here is a skill description: [paste]. Write three prompts that should trigger it and three near-miss prompts that should not. Tell me if the description is too broad or too narrow, and rewrite it as "use when ..." with concrete triggers.
```

## E. Personal brand map score (reference: linkedin-magnetic-brand-9-rules/references/personal-brand-strategy-map.md)

```
Score my personal brand 0-2 on each of the 14 parts (niche, positioning, story, voice, content pillars, proof, offer ladder; content engine, distribution, community, lead magnets, social proof, monetisation, optimisation) using what I tell you. Ask one question per part, then show the scores, name the lowest level-one part, and give one action for it this week.
```

## F. Check a repo card before you trust it

```
Here is a card claiming [repo] does [claim]. Open the repository README, state what it actually does, the licence, last release date and star count, and tell me whether the card matches. List the risks of installing it (permissions, network access, what it can delete).
```
