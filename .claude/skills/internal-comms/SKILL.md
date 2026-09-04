---
name: internal-comms
description: A set of resources to help me write all kinds of internal communications, using the formats that my company likes to use. Claude should use this skill whenever asked to write some sort of internal communications (status reports, leadership updates, 3P updates, company newsletters, FAQs, incident reports, project updates, etc.).
license: Complete terms in LICENSE.txt
---

## When to use this skill
To write internal communications, use this skill for:
- 3P updates (Progress, Plans, Problems)
- Company newsletters
- FAQ responses
- Status reports
- Leadership updates
- Project updates
- Incident reports

## How to use this skill

To write any internal communication:

1. **Identify the communication type** from the request
2. **Load the appropriate guideline file** from the `examples/` directory:
    - `examples/3p-updates.md` - For Progress/Plans/Problems team updates
    - `examples/company-newsletter.md` - For company-wide newsletters
    - `examples/faq-answers.md` - For answering frequently asked questions
    - `examples/general-comms.md` - For anything else that doesn't explicitly match one of the above
3. **Follow the specific instructions** in that file for formatting, tone, and content gathering

If the communication type doesn't match any existing guideline, ask for clarification or more context about the desired format.

## Keywords
3P updates, company newsletter, company comms, weekly update, faqs, common questions, updates, internal comms

## Related skills in this repo

- **doc-coauthoring**: Use that skill instead when the piece is a long-form, iteratively-refined document (a spec, proposal, or policy) rather than a short-format update covered by this skill's `examples/` guides.
- **quarterly-okr-architect** / **business-intelligence-report** / **ceo-reporting-skill**: Good sources of content for a leadership update or status report — draft the analysis there, then use this skill's formats to communicate it internally.
- **stakeholder-engagement-matrix**: Decides *who* gets *how much* of a given communication and how often (Power/Interest quadrant) — use that first when a project has multiple stakeholder types, then this skill's formats to draft each one.
- **docx**: Produce a formal internal memo/update as an actual Word file when a plain message isn't sufficient.
