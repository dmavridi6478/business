---
description: Turn one carousel/reel into native posts for up to 9 platforms through the Blotato connector - drafts first, nothing scheduled without a yes
argument-hint: <paste the content or file path, platforms, day and time>
---

Use skill `blotato-nine-platform-posting`. Input: "$ARGUMENTS".
1. Check the Blotato connector is authenticated and the plan is paid; if not, stop and tell the user what to do.
2. List accounts, read the media (must be a public URL), then draft one post per platform in its native format with the required fields (TikTok privacy + AI label, YouTube title + privacy, Pinterest board, Facebook page).
3. Show all drafts in one table with character counts. Run claims through `docs/marketing-context/proof.md` and `banned.md`.
4. Wait for an explicit approval of text, platform and time. Only then schedule; report only what the tool confirms.
