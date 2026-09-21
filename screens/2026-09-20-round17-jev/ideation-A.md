# Ideation A, Jev, lane: pre-action outcome prediction across a system boundary

Method read: METHOD.md lines 34-291 (Part 1, stages 0-6). Room read: STATE.md "THE ROOM" section
(lines 32-95ish). Technology and lane as specified in the ideation brief. Competitor research is out of
scope for this pass (separate blind agent). All dollar figures below were fetched and read as primary
documents (government code, government fee schedule, bank tariff PDFs via `pdftotext`, or an industry
policy brief); none are search-engine summaries taken on faith. Where I could not get a primary number,
it is marked NOT VERIFIED rather than estimated.

---

## Candidate 1: Export-Control Enforcement-Risk Score

**1. Name:** Export-Control Enforcement-Risk Score

**2. Tuple:**
- **Customer segment and band:** small-to-mid manufacturers and distributors of dual-use goods
  (electronics, machine tools, specialty chemicals, sensors) that self-classify their own products under
  the Commerce Control List and self-file export declarations, roughly 50-500 employees, shipping
  internationally at least monthly, without a dedicated export-compliance officer.
- **Asset:** a private ledger, per SKU/destination/end-user combination, of this company's own past
  classification and licensing decisions matched against what actually happened to that shipment
  afterward (cleared cleanly, held at port, flagged by AES, or drew a BIS inquiry). No public dataset
  contains a single company's own shipment-to-enforcement-outcome history.
- **Document set / state input:** the order or shipment record as it sits in the exporter's order-
  management or trade-compliance software before the Electronic Export Information filing, product
  description, proposed ECCN, destination country, end-user, and stated end-use, as text/JSON.
- **The mistake:** shipping without a required license, or under a classification that understates
  control, which surfaces later as an AES hold, a port detention, or a Bureau of Industry and Security
  (BIS) enforcement action.
- **The checker and the rule:** BIS Office of Export Enforcement, acting under the Export Administration
  Regulations (15 CFR Parts 730-774) and the Export Control Reform Act of 2018 (50 U.S.C. §§ 4801-4852).

**3. Differentiated claim:** An incumbent would already have to be claiming it can predict, from its own
cross-customer ledger of past product/destination/end-user combinations and what BIS actually did about
each one afterward, which of a NEW exporter's specific shipments are likely to draw an AES hold or a BIS
enforcement inquiry, not merely that it can look up the technically correct ECCN against the public
Commerce Control List (any classification-lookup tool already does that for free).

**4. Question shape:** **Noul**, "does this shipment line require a license / carry elevated enforcement
risk, yes or no" with a probability, run on every order line at the moment it is entered, before the EEI
filing. Why sub-second and near-zero cost: an active exporter in this band can push thousands of order
lines a year through classification; scoring each one at $0.042/M input tokens inside the ERP's save
action is free relative to a compliance analyst's hourly rate, and sub-second latency is what lets the
check run synchronously inside order entry instead of as an offline batch review days later.

**5. Where the outcome is observed:** By the exporter's compliance team (or its freight forwarder), in
three possible systems, none of which is the order-management system that produced the original
decision: (a) the Census Bureau's AES system returns a fatal/hold response code at the time of Electronic
Export Information filing; (b) CBP detains or seizes cargo at the port of export, communicated to the
exporter or its forwarder; (c) BIS Office of Export Enforcement sends a subpoena or proposed charging
letter by mail. The company would get this by routing any AES rejection code, port hold notice, or BIS
letter into the product, tagged back to the original order/shipment ID, a manual "log this letter" step
at first, later an AES status-code pull if BIS/Census exposes one.

**6. D1, VERIFIED.** BIS's own enforcement page states: **"As of January 15, 2025, the maximum
administrative monetary penalty is $374,474 per violation or twice the value of the transaction,
whichever is greater."** Source: https://www.bis.gov/enforcement/penalties (fetched directly; confirmed
by raw HTML grep, not just a summarized fetch). Criminal exposure on the same page: up to 20 years
imprisonment and up to $1,000,000 in fines per violation under the Export Control Reform Act.
**Purchase frequency: inherent to the segment definition** (ships internationally at least monthly) but
the exact per-company shipment count is **NOT VERIFIED**, I did not find a published average.

**7. Computed or observed / paperwork or physical act:** Split answer, stated honestly. Determining the
textbook-correct ECCN is largely **COMPUTED**, a rules lookup against a public instrument (the Commerce
Control List), so a plain classification assistant has no moat here (Stage 1f applies). The thing this
candidate actually sells is a different, **OBSERVED** question: whether THIS company's own shipment
pattern resembles ones that historically drew scrutiny, which only accumulates by operating. Money sits
in the **paperwork**, the classification/licensing determination, though the trigger event (a hold,
a detention) attaches to a physical shipment.

