# Screen A4, Candidate 4: H-1B Petition RFE-Risk Score

Customer: mid-size tech/IT-staffing employers filing ~10-200 H-1B petitions/year through in-house
immigration staff or outside counsel. Source: `ideation-A.md` lines 227-301.

**A sourcing note that governs this whole file, stated once up front:** the web-search budget for this
session (200 calls) was exhausted partway through Rung 4. Several findings below rest on a WebSearch
AI-summary rather than a fetched primary page, and are explicitly labeled NOT VERIFIED AT PAGE even where
I believe them true. Every fetched (WebFetch-read) source is labeled VERIFIED. Do not upgrade a NOT
VERIFIED AT PAGE line without going back and fetching it.

---

## 1. THE CASE FOR

The strongest number on the board is still **D1, VERIFIED, established by the ideation agent from two
fetched primary sources and independently corroborated this session by a third, freshly fetched one**:
USCIS's own G-1055 fee schedule prices premium processing on an I-129 H-1B at **"Paper Filing: $2,965"**
plus a **$780/$460** base fee and a mandatory **$500** fraud-prevention fee
(https://www.uscis.gov/sites/default/files/document/forms/g-1055.pdf); NFAP's December 2024 brief prices
the RFE itself as a distinct, non-refunded line: **"Attorney Fees if a Request for Evidence, $2,000 to
$4,500"**
(https://nfap.com/wp-content/uploads/2024/12/H-1B-Petitions-and-Denial-Rates-For-FY-2024.NFAP-Policy-Brief.December-2024.pdf).
This session I fetched and read NFAP's **November 2025** follow-on brief directly (VERIFIED) and it raises
the stakes further: total legal-plus-government cost for one H-1B hire through green card is **"up to
$34,900 over a number of years, and as high as $50,000"**
(https://nfap.com/wp-content/uploads/2025/11/H-1B-Petitions-and-Denial-Rates-For-FY-2025.NFAP-Policy-Brief.2025.pdf,
p.3). Money is real, it is not refunded on an RFE, and the petitioner (my customer) pays USCIS and counsel
directly, nothing here requires a third party to release funds, so rung 1 clears clean.

The best rung-2 pass: the duty to establish specialty occupation status runs to **the petitioner**, i.e.
the employer, not to any counterparty, see KILL section below. That means this is a K2-clean instrument,
which is rarer on this board than a K1 pass.

The single most consequential new finding this session, VERIFIED by direct fetch, cuts the other way from
what `STATE.md` line 808 worried about: the $100,000 fee (Proclamation 10973) is **narrower than the
"shrinking the customer base" fear implies**. NFAP's own November 2025 brief, quoting USCIS's own
guidance, states the fee **"would not apply when people change from one visa category to another without
leaving the United States, such as moving from F-1 student status to H-1B status."** It hits only new
petitions for beneficiaries entering from outside the U.S., extensions, amendments, and changes of status
filed from within the U.S. (the majority of filing volume: NFAP counts 291,542 continuing-employment
approvals in FY2025 against 114,806 for initial employment) are untouched by it either way. The customer
base this candidate targets is largely intact regardless of that fee's fate. (Its litigation status , 
vacated by a Massachusetts district court June 8, 2026, stayed pending a First Circuit appeal, with the
underlying Proclamation nominally expiring today, 2026-09-20, is NOT VERIFIED AT PAGE this session; it
rests on converging law-firm client alerts (Littler, Klasko, HRWatchdog) I did not independently fetch.)

---

## 2. THE SCORED WEAKNESSES

- **Rung 4 / differentiation, criterion 4.** Prolexis's own product page (VERIFIED, fetched directly,
  https://prolexis.ai/) already offers, as a named optional feature: **"Optional: train a private model on
  your firm's winning briefs and RFE responses."** That is the same underlying capability this candidate's
  differentiated claim rests on, training an outcome model on one party's own private filing history
  rather than public criteria. Prolexis's own page frames its DEFAULT tool differently and more modestly , 
  **"Outcome likelihood estimator using base-rate USCIS approval data by form type and service center, a
  statistical estimate, not a prediction"**, but the private-model option exists today, on the incumbent's
  own page (G1). No named deployment of that specific feature and no stated outcome for it were found (G2
  and G3 do not clear, see KILL below), so this is a score, not a K3, but it is a real capability-gap
  finding: the "private ledger trained on your own past outcomes" idea is not a technology gap, it is
  already shipped as a checkbox by at least one incumbent. What is different about this candidate is the
  buyer (the employer directly, in its own case-management flow) rather than the law firm Prolexis sells
  to, a **distribution gap, not a capability gap** (METHOD.md Stage 4).

- **Rung 4 / differentiation, criterion 4.** SpaceLizit's own page (VERIFIED, fetched,
  https://spacelizit.com/industries/legal-compliance-services) states its **"AI pre-filing audit checks
  every H-1B, L-1, and O-1 petition against 10,000+ USCIS denial patterns"** and claims (vendor's own
  number, no named customer) **"RFE rates dropping from 25% to under 3%."** This is a generic-pattern
  competitor, not a private-ledger one, but it already occupies the "pre-filing RFE audit" one-liner as
  the room would hear it, adding to the crowded-claim-space weakness alongside Visalaw.ai and AutoPetition
  (both carried from the already-established I1 screen, `screens/2026-09-08-round11/I1-immigration-rfe.md`,
  not re-fetched this session).

