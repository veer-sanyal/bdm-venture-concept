# Ideation B, Lane: 100% review of sampled work, and rubric grading disputed for money

Generated 2026-09-20, for the Jev launch (TypeSafe AI, 2026-09-18). Four candidates. Dead list and
already-live-in-project items checked against each name and mechanism below; none repeat.

---

## 1. Consumer Report Match-Confidence Grading

**Tuple.** Customer segment and band: consumer reporting agencies (CRAs) doing employment and tenant
background screening, sub-300 employees (the PBSA, the industry's own accrediting body, describes its
member CRAs as running "millions" of checks a year in aggregate, a base far larger than the handful of
household names). Asset: a ledger pairing every criminal-record "hit" the CRA's name-matching step
produced against the same-person confidence it was given, joined later to what the CRA's own reinvestigation
team actually concluded when the consumer disputed it. Document/state input: the court-record hit (name,
DOB fragment, offense, jurisdiction, disposition date) plus the applicant's identifying fields from the
order, text/JSON, no images. The mistake: attaching a criminal record to the wrong person, which is
exactly the failure 15 U.S.C. § 1681e(b) exists to prevent ("[a] consumer reporting agency... shall follow
reasonable procedures to assure maximum possible accuracy of the information concerning the individual
about whom the report relates"). Checker and rule: the consumer, through the FCRA reinvestigation right at
§ 1681i, and ultimately a federal court applying § 1681n (willful) or § 1681o (negligent) liability.

**Differentiated claim.** An incumbent would already have to be claiming: "our matching engine independently
re-verifies every borderline hit against full identifying detail before a human ever sees it, not just a
similarity score that still sends the ambiguous ones to a queue a person has to work through." Today's
courthouse-record aggregators (LexisNexis, Appriss and similar) produce a match score; CRAs still route the
"possible match" bucket to human adjudicators because reviewing every hit with an LLM call was too slow and
too expensive to do on all of them, so review is sampled by risk tier, not exhaustive.

**Question shape.** Noul, "is this court record the same individual as the applicant" (returns probability
of yes). Sub-second, near-zero-cost matters here because match adjudication sits inside the CRA's report
turnaround SLA, and CRAs generate far more hits than they can afford to have a person (or a per-call LLM)
touch one at a time; the point of Jev is that every hit, not just the flagged ones, gets scored before a
person is in the loop at all.

**Where the outcome is observed.** By the CRA's own reinvestigation team, in its case-management system,
when a consumer disputes a report under § 1681i, and by the client employer if an adverse-action complaint
comes back. The company gets it by having the CRA log the reinvestigation's final determination against the
probability Jev gave that hit when the report was built.

**D1.** VERIFIED. Statute: 15 U.S.C. § 1681n(a), willful noncompliance carries "damages of not less than
$100 and not more than $1,000" in statutory damages per violation, on top of actual and punitive damages and
attorney's fees. Concrete instance: *Williams v. First Advantage Background Services Corp.*, 11th Cir. 2020
,  a jury awarded a wrongly-matched applicant $250,000 in compensatory damages and $3.3 million in punitive
damages after First Advantage twice attached a stranger's ("Ricky" Williams's) criminal record to him,
costing him two job offers; the Eleventh Circuit affirmed the $250,000 compensatory award and reduced
punitive damages to $1 million on remand as the constitutional maximum, not eliminating it.
Purchase frequency: NOT VERIFIED as an exact number, PBSA states member CRAs run "millions" of checks a
year in aggregate but does not publish a per-company annual count, though the mechanism (every job
requisition triggers a new screen) makes many-times-per-year purchase self-evident for any operating CRA.

**Computed or observed / paperwork or physical act.** OBSERVED: whether a given hit is the same person is
not deducible from the applicant's own two documents, it requires the pattern of what the CRA's own
reinvestigations have actually confirmed or overturned over time, which only accumulates by operating.
Paperwork: the liability is the furnished report itself; nothing physical has to happen for the mistake to
cost money.

