---
name: sales-email-prompt-pack
description: Nine copy-paste AI prompts for better B2B sales emails - personalised opener, simplifier, subject-line factory, feature-to-benefit translator, objection follow-up, breakup email, case-study snippet, spam and tone audit, and a full five-email sequence builder - each with its purpose, required inputs, quality checks and the compliance gates that apply before anything is sent. Use when someone wants to write, shorten, test, audit or sequence a sales or outreach email. Run via /sales-email (a number 1-9 or a name). Source - "9 AI Prompts to Write Better Sales Emails" infographic (SalesDaily.co).
---

# 9 AI prompts for better sales emails

Prompts are transcribed from the source; square brackets are inputs the user must supply. Claude fills nothing in by guessing. Every output is a **draft**: sending is a human decision after the checks below.

## The prompts

**1. The personalised opener** - purpose: skip the "hope you're well" trap and prove you did your homework.
> Here's my prospect's LinkedIn profile: [paste]. Write 3 opening lines for a cold email that reference something specific about their career, recent activity, or company. No flattery. Make it sound like I actually read their page.

**2. The simplifier** - purpose: shorter emails get more replies.
> Rewrite this sales email at a 5th grade reading level. Cut it to under 80 words. Remove every word that doesn't earn its spot. Keep one clear CTA: [paste draft]

**3. The subject line factory** - purpose: test 10 options instead of guessing one.
> Here's my email body: [paste]. Give me 10 subject lines using these angles: curiosity, a specific number, their company name, a pain point, and a bold claim. Keep each under 6 words.

**4. The feature-to-benefit translator** - purpose: features describe your product; benefits describe their life after buying.
> I'm selling [product] to a [prospect's title] at a [company type]. Here are my product's features: [list]. Rewrite each one as a benefit statement this buyer would actually care about. Start each with "You" or "Your team."

**5. The objection follow-up** - purpose: address the real blocker instead of "circling back".
> My prospect said: "[exact objection]". Their role is [title] at a [company type]. Write a follow-up email that acknowledges their concern without agreeing, reframes the value around their specific pain point, and ends with a soft CTA. Under 100 words.

**6. The breakup email** - purpose: remove all pressure with a final message.
> I've sent [number] emails to [prospect's title] at [company] over [timeframe] with no reply. Write a final email that's honest, zero-pressure, and gives them an easy out. Make it feel human, not passive-aggressive. Under 60 words.

**7. The case study snippet** - purpose: one case study becomes ammunition for every persona.
> Here's a full case study: [paste]. Write a 2-sentence version for a [specific role] that leads with the metric they care about most. Then write a different 2-sentence version for a [different role]. No buzzwords.

**8. The spam and tone audit** - purpose: catch spam-trigger language and robotic tone before sending.
> Here's my sales email: [paste]. Flag any words or phrases likely to trigger spam filters. Rate the tone from 1-10 on warmth and confidence. Then rewrite it with your fixes applied.

**9. The full sequence builder** - purpose: a working five-email draft in minutes.
> I sell [product/service] to [ICP]. The main pain point I solve is [pain]. Build a 5-email outbound sequence. Email 1: pain-focused. Email 2: social proof. Email 3: insight or contrarian take. Email 4: direct ask. Email 5: breakup. Keep each under 80 words.

## Checks Claude must apply to every output

1. **No invented facts.** Personalisation (prompt 1) uses only text the user pasted. Case-study numbers (prompt 7) come only from the pasted case study. Social proof (sequence email 2) must match a row in `docs/marketing-context/proof.md`, else write "[proof needed]".
2. **Word limits are counted** and stated (e.g. "74 words").
3. **One CTA** per email.
4. **Banned phrases** in `docs/marketing-context/banned.md` are absent; voice follows `voice.md` when present.
5. **Deliverability reality check (prompt 8).** Word lists are heuristics; inbox placement depends mainly on authentication (SPF, DKIM, DMARC), sending reputation and list quality. Say so.
6. **Source claims are unproven.** The source's statements that shorter emails get more replies and that breakup emails pull the highest reply rates are assertions with no data shown; do not present them as facts to a client.

## Compliance gates before sending

- Lawful basis for contacting the person (legitimate interest assessment under GDPR for EU recipients; ePrivacy rules for email) and a working opt-out.
- Human approval and a stated send cap; follow `outbound-campaign-brief` and `gtm-outbound-engine`.
- Greek-language emails: keep original product and place names in Latin script where the brand uses them; no punctuation in capital letters in Greek text.

Pairs with: `cold-email`, `outreach-planning`, `outreach-execution`, `copywriting`, `email-drafter`, `handle-objection` (sales plugin), `claude-marketing-50-verbs`.

## Keywords
sales email prompts, cold email, subject lines, breakup email, objection follow-up, sequence, spam audit
