---
name: free-llm-api-providers-13
description: The "GitHub's free LLM API resources" list from a @your.aimentor video (13 providers with free access or credits - OpenRouter, Google AI Studio, NVIDIA NIM, Mistral La Plateforme and Codestral, Hugging Face Inference Providers, Vercel AI Gateway, OpenCode Zen, Cerebras, Groq, Cohere, GitHub Models, Cloudflare Workers AI) with the safe way to use free tiers, and a note that the source repository could not be reached on 15 October 2026.
---

# Free LLM API providers (13)

Source: a short video: cover "GitHub's free LLM API resources" and one screenshot of a README titled "Free LLM API resources". The README text on screen: "This lists various services that provide free access or credits towards API-based LLM usage." Note: "Please don't abuse these services, else we might lose them." Warning: "This list explicitly excludes any services that are not legitimate (eg reverse engineers an existing chatbot)."

**Free Providers (as listed):** OpenRouter, Google AI Studio, NVIDIA NIM, Mistral (La Plateforme), Mistral (Codestral), HuggingFace Inference Providers, Vercel AI Gateway, OpenCode Zen, Cerebras, Groq, Cohere, GitHub Models, Cloudflare Workers AI.

## What I could and could not verify
- Web results name the repository as **cheahjs/free-llm-api-resources**. On 15 October 2026 `git ls-remote` and the raw README both failed for that slug from this session (not found), while third-party mirrors exist. Confirm the current repository before relying on it. I did not fetch or copy its contents.
- **No rate limits are given here.** Secondary sources disagree on them (for example Groq and Cerebras daily and per-minute limits) and free tiers change often; read each provider's own page the day you use it.

## Using free tiers safely
1. **Prototypes only.** Free tiers have rate limits, can be withdrawn, and carry no uptime promise. Production needs a paid plan or a fallback provider.
2. **No customer or confidential data.** Free tiers may log prompts and use them for improvement unless the terms say otherwise; read the data terms per provider. For EU personal data you need a lawful basis and often a data processing agreement, which free tiers rarely offer.
3. **Do not abuse them.** Use one key per person, no key sharing, no scraping many accounts; the list itself warns that abuse loses everyone the service.
4. **Abstract the provider.** Call models through one thin interface (or a router such as OpenRouter or the Vercel AI Gateway) so you can switch when a free tier ends.
5. **Record the model, provider and date** for any result you publish; free models change without notice.
6. **Quality varies:** small free models are fine for classification, drafting and tests, weaker for reasoning; evaluate on 10-20 of your own examples first (`eval-harness-first`).

Pairs with `cost-aware-llm-pipeline`, `model-router-2026`, `oss-ai-alternatives`, `huggingface-skills`.
