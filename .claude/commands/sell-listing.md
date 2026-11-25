---
description: Prepare a second-hand sale one step at a time (value research, listing, marketplace draft, buyer replies) - never publishes, messages a buyer or spends money
argument-hint: [item to sell, and the marketplace if you know it]
---

Input: "$ARGUMENTS". If empty, ask what is being sold and where.

Use `.claude/skills/sell-unused-things-prompts/SKILL.md`. Work in four steps and stop after each one for the user's OK.

1. Ask for clear photos (item, model number, condition, defects, no private information). Identify the item and compare recent comparable SOLD listings, not asking prices. Link every source and state how uncertain the range is; two or three sales is a weak range.
2. Write a clear title and description using only the condition and details the user confirmed. Ask about anything the photos do not show. Never invent condition, accessories or warranty.
3. Prepare the photos and draft for the chosen marketplace. The user approves the price and publishes. Do not post anything.
4. When buyers write, draft replies and negotiation options. The user approves every commitment, payment and collection detail. Never share an address, phone number or payment details, and flag off-platform payment, overpayment offers and buyer-arranged couriers as warning signs.

Write nothing outside the chat. End with `Not verified:` for any price or marketplace rule not read from a source.
