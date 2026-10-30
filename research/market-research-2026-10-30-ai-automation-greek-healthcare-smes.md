All dates in this report are as of the run date, 2026-10-30. This is research, not legal advice. Every regulatory point below needs a Greek lawyer's or accountant's check before it is published or relied on.

Conventions. VERIFIED means I opened the document or data in this run and read the statement or figure cited. UNVERIFIED means the source could not be opened, did not contain the figure, appeared only in a search-result summary, or was not re-opened in this run. Unverified figures appear only in the Sources table and the "Not verified" list, never as facts. "Inference" marks my own reasoning. Labels S1, S2 and so on refer to the Sources table.

## Research topic

Topic: AI automation for Greek healthcare SMEs. Audience: owners of small healthcare businesses in Greece: private medical and dental practices, small clinics, diagnostic and physiotherapy centres, pharmacies and small medical-supply firms.

Method and limits of this run:

- Searches ran in English and Greek with WebSearch. No WebFetch tool was available in this session, so I opened sources with command-line HTTP requests. Perplexity was not connected. EUR-Lex returns an empty response (HTTP 202) to scripted requests, so I read the Official Journal texts through the EU Publications Office (Cellar) full-text service. AADE returned HTTP 403 and e-nomothesia reset the connection again this run.
- Baseline for "what changed": no file matching research/market-research-*-ai-automation-greek-healthcare-smes.md exists on this branch (the research/ directory did not exist before this run), and docs/about-me.md is an unfilled template. The only previous report is the Notion page 40828b58-08a5-8143-a2de-c0ea424a17b1 as it stood before this update (titled 2026-10-28, last edited 2026-10-29, run date 2026-10-29). I read it and used it as the baseline. It is one day old.
- The skill file .claude/skills/ai-market-research-engine/SKILL.md does not exist in this repository. I followed the written task instructions instead.

## Main findings

### A. What changed since the previous report (2026-10-29)

The gap is one day, so little has moved. Every verified fact in the previous report's section B was re-opened in the primary text and held. Differences:

| Item | Status now | What changed |
| --- | --- | --- |
| Final text of Regulation (EU) 2026/1744 | Resolved (unchanged) | Re-read in the Official Journal text. All dates and the Article 4 wording match the previous report. EUR-Lex itself still cannot be opened (HTTP 202), so its status field remains unchecked. |
| EHDS application dates, Article 105 | Resolved (unchanged) | Article 105 re-read. 26 March 2027 general; 2029 and 2031 staging confirmed. |
| Decision A.1197/2026: clinics, B2C receipts, EOPYY billing | Partly resolved, with one new source | New this run: an EOPYY announcement (republished by OENET, 5 January 2026) shows EOPYY is set up as an e-invoicing contracting authority and gives invoicing coordinates for "all categories of Other Providers and Private Pharmacies" for 2026 (B6). The decision texts still do not mention healthcare. Whether the mandate applies to a given provider is still unanswered. |
| Greek no-show data | Not resolved | Another English search found no Greek figure; only non-Greek studies in search summaries. |
| Healthcare breakdown of AI adoption | Not resolved | A Eurostat query for NACE Q (human health and social work) returned an empty data set again. A search for ELSTAT's 2025 ICT-in-enterprises results returned nothing usable. |
| Law 5302/2026, Article 92 | Re-read in part | The "Ψηφιακός Βοηθός Πολίτη" and "Ψηφιακός Βοηθός Ιατρού" provisions were re-read. Paragraphs 2 to 5 (booking platform, impact assessments) were not re-opened this run. |

Top changes, in order: (1) new EOPYY e-invoicing evidence (B6); (2) the size-class and all-sector Eurostat figures were re-pulled and match; (3) the e-invoicing start, 2 November 2026, is now two days away.

### B. Verified facts this run

