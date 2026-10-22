---
name: watchthefacts-skill-finder-warning-greek
description: A Greek-language 36-second @watchthefacts video about finding Claude skills (claims of 173,130 then more than 1,000,000 skills, an auto-installing skill finder, and the advice never to install skills without checking their reliability first), with the Greek wording kept and a safe-install checklist. The tool promoted sits behind a link in the profile and was not inspected.
---

# Skill finder and the "never install unchecked skills" advice (@watchthefacts, Greek)

Source: a Greek-captioned slideshow video. Original wording kept in brackets. There is no transcript.

## What it says
- "Ήξερες ότι..." (Did you know...): skill types shown as tiles: docx, pdf, xlsx, pptx, seo, design, code, data, email.
- A library counter climbs from **173,130** to **1,000,000+** skills for Claude ("Αντλεί δεδομένα από μια βιβλιοθήκη με πάνω από 1 εκατομμύριο skills").
- A mock chat: "Χρειάζομαι skill για PDF" (I need a PDF skill); the finder "searches 1,000,000+ skills", picks **pdf-toolkit, rating 4.9, Best choice (Καλύτερη επιλογή)** and installs it automatically ("Εγκατάσταση... 71%").
- Then the warning: "Ποτέ μην εγκαθιστάς skills χωρίς έλεγχο" (never install skills without checking), "Άγνωστη πηγή" (unknown source), "Έλεγξέ τα πρώτα!" (check them first), "Ζήτα από το ChatGPT ή το Claude να τα ελέγξουν για σένα" (ask ChatGPT or Claude to check them for you).
- Call to action: the link to get it is in the profile and description; like and follow.

## Read critically
- **[Certain]** The video contradicts itself: it sells an auto-installing finder, then says never to install without checking. Auto-install of unvetted skills is exactly the risk.
- **[Certain]** The "pdf-toolkit 4.9" result is a staged mock-up; the count figures are unsourced and the finder was not inspected.
- **[Likely]** Asking a model to review a skill helps find obvious problems but is not a security audit; a skill can contain scripts and instructions that act on your files and accounts.

## Safe-install checklist (mine)
1. Read the whole SKILL.md and every script it references.
2. Check the repo owner, age, issues and licence; pin a commit.
3. Install only in a test project first; keep file and network access minimal.
4. Never let a finder install automatically; require a yes per skill.
- Related: `skill-scout`, `skill-stocktake`, `claude-5-official-skills`, `prompt-injection-defense`.
