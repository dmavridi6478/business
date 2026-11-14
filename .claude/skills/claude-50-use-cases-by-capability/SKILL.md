---
name: claude-50-use-cases-by-capability
description: The 50 Claude use cases infographic by Jonathan Parsons, grouped as printed in three columns (create and build; read, analyse and learn; connect, automate and personalise), with the Claude surface each uses and the installed skill or connector that covers it. Use when someone asks what Claude can do, which Claude surface (chat, Code, Cowork, Chrome, Excel, PowerPoint, Tag) fits a task, or wants ideas by capability rather than by job role.
---

# 50 Claude use cases (Jonathan Parsons)

This list differs from `claude-50-use-cases` (the Batch 102 slide grouped by ten areas). Numbers are as printed.

## Column 1 - create and build

| # | Use case | Surface | Start here |
|---|---|---|---|
| 1 | Email drafting | Chat | `email-drafter` |
| 2 | Blog and article writing (saved file, markdown) | Chat, writing skill | `article-writing` |
| 3 | Code generation | Chat, Code | `python-patterns`, `coding-standards` |
| 4 | Code review and debugging | Claude Code | `code-review` |
| 5 | End-to-end app building | Claude Code, IDE, desktop | `saas-mvp-24h` |
| 6 | Spreadsheet data analysis | Claude in Excel | `xlsx` |
| 7 | Slide deck creation | Claude in PowerPoint | `pptx` |
| 8 | Word document creation (.docx) | docx skill | `docx` |
| 9 | PDF creation and editing | pdf skill | `pdf` |
| 10 | Web research with citations | Chat search | `deep-research` |
| 11 | Deep research reports | Research feature | `hyperresearch` |
| 12 | Browser automation | Claude in Chrome | `browser` |
| 13 | Desktop task automation | Cowork | `cowork-sales-prompts-10` |
| 14 | Google Workspace tasks | Gmail, Calendar, Drive connectors | `google-workspace-ops` |
| 15 | Interactive diagrams (flowcharts, mind maps) | Inline visuals | `artifact-diagramming` |
| 16 | Data visualization | Artifacts | `dataviz` |
| 17 | Web prototypes (HTML or React) | Artifacts | `frontend-design` |

## Column 2 - read, analyse and learn

| # | Use case | Start here |
|---|---|---|
| 18 | Reading uploaded files and images | `attachment-intake` |
| 19 | Translation keeping tone | `translate-preserve-tone` |
| 20 | Summarization | `research-summary` |
| 21 | Meeting notes from transcripts | `meeting-notes-processor` |
| 22 | Tutoring | `learn-topic` |
| 23 | Quiz and flashcard generation | `quiz` |
| 24 | Brainstorming | `brainstorm` |
| 25 | Resume and cover letter writing | `resume-review` |
| 26 | Contract review (not legal advice) | `contract-review` |
| 27 | Financial modeling | `startup-financial-modeling` |
| 28 | Slack-based team support with Claude Tag | `slack-by-salesforce:slack-messaging` |
| 29 | Social media content | `social-publisher` |
| 30 | SEO-informed writing | `seo` |
| 31 | Multi-step agentic tasks | `orchestration` |
| 32 | Third-party tool integration (Asana, Jira, Notion via MCP) | `connector-starter-stacks` |
| 33 | Recipe planning with scaling servings | Artifacts |

## Column 3 - connect, automate and personalise

| # | Use case | Start here |
|---|---|---|
| 34 | Trip itinerary planning with a map | `tineo-travel:plan-a-trip` |
| 35 | Product comparisons | `product-comparison-table` |
| 36 | Custom trackers and small tools | `claude-mini-app-builder` |
| 37 | Custom skill creation | `skill-creator` |
| 38 | Long-document drafting by section | `doc-coauthoring` |
| 39 | Data cleaning | `data-quality-frameworks` |
| 40 | Building AI features with the API | `claude-api` |
| 41 | Customer feedback analysis | `customer-feedback-themes` |
| 42 | Visual mockups with Claude Design | `design-superpowers:design` |
| 43 | Inbox triage in Outlook | `inbox-manager` |
| 44 | Competitive research (Chrome plus Cowork report) | `competitor-analysis` |
| 45 | Small interactive games or demos | Artifacts |
| 46 | Journaling tools with artifact storage | Artifacts |
| 47 | Cross-device continuity (mobile to Cowork) | Claude apps |
| 48 | Sports and market lookups | Search tools |
| 49 | Image-based place and shopping discovery | Chat with photos |
| 50 | Company-wide workflow orchestration (Team or Enterprise, SSO) | `enterprise-agent-ops` |

## Reading it critically

- Several items depend on plan and surface (Claude in Excel and PowerPoint, Tag, Cowork, company-wide SSO): confirm availability before promising them to a client.
- The slide groups by capability, not by outcome; for outcomes use `claude-sales-by-role` or `claude-marketing-jobs`.
- Use `/use-case-pick [goal or role]` to select three items and the surface to use.
