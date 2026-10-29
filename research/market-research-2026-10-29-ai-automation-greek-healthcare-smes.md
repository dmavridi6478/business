# Market research: AI automation for Greek healthcare SMEs

All dates in this report are as of 2026-10-29.

Conventions. VERIFIED means I opened the page or PDF and read the figure or statement cited. UNVERIFIED means the page could not be read (403, 404, 503, empty, unreadable), did not contain the figure, or the figure appeared only in a search-result summary. Unverified numbers appear only in the "Not verified" list and in the Sources table, never as facts. Numbers in square brackets refer to the Sources table. "Inference" marks my own reasoning. Nothing here is legal advice.

## Research topic

**Topic:** AI automation for Greek healthcare SMEs.

**Audience:** owners and owner-managers of small healthcare businesses in Greece: private medical and dental practices, small clinics, diagnostic and physiotherapy centres, pharmacies and small medical-supply firms.

**Requester context (assumption):** docs/about-me.md is an unfilled template, and no content strategy or brand positioning file exists. I assumed a general AI and business-content publisher writing in English for Greek owner-managers, with no medical or legal credentials. Correct this if the real positioning differs.

**Method and limits:**
- Searches ran in English and Greek with WebSearch, and sources were opened with WebFetch. Perplexity was not connected. Semrush and Ahrefs were not used, so there is no search-demand data. Exa and Consensus were not needed. The gap analysis is qualitative.
- Every Greek primary body I could reach was tried: ELSTAT, Eurostat, EUR-Lex, the Commission, the Hellenic Data Protection Authority (HDPA/ΑΠΔΠΧ), the Panhellenic Pharmaceutical Association (ΠΦΣ) and the Athens Medical Association (ΙΣΑ). EUR-Lex, ELSTAT's health tables, AADE's press release and several news sites would not open. Where a PDF was unreadable through WebFetch, I read the saved PDF directly. That worked for the EPF report, the Cuatrecasas legal flash, the ΠΦΣ press clipping, the ΙΣΑ-hosted Digital4u price sheet and the Kalimera.ai deck.
- I did not open anything from the Panhellenic Medical Association (ΠΙΣ), the Hellenic Dental Federation, EOPYY or IDIKA/ΗΔΙΚΑ directly. Their positions reach this report only through news items, a ΙΣΑ letter and ministers' statements.
- No fetched page contained instructions aimed at me.
- The previous general-SME report (2026-10-28) was read for context. None of its figures are reused here unless re-verified for healthcare. I did not re-verify its Eurostat or NBG figures, so I do not use them.

**Not a healthcare-specific data set.** Eurostat's AI-in-enterprises table, as returned for Greece in 2025, carries only one NACE aggregate (all activities except agriculture, mining and finance) [41]. Healthcare is not broken out, and micro firms (0 to 9 employees) show "no data". Therefore no verified statistic on AI adoption by Greek healthcare SMEs exists in this report. That is itself a finding.

## Main findings

### A. Regulation: what has changed and what applies now

1. **The EU AI Act deferral is now law.** Regulation (EU) 2026/1744 (the "Digital Omnibus on AI") is dated 8 July 2026 and was published in the Official Journal on 24 July 2026 [1]. It entered into force on 27 July 2026 [2]. High-risk obligations under Article 6(2) and Annex III move to 2 December 2027, and those under Article 6(1) and Annex I (products such as medical devices) move to 2 August 2028 [1]. The deadline for systems aimed at public authorities is 2 August 2030 [1]. This settles the "provisional agreement" status that the previous report could not confirm. Both sources are law-firm commentary. I could not open EUR-Lex itself [4].

2. **Transparency duties are not deferred.** HDPA states that Article 50 transparency obligations applied from 2 August 2026 [11]. A law-firm article says organisations "must continue to comply" with disclosure that people are interacting with an AI system [2]. Inference: a clinic that puts a patient-facing chatbot or voice agent online should tell patients it is an AI.

3. **Medical-device AI sits in the Annex I track.** The Commission's November 2025 proposal kept AI that is, or is a safety component of, an MDR/IVDR product as high-risk [3]. The same proposal aimed at a single notified-body assessment under both laws [3]. That source is the proposal, not the adopted text. The Cuatrecasas summary confirms the final Annex I date of 2 August 2028 [1]. I could not verify the MDCG 2025-6 guidance on which device classes trigger high-risk [43], and I did not verify MDR classification rules for software. Inference: AI for diagnosis or imaging is the device-regulation question. Administrative AI (appointment calls, reminders, website answers) is a different and probably lighter question. A regulatory adviser must confirm this before anything is published.

4. **Greece has a national AI Act law.** Law 5321/2026 was published as ΦΕΚ Α' 114 on 20 July 2026 [10]. HDPA is the market-surveillance authority for prohibited practices, Annex III systems and Article 50 transparency, and also the single point of contact and complaints channel [10][11]. EETT is the notifying authority. EOF (the national medicines organisation) supervises AI in medical devices and IVDs as a sectoral authority [10]. Sanction-setting treats AI-literacy measures and voluntary disclosure as mitigating factors [10]. The EY alert does not address SMEs [10].