**8. Competition fit:** It is a scoring API sitting inside the exporter's own order-entry workflow, whose
product is a compounding private ledger (this company's classification decisions matched to this
company's own downstream enforcement outcomes), not a per-shipment compliance-review service, and not
something a classification-lookup vendor accumulates today.

---

## Candidate 2: Documentary Credit Discrepancy Predictor

**1. Name:** Documentary Credit Discrepancy Predictor

**2. Tuple:**
- **Customer segment and band:** small-to-mid exporters (under 500 employees) that sell internationally
  under documentary letters of credit at least monthly, without an in-house trade-finance specialist to
  pre-check every document set.
- **Asset:** a private ledger of past document sets this exporter presented (invoice, packing list, bill
  of lading, certificate of origin, etc.) matched against what THIS exporter's specific issuing/
  confirming bank and examiner actually did with each one, accepted, waived, or rejected as discrepant , 
  which captures bank-specific and examiner-specific leniency that the plain UCP 600 text cannot.
- **Document set / state input:** the draft document set (commercial invoice, packing list, bill of
  lading, insurance certificate, etc., as text/JSON) plus the LC's own terms, scored before the exporter
  physically presents the documents to its bank.
- **The mistake:** presenting a document set the bank's examiner finds discrepant under UCP 600's
  strict-compliance standard.
- **The checker and the rule:** the issuing or confirming/negotiating bank's documentary examiner, under
  ICC Publication 600 (UCP 600) Articles 14 and 16, which require refusal of any non-complying
  presentation absent an applicant waiver.

**3. Differentiated claim:** An incumbent would already have to be claiming it can predict, bank-by-bank
and examiner-by-examiner, which specific document variances THIS exporter's own bank has actually waived
versus rejected in the past, not merely that it can run a UCP 600 text-matching checklist against the
LC's stated terms (existing LC-checking software already does the latter for free or near it).

**4. Question shape:** **Score** (place the document set on a 2-10 discrepancy-risk rubric, not a bare
yes/no) so the exporter's trade-finance staff can triage: green bands ship as-is, red bands get a human
look before mailing. Why sub-second/near-zero cost matters: exporters redraft the same document set
several times before presentation, and want instant feedback on each edit; a paid compliance review or
the bank's own up-to-five-banking-day examination window (UCP 600 Art. 14(b)) cannot support that
iteration loop.

**5. Where the outcome is observed:** By the exporter's trade-finance/AR team, when the negotiating or
issuing bank returns a SWIFT MT734 (Advice of Refusal) or a paper discrepancy notice, and/or when the
discrepancy fee is debited on the exporter's bank statement, both arriving through the bank's own
messaging/statement system, not the exporter's document-preparation software. The company would get this
by ingesting the bank notice or statement line item and tagging it back to the document-set ID that was
originally scored.

**6. D1, VERIFIED**, from three actual bank tariff schedules (fetched as PDF, extracted with
`pdftotext`, not a search summary):
- Standard Chartered Tanzania, Corporate & Investment Banking Tariff 2025: **"Discrepancy fee on each
  set of documents received with any discrepancy, USD 130"** (import side) and **"USD 120 or equivalent
  will be charged from the proceeds"** (export side).
  https://www.sc.com/tz/uploads/sites/73/content/docs/SCB-CIB-TARIFF-2025.pdf
- Hang Seng Bank (Hong Kong) Commercial Banking Service Charges, Import Bills: **"Discrepancy Fee , 
  HK$700"** (≈ USD 90). https://www.hangseng.com/content/dam/hase/en_hk/business/bank-accounts/PDF/Service%20Charges.pdf
- Bandhan Bank (India) Schedule of Charges for Trade Finance: **"Discrepancy fee per bill - import bill
  (on overseas beneficiary), USD 50."**
  https://bandhan.bank.in/sites/default/files/2026-07/Schedule-of-Charges-for-Trade-Finance-07072026.pdf
Honest caveat: the directly quoted bank fee is modest ($50-130 per set). The bigger cost, payment delay,
lost negotiating leverage if the buyer conditions waiver on a price concession, or non-payment if the
buyer refuses to waive, is real in the trade-finance literature but I found no published dollar figure
for it, so it is **NOT VERIFIED**.
**Purchase frequency, VERIFIED as a widely-repeated industry figure, sourced from two secondary pages I
fetched directly (not just a search snippet):** tradefinance.training states **"the percentage of
documents refused on first presentation ranges between 60-75%,"** attributed to ICC survey data; ovrseas.io
states **"According to ICC estimates, 60-75% of documentary credit presentations are refused on first
submission."** Both are secondary citations of ICC's own (unfetched) survey, marked VERIFIED at the
secondary-source level, not the ICC primary level.
https://www.tradefinance.training/blog/articles/discrepancies-in-documentary-credit-presentations/ ,
https://ovrseas.io/blog/lc-document-rejection-why-most-fail-first-try

**7. Computed or observed / paperwork or physical act:** Honest tension, per Stage 1f. Matching a
document set's text against the LC's stated terms is largely a **COMPUTED** inequality, an off-the-shelf
LC-checking tool already does deterministic matching. What is **OBSERVED** is the divergence between that
textual matching and what a specific bank/examiner actually did, banks routinely waive or enforce
variances beyond pure UCP text, and that pattern is only knowable by watching this exporter's own
outcomes accumulate. Money sits entirely in the **paperwork**, nothing physical returns; by the time
documents are presented the goods have typically already shipped, which is exactly the shape Stage 0c-i's
correction says produces a real, billed D1 (a third party, the bank, invoices for the mistake) rather
than a P&L-only phantom.

**8. Competition fit:** A scoring API over an exporter's own document-drafting workflow whose asset is a
private, bank-specific waive/reject ledger that compounds only by presenting real document sets to real
banks, not a static UCP-matching checklist, which any vendor can already sell.

---

## Candidate 3: Import Classification Audit-Risk Score

**1. Name:** Import Classification Audit-Risk Score

**2. Tuple:**
- **Customer segment and band:** mid-market importers of record (not customs brokers) that classify their
  own merchandise under the Harmonized Tariff Schedule in-house before handing entries to a licensed
  broker for filing, filing roughly 500 to 20,000 CBP entry summaries per year, without in-house trade
  attorneys reviewing every new SKU.
- **Asset:** a private ledger, per product line, of this importer's own past HTS classification decisions
  matched against what CBP actually did with those entries afterward, a clean liquidation, a Form 28
  Request for Information, a Form 29 Notice of Action (rate advance), a Focused Assessment finding, or a
  19 U.S.C. § 1592 penalty notice.
- **Document set / state input:** the new SKU's commercial description/spec sheet plus the proposed HTS
  code, scored before that classification is locked into the broker's ABI entry filing.
- **The mistake:** misclassifying merchandise (or misstating value or country of origin), discovered
  later at CBP audit or Focused Assessment.
- **The checker and the rule:** CBP's Office of Trade / Regulatory Audit, under 19 U.S.C. § 1592 and
  CBP's published Mitigation Guidelines.

**3. Differentiated claim:** An incumbent would already have to be claiming it can predict, from a
private ledger of THIS importer's own past CBP Form 28/29 and § 1592 history by product line, which new
SKUs are likely to draw a rate advance or penalty, not merely that it can look up the nominally correct
HTS code from the public tariff schedule (any HTS lookup tool already does that for free).

**4. Question shape:** **Score** (2-10 classification/audit-risk rubric) run in batch against every new
SKU added to the product master before it is locked into the entry-filing system. Why cost matters more
than raw speed here: product masters can add hundreds of new SKUs per cycle, and paying a licensed broker
or trade attorney to individually review each one is the actual incumbent cost this replaces; near-zero
per-line cost is what makes scoring the FULL SKU list feasible instead of only a sampled subset.

**5. Where the outcome is observed:** By the importer's own trade-compliance team, via CBP's ACE portal
or physical mail, when CBP issues a Form 28, Form 29, a Focused Assessment finding, or a § 1592
pre-penalty/penalty notice tied to a specific entry number, none of which lives in the product-master or
ERP system where the original classification was chosen. The company (or its broker, on its behalf) pulls
these from ACE and matches them back to the SKU/HTS pairing that was scored pre-filing.

**6. D1, VERIFIED, directly from the statute** (fetched from uscode.house.gov, the U.S. Code itself, not
a summary):
- Fraud: **"punishable by a civil penalty in an amount not to exceed the domestic value of the
  merchandise."**
- Gross negligence: penalty not to exceed the domestic value or **four times the lawful duties, taxes,
  and fees of which the United States is deprived**, or 40% of dutiable value if duties were unaffected.
- Negligence: penalty not to exceed the domestic value or **two times** the duty loss, or 20% of dutiable
  value if duties were unaffected.
https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-prelim-title19-section1592&num=0&edition=prelim
**Purchase frequency:** the classification DECISION recurs on every entry/new SKU, inherent to the
500-20,000 entries/year band that defines the segment, but the graded VERDICT (a full audit or § 1592
penalty) lands far less often per company; the more frequent, less severe verdict is a Form 29 rate
advance at the individual-entry level. This is the exact tension METHOD flags between physical arrival
and frequency; I am recording it rather than papering over it. Exact per-company audit/penalty frequency
is **NOT VERIFIED.**

**7. Computed or observed / paperwork or physical act:** Same honest split as Candidate 1. The nominally
"correct" HTS classification is largely **COMPUTED**, applying the General Rules of Interpretation to a
public tariff schedule and public CBP rulings (CROSS), so a bare classification assistant has no moat.
The defensible layer is **OBSERVED**: this importer's own private history of which of ITS product/HTS
pairings have actually drawn CBP scrutiny. Money sits in the **paperwork**, the code entered on the
entry summary, with no physical defect in the goods themselves, which avoids the round-16 trap where
object-return candidates had no verifiable price (here the biller is CBP, applying a published statute).

**8. Competition fit:** A classification-and-audit-risk scoring API sitting ahead of the broker's ABI
filing, whose asset is this importer's own CBP correspondence history mapped to product attributes, a
ledger that a classification-software vendor or the broker itself does not accumulate on a per-importer
basis today.

---

## Candidate 4: H-1B Petition RFE-Risk Score

**1. Name:** H-1B Petition RFE-Risk Score

**2. Tuple:**
- **Customer segment and band:** mid-size technology and IT-staffing/consulting employers filing roughly
  10 to 200 H-1B petitions per year through in-house immigration staff or outside counsel, without a
  dedicated RFE-analytics function of their own.
- **Asset:** a private ledger of this employer's own past petition fact patterns (role, wage level,
  degree match, job-duties language, employer-employee relationship structure, end-client placement
  details for staffing cases) matched against the actual USCIS adjudication outcome for that same
  employer over time, approval, RFE, or denial, because RFE triggers are service-center- and even
  adjudicator-specific patterns that are not published anywhere.