**Competition fit.** The moat is the joined ledger of match-confidence-at-issuance versus
reinvestigation-outcome-later, across millions of hits and thousands of idiosyncratic county court naming
conventions, a nuisance to assemble that no one can buy by licensing a name-matching API, and it is sold as
software the CRA runs, not a review service performed by the founders.

---

## 2. Customs Entry Classification Second-Look

**Tuple.** Customer segment and band: licensed customs brokerage firms, sub-300 employees (the great
majority of the ~11,000 CBP-licensed brokers are small shops, not the handful of global forwarders), and
small/mid importers of record who self-file. Asset: a ledger pairing each line item's classification
confidence at filing against what CBP actually did with it later (cleared silently, issued a Request for
Information, issued a CF-29 Notice of Action, opened a Focused Assessment, assessed a penalty). Document/
state input: the commercial invoice description, the broker's proposed HTS code, and relevant CBP CROSS
ruling text, text/JSON. The mistake: misclassifying an entry's Harmonized Tariff Schedule code, exposing
the importer to a duty/penalty assessment under 19 U.S.C. § 1592 and exposing the broker itself to liability
for failing "responsible supervision and control" under 19 U.S.C. § 1641. Checker and rule: CBP, through
post-entry audit (Focused Assessment / Regulatory Audit) applying § 1592's negligence/gross-negligence/fraud
standards, and § 1484's "reasonable care" duty on the filer at time of entry.

**Differentiated claim.** An incumbent would already have to be claiming: "our trade-compliance software
checks every line of every entry, not the highest-dollar or newest-SKU lines a compliance officer has time
to sample, against the current tariff schedule and this broker's own audit history, and tells you which
classifications CBP is statistically likely to challenge." Existing tools (Amber Road/E2open, Descartes)
do rules-based HTS lookup and flag ambiguous cases for a human; none price a calibrated, thresholdable
probability of enforcement risk tuned to a specific broker's own history, because reviewing every line that
way was previously an LLM-cost decision, not a lookup.

**Question shape.** Choice, "which of these candidate HTS headings is correct" with a per-option
probability, since classification disputes are usually between 2-4 plausible headings, not a binary. Latency
matters because a broker files entries continuously across many clients and many line items per entry;
near-zero cost is what makes reviewing every line economical instead of only the highest-value SKUs, which
is the current sampling practice this candidate targets.

**Where the outcome is observed.** CBP's own post-entry correspondence (CF-29, Request for Information,
protest denial, Focused Assessment finding, penalty notice) arrives in writing at the broker's or importer's
own file, this passes the "does the evidence of the mistake physically arrive at the customer's building"
test directly. The company gets it by having the client log that correspondence back against the
pre-filing risk score for the same entry.

**D1.** VERIFIED. Case: *United States v. UPS Customhouse Brokerage, Inc.*, Ct. Int'l Trade, the court held
UPS liable for a **$75,000** judgment tied to **45** misclassified entries of computer parts under HTSUS
subheading 8473.30.9000, for violating the broker's § 1641 duty of responsible supervision and control , 
roughly $1,667 per misclassified entry, to one brokerage, from one pattern of repeated misclassification.
Statute: 19 U.S.C. § 1592(c), negligence penalties run up to "two times the lawful duties, taxes, and fees
of which the United States is or may be deprived" (or the domestic value of the merchandise if greater);
gross negligence up to four times; fraud "in an amount not to exceed the domestic value of the merchandise."
Purchase frequency: VERIFIED as a magnitude, not an exact per-broker count, CBP's own public data shows
tens of millions of entries filed nationally per year (its public data portal returned roughly 39.1 million
entries for the Feb 2024-Feb 2025 period), so any operating broker files far more than one classified line
a year.

