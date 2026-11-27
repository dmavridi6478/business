# Batch 113 - prompts in plain text

Copy and paste. Replace every [BRACKET] and read the output before using it.

## A. 25 prompts to check your visibility in LLMs (verbatim)

Source: Amanpreet, "25 Prompts to Check Your Visibility in LLMs, without paying for any tool". Skill: `llm-visibility-prompt-check`; command: `/llm-visibility-check`.

### Discovery and fit

01. What are the best [product/service category] providers?
02. What are the best [product/service category] companies in [location]?
03. Which [product/service category] would you recommend for [target audience]?
04. What are the best [product/service category] options for [industry]?
05. What is the best [product/service category] for [specific use case]?
06. Which companies can help me solve [customer problem]?

### Budget, features and trust

07. What are the best [product/service category] options under [budget]?
08. Which [product/service category] providers offer [key feature]?
09. What are the best [product/service category] options that integrate with [tool/platform]?
10. Which [product/service category] is easiest to implement for [team/company size]?
11. What are the most reliable [product/service category] providers?
12. Which [product/service category] companies have the best customer support?

### Comparisons and alternatives

13. Compare the top [number] [product/service category] providers for [use case].
14. Which [product/service category] companies should I shortlist for [requirements]?
15. What are the best alternatives to [competitor name]?
16. What should I choose instead of [competitor name] if I need [requirement]?

### Your brand

17. What is [brand name], and what does it offer?
18. Who is [brand name] best suited for?
19. Is [brand name] a good choice for [specific use case]?
20. What are the strengths and weaknesses of [brand name]?
21. How does [brand name] compare with [competitor name]?
22. What are the best alternatives to [brand name]?
23. What do customers say about [brand name]?
24. What should I know before buying from [brand name]?
25. Which sources would you use to evaluate [brand name]?

## B. Nine LinkedIn lead-generation strategy prompts (verbatim)

Source: ContentSmash, "9 LinkedIn Strategies for Lead Generation" (the graphic claims they "quickly generate 100+ inbound leads"; that claim is not evidenced). Stay inside LinkedIn's terms: no bulk automation or scraping; a human sends every message. Related: `linkedin-b2b-sales-levels`, `/linkedin-cold-traffic-system`.

### 1. Authority Content Strategy

```
Act as an industry expert. Create content that positions you as the go-to authority in [your niche]. Share client wins, behind-the-scenes insights, and contrarian takes. Post 5-7 times per week with strategic messaging that builds trust. Include specific results and case studies. Focus on problems your ICP faces daily. Use formats like "Here's what I learned after..." or "Most founders get this wrong..." Keep posts under 1,300 characters for maximum engagement.
```

### 2. Strategic Network Building

```
You're targeting decision makers. Connect with 20-30 ideal prospects daily using LinkedIn Sales Navigator. Filter by company size, role, and industry. Send personalized connection requests mentioning something specific from their profile or recent activity. Avoid generic messages. Build relationships before pitching. Focus on quality over quantity. Track connection acceptance rates and optimize your approach based on what works.
```

### 3. Lead Magnet Distribution

```
Act as a value provider. Create high-value resources your ICP actually wants. Share frameworks, templates, or case studies through LinkedIn posts. Use clear CTAs like "Comment 'FRAMEWORK' for the template." Gate valuable content behind email capture. Promote lead magnets 3-4 times per week. Test different formats: PDFs, video walkthroughs, or exclusive communities. Track conversion rates and double down on what performs best.
```

### 4. Engagement Amplification

```
You're building social proof. Engage meaningfully on your ideal prospects' content within 30 minutes of them posting. Leave thoughtful comments that add value, not generic praise. Share insights from your experience. Ask intelligent questions that spark discussion. This puts you on their radar consistently. Spend 15-20 minutes daily engaging strategically. Focus on posts from your target audience, not random content.
```

### 5. Direct Message Sequences

```
Act as a relationship builder. Send personalized DMs to connections who engage with your content or visit your profile. Start conversations, don't pitch immediately. Reference their recent posts or company updates. Use the formula: compliment + question + value offer. Keep initial messages under 50 words. Follow up consistently but not aggressively. Track response rates and refine your messaging based on what generates replies.
```

### 6. Profile Optimization System

```
You're creating a conversion machine. Optimize your LinkedIn profile as a landing page for your ideal clients. Use a professional headshot, compelling headline that states your value proposition, and a summary that speaks directly to your ICP's pain points. Include social proof, client results, and a clear CTA. Update your featured section with case studies and testimonials. Make it easy for prospects to understand how you help them.
```

### 7. Content Repurposing Engine

```
Act as a content multiplier. Turn one piece of successful content into 10 different formats. Transform client case studies into posts, carousels, videos, and stories. Repurpose webinar content into LinkedIn articles. Break down long-form content into bite-sized posts. Use different angles for the same core message. This maximizes your content ROI and ensures consistent posting without constant creation. Track which formats perform best for your audience.
```

### 8. Social Proof Amplification

```
You're building credibility at scale. Systematically collect and showcase client testimonials, case studies, and results. Create posts highlighting specific client wins with permission. Share screenshots of positive feedback and measurable outcomes. Use video testimonials when possible. Feature client logos and success metrics. This builds trust with prospects who see others achieving results. Update social proof regularly to keep content fresh and relevant.
```

### 9. Conversion Tracking System

```
Act as a data-driven marketer. Track every lead source, engagement metric, and conversion point. Use UTM parameters for links, monitor profile views, and measure content performance. Identify which posts generate the most leads and double down on similar content. Track the customer journey from first touch to closed deal. Use this data to optimize your strategy continuously. Set up monthly reviews to analyze what's working and eliminate what isn't.
```

## C. Command prompts (the instruction each new slash command runs)

### /llm-visibility-check

```
Use the `llm-visibility-prompt-check` skill for: "$ARGUMENTS"

1. Ask for any missing bracket values in one question (brand, category, location, audience, use case, competitor).
2. Print the 25 prompts with brackets filled, grouped as in the skill.
3. Give the empty recording sheet and the three-runs-per-prompt rule.
4. Do not run the prompts against any assistant yourself unless the user asks; do not invent results.
```

### /build-tal

```
Use the `tal-build-7-steps` skill for: "$ARGUMENTS"

1. From the customers and the product, propose: lookalike seed set, product tags to test, include and exclude keywords, department and minimum headcount, buyer role, and a relevance cutoff.
2. Say which step you could not complete without a data source, and what that source must provide.
3. End with the step 7 caution and a small test-batch plan. Do not export, scrape or send anything.
```

### /lead-gen-route

```
Use the `b2b-lead-gen-router` skill for: "$ARGUMENTS"

Name the matching phase or group, then the one or two existing skills or commands to use and why. If nothing fits, say so and stop; do not create a new file.
```

## D. Ready-to-paste task prompts

**Strategy before plan:** "Write my marketing strategy as a connected system: customer, positioning, offer, channel, brand, and how each reinforces the others. Then derive a six-week plan and cut any plan item that does not trace to a strategy link."

**Board deck:** "I uploaded our business plan, financial model and market research. Read them, check the slide titles against my materials, review the plan assumptions, then draft a 12-slide board deck: where we stand, performance, strategic priorities, investment plan, financial projections, decisions we need from the board. Mark every number with its source file and flag estimates."
