---
name: prelaunch-website-audit-20
description: A 20-point pre-launch audit for a website (secrets, HTTPS, privacy and terms pages, cookie consent, forms, spam, meta tags, social image, favicon, sitemap and robots, alt text, image weight, speed, contrast, mobile, 404, broken links, analytics, one call to action) with the exact copy-paste prompt, what to paste so each check can actually be decided, which checks Claude cannot do from pasted code, a stdlib script that settles the mechanical ones, and the fix for each. Use when the user is about to launch or relaunch a site, wants a launch checklist, or asks Claude to audit a page before going live.
---

# Pre-launch website audit (20 checks)

Source: @claude.with.christelle carousel, 3 slides ("20 things to have Claude check before you launch your website"). Read on 13 October 2026. The slides are the author's list and prompt; the method, the limits table and the script below were added here.

## The 20 checks, in two groups (as on the slides)

**Group 1, "the ones that get you hacked or fined" (1-7):** secrets off the frontend, force HTTPS, privacy policy page, terms and conditions page, cookie consent banner, form validation, spam protection. The slide says #1 matters most: an API key in page code is visible to every visitor, so keys belong on the server.

**Group 2, "the ones that make you invisible or broken" (8-20):** meta titles and descriptions, social preview image, favicon, sitemap and robots.txt, alt text on images, compress images, page load speed, colour contrast, mobile friendly, custom 404 page, fix broken links, set up analytics, one clear call to action.

## The prompt (copy and paste; the slide's own words, lightly tidied)

```
You are a pre-launch auditor. I'll paste my site's code and page copy below.

Check these 20: secrets in frontend, HTTPS, privacy policy, terms, cookie consent, form validation, spam protection, meta titles and descriptions, social preview image, favicon, sitemap and robots.txt, alt text, image compression, page speed, color contrast, mobile layout, 404 page, broken links, analytics, one clear call to action.

For each: PASS / FAIL / CAN'T CHECK, one line why, and the exact fix. Never guess. If you can't verify it from what I pasted, say CAN'T CHECK.

End with the 5 fixes to do first.

[paste page HTML, page copy, robots.txt, sitemap.xml, a Lighthouse report, and a list of your forms here]
```

## What to paste so a check can be decided

| # | Check | Decidable from | Cannot be decided from pasted HTML |
|---|---|---|---|
| 1 | Secrets in the frontend | all shipped JS and HTML | keys that live only in server code (good) |
| 2 | HTTPS | any `http://` resource links in the code | the server redirect and HSTS header: test with `curl -I http://yoursite` |
| 3-4 | Privacy and terms pages | footer links and the page text | whether the text is legally adequate |
| 5 | Cookie consent | consent script present | whether tracking really waits for consent: test in a browser with cookies cleared |
| 6-7 | Form validation, spam | form markup, attributes, captcha or honeypot | server-side validation: needs the backend code |
| 8-10 | Meta tags, social image, favicon | `<head>` | whether the image URL loads and is the right size |
| 11 | Sitemap and robots | the files themselves | whether search engines fetched them |
| 12 | Alt text | `<img>` tags | whether the alt text is meaningful |
| 13-15 | Image size, speed, contrast | a Lighthouse report | anything else: Claude cannot measure these |
| 16 | Mobile | viewport tag and CSS | real devices |
| 17-18 | 404 page, broken links | a crawl result | live requests |
| 19-20 | Analytics, one call to action | snippet and page copy | whether the data arrives |

The slide's own "honest limits": Claude audits what you paste; it cannot test real speed, so run Lighthouse and paste the results; legal pages it drafts are starting points, not legal advice. That is correct. Add: **a PASS means "nothing wrong in what was pasted", not "this is fine".**

## Mechanical pre-check (no model, no network)

`scripts/prelaunch_check.py` settles the items that can be decided from HTML alone and reports everything else as CAN'T CHECK:

```bash
python3 -I scripts/prelaunch_check.py index.html about.html
```

It checks: key-like strings (OpenAI, AWS, GitHub, Slack, Google patterns and hard-coded credentials), `http://` resources, privacy and terms links, cookie-consent code, form fields without `required` or `pattern`, captcha or honeypot, title and description length, `og:image`, favicon link, `alt` attributes, viewport meta, analytics snippet and an action button. It was tested on a deliberately broken page (12 FAILs) and on this repo's `Artifacts/index.html` (an internal index, not a launch site: it has no description, social image, favicon, viewport tag or analytics, which is expected for its purpose).

## Fix guide (the first five to do on most sites)

1. Move any key to the server and rotate the exposed one; a key that was public is burned.
2. Redirect HTTP to HTTPS at the host and set HSTS.
3. Add privacy policy and terms pages, written or reviewed by someone who knows your jurisdiction (GDPR if you serve the EU).
4. Add a viewport meta tag, a unique title (under about 60 characters) and description (about 50 to 160) to every page.
5. Add a captcha or honeypot to every public form and validate on the server.

## Rules

- A script and a model both miss things. Treat the result as a work list, not a certificate.
- Never paste real secrets into a prompt. If check 1 fails, rotate the key; do not repeat it in the conversation.
- The privacy and cookie items are legal duties in many places; the audit flags absence only.

## Command

`/prelaunch-audit <paste or path>` runs the script first, then the model pass on what the script could not decide. A design template for the checklist card is `Artifacts/templates/checklist-dark-copper-grid.html`.