**Computed or observed / paperwork or physical act.** Mixed, stated honestly: the raw classification lookup
against the published tariff schedule and CROSS rulings leans COMPUTED, a broker with the product
description and the tariff text can often deduce the technically correct heading without any outcome data.
What is OBSERVED, and is the actual asset, is which technically-defensible classifications CBP has
historically chosen to challenge, that calibration cannot be deduced from the tariff schedule alone and
only accumulates by watching real enforcement outcomes. Paperwork: the entry document and its HTS code
carry the exposure; the goods cross the border and the freight movement happens regardless of the code, so
the money sits almost entirely in the paperwork.

**Competition fit.** The calibration ledger, which classifications draw a CBP challenge, by HTS chapter and
product pattern, per broker's own enforcement history, is proprietary and grows only by operating a
compliance-review business across real client audit histories; it is sold as software the broker runs on
every entry, not diligence performed by the founders.

---

## 3. Claims File Compliance Severity Grading

**Tuple.** Customer segment and band: third-party claims administrators (TPAs) handling workers' comp, auto,
or general-liability claims for self-insured employers and small regional insurers, sub-300 employees.
Asset: a ledger scoring each closed claim file's compliance posture against state Unfair Claims Settlement
Practices Act (UCSPA) requirements, correlated against what a state market-conduct exam or DOI complaint
actually cited later. Document/state input: the claim file's timeline and correspondence log, acknowledgment
date, investigation date, payment or denial date, stated reason for denial, text/JSON. The mistake: a claim
handled outside the state's UCSPA standard (late acknowledgment, an inadequately documented denial reason)
that a QA sample happened to pass because full review of every closed file is too expensive to do routinely.
Checker and rule: the state Department of Insurance market-conduct examiner, applying the state's UCSPA (for
example California Insurance Code § 790.035), and the self-insured client auditing the TPA's own contractual
service-level compliance.

**Differentiated claim.** An incumbent would already have to be claiming: "our claims system verifies, on
every single closed claim, that each UCSPA timeliness and documentation requirement was actually met, not
just logs the timestamps and leaves the judgment call ('was this denial reason properly documented and
reasonable') to whatever percentage of files a QA reviewer has hours to read." Claims platforms (Guidewire,
Origami and similar) log the timestamps; the compliance judgment itself is still a human sampling exercise.

**Question shape.** Score, rate each closed file's UCSPA-compliance defensibility on a rubric from clearly
compliant to clearly citable. Near-zero cost matters because TPA QA teams today commonly audit only a
percentage of closed files for compliance, not all of them, purely on reviewer-hour cost; scoring every file
lets the state's own market-conduct sample never be the first time a violation is found.

**Where the outcome is observed.** The TPA's own file, when the state DOI's market-conduct exam findings or
a consumer complaint disposition arrive in writing. The company gets it by having the TPA log the exam
finding or complaint outcome back against the pre-scored file.

**D1.** VERIFIED, as a statutory ceiling rather than a paid fine (the instrument itself is the published
number). California Insurance Code § 790.035: a civil penalty "not to exceed five thousand dollars ($5,000)
for each act" for a non-willful unfair claims practice, or "not to exceed ten thousand dollars ($10,000) for
each act" if willful, per violation, not per exam, so a file with several distinct violative acts multiplies.
Purchase frequency: NOT VERIFIED as a published industry count of claims-per-TPA-per-year, but the underlying
obligation, UCSPA compliance is required on every claim handled, not just audited claims, makes many
purchases per year for any operating TPA a near-certainty rather than a project purchase.

**Computed or observed / paperwork or physical act.** OBSERVED: whether a stated denial reason will be
judged "reasonable" by an examiner is not deducible from the claim file's own documents alone, it requires
matching against the pattern of what examiners have actually cited as a violation across many prior files,
which only accumulates by operating. Paperwork: the exposure is entirely about documentation and timing, not
a physical act, the claim payment itself is a separate question from whether the file was handled
compliantly.

