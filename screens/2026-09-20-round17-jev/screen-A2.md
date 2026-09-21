# Screen: Candidate 2, Documentary Credit Discrepancy Predictor

Blind screen, round 17. Candidate source: `ideation-A.md` lines 79-158. Ladder per `METHOD.md` Part 3
(kill/score split, C-72). No subagents spawned; all searches run directly. `predictions/` not read.

---

## 1. THE CASE FOR

**Strongest demand tier: D1, VERIFIED, already established by the ideation agent and re-checked here for
tense and currency (both tariffs are 2025/2026-dated, live, not archived).** Three banks' own published
tariff schedules price the mistake itself: Standard Chartered Tanzania **"Discrepancy fee on each set of
documents received with any discrepancy, USD 130"**
(https://www.sc.com/tz/uploads/sites/73/content/docs/SCB-CIB-TARIFF-2025.pdf); Hang Seng Bank **"Discrepancy
Fee, HK$700"** (≈USD 90) (https://www.hangseng.com/content/dam/hase/en_hk/business/bank-accounts/PDF/Service%20Charges.pdf);
Bandhan Bank **"Discrepancy fee per bill - import bill (on overseas beneficiary), USD 50"**
(https://bandhan.bank.in/sites/default/files/2026-07/Schedule-of-Charges-for-Trade-Finance-07072026.pdf).
This is D1's floor, not its ceiling, see the honest caveat under weaknesses below.

**Strongest rung-2 pass: the instrument binds the customer directly, confirmed from the rule-writer's own
text, not a summary.** ICC Banking Commission Technical Advisory Briefing No. 3 (27 June 2022, free PDF,
fetched and read with `pdftotext`, https://library.iccwbo.org/content/tfb/BRIEFINGS/20220627_TA_Briefing_No3_reducing_discrepancy_rates.pdf)
quotes UCP 600 sub-article 14(a) directly: banks **"must examine a presentation to determine, on the basis
of the documents alone, whether or not the documents appear on their face to constitute a complying
presentation."** The refusal notice under Article 16 goes to **the presenter**, the exporter/beneficiary,
who is this candidate's customer, not to the buyer's bank or any other counterparty. **No K2: the wrong
party is not being charged.**

**Best structural finding, not in the demand ladder but load-bearing for criterion 5:** rung 5c passes
cleanly. Unlike a skilled-nursing referral (where a DECLINE is never graded), essentially every LC
presentation is examined and returns one of two labels, accepted or refused, so **both branches the
model can output get graded, on almost every transaction**, which is a genuinely rare property on this
board. Base rate is also unusually balanced: ICC's own historical range, **"65-80%"** refused on first
presentation (same ICC briefing, ISSUE section), is nowhere near cargo-theft-style rarity, so there is real
class balance to learn from.

---

## 2. THE SCORED WEAKNESSES

- **Rung 1 (magnitude), criterion 3.** The only VERIFIED dollar figure is the bank's own discrepancy fee,
  **$50-130 per set** (sources above), modest. The ideation file's own honest caveat stands: the larger
  claimed cost (payment delay, lost negotiating leverage, non-payment if the buyer refuses to waive) has
  **no published dollar figure anywhere I found** and is **NOT VERIFIED**. ICC Opinion R441 (TA487), quoted
  in the same briefing, adds a further limiter: **"if an issuing bank intends to deduct a discrepancy fee
  the credit should contain a condition to this effect together with an indication of the fee"**, the fee
  is a per-credit contractual term set unilaterally by each bank, not a mandated floor, so it cannot be
  generalized across customers without checking each customer's own LC wording.

- **Rung 1.5 (patent), criterion 4.** Google Patents search on the differentiated claim ("predict, per
  issuing/confirming bank and examiner, which document variances will be waived vs. rejected, from that
  exporter's own presentation history") returned no hit reading on it. The nearest analog found, a "cash
  account discrepancy predictor" ML patent (https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12266022),
  is a different domain (bank cash-account reconciliation, not documentary credits) and does not narrow to
  trade finance. **Clean not-found, a finding, not a gap in the search.**

- **Rung 3, GIVES, criterion 4 (heaviest rung-3 finding).** A major issuing/negotiating bank already gives
  the mechanical half of this away for free to its own export customers. J.P. Morgan Chase's **"Export
  Letter of Credit Guide"**, addressed **"To: Our Export Customers"** (fetched and read directly,
  https://www.jpmorgan.com/content/dam/jpm/commercial-banking/documents/international-banking/export-letter-credit.pdf),
  bundles an **"Export Letter of Credit Checklist"** and a document titled **"Most Common Discrepancies in
  Letter of Credit Documents"**, free, unprompted, handed to the exact customer segment this candidate
  targets. It is generic (not bank/examiner-specific), so it does not reach the differentiated claim, but
  it removes exactly the "does a free checklist already exist" question at rung 3's own instruction ([C-9]).

- **Rung 3, PUBLISHES, criterion 4.** ICC Banking Commission Briefing No. 3 (same source as above) is the
  standard-setter publishing both the failure taxonomy and the fix, for free: it lists the common
  discrepancy causes verbatim and closes with **"Each bank has a duty to educate its own staff… it is
  desirable that each bank educate their clients"** and a bulleted list of **"simple tasks that can help to
  reduce discrepancy rates."** This is the free substitute for the generic/systemic half of the problem;
  the residue it leaves unaddressed is explicit in its own text, refusals **"owing to… lack of UCP and/or
  ISBP and/or ICC Opinion knowledge of the document examiner"**, i.e., ICC itself attributes some
  refusals to the individual examiner's own judgment, which is exactly the private, examiner-specific
  variance this candidate's asset claims to capture. **The residue is real but ICC's own briefing shows it
  is a subset of causes, not the majority** (poor drafting and beneficiary document errors are named first).

- **Rung 3, competitor GIVES/scale, criterion 4.** Traydstream (fetched directly, https://traydstream.com/for-exporters)
  already sells a live, funded "pre-doc check" product to exporters: it **"digitizes trade finance
  documents, extracts structured and unstructured data, and validates it against 250,000+ trade and
  compliance rules,"** checks **"Automated Global Trade Rules (UCP, ISBP)"** and **"Letter of Credit (LC)
  Conditions,"** and names a live customer, Vinmar International, with a stated outcome in its own words:
  reducing **"days sales outstanding (DSO), and time-to-market"** via **"AI based document pre-checks."**
  G1 and G2 are both quoted here. **G3 (the differentiated claim's own outcome) is missing**: nothing on
  either fetched Traydstream page (the `/ucp-600-rules/` URL 404s, NOT VERIFIED, dropped) claims
  bank-specific or examiner-specific historical waive/reject prediction; the page describes standard
  rule-matching only. So this scores criterion 4 hard on the mechanical half of the claim without killing
  it (see KILL section).

- **Rung 4, empty-category reasoning, criterion 4.** No vendor page found (Traydstream, CGI Trade360,
  Surecomp, Finastra all checked) claims bank-specific or examiner-specific historical leniency
  prediction. Per C-53 this must be explained, not just recorded as an opening: **reason (ii) applies**, a
  free/near-free actor (ICC + individual issuing banks + Traydstream's generic pre-check) already covers
  the profitable, high-volume mechanical-matching half of the value, which likely suppresses demand for a
  narrower paid layer on top of it. Reason (iii) is a live, unresolved possibility too (see D3 below).
  Reason (i), legal foreclosure on assembling the ledger, has no supporting evidence; the exporter is a
  party to its own presentation outcomes, so no counterparty confidentiality clause was found that would
  bar it (none searched foreclosed this; recorded as searched, not found, see VERIFIED/NOT VERIFIED list).

- **Rung 4, exited predecessor, criterion 4.** Searched for abandoned patents, paused products, and Wayback
  captures of a discontinued documentary-credit discrepancy-prediction product. **Found nothing**, a
  clean not-found, not a gap. No buyer's guide for this specific narrow category was found either (broader
  trade-finance-software "top 10" roundups exist and name Traydstream/Surecomp/CGI/Finastra, but none
  singles out bank-specific discrepancy prediction as a category).

- **Rung 5b (attribution), criterion 5, mild, not fatal.** The outcome (MT734 refusal notice or a fee
  line-item) is itemized per presentation, which is good, but it is not confounded-free: whether a given
  discrepancy is waived depends partly on the **applicant's own commercial willingness to waive** (Art
  16(b)) rather than purely the examiner's judgment, so some of the "waived vs. rejected" label reflects
  the buyer's negotiating posture, not a stable bank/examiner pattern. This is a real but partial
  confound, not a 5a failure (the outcome still comes back to the customer).

- **Rung 6, criterion 6, partial.** Countable, VERIFIED source found (Federal Reserve, fetched directly,
  https://www.federalreserve.gov/econres/notes/feds-notes/trade-finance-activities-of-u-s-banks-what-the-data-can-tell-us-20260508.html):
  **"Commercial letters of credit: approximately $15 billion"** outstanding and **"$15-25 billion"**
  quarterly in LC-financed exports (Q4 2024/2024 estimates), concentrated among roughly 90 reporting
  institutions, with **"the five largest trade finance providers account for more than 75 percent of all
  trade finance loans."** This sizes the **bank-side** volume, not the number of small-to-mid exporter
  customers in the named segment, no countable figure for that customer count was found (searched;
  Liberty Street Economics' 2013-era **"7.6 percent of exports"** figure is stale and firm-count was never
  stated even then). **Segment sizing is bank-volume-derived, not customer-count-derived, a real gap on
  criterion 6.**

---

## 3. KILL

**NO KILL.**

- **K1 not fired.** No published incumbent fee floor for a *predictive* product exists to compare against;
  the only floor found (the bank's own $50-130 discrepancy fee) is a cost the product would help the
  customer avoid, not a competing price the product must beat. Customer control-of-money is intact: the
  presenter (customer) is the one who decides whether to present, correct, or accept the fee.
- **K2 not fired.** UCP 600 Art. 14/16, quoted directly above from ICC's own briefing, binds the presenter
  (the customer) as the party examined and notified. Right instrument, right duty-holder.
- **K3 CANDIDATE not fired.** Traydstream clears G1 (own product page) and G2 (named deployment, Vinmar,
  in the customer segment) for the **mechanical UCP/ISBP rule-matching** half of the claim, with a stated
  outcome (DSO, time-to-market). But the **differentiated claim**, bank-specific, examiner-specific
  historical waive/reject prediction, is not made on Traydstream's page, JPMorgan's guide, ICC's briefing,
  or any other vendor page found (CGI Trade360, Surecomp, Finastra checked). All three of G1+G2+outcome
  are required on the *same* claim for K3; here they are satisfied only for the narrower, undifferentiated
  half of the product, which the room scores on criterion 4 rather than killing (Veer, 2026-09-07: "comp
  should score not kill unless its actually already solved").
- **K4 not run.** This is a desk screen; no operator call was made.

---

## 4. D3 STATE

**UNRUN, with a negative-leaning signal, not EMPTY, not FILLED.**

Two directly-fetched, non-bank-blocked job-description sources were checked because ZipRecruiter, Indeed,
Glassdoor and similar boards are known to 403 the fetcher (established toolchain limit, not re-tested
here per instruction not to re-verify established facts):

- AgCareers' own career profile for **"Export Documentation Specialist"** (fetched directly,
  https://www.agcareers.com/career-profiles/export-documentation-specialist.cfm) lists real duties , 
  auditing shipment documentation, sanctioned-party screening, freight-forwarder coordination, and
  **contains no mention of letters of credit, discrepancy checking, or bank presentation at all.**
- VelvetJobs' generic "Export Specialist" template (fetched directly,
  https://www.velvetjobs.com/job-descriptions/export-specialist) does list LC duties, but reads as
  bank-side leakage into a generic template: **"Drafts, develops, updates and prepares letters of credit
  for all areas of the Bank"**, a duty that belongs to the issuing/confirming bank's own staff, not the
  exporter-customer's.

Together these two fetched pages point toward the D3 state **FILLED AT THE COUNTERPARTY** for the specific
document-checking task (the bank employs the examiner who does this; see the widely-repeated but only
title-level $18.75-$26.44/hr "Documentary Credit Specialist" band, **NOT VERIFIED AT PAGE**, ZipRecruiter
being one of the blocked boards) rather than FILLED AT THE CUSTOMER. A search-engine summary (not a
fetched page) had earlier suggested an exporter-side "Export Documentation Specialist" posting explicitly
includes "reviewing Letter of Credit (L/C) requirements", that specific claim did **not** survive being
checked against the one fetched exporter-side career profile available, so per rule 7 it is **discarded,
not reported as a finding.** This toolchain gap means the customer-side D3 question cannot be answered
past UNRUN; it should not be read as EMPTY, but the two data points available lean toward the labor being
on the bank's side of the transaction, which, per rung 2's own note that "who actually feels the pain" and
"is the budget line on the other side" both belong at rung 2, modestly reinforces rather than
contradicts the K2 pass (the pain is the customer's; the pre-existing labor to prevent it may not be).

---

## 5. MUTATION

**Forcing evidence exists; a narrower formulation is worth naming, though this screen proposes only.**

The evidence gathered points at one specific gap rather than the whole candidate: the mechanical
UCP/ISBP-matching layer is already free or cheap and widely distributed (ICC's own guidance, JPMorgan's
free customer checklist, Traydstream's live product with a named, quoted deployment). Nobody found makes
the narrower claim, a private, bank-and-examiner-specific waive/reject ledger built from one exporter's
own presentation history. That narrower claim is exactly what stays alive after this screen. **The forcing
evidence is Traydstream's own page plus JPMorgan's own checklist**: both establish that "does this document
set match UCP 600" is already commoditized, so a formulation that competes on that mechanical layer is
racing a funded, live incumbent for free; a formulation that positions as a **decision layer sitting on top
of an exporter's existing document-prep tool** (its own or a competitor's), scoring only the residual
bank-specific leniency question, is the version this evidence supports. This is a proposal for Veer's
consideration, not a mutation performed here.

---

## 6. RUBRIC SCORES

VERIFIED evidence only, no operator call made (criterion 3 caps at 4 regardless of ladder outcome).

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Clarity of target customer | 3 | Segment named (small-mid exporters, LC-monthly, no in-house specialist), but D3 evidence (below) creates real tension with the "no in-house specialist" framing that was not resolved |
| 2 | Clarity of JTBD | 4 | One clean sentence a practitioner would recognize; not scored 5 because no operator confirmed it in their own words |
| 3 | Significance and magnitude of unmet need | **2** | Only one demand tier cleanly clears (D1, verified, but modest at $50-130/set); D3 is UNRUN with a negative lean, not a second clean tier; no salience call |
| 4 | Differentiation and uniqueness | 3 | No K3; but a funded, live competitor (Traydstream) plus two free incumbent giveaways (ICC, JPMorgan) already cover most of the addressable claim, leaving only a narrow, unclaimed residual |
| 5 | Performance improvement over existing solutions | 3 | Structurally sound compounding loop (5c passes cleanly, base rate balanced), but no measured number exists yet |
| 6 | Size of market opportunity | 3 | Countable Federal Reserve source found ($15B outstanding, $15-25B/quarter), but it sizes bank-side volume, not the customer segment's own count |
| 7 | Market / technical / execution risk | 3 | Buildable on Jev given text/JSON input; cold start is thin, only the customer's own presentation history, which accrues slowly and is mostly the already-commoditized mechanical signal |

**Lowest criterion: 3 (magnitude and significance of unmet need). Sum: 21.**

---

## 7. VERIFIED / NOT VERIFIED

**VERIFIED (fetched and read directly, quotes above):**
- https://www.sc.com/tz/uploads/sites/73/content/docs/SCB-CIB-TARIFF-2025.pdf
- https://www.hangseng.com/content/dam/hase/en_hk/business/bank-accounts/PDF/Service%20Charges.pdf
- https://bandhan.bank.in/sites/default/files/2026-07/Schedule-of-Charges-for-Trade-Finance-07072026.pdf
- https://library.iccwbo.org/content/tfb/BRIEFINGS/20220627_TA_Briefing_No3_reducing_discrepancy_rates.pdf
- https://www.jpmorgan.com/content/dam/jpm/commercial-banking/documents/international-banking/export-letter-credit.pdf
- https://www.federalreserve.gov/econres/notes/feds-notes/trade-finance-activities-of-u-s-banks-what-the-data-can-tell-us-20260508.html
- https://traydstream.com/for-exporters
- https://www.agcareers.com/career-profiles/export-documentation-specialist.cfm
- https://www.velvetjobs.com/job-descriptions/export-specialist
- https://image-ppubs.uspto.gov/dirsearch-public/print/downloadPdf/12266022 (checked for a rung-1.5 hit; confirmed off-topic)

**VERIFIED at secondary-source level only (established by the ideation agent, re-cited, not re-fetched
per instruction):**
- https://www.tradefinance.training/blog/articles/discrepancies-in-documentary-credit-presentations/
- https://ovrseas.io/blog/lc-document-rejection-why-most-fail-first-try

**NOT VERIFIED / dropped:**
- https://traydstream.com/ucp-600-rules/, 404, not found, dropped
- Any exporter-side job posting explicitly naming "reviewing Letter of Credit (L/C) requirements" as a
  duty, appeared only in a search-engine summary, did not survive a fetch of the one available
  exporter-side career profile, discarded per rule 7
- ZipRecruiter "Documentary Credit Specialist" $18.75-$26.44/hr band, title-level only, page itself not
  reachable (known 403 toolchain limit)
- "Quality Letters of Credit, Inc." money-back guarantee claim (appeared only in a FasterCapital-style
  aggregator summary), could not find or confirm the company's own page; not cited above, not counted as
  a finding
- Any figure on the larger downstream cost of a discrepancy (payment delay, lost negotiating leverage,
  non-payment), searched, nothing published found, remains NOT VERIFIED as the ideation file itself
  already flagged