- **Document set / state input:** the petition support package (job description, wage-level
  justification, beneficiary credentials, end-client itinerary letters for staffing placements) as it
  sits in the immigration case-management software, scored before Form I-129 is filed with USCIS.
- **The mistake:** filing a petition that draws a Request for Evidence or denial, independent of whether
  the beneficiary is in fact qualified.
- **The checker and the rule:** USCIS service-center adjudicators, applying the specialty-occupation and
  employer-employee-relationship standards of 8 CFR § 214.2(h), with RFE authority under 8 CFR §
  103.2(b)(8).

**3. Differentiated claim:** An incumbent would already have to be claiming it can predict, from a
private ledger of THIS employer's own past USCIS outcomes by role, wage level, and service center, which
new petitions are likely to draw an RFE or denial, not merely that it can check the petition against the
published specialty-occupation criteria in 8 CFR § 214.2(h) (any immigration-software checklist already
does that).

**4. Question shape:** **Noul**, "will this petition draw an RFE, yes or no" with a probability, run
against each draft of the job description/wage-level/support letter before the final petition is
assembled. Honest answer on why-now: at 10-200 filings/year, per-event cost is not the binding
constraint, even a paid attorney glance would be affordable. The real "why now" is **latency**: an
immigration team wants to test several rewordings of a job description or duty list against the model in
minutes while drafting, which a human attorney review (typically a multi-day turnaround per draft) cannot
support as an iteration loop.

