# Predictions, ROUND 5 - the subcontractor claim-notice candidate, recorded BEFORE dispatch

**This is not a generation round. Round 4 generated 12 and screened 3, all dead; 9 remain unscreened.
Generation stops 2026-09-14. This round closes the open rungs on candidate 4 (construction
change-order / delay-claim NOTICE), the only lane that STRENGTHENED this week and the only live
candidate that has never been gated.**

## The one-sentence differentiated claim being tested

> *For a specialty trade subcontractor, we read their executed subcontract and the prime contract
> together and tell them the actual date by which notice of THIS specific event must be given, and
> whether missing it forfeits the claim.*

## Standing calibration in force (from round 4, and it is the correction that matters)

**Verdicts 6 of 7 correct; rung placement 0 clean of 6.** Cause: I predict from the most INTERESTING
mechanism I can see, and the ladder stops at the earliest one. **The rule now: name the mechanism, then
ask what a LAZIER screener would have found first, and predict THAT.**

## What I predict, per lane

| Lane | I predict | The mechanism I think kills it | Confidence |
|---|---|---|---|
| **A. Associations (rung 3, free substitute)** | **This is where I think it dies**, and it is the lazy-screener answer rather than the interesting one | **Rung 3.** ABC, AGC, NECA, MCAA or SMACNA publishes a free notice-provisions checklist or contract-review guide keyed to the standard forms, to members, as a membership benefit. The ASA Info Hub "Model Contract Language" category is the known highest-risk instance and is behind a login; I expect one of the five UNSWEPT associations to have the same thing in the open. **Kill rule 6 shape: PUBLISHES the answer.** Counter-consideration already in evidence: law firms produced a CLEAN not-found on templates, which is the opposite of the Levelset outcome | Medium-high |
| **B. Generic contract-AI (rung 4 + rung 1.5 patent)** | **The hole I found reading STATE, and the sweep never touched it** | **Rung 4.** The platform sweep checked CONSTRUCTION products and found every date field to be user-entered. It never checked the **CLM / obligation-extraction** category - Icertis, Agiloft, Evisort, Ironclad, Luminance, Sirion, LinkSquares, DocJuris, Conga, Malbek - whose entire published pitch is extracting obligations and deadlines FROM contract language. That is my claim stated generically. **And round 4 proved a granted patent is invisible to product pages** (Resideo US11282374B2). I expect a granted claim on deadline/obligation extraction from contract text to exist; per rung 1.5 that is a G1/G3 finding, never a kill | Medium-high |
| **C. Demand (rung 2.5 D3) + economics (rung 6)** | **D3 fails a third time** | Not a kill by itself, but **D3 has now failed twice on this candidate and the third failure is the unpaid-market tell** - the same signal that downgraded inspection readiness ("what looks like an UNSERVED market reads more like an UNPAID one"). D1 is strong here and is a COURT's number ($1.56M waived in *Cascade*), and round 4 taught me explicitly to stop letting a strong D1 raise my survival estimate | Medium |

## The interesting mechanism I am deliberately NOT predicting, per the calibration rule

**Rung 5b, attribution.** Whether a notice preserved a claim resolves months or years later, usually in
settlement, so the graded label may never come back cleanly. STATE already flags this as the weakest
link in the candidate's AI-native story. **I think it is true and I do not think it is what kills it
first** - that is exactly the error pattern round 4 identified.

## My bet

**KILL at rung 3 or rung 4. If it survives BOTH lanes A and B, this is the strongest candidate the
project has produced and it goes straight to the Final Gate with a pass statement written first.**

## What would make me wrong in a way worth learning from

If lanes A and B both come back clean, the emptiness needs an explanation under **[C-53]**, and the
explanation is already written in STATE and is unusually good: **notice tracking is adversarial to the
GC, so no GC-side platform builds it, and the clause is drafted bespoke rather than copied, so it cannot
be looked up.** That is reason (i)-adjacent but not identical - it is a *structural adversary* reason
rather than a legal-assembly one. **If that holds, C-53 needs a fourth reason.**

# SCORING - filled in as lanes land

## LANE B - generic contract-AI (rung 4) + patent (rung 1.5). **I PREDICTED KILL. IT SURVIVED.**

