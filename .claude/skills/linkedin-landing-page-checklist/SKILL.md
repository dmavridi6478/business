---
name: linkedin-landing-page-checklist
description: A section-by-section checklist for turning a LinkedIn profile into a landing page (profile picture, banner, headline, About, Services page, Featured, Experience, Skills, custom button) with the slide's numbers, the audit prompt to run on your own profile, what could not be verified, and how it connects to the existing LinkedIn skills in this repo. Use when the user wants to optimise a LinkedIn profile for traffic or leads, or asks about banner, Featured or custom-button sizes and steps.
---

# How to make LinkedIn a landing page

Source: one infographic, "How to Make LinkedIn a Landing Page" (Charlie Hills, "AI Content Marketer"), attached in chat, 13 October 2026. Every number below is the slide's. I did not re-check LinkedIn's help pages, and LinkedIn changes its interface and Premium features.

## Checklist (one row per profile section)

| Section | What the slide says |
|---|---|
| Profile picture | Smile; 400 x 400 pixels; use your brand colours; zoomed in so the face takes up about 80% of the frame |
| Banner | The first impression. To add a slideshow banner: click the pencil icon, Change photo, Create slideshow, upload up to five images |
| Headline | Short and punchy; say what you do; simple language. Example on the slide: "I use AI to create content that converts." A famous title can do the talking; yours has to |
| About | Use storytelling; use quantifiable results; give contact details as the call to action. The slide says to use a prompt to template other creators' About sections, but the prompt is not shown |
| Services page | 1200 x 628 pixel image; send LinkedIn traffic to your website or newsletter |
| Featured | 1200 x 628 pixel images; show your core offering and drive traffic to it |
| Experience | Add a call to action; remove irrelevant roles; keep roles that complement your offer; add external links |
| Skills | Put your top three most relevant skills first (they collect endorsements); use all 50 slots to appear in more searches |
| Custom link (button) | A call to action under your headline. Premium custom links show in feeds under headlines. Steps: select the pen icon on your profile, scroll to the bottom and select "Edit Custom Button", set your call to action and URL, and turn on "Display on posts, messages & search results" |

## What I could not verify

- The sizes (400 x 400, 1200 x 628), the 50-skill limit, the slideshow banner and the custom button being Premium-only. Check LinkedIn's current help pages before you design to the pixel.
- The banner size is not on the slide. Look it up; do not guess.
- "Visibility in searches" gains from filling all 50 skills are the author's claim.

## Prompt: audit my profile against this checklist (mine, not the slide's)

```
Act as a LinkedIn strategist. I will paste my current headline, About section, Featured item titles, Services text, the last two Experience entries and my top skills. Check each section against this list: headline says what I do in plain words; About tells a short story, includes at least one quantified result that I supplied, and ends with a contact call to action; Featured and Services point to one clear offer; Experience has a call to action and no irrelevant roles; top three skills match my offer. For each section give PASS, FAIL or CAN'T CHECK with one line of why, then a rewrite that uses only facts I gave you. Never invent results or numbers. If a number is missing, ask me.

[paste your sections here]
```

## Using other creators' About sections

Look at public profiles for structure only. Do not copy their wording, and do not scrape profiles: LinkedIn's terms restrict automated collection. Ask Claude to describe the structure of an About section you pasted by hand, then write yours from your own facts.

## Connects to

- `linkedin-profile-auditor` (Claude Project audit, section by section)
- `/linkedin-profile-funnel`, `/linkedin-profile-rewrite`, `/linkedin-optimizer-system`
- Template `Artifacts/templates/annotated-callout-map-navy.html` for a similar annotated infographic

Command: `/linkedin-landing-page <paste your profile sections>`.