**Competition fit.** The correlation ledger between claim-file patterns and actual market-conduct citations,
built across many TPA clients and each state's own idiosyncratic UCSPA enforcement history, is the asset , 
not obtainable by encoding a state statute's text into a rules engine, and sold as software the TPA runs on
every file.

---

## 4. Grant Cost-Allowability Documentation Grading

**Tuple.** Customer segment and band: small regional CPA firms performing Single Audits under 2 CFR Part 200
Subpart F for nonprofit and higher-ed federal grant recipients, and the grant recipients' own small
finance/compliance offices (community health centers, small nonprofits), sub-300 employees. Asset: a ledger
scoring each grant transaction's cost-allowability documentation against the specific cost principles in
2 CFR 200 Subpart E and the award's own terms, correlated against which transactions later actually became
audit findings or "questioned costs." Document/state input: the transaction description, GL coding, the
applicable cost principle, and a summary of supporting documentation on file, text/JSON. The mistake:
charging an unallowable or inadequately documented cost to a federal award, discovered only because
auditors sample-test transactions under Yellow Book/AU-C audit-sampling standards rather than reviewing
every one, so unreviewed unallowable transactions pass into the final claim. Checker and rule: the
independent auditor performing the Single Audit under 2 CFR Part 200 Subpart F, and the federal awarding or
cognizant agency, which must act once "known or likely questioned costs are greater than $25,000 for a type
of compliance requirement for a major program" under 2 CFR § 200.516.

**Differentiated claim.** An incumbent would already have to be claiming: "our grants-accounting system
checks every transaction, not a statistically drawn sample, against the specific cost principles in this
award's own terms, and tells you which ones an auditor is statistically likely to question." Grants/fund
accounting software (MIP, Blackbaud and similar) enforces budget-line coding; it does not grade
documentation sufficiency or allowability judgment calls transaction by transaction.

**Question shape.** Score, rate each transaction's allowability-documentation defensibility on a rubric
given the specific cost principle and the documentation summary on file. Near-zero cost matters because a
mid-size nonprofit posts thousands of transactions per federal award per year while auditors sample a small
fixed count (commonly dozens, not thousands) per major program under standard audit-sampling guidance;
scoring every transaction catches unallowable costs sitting in the 95%-plus that a statistical sample would
never touch.

**Where the outcome is observed.** The recipient's own Single Audit report (its Schedule of Findings and
Questioned Costs) and the federal agency's management-decision letter requiring a refund, both arrive in
writing at the recipient. The company gets it by having the client log the final Schedule of Findings and
the questioned-cost resolution back against the pre-scored transactions for that award year.

**D1.** VERIFIED. Case: HHS Office of Inspector General audit of North Shore Community Health, Inc., OIG
recommended HRSA "require North Shore to refund $2 million to the Federal Government, or work with North
Shore to determine whether any of the costs that it claimed against [American Recovery and Reinvestment
Act] grants were allowable," after finding North Shore "did not track and account for Recovery Act
expenditures separately from other... operating expenses" and so "could not demonstrate that it spent
Recovery Act grant funds for allowable costs", one nonprofit grant recipient, one review, $2 million.
Regulatory threshold: 2 CFR § 200.516 requires reporting once "known or likely questioned costs" exceed
$25,000 for a compliance requirement on a major program. Purchase frequency: VERIFIED at "at least yearly" , 
2 CFR § 200.501 requires a Single Audit for any non-federal entity expending $1,000,000 or more in federal
awards in its fiscal year (raised from $750,000 for fiscal years beginning on or after 2024-10-01), which is
an annual, not project, obligation for any recipient above threshold.

**Computed or observed / paperwork or physical act.** OBSERVED: whether a given transaction's documentation
is "sufficient" is not deducible from the transaction's own two documents (the invoice and the cost
principle text) alone, it requires the pattern of what auditors and agencies have actually flagged as
insufficient across many prior awards, which only accumulates by operating. Paperwork: the cost-principle
compliance question is entirely documentary, the underlying goods or services were already delivered, so
essentially all of the exposure sits in the paperwork, not a physical act.