5. **GDPR Article 9 is the daily constraint.** Health data are special-category data under Art. 9(1). Processing for diagnosis, care and treatment is allowed under Art. 9(2)(h) only when a professional bound by secrecy handles it (Art. 9(3)). Member States may add conditions for health data (Art. 9(4)) [9]. I read an unofficial reproduction of the text, not EUR-Lex.

6. **The Greek authority does fine small providers.** Two cases, both through secondary reports:
   - ΑΠΔΠΧ 11/2025: €5,000 against a gynaecologist who opened a former patient's electronic health record without authority, after the patient had ended the relationship. The Authority cited Art. 5(1)(a) as the basis for the fine and found no Art. 9(2) condition applied. It found no breach of the access right and no proof of transfer to third parties. Article dated 19 June 2025 [13].
   - A €30,000 fine on a diagnostic centre that had not kept an imaging exam for ten years from the patient's last visit and could not satisfy a GDPR Art. 15 access request. It cited Art. 14(4)(a) of Law 3418/2005. Article dated 22 August 2022 [14].
   - Inference: enforcement against small providers has so far concerned access to records and retention, not AI. A practice that feeds records to a cloud AI tool adds a new processor and a new transfer to a process the Authority already scrutinises.

7. **HDPA publishes AI-and-GDPR training material.** Its home page lists "Εκπαιδευτικό Υλικό – ΤΝ και ΓΚΠΔ". I saw the link but did not read the material [12].

8. **EHDS arrives in stages, and it is slow.** Regulation (EU) 2025/327 was published on 5 March 2025 (adopted 11 February 2025) [7] and entered into force on 26 March 2025 [6]. According to the Commission page, the exchange of patient summaries and ePrescriptions/eDispensations starts in March 2029, and images, lab results and discharge reports follow in March 2031. Secondary use starts in March 2029 for most data categories [6]. EHR-system manufacturers must certify, with most obligations about four years after entry into force [6]. Inference: EHDS is a 2029 planning item for a small practice, not an urgent 2026 one. It matters most when choosing EHR software now.

