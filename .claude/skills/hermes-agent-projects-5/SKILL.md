---
name: hermes-agent-projects-5
description: Five Hermes agent projects to build (email + calendar, content, personal research, lead research, personal Jarvis) and the rule to build only one first. Source: @aiclawbots. Maps to Claude Code agents in this repo.
---

# 5 Hermes agent projects (@aiclawbots)
Hermes = the open-source Hermes agent (`NousResearch/hermes-agent`, already in `setup-repos.sh`; see `hermes-nousresearch`). The projects are platform-agnostic; Claude Code versions are the agents named below (drafts only).
1. **Email + calendar agent** - connect inbox and calendar; summarise important emails, draft replies, prepare for meetings, flag what needs attention. -> agent `inbox-calendar-agent`.
2. **Content agent** - give it best posts, writing examples, offers, audience info; workflow researches ideas, drafts in your style, repurposes content, sends all to you for approval. -> `voice-content-agent`.
3. **Personal research agent** - topic, company or industry in; web research collected into one report; AgentReach adds YouTube, Reddit, X. -> `topic-research-agent`.
4. **Lead research agent** - give your ideal customer profile and what makes a company worth contacting; it researches, finds context, qualifies against your criteria, prepares personalised outreach research. -> `lead-research-agent`.
5. **Personal Jarvis** - Telegram or Slack front end, ElevenLabs voice, persistent memory, everyday tools. Needs accounts and tokens only you can create; not built here.
**The mistake:** building all five at once. Pick ONE repetitive job you already do weekly, build the agent around it, improve until you trust the output, then move on. Rule of thumb from `claude-50-hacks`: start read-only, connect tools only when needed.