- **Rung 3 / RATCHET + PUBLISHES, criterion 5.** The specialty-occupation evidentiary standard itself, the
  four-part test at 8 CFR 214.2(h)(4)(ii), is a free, public standard (general legal fact, NOT
  independently re-fetched at eCFR this session; carried from a WebSearch summary of NAFSA/AILA sources, so
  flagged NOT VERIFIED AT PAGE though it is well-established black-letter regulation). USCIS's own Policy
  Manual Volume 2, Part H exists as the free reference for it (VERIFIED, fetched,
  https://www.uscis.gov/policy-manual/volume-2-part-h), though on inspection it functions as an index into
  legal authorities rather than a worked petitioner checklist, so the PUBLISHES finding is real but weaker
  than a true step-by-step free substitute. The RATCHET problem is the sharper one: the model's stated edge
  is exactly the part that is NOT public, adjudicator- and service-center-specific tendencies, but a
  probability score built on that edge produces a "this wording is probably fine" signal that a risk-averse
  in-house team or outside counsel, already following the free public four-part test as the conservative
  floor, has no clean way to act on. Agreeing with maximal evidence is free; disagreeing with caution
  (filing lighter because the score says the risk is low) is the only saleable output and it is also the
  one a prudent petitioner's counsel is least likely to accept. (Un-fetched, general-knowledge framing , 
  NOT VERIFIED AT PAGE against a specific incumbent statement, but consistent with the RATCHET pattern
  already confirmed twice elsewhere on this board per METHOD.md C-62.)

- **Rung 5c, criterion 5.** The product's own selling point, testing several rewordings of a job
  description or duty list against the model **before** the final petition is assembled (ideation-A.md
  line 258-261), means the customer's most likely action on a high-risk score is to revise the language
  and file the revised version. The counterfactual outcome of the UNREVISED draft is then never observed.
  This is the same right-censoring failure METHOD.md documents for accept/decline recommenders (the
  skilled-nursing referral case, C-66): the tool can only ever grade the branch the customer acted on, so
  its own use suppresses exactly the training signal ("was my worry correct") that would validate it.

- **Rung 2.5 (D3), criterion 3.** I could not establish, within this session's exhausted search budget and
  the documented job-board-fetch-blocking tooling limit (METHOD.md, "EVERY MAJOR JOB BOARD 403s ON FETCH"),
  a job posting whose stated duty is specifically "score H-1B petitions for RFE risk before filing" at an
  in-house team of a 10-200-filing employer. What I found instead (WebSearch summary only, NOT VERIFIED AT
  PAGE) is that "Global Mobility / Immigration Manager" roles at companies this size are real and salaried
  ($48k-$120k range across postings referenced) but their described duties are coordination and compliance
  tracking, not petition-drafting risk judgment, that evaluative task traditionally sits with retained
  outside counsel, whose fee (the D1 numbers above) already prices exactly this judgment. That points
  toward the state **FILLED, TASK ABSENT** at the named customer (an in-house seat exists; this specific
  task is not in it) with the task itself **FILLED AT THE COUNTERPARTY** in the sense that a paid,
  professionally-liable outside party (counsel) already does it, not a clean EMPTY, but not a clean pass
  either. See D3 STATE section below.

- **Rung 6, criterion 6.** NFAP's November 2025 brief (VERIFIED, fetched) states **"28,277 different
  employers in the United States were approved to hire at least one new H-1B visa holder in FY 2025"** and
  **"95% were approved for ten or fewer new H-1B petitions in FY 2025 ... [and] 72% [of new petitions]
  went to employers with 100 or fewer approvals."** That bounds the >10-approval tail at roughly 1,400
  employers (5% of 28,277) for INITIAL employment alone, the true 10-200 band (which, per the candidate's
  own document-set description, would also include continuing/extension filings scored the same way) is
  therefore somewhere in the low thousands at most, not independently counted at that exact band by any
  source I fetched. This is a real but narrow market, and per the rung-4 finding above, the vendors
  already serving it (Prolexis, SpaceLizit) sell into outside counsel rather than direct to employers , 
  suggesting the practical point of sale for this exact task is already occupied.

