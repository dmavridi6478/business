# Procedure: Building a Personal Voice Skill

## When this applies

The user wants Claude to consistently write in *their* actual voice —
not a generic AI tone — across future drafts, without re-explaining their
preferences every time. Use Anthropic's own Skill Creator tool for this
(already available in a standard Claude Code setup — not vendored into
this repo, since it's Anthropic's own meta-tool for building skills, the
same category as `claude-code-tooling`'s standalone-software entries).

## Steps

1. **Gather source material before starting.** Collect:
   - The user's strongest published posts/writing (3-5 real examples, not
     paraphrased from memory)
   - Specific phrases or words the user avoids or dislikes
   - Their preferred structure (short punchy sentences? long-form? lists?)
   - Examples that clearly show their tone (formal vs. casual, direct vs.
     warm, technical vs. plain-language)
   - Formatting rules (em dashes, headers, emoji use, capitalization
     conventions)
   - Audience context (who they're usually writing to)

2. **Don't fabricate examples.** If the user hasn't supplied real writing
   samples, ask for them rather than inventing "the user's voice" from a
   generic assumption — a voice skill built on invented examples teaches
   Claude the wrong voice with false confidence.

3. **Invoke Skill Creator** with a name (e.g. `my-voice`) and description
   (e.g. "My writing voice, preferences, rules, and structure"). Default to
   **private** visibility — this captures personal writing style, not
   something to publish.

4. **Structure the output** the same way this repo's own skills are
   structured, since the pattern is identical:
   - `SKILL.md` — the core voice description (tone, structure, principles)
   - `examples/` — the real writing samples that ground the voice, kept
     verbatim
   - `rules.md` — explicit do/don't formatting and phrasing rules

5. **Verify it before relying on it.** Generate one test draft using the
   new skill and check it against the real examples — does it actually
   sound like the person, or like a plausible-but-generic approximation?
   If it drifts, add a more specific example or rule rather than
   broadening the description.

6. **Reuse, don't rebuild.** Once saved, this skill should be the default
   voice for the user's future drafts (posts, emails, scripts) — apply it
   automatically alongside `humanizer` rather than asking the user to
   re-specify their voice preferences each time.

7. **Revisit periodically.** A voice skill built from a handful of
   examples can drift out of date as the person's style evolves — treat
   it as a living reference to refresh with new strong examples, not a
   one-time setup.

## Related skills in this repo

- **humanizer**: Run after drafting with the voice skill — a voice skill defines *whose* voice to write in, `humanizer` removes generic AI-writing tells that can creep in regardless of whose voice is targeted.
- **copywriting**: The Problem→Promise→Proof→CTA framework there is the structural layer; a personal voice skill is the tone/style layer — use both together for persuasive copy that also sounds like a specific person.
- **content-repurposing-service**: A natural place to apply a personal voice skill — the same person's voice should carry consistently across the 7-asset content pack that skill produces.
