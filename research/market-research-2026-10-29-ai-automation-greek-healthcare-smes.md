All dates in this report are as of the run date, 2026-10-29. This is research, not legal advice. Every regulatory point below needs a Greek lawyer's or accountant's check before it is published or relied on.

Conventions. VERIFIED means I opened the document or data and read the statement or figure cited. UNVERIFIED means the source could not be opened, did not contain the figure, or appeared only in a search-result summary. Unverified figures appear only in the Sources table and the "Not verified" list, never as facts. "Inference" marks my own reasoning. Source labels (S1, S2 and so on) refer to the Sources table.

## Research topic

Topic: AI automation for Greek healthcare SMEs. Audience: owners of small healthcare businesses in Greece: private medical and dental practices, small clinics, diagnostic and physiotherapy centres, pharmacies and small medical-supply firms.

Method and limits of this run:

- Searches ran in English and Greek with WebSearch. No WebFetch tool was available, so I opened sources with command-line HTTP requests. Perplexity was not connected. EUR-Lex pages return an empty response to scripted requests (HTTP 202). I therefore read the Official Journal texts through the EU Publications Office (Cellar) full-text service, which serves the same Official Journal documents. AADE's site returned HTTP 403 and e-nomothesia reset the connection.
- Baseline for "what changed": no file matching research/market-research-*-ai-automation-greek-healthcare-smes.md exists on this branch (the research/ directory did not exist), and docs/about-me.md is an unfilled template. The only previous report I could find is the existing Notion page 40828b58-08a5-8143-a2de-c0ea424a17b1 (titled 2026-10-28, last edited 2026-10-29). I read it and used it as the baseline. I did not re-verify its other findings in this run (see item D).
- The skill file .claude/skills/ai-market-research-engine/SKILL.md does not exist in this repository. I followed the written task instructions instead.

## Main findings

### A. What changed since the previous report

| Open item from the previous report | Status now | What changed |
| --- | --- | --- |
| Final text of Regulation (EU) 2026/1744 | Resolved (read in full) | Official Journal text opened via the Publications Office. See B1 to B4. The previous report relied on law-firm summaries. |
| EHDS application dates, Article 105 | Resolved (read in full) | Article 105 text opened. General application 26 March 2027, with staged dates in 2029, 2031 and 2035. See B5. This settles the conflict the previous report left open. |
| E-invoicing decision A.1197/2026: clinics, B2C receipts, EOPYY billing | Partly resolved | The decision text and the codified base decision A.1128/2025 were read. Neither mentions healthcare, clinics or EOPYY. Domestic retail (B2C) sales are not in the listed categories (my reading). EOPYY billing remains unresolved. See B6. |
| Greek no-show data | Not resolved | Two more searches found no Greek figure. Only international benchmarks, which I did not open. |
| Healthcare breakdown of AI adoption | Not resolved, but now documented | Eurostat's enterprise AI table was decoded correctly this time. It carries no healthcare (NACE Q) breakdown. Greece's all-sector figure is now verified: 8.93% in 2025, down from 9.81%. See B7. |
| New this run | Law 5302/2026, Article 92 | A statute now authorises AI in the national health record and in the national appointment platform. See B8. |

### B. Verified facts this run