---

## 3. KILL: NO KILL

- **K1 (money cannot move):** does not fire. The recoverable/avoidable amounts (D1, verified above) are
  well above any incumbent fee floor, and the petitioner (my customer) pays USCIS and counsel directly , 
  nobody else controls release of that money.
- **K2 (instrument doesn't bind the customer):** does not fire. The specialty-occupation burden of proof
  and the RFE process both run to the petitioning employer, not a counterparty. (The precise duty-holder
  sentence, "the petitioner must establish that the job it is offering to the beneficiary meets the
  following statutory and regulatory requirements", is carried from a WebSearch summary of
  NAFSA/AILA-sourced pages, NOT independently fetched at eCFR this session, so flagged NOT VERIFIED AT PAGE;
  the underlying structural fact that Form I-129 is filed BY the employer and the burden sits on the
  petitioner is basic, undisputed H-1B law.) The one piece I did fetch and verify directly, Cornell LII's 8
  CFR 103.2(b)(8)(iv)
  (https://www.law.cornell.edu/cfr/text/8/103.2), confirms the RFE **"will specify the type of evidence
  required ... sufficient information to respond"**, issued to the petitioner, supporting the same
  conclusion.
- **K3 CANDIDATE:** does not fire. Prolexis clears G1 (its own page states the private-model capability)
  but not G2 (no named deployment of that specific feature) or G3 (no stated outcome for it), all three
  are required conjunctively, and only a fresh gate agent can confirm a K3 in any case. SpaceLizit and the
  I1-established vendors (Visalaw.ai, AutoPetition) don't clear G1 for the private-ledger claim at all , 
  their own pages describe generic/aggregate pattern-matching, not one employer's own outcome history.
- **K0:** not evaluated here (Stage 0 room-gate is a main-session check, not this screen's job).
- **K4:** not applicable, no call has been run; this is a desk screen.

---

## 4. D3 STATE: UNRUN (for the named in-house customer), leaning FILLED AT THE COUNTERPARTY

I did not find, and could not search further to find (budget exhausted before a targeted job-posting query
completed), a job posting at a 10-200-filing employer whose duty is explicitly "score H-1B petitions for
RFE risk before filing." What is available (NOT VERIFIED AT PAGE, WebSearch summary of Indeed/ZipRecruiter
listings, not fetched, consistent with the documented job-board 403 limitation) is general "Global
Mobility / Immigration Manager" compensation data ($48k-$120k) whose described duties are coordination,
not risk judgment. The judgment task itself is, as far as this screen could establish, priced and
performed by retained outside counsel (the D1 attorney-fee figures above), which is closer to **FILLED AT
THE COUNTERPARTY** than to a clean EMPTY. Record this explicitly as UNRUN-AT-THE-NAMED-CUSTOMER rather than
EMPTY, per METHOD.md's rule that a search that could not reach a posting is NOT VERIFIED, not a finding.

---

## 5. MUTATION (Part 5, M0)

Two pieces of evidence gathered this session force a real reconsideration, though I propose only, I do
not mutate.

**Forcing evidence 1, the $100k fee is not the threat `STATE.md` line 808 flagged.** VERIFIED (NFAP,
fetched directly): the fee applies only to new consular-processed H-1B entries, not to extensions,
amendments, or changes of status filed from within the U.S., which make up the majority of filing volume.
The "shrinking customer base" concern that kept this candidate off the board is overstated as a blanket
worry, most of what this candidate scores is untouched by that fee regardless of its litigation outcome.
This does not force a mutation; it removes one that was never needed.

**Forcing evidence 2, the real overlap with I1 is about WHO does the evaluative work, not just which
candidate number it is.** Every vendor found on rung 4 that makes any version of this claim (Prolexis,
SpaceLizit) sells to immigration LAW FIRMS, and the D3 evidence (thin as it is) points the same way: the
task of judging whether a draft will trigger an RFE is currently performed by retained outside counsel, not
by an in-house "immigration staff" coordinator at the employer. That suggests the customer as pitched here
,  "in-house immigration staff... without a dedicated RFE-analytics function", may not be the actual
point of purchase. **A principled mutation to weigh:** narrow the customer to employers large enough to run
petition drafting through attorneys they employ directly (in-house counsel of record, not HR/mobility
coordinators who route everything to an outside firm), since that is the only version of "the employer" for
whom the evaluative task is genuinely in-house rather than one phone call away from I1's segment. I name
this as the forcing evidence and the candidate mutation; I do not adopt it.

---

## 6. RUBRIC SCORES

Scale 1-5, VERIFIED evidence only, criterion 3 capped by the D3 ambiguity above (not a clean EMPTY-tell 1,
but not a clean pass either).

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Clarity of target customer | 3 | Segment is named precisely (10-200 filings/yr, in-house staff), but rung-4/D3 evidence suggests the real buyer may be outside counsel, not this named customer |
| 2 | Clarity of JTBD | 4 | Clean Noul shape, single decision, no incentive-inversion found (unlike I1's RFE-billing inversion, a genuine improvement over that sibling candidate) |
| 3 | Significance/magnitude of unmet need | 2 | D1 strong and VERIFIED (two independent fetched sources), but D3 is UNRUN/ambiguous and leans toward the task already being FILLED at outside counsel |
| 4 | Differentiation and uniqueness | 2 | Prolexis's own page already ships the core "train on your own private outcome history" capability as an optional feature (G1, VERIFIED); four vendors total occupy adjacent claims |
| 5 | Performance improvement over existing solution | 2 | RATCHET (saleable signal is the one counsel can't act on) + 5c right-censoring (tool suppresses its own best training data) + no cross-customer compounding moat (single-employer ledger, by design) |
| 6 | Size of market opportunity | 3 | Real but narrow: bounded at roughly ~1,400 employers or fewer for the >10-petition tail (VERIFIED, NFAP), and the existing vendors already sell through outside counsel into this population |
| 7 | Market/technical/execution risk | 3 | Technology (Jev) is a commodity per the brief; the live risk is distribution (who is the real buyer), not technical feasibility of the scoring task itself |

**Lowest criterion: 2 (tied on criteria 3, 4, 5). Sum: 19.**

---

## 7. VERIFIED / NOT VERIFIED

**VERIFIED (fetched directly and read this session):**
- https://nfap.com/wp-content/uploads/2025/11/H-1B-Petitions-and-Denial-Rates-For-FY-2025.NFAP-Policy-Brief.2025.pdf, employer counts, denial rates, total cost, $100k fee scope
- https://prolexis.ai/, "private model" optional feature, base-rate estimator disclaimer
- https://prolexis.ai/blog/best-immigration-practice-management-software-2026, pricing $69-$119/user/month, outcome-estimator disclaimer
- https://spacelizit.com/industries/legal-compliance-services, "10,000+ USCIS denial patterns" claim, aggregate outcome claim
- https://www.law.cornell.edu/cfr/text/8/103.2, 8 CFR 103.2(b)(8)(iv) RFE-specificity text
- https://assets.equifax.com/ews/lawlogix/assets/EDGE-Agreement_Online-09-01-22.pdf, no aggregation/derived-data clause found in accessible MSA text (negative finding, incomplete: referenced separate ToS not located)
- https://www.uscis.gov/policy-manual/volume-2-part-h, functions as an index, not a worked checklist

**CARRIED FROM IDEATION / I1 AS ESTABLISHED (not re-fetched this session, per brief instruction):**
- https://www.uscis.gov/sites/default/files/document/forms/g-1055.pdf, G-1055 fee schedule
- https://nfap.com/wp-content/uploads/2024/12/H-1B-Petitions-and-Denial-Rates-For-FY-2024.NFAP-Policy-Brief.December-2024.pdf, RFE attorney fee $2,000-$4,500
- I1's vendor findings on Visalaw.ai and AutoPetition (`screens/2026-09-08-round11/I1-immigration-rfe.md`)
- USCIS FY2026 Q2 H-1B RFE rate (8.9%), cited in ideation-A.md, originally from I1

**NOT VERIFIED AT PAGE (WebSearch AI-summary only, not independently fetched, flagged, not relied on for the kill or the case-for beyond what is separately verified):**
- $100,000 fee litigation status (vacated 2026-06-08, stayed on appeal, Proclamation 10973 expiring 2026-09-20), Littler, Klasko, HRWatchdog, Lexology summaries
- 8 CFR 214.2(h)(4)(ii) specialty-occupation four-part test and petitioner burden-of-proof sentence, NAFSA/AILA-sourced summary
- Global Mobility/Immigration Manager job-posting duties and comp bands, Indeed/ZipRecruiter summary (job boards 403 on fetch, a documented tooling limit, not a finding about the world)
- Absence of an exited predecessor / abandoned patent, searched twice (web + Google Patents XHR query), no hit found; absence of a negative is not a positive, recorded as NOT FOUND WITHIN BUDGET, not as a clean field
- Buyer's own job posting naming immigration case-management tooling (LawLogix/Deel/Envoy Global), query not completed before web-search budget exhausted
