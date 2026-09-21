# Screen B4, Grant Cost-Allowability Documentation Grading

Candidate: ideation-B.md, item 4 (lines 178-237). Screened blind, round 17, against the Jev question-shape
(rubric score, 2-10 levels) and the split ladder (METHOD.md Part 3).

---

## 1. THE CASE FOR

**Strongest demand tier + best D1 number, VERIFIED.** HHS OIG's audit of North Shore Community Health, Inc.
recommended HRSA "require North Shore to refund $2 million to the Federal Government, or work with North
Shore to determine whether any of the costs that it claimed against [Recovery Act] grants were allowable,"
after finding North Shore "could not demonstrate that it spent Recovery Act grant funds for allowable
costs", one nonprofit grant recipient, one review, $2,000,000. This is D1: a real regulator's own written
account of the mistake's dollar cost at one customer. (Established by the ideation agent; not re-fetched,
per dispatch instructions, the quote reads correctly against the regulatory text I did verify below.)

**The regulatory floor and frequency are independently VERIFIED, not just cited.** I read 2 CFR 200.516 at
Cornell LII directly: the auditor "must report the following as an audit finding in the schedule of
findings and questioned costs" once "known or likely questioned costs are greater than $25,000 for a type
of compliance requirement for a major program", so the $2M North Shore case is 80x the reporting floor,
not a marginal one. And 2 CFR 200.501, also read directly: "A non-Federal entity that expends $1,000,000 or
more during the non-Federal entity's fiscal year in Federal awards must have a single or program-specific
audit conducted for that year", an annual, recurring obligation for anyone above threshold, confirming
Part 2b's 2c frequency test (a purchase-equivalent recurs at least once a year for every customer in band).

**Rung 2 duty-holder check passes cleanly, read from the instrument itself, not inferred.** The Cornell LII
text names the auditee, the recipient, as the party for whom "corrective action" is required, and the
$1M threshold text names the "non-Federal entity" (the recipient) as the party the whole Subpart F
apparatus is triggered by. Both named customers in the tuple (the recipient's finance office and the CPA
firm performing the audit) sit directly on the instrument; neither is the wrong party.

**Rung 4 (incumbent-vocabulary sweep) came back clean, a real finding, not an absence of searching.** I
searched grant/fund-accounting incumbents (MIP Fund Accounting, Blackbaud Financial Edge NXT), research-
administration systems (Kuali Research, Cayuse, Huron), continuous-transaction-monitoring AI vendors
(MindBridge Ai Auditor, Oversight Systems), and grantee due-diligence tools (Candid/GuideStar Charity Check,
Temelio), the vendors a practitioner would actually name using "grant management," "post-award," "cost
principles," "subrecipient monitoring" vocabulary. None of them, on their own product pages, claims to
grade a transaction's cost-allowability *documentation defensibility* against the *specific cost principle
and the award's own terms*, transaction by transaction. MIP/Blackbaud enforce budget-line coding (CAPTURES
the wrong-fund-coding half of the mistake, leaves the harder documentation-judgment half untouched, this
independently confirms the ideation file's own "Competition fit" claim rather than just restating it).
MindBridge and Oversight do continuous AP/GL anomaly detection for commercial fraud and expense risk, with
no federal-grant or 2 CFR 200 language anywhere I could find on their sites. Candid/Temelio check whether a
subrecipient's Single Audit exists and is clean, a funder-side, post-hoc, existence check, not a
recipient-side, pre-emptive, transaction-level grading tool. **No vendor's own page carries the claim; no
named deployment doing this job was found. NO K3 CANDIDATE.**

**A genuine, unprompted tailwind, found searching for the opposite (whether the instrument is being
legislated away).** OMB's May 29, 2026 proposed rewrite of 2 CFR Part 200 (comment period closed July 13,
2026, effective date proposed October 1, 2026) leaves the cost principles and the $1M/25,000 thresholds
"largely untouched" and instead **"reflects changes and policy priorities outlined in the August 7, 2025,
Executive Order 14322, Improving Oversight of Federal Grantmaking,"** which "expand[s] agency authority to
terminate grants" and "increase[s] accountability requirements across the full award lifecycle." The
instrument is not being weakened; the enforcement environment is tightening. This is the opposite of the
Colorado AI Act / amnesty pattern this method warns about, and it was checked, not assumed.

