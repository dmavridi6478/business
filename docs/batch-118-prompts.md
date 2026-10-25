# Batch 118 prompts (plain text, copy and paste)

Sources: the Nicolas Boucher Excel/PPT infographic (prompts 1 to 10, verbatim), the Eric Partaker sales-growth graphic, the @aigenesis.official Unsloth carousel. Prompts 11 to 14 are original.

## 1 to 10. Excel and PowerPoint (verbatim; run in Excel or PowerPoint with Copilot or Claude)

1. Build a waterfall chart in a new sheet showing the bridge from [START VALUE] to [END VALUE]. Bars for: [DRIVER 1], [DRIVER 2], [DRIVER 3]. Color positive bars [COLOR] and negative bars [COLOR].
2. Build a rolling 12-month dashboard on a new tab. Pull revenue, gross margin %, EBITDA, and headcount from the data in [SHEET NAME]. Update automatically as I add new months to the source data.
3. Scan the '[SHEET NAME]' tab for cells that violate data validation rules. List the cell address, the expected format, and what is currently there. Group by column.
4. Build formulas to match PO numbers in [SHEET 1] to invoice numbers in [SHEET 2] to payment references in [SHEET 3]. Flag every row where the amounts do not match within [TOLERANCE].
5. Build a KPI scorecard tab with [NUMBER] metrics. For each: actual, target, variance, variance %, and a RAG status (red/amber/green based on [THRESHOLDS]). Pull actuals from [SHEET NAME].
6. Reformat the raw P&L in [SHEET NAME] to match the board template layout. Apply currency formatting, freeze the header row, bold the subtotals, and add a print area for A4 landscape.
7. In [SHEET NAME], identify all intercompany transactions between [ENTITY 1] and [ENTITY 2]. Sum the balances and build elimination entries in a new tab with debit, credit, account, and entity columns.
8. Review the slide deck attached. For each slide, confirm: does the title match the content, is there one clear message, and is the data traceable to a named source? Flag every gap.
9. Build a one-page summary slide for [TOPIC]. Include: headline number, 3 key drivers, 1 risk, and 1 recommendation. All in under [X] words. Board-ready format.
10. Build a summary table showing how [OUTPUT METRIC] changes when [ASSUMPTION 1] moves from [LOW] to [HIGH] and [ASSUMPTION 2] moves from [LOW] to [HIGH]. Format as a heat map with green/red shading.

Add to any of them: "Work on a copy, use live formulas, and show a tie-out check at the end." Slash command: `/excel-ppt-prompt`.

## 11. Sales growth diagnostic (original; 4 multipliers)

My sales per [period] come from [leads] leads, a [conversion %] conversion rate, an average deal size of [amount] and a [retention %] retention rate. Compute baseline sales = leads x conversion x deal size x retention and show the arithmetic. Test a 10% gain on each lever alone and on all four together. Which lever is weakest and why? Propose one two-week test for it with a metric and a stop rule. Tell me where the formula does not fit my business model. Do not quote benchmarks I did not give you. Slash command: `/sales-growth-check`.

## 12. Run a model locally with Unsloth (original)

I have a [GPU model and VRAM, or "no GPU"], [OS] and Python [version]. Give me the current install steps from the Unsloth documentation, a minimal script to load [model name] in 4-bit and run one prompt, the expected memory use, and what to do if it runs out of memory. Tell me which parts of your answer you could not verify against the docs.

## 13. Fine-tune plan with an evaluation gate (original)

I want a model to do [task] in [format]. Before any training, list what I should try first (prompting, retrieval), the evaluation set I need (size, how to build it, the pass mark), the dataset licence and privacy checks, and the chat template I must reuse when serving. Then give the smallest LoRA fine-tune plan with one hyperparameter table, and the GGUF export call with `save_pretrained_gguf`. Stop and ask me for the evaluation set before writing training code.

## 14. Record a 30-second demo (original)

My app does [one sentence]. Write a 30-second demo script as: the one action to show, the exact steps and clicks, what to zoom into, what to say in under 60 words, and what customer data must be hidden. Then tell me which tool fits (VHS for a terminal, a screen recorder with auto-zoom for a GUI, a click-through tool for a tour) and give the first command or setting to use.