| I predicted | Actual | Verdict? | Rung? |
|---|---|---|---|
| **KILL at rung 4**, medium-high confidence. My reasoning: the CLM / obligation-extraction category's entire published pitch is "extract obligations and deadlines from contract language," which is my claim stated generically, and the construction-only sweep never touched it | **SURVIVES.** 15 CLM vendors read directly: **one passes half (i), none passes half (ii), none reads two contracts in a chain.** Patent search on the full claim is a **clean not-found** | **NO** | n/a |

**This is the first time this round a prediction failed toward survival, and the failure is instructive.**
I reasoned from the category's SLOGAN ("extract obligations and deadlines") rather than from its product
pages. The category extracts dates that are WRITTEN IN the document. It does not compute one, and with a
single exception it does not try.

**THE CLAIM SPLITS CLEANLY IN TWO, AND ONLY ONE HALF IS CONTESTED.**

- **Half (i), DERIVING the date: contested by exactly one vendor, and honestly it is a good hit.**
  **ContractPodAi / Leah**, `leahai.com/use-cases/obligation-management`, verbatim: *"Critical dates are
  calculated with precision, including chained dependencies, notice periods, and jurisdiction-specific
  business day rules."* **"Calculated," "chained dependencies," "business day rules" is date COMPUTATION,
  not field capture**, and it is the only instance found anywhere. Two limits, both real: the chaining is
  **within one contract** (no mention of a second contract, flow-down, prime or subcontract anywhere on
  the page), and the stated stakes are commercial, *"Renewal windows close, cure periods lapse"* and
  *"revenue leakage from untracked renewals."*
- **Half (ii), the CONSEQUENCE - waiver, forfeiture, condition precedent: UNCLAIMED BY ALL FIFTEEN, and
  unclaimed in the patent literature.** Not one vendor tells a user that missing the date destroys the
  claim. The nearest anyone comes is commercial penalty language (Icertis: *"avoid penalties"*, *"service
  credits"*).

**The rest of the category is capture, not computation, and two vendors say so outright.**
**Robin AI is the affirmative opposite of the claim**: ML labels the clause, then *"the user can enter the
event date."* **Agiloft's own user guide** defines the two fields as *"The Date Due allows selection of a
day and time, and the Advance Notification Date is when the system will send an email notification"* - a
picker plus a lead-time, **the identical pattern the construction sweep found**. LinkSquares ships a fixed
113-field extraction schema. Summize extracts dates already written and syncs them to a calendar.

**⚠ AND THE SHARPEST SINGLE DATA POINT IS SPELLBOOK, because it is a generic vendor on its OWN
CONSTRUCTION PAGE.** `spellbook.com/learn/ai-construction-contract-review` claims *"AI highlights key
contract obligations and automatically verifies compliance with construction regulations."* Notice
provisions, notice of claim, time bars, condition precedent, waiver, flow-down and prime/subcontract
reading are **all absent** - on the page where the category points itself at this exact industry.

**RUNG 1.5, PATENTS: A CLEAN NOT-FOUND ON THE CLAIM, with two documents that go to the gate as G1/G3
evidence rather than as kills (per METHOD rung 1.5, a hit is never a kill).**

- **US20220092711A1 (Simplicontract) is the near-miss and it is ABANDONED** - final rejection 2024-06-04,
  discontinued 2025-01-07, no granted patent in the family. Its spec discloses half (i) almost verbatim:
  *"the NLP... interprets the language of the contract, determines the expiry date and calculates for
  arriving at the exact date by when a notice needs to be issued in case of a termination."* **It is prior
  art, not an enforceable right.** It also means somebody tried this and did not finish.
- **US11416956B2 (Coupa), granted 2022-08-16, ACTIVE TO 2041, is the one to watch.** Its CLAIMS recite
  *"cure and notice periods, and carve-outs"* and *"event-triggered notification"* but contain **no
  date-computation language and no waiver, condition precedent or subcontract.** Its DESCRIPTION does:
  it defines *"Waiver: Language indicating that one or more parties has waived or relinquished or gave up
  a right"* and states *"Contract 222 may describe itself as a subcontract under Contract 111"* with
  *"master, standalone, sub-contract and other relationships."* **Description is not claim scope.** Carry
  it to the gate; do not treat it as a kill.

**The six unswept construction products all fail both halves**, and four are not in the contract-document
business at all (CompanyCam photos, Billd material financing, Adaptive project accounting, Kojo materials,
Bridgit workforce planning). **Contractor Foreman is a contract GENERATOR, not a reader** - *"Create
detailed subcontracts with terms, conditions, and scope of work"* - and its only date tracking is for
PERMITS, user-entered.

**⚠ A PROVENANCE INCIDENT WORTH MORE THAN ONE VENDOR FINDING, and the agent caught it itself.** A search
engine returned, presented as Ironclad's own copy, a sentence saying their AI *"calculates or surfaces the
notice deadline... and explains the consequence of missing the window."* **That is a direct hit on BOTH
halves and would have killed the candidate.** The agent fetched the page to confirm and **the sentence is
not there.** It was search-engine synthesis. **This is rule 7 catching a fabricated kill rather than a
fabricated survival, which is the first time that has happened here**, and it is the argument for the
standing rule that a vendor claim is verified by direct fetch or it is not verified.

**NOT VERIFIED, and honestly stated:** **Sirion** (site 403s to every fetch - its patent was read and is
clear, the product is not), **Malbek**, **Lexion**, and Icertis' main obligation-management page (login
wall). **Conga's obligation field definitions 404'd**, so whether its due date supports a computed offset
is unknown.

