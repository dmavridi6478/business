---
name: client-finding-seven-repos-promptifex
description: Checked register of the @promptifex carousel "7 GitHub repos for high-paying clients" - Google Maps scraper, Huginn, Firecrawl, check-if-email-exists, remote-jobs, Listmonk, Twenty - with licences read from the repos, what each really does, and the legal and consent cautions the slides omit (scraping terms, probing mailboxes, cold email consent, AGPL). Use before building a lead-finding stack from these, or when choosing a free CRM, mailer or scraper.
---

# "7 GitHub repos for high-paying clients" (read 22 November 2026)

Checked: six repos exist (`git ls-remote`) and their licences were read from the repo files; `remoteintech/remote-jobs` was not checked. Star counts on the cards (50.1k, 193k, 23.9k, 6.6k, 10.2k, 40.9k, 58.5k) are unchecked (GitHub API blocked). Nothing was cloned, installed or run. Headlines such as "your next 100 clients in 10 minutes" and "zero bounces" are marketing, not measured results.

| # | Project | Repo | Card says | Licence (read) | Cautions the card omits |
|---|---|---|---|---|---|
| 1 | Google Maps scraper | `gosom/google-maps-scraper` | Local businesses to a spreadsheet: name, phone, website, rating | MIT | Scraping Google Maps may breach Google's terms; collected business data can include personal data (GDPR); check terms and use official APIs where you can |
| 2 | Huginn | `huginn/huginn` | Agents that watch Reddit, X and the web and alert you | MIT | Self-hosted Ruby app with real set-up; watching social sites is limited by their terms and APIs; it finds posts, it does not qualify buyers |
| 3 | Firecrawl | `firecrawl/firecrawl` | Read any company site in seconds | AGPL-3.0 | AGPL: offer source if you run a modified copy as a service; respect robots.txt and site terms; a hosted paid version exists |
| 4 | check-if-email-exists | `reacherhq/check-if-email-exists` | Check an inbox exists without sending | MIT | It connects to mail servers (SMTP probing); results are probabilistic, many servers hide or block it, and your server IP can be blocklisted; commercial licence and hosted tier are separate |
| 5 | remote-jobs | `remoteintech/remote-jobs` | Directory of remote-friendly tech companies to pitch | not checked | A company list, not leads; "every company is open to remote work" is the card's claim; a directory entry is not consent to be pitched |
| 6 | Listmonk | `knadh/listmonk` | Free Mailchimp alternative: send to thousands, see opens and clicks | AGPL-3.0 | You still need an SMTP provider, SPF/DKIM/DMARC, an unsubscribe link and a lawful basis for every recipient; "free" excludes hosting and sending costs |
| 7 | Twenty | `twentyhq/twenty` | Free CRM, "like Salesforce, except free" | Mostly AGPL-3.0 (its LICENSE says so; some parts differ) | Self-hosting costs time and upkeep; check which features are in the paid cloud |

## The pipeline the carousel implies, and its weak point

Find businesses (1, 5) then research them (3, 2), clean emails (4), email them (6), track deals (7). The weak point is step 4 to 6: unsolicited bulk email needs a lawful basis and an opt-out in the EU, UK and many other places, and list-scraped addresses are the usual cause of spam complaints. A small, personal, relevant first message to a few dozen well-chosen prospects beats volume; use `cold-email` and `outreach-planning` and have your own counsel check local rules.

Related: `self-hosted-docker-stack` (Listmonk), `competitor-profiling-corey-haines` (Firecrawl), `gdpr-data-handling`. Use `/repo-vet owner/repo` and `/repo-licence-check` first.
