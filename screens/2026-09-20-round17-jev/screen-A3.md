# Blind screen, Candidate 3: Import Classification Audit-Risk Score

Round 17, Jev. Screened against `METHOD.md` Parts 1, 2, 2b, 2c, 3, 7 and `STATE.md` -> THE ROOM.

---

## 1. THE CASE FOR

The strongest demand tier is **D1, VERIFIED directly from the U.S. Code** (not a summary): 19 U.S.C.
§ 1592 sets penalties for misclassification up to the domestic value of the merchandise (fraud), or up to
**four times** the duty loss / 40% of dutiable value (gross negligence), or **two times** the duty loss /
20% of dutiable value (negligence).
https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-prelim-title19-section1592&num=0&edition=prelim
(re-confirmed against Cornell LII, https://www.law.cornell.edu/uscode/text/19/1592, same operative
figures).

The strongest rung-2 pass: the duty-holder check is clean. The statute's civil-penalty regime runs against
"the person" who enters merchandise by a material false statement, the importer of record is that
person, matching this candidate's customer exactly (K2 does not fire; see Part 3 below).

The best D-tier beyond D1 is **D3, FILLED AT THE CUSTOMER**: a "Trade Compliance Manager" role whose
duties include "determining and/or reviewing HTS classification, customs valuation, country of origin,
marking requirements, duty treatment" exists at scale, averaging **$135,096/year** (Glassdoor) and
**$133,100/year** (Salary.com), both aggregator surveys, title-level, not read at an employer's own ATS
(toolchain limit, see D3 STATE below).
https://www.glassdoor.com/Salaries/trade-compliance-manager-salary-SRCH_KO0,24.htm
https://www.salary.com/research/salary/posting/trade-compliance-manager-salary

---

## 2. THE SCORED WEAKNESSES

**Rung 1.5 (patent search).** No granted claim reads on "predict CBP audit/penalty risk for a new SKU from
a private ledger of that importer's own past Form 28/29/§1592 history." The nearest hits are (a)
WO2016057000A1, a machine-learning method that *assigns* an HS code from historical data (classification,
not audit-risk prediction) and (b) a World Customs Journal paper, "Data mining in customs risk detection
with cost-sensitive classification", government-side risk *targeting* research, not an importer-facing
product. Neither is close enough to score as a hit, but neither is a clean field either. **Weakness:
none scored; recorded as a clean patent search.**
https://patents.google.com/patent/WO2016057000A1/en
https://www.worldcustomsjournal.org/article/116219-data-mining-in-customs-risk-detection-with-cost-sensitive-classification/attachment/223059.pdf

**Rung 2, AMNESTY, heaviest finding on this rung.** 19 U.S.C. § 1592(c)(4), quoted directly from Cornell
LII: a valid prior disclosure, made before CBP opens a formal investigation, caps the penalty at **"the
interest ... on the amount of lawful duties, taxes, and fees of which the United States is or may be
deprived,"** for both negligence and gross negligence, regardless of whether duties were affected, so
long as the importer tenders the unpaid duties within 30 days of CBP's notice. This is dramatically below
the headline "up to 4x duty loss / 40% of value" figure D1 quotes. **Weakens criterion 3 (magnitude):** the
real expected cost of a misclassification an importer catches and discloses itself, at any point before
CBP opens an investigation, is bounded near the interest on the duty shortfall, not the statutory
multiplier. A predictive pre-filing score competes against "just self-disclose if you ever find out," which
is cheap and needs no product.
https://www.law.cornell.edu/uscode/text/19/1592

**Rung 2, FREE PUBLISHED GUIDANCE.** CBP's own Informed Compliance Publication, "Reasonable Care," gives
importers a free checklist for exactly the pre-entry classification-risk judgment this candidate scores
(has the importer used a broker or in-house expert, sought a binding ruling, checked CROSS, etc.).
**Weakens criterion 4:** the free instrument covers the qualitative half of the same judgment.
https://www.cbp.gov/sites/default/files/assets/documents/2018-Mar/icprescare2017revision.pdf

**Rung 2, FREE SELF-INVOCABLE INSTRUMENT.** CBP's binding ruling program (NCSD eRulings) is confirmed
**free of charge**, with rulings issued within **30 calendar days** of receipt (90 days if referred to
Headquarters). Any importer uncertain about a new SKU's classification can eliminate the audit-risk
question entirely, for $0, by asking CBP directly. **Weakens criterion 4 and criterion 5 (residue):** the
product's real value is confined to SKUs where the 30-day wait is unacceptable given product-master
cycle time, or where the importer does not want to create a CROSS-visible public precedent. That residue is
real but narrower than "every new SKU," which is the candidate's own stated batch-scoring use case.
https://www.cbp.gov/trade/rulings/eruling-requirements