**WHAT THIS DOES TO THE CANDIDATE.** The differentiated claim must now be written to lead with half (ii),
because half (i) has one credible claimant. **The defensible sentence is no longer "we compute the date."
It is "we tell a subcontractor whether missing it forfeits the claim, by reading their subcontract against
the prime" - and nothing in fifteen CLM products, six construction products or the patent literature makes
that statement.**

## LANE A - associations, rung 3 free substitute. **I PREDICTED KILL. IT SURVIVED.**

| I predicted | Actual | Verdict? | Rung? |
|---|---|---|---|
| **KILL at rung 3**, medium-high. I expected one of the five unswept associations to publish a free notice-provisions checklist keyed to the standard forms, or to offer free member contract review. **Kill rule 6 shape: PUBLISHES the answer** | **SURVIVES.** Everything found is tier (a) commentary or tier (b) restatement of the standard forms. **Nothing produces a DATE or a go/no-go for an executed subcontract.** The free contract-review benefit is real but is a **legal HOTLINE**, and the review itself is discounted, not free | **NO** | n/a |

**Both of my kill predictions this round were wrong, and they were wrong the same way: I predicted from
what the category SOUNDS like it must contain rather than from what its documents actually say.**

**THE STRONGEST ARTIFACT FOUND, and it is the closest anything has come to tier (c).**
*Subcontractor Contract & Collections Handbook*, ©2025, published by the **California Chapters of NECA**,
authored by Sweeney Mason LLP, free, no login, ~85pp.
`ccneca.org/NECA_Subcontractor_Contract_and_Collections_Handbook.pdf` It ships real template letters  - 
**Form 1 Response to Directed Change Notice, Form 2 Notice of Changed Condition, Form 3 Constructive
Change Notice, Form 4 Change Order Proposal Checklist, Form 18 Change Order Request Demand Letter.**

**And it stops exactly short of the date, in a way that is almost too on the nose to be believed.**
- **Form 4's item 2 is the question, unanswered:** *"When should the proposal be submitted?"* **The
  checklist asks it and does not answer it.**
- The body text names the problem and declines it: *"Public contract clauses usually require the
  contractor to give written notice of its contention within **a specified number of days**… the
  possibility of being foreclosed from asserting claims of extra work makes it imperative for the
  contractor to comply."* **It never supplies the number, because it cannot.**
- Form 3's operative text is a protest letter with **no deadline field, no day count, no trigger date.**

**⚠ AND HERE IS THE FINDING THAT IS WORTH MORE THAN THE VERDICT. EVERY HARD DAY-COUNT IN THAT HANDBOOK IS
STATUTORY** - 20-day preliminary notice, 90-day lien, 30-day stop payment notice, 15/75-day bond notice.
**That is the Levelset category exactly.** The free layer reaches every notice with a PUBLIC STATUTORY
SCHEDULE and stops precisely where the schedule becomes private.

**This is now confirmed on FOUR independent instances and it should be treated as the candidate's central
structural fact rather than as a lucky gap:**
1. **Levelset** ships a free lien-notice deadline calculator and nothing for contract notice.
2. **The NECA handbook's** day-counts are 100% statutory; its contract-notice guidance is prose.
3. **ASA's own topic pages are asymmetric**: on liens it lists a 50-state resource (*"FASA Lien & Bond
   Claims in the 50 States"*); on change orders it lists only prose titles.
