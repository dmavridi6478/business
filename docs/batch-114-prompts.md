# Batch 114 prompts (plain text, copy and paste)

Source material: two infographics (20 AI GTM tools; SEO keyword research strategy 2026) and a 48-image photo set (GitHub project cards, free-alternatives cards, Claude skill-install cards, GitHub trending cards).

## A. Pick an AI GTM tool by job (command: /ai-gtm-tools)

```
/ai-gtm-tools [the stage where pipeline leaks, for example "replies drop after the first email", or a tool name]
```

Plain version:

```
Use the ai-gtm-tools-20 skill. My pipeline leaks at: [stage and the number that shows it]. List the tools for that stage, what I already have for the same job, and recommend at most two to trial or none. For each give a success metric, a kill date, the vendor checks (data stored, opt-out handling, CRM write access) and a human approval step. Remind me the source list is sponsored and unverified. Draft only; do not sign up, connect or pay for anything.
```

## B. Keyword research plan (command: /keyword-research-plan)

```
/keyword-research-plan [business or site, audience, goal]
```

Plain version:

```
Build a keyword research plan for [business, audience, goal] using the 7 steps: understand the business, find seed keywords, expand ideas, analyze and evaluate, group and prioritize, map to content, track and refine. Cover the 10 keyword types (short-tail, long-tail, branded, non-branded, informational, navigational, commercial, transactional, local, question). Suggest which of the 10 research methods to use first. Score each keyword 0-2 on relevance, traffic potential, difficulty, intent match and business value, and state the cutoff before scoring. If Ahrefs or Semrush is connected, use it and name it; otherwise label every number an estimate. End with a keyword-to-URL map and a monthly tracking list.
```

## C. Turn the weekly task into a skill (existing command: /task-to-reusable-skill)

```
What task do I repeat every week? Ask me three questions to find the best candidate, then turn it into a skill with skill-creator: name, trigger description, steps, inputs, outputs, and one test prompt. Do not install anything until I approve.
```

## D. Self-host triage (existing command: /self-host-swap)

```
/self-host-swap [tool you pay for]
```

Plain version:

```
I pay for [tool]. Find the open-source alternative, read its licence (flag AGPL, fair-code and "Other"), estimate hosting, backup and maintenance time, and tell me whether to self-host, use its hosted plan, or keep what I have. Do not trust price comparisons on cards; ask me for my real bill.
```

## E. Anthropic skills install (run yourself; verified against the anthropics/skills README, 22 October 2026)

```
/plugin marketplace add anthropics/skills
/plugin install example-skills@anthropic-agent-skills
/plugin install document-skills@anthropic-agent-skills
```

These are demonstration skills and the document skills are source-available, not open source. Test before relying on them. All seven skills on the cards (frontend-design, skill-creator, pptx, pdf, webapp-testing, theme-factory, mcp-builder) already exist in this repository.
