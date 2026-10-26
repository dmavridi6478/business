# Batch 120 prompts (plain text, copy and paste)

Sources: the SalesDaily.co Cowork graphic (1 to 10, verbatim), the @buildbefore30 carousel (11 to 15, verbatim), the @ai_slacker carousel (16 to 21, verbatim). Prompts 22 and 23 are original.

## 1 to 10. Claude Cowork for sales reps (verbatim)

1. Go through my Google Drive folder [folder name]. Pull every doc, email, and note related to [account name]. Build me a one-page account brief with: deal history, key stakeholders, open issues, and last 3 touchpoints.
2. Here's my pipeline export [file]. Score every deal by likelihood to close this quarter based on last activity date, deal stage, and deal size. Flag anything that's been stuck in the same stage for 14+ days. Save as a spreadsheet sorted by priority.
3. Check my Gmail for any prospect threads where I sent the last message and haven't gotten a reply in 7+ days. List them out with the contact name, company, what I last sent, and draft a follow-up for each one.
4. Schedule this: Every Friday at 4pm, pull my latest pipeline data from [CRM export folder], calculate week-over-week movement by stage, flag any deals that slipped or stalled, and save a one-page summary to my Desktop.
5. Use the browser to research [prospect name] at [company]. Check their LinkedIn activity, recent company press releases, job postings, and earnings calls. Save a one-page research brief to my Sales Prep folder.
6. Go to [competitor website] and pull their pricing page, features page, and latest case studies. Compare against our positioning doc in [folder]. Build a battle card with: where we win, where they win, objection responses, and talk tracks.
7. Schedule this: Each morning at 7am, check my calendar for today's external meetings. For each one, look up the attendee's company, pull any related files from my Drive, and drop a 5-bullet prep doc on my Desktop before I start work.
8. Here are my call transcripts from this week [folder]. For each call, extract: buyer's stated priorities, objections raised, competitors mentioned, next steps promised, and any budget or timeline signals. Save as one summary doc.
9. Take this spreadsheet of leads [file]. Use the browser to verify each company's website, employee count, and industry. Remove any that are under 50 employees. Add a column with a personalized reason to reach out based on what you find. Save the updated file.
10. Open my [account name] folder. Read through every doc, email thread, and note from the last 90 days. Build a QBR presentation with: executive summary, key wins, usage highlights, open risks, and a proposed plan for next quarter. Save as a PPTX to my Desktop.

Add to any: "Use only the folder I named, name the source file for every claim, draft messages but do not send." Slash command: `/cowork-sales-prompt`.

## 11 to 15. Five prompts for building a business (verbatim)

11. Find 10 real problems that people or small businesses are already willing to pay for. For each, identify the target customer, an affordable solution, a simple MVP, pricing, and how I could find my first three customers. Prioritize ideas I can test within seven days.
12. Act as a senior UX designer, brand strategist and frontend developer. Create a premium, responsive website for [business]. First define the target audience, value proposition, visual direction and user journey. Avoid generic AI templates. Then build the complete website with polished typography, authentic visuals, mobile optimization and working interactions.
13. Create [number] photorealistic, high-quality images for [business]. The images should match my brand, feel authentic and not look like typical AI stock photos. Include different scenes, settings and angles that I can use for my website and social media. Save the images in high resolution and in WebP format. Suggest a consistent visual style and color palette based on my brand.
14. Act as a critical UX, conversion and product marketing expert. Review my website as if you were a first-time visitor. Identify confusing messaging, weak trust signals, unnecessary friction and missed conversion opportunities. Rank the most important improvements by impact. Don't flatter me. Give specific, actionable fixes and explain what to test before redesigning everything.
15. I have this product idea: [idea]. Help me validate demand before investing heavily. Identify my riskiest assumptions, define three potential customer segments, create a simple landing-page experiment, propose pricing tests and recommend what user actions to measure. Give me clear criteria for deciding whether to continue, change direction or stop.

## 16 to 21. Passive-income prompts (verbatim)

16. Act as a business systems architect. Design an automation framework for my passive income business that includes AI workflows, customer onboarding, payment processing, email marketing, analytics, customer support, documentation, CRM, content scheduling, and reporting. Clearly identify which processes should be automated and which require periodic human oversight. Restrictions: scalable automation only.
17. Act as a world-class entrepreneur and financial planner. Build a complete operating system for creating multiple passive and semi-passive income streams based on my skills, interests, available time, risk tolerance, and financial goals. Analyze my current situation, recommend the highest-leverage opportunities, validate each business model, and create a step-by-step execution plan.
18. Act as a creator economy strategist. Build a complete system for using content platforms such as YouTube, Instagram, Threads, TikTok, newsletters, blogs, and podcasts to create multiple income streams. Include audience growth strategy, content repurposing workflows, affiliate marketing, sponsorships, digital products, memberships, consulting, and email marketing. Explain how each income stream supports the others.
19. Act as a digital product entrepreneur. Design a complete strategy for creating digital assets that can generate recurring income over time. Recommend products such as online courses, eBooks, templates, prompt packs, software, memberships, printables, stock resources, and licensing opportunities. For each asset, include a creation roadmap, pricing strategy, marketing plan, delivery system, and maintenance requirements.
20. Act as a financial strategist. Build a diversified portfolio of passive and semi-passive income streams based on businesses that reduce dependence on a single source of income. Recommend an order for launching each income stream, explain how they complement one another, and identify the risks associated with each model. Restrictions: balanced, long-term strategy only, optimized for financial resilience.
21. Act as an elite business strategist. Generate 30 passive and semi-passive income ideas that fit my skills and resources. For each opportunity, include startup cost, implementation time, technical difficulty, scalability, recurring revenue potential, maintenance requirements, level of competition, and long-term profit potential. Rank each opportunity by launch speed, sustainability, and automation potential.

Slash command for 11 to 21: `/business-prompt`.

## 22. pgvector filtered-search test (original)

I use Postgres with pgvector, version [version], a table docs(id, tenant_id, content, embedding vector([dimension])) and [row count] rows. Write the SQL to create an HNSW cosine index and a filtered query for one tenant that returns 5 rows. Then give a test that compares the filtered approximate result with the exact result on 20 sample questions and reports recall and how many queries returned fewer than 5 rows. Show how to enable iterative scans if recall is poor, and how to enforce tenant isolation with row-level security. Say which parts depend on the pgvector version.

## 23. Trial an open-source agent app safely (original)

I want to try [app and repo] on my own machine. Read its README and licence and tell me: what it can access (files, shell, browser, accounts, connected apps), how it stores keys and transcripts, what runs in the cloud, and how recent and active the project is. Give me a plan to trial it in a virtual machine with a throwaway account and the fewest connectors, a checklist of what to inspect before I give it real credentials, and the stop conditions.