4. **NASBP is a clean not-found** - bonding checklists and a bond-forms library, no notice tool.

**THE REST, association by association, all tier (a) or (b):**
- **SMACNA Contracts Bulletin #98 "Change Orders and Extra Work" was read IN FULL and grepped. The words
  "notice", "condition precedent", "waiver", "forfeit" and "timely" DO NOT APPEAR.** The only "days" in
  the bulletin is a form-filling instruction. Its advice is upstream: *"review the original contract to
  determine the steps required."* No bulletin in the whole index covers notice or claim deadlines.
- **MCAA's** change-order primer is member-free and its published contents list - identify and manage
  change orders, organize and submit a claim, time impact analysis, concurrent delay - **contains no
  notice-timing topic at all.** Its productivity study points AWAY from a tool: *"have experienced
  construction personnel review applicable contract documents."* **NECA formally endorses this MCAA
  document, so the two largest MEP associations point at the same guide and it does not compute a date.**
- **ABC national has nothing**; its Contract Document Resource Center is a ConsensusDocs promotion and its
  Law Library is litigation funding. **Chapter level names the stakes precisely and offers no tool** - ABC
  Ohio Valley: *"Many contracts require 3-day or 7-day written notice… Missing those deadlines can waive
  claims even when the contractor is right."*
- **AGC** publishes a free construction-law newsletter, tier (a). Its best free artifact is the 2013
  **ConsensusDocs Guidebook**, which does give clause-by-clause day counts - *"notice of a claim should be
  made within 21 days after the occurrence"* - **but that is the STANDARD FORM's number, and the EDGAR
  survey already established that executed subcontracts do not follow the standard forms.**
- **AIA and ConsensusDocs both publish free commentary and both hand the problem straight back.** AIA:
  *"A contractor's failure to file a notice of claim within a prescribed time period, with few exceptions,
  will forego any chance of compensation"* - then instructs the reader to review their own documents.
  **AIA's article never mentions A401 or subcontract flow-down at all. ConsensusDocs' does not address
  subcontractors.**
- **The free-review benefit exists and is NOT what I predicted.** SADV: *"special rates for contract
  review, a free hotline"* - **hotline free, review discounted.** ASA Central PA's "free contract review"
  is a **webinar series**, not a review of the member's own subcontract. Membership behind it is priced:
  **ASA Georgia $975/yr.**

**⚠ THE ONE LIVE KILL RISK THE LANE COULD NOT CLOSE, and it must be chased before the gate.** An
aggregator listing describes a **"Notice Deadline Calculator"** - *"tells you exactly when your claim
notice is due, based on AIA A201-2017, ConsensusDocs 200, or a custom day count. Free, no signup."* The
listing is real (`launches.uicomet.com/products/notice-deadline-calculator-J8BmPFc`); the product's own
site and its Product Hunt page were unreachable (403 / Cloudflare) and **the tool was never exercised.**
**Even taking the copy at face value it works from a standard form or a day count the user supplies - it
does not read an executed subcontract against a prime - but it is the nearest miss on the board and it is
unconfirmed.**

**ALSO UNCONFIRMED:** an Associated Subcontractors of Massachusetts *"legal hotline… free of charge"*
(site 403s); the ASA Info Hub's four named change-and-claims resources (login, not bypassed); AGC's
member-only ConsensusDocs 751 comments (login); and **SMACNA's paid "Guidelines for Change Orders"**
($75 non-member, free to members), whose TOC includes *"Negotiating and Confirming the Change (Preserving
the Subcontractor's Rights)"* and which was not obtained.

### Main-session follow-up on lane A's one open risk, run 2026-09-07 immediately after

**THE "NOTICE DEADLINE CALCULATOR" IS STILL UNRESOLVED AND I AM RECORDING IT AS SUCH.** Its only
reachable trace is the `launches.uicomet.com` listing, which **403s to a direct fetch**. The identical
descriptive sentence came back from two separate searches, which is what a search engine does when
paraphrasing one indexed listing - **and lane B just demonstrated that this exact domain's search
summaries fabricate vendor copy.** So the snippet is NOT evidence. **No vendor, no domain and no working
instance of this tool has been reached.**

