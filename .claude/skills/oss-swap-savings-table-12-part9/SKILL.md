---
name: oss-swap-savings-table-12-part9
description: The "Save $6,846/year, use these free tools instead" (Part 9) swap table of 12 paid tools and their self-hosted replacements (Ulysses to Zettlr, Inoreader to Miniflux, Zoho Sign to OpenSign, CloudAMQP to RabbitMQ, Help Scout to FreeScout, Canny to Fider, Customer.io to Dittofeed, Hevo to Meltano, Roboflow to CVAT, Ecwid to Bagisto, Weebly to WordPress, Control D to AdGuard Home) with the licence read from each repo, the arithmetic of the headline total, where the saving is smaller than it looks, and which swaps need no server. Use when the user asks whether to replace one of these paid tools, wants the licence consequence, or wants to check the savings claim.
---

# Part 9: 12 free tools instead of paid ones

Source: @modelsignal, 14 slides (cover, 12 one-swap slides, a summary). Read 14 October 2026. Same series and format as Part 2 (see `oss-swap-savings-table-10`). Paid prices on the slides are marked "read 11 Oct" or "read 12 Oct"; star, developer and "pushed" figures are marked "checked" on the same dates. None of those figures was re-checked here (the GitHub API is out of reach in this session).

## The 12 swaps

Prices are the slide's monthly price times 12. Licences were read from each repo's LICENSE file on 14 October 2026.

| # | Job | Paid (slide) | Free tool | Licence (read) | What the "$0" leaves out |
|---|---|---|---|---|---|
| 1 | ELT data pipelines | Hevo $265/mo, $3,180/yr | Meltano | MIT | A managed service becomes pipelines you run, monitor and fix. The slide counts none of that time |
| 2 | Lifecycle email | Customer.io $100/mo, $1,200/yr | Dittofeed | MIT | You also own email deliverability: sending domain, warm-up, bounces, unsubscribe law |
| 3 | Feedback boards | Canny $79/mo, $948/yr | Fider | AGPL-3.0 | A server and database. AGPL: if you modify it and let others use it over a network, you must offer them your source |
| 4 | Image labeling | Roboflow $39/mo, $468/yr | CVAT | MIT | [Likely] CVAT is annotation. Roboflow also covers dataset versions, training and hosting, so check you only used labeling |
| 5 | Help desk | Help Scout $25/mo, $300/yr | FreeScout | AGPL-3.0 | The core is free; the README lists official and community modules separately. Check that the modules you need are free before counting the saving |
| 6 | Queues | CloudAMQP $19/mo, $228/yr | RabbitMQ | MPL-2.0 (core), some files Apache-2.0 | You take over upgrades, clustering, backups and alerts. Only a real saving if you already run servers |
| 7 | Websites | Weebly $13/mo, $156/yr | WordPress | GPL-2.0 or later | Hosting, security updates, backups. Hosting alone can cost about as much as the saving |
| 8 | Signatures | Zoho Sign $10/mo, $120/yr | OpenSign | AGPL-3.0, with one directory (`customRoute`) under its own licence and third-party parts under theirs | See below: a self-hosted tool is not a trust service |
| 9 | Online store | Ecwid $5/mo, $60/yr | Bagisto | MIT | A shop you host yourself, with payments, tax and PCI duties. [Likely] a small VPS costs more than $60 a year |
| 10 | Writing | Ulysses $5.99/mo, $72/yr | Zettlr | GPL-3.0 | Nothing to host: it is a desktop Markdown editor. The cleanest swap in the set |
| 11 | Feeds | Inoreader $7.50/mo, $90/yr | Miniflux | Apache-2.0 | A server and database for one reader. Small saving |
| 12 | Ad blocking | Control D $2/mo, $24/yr | AdGuard Home | GPL-3.0 | A device that is always on, and DNS you must secure. The saving is smaller than the cost of a Raspberry Pi |

## The arithmetic

- All 12 annual prices add to **$6,846**. That matches the cover and the summary headline.
- The summary slide is titled "8 of 12. Save it." and lists eight swaps. Those eight add to **$6,600** (3,180 + 1,200 + 948 + 468 + 300 + 228 + 156 + 120). The $6,846 headline therefore includes four swaps that are not on the list (the stated 8 miss Ecwid $60, Ulysses $72, Inoreader $90 and Control D $24 = $246). This is the same pattern as Part 2.
- Every monthly-to-yearly conversion on the slides checks out.
- Every figure is for one plan and one seat, as read on the slide date.

## Where the saving shrinks

1. **Small swaps cost more than they save.** Control D, Ecwid, Ulysses, Inoreader and Zoho Sign are $24 to $120 a year. Unless you already run a server, hosting and your time cost more.
2. **"You run it" is not free.** The slide ends every swap with "and you run it". Add your hourly cost for installing, upgrading, securing and backing up.
3. **The three big savings (Hevo, Customer.io, Canny) are the ones that need real operations work.** Do these only if someone on your team already runs data or email infrastructure.
4. **Maintenance signal.** OpenSign's slide reads "pushed 52d ago" while every other free tool except AdGuard Home (4 days) reads "today" or a few days, yet the slide still says "Switch this one". Read the repo's commit history yourself.

## Signatures: what a self-hosted tool does not give you

A self-hosted e-signature tool produces signed PDFs and an audit trail. It does not make you a trust service provider. [Likely] Under the EU's eIDAS rules a basic electronic signature is valid in many cases but is weaker evidence than an advanced or qualified signature, and the rules differ by document type and country. For contracts that matter, ask a lawyer before replacing a provider that issues qualified signatures.

## Decision rule

- **Do without a server:** Zettlr.
- **Do if you already run servers and have an owner:** Meltano, Dittofeed, Fider, FreeScout, CVAT, RabbitMQ.
- **Think twice:** WordPress, Bagisto, OpenSign, Miniflux, AdGuard Home. The saving is small, or the risk (payments, signatures, DNS) is large.
- **Do not count:** the $6,846 headline.

## Rules

- Do not state a price, star count or "pushed" date as current. They were read on 11 and 12 October.
- Self-hosting AGPL software for your own use is fine. Offering a modified version to others over a network is where the AGPL obligations start.

Command: `/swap-savings <the paid tools you use, seat counts, who would run a server>` (covers Part 2 and Part 9).
