---
name: linkedin-six-profile-prompts-abby
description: The @abby.ai.business carousel "I just cancelled my LinkedIn premium. I asked Claude to fix my LinkedIn profile" - six profile prompts (experience to show ROI, profile into a 30-second pitch, keyword injection, full profile fix, headline, About section under 260 words) transcribed with their slots, how they differ from the repo's other LinkedIn prompt sets, and the checks the carousel omits (invented numbers, privacy of pasted profile text, keyword stuffing, claims that Claude replaces Premium). Use when rewriting a LinkedIn profile with any chat model.
---

# Six Claude prompts to fix a LinkedIn profile

Source: seven slides from @abby.ai.business ("AI Business Gains"): a cover ("I just cancelled my LinkedIn premium. I asked Claude to fix my LinkedIn profile. No costly or secret tools. Just prompts that actually deliver results.") and six prompt slides. Prompt texts are the slides'; slots in [BRACKETS] are theirs. The checks and order are my additions; nothing was tested.

| # | Slide title | Prompt (verbatim) |
|---|---|---|
| 1 | Rewrite Experience to Show ROI | "You are a resume and LinkedIn optimization specialist. Rewrite my 'Experience' section for each job listed in my LinkedIn so it focuses on outcomes, numbers, KPIs, and skills recruiters look for. Make sure it's easy to skim and speaks in recruiter language. Here's my current experience section: [PASTE TEXT]" |
| 2 | Turn Your Profile Into a Pitch | "You are a career storyteller and elevator pitch expert. Based on my LinkedIn profile, write a 30-second pitch that I can use in my summary section or video intro. Make it sharp, confident, and results-driven. Profile: [PASTE PROFILE TEXT]" |
| 3 | Inject Keywords To Rank Higher | "You are a LinkedIn SEO expert. Scan my profile and inject high-ranking keywords for my industry (e.g., data science, UX, etc.) in a natural way to make it rank higher in recruiter search. Do not keyword stuff. My profile: [PASTE PROFILE TEXT]" |
| 4 | Fix Your LinkedIn Profile Instantly | "You are a professional LinkedIn profile optimizer for Fortune 500 job seekers. Review my entire LinkedIn profile below and suggest exact rewrites for headline, about, experience, skills, and featured sections. Make sure it's fully keyword optimized for ATS and recruiter search. My goal: [Insert goal]. Here's the profile: [PASTE PROFILE TEXT]" |
| 5 | LinkedIn Headline That Sells | "You are a world-class LinkedIn personal branding expert. Rewrite my LinkedIn headline to make it highly attractive to recruiters in my field. Use clear keywords, job specific value, and a positioning that makes me irresistible in search. Here's my profile for context: [PASTE LINKEDIN PROFILE]" |
| 6 | Optimize Your About Section | "You are a top tier LinkedIn copywriter. Rewrite my About section so that it clearly explains who I am, what problems I solve, and why I'm valuable while keeping it warm, clear, and keyword optimized. Keep it under 260 words. Here's my existing profile: [PASTE PROFILE TEXT]" |

## How this differs from the repo's other sets

`/cv-linkedin-prompts` (six chained prompts built on a career file and a role-fit map) and `linkedin-opus-lead-machine` (15 prompts, lead generation) are structured and ask for evidence first. These six are one-shot rewrites aimed at recruiters. For a client-attracting profile use the six-part formula in `linkedin-headline-six-parts` instead.

## Checks the carousel omits

- **Invented results.** Prompts 1, 2 and 4 ask for "numbers, KPIs, results-driven". A model will invent figures if you give none. Add "use only numbers I provide; mark gaps with a question" to every prompt.
- **Privacy.** You paste your whole profile; if you paste other people's names or confidential employer figures, remove them first.
- **Keywords come from job ads, not the model.** Copy the real words from 5 target job posts and tell the model to use only those; "high-ranking keywords" are a guess.
- **ATS and ranking claims.** "Fully optimised for ATS" and "irresistible in search" are not measurable. Track search appearances and recruiter messages for four weeks before and after.
- **The cover's claim.** Cancelling Premium is a personal anecdote with no data; Premium's features (InMail, insights) are not what these prompts replace.
- **Your voice.** Rewrites read generic; edit so every sentence is something you can defend in an interview.

## Order (my addition)

5 headline, then 6 About, then 1 Experience, then 2 pitch, then 3 keywords against real job ads, then 4 as a final read-through. Change one section at a time. Use `/linkedin-six-prompts [number]`. Nothing is posted or edited on LinkedIn.