**Rung 2 pooling check, read from the actual portal, is clean, and this is unusually good news.** The
Federal Audit Clearinghouse (FAC) is a *free, public, no-registration* API. I fetched its own terms page:
"no explicit restrictions on redistributing, pooling, compiling, or commercially using FAC API data are
stated." Findings, questioned-cost amounts, and the finding's own criteria/condition/cause/effect narrative
text are all public fields (`findings`, `findings_text` endpoints). There is no Ford-PPGTC-style foreclosure
here, the outcome half of the ledger (which findings actually became questioned costs, and why) is
lawfully poolable **before a single paying customer signs up**, which is a real answer to Part 8's cold-
start criterion that most private-by-operating candidates in this file do not get for free.

---

## 2. THE SCORED WEAKNESSES

- **Two-headed customer, un-forced by any single instrument reading (weakens criteria 1, 2).** The tuple
  names two different buyers, the recipient's own finance/compliance office and the small CPA firm
  performing the Single Audit, with two different JTBDs (avoid a clawback vs. test efficiently) and two
  different economics (the recipient bears the $2M risk; the auditor bears professional-standards risk).
  Nothing I read forces a choice between them, but the pitch and the GTM plan are different products
  depending on which one is primary, and the candidate does not yet say which.

- **The "near-zero cost" framing rests on an unverified number (weakens criterion 3, held to 4 not 5 even
  before the no-call cap).** The ideation file's central magnitude claim, "auditors sample a small fixed
  count (commonly dozens, not thousands) per major program", is stated without a citable source, and I
  could not independently verify a specific sample-size figure from AICPA/GAGAS guidance before this
  session's web-search budget was exhausted. It is directionally correct that statistical audit sampling
  tests less than 100% of a population, but the specific "dozens vs. thousands" contrast that makes the
  near-zero-marginal-cost argument compelling is **NOT VERIFIED**, not confirmed.

- **The learning loop is thin, which is a real weakness on criterion 5, not just a theoretical one (rung
  5c).** Because the checker (auditor) only tests a statistical sample, the overwhelming majority of
  transactions the product would score every year *never receive a ground-truth label at all*, no auditor
  ever looks at them, so the model never learns whether its "documentation insufficient" call on the
  untested 95%+ was right. The label arrives, at best, once a year, for a small fraction of what was
  scored. This is the same asymmetry that C-66 (2b) flags for skilled-nursing declines: the model trains
  disproportionately on the branch that got checked, not the one it graded. **No measured performance
  number exists yet; the compounding claim is asserted, not shown.**

- **GIVES shape fires, residue is real but not zero.** CPA firms compete for this exact recurring-audit
  relationship and market with free content: Wegner CPAs runs a free, recorded webinar, "Strengthening
  Your Single Audit Readiness," addressing single-audit compliance including cost allowability (VERIFIED
  free, VERIFIED title, via the firm's own webinar page). CASRAI (a nonprofit standards body) publishes a
  free plain-language guide to 2 CFR 200 Subpart E's cost principles. Both give away the *concept*, not a
  transaction-level, per-award, per-cost-principle score, so the residue (an actual per-transaction call)
  survives, but "nobody explains cost allowability for free" would have been false, and the pitch should
  not claim it.

