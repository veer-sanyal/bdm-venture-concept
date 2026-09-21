# Screen B1, Consumer Report Match-Confidence Grading (Ideation B, Candidate 1)

Blind screen, round 17. Candidate: CRAs (sub-300 employees) doing employment/tenant background
screening; Jev grades whether a courthouse criminal-record hit is the same person as the applicant,
joined later to the CRA's own reinvestigation-team determination when the consumer disputes it.

---

## 1. THE CASE FOR

The strongest demand tier is a fresh, on-point **D1**: *Walker, Ross & Wilson v. Inflection Risk
Solutions, LLC* (San Mateo County Superior Court, Case No. 22-CIV-02954), a **$1,765,000** class
settlement (final approval hearing 2025-07-28) built around a "Name & DOB Match Group": consumers whose
Inflection background reports (2020-07-20 to 2024-05-30) attached a criminal or sex-offender record
that **did not match their first name, last name, and date of birth**, the exact failure mode this
candidate prices. Source: the official settlement site, `walkerfcrasettlement.com`, and
`claimdepot.com/settlements/walker-fcra-settlement`. This sits alongside the ideation file's own D1
(*Williams v. First Advantage*, $250K compensatory / $1M punitive, 11th Cir. 2020) as a second,
independent, more recent instance of the same mechanism.

The strongest rung-2 pass: the duty-holder check is clean and unambiguous. 15 U.S.C. § 1681e(b) names
the CRA, the buyer of this product, as the party who "shall follow reasonable procedures to assure
maximum possible accuracy," and the CFPB's own (now-withdrawn, see weaknesses) 2021 advisory opinion
confirms the specific failure mode is "name-only matching... without verifying the match using
additional identifying information." No instrument problem, no K2.

The best D1/D2 number is the Walker settlement above; it is fresher, more specific to the exact match
failure, and better-sourced than any comparative substitute or vendor number found in this screen.

---

## 2. THE SCORED WEAKNESSES

**Rung 1.5 (patent).** Checkr Inc. holds **US10878524B2**, "Continuous background check monitoring,"
filed 2019-03-27, status **active** (Google Patents), whose claim 1 covers "receiving enrollment
information," running an "identity matcher" that performs "probabilistic matching to calculate a
probability that the record belongs to the candidate," and automatically triggering "a manual review of
the record" when "a compliance review may be determined to be needed depending on the severity of the
record", i.e., a granted claim on confidence-threshold-gated review routing, already offered as
Checkr's own consumer-report service (enrollee is "an employer or potential employer," per the patent
text). **Weakens criterion 4**: the core matching-plus-threshold-routing mechanism is not patent-white-
space; it converts part of the capability gap into a distribution gap (Checkr does not license this
engine to competitor CRAs; it uses it to compete for the same end-employer customers).

**Rung 2, instrument being legislated away.** VERIFIED: the CFPB withdrew both **"Fair Credit
Reporting; Name-Only Matching Procedures," 86 FR 62468 (2021-11-10)**, and **"Fair Credit Reporting;
Background Screening," 89 FR 4171 (2024-01-23)**, effective 2025-05-12, as part of a 67-document
guidance rollback (Federal Register 2025-08286; confirmed independently via
`americascreditunions.org` and `clearstar.net`, which both list these two titles by name). The
withdrawal notice states guidance "should no longer be relied upon or enforced during the period of
further review," and is explicit that this reaches only the agency's own interpretive documents, not
the underlying statute. **Weakens criterion 3 and 7**: the regulatory-enforcement layer that made
"name-only matching is a violation" a bright-line, agency-stated rule is gone; what remains is the bare
statutory text plus private litigation (which is what actually produced both D1 numes, so the money is
real), but a pitch that leans on "the regulator says this is illegal" now overstates the current state
of federal guidance.