**What can be said without it:** even at face value the description is *"based on AIA A201-2017,
ConsensusDocs 200, or a custom day count."* **The EDGAR survey already established that executed
subcontracts do not follow the standard forms** - 5 days modal, express forfeiture in 5 of 6, each
distinctive clause phrase returning exactly one document in all of EDGAR full text, i.e. bespoke drafting.
**A calculator seeded from A201 and ConsensusDocs 200 answers the question the EDGAR survey proved is the
wrong one.** It is tier (b) in a calculator's clothing. **Chase it once more before the December pitch;
it does not block the gate.**

**Two adjacent things checked and cleared:**
- **The Chrome Web Store "Legal Deadline Calculator"** (`lpmgmfbjmmfpfchacoahaoplehlglkik`) is a court
  filing tool: *"Compute legal deadlines using federal holiday & business rules."* Published by an
  individual, **9 users**, updated 2026-03-17, **no mention of construction, subcontracts, claim notice or
  contract-derived deadlines.** Not a competitor.
- **Kamine Construction Law Firm's "Notice, Claim & Lawsuit Deadlines"** is the law-firm deadline chart
  lane A's clean not-found predicted should not exist. **It exists, and it is a FIFTH instance of the
  structural finding rather than a kill.** Its categories are *preliminary notice, bond claim notice,
  mechanics lien, stop payment notice, and Government Code claim* - **every one statutory.** (Evidence
  level: search index only. `kamineconstructionlaw.com` serves an **expired certificate** and could not be
  fetched directly.)

**So the count is now FIVE independent instances**: Levelset's free calculator, the NECA handbook's
all-statutory day counts, ASA's 50-state lien resource against prose-only change-order titles, NASBP's
clean not-found, and Kamine's chart. **The free layer stops at the statutory line every single time.**
**That is no longer a gap the project noticed. It is a boundary with five data points and a stated cause,
and it is the strongest single asset this candidate has.**

## LANE C - demand (rung 2.5 D3) + economics (rung 6). **PREDICTION HALF RIGHT, AND IT IS THE LANE THAT DECIDES THE CANDIDATE.**

| I predicted | Actual | Verdict? |
|---|---|---|
| **"D3 fails a third time"**, medium confidence, and I said the third failure is the unpaid-market tell | **D3 did not fail the way it failed twice before. It failed BETTER-EVIDENCED, and the finding is sharper than a failure.** Three real named-employer postings were reached; **none is the job.** And the decisive negative is new: **the function IS staffed, on the other side of the transaction** | **YES, on substance** |

**ROUND 5 FINAL: I predicted KILL on all three lanes. Two survived outright and the third capped the
candidate without killing it. 0 of 3.** After going 6 of 7 on verdicts in rounds 3 and 4, that is worth
sitting with rather than explaining away. **The common error in all three: I predicted from what a
category sounds like it must contain, and each time the documents said otherwise.**

**WHY D3 IS EMPTY, AND THE REASON IS WORSE FOR THE CANDIDATE THAN A BLANK WOULD HAVE BEEN.**
- **Zero postings, at any subcontractor, for a role whose duties include serving claim notice, change
  order notice, or preserving a claim against an upstream party.** Zero for "notice of claim," zero for
  "notice of delay."
- **The NECA Career Center - the electrical industry's OWN national job board - carries 14 postings and
  all 14 are field craft.** Service Electrician, Industrial Electrician, Apprentice. **Zero contract
  administration roles of any kind.**
- **⚠ AND THE ROLES THAT DO CARRY CLAIM AND NOTICE DUTIES ARE ALL AT THE BANNED CUSTOMER TYPES:** the
  Metropolitan Council (owner) negotiating *"change orders, contract conflicts, or claims"*; a San Jose
  owner-side role processing *"Notices of Potential Change (NOPCs)"*; Nibbi Bros, Matt Construction,
  McShane (**GCs**); McKinley (**A/E**). **The function is staffed on the owner, GC and A/E side and not
  on the subcontractor side.** That is not an absence of evidence. It is evidence of an absence, and it
  says the money to administer notice sits with the parties the sub is noticing.