**5. Where the outcome is observed:** By the employer's immigration team or outside counsel, through
USCIS's online case-status system or physical mail, when USCIS issues an RFE, a Notice of Intent to Deny,
or a final approval/denial tied to the petition's receipt number, a system entirely separate from the
case-management software that assembled the original filing. The company logs the outcome against the
receipt number of the petition draft that was originally scored.

**6. D1, VERIFIED**, from a primary DHS fee schedule and a named industry policy brief (both fetched and
extracted, not summarized from a search snippet):
- USCIS Form G-1055 Fee Schedule (DHS, edition 09/09/26): Form I-907 premium processing for an I-129
  H-1B petition, **"Paper Filing: $2,965."** Base I-129 H-1B filing fee **$780** ($460 for a small
  employer/nonprofit), a mandatory **$500** Fraud Prevention and Detection fee on initial petitions, and
  a further **$4,000** fee under Pub. L. 114-113 for petitioners with 50+ U.S. employees where H-1B/L-1
  holders exceed 50% of staff. https://www.uscis.gov/sites/default/files/document/forms/g-1055.pdf
- National Foundation for American Policy, "H-1B Petitions and Denial Rates For FY 2024" (December
  2024), Table 9, "H-1B Legal and Government Fees For Employers": **"Attorney Fees if a Request for
  Evidence, $2,000 to $4,500"** (versus $1,500-$4,000 for the underlying petition itself), alongside a
  listed Premium Processing cost of $2,805 (the pre-March-2026 figure; USCIS's own schedule above shows
  it has since risen to $2,965).
  https://nfap.com/wp-content/uploads/2024/12/H-1B-Petitions-and-Denial-Rates-For-FY-2024.NFAP-Policy-Brief.December-2024.pdf