**Rung 2, pooling / confidentiality clause.** **NOT VERIFIED, clean not-found.** The actual wholesale
contracts between CRAs and court-record aggregators/data wholesalers (LexisNexis Risk Solutions,
Appriss Insights/Equifax) are not publicly posted; only Appriss Insights' public-site terms of use were
found (governs submissions to their consumer-facing site, not enterprise data licensing) and a
government (TennCare) contract exhibit stating Appriss "contractor data" does not itself constitute a
"consumer report." No clause resembling Ford PPGTC §20.01's foreclosure language was located for this
industry. **This is an open item, not a finding either way**, the asset here does not obviously
require pooling ACROSS CRAs (each CRA's own ledger of its own hits and its own reinvestigation outcomes
is single-tenant), so the Part 3 pooling check may not even bind this formulation; flagged as unresolved
rather than scored.

**Rung 3, RATCHET.** The conservative move, route every ambiguous hit to a human, or simply don't
report it, is already free and lawful (it is what CFPB's guidance told CRAs to do, and what CRAs do
today per the ideation file's own account of current practice). The only thing a customer can lawfully
buy from this product is a **less-conservative** action: trusting an automated high-confidence "yes,
same person" call enough to skip the human queue on hits that would otherwise get sampled or reviewed.
**Weakens criterion 5**: exactly the shape flagged at C-62/C-56, "agreeing with the free guidance is
free; disagreeing with it is unusable" inverted here as "the safe answer costs nothing; the only
saleable answer is the one that increases the CRA's own § 1681n/o exposure if wrong." No dollar evidence
was found that any CRA has priced this trade-off; NOT VERIFIED.

**Rung 4, capability already deployed by the two largest incumbents, in-house.** Sterling's own site
(`sterlingcheck.com`, product-overview material; the dedicated product URL 404'd, content confirmed via
cached search summary of sterlingcheck.com pages) states SmartData delivers "increased automation across
the end-to-end employment criminal background check process, from matching candidate data to
determining reportability and applying order rules," that "approximately 90% of Sterling's US searches
leverage automation in combination with a strategic human touch," and that Sterling "constantly refine[s]
its SmartData algorithms... to continually evolve and improve criminal record turnaround times and
accuracy rates." Sterling has since been absorbed into **First Advantage** (sterlingcheck.com's own
banner: "Sterling Background Check Solutions is now First Advantage", merger date NOT VERIFIED this
session, search budget exhausted before it could be pinned down). First Advantage is also the defendant
in the ideation file's own Williams D1. **No deployment was found in the sub-300-employee segment** , 
Checkr and First Advantage/Sterling both run this in-house to compete directly for end-employer
customers, not as software licensed to smaller competitor CRAs, so **G2 fails and this is NO KILL**,
but it is a heavy **criterion 2 and 4 weakness**: the specific claim "not just a similarity score that
still sends the ambiguous ones to a queue" is not true of the two firms controlling the largest
disclosed revenue share (First Advantage 7.4% + Sterling 6.6% = 14% of 2019 industry revenue per the
IBISWorld figure below, now consolidated under one owner). What is NOT shown to exist anywhere is the
second half of the claimed asset, a ledger joining match-confidence-at-issuance to the LATER
reinvestigation-outcome, so the surviving, narrower differentiated claim is the feedback loop, not the
initial matching step. No forcing evidence for a different formulation (see MUTATION below), but the
claim as ideated is broader than the evidence supports.

**Rung 5b, attribution confound.** The graded label (reinvestigation outcome) is produced by the CRA's
own reinvestigation team under active dispute, whose incentive is to resolve exposure (settle/delete)
rather than adjudicate ground truth, the same "adjuster who settles rather than fights" confound named
in Part 3. NOT VERIFIED as a measured bias, but structurally present and unaddressed in the ideation
file. Weakens criterion 5.

**Rung 5c, label scarcity / base rate.** A label only arrives for hits a consumer actually disputes
under § 1681i. Consumers who never learn a mismatched record cost them a job (the exact injury in both
Williams and Walker) never generate a dispute, so the model only ever trains on the disputed subset , 
the same failure mode as the skilled-nursing "never learns what happened to a declined referral"
example in Part 3. No published dispute-rate statistic was found to size this gap (NOT VERIFIED), but
the mechanism itself is not in dispute. Weakens criterion 5.