- The three real hits confirm it rather than rebutting it. **Baker Construction's Federal Contract
  Specialist** handles *"Request for Equitable Adjustments (REAs)"* but is FAR/DFARS-specific at a
  national firm far above the band, no salary posted. **Ferguson Electric's PM is $95,000-$125,000 stated
  under NY pay transparency** - but change orders are **one bullet of about fourteen** and **notice and
  claims appear nowhere in the posting.** **Rosendin's Corporate Subcontract Administrator is the mirror
  image of the customer**: Rosendin issuing agreements to its OWN subs, i.e. downstream, not upstream.

**APPLYING THE RULE THAT ALREADY EXISTED - this is METHOD Part 2b as written before this round, not a new
rule, so C-58 does not apply and no pass condition moved.** *"An EMPTY D3 CAPS THE CANDIDATE... it clears
only if D1 is larger than the annual cost of the labour it would replace at one customer."*
**D1 here is $1,561,818.66 waived in *Cascade*, against a $95k-$125k PM salary of which this task is a
fraction. Nominally D1 wins by an order of magnitude. But D1 is a LITIGATED TAIL EVENT, not a fee
schedule, and lane C established that NO RATE EXISTS ANYWHERE**, so the expected annual loss per firm
cannot be computed. **$1.5M times an unknown probability is not a number.** If the true frequency is one
firm-year in five hundred, the expected loss is $3k a year and there is no business here.

**⚠ THE UNPAID-MARKET TELL NOW HAS ITS SECOND, INDEPENDENT CASE AND SHOULD GRADUATE FROM HYPOTHESIS TO
RULE.** Instance one was inspection readiness (D1 $250, D3 empty). Instance two is this candidate,
**different industry, different customer, different mechanism, same signature: verified competitor
absence sitting on top of an empty D3.** Round 4 already wrote the warning in plain words - *"I have been
reading a strong D1 as a good sign. It is not a sign of anything except that the mistake is real"* - and
this is the second time the same shape has produced the same result.
**Note carefully: this candidate is CAPPED by the rule, not killed by it, so the rule is not being
confirmed by the very candidate it condemns.**

**⚠ AND TWO AGGREGATE FINDINGS THAT CUT AGAINST THE PREMISE AND MUST NOT BE BURIED.**
- **Arcadis Global Construction Disputes Report 2019 ranks "Failure to serve the appropriate notice under
  the contract" as the #3 cause of disputes - IN THE UNITED KINGDOM.** In **North America**, verbatim,
  *"the most common cause for disputes in North America was errors and/or omissions in the contract
  documents"* for the fifth year running, and *"Failure to properly administer the contract... did not
  appear in the top three this year."* **Notice does not appear in the North America top three in any
  year shown.** The candidate's core premise is best evidenced in the wrong country.
- **HKA CRUX Insight 2025, across 2,200+ projects worth $2.433 trillion: "Contract
  management/administration failures: less than 9% (nearly halved)." The trend is DECLINING.**
- **Both datasets study global megaprojects** - HKA's average project capex is $1.25 billion - **so
  neither speaks to a $2M commercial subcontract at a 40-person electrical firm.** That cuts both ways
  and is the honest statement of it.
- **No published rate, average or frequency of subcontractor claims waived on notice grounds exists
  anywhere.** Not Arcadis, not HKA, not AIA, not ConsensusDocs, not surety data, not academia. **The
  literature is 100% case-anecdote and doctrine.** Our three cases are the form the evidence comes in;
  there is no aggregate to escalate to.

**RUNG 6 IS ANSWERED AND IT IS THE CLEANEST MARKET NUMBER THE PROJECT HAS EVER HAD.**
**US SUSB 2022 (released 2025-04-10), enterprise employment size, bands matching 20-299 EXACTLY, no
interpolation: 42,774 specialty trade contractor FIRMS with 20-299 employees.** Of those **19,252**
building equipment contractors, **7,791** electrical, **10,425** plumbing/HVAC, **2,419** poured concrete.
All construction (NAICS 23) in band: 61,458. **Carry the caveat: "enterprise" counts the whole company,
so a firm owned by EMCOR, Comfort Systems or APi is counted at parent size.** That is a rubric-criterion-6
answer sized from a countable government source, which is exactly what a 5 requires.

**DO NOT USE:** the "Airco Mechanical" posting from the earlier sweep. Lane C tried to verify it and found
the search snippet had **blended two different postings** (a Washington State L&I certified-payroll
reference with a Round Rock, Texas location). **It is withdrawn.** That is the third fabricated or blended
search artifact caught in a single round.
