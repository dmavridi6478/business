Load the user's saved personal/working context from `docs/about-me.md` and
apply it to the rest of this conversation.

1. Read `docs/about-me.md`.
2. **If it doesn't exist yet**, say so and offer to create it: ask the user
   directly for (a) who they are / their role, (b) current priorities or
   what they're working on right now, (c) working style and tone
   preferences, and (d) what "good" looks like for the kind of output they
   usually want from Claude. Write their actual answers to
   `docs/about-me.md` verbatim — never invent or template-fill placeholder
   content on their behalf.
3. **If it exists**, treat its contents as standing context for this
   conversation from this point forward. Apply it silently to how you
   answer — don't restate the file's contents back to the user unless they
   ask to see it.
4. This context loads only when `/about-me` is explicitly invoked, not on
   every message — that's deliberate. Keeping it out of the global/always-on
   context keeps answers sharp and task-specific instead of anchored to the
   same personal framing on every unrelated task; invoke it again in a new
   conversation whenever that context is actually relevant.
5. If the user's request in the same message conflicts with something in
   `docs/about-me.md` (e.g. a stated preference), the explicit request in
   the message wins — the file is background context, not an override.