**Rung 6, economics floor, but stale.** Countable source: CFPB's *Market Snapshot: Background
Screening Reports* (October 2019), citing IBISWorld Industry Report OD6058 (April 2019): **"there are
1,954 background screening companies [in 2019] with revenue of $3.2 billion; two firms account for
fourteen percent of the industry's revenue"** (First Advantage 7.4%, Sterling 6.6%). That leaves
roughly 1,952 firms holding ~86% of revenue, consistent with a large sub-300-employee long tail, and a
usable count for criterion 6, but the figure is **seven years old**, predates the First
Advantage/Sterling merger, and no current per-customer price point for a comparable tool was found to
compute an annual dollar-at-one-customer figure. NOT VERIFIED as a current number.

**D3.** No specific, page-verified job posting was found describing this exact task with a comp band at
a real CRA's own careers page or ATS (Entrata's Lever posting 404'd on fetch; ZipRecruiter/Indeed/
Glassdoor aggregate figures for "Background Adjudication Specialist" are NOT VERIFIED AT PAGE, consistent
with this repo's known toolchain limit that major job boards 403 on fetch). See D3 STATE below.

---

## 3. KILL

**NO KILL.** K1 does not fire, the recoverable amount at one customer is real and multi-million-dollar
(Walker $1.765M, Williams $1.25M combined), and the CRA customer controls its own matching investment
decision even though settlement dollars flow through courts, not the CRA directly. K2 does not fire , 
§ 1681e(b) squarely binds the CRA, the buyer of this product. K3 CANDIDATE does not fire, Checkr and
First Advantage/Sterling both clear G1 (their own product-page/patent language) but neither clears G2
(a named deployment **in the sub-300-employee CRA segment**, as opposed to in their own end-employer-
facing report business), so the "already solved for your segment" bar is not met.

---

## 4. D3 STATE