**Rung 2, portal terms of use / pooling.** The ACE Secure Data Portal's Terms and Conditions are published
at 72 FR 27632 (2007-05-16); full text could not be fetched (search engines and the Federal Register PDF
were not reachable in this session, a toolchain limit, not a finding). **Not scored, recorded as
UNRUN.** This matters less than in a cross-customer-pooling candidate, because the asset as described (a
per-importer private ledger of that importer's own CBP correspondence) is single-tenant, not a
cross-customer pool; there is no described act of one importer's outcomes flowing into another's model, so
the pooling/confidentiality-clause risk that has foreclosed other candidates in this file does not appear
to apply the same way here. Flagged as unverified rather than asserted clean.

**Rung 2, CBP HQ H350722 (2026-01-16), the customs-business/licensing structural risk.** This is the exact
ruling `METHOD.md` Part 2c already cites for AI-and-classification candidates. Confirmed via a secondary
source quoting the ruling directly (primary CROSS page would not render readable text in this session , 
JS-rendered, a toolchain limit): **"If the Unlicensed Company's AI classification tool only derives
potential HTSUS subheadings to the six-digit level, then customs business is not being conducted."** The
ruling's six-digit/output-a-code threshold is squarely about tools that *propose a classification*. This
candidate's product does not propose a classification, it scores audit risk against a classification the
importer (or its broker) already chose, so it sits one step further from the line than the tool H350722
addressed. **Not a K2 fire** (no instrument text names a risk-scoring tool as customs business), but it is
a live, unresolved nexus question the file's own escape-2 logic requires be asked before building: **(a) is
the decision sold the classification itself, or only a risk flag on someone else's decision, and (b) how
low is the nexus threshold**, HQ 115248 (2001) sets it at mere *possibility* that "corrected classification
information derived from the verification process will end up on the entry." If a high-risk score
predictably causes the broker to change the code, a regulator could plausibly read that as influencing the
entry's classification. **Weakens criterion 7 (execution risk):** this needs actual legal diligence, not
just a favorable reading of one ruling, before productizing.
https://diaztradelaw.com/even-ai-needs-a-license-know-when-automation-unlawfully-crosses-into-customs-business/
https://gingercontrol.com/blog/hts-classification-six-digit-broker-requirement

**Rung 3, RATCHET.** The conservative answer (classify at the higher-duty, harder-to-challenge code) is
already free and requires no product; the only answer worth paying for is the less-conservative,
lower-duty code, which is exactly the one this tool cannot make legally safe to act on (a probability score
is not a binding ruling). **Weakens criterion 5:** the saleable half is the half the customer cannot
actually rely on without separately confirming it, e.g., via the free ruling process above.

**Rung 3, CAPTURES (upstream).** Flexport's own product page states: **"In 2025 we introduced the
customs industry's first AI auditor which audits 100% of entries before we transmit them to the U.S.
government,"** reporting the error rate found in manual compliance audits fell to **"just 0.2%,"** which
Flexport says is "more than 10 times lower than any competitor." A second Flexport tool, "Audit Your
Customs Broker," analyzes 100% of a company's historical entries for HTS, tariff, valuation and SPI
errors. This is a broker building free-to-its-own-customers pre-filing and post-filing audit tooling
directly into the brokerage relationship, the exact CAPTURES shape (a checker-adjacent party builds a
tool that removes the mistake at the point of filing, rather than selling a prediction about it).
**Weakens criterion 4 (this is real, quoted, quantified competition)**, though it does not meet the K3 bar:
Flexport's tool audits entries it is itself about to file as broker, using general classification/valuation
rules, nothing on the page claims it uses a per-importer private ledger of that importer's own past CBP
Form 28/29 or §1592 history to score SKUs not yet filed with any broker, which is this candidate's specific
differentiated claim. G1 exists (own page); a G2 deployment matching this exact segment (importers who
classify in-house before handing off to an *external* broker, rather than to Flexport-as-broker) and a
customer-quoted outcome (not just Flexport's own words) were not found. **K3 CANDIDATE not established , 
recorded as a rung-4 SCORE, not a kill.**
https://www.flexport.com/products/customs/

**Rung 5c, unlabeled branch.** When the score flags a SKU as high-risk and the importer changes the code
or gets a binding ruling instead of filing the original code, CBP never issues a Form 28/29/FA finding/
§1592 notice on the code that was avoided, so the model's highest-value predictions (the ones acted on)
are precisely the ones that never receive a graded outcome. Feedback only arrives for codes the importer
filed anyway (mostly the low-risk-scored ones) or where the model was silent and something happened
regardless. This is the same shape `METHOD.md` names for the skilled-nursing decline problem.
**Weakens criterion 5 (compounding moat):** the tool cannot fully learn from its own best interventions.

**Rung 6, economics floor, NOT VERIFIED at the segment.** Total active U.S. importer-of-record numbers:
**~300,000-350,000** (CBP Broker Management Branch, cited in a 2019 Federal Register notice; a separate
2016 CBP Commissioner figure cites "over 300,000 active unique importer-of-record numbers," 30.4M
transactions, $2.4T in imports). No source was found that breaks this down by the candidate's specific
500-20,000-entries/year band. **Weakens criterion 6:** the addressable universe is bounded by a real,
cited total, but the actual target segment's size is asserted, not counted.
https://www.federalregister.gov/documents/2019/08/14/2019-17179/customs-broker-verification-of-an-importers-identity

**Checked and NOT found (recorded so nobody re-runs these searches):**
- No fee-shifting provision in 19 U.S.C. § 1592 or its CIT procedure ("prevailing party," "attorney's
  fees") was found, FEE-SHIFT does not fire.
- No tariff-classification-specific insurance/indemnity product was found; a customs bond is confirmed
  **not insurance**, the surety pays CBP and then collects from the importer under the indemnity
  agreement, so ABSORB does not fire.
- The Importer Self-Assessment program, which gave free CBP-side entry-summary trade data (ITRAC) to
  participants, was **discontinued for new applicants in 2020**, replaced by "Trusted Trader" concepts , 
  a dead predecessor, not a live free substitute.
  https://www.federalregister.gov/documents/2018/09/21/2018-20581/discontinuation-of-customs-broker-importer-self-assessment-pre-certification-test

---

## 3. KILL

**NO KILL.** No K1 (the statute prices the mistake in real dollars the importer controls avoiding, by not
misclassifying, or mitigating, by disclosing, the money is real and moveable). No K2 (the importer of
record is the named duty-holder under §1592; the instrument binds the customer, not a counterparty). No
K3 CANDIDATE (Flexport's AI auditor is the closest competitor found, and it is real, quoted, and
quantified, but it does not make this candidate's specific claim on its own page, and no deployment in
this exact segment with an outcome in a customer's own words was found). The CBP HQ H350722 licensing
question is a live structural risk, scored on criterion 7, not a kill, no instrument text was found that
names a risk-scoring (as opposed to classification-proposing) tool as "customs business."

---

## 4. D3 STATE

**FILLED AT THE CUSTOMER**, at the band, title-level. "Trade Compliance Manager" postings whose duties
name HTS classification review exist and average **$133,100-$135,096/year** (Glassdoor, Salary.com) , 
these are aggregator salary-survey pages, not a live posting read at an employer's own ATS or a state/
university portal, so per this file's standing toolchain limit (every major job board 403s the fetcher)
this is **title-level and NOT VERIFIED AT PAGE**, not a live posting count. No specific posting count was
obtained (search-engine job-board listings for "HTS classification analyst" and "tariff classification"
roles exist on Indeed/Glassdoor/ZipRecruiter/SimplyHired but could not be fetched and counted). Recorded as
FILLED AT THE CUSTOMER rather than UNRUN because the salary-survey evidence is a genuine, if weak,
signal that a budget line for this exact task exists at this segment size, but it is the seat, not the
specific answer this candidate sells (audit-risk *prediction*, as opposed to classification review itself),
so it sits closer to the "FILLED, TASK ABSENT" state than a clean FILLED-AT-CUSTOMER hit. Recording both
readings rather than picking one: **FILLED AT THE CUSTOMER / FILLED-TASK-ABSENT boundary case.**

---

## 5. MUTATION

Does the evidence force a different formulation? **NONE**, with one qualification worth naming rather than
treated as a forcing fact: the rung-2 finding on CBP HQ H350722 suggests the safer formulation sells
*only* the risk score as an internal triage/prioritization signal that never itself proposes or changes an
HTSUS code, which is already how the candidate is written ("scored... before it is locked into the
broker's ABI entry filing," not "assigns the code"). No evidence gathered here contradicts that framing or
requires a different customer, asset, or mistake. **No principled mutation exists.**

---

## 6. RUBRIC SCORES

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Clarity of target customer | 4 | Named precisely (mid-market importer, 500-20k entries/yr, no in-house counsel reviewing every SKU); count of firms in the exact band NOT VERIFIED |
| 2 | Clarity of JTBD | 3 | Well-specified but not evidenced in a practitioner's own words (no D5/D6 quote gathered) |
| 3 | Significance and magnitude of unmet need | 3 | D1 verified + D3 filled reaches two tiers, but no salience call was run (caps at 4 regardless) and the prior-disclosure amnesty (§1592(c)(4)) meaningfully compresses the real-world magnitude below the headline multiplier |
| 4 | Differentiation and uniqueness | 2 | Real, quoted, quantified competition found (Flexport's AI auditor, CBP's own free reasonable-care checklist, the free binding-ruling program) that narrows the space this candidate's exact claim can still occupy, short of K3 |
| 5 | Performance improvement over existing solutions | 2 | RATCHET (the saleable output is the one the customer can't safely act on) and the rung-5c unlabeled-branch problem (the model doesn't get graded outcomes on its own best-acted-on predictions) both weigh on the compounding story |
| 6 | Size of market opportunity | 2 | A countable total exists (~300-350k active US importers, CBP/Federal Register) but the specific 500-20k-entry band is not sized from any source found |
| 7 | Market/technical/execution risk | 3 | Buildable as a scoring model over existing structured data, but the CBP HQ H350722 "customs business" nexus question is real, unresolved, and needs legal diligence before productizing |

**Lowest criterion: 2** (tied on criteria 4 and 5). **Sum: 19.**

---

## 7. VERIFIED / NOT VERIFIED

**VERIFIED (fetched and read, not summary-only):**
- 19 U.S.C. § 1592 penalty structure, https://uscode.house.gov/view.xhtml?req=granuleid%3AUSC-prelim-title19-section1592&num=0&edition=prelim and cross-checked at https://www.law.cornell.edu/uscode/text/19/1592
- 19 U.S.C. § 1592(c)(4) prior-disclosure penalty cap, quoted verbatim, https://www.law.cornell.edu/uscode/text/19/1592
- CBP eRulings program is free, 30-day (90-day HQ) turnaround, https://www.cbp.gov/trade/rulings/eruling-requirements
- Flexport's AI auditor claim and 0.2% error-rate figure, on Flexport's own product page, https://www.flexport.com/products/customs/
- ISA program discontinued for new applicants in 2020, https://www.federalregister.gov/documents/2018/09/21/2018-20581/discontinuation-of-customs-broker-importer-self-assessment-pre-certification-test
- ~300,000-350,000 active U.S. importer-of-record numbers, https://www.federalregister.gov/documents/2019/08/14/2019-17179/customs-broker-verification-of-an-importers-identity
- Customs bond is not insurance; surety recovers from importer under indemnity agreement (confirmed across multiple surety-industry pages, consistent account, no single canonical primary source fetched, treated as VERIFIED by consistency, not by statute text)

**NOT VERIFIED (secondary source only, or fetch failed):**
- CBP HQ H350722 exact ruling text, the CROSS page (https://rulings.cbp.gov/ruling/H350722) would not render readable text in this session (JS-rendered); the six-digit-threshold quote is confirmed only via two law-firm summaries (https://diaztradelaw.com/even-ai-needs-a-license-know-when-automation-unlawfully-crosses-into-customs-business/, https://gingercontrol.com/blog/hts-classification-six-digit-broker-requirement) that agree with each other verbatim on the quoted sentence
- CBP Reasonable Care Informed Compliance Publication, fetched but returned unreadable binary/PDF stream in this session; existence and title confirmed via search only, https://www.cbp.gov/sites/default/files/assets/documents/2018-Mar/icprescare2017revision.pdf
- ACE Portal Terms and Conditions (72 FR 27632) pooling/confidentiality language, could not be fetched, recorded as UNRUN, not clean
- Trade Compliance Manager salary figures, Glassdoor and Salary.com are aggregator surveys, not an employer's own ATS or a state/university portal, so title-level only per this file's standing toolchain limit, https://www.glassdoor.com/Salaries/trade-compliance-manager-salary-SRCH_KO0,24.htm, https://www.salary.com/research/salary/posting/trade-compliance-manager-salary
- No fee-shift provision found (absence, not a positive finding), searched via Cornell LII and general web search, no primary text located
- Patent search (rung 1.5), Google Patents result WO2016057000A1 and one non-patent research paper reviewed; no granted claim reads directly on this candidate's differentiated claim, https://patents.google.com/patent/WO2016057000A1/en