**Competition fit.** The ledger correlating documentation patterns with actual audit findings and
questioned-cost resolutions, accumulated across many recipients' real Single Audit histories, is the asset , 
not obtainable by encoding 2 CFR 200's cost principles into a rules engine, and sold as software the
CPA firm or recipient runs on every transaction, not audit work performed by the founders.

---

## Sources, VERIFIED / NOT VERIFIED

**VERIFIED**
- 15 U.S.C. § 1681e(b), https://www.law.cornell.edu/uscode/text/15/1681e, "Whenever a consumer reporting agency prepares a consumer report it shall follow reasonable procedures to assure maximum possible accuracy of the information concerning the individual about whom the report relates."
- 15 U.S.C. § 1681n, https://www.law.cornell.edu/uscode/text/15/1681n, "actual damages sustained by the consumer as a result of the failure or damages of not less than $100 and not more than $1,000."
- *Williams v. First Advantage Background Services Corp.*, 11th Cir. 2020, https://caselaw.findlaw.com/court/us-11th-circuit/2041174.html and https://www.troutman.com/insights/eleventh-circuit-affirms-dollar250k-compensatory-damages-award-and-allows-a-dollar1-million-punitive-damages-award-in-individual-mixed-file-fcra-action/, jury awarded $250,000 compensatory and $3.3 million punitive (reduced to $1 million on appeal as the constitutional maximum) after First Advantage twice mismatched a stranger's criminal record to the plaintiff.
- 19 U.S.C. § 1592, https://www.law.cornell.edu/uscode/text/19/1592, fraud penalty "not to exceed the domestic value of the merchandise"; gross negligence up to "four times the lawful duties, taxes, and fees... or, if the violation did not affect the assessment of duties, 40 percent of the dutiable value"; negligence up to two times lawful duties or 20 percent of dutiable value.
- 19 U.S.C. § 1641 (via case) and *United States v. UPS Customhouse Brokerage, Inc.*, https://caselaw.findlaw.com/court/us-federal-circuit/1444493.html and https://www.courtlistener.com/opinion/208224/united-states-v-ups-customhouse-brokerage-inc/, $75,000 judgment tied to 45 misclassified entries for failure of responsible supervision and control.
- CBP entry volume, https://www.cbp.gov/newsroom/stats/cbp-public-data-portal, approximately 39.1 million entries filed nationally, Feb 2024-Feb 2025.
- California Insurance Code § 790.035, https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=INS&sectionNum=790.035, civil penalty "not to exceed five thousand dollars ($5,000) for each act," or "not to exceed ten thousand dollars ($10,000) for each act" if willful.
- HHS OIG audit of North Shore Community Health, Inc., https://oig.hhs.gov/reports/all/2012/north-shore-community-health-inc-claimed-unallowable-costs-against-recovery-act-grants/, OIG recommended HRSA "require North Shore to refund $2 million to the Federal Government."
- 2 CFR § 200.516, https://www.ecfr.gov/current/title-2/subtitle-A/chapter-II/part-200/subpart-F/subject-group-ECFRea73e47c9a286e6/section-200.516, reporting required once known or likely questioned costs exceed $25,000 for a compliance requirement on a major program.
- 2 CFR § 200.501, https://www.law.cornell.edu/cfr/text/2/200.501, Single Audit required at $1,000,000 in federal awards expended per fiscal year (raised from $750,000 for fiscal years beginning on or after 2024-10-01).

**NOT VERIFIED**
- Exact per-CRA annual background-check volume (PBSA states "millions" industry-wide, no per-company published figure).
- Exact per-TPA annual claims volume (no published industry count found; frequency argued from the regulatory mechanism instead).
- US-dollar average fleet-lease "excess wear and tear" bill-back per vehicle (only UK FN50 figures in GBP were found; this line of inquiry was dropped from the candidate set for lack of a US-dollar published or contractual number, per the no-fabrication rule).