**UNRUN** (not EMPTY). A generic aggregator estimate exists ("Background Adjudication Specialist,"
$33.32-$50.48/hr, ZipRecruiter, Charlotte NC) but is NOT VERIFIED AT PAGE per this repo's known job-board
toolchain limit, and the one specific lead worth checking (Entrata's Lever posting for a "Background
Verification Analyst") returned a 404 on fetch and could not be read end to end. No conclusion should be
drawn in either direction; this needs a state/university portal, an employer's own careers page, or a
phone call to resolve.

---

## 5. MUTATION

Does the evidence force a different formulation, or does it not? **It narrows the claim; it does not
force a different formulation.** The forcing evidence (Checkr's active patent, Sterling/First
Advantage's SmartData marketing) shows that automated probabilistic identity-matching with
threshold-gated human review is not novel and is already run in-house by the two largest incumbents by
disclosed revenue. But nothing found shows that anyone, incumbent or vendor, joins match-confidence-
at-issuance to the LATER reinvestigation-team determination into a ledger that improves the threshold
over time; that feedback loop, not the initial matching step, is the only part of the claimed asset this
screen could not find already built. That is a rung-4 scoring correction (the claim must be stated as
the feedback loop, not "automated matching" generally, a narrower and more defensible claim), not a
structural barrier of the kind M1 requires (no reserved determination, no liability floor, no compelled
publication, no free self-invocable appeal blocking it). **NONE**, no principled mutation is forced by
this evidence; the candidate's own differentiated-claim sentence needs tightening, which is a drafting
fix, not a reformulation.

---

## 6. RUBRIC SCORES

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Clarity of target customer | 3 | Segment is named and a countable (if stale) source exists, 1,954 firms, 2019, but no specific title/person was confirmed via a real posting or call |
| 2 | Clarity of JTBD | 4 | One clean practitioner sentence ("is this court record the same individual as the applicant"), directly traceable to the CFPB's own "name-only matching" vocabulary |
| 3 | Significance and magnitude of unmet need | 3 | One VERIFIED D1 tier reached (Walker $1.765M, 2025) but D3 is UNRUN and no salience call was made, Part 3 caps this at 4 with no call, and the unresolved D3 pulls it to 3 |
| 4 | Differentiation and uniqueness | 2 | Both Checkr (active patent) and First Advantage/Sterling (on-page SmartData claim) already run threshold-gated automated matching in-house; the surviving differentiated claim narrows to the reinvestigation-feedback loop only |
| 5 | Performance improvement over existing solutions | 2 | RATCHET (the safe answer is free, the saleable one raises the CRA's own liability), a 5b confound (reinvestigation outcomes may reflect settlement-averse deletion, not ground truth), and a 5c label-scarcity problem (only disputed hits ever generate a label) all sit unresolved against the compounding-moat claim |
| 6 | Size of market opportunity | 3 | Countable source exists (1,954 firms / $3.2B, 2019) but is seven years stale and predates the First Advantage-Sterling merger; no current per-customer price point to size the dollar opportunity |
| 7 | Market / technical / execution risk | 3 | A Jev-shaped yes/no question is buildable as a demo; real open risk sits in whether cross-CRA pooling is even needed (probably not, per the pooling note above) and in the 5c cold-start problem for any customer with few historical disputes |

**Lowest criterion: 2** (criteria 4 and 5, tied). **Sum: 20.**

---

## 7. VERIFIED / NOT VERIFIED

**VERIFIED**
- 15 U.S.C. § 1681e(b), https://www.law.cornell.edu/uscode/text/15/1681e (established by ideation file, quote checked, not re-fetched)
- *Williams v. First Advantage Background Services Corp.*, 11th Cir. 2020, established by ideation file (quote checked, not re-fetched)
- *Walker, Ross & Wilson v. Inflection Risk Solutions, LLC*, Case No. 22-CIV-02954 (San Mateo County Superior Court), https://www.walkerfcrasettlement.com/ and https://www.claimdepot.com/settlements/walker-fcra-settlement, $1,765,000 total settlement, "Name & DOB Match Group," final approval hearing 2025-07-28
- CFPB, "Fair Credit Reporting; Name-Only Matching Procedures," 86 FR 62468 (2021-11-10), withdrawal confirmed via https://www.americascreditunions.org/blogs/compliance/withdrawn-sixty-seven-pieces-guidance-withdrawn-cfpb and https://www.clearstar.net/cfpb-withdraws-several-guidance-documents-for-fcra-and-consumer-reporting-agencies/, effective 2025-05-12 per Federal Register 2025-08286
- CFPB, "Fair Credit Reporting; Background Screening," 89 FR 4171 (2024-01-23), same withdrawal, same sources
- US10878524B2, "Continuous background check monitoring," Checkr Inc., https://patents.google.com/patent/US10878524B2/en, filed 2019-03-27, status active, claim language on probabilistic matching and threshold-gated compliance review quoted above
- PBSA, "Criminal Record Information for Background Checks: The Need for an Identifier Matching Process", https://www.cdiaonline.org/wp-content/uploads/2022/06/PBSA-Criminal-Record-Information-Identifier-Matching.pdf, free published guidance on court-side identifier matching, read in full
- CFPB, *Market Snapshot: Background Screening Reports* (October 2019), https://files.consumerfinance.gov/f/documents/201909_cfpb_market-snapshot-background-screening_report.pdf, "1,954 background screening companies" and "two firms account for fourteen percent of the industry's revenue" (citing IBISWorld OD6058, April 2019)
- PBSA membership dues tiers by employee count, https://www.thepbsa.org/membership/membership-categories-pricing/
- Sterling "SmartData" automation and accuracy-improvement claims, sourced from sterlingcheck.com content (dedicated product URL 404'd on direct fetch; content confirmed via search-engine cache of sterlingcheck.com pages, so treat the exact wording as SCORE-level, not gate-level, evidence pending a direct-page re-fetch)

**NOT VERIFIED**
- Any specific pooling/confidentiality clause in a CRA's wholesale contract with LexisNexis Risk Solutions or Appriss Insights (contracts are not public; only public-site terms of use and one unrelated government contract exhibit were found)
- D3: any page-verified job posting at a real CRA's own careers site or ATS describing this exact task with a comp band (Entrata Lever posting 404'd; job-board aggregator figures are estimates, not page-verified, per this repo's known toolchain limit)
- Exact date First Advantage completed its acquisition/merger with Sterling (web search budget exhausted before this could be pinned down)
- Any published dispute rate (what fraction of mismatched consumers ever file a § 1681i dispute) to size the rung-5c label-scarcity gap
- Any current (post-2019) count of background screening companies or industry revenue
- Any published price for a comparable match-confidence or identity-resolution tool, needed to compute an annual dollar-at-one-customer figure for rung 6
