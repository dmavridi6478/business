---
name: sell-unused-things-prompts
description: The five-step prompt sequence from the @dotdevs "Selling unused things? Let ChatGPT help" carousel, adapted for any AI assistant - start with clear photos, research the value from recent sold listings, draft the listing from confirmed facts only, prepare the marketplace post for your approval, and draft buyer replies while you approve commitments, payments and collection details - with the approval gates kept and scam-safety rules added. Use when someone wants to sell a second-hand item, a small business wants to clear stock, or an assistant must be set up so it never publishes or promises anything unapproved.
---

# Selling unused things with an AI assistant

Source: a six-slide carousel (cover, "start with clear photos", steps 1 and 2, steps 3 and 4). The slides show the Claude and ChatGPT logos and say ChatGPT; the text works in any assistant that can read photos. The wording of each step below follows the slides; the safety rules in the last section are my additions.

## The sequence

| Step | What you ask | Slide wording |
|---|---|---|
| 0. Start with clear photos | Take the photos yourself | Photograph the item, model number, condition and any defects. Remove private information. |
| 1. Research the value | Price evidence | Identify [item] and compare recent comparable sold listings. Link the evidence and note uncertainty. |
| 2. Draft the listing | Title and description | Write a clear title and description using only the condition and details I have confirmed. |
| 3. Review the public listing | Marketplace-ready draft | Prepare the photos and draft for the chosen marketplace. I will approve the price and publish. |
| 4. Handle buyer questions | Replies and negotiation | Draft replies and negotiation options. Let me approve commitments, payments and collection details. |

The pattern worth keeping is the gate in steps 3 and 4: the assistant prepares, you decide the price, publish and every commitment.

## One prompt to paste

```
I want to sell [item]. Work in four steps and stop after each one for my OK.
1. Identify the item from my photos and compare recent comparable SOLD listings (not asking prices). Link every source and say how uncertain the price range is.
2. Write a clear title and description using only the condition and details I have confirmed. Ask me about anything you cannot see.
3. Prepare the photos and draft for [marketplace]. I will approve the price and publish. Do not post anything.
4. When buyers write, draft replies and negotiation options. I approve every commitment, payment and collection detail. Never share my address, phone number or payment details.
```

## Safety rules (my additions)

- **Photos:** check for names, addresses, serial numbers tied to accounts, reflections and background documents before uploading.
- **Prices:** "sold" prices are evidence; asking prices are not. A range from two or three sold items is weak; say so in the listing decision.
- **Honesty:** describe defects the photos show. An assistant must not invent condition, accessories or warranty.
- **Payment:** prefer in-platform payment or cash on collection. Treat requests to pay or be paid outside the platform, overpayment offers, or couriers arranged by the buyer as warning signs.
- **Collection:** meet in a public place; the assistant should never receive or store your home address.
- **Rules:** each marketplace has its own prohibited-items and fee rules; check them before step 3.
- **Business stock:** invoicing, VAT and consumer-rights obligations differ from private sales; this skill does not cover them.

## Use

`/sell-listing [item]` runs the sequence one step at a time and writes nothing outside the chat. It never publishes, messages a buyer or spends money.