- **PUBLISHES shape fires at the auditor level, not the recipient level.** The OMB Compliance Supplement is
  a free, official, annually updated federal publication that tells *auditors* exactly which procedures to
  run to test allowable-costs compliance. It reduces the auditor's own cost of knowing what to test; it
  does nothing for a recipient trying to self-check before the audit arrives. Residue: real, on the
  recipient side; thin, on the auditor-efficiency side (a rung-4 vendor question, not answered here, is
  whether an auditor would rather run its Compliance-Supplement-directed sample by hand or pay for scored
  transactions, the case for is written from the recipient's side).

- **Rung 6 (economics floor) is only partly countable, a real gap, not a NOT-VERIFIED I chose not to
  chase.** VERIFIED: ~40,000 Single Audits/year across *all* non-Federal entity types (GAO, FY2023, "about
  40,000 single audits were submitted to the FAC" against "$1.1 trillion of awards"). VERIFIED: 1,512
  Community Health Centers nationally (NACHC), one countable slice of the "small nonprofit" half of the
  segment. **NOT VERIFIED:** how many of the 40,000 are specifically nonprofits/higher-ed under $300
  employees (as opposed to state/local governments, which the 40,000 figure includes), and how many "small
  regional CPA firms" perform Single Audits (AICPA's Governmental Audit Quality Center has "more than 450"
  *member firms*, which is an undercount of all firms doing this work since GAQC membership is voluntary).
  The addressable band is real but its size is not pinned down.

- **D3 is title-level only, a known toolchain limit, not a world-finding.** Every major job board
  (ZipRecruiter, Indeed, Glassdoor) either 403s on fetch or only returns search-engine-summarized
  aggregates; I could not reach a live employer ATS or university/nonprofit portal posting end to end in
  the time available. Per the method's own recorded toolchain limit (C-60), this is recorded as a tooling
  constraint, not a finding about the world.

- **Rung 4's clean result is not yet explained, and the method requires that it be (C-53).** An empty
  competitive category needs a reason named: (i) the asset can't legally be assembled, (ii) a free actor
  covers the profitable half, or (iii) nobody has a budget line at this granularity. Rung 2's pooling check
  rules out (i), the FAC data is free and poolable. (ii) is partially true (GIVES/PUBLISHES cover general
  education, not per-transaction grading). (iii) is ambiguous given D3's FILLED-but-general-titled result.
  I could not, in the time available, run the fuller sweep (buyer's-guide check, exited-predecessor search
  beyond what's above, a dedicated abandoned-patent-application search) that would let this be named with
  confidence rather than left as a reasonable but unconfirmed inference. **Recording as UNEXPLAINED**, per
  the method's own instruction for this exact situation, rather than claiming an opening.

- **Rung 1.5 (patent search) returned no on-point hit, but the search itself was constrained.** Multiple
  Google-Patents-directed queries (via search engine, since Google Patents' own search UI did not render
  through the fetch tool) returned no patent whose claim reads on "grade every grant transaction's cost-
  allowability documentation against the specific cost principle and correlate against actual audit
  findings." This is a genuine not-found, but I could not run a proper claim-language search directly
  against Google Patents' own search index, so treat this as a weaker not-found than a rung 1.5 search
  normally produces.

---

## 3. KILL

**NO KILL.**

- **K0 (eligibility):** not assessed here (Stage 0 room gate is the main session's job); nothing in this
  screen suggests a Purdue-IP or funding/revenue-cap issue.
- **K1 (money can't move):** does not fire. $2,000,000 (D1) is 80x the $25,000 statutory reporting floor;
  I found no incumbent "fee floor" concept that this magnitude sits below. The "who controls release of the
  money" framing fits this candidate awkwardly, the loss is a clawback triggered by the recipient's own
  documentation failure, not a third party withholding a payment the recipient is owed, so K1's test does
  not cleanly apply either way; recorded as not fired rather than force-fit.
- **K2 (wrong duty-holder):** does not fire. 2 CFR 200.516 and 200.501, read directly at Cornell LII, name
  the non-Federal entity (the recipient) as the party the Subpart F process runs against, and the auditor
  (the CPA firm) as the party with the reporting duty. Both named customers sit on the instrument.
- **K3 CANDIDATE:** does not fire. The rung-4 sweep (above) found no vendor with the exact claim on its own
  product page (G1), let alone a named deployment (G2) and a stated outcome (the third leg).

---

## 4. D3 STATE

**FILLED AT THE CUSTOMER, NOT VERIFIED AT PAGE (toolchain limit).**

- Recipient-side seat: "Grants Compliance Officer," aggregate band **$55,000–$96,000** (ZipRecruiter,
  average $68,117); a broader "Grant Compliance" band reads **$61,500–$115,000**. Duties described as
  monitoring fund use, preparing compliance reports, and conducting internal audits against grant
  regulations, a real seat, doing a rougher, manual version of this task, at companies this size.
- Auditor-side seat: "Senior Auditor/Assurance, nonprofit and governmental," **$88,000–$118,000**, with
  postings explicitly naming "Single Audits" and "Uniform Guidance" experience as required.
- Per the method's own recorded finding (C-60), every major job board 403s on direct fetch or returns only
  a search-engine aggregate; I could not reach a live employer ATS, state portal, or university posting to
  verify a band at the page level. This is the same tooling limit two prior rounds hit, not a new finding
  about the world. State: **FILLED**, band **title-level only**.

---

## 5. MUTATION

**Does the evidence force a different formulation? No new instrument or asset was found that forces a
mutation, but the two-headed customer is worth naming as a needed narrowing, not a forced pivot.**

The candidate, as written, sells the same asset to two parties who sit on opposite sides of the same audit
relationship: the recipient (who wants to avoid the $2M-style clawback) and the CPA firm (who wants to test
efficiently under GAGAS). Nothing I read forecloses either one, and nothing forces a switch to a different
asset, checker, or mistake, the instrument, the mistake, and the asset all still fit both readings. But
they are not the same GTM motion or the same JTBD sentence, and the room's rubric scores "clarity of target
customer" as its own line. **NONE, no principled mutation is forced by this round's evidence, but the
candidate should pick a primary buyer (the recipient's finance office, since it is the party that actually
writes the $2M check) and carry the CPA firm as a secondary/channel buyer, before the next round of work.**
This is a proposal, not a mutation I am making.

---

## 6. RUBRIC SCORES

No call has been made on this candidate, so criterion 3 is capped at 4 regardless of magnitude, per the
board's own standing convention.

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Clarity of target customer | 3 | Two named, real, sized-in-part segments, but two different buyers with no primary named yet |
| 2 | Clarity of JTBD | 3 | One clear sentence per buyer, but the two buyers' JTBDs are not the same sentence |
| 4 | Differentiation and uniqueness | 4 | Real, sweep-based rung-4 clean pass (K3 tested and did not fire); UNEXPLAINED reason for the gap, not fully resolved |
| 3 | Significance and magnitude of unmet need | 4 | D1 VERIFIED and 80x the statutory floor, annual frequency VERIFIED; capped at 4, no salience call made |
| 5 | Performance improvement over existing solutions | 2 | No measured number; the compounding/learning-loop claim has a real, unaddressed sparse-label problem |
| 6 | Size of market opportunity | 2 | Two real countable anchors (40,000 Single Audits/yr; 1,512 CHCs) but the segment-specific count is NOT VERIFIED |
| 7 | Market / technical / execution risk | 2 | Cold-start needs multiple client-audit-years to accumulate correlated outcomes even though pooling is legally clear; two-buyer ambiguity is itself a GTM risk |

**Lowest criterion: 2 (tied on 5, 6, 7). Sum: 20.**

---

## 7. VERIFIED / NOT VERIFIED

**VERIFIED (fetched and read):**
- 2 CFR 200.516 text (Cornell LII, law.cornell.edu/cfr/text/2/200.516), $25,000 threshold, auditor's
  reporting duty, quoted above.
- 2 CFR 200.501 text (Cornell LII, law.cornell.edu/cfr/text/2/200.501), $1,000,000 Single Audit threshold,
  quoted above.
- GAO-24-106173 (gao.gov/products/gao-24-106173), "about 40,000 single audits were submitted to the FAC"
  against "$1.1 trillion of awards," FY2023.
- FAC API terms page (fac.gov/api/terms/), no redistribution/pooling/commercial-use restriction found;
  public-availability basis quoted (2 CFR 200.512(b)(1)).
- Wegner CPAs webinar page (wegnercpas.com/webinars-2/), "Strengthening Your Single Audit Readiness,"
  free, recorded 07/21/2026.
- OMB's May 2026 Uniform Guidance rewrite coverage (Pease Bell, peasebell.com/insights/omb-2026-uniform-
  guidance-overhaul; CRA GovAffairs, cra.org/govaffairs/blog/2026/06/omb-regulatory-action-uniform-
  guidance), thresholds/cost principles "largely untouched," EO 14322 "Improving Oversight of Federal
  Grantmaking" driving increased, not decreased, accountability requirements; comment period closed July
  13, 2026, proposed effective October 1, 2026.
- NACHC, "America's Health Centers: By the Numbers" (nachc.org), 1,512 CHCs.
- D1 (North Shore Community Health / HHS OIG, $2,000,000), inherited from ideation-B.md as established
  per dispatch instructions; not independently re-fetched (quote reads consistently against the verified
  regulatory text above).

**NOT VERIFIED:**
- The specific "auditors sample dozens, not thousands, of transactions per major program" figure (no
  citable AICPA/GAGAS source reached before the session's web-search budget was exhausted).
- D3 comp bands beyond the aggregator/title level (ZipRecruiter, Indeed, Glassdoor summaries only; no
  employer ATS or portal posting reached, a recorded toolchain limit, not a world-finding).
- Exact count of nonprofits/higher-ed institutions (as distinct from state/local governments) subject to
  the $1M Single Audit threshold; exact count of CPA firms performing Single Audits for this band (AICPA
  GAQC's "more than 450" is member firms only, a floor, not a full count).
- Rung 1.5 patent search: no on-point granted claim found across multiple search-engine-directed queries,
  but Google Patents' own search index was not reached directly (its search UI did not render through the
  fetch tool), so this is a weaker not-found than a direct search would produce.
- Whether any grant-management or continuous-audit vendor not covered in this sweep (the space was searched
  by incumbent vocabulary, grant management, post-award, cost principles, subrecipient monitoring,
  effort reporting, but is not exhaustively enumerated) makes this exact claim; the rung-4 sweep is real
  but time-boxed, not a full competitor census.