1. Regulation (EU) 2026/1744 (Digital Omnibus on AI) amends Regulation 2024/1689 (AI Act) and others. Article 113 as amended: Chapter III, Sections 1 to 3 apply from 2 December 2027 for high-risk systems under Article 6(2) and Annex III, and from 2 August 2028 for those under Article 6(1) and Annex I (S1). Annex I covers product legislation, which is where medical-device AI sits (inference). Articles 102 to 110 apply from 27 July 2026 (S1). Publication date 24 July 2026 and the 27 July 2026 entry into force were read in the previous run; the entry-into-force clause was not re-read in this run.
2. Article 4 (AI literacy), as replaced: the text states the obligation "does not require providers or deployers to guarantee any specific level of AI literacy of any individual", and the Commission and Member States must support providers and deployers, "in particular SMEs" (S1). Inference: a clinic that uses AI still has a duty, but a lighter one.
3. Article 50 transparency: the previous run found no postponement of Article 50(1) and a 2 December 2026 grace for Article 50(2) marking by earlier-placed generative systems. I did not re-read those provisions this run. Treat as carried forward. A lawyer must confirm which duties fall on a clinic as deployer.
4. EHDS, Regulation (EU) 2025/327, Article 105 (S2): applies from 26 March 2027. Articles 3 to 15, 23(2) to (6), 25, 26, 27, 47, 48 and 49 apply from 26 March 2029 for priority categories of health data under Article 14(1)(a) to (c) and the EHR systems that process them, and from 26 March 2031 for categories (d) to (f). Further dates run from delegated acts. Inference: a small practice faces no EHDS data-exchange duty before 2029, but should ask EHR vendors about their plans now. Entry into force is the twentieth day after publication; secondary sources give 25 or 26 March 2025 (see Conflicts).
5. Eurostat, dataset isoc_eb_ai, indicator E_AI_TANY, percent of enterprises, Greece (S5; Eurostat file updated 2026-06-15). Coverage: enterprises with 10 or more employees, all activities excluding agriculture, mining and finance. Micro practices (0 to 9) are not measured. A query for NACE Q returned no values, so there is no healthcare breakdown.

   | Group | 2021 | 2023 | 2024 | 2025 |
   | --- | --- | --- | --- | --- |
   | Greece, 10+ employees | 2.61 | 3.98 | 9.81 | 8.93 |
   | EU27, 10+ employees | 7.65 | 8.06 | 13.48 | 19.95 |
   | Greece, 10 to 49 | 1.97 | 3.54 | 8.20 | 7.33 |
   | Greece, 50 to 249 | 7.53 | 5.68 | 15.91 | 15.18 |
   | Greece, 250+ | 9.85 | 13.96 | 24.27 | 37.58 |

   Greece fell 0.88 points from 2024 to 2025 while the EU rose 6.47; the 2025 gap is 11.02 points (my arithmetic).