1. Regulation (EU) 2026/1744 (Digital Omnibus on AI) is dated 8 July 2026 and was published in the Official Journal on 24 July 2026. It amends Regulations 2024/1689 (AI Act), 2018/1139 and 2023/1230 (S1, S2). It enters into force on the third day after publication (S1). By calendar count that is 27 July 2026 (my arithmetic), the date the previous report used.
2. Application dates in the amended AI Act, Article 113 (S1): high-risk systems under Article 6(2) and Annex III apply from 2 December 2027. High-risk systems under Article 6(1) and Annex I apply from 2 August 2028. Annex I covers product legislation, which is where medical-device AI sits (inference). High-risk systems intended for use by public authorities must comply by 2 August 2030.
3. Article 4, AI literacy, is replaced (S1). Providers and deployers must "take measures to support the development of AI literacy" of staff and others using AI on their behalf, taking context into account. The text states this "does not require providers or deployers to guarantee any specific level of AI literacy of any individual". The Commission and Member States must support providers and deployers, "in particular SMEs", including by publishing practical examples. Inference: the duty still applies to a clinic that uses AI, but it is lighter than the original wording. The previous report could not verify this wording.
4. Article 50 transparency. The amending text adds only a transitional rule: providers of generative systems that produce synthetic audio, image, video or text and were placed on the market before 2 August 2026 must comply with Article 50(2) (machine-readable marking) by 2 December 2026 (S1). I found no amendment postponing Article 50(1), which requires users to be told they are interacting with an AI system. Inference: the previous report's statement that Article 50 applies from 2 August 2026 stands for patient-facing chatbots and voice agents, and the 2 December 2026 grace applies to marking of generated content by earlier-placed systems. A lawyer must confirm which duties fall on a clinic as deployer and which on the vendor as provider. Separately, Article 63 now lets all SMEs (not only microenterprises) simplify parts of the quality-management system for high-risk AI. That binds providers of high-risk systems, so it matters to vendors more than to clinics (S1).
5. EHDS, Regulation (EU) 2025/327, Article 105 (S3). The Regulation enters into force on the twentieth day after publication (5 March 2025), which is 25 March 2025 by calendar count (my arithmetic). The previous report cited 26 March 2025 from a Commission page; the difference is one day and does not affect the application dates. Application: the Regulation applies from 26 March 2027. Articles 3 to 15, 23(2) to (6), 25, 26, 27, 47, 48 and 49 apply from 26 March 2029 for the first three priority categories of health data and the EHR systems that process them, and from 26 March 2031 for the next three. Chapter III (EHR systems) applies from 26 March 2031. Chapter IV (secondary use) applies from 26 March 2029, with listed exceptions from 26 March 2027 and 26 March 2031, and Article 75(5) from 26 March 2035. Inference: a small practice faces no EHDS data-exchange duty before 2029, but should ask EHR vendors about their EHDS plans now.
6. E-invoicing (S4, S5). Decision A.1197/2026 (joint decision, ΦΕΚ Β' 5905, 30 September 2026) replaces Article 2(2) of A.1128/2025. From 2 November 2026, "second period" entities must issue only electronic invoices. From 2 November 2026 to 31 January 2027 they may use the older methods in parallel (ERP issuance, or the AADE form), provided they filed a start declaration or a declaration of use of the AADE timologio application dated no later than 2 November 2026. Scope under Article 1 of A.1128/2025 (S5): entities within Article 1 of Law 4308/2014 issue e-invoices exclusively for (a) domestic sales to an entity subject to that law (B2B), (b) sales to a foreign entity outside the EU, excluding retail, and (c) public contracts and other spending of General Government bodies (B2G). The first period covers entities with gross revenue above €1,000,000 per their 2023 income tax return (from 2 March 2026); the second period covers all other entities. The text I read does not mention healthcare, clinics, doctors, pharmacies or EOPYY (search of both texts returned no match). Inference: receipts issued to private patients (domestic B2C) are not among the three listed categories. Whether invoices to EOPYY fall under limb (c), and whether a given practice, pharmacy or supply firm is within Article 1 of Law 4308/2014, are not answered by these texts. Flag for an accountant. Time-sensitive: 2 November 2026 is four days after the run date.
7. AI adoption in Greek enterprises, Eurostat dataset isoc_eb_ai, indicator E_AI_TANY (any AI technology), percent of enterprises (S6). Coverage as served: enterprises with 10 or more employees, all activities excluding agriculture, mining and finance (NACE C10-S951_X_K). No values were returned for 0 to 9 employees, so micro practices are not measured. A query for NACE Q (human health and social work) returned no category, so there is no healthcare breakdown in this dataset. All-sector results:

   | Group | 2021 | 2023 | 2024 | 2025 |
   | --- | --- | --- | --- | --- |
   | Greece, 10+ employees | 2.61 | 3.98 | 9.81 | 8.93 |
   | EU27, 10+ employees | 7.65 | 8.06 | 13.48 | 19.95 |
   | Greece, 10 to 49 | 1.97 | 3.54 | 8.20 | 7.33 |
   | Greece, 50 to 249 | 7.53 | 5.68 | 15.91 | 15.18 |
   | Greece, 250+ | 9.85 | 13.96 | 24.27 | 37.58 |

   Greece fell 0.88 percentage points between 2024 and 2025, while the EU rose 6.47 points. The 2025 gap is 11.02 points (my arithmetic). The previous report marked these figures unverified because it could not decode the response; this run decoded them against the dataset's dimension index and cross-checked the aggregate against a separate query.
8. Law 5302/2026, Article 92 (S7). The Ministry of Health, as controller of the Individual Electronic Health Record (ΑΗΦΥ), may use AI systems. Named applications: "Ψηφιακός Βοηθός Πολίτη" inside the myHealth app, which answers citizens' questions using their own or dependants' records, and "Ψηφιακός Βοηθός Ιατρού" inside myHealthDoc, which lets a treating doctor retrieve a patient's data. AI may also produce aggregated, non-identifiable data. Paragraph 2 extends this to the national digital appointment-booking platform run by ΗΔΙΚΑ (Η.Δ.Υ.Κ.Α. Μ.Α.Ε.) for the Ministry, to help citizens communicate with the platform and get information and answers. The systems must operate in line with the AI Act, GDPR and Law 4624/2019, and ΗΔΙΚΑ must carry out a GDPR Article 35 impact assessment and an algorithmic impact assessment under Article 5 of Law 4961/2022 for each application. I read paragraphs 1 to 4 and the start of paragraph 5. Inference: the state is building AI into the booking layer that private practices connect to, and owners will be compared with it.

### C. Implications for the audience (inference)

- The regulatory timeline is now fixed enough to publish: Annex III high-risk duties in December 2027, device-type AI in August 2028, EHDS data-exchange duties from 2029. The nearest hard dates for owners are not AI dates: e-invoicing on 2 November 2026 and the Article 50 transparency duty already running.
- The Eurostat result supports a market-timing point: Greek enterprise AI use is low and slipped in 2025 while the EU accelerated. It does not show healthcare adoption, and the survey excludes micro practices. Do not present it as a healthcare figure.
- The still-missing evidence is Greek no-show data, healthcare-specific adoption data and EOPYY e-invoicing scope. These are the gaps a neutral publisher can fill, for example with an owner survey.

### D. Carried forward from the previous report, not re-verified in this run

Owner pain points (EOPYY platforms, e-prescription, clawback and payment delays), the HDPA fines, Law 5321/2026 on national AI supervision, the Digital4u price sheet (€700 + VAT setup, €700 + VAT per year), the Kalimera.ai vendor figures, the European Patients' Forum survey, the ILSP Krikri model, medical-tourism figures and health-spending shares. I did not re-open these. Treat them as the previous report's findings with its own VERIFIED marks, not as confirmed by this run.

## Conflicts

1. EHDS dates. Previous report: Commission page with 2029 and 2031 dates against a search summary giving 26 March 2027. Resolved by Article 105 (S3): 26 March 2027 is the general application date, and the data-exchange duties are staged to 2029, 2031 and 2035. Residual discrepancy: entry into force 25 March 2025 by count from the Regulation's text against 26 March 2025 on a Commission page. Immaterial for planning.
2. AI Act timing for medical-device AI. The original 2 August 2027 date and the November 2025 proposal are superseded by the adopted text: 2 August 2028 for Annex I and 2 December 2027 for Annex III (S1). Older articles may still show 2027.
3. Article 50 scope. The previous report said Article 50 transparency obligations applied from 2 August 2026. The amending text confirms no postponement of Article 50(1) but gives earlier-placed generative systems until 2 December 2026 for Article 50(2) marking (S1). The two statements are consistent once the paragraphs are separated. Which paragraph applies to a clinic's tool is for a lawyer.
4. E-invoicing start dates. Official text: 2 November 2026 with a transition to 31 January 2027 (S4, S5). A news report of January 2026 gave 1 October 2026 with a transition to 31 December (S16, unverified), and another report gave 1 March 2027 for the provider-based start (S15, unverified). The official text governs. A search result described the decision as dated 30 September 2026 while Taxheaven lists it under 1 October 2026; the decision text and ΦΕΚ carry 30 September 2026.
5. Greek AI adoption. A Greek briefing pack cited about 9.8% for 2024 (S19, unverified). Eurostat gives 9.81% for 2024 (S6), which matches, and 8.93% for 2025. No source I opened gives a healthcare-specific figure.
6. No-show rates. International figures from search summaries (a European average of 19.3%, other single-centre rates) differ widely by setting (S13, S17, unverified). I did not open them, and none is Greek. No conflict can be resolved without Greek data.

## Content ideas

Ranked by urgency and by strength of verified evidence. Each piece should carry its source dates and state that it is not legal advice.

1. "2 November: what Greek e-invoicing does and does not say about your practice." Verified dates and the three listed categories (S4, S5). Be explicit that the texts are silent on clinics, pharmacies and EOPYY billing, and send readers to their accountant. Publish before 2 November 2026.
2. "The AI Act for a Greek clinic, now that the text is final." Dates from Regulation 2026/1744 (S1): December 2027, August 2028, Article 50 now. Include the softened AI-literacy duty in Article 4. A regulatory adviser must check device-type tools and which duties fall on the clinic.
3. "Greece's AI adoption is 8.93% and fell in 2025: what it means for a small practice." Eurostat (S6). Must state that the data cover enterprises with 10 or more employees, all sectors, and no healthcare split.
4. "The state is putting AI into booking: what private practices should watch." Law 5302/2026 Article 92 (S7). Compare with private booking tools. Do not claim the platform AI is live; I did not verify that.
5. "EHDS for small practices: 2027, 2029, 2031." Article 105 (S3). Frame as an EHR-vendor question list.
6. "Missed calls are not no-shows: measure before you buy." Still no Greek data. Offer a one-week self-audit and consider running an owner survey to create the missing Greek benchmark.
7. "Before you paste patient data into a chatbot." Carried forward (item D): GDPR Article 9 and the HDPA cases. Re-verify before publishing.

Content gaps this run confirmed: no Greek no-show data, no healthcare breakdown of AI adoption, no official statement on EOPYY e-invoicing scope.

## Sources

Verified means I opened the document or data and the cited statement is there. Type: P = primary; S = secondary.

| ID | Publisher and document | Date | URL | Mark |
| --- | --- | --- | --- | --- |
| S1 | EU Publications Office, Official Journal L 2026/1744: Regulation (EU) 2026/1744 (Digital Omnibus on AI), full text (P) | Adopted 2026-07-08; published 2026-07-24 | http://publications.europa.eu/resource/cellar/b459c07f-86fb-11f1-bf5e-01aa75ed71a1.0006.03/DOC_1 | VERIFIED |
| S2 | EU Publications Office: record for CELEX 32026R1744 (title, OJ reference) (P) | 2026-07-24 | https://publications.europa.eu/resource/celex/32026R1744 | VERIFIED |
| S3 | EU Publications Office, Official Journal L 2025/327: Regulation (EU) 2025/327 (EHDS), full text including Article 105 (P) | Adopted 2025-02-11; published 2025-03-05 | http://publications.europa.eu/resource/cellar/531b8c37-f962-11ef-b7db-01aa75ed71a1.0006.03/DOC_1 | VERIFIED |
| S4 | Taxheaven: Α.1197/2026, amendment of Α.1128/2025, ΦΕΚ Β' 5905 (S, publishes decision text) | 2026-09-30 | https://www.taxheaven.gr/circulars/55463/a-1197-2026 | VERIFIED |
| S5 | Taxheaven: Α.1128/2025, codified text, Articles 1 and 2 (S, publishes decision text) | Decision 2025-09-15; page read 2026-10-29 | https://www.taxheaven.gr/circulars/51018/a-1128-2025 | VERIFIED |
| S6 | Eurostat: dataset isoc_eb_ai, indicator E_AI_TANY, API response for Greece and EU27 (P) | Data extracted 2026-10-29; reference years 2021 to 2025 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_eb_ai?format=JSON&lang=en&indic_is=E_AI_TANY&unit=PC_ENT&geo=EL&geo=EU27_2020&size_emp=GE10 | VERIFIED |
| S7 | Taxheaven: Law 5302/2026, Article 92, AI in the Individual Electronic Health Record (S, publishes law text) | Law date not shown on page read | https://www.taxheaven.gr/law/5302/2026/arthro/92 | VERIFIED (paragraphs 1 to 4 read in full) |
| S8 | EUR-Lex: Regulation (EU) 2026/1744 | 2026-07-24 | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | UNVERIFIED (empty response, HTTP 202; same Official Journal text read via S1) |
| S9 | EUR-Lex: Regulation (EU) 2025/327 | 2025-03-05 | https://eur-lex.europa.eu/legal-content/EN/TXT/HTML/?uri=CELEX:32025R0327 | UNVERIFIED (empty response, HTTP 202; same text read via S3) |
| S10 | e-nomothesia: Α.1197/2026 | 2026-09-30 | https://www.e-nomothesia.gr/kat-oikonomia/koine-upourgike-apophase-a1197-2026.html | UNVERIFIED (connection reset) |
| S11 | AADE: Α.1197 / 30-09-2026 | 2026-09-30 | https://www.aade.gr/egkyklioi-kai-apofaseis/1197-30-09-2026 | UNVERIFIED (HTTP 403) |
| S12 | Eurostat Statistics Explained: Use of artificial intelligence in enterprises | Accessed 2026-10-29 | https://ec.europa.eu/eurostat/statistics-explained/index.php/Use_of_artificial_intelligence_in_enterprises | UNVERIFIED (page returned only the site main page, no AI data) |
| S13 | PubMed Central: no-show patterns, northern Italy (PMC12345966) | 2025 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12345966/ | UNVERIFIED (search summary only) |
| S14 | Parianos Typos: online booking of medical appointments (Greek booking data, not no-shows) | Undated | https://parianostypos.gr/kosmos/kosmos-texnologia/item/14092-kerdizei-edafos-to-online-kleisimo-iatrikon-rantevoy | UNVERIFIED (search summary only) |
| S15 | Powergame: e-invoicing, provider-based start reported as 1 March 2027 | Undated | https://www.powergame.gr/?p=1408592 | UNVERIFIED (search summary only) |
| S16 | Ta Nea: e-invoicing, second group from 1 October 2026 | 2026-01-15 | https://www.tanea.gr/2026/01/15/economy/erxontai-ta-ilektronika-timologia-ti-allazei-stis-synallages-ton-epixeiriseon/ | UNVERIFIED (search summary only; superseded by S4) |
| S17 | Doctena: no-show rates, systematic review of over 100 studies (vendor blog) | May 2026 | https://www.doctena.com/en-de/blog/online-medical-agenda-doctena-experience/reduce-no-shows-medical-practice/ | UNVERIFIED (search summary only) |
| S18 | Cyprus Mail: Cyprus firms slow to adopt AI (Greece rank in 2025) | 2025-12-12 | https://cyprus-mail.com/2025/12/12/cyprus-firms-slow-to-adopt-ai-despite-steady-improvement | UNVERIFIED (search summary only) |
| S19 | Bryq: AI Proficiency Greece briefing (cites about 9.8% for 2024) | 2026-03 | https://www.tanea.gr/wp-content/uploads/2026/03/Bryq_AI_Proficiency_Greece_Briefing-1.pdf | UNVERIFIED (search summary only; figure matches S6) |

Counts: 19 sources listed; 7 VERIFIED and 12 UNVERIFIED. The Notion baseline page was read as a document and is not counted as a source of facts.

Not verified:

- The EUR-Lex pages themselves (S8, S9), including EUR-Lex's legal-status field. The Official Journal texts were read through the Publications Office instead.
- Whether the 2 November 2026 e-invoicing date or the 31 January 2027 transition changed after 30 September 2026. AADE's site could not be opened (S11).
- The scope of Article 1 of Law 4308/2014: whether sole practitioners, pharmacies, medical-supply firms and clinics are within it, and any exemptions. The law itself was not read.
- Whether invoices to EOPYY count as B2G under limb (c), and whether domestic B2C receipts are outside the mandate beyond my reading of the list.
- E-invoicing penalty amounts and the AADE circular on penalties.
- The 1 March 2027 provider-based start and the 1 October 2026 / 31 December 2026 dates in news reports (S15, S16).
- Healthcare-specific AI adoption, from any source. Other Eurostat tables and ELSTAT's national ICT survey for 2025 were not checked.
- Any Greek no-show rate. International rates (S13, S17) were not opened.
- Whether the AI features named in Law 5302/2026 Article 92 are live, the law's date and ΦΕΚ reference, and paragraph 5 onward.
- HDPA guidance on AI and health data. One search found none; the HDPA site was not read.
- Everything in item D of the Main findings, which I carried forward from the previous report without re-checking.
