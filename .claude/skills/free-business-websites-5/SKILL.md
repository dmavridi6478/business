---
name: free-business-websites-5
description: Five free websites for a small business from the @entr3p2 carousel (Calendly for booking, SERPtag for SEO rank tracking, Google Business Profile for Maps and local search, Wave for invoicing and bookkeeping, Tally for forms) with what each is for, a fit check, the limits and data-protection questions the slides do not mention, and a setup order. Use when the user asks for free tools to run a small business, to take bookings, track rankings, appear on Google Maps, invoice customers or collect leads with forms.
---

# 5 useful websites for your business

Source: @entr3p2 carousel, 6 slides (cover, then five numbered sites with a screenshot each). Read on 13 October 2026. The slides give a one-line purpose per site; **free-plan limits, pricing and terms were not re-checked here**, because they change. Check each site's current pricing page before you rely on it.

| # | Site | One line on the slide | Good fit when | Questions the slide does not answer |
|---|---|---|---|---|
| 1 | **Calendly** (calendly.com) | Let customers book you while you sleep | You sell appointments or calls | What the free plan limits (event types, integrations, reminders); where the booking data is stored (GDPR) |
| 2 | **SERPtag** (serptag.com) | Find and track your SEO ranking and improve your online visibility | You want a first look at where you rank | How many keywords and domains are free; how current its data is. For serious work this repo already connects Ahrefs and Semrush |
| 3 | **Google Business Profile** (business.google.com) | Show up on Maps and local searches | You have a physical location or serve a local area | Verification takes time; reviews, opening hours and phone must be kept current; the listing is public |
| 4 | **Wave** (waveapps.com) | Free invoicing and bookkeeping | You invoice in a market Wave supports | **Tax and e-invoicing rules.** Wave is built for North American small businesses. [Likely] it does not meet Greek or other EU e-invoicing and tax reporting requirements, so confirm with your accountant before using it for real invoices there. Payment processing is normally paid |
| 5 | **Tally** (tally.so) | Free forms that collect orders and leads | You need a lead form, a survey or a simple order form | Where responses are stored; whether you need a consent line for personal data; payment features and file uploads may be paid |

## Setup order for a new small business

1. **Google Business Profile** first: it is free, local and the most likely source of a first enquiry.
2. **Tally** form for enquiries, linked from your site and your profile.
3. **Calendly** if enquiries lead to calls or appointments.
4. **Wave** (or your accountant's system) for invoices, after the tax question above is settled.
5. **SERPtag** monthly, to see whether the work above moved your rankings.

## Rules

- Free tools collect your customers' data. Before use, check where it is stored, add a privacy notice, and do not put health or other sensitive data into a general-purpose form or calendar.
- Do not rely on a free tool for something the business cannot stop doing (invoicing, bookings) without an export of your data.
- Use `prelaunch-website-audit-20` on the page that carries your form and booking links.

## Command

`/biz-sites-pick <your business, country and what you sell>` returns which of the five to set up first, what to check on each, and the data-protection note for your country.