6. E-invoicing. Decision A.1197/2026 (ΦΕΚ Β' 5905, 30 September 2026) replaces Article 2(2) of A.1128/2025 (S3). From 2.11.2026, second-period entities must issue electronic invoices only, for sales and services under Article 1(1) limbs (a) to (c). From 2.11.2026 to 31.1.2027 they may in parallel use ERP issuance or the AADE form under A.1138/2020. Article 1 of A.1128/2025 (S4) limits the mandate to (a) domestic sales to entities under Law 4308/2014 (B2B), (b) sales to non-EU foreign entities, excluding retail, and (c) public contracts and other spending of General Government bodies (B2G). Neither text mentions healthcare, doctors, clinics, pharmacies or EOPYY (keyword search of both texts, run this time). New: an EOPYY announcement dated 5 January 2026 (S6, republished by OENET) lists the e-invoicing identifiers for 2026: an ΑΔΑ valid for all categories of Other Providers and Private Pharmacies, EOPYY's ΑΑΗΤ number, tax number and tax office, and budget type "3". Inference: EOPYY invoicing is already organised as electronic invoicing to a contracting authority, which points to limb (c), but the announcement does not say that providers are obliged or from when. Receipts to private patients (domestic B2C) are not among the three listed categories (my reading). Flag for an accountant.
7. Law 5302/2026, Article 92 (S7): the Ministry of Health may operate AI applications "Ψηφιακός Βοηθός Πολίτη" in myHealth and "Ψηφιακός Βοηθός Ιατρού" in myHealthDoc, both integrated in the Individual Electronic Health Record (Α.Η.Φ.Υ.). Whether these are live was not verified.

### C. Implications for the audience (inference)

- The regulatory timeline is fixed enough to publish: Annex III high-risk duties in December 2027, device-type AI in August 2028, EHDS data-exchange duties from 2029. The nearest hard date for owners is not an AI date: e-invoicing on 2 November 2026.
- The Eurostat result supports a market-timing point: Greek enterprise AI use is low and slipped in 2025 while the EU accelerated. It is not a healthcare figure and excludes micro practices.
- Still missing: Greek no-show data, healthcare-specific adoption data, and an official statement of e-invoicing scope for clinics and EOPYY billing. A neutral publisher could fill these with an owner survey.

### D. Carried forward, not re-verified in this run

Owner pain points (EOPYY platforms, e-prescription, clawback, payment delays), HDPA fines, Law 5321/2026 on national AI supervision, the Digital4u price sheet, Kalimera.ai vendor figures, the European Patients' Forum survey, the ILSP Krikri model, medical-tourism figures and health-spending shares. These come from the previous report only. Treat them as UNVERIFIED for this run.

## Conflicts

1. EHDS entry into force: the Regulation says the twentieth day after publication (5 March 2025), which is 25 March 2025 by count (S2, my arithmetic). Most secondary sources give 26 March 2025; one lists 25 March 2025 (eumonitor, search summary, S11). Immaterial: the application dates in Article 105 are fixed calendar dates.
2. AI Act timing for medical-device AI: older articles show 2 August 2027. The adopted text says 2 August 2028 for Annex I and 2 December 2027 for Annex III (S1). The adopted text governs.
3. E-invoicing start dates: official text says 2 November 2026 with transition to 31 January 2027 (S3). Search-result reports give 1 October 2026 with transition to 31 December 2026, and a provider-based start of 1 March 2027 (S8, S9, unverified). The official text governs. I could not check whether AADE changed the dates after 30 September 2026 (AADE returned HTTP 403).
4. Greek AI adoption: Eurostat gives 9.81% for 2024 and 8.93% for 2025 (S5). No source I opened gives a healthcare-specific figure, so no healthcare adoption claim can be made.
5. No-show rates: search summaries give 15 to 23% in non-Greek settings (Geneva 15.8%, Çorum 16.2%, a Brazilian review average of 23%) (S10, unverified). None is Greek and none was opened, so no rate can be quoted for Greece.

## Content ideas

Ranked by urgency and strength of verified evidence. Each piece should carry source dates and state that it is not legal advice.

1. "2 November: what Greek e-invoicing says and does not say about your practice." Verified dates and three listed categories (S3, S4), plus the EOPYY identifiers announcement (S6). Be explicit that the texts are silent on clinics, pharmacies and EOPYY obligations, and send readers to their accountant. Publish before 2 November 2026.
2. "The AI Act for a Greek clinic, now that the text is final." Dates from Regulation 2026/1744 (S1) and the softened Article 4. A regulatory adviser must check device-type tools and which duties fall on the clinic.
3. "Greece's enterprise AI use is 8.93% and fell in 2025." Eurostat (S5). State the 10+ employee scope, all sectors, no healthcare split.
4. "The state is putting AI into the health record: what private practices should watch." Law 5302/2026 Article 92 (S7). Do not claim the tools are live.
5. "EHDS for small practices: 2027, 2029, 2031." Article 105 (S2). Frame as a question list for EHR vendors.
6. "Missed calls are not no-shows: measure before you buy." No Greek data exists in what I found; offer a one-week self-audit or an owner survey to create the Greek benchmark.

## Sources

Type: P = primary, S = secondary. Mark and date as of 2026-10-30.

| ID | Publisher and document | Date | URL | Mark |
| --- | --- | --- | --- | --- |
| S1 | EU Publications Office, Official Journal: Regulation (EU) 2026/1744, full text (P) | Adopted 2026-07-08; opened 2026-10-30 | http://publications.europa.eu/resource/cellar/b459c07f-86fb-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1 | VERIFIED |
| S2 | EU Publications Office, Official Journal: Regulation (EU) 2025/327 (EHDS), full text including Article 105 (P) | Published 2025-03-05; opened 2026-10-30 | http://publications.europa.eu/resource/cellar/531b8c37-f962-11ef-b7db-01aa75ed71a1.0006.03/DOC_1 | VERIFIED |
| S3 | Taxheaven: Α.1197/2026, ΦΕΚ Β' 5905 (S, publishes decision text) | 2026-09-30; opened 2026-10-30 | https://www.taxheaven.gr/circulars/55463/a-1197-2026 | VERIFIED |
| S4 | Taxheaven: Α.1128/2025, Articles 1 and 2 (S, publishes decision text) | 2025-09-15; opened 2026-10-30 | https://www.taxheaven.gr/circulars/51018/a-1128-2025 | VERIFIED |
| S5 | Eurostat: isoc_eb_ai, E_AI_TANY, API responses for Greece and EU27 and four size classes; NACE Q query empty (P) | File updated 2026-06-15; opened 2026-10-30 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_eb_ai?format=JSON&lang=en&indic_is=E_AI_TANY&unit=PC_ENT&geo=EL&geo=EU27_2020&size_emp=GE10 | VERIFIED |
| S6 | OENET (republishing an EOPYY announcement): e-invoicing identifiers for 2026 for providers and private pharmacies (S) | 2026-01-05 (modified 2026-02-03); opened 2026-10-30 | https://www.oenet.gr/τελευταία-νέα/φορολογικά-οικονομικά/item/131842-eopyy-anakoinosi-pros-paroxous-promitheutes-ipiresion-ygeias-gia-tin-ilektroniki-timologisi | VERIFIED (page text read; the original EOPYY file was not opened) |
| S7 | Taxheaven: Law 5302/2026, Article 92 (S, publishes law text) | Opened 2026-10-30; law date not shown | https://www.taxheaven.gr/law/5302/2026/arthro/92 | VERIFIED for the two named assistants; later paragraphs not re-read |
| S8 | Ta Nea: e-invoicing, second group from 1 October 2026 | 2026-01-15 | https://www.tanea.gr/2026/01/15/economy/erxontai-ta-ilektronika-timologia-ti-allazei-stis-synallages-ton-epixeiriseon/ | UNVERIFIED (not opened; superseded by S3) |
| S9 | Powergame: provider-based e-invoicing start reported as 1 March 2027 | Undated | https://www.powergame.gr/?p=1408592 | UNVERIFIED (search summary only) |
| S10 | Folia (Geneva University Hospitals no-show study) and PMC12345966 (northern Italy) | Undated; 2025 | https://folia.unifr.ch/global/documents/21173 ; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12345966/ | UNVERIFIED (search summaries only; non-Greek) |
| S11 | EU Monitor: Regulation 2025/327 key dates | Undated | https://www.eumonitor.eu/9353000/1/j9vvik7m1c3gyxp/vmlg5gptv7zp | UNVERIFIED (search summary only) |
| S12 | EUR-Lex: Regulation (EU) 2026/1744 | 2026-07-24 | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | UNVERIFIED (empty response, HTTP 202; same text read via S1) |
| S13 | AADE: Α.1197 / 30-09-2026 | 2026-09-30 | https://www.aade.gr/egkyklioi-kai-apofaseis/1197-30-09-2026 | UNVERIFIED (HTTP 403) |
| S14 | e-nomothesia: Α.1197/2026 | 2026-09-30 | https://www.e-nomothesia.gr/kat-oikonomia/koine-upourgike-apophase-a1197-2026.html | UNVERIFIED (connection reset) |

Counts: 14 sources listed; 7 VERIFIED and 7 UNVERIFIED.

Not verified:

- EUR-Lex pages themselves (S12), including the legal-status field.
- Whether the 2 November 2026 date or the 31 January 2027 transition changed after 30 September 2026 (AADE and e-nomothesia unreachable).
- Scope of Article 1 of Law 4308/2014: whether sole practitioners, pharmacies, medical-supply firms and clinics are within it. The law was not read.
- Whether invoices to EOPYY are B2G under limb (c), and whether providers are obliged to issue them electronically from 2 November 2026. The original EOPYY announcement was not opened.
- E-invoicing penalty amounts.
- Healthcare-specific AI adoption from any source; ELSTAT's 2025 ICT survey was not found.
- Any Greek no-show rate; the non-Greek rates in S10 were not opened.
- Whether the AI assistants in Law 5302/2026 Article 92 are live, the law's date and ΦΕΚ reference, and paragraphs 2 to 5.
- The publication date and entry-into-force clause of Regulation 2026/1744, and the Article 50 provisions: carried from the previous run, not re-read.
- HDPA guidance on AI and health data.
- Everything in item D of Main findings.