None of these fees is refunded if the petition draws an RFE; the RFE simply adds the second attorney-fee
line on top. **Purchase frequency:** inherent to the segment definition (10-200 filings/year, well above
the roughly-one-per-year bar). A specific current RFE incidence rate for FY2025-2026 was reported only by
aggregator/blog sources (e.g., a cited "24% of all H-1B petitions" and "RFE rates rising from roughly 9%
to over 30%") that I could not trace to a fetched primary USCIS or AILA document, **NOT VERIFIED.**

**7. Computed or observed / paperwork or physical act:** **OBSERVED**, whether a specific fact pattern
(this wage level, this job-duty phrasing, this service center) draws an RFE is not deducible from the
regulation text alone; it depends on adjudicator behavior that only shows up by watching outcomes
accumulate, which is exactly the kind of asset Stage 1f says a customer's own two documents cannot
produce by arithmetic. Money sits in the **paperwork**, the petition and its supporting letters, with
no physical act at all.

**8. Competition fit:** A scoring API sitting inside the employer's own immigration case-management
workflow, whose asset is a private, employer-specific outcome ledger (fact pattern -> RFE/approval) built
only by actually filing petitions and watching what USCIS does, not a static regulatory checklist, which
existing immigration case-management software already provides for free.

---

## VERIFIED / NOT VERIFIED source list

**VERIFIED (primary document fetched and read directly):**
- https://www.bis.gov/enforcement/penalties, BIS maximum civil penalty, $374,474 per violation or 2x
  transaction value (confirmed via raw HTML grep of the live page).
- https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-prelim-title19-section1592&num=0&edition=prelim
 , 19 U.S.C. § 1592(c), fraud/gross negligence/negligence penalty caps, quoted from the U.S. Code text.
- https://www.sc.com/tz/uploads/sites/73/content/docs/SCB-CIB-TARIFF-2025.pdf, Standard Chartered
  Tanzania CIB tariff, LC discrepancy fee USD 130 / USD 120 (extracted with `pdftotext`).
- https://www.hangseng.com/content/dam/hase/en_hk/business/bank-accounts/PDF/Service%20Charges.pdf , 
  Hang Seng Bank service charges, LC discrepancy fee HK$700 (extracted with `pdftotext`).
- https://bandhan.bank.in/sites/default/files/2026-07/Schedule-of-Charges-for-Trade-Finance-07072026.pdf
 , Bandhan Bank trade finance schedule, discrepancy fee USD 50 per import bill (extracted with
  `pdftotext`).
- https://www.uscis.gov/sites/default/files/document/forms/g-1055.pdf, USCIS/DHS Form G-1055 fee
  schedule: I-907 premium processing $2,965 for I-129 H-1B; base fee $780; Fraud Prevention fee $500;
  Pub. L. 114-113 fee $4,000 (extracted with `pdftotext`).
- https://nfap.com/wp-content/uploads/2024/12/H-1B-Petitions-and-Denial-Rates-For-FY-2024.NFAP-Policy-Brief.December-2024.pdf
 , NFAP Table 9, attorney fee for an RFE response $2,000-$4,500 (extracted with `pdftotext`).

**VERIFIED at the secondary-citation level only (fetched and read directly, but citing an unfetched ICC
primary survey):**
- https://www.tradefinance.training/blog/articles/discrepancies-in-documentary-credit-presentations/ , 
  "the percentage of documents refused on first presentation ranges between 60-75%."
- https://ovrseas.io/blog/lc-document-rejection-why-most-fail-first-try, "According to ICC estimates,
  60-75% of documentary credit presentations are refused on first submission."

**NOT VERIFIED (no primary source found; not used as a load-bearing number):**
- Dollar cost of an LC discrepancy beyond the bank's own quoted fee (delay, negotiating leverage, risk of
  non-payment).
- Per-company shipment frequency for the export-control candidate.
- Per-company CBP audit/§ 1592 penalty frequency for the customs-classification candidate.
- Current (FY2025-2026) H-1B RFE incidence rate, only aggregator/blog figures found (~24%; "9% to over
  30%"), not traced to a fetched primary USCIS/AILA report.
