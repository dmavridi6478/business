# Batch 114 prompts (plain text; replace [brackets])

## 1. App business check (`/app-business-check`) - @alinacoding
For [APP IDEA] and [TARGET CUSTOMER], answer six steps in one or two lines each: (1) the questions to ask real customers about how they handle this today; (2) the smallest demo that shows the core result; (3) the one paid feature and one plan, and how I test purchase and restore; (4) three funnel events: first useful action, paywall opened, purchase completed, and where I expect the biggest drop; (5) the failure that must never ship, for example a slot being booked twice; (6) the one store image: a real app screen with one short benefit above it. Flag any privacy or consent issue. Name the riskiest assumption, then stop.

## 2. Apple-style design audit (`/apple-design-audit`) - reconstructed from a video
[URL]. Audit this website's design using Apple's Human Interface Guidelines principles: clarity, deference, depth, hierarchy, consistency, typography, spacing, colour and contrast, motion and feedback, accessibility. For each principle give: what works, what breaks, evidence, severity, and a concrete fix. Then list the 5 highest-impact changes. Do not edit anything yet.
Follow-up: implement the top fixes, take a screenshot of the result, compare it to the original, list differences and fix them.

## 3. Single-line prompts from the tips on the slides
Ask owners: How do you handle bookings today? Who answers messages? What happens when a client cancels?
Sentry: Check the app version attached to this error. If it is from an old build, do not assume the new fix failed. Reproduce it in the current build before changing more code.
PostHog: Track the first useful action, paywall opened and purchase completed. Find the largest drop. Watch that part of the flow before adding another feature.
Canva: Show the result my app gives people, using an actual app screen. Put one short benefit above it. Check the image on a phone before making the rest of the set.

## 4. Token-saving claim check (for billion-context, Ruflo and similar)
Evaluate [TOOL] by its README and source. List what it changes in my prompts, what it sends to third parties, how compression could drop a needed detail, whether it breaks prompt caching, and one test I can run on a session where I already know the answer. Give a verdict: adopt, trial on a throwaway repo, or skip.