9. **E-invoicing: the date holds as of 29 October 2026.** Decision Α.1197/2026 (ΦΕΚ Β' 5905, 30 September 2026) says second-period entities must issue "αποκλειστικά ηλεκτρονικό τιμολόγιο" from 2 November 2026. A transition to 31 January 2027 allows ERP or the AADE form, if a start declaration (or declared use of the timologio app) is dated no later than 2 November 2026 [15]. A tax-information site says the provider-or-AADE-apps-only rule applies from 1 February 2027, and that nothing further has been postponed [16]. My searches found no postponement after 30 September 2026. I could not read AADE's own site. The decision text says nothing about healthcare providers, EOPYY or B2C receipts [15]. The scope question for clinics is therefore open, not answered (see content idea 3). Phase 1 (businesses above €1m) moved from 2 February to 2 March 2026 under Α.1044/2026 [17][18]. EY's February 2026 alert still showed 1 October 2026 for phase 2, which A.1197/2026 superseded [18][15]. EY also reports AADE circular Ε.2004/2026, which treats manual or ERP-only issuance as non-issuance of an invoice except during outages. The penalty amounts sit in a table I could not read [18].

### B. Owner pain points, grounded in sources

10. **Admin load and e-prescription.** The union of EOPYY doctors (ΕΝΙ-ΕΟΠΥΥ) said on 22 January 2025 that the new e-prescription platform led to a "διπλασιασμού του χρόνου συνταγογράφησης". It also said the new ΗΔΙΚΑ appointment platform "απαιτεί τη δήλωση ωραρίου" committed to EOPYY, that electronic requests need phone verification, and that specialist contracts pay "αμοιβή ύψους 6€ καθαρά" per act, with EOPYY buying visits up to a cap of 200 a month [23]. This is a union statement, not an audit. The Athens Medical Association (ΙΣΑ) wrote to EOPYY and ΗΔΙΚΑ on 17 October 2024 about άυλη συνταγογράφηση. A doctor prescribed to four patients who had not activated the service and was refused reimbursement and warned of a fine. ΙΣΑ argued that doctors "cannot check each patient's activation status" given their workload, and asked the system to block completion [24]. The Commission's 2026 Digital Decade report for Greece says access to e-health records "has surged ahead" via the National Electronic Health Record and the MyHealth app. It gives no numbers on this point [31]. In May 2025 the health minister claimed that e-prescriptions cover almost 100% and EOPYY waiting time fell from two months to 48 hours [38]. That is a political claim.

11. **Billing and EOPYY claims (clawback and arrears).** Ministers said on 27 June 2025 that the clawback debt of private diagnostic centres since 2016 is about €1bn, of which about €800m (80%) arose from 190 added reimbursable tests without a budget increase. They announced €42m for EOPYY: €30m raising the diagnostics credit limit, and €12m for distributing high-cost drugs through pharmacies (up to 50,000 prescriptions). They also announced the abolition of a 0.8% fine on pharmacists who do not dispense the generic [21]. The ministers attribute most of the debt to the previous government, so treat the framing as political. On 4 August 2026, ΠΦΣ reported that the obesity programme's debts to private pharmacies total €15m, about €1,500 per pharmacy on average, with payment for May and June delayed after the programme lost EU funding [22]. Inference: payer-dependent small providers face cash-flow risk that is not an IT problem. AI can help prepare, check and reconcile claims, but no source shows this working in Greece.

12. **Appointment no-shows.** I found no Greek measurement of no-show rates. International studies exist but are unverified [46]. The only Greek-language evidence in this run is vendor material. Kalimera.ai's deck, presented in a ΣΕΒ-hosted document, reports for one diagnostic group (14 sites, 143 employees) over 98 days (7 October 2025 to 13 January 2026), on overflow traffic only: 4,572 calls, 2,078 appointments booked, a 45.5% call-to-appointment conversion, 92% of calls completed, and 43% of calls lost before the tool [35]. These are vendor claims about missed calls, which are not the same as no-shows. The deck also cites "43% of doctors report burnout due to inefficient EHR systems" with a US library as its source. I did not verify that [35].

13. **Cost.** Digital4u's "AI Medical Assistant" website chatbot, listed on a ΙΣΑ-hosted sheet (PDF created 19 May 2026), costs €700 + VAT setup in the first year and €700 + VAT per year, with a 25% discount for ΙΣΑ members. The sheet says answers are based "αποκλειστικά" on the doctor's own website content [34]. First-year list cost is €1,400 + VAT (my arithmetic). The sheet does not say how the discount applies. Inference: this is the first priced, Greek-language, doctor-facing AI product I could verify, and a professional body is distributing it. The wider cost context is a patient-funded system. Greek private health spending is 5% of GDP against an EU 2%, and out-of-pocket is 2.9% against 1.5% (IOBE, reported 9 June 2026) [27]. The WHO-based figure for out-of-pocket is 34% of health spending against about 15% in the eurozone (reported 1 December 2025) [26]. ELSTAT's private share of health financing is 39.1% for 2023 (reported 1 April 2025) [25].

14. **GDPR and liability.** See findings 5 to 7. I found no Greek source on liability for AI errors in a clinic. Inference: no authoritative Greek guidance exists for small practices, so this is open ground.

15. **Skills.** The Commission says the gap in basic digital skills between Greece and the EU is growing, and that AI adoption by enterprises "remains low". The report gives no numbers on this page [31]. I found no healthcare-specific skills survey.

16. **Patient trust.** The European Patients' Forum survey (874 responses, analysed with KU Leuven, 28 May 2026) is EU-wide and self-selected, with no Greek breakout. Findings: 98% think AI could bring benefits. 59% are comfortable with AI for administrative tasks, 72% for analysing test results and imaging, and 42% for recommending medications. 39% are not very or not at all confident in how AI is applied. 70% worry about lost empathy, and 51% worry about doctors using AI tools "not specifically approved for healthcare purposes". 93% want to be told at the start of the visit, 82% want to hear it from their doctor, and 61% want AI-specific consent forms. 22% are unsure whether AI was ever involved in their care. About 30% say patients should have full control over any AI use, including scheduling [32]. Inference: administrative AI is the most accepted use, but disclosure is expected. A Greek small practice should treat disclosure as a trust feature.

17. **Greek-language tools.** The ILSP Krikri-8B-Instruct model is a Llama-3.1-8B model continued on Greek text. It supports Greek and English, has a 128k context and the Llama 3.1 licence, and links to a paper dated 19 May 2025. Its page claims "domain-specifc expertise for specialized legal, financial, medical, and scientific applications" and gives no evidence or limits for the medical claim [40]. Kalimera.ai claims 65+ languages with specialisation in Greek and the Cypriot dialect, and ISO 27001, ISO 42001, GDPR and HIPAA compliance. It is a vendor claim that I did not test [35]. No independent Greek clinical-language evaluation was found.

18. **Public-sector AI sets expectations.** The Digital Doctor Assistant (Ψηφιακός Βοηθός Ιατρού) inside the National Electronic Health Record is described on 30 October 2025 as the first AI application in the health sector. Doctors reach it through myHealthDoc and ask plain-language questions about a patient's history, examinations and medication. The article describes no data-protection safeguards [39]. Inference: private practices will be compared with a free state tool, and may be asked how their own tools differ.

19. **Medical tourism and seasonality.** An Elitour study funded by the EBRD, reported 5 December 2025, puts Greek medical-tourism turnover at about €100m, of which €22m is emergency medical services. It says wellness tourism is ten times larger, with patients from the UK, Germany and the Middle East, and strengths in dialysis, IVF and dental care [36]. Bank of Greece provisional data for 2025 give 37.98m inbound visitors and €23.6bn in travel receipts [37]. Neither source gives a seasonality profile, and I found no verified source on seasonality for clinics. Inference: multi-language booking and reminders are a plausible fit for dental and IVF providers with foreign patients, but no source shows demand or results.

### C. What the sector looks like

20. **Size, verified for 2021 only.** 66,504 registered doctors and 13,759 dentists in 2021. ΠΦΣ counted 11,414 pharmacists working in pharmacies [28]. A secondary outlet reports newer 2024 ELSTAT figures, but I could not open that page, so they appear only under Not verified.

### D. Patterns (inference)

- **Pattern 1: The payer and the regulator shape the pain more than the technology.** The loudest verified complaints concern EOPYY platforms, e-prescription rules, clawback and payment delays [21][22][23][24]. AI sales pitches focus on call handling and websites [34][35].
- **Pattern 2: Vendors fill the information gap, and professional bodies relay them.** The two Greek-language AI product documents found are a ΙΣΑ-hosted price sheet and a ΣΕΒ-hosted vendor deck [34][35]. I found no neutral buyer's guide.
- **Pattern 3: Administrative AI is the low-regret entry.** Patients are most comfortable with administrative uses [32], and the AI Act's heavy duties attach to high-risk and device-type systems [1][3]. But health data still enter via phone calls, so GDPR applies even to a booking agent (inference).
- **Pattern 4: Disclosure is both a legal and a trust issue.** Article 50 applies now [11][2], and patients want to be told [32].
- **Pattern 5: Compliance deadlines compete for attention.** E-invoicing starts on 2 November 2026 [15], and AI Act high-risk dates have moved to late 2027 and 2028 [1]. Inference: owners will not prioritise AI until invoicing settles, and the scope for clinics is unclear.

## Conflicts

1. **EHDS dates.**
   - The Commission's page gives March 2029 (patient summaries and ePrescriptions) and March 2031 (images, lab results, discharge reports) for primary use. Secondary use is March 2029 and March 2031. It gives entry into force as 26 March 2025 [6].
   - A search summary of law-firm and Spanish-ministry pages gave 26 March 2027 as the general application date, and 25 March 2025 as entry into force on one dossier site. I could not open those pages, so the summary is unverified [8].
   - Likely reconciliation (inference): the Regulation applies in stages, with 2027 as a first milestone and 2029 and 2031 for the data-exchange duties. Check Article 105 on EUR-Lex before publishing.

2. **AI Act timing for medical-device AI.**
   - Original date: 2 August 2027 (stated in a search summary and used by older commentary, unverified [43]).
   - Commission proposal, November 2025: 12 months after a Commission decision, with a backstop of 2 August 2028 [3].
   - Adopted Regulation (EU) 2026/1744: 2 August 2028 for Annex I, and 2 December 2027 for Annex III [1].
   - Use the adopted dates. Older articles, including the MDCG 2025-6 commentary found in searches, may still say 2027.

3. **E-invoicing start for businesses up to €1m.**
   - 1 October 2026: EY alert of 27 February 2026 [18].
   - 2 November 2026, with a transition to 31 January 2027: Decision Α.1197/2026 [15][16].
   - Resolved: the later official decision governs. A search summary also mentioned a transition to 31 December 2026 in earlier reporting. That is superseded by [15].
   - Phase 1: 2 February 2026 [18] against 2 March 2026 [17], where Α.1044/2026 made the move. The previous report could not resolve this.

4. **Private share of health spending.**
   - 39.1% (ELSTAT, 2023, as reported on 1 April 2025). The same article also prints 38.6% in one paragraph, which does not match its 60.9% public share [25].
   - 34% out-of-pocket (WHO data, reported 1 December 2025) [26], against 2.9% of GDP out-of-pocket in the IOBE report [27].
   - These measure different things: total private financing (including voluntary insurance) against household out-of-pocket payments, and shares of spending against shares of GDP. They are consistent. Publish each with its definition. Search summaries gave 60%, 40% and 35% for other framings. I could not verify those.

5. **Is the e-prescription and referral burden real?**
   - Minister, 24 May 2025: e-prescriptions cover almost 100%, EOPYY waiting time cut from two months to 48 hours [38].
   - ΕΝΙ-ΕΟΠΥΥ, 22 January 2025: prescribing time doubled, €6 net per act, capped at 200 visits a month [23]. ΙΣΑ, 17 October 2024: reimbursement refused for άυλη prescriptions to unactivated patients [24].
   - These claim different things: coverage and patient waiting against doctor workload and pay. Neither source is an audit. Present both as claims by their authors.

6. **Who caused the clawback debt?**
   - Ministers: about €800m of €1bn arose from 190 extra tests added without budget [21].
   - Search summary of a ΠΙΣ letter (unverified): clawback demands "often exceed 50% of monthly submissions" [not opened].
   - These do not contradict each other, but they blame different parties. Avoid taking a side.

7. **Vendor outcomes against independent evidence.**
   - Kalimera.ai: 43% of calls lost before the tool, a 45.5% call-to-appointment conversion [35]. Digital4u: more conversions and fewer calls, with no figure [34].
   - No independent Greek measurement of missed calls or no-shows was found.
   - Treat vendor numbers as claims. A fair test would compare the same clinic before and after.

## Content ideas

Ranked by urgency, strength of verified evidence and fit with the audience. Each should carry its source dates and avoid legal advice.

1. **"The AI Act for a Greek clinic, as of today."** Verified base: Regulation 2026/1744 dates, Article 50 already applying, HDPA and EOF roles, Law 5321/2026 [1][2][10][11]. Message: what a booking chatbot must disclose now, what is high-risk later, and who supervises. Needs a regulatory adviser's check for device-type tools, and the EUR-Lex text for Article 4 (AI literacy), which I could not verify in its final form [45].

2. **"Before you paste a patient's data into a chatbot."** GDPR Art. 9(2)(h) and 9(3), with the two ΑΠΔΠΧ cases as concrete examples [9][13][14]. Include a plain checklist: processor contract, where data go, who can see them, retention. Do not claim a Greek AI-specific rule exists. Point readers to the HDPA material [12].

3. **"2 November: does e-invoicing touch your practice, pharmacy or supply firm?"** Verified dates [15][17]. The scope for B2C patient receipts, EOPYY billing and pharmacies is not verified, so the piece must start by sending readers to their accountant and AADE. Inference: medical-supply firms and pharmacy suppliers, who sell to businesses, are most exposed. Very time-sensitive.

4. **"What a €700-a-year AI website assistant does, and what it does not."** Use the ΙΣΑ-hosted Digital4u sheet as the verified anchor [34]. A buyer's checklist: what content it answers from, what happens when a visitor types symptoms, GDPR role, disclosure, exit terms. Positions the publisher as neutral against vendor-written material.

5. **"Missed calls are not no-shows: measure before you buy."** Use the Kalimera.ai case as an illustration of vendor claims [35], and explain a one-week self-audit. Add international no-show benchmarks only after verification [46].

6. **"Tell your patients: what they expect on AI disclosure."** EPF data (93%, 82%, 61%) [32] and Article 50 [11]. Includes a short patient-notice template for owners to adapt, marked as not legal advice. Caveat: EU-wide, self-selected sample.

7. **"EOPYY paperwork: where software can help, where it cannot."** Anchor on the union and ΙΣΑ statements [23][24] and the ΠΦΣ payment delays [22]. The gap: no Greek source shows AI cutting claims work. Frame as a question to test.

8. **"Medical and dental tourism: multi-language booking."** Elitour/EBRD [36] and Bank of Greece [37] give the market. There is no seasonality data and no result data, so frame as a hypothesis, not advice.

9. **"Greek-language AI for clinical notes: test it yourself."** Krikri page [40] versus vendor claims [35]. Offer a test protocol on non-patient sample text. Original content, not research.

10. **"EHDS: what 2029 and 2031 mean for a small practice."** Commission dates [6], plus the 2027 conflict above [8]. Lower urgency.

**Content gaps (inference, from what the searches surfaced).**
- **Vendors and professional bodies** are the visible sources of Greek-language AI-for-clinics material [34][35]. **Law firms and consultancies** cover the AI Act in general [1][10], and I found none with a Greek clinic angle. A search for Big Four healthcare-AI reports on Greece returned none, based on a single search [44]. **Banks:** the NBG report from the previous run is about general SMEs, and I found no bank paper on healthcare.
- **Unanswered:** Greek no-show rates; the cost of AI for a small practice beyond one vendor price; AI liability for a small provider; which e-invoicing duties apply to B2C and EOPYY billing; pharmacy-specific AI use; physiotherapy and diagnostic-centre use cases; tourism seasonality for clinics; independent Greek clinical-language tests.
- **Advice worth challenging:**
  - "Automate your front desk and no-shows disappear": the only Greek numbers are vendor numbers about calls [35].
  - "AI Act deadlines are 2026": superseded by Regulation 2026/1744 [1], but Article 50 is live [11].
  - "Digital doctor tools are the same as AI scribes": the Greek state tool queries records [39], whereas ambient scribes record consultations, and I found no Greek evidence on those.
  - "Greek adoption is X%" for healthcare: no source breaks it out [41].
  - Blaming owners' mindset: the verified pain points are structural (platforms, payment, rules) [21][22][23][24].

## Sources

Verified means I read the page or PDF and the cited statement or figure is there. Type: P = primary or near-primary; S = secondary (news or law-firm); V = vendor or advocacy.

| # | Publisher and title | Date | URL | Mark |
|---|---|---|---|---|
| 1 | Cuatrecasas (S): Digital Omnibus on AI, Key Changes (Legal Flash, PDF read) | July 2026 | https://www.cuatrecasas.com/resources/ai-omnibus-regulation-eng-txt-6a6c91679b13e331880996.pdf | VERIFIED |
| 2 | National Law Review (S): EU Digital Omnibus on AI enters into force | 2026 (not shown) | https://natlawreview.com/article/eu-digital-omnibus-ai-enters-force | VERIFIED (does not address Article 4 or SMEs) |
| 3 | Osborne Clarke (S): medical devices and the Digital Omnibus proposal | Proposal of 2025-11-19 | https://www.osborneclarke.com/insights/medical-devices-diagnostics-and-pharma-win-concessions-eu-digital-omnibus-proposal | VERIFIED (proposal, not adopted text) |
| 4 | EUR-Lex: Regulation (EU) 2026/1744 | 2026-07-24 | https://eur-lex.europa.eu/eli/reg/2026/1744/oj | UNVERIFIED (page returned empty) |
| 5 | White & Case: EU AI Omnibus enters into force | 2026 | https://www.whitecase.com/insight-alert/eu-ai-omnibus-enters-force-amending-ai-act | UNVERIFIED (HTTP 403) |
| 6 | European Commission, DG SANTE (P): EHDS Regulation page | Undated | https://health.ec.europa.eu/ehealth-digital-health-and-care/european-health-data-space-regulation-ehds_en | VERIFIED |
| 7 | European Commission (P): publication page for Regulation (EU) 2025/327 | 2025-03-05 | https://health.ec.europa.eu/publications/regulation-eu-2025327-european-health-data-space-and-amending-directive-201124eu-and-regulation-eu_en | VERIFIED (no application dates on page) |
| 8 | EUR-Lex: Regulation (EU) 2025/327 (Article 105) | 2025-03-05 | https://eur-lex.europa.eu/eli/reg/2025/327/oj | UNVERIFIED (page returned empty) |
| 9 | gdpr-info.eu: GDPR Article 9 (unofficial reproduction of Regulation (EU) 2016/679) | Undated | https://gdpr-info.eu/art-9-gdpr/ | VERIFIED (EUR-Lex official text not opened) |
| 10 | EY Greece (S): Act no. 5321/2026, Greek legal framework for AI supervision | 2026-09-02 | https://www.ey.com/en_gr/technical/tax/tax-alerts/ai-act-greek-legal-framework-for-the-supervision-of-artificial-intelligence-systems | VERIFIED (secondary summary of the law) |
| 11 | Hellenic Data Protection Authority (P): press release on its role in implementing the AI Act | 2026-08-18 | https://www.dpa.gr/en/enimerwtiko/press-releases/hellenic-dpa-takes-leading-role-implementing-eu-ai-act-greece | VERIFIED |
| 12 | Hellenic Data Protection Authority (P): home page (AI and GDPR training material link, items of 8 and 9 October 2026) | 2026-10-29 (accessed) | https://www.dpa.gr/el | VERIFIED (link seen; material not read) |
| 13 | Lawspot (S): ΑΠΔΠΧ 11/2025, €5,000 fine on a gynaecologist | 2025-06-19 | https://www.lawspot.gr/nomika-nea/anthropino-endiaferon-kostise-akriva-5000-eyro-prostimo-se-gynaikologo-gia-horis-dikaioma/ | VERIFIED (decision's own date not stated) |
| 14 | Insurancedaily (S): €30,000 fine on a diagnostic centre | 2022-08-22 | https://www.insurancedaily.gr/prostimo-30-000-eyro-se-diagnostiko-kentro-apo-tin-archi-prostasias-dedomenon | VERIFIED (decision number not stated) |
| 15 | Taxheaven (S, publishes decision text): Α.1197/2026, ΦΕΚ Β' 5905 | 2026-09-30 | https://www.taxheaven.gr/circulars/55463/a-1197-2026 | VERIFIED |
| 16 | LookupTax (S, vendor): e-invoicing B2B phase 2 moved to 2 Nov 2026 | 2026 (undated) | https://lookuptax.com/tax-changes/greece/einvoicing-b2b-phase-2-moved-2-nov-2026 | VERIFIED |
| 17 | Taxheaven (S): news on Α.1044/2026 moving phase 1 to 2 March 2026 | 2026-02-17 | https://www.taxheaven.gr/news/72877/paratash-gia-thn-hlektronikh-timologhsh | VERIFIED |
| 18 | EY Greece (S): mandatory e-invoicing, recent developments (Α.1044/2026, Ε.2004/2026) | 2026-02-27 | https://www.ey.com/el_gr/technical/tax/tax-alerts/ypoxrewtiki-ilektroniki-timologisi-prosfates-ekselikseis | VERIFIED (penalty amounts in an unreadable table) |
| 19 | e-nomothesia: Α.1197/2026 text | 2026-09-30 | https://www.e-nomothesia.gr/kat-oikonomia/koine-upourgike-apophase-a1197-2026.html | UNVERIFIED (HTTP 503) |
| 20 | AADE (P): press release dt_16.09.2025 | 2025-09-16 | https://www.aade.gr/sites/default/files/2025-09/dt_16.09.2025..pdf | UNVERIFIED (HTTP 403) |
| 21 | Το Μανιφέστο via Innews press clip hosted by ΠΦΣ (S): ministers on clawback and the €42m package | 2025-06-27 | https://files1.psf.org.gr/img/enimerosi_files/20250627_123650_14cc.pdf | VERIFIED (PDF read; ministers' statements, politically framed) |
| 22 | Panhellenic Pharmaceutical Association (P): press release 3385/2026 (via OENET) on obesity programme debts | 2026-08-04 | https://www.oenet.gr/online/dnef/item/137818-pfs-enimerosi-gia-ti-sinexisi-tou-programmatos-prolipsis-kai-antimetopisis-tis-paxisarkias-kai-gia-tin-eksoflisi-ton-ofeilon-ton-minon-maiou-kai-iouniou | VERIFIED |
| 23 | News4health (S): ΕΝΙ-ΕΟΠΥΥ statement on e-prescription and the ΗΔΙΚΑ referral platform | 2025-01-22 | https://www.news4health.gr/epikairotita/eni-eopyy-ilektroniki-grafeiokratia-ligotero-iatriko-ergo-amoives-peinas | VERIFIED (union statement) |
| 24 | News4health (S): Athens Medical Association letter on άυλη συνταγογράφηση | 2024-10-17 | https://www.news4health.gr/pharma-policy/epistoli-isa-se-eopyy-kai-idika-gia-ti-leitourgia-tou-systimatos-ilektronikis-syntagografisis | VERIFIED |
| 25 | Parapolitika (S): ELSTAT total health spending 2023, 9.60% of GDP | 2025-04-01 | https://www.parapolitika.gr/ugeia/article/1536767/elstat-sto-960-epi-tou-aep-oi-sunolikes-dapanes-ugeias-stin-ellada-gia-to-2023/ | VERIFIED (secondary; ELSTAT release not opened) |
| 26 | in.gr (S): out-of-pocket 34% (WHO and OECD data) | 2025-12-01 | https://www.in.gr/2025/12/01/greece/to-aorato-elleimma-tis-ygeias-stin-ellada/ | VERIFIED (secondary) |
| 27 | To Vima (S): IOBE report on private health spending | 2026-06-09 | https://www.tovima.com/society/greeks-pay-twice-the-eu-average-out-of-pocket-for-healthcare/ | VERIFIED (secondary; reference year not stated) |
| 28 | Protothema (S): ELSTAT registered doctors and dentists 2021, pharmacists per ΠΦΣ | 2022-12-21 | https://www.protothema.gr/greece/article/1321212/elstat-posous-giatrous-kai-farmakopoious-ehoume-analutika-stoiheia-apo-tin-apografi/ | VERIFIED (secondary; data year 2021) |
| 29 | Forin.gr: ELSTAT 2024 registered health professionals | 2025 | https://www.forin.gr/articles/article/88376/elstat-aukshsh-17-shmeiwsan-perusi-oi-eggegrammenoi-epaggelmaties-ugeias | UNVERIFIED (HTTP 403; figures from a search summary only) |
| 30 | ELSTAT (P): Health Interview Survey 2025 page; ESSPROS 2023 page | Undated | https://www.statistics.gr/en/statistics/-/publication/SHE22/- | UNVERIFIED (pages opened, no relevant figures) |
| 31 | European Commission (P): Greece 2026 Digital Decade country report, factpage | 2026 | https://digital-strategy.ec.europa.eu/en/factpages/greeces-2026-digital-decade-country-report | VERIFIED (qualitative text only; KPI charts unreadable) |
| 32 | European Patients' Forum with KU Leuven (V, advocacy): What do patients think about AI in healthcare? (PDF read) | 2026-05-28 | https://www.eu-patient.eu/globalassets/final---epf-ai-survey-report-2026_v2.0.pdf | VERIFIED (874 responses, EU-wide, self-selected, no Greek breakout) |
| 33 | GreekReporter (S): NielsenIQ survey, Greek attitudes to AI | 2025-11-25 | https://greekreporter.com/2025/11/25/greek-attitudes-towards-ai-high-familiarity-low-trust/ | UNVERIFIED (HTTP 403) |
| 34 | Digital4u (V), AI Medical Assistant price sheet hosted by Athens Medical Association (PDF read) | PDF created 2026-05-19 (path 2026/06) | https://portal.isathens.gr/wp-content/uploads/2026/06/AI-Medical-Assistant__ISA.pdf | VERIFIED (vendor sheet) |
| 35 | Kalimera.ai (V), presentation hosted on sev.org.gr (12 slides read) | Path 2026/02; data to 2026-01-13 | https://www.sev.org.gr/wp-content/uploads/2026/02/Chalkiadakis.pdf | VERIFIED (vendor claims only) |
| 36 | To Vima (S): Greece eyes gains in wellness and medical tourism (Elitour/EBRD study) | 2025-12-05 | https://www.tovima.com/travel/greece-eyes-major-gains-in-wellness-and-medical-tourism/amp/ | VERIFIED (secondary) |
| 37 | Euronews (S): record arrivals and tourism revenues for Greece in 2025 (Bank of Greece provisional data) | 2026-02-24 | https://www.euronews.com/2026/02/24/record-arrivals-and-tourism-revenues-for-greece-in-2025 | VERIFIED (no seasonality data) |
| 38 | CNN Greece (S): health minister on AI and health at the Economist summit | 2025-05-24 | https://www.cnn.gr/politiki/story/478482/georgiadis-o-xoros-tis-ygeias-tha-exei-ti-megalyteri-anaptyksi-logo-tis-texnitis-noimosynis | VERIFIED (ministerial claims) |
| 39 | Lawspot (S): Digital Doctor Assistant in the National Electronic Health Record | 2025-10-30 | https://www.lawspot.gr/nomika-nea/se-leitourgia-o-psephiakos-boethos-iatrou-ston-ethniko-elektroniko-phakelo-ugeias/ | VERIFIED |
| 40 | Hugging Face (P, model publisher page): ilsp/Llama-Krikri-8B-Instruct | Paper 2025-05-19 | https://huggingface.co/ilsp/Llama-Krikri-8B-Instruct | VERIFIED |
| 41 | Eurostat (P): isoc_eb_ai API response, Greece 2025 | 2025 data | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_eb_ai?format=JSON&lang=en&geo=EL&time=2025 | UNVERIFIED for figures (value decoding unreliable). Used only for dimension structure (one NACE aggregate; 0-9 size class "no data") |
| 42 | Eurostat isoc_ehe_iu_hlt API; Trading Economics (online health information) | Dec 2025 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/isoc_ehe_iu_hlt | UNVERIFIED (404; Trading Economics figure from a search summary) |
| 43 | MDCG 2025-6 on MDR/IVDR and AI Act interplay (via OpenRegulatory and other summaries) | 2025 | https://openregulatory.com/mdcg/mdcg-2025-6 | UNVERIFIED (HTTP 403; search summaries only) |
| 44 | Naftemporiki: private healthcare market over €2bn in 2023 | Undated | https://www.naftemporiki.gr/?p=1998325 | UNVERIFIED (search summary only) |
| 45 | Commentary on final Article 4 AI-literacy wording (ahaslides, Opsio, presencis) | 2026 | https://opsiocloud.com/knowledge-base/eu-ai-act-ai-literacy-article-4/ | UNVERIFIED (search summaries only) |
| 46 | PubMed Central: no-show studies (Israel PMC6664577; northern Italy PMC12345966) | 2019; 2025 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12345966/ | UNVERIFIED (search summaries only) |
| 47 | BMJ Health & Care Informatics: UK GP survey on ambient AI scribes | 2025 | https://www.citedrive.com/en/discovery/ambient-ai-in-primary-care-an-exploratory-mixed-methods-survey-of-uk-general-practitioners/ | UNVERIFIED (search summary only) |

**Counts:** 47 sources listed; 32 VERIFIED and 15 UNVERIFIED. Of the 32 verified, only 8 are primary or near-primary: [6], [7], [11], [12], [15], [22], [31], [40]. The rest are news, law-firm, vendor or advocacy material, and are marked so.

Not verified:
- The final text of Regulation (EU) 2026/1744 on EUR-Lex, including the final wording of Article 4 (AI literacy) and any SME or small mid-cap relief. Only law-firm summaries were read [1][2][4][45].
- MDCG 2025-6, including which MDR/IVDR classes make device AI high-risk, and any MDR classification rule for software [43].
- EHDS Article 105 on EUR-Lex, and the 26 March 2027 general-application date given in a search summary [8].
- Whether Decision Α.1197/2026 and its underlying framework cover B2C patient receipts, EOPYY billing, pharmacies or sole-practitioner doctors, and the penalty amounts under Law 5104/2024 [15][18][19][20].
- Whether AADE or the ministry has changed the 2 November 2026 date since 30 September 2026. I found no change, but could not read AADE's own site.
- ELSTAT 2024 health-workforce figures (a search summary gave 69,937 doctors, 13,840 dentists, 10.1 pharmacies per 10,000 people, 11,447 physiotherapists, 11,498 pharmacists), and any ELSTAT table on private diagnostic centres [29][30].
- Eurostat figures for Greece on AI use, and on online health information or appointment booking. A Trading Economics figure of 51.13% for 2025 appears only in a search summary [41][42].
- Any Greek no-show rate. International benchmarks (about 15% in an Israeli hospital, 5.1% in northern Italy, a European average of 19.3%) come from search summaries [46].
- The NielsenIQ Greek AI-trust figures (85% familiar, 30% trust) [33].
- The "43% of doctors report burnout due to inefficient EHR systems" slide in [35], and any Kalimera.ai or Digital4u performance and compliance claim.
- Pharmacy-specific, physiotherapy-specific and dental-specific AI evidence. Nothing from the Panhellenic Medical Association, the Hellenic Dental Federation, EOPYY or ΗΔΙΚΑ was opened directly.
- Tourism seasonality for clinics, and the methodology of the Elitour/EBRD medical-tourism figure [36].
- A ΠΙΣ letter (search summary) that clawback demands often exceed 50% of monthly submissions.
- The UK GP survey on AI scribes (14% use, 39% intend) [47]. Not used as a fact.
- Whether Law 5321/2026 is in force as of a specific date other than its publication on 20 July 2026. One database summary said 20 October 2026, uncorroborated.
