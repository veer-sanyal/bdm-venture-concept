# Screen: Candidate 3, "Claims File Compliance Severity Grading" (ideation-B.md, lines 127-177)

Blind screen, round 17. Full ladder run per SCREEN-BRIEF.md. WebSearch budget was exhausted mid-session
(hard session cap, not a finding about the world); remaining gaps are marked NOT RUN / NOT VERIFIED rather
than inferred.

---

## 1. THE CASE FOR

The strongest thing on the board for this candidate is a clean, instrument-quoted D1 plus a real D3 seat,
even though the D3 seat sits off-band. **D1, VERIFIED**: California Insurance Code § 790.035, "any person
who engages in any unfair method of competition or unfair or deceptive act or practice defined in Section
790.03 is liable to the state for a civil penalty not to exceed five thousand dollars ($5,000) for each
act, or, if the act or practice was willful, ... not to exceed ten thousand dollars ($10,000) for each act"
(https://www.law.cornell.edu/regulations/california/10-CCR-2695.1, cross-referencing 790.03/790.035 , 
statutory text corroborated by FindLaw/Justia mirrors of § 790.035). Per-act penalties stack across a
single file with multiple violative acts, so the exposure scales with how many distinct UCSPA failures a
file contains, not just whether one was found.

The best rung-2.5 pass is **D3, FILLED (off-band)**: QBE's own applicant-tracking listing, "Claims
Compliance Analyst (Workers Compensation)," Madison, WI, salary band **$69,500–$114,500**, duties
"facilitating regulatory examinations," "conducting compliance-focused audits," "overseeing critical
federal and state reporting obligations" (job exists at
https://qbe.wd3.myworkdayjobs.com/qbe-careers/job/madison-wi-usa/claims-compliance-analyst--workers-compensation-_356023/apply,
duties corroborated via aggregator mirror at
https://www.complyapply.com/jobs/537576387-claims-compliance-analyst-workers-compensation-at-qbe since the
ATS page itself is JS-rendered and would not return text to the fetcher, this is the job-board toolchain
limit METHOD.md already names, not a finding). This is a real, currently-funded seat whose job description
IS the task the candidate sells, but QBE is a large global insurer, not the sub-300-employee TPA/small
regional insurer the tuple names as the customer, so it establishes the task has a budget line somewhere
in the value chain without confirming it at the target band.

Rung 6 gives a countable, if broad, market: IBISWorld's NAICS 52429 ("Third-Party Administrators &
Insurance Claims Adjusters") reports **123,451 U.S. businesses in 2025**, a fragmented industry with no
firm holding more than 5% share (https://www.ibisworld.com/united-states/industry/third-party-administrators-insurance-claims-adjusters/1332/).

## 2. THE SCORED WEAKNESSES

- **Rung 2 (instrument scope), weakens criteria 1 and 7.** The candidate's own tuple names the customer as
  TPAs "handling **workers' comp**, auto, or general-liability claims for **self-insured employers** and
  small regional insurers" and cites Cal. Ins. Code § 790.035 as the governing instrument. Fetched directly:
  10 CCR § 2695.1 (the regulation implementing 790.03/790.035) states these Fair Claims Settlement Practices
  Regulations apply to claims "subject to Article 6.5 ... commencing with Section 790, **except as
  specifically provided** for: (1) **Workers' compensation insurance**; (2) ... (3) **Self insured or self
  funded plans which are bona fide ERISA plans** ... to the extent not covered by insurance; and (4) **Any
  other self funded or self insured plan**, to the extent it is not covered by insurance"
  (https://www.law.cornell.edu/regulations/california/10-CCR-2695.1). Two of the three named populations in
  the tuple, workers' comp claims, and self-insured employers generally, are **expressly carved out** of
  the cited instrument. This is not a K2 (a different, real instrument does bind them, see below) but it
  is a wrong-instrument citation covering roughly two-thirds of the named segment.

- **Rung 2 (instrument scope, second instance), weakens criterion 1.** Separately, Cal. Ins. Code Chapter
  5A ("Administrators," §§ 1759–1759.10), the chapter that actually regulates TPAs as a licensed category
  in California, defines "administrator" as "any person who collects any charge or premium from, or who
  adjusts or settles claims on, residents of this state **in connection with life or health insurance
  coverage or annuities** or coverage described in Section 740" (verbatim, fetched at
  https://california.public.law/codes/ca_ins_code_section_1759). Property/casualty lines, auto and general
  liability, the other two-thirds of the tuple, are **not mentioned**. Whether a P&C-claims TPA is bound by
  § 790.03/790.035 directly (as "any person"), or only its insurer client is, was not resolved this session
  (WebSearch budget exhausted before a market-conduct accusation naming a TPA, rather than an insurer, could
  be found). This is recorded as an **open duty-holder question**, not a kill, and not yet a score either
  way, but it is the single most important unresolved item on rung 2.

- **Rung 2 (correct instrument for workers' comp exists, but is a different checker), weakens criterion 3
  and criterion 5.** For the workers'-comp slice, the real instrument is Labor Code §§ 129, 129.5 and the
  DWC Audit & Enforcement Unit's Profile Audit Review (PAR), which "audits insurance companies, self-insured
  employers, and third-party administrators", so the customer IS bound, just not by the instrument named in
  the write-up. But this checker's frequency and grading unit both cut against the product: PAR runs "at
  least once every five years" per adjusting location (quoted directly from
  https://www.cwci.org/us_technical-issues/dwc-announces-2026-audit-standards/), and its pass/fail output is
  a single blended location-wide rating, the 2026 standard is **1.58582**, and "audit subjects with PAR
  performance ratings of 1.58582 or lower will be required to pay any unpaid compensation, but **no
  administrative penalties will be assessed**" (same source, directly fetched). A five-year-per-location
  audit cycle graded on one aggregate number, with a built-in floor beneath which errors are free, is a thin
  and slow feedback loop for a product whose whole pitch is a file-level, continuously-updating calibration
  ledger, and it functions as a RATCHET: stay under the aggregate threshold and individual file mistakes
  cost nothing.

- **Rung 3 (RATCHET), weakens criterion 5.** See above, DWC's own published performance standard is a
  free, government-set floor. A TPA whose overall error rate stays under 1.58582 owes nothing regardless of
  what any single file's compliance grade says, which is the ratchet shape METHOD.md flags: the conservative
  aggregate answer is already free, and the product's per-file severity grade only pays for itself in the
  narrow band of TPAs already failing the aggregate.

- **Rung 3 (GIVES/PUBLISHES), weakens criterion 4, NOT VERIFIED at page.** NAIC's Market Regulation Handbook
  Examination Standards Summary is a free, publicly linked PDF covering a claims examination-standards
  chapter (confirmed to exist and be free at
  https://content.naic.org/sites/default/files/publication-mes-hb-market-handbook-examination.pdf), but the
  fetch returned an unreadable compressed PDF and the actual claims-standards checklist content could not be
  read this session. Recorded as NOT-YET-VERIFIED rather than a clean pass, a free industry-standard
  checklist, if it in fact itemizes timeliness/documentation criteria at the level the candidate proposes to
  grade, would directly compete with the "self-check every file" half of the pitch.

- **Rung 4 (competitor claim), weakens criterion 4.** Origami Risk's own Regulatory Compliance Management
  page, fetched directly, lists its capabilities as "Monitor and manage regulatory obligations and
  frameworks, including ISO, NIST, SOX, and HIPAA," "Automate training, certifications, and issue
  workflows," "Evaluate your organization's compliance posture with configurable assessments", generic
  GRC task-tracking, not file-level UCSPA judgment
  (https://www.origamirisk.com/solutions/grc/compliance-management/). This corroborates the ideation's
  differentiated claim rather than weakening it. But **Verisk publishes a page literally titled "Insurance
  Claims Compliance Solutions"** (https://www.verisk.com/solutions/claims/compliance/) and its content could
  not be fetched (JS-rendered, returned only the title tag) before the search budget ran out. This is the
  single open rung-4 item most likely to matter and is recorded as **UNRESOLVED**, not cleared.

- **Rung 5c (base rate / one-sided labels), weakens criterion 5.** The product's whole value proposition is
  that it grades every closed file, not just the sampled ones a QA team or a five-year state audit would
  reach. But that means the overwhelming majority of "clearly compliant" grades the model issues are never
  externally checked at all, the only labels that come back are the rare ones a market-conduct exam or DWC
  PAR happens to cite. The calibration ledger accumulates almost entirely on the "citable" tail and gets
  almost no confirmation on the "clearly compliant" majority, the same one-sided-label problem METHOD.md
  documents for accept/decline recommenders.

- **Rung 6 (magnitude of the countable source), weakens criterion 6.** IBISWorld's 123,451-firm NAICS 52429
  figure bundles independent insurance claims adjusters together with third-party administrators; it is not
  a TPA-specific count, and it says nothing about how many of those firms are sub-300-employee TPAs or small
  regional insurers specifically. A California-specific licensed-TPA roster exists (published at
  https://www.dir.ca.gov/osip/TPARoster.pdf) but returned as an unreadable compressed PDF this session, the
  count could not be verified.

- **Rung 2 pooling / portal terms-of-use check: NOT RUN.** Whether a TPA's services agreement with its
  insurer clients, or a claims-platform vendor's terms of use, would foreclose pooling claim-file compliance
  data across customers was not checked this session (budget). This is the heaviest possible rung-2 finding
  if it exists and is flagged as the top follow-up alongside the Verisk product page.

- **Rung 1.5 (patent), weakens nothing decisively, NO on-point hit.** The closest Google Patents result,
  US20030163778A1 ("System and method for improved validation for claims compliance"), is **abandoned**
  (failure to respond to office action, 2005) and is EDI field-validation (member number, provider number,
  procedure code, date of service), not UCSPA judgment scoring
  (https://patents.google.com/patent/US20030163778). No granted claim reading on this candidate's
  differentiated claim was found.

- **Rung 1 (K1 test doesn't map cleanly onto this candidate), weakens criterion 3 slightly.** K1 asks
  whether "the customer controls the release of the money." Here the $5,000-$10,000-per-act exposure is a
  liability the TPA avoids by being compliant, not a receivable it collects, there is no counterparty
  "releasing" money and no incumbent contingency-fee floor to compare against. The magnitude test is real
  but doesn't fit the K1 shape as written; recorded honestly rather than forced into a kill or a clean pass.

- **Amnesty / free self-invocable appeal / FEE-SHIFT / COMPELLED / legislated-away checks: NOT RUN** (rung-2
  and rung-3 sub-checks not reached before the search budget was exhausted). D2 (published price for a
  worse substitute, e.g. an outsourced QA-sampling rate card): **NOT VERIFIED**, not found this session.
  Exited-predecessor search (abandoned patents beyond the one found, paused products, Wayback captures):
  **NOT RUN**.

## 3. KILL

**NO KILL.** No K1, K2, or K3 fired on quoted, fetched evidence.

- K1 does not fire: no fee-floor-vs-recovery structure exists to test it against (see above); the magnitude
  itself is verified and real.
- K2 does not fire: the cited instrument (§ 790.035) is expressly excluded for workers' comp and
  self-insured plans, but a different real instrument (Labor Code § 129.5 / DWC PAR) does bind that slice of
  the customer, so the money is not landing on an unreachable counterparty, it is landing on the right
  party under the wrong citation. The auto/GL duty-holder question is open, not resolved against the
  candidate.
- K3 does not fire: no vendor's own product page, with a named deployment and a stated outcome, was found
  making this candidate's exact claim. Origami Risk's own page affirmatively does NOT make it. Verisk's
  "Claims Compliance Solutions" page is unresolved and is the one live risk to this verdict.

## 4. D3 STATE

**FILLED, but off-band.** QBE's "Claims Compliance Analyst (Workers Compensation)" posting (Madison, WI,
$69,500–$114,500) is a real, currently-open seat whose stated duties are exactly this task. One posting
counted. QBE is a large global insurer (thousands of employees), not the sub-300-employee TPA / small
regional insurer the tuple names as the buyer, so this establishes the task has a budget line in the value
chain without confirming it at the target band. No sub-300-employee TPA or small regional insurer posting
was found or fetched this session (job-board 403s on direct fetch, per METHOD.md's known toolchain limit , 
title-level only, not independently page-verified for a smaller employer).

## 5. MUTATION

Forcing evidence exists, and it points at splitting the tuple rather than keeping it whole. The workers'
comp slice and the self-insured-employer slice run under a five-year, aggregate-rated audit (DWC PAR, Labor
Code § 129.5) with a built-in ratchet floor; the DOI-regulated small-insurer/TPA slice for auto and GL runs
(if it runs at all against the TPA specifically, which is unresolved) under § 790.03/790.035's per-act
penalty with no verified floor and a market-conduct-exam cadence that was not established this session
either way. These are two different checkers, two different frequencies, and two different penalty
mechanics wearing one tuple. The forced move is either (a) narrow to the DOI/P&C slice only and drop
workers' comp and self-insured employers from the customer definition, since the cited instrument does not
reach them, or (b) treat "workers' comp PAR compliance grading" as a separate candidate built on Labor Code
§ 129.5 rather than a sub-case of this one. I propose only; I do not mutate.

## 6. RUBRIC SCORES

No customer call has been made for this candidate, so criterion 3 is capped at 4 regardless of desk
evidence (per Part 8/Part 3's ranking rule).

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Clarity of target customer | 3 | Segment is named and sized, but the tuple bundles three sub-populations (TPA, self-insured employer, small insurer) that turn out to sit under different governing instruments, the "one customer" is really at least two |
| 2 | Clarity of JTBD | 4 | "Rate each closed file's UCSPA-compliance defensibility" is one sentence a claims QA practitioner would recognize |
| 3 | Significance and magnitude of unmet need | 3 | D1 verified and real ($5k-$10k/act, stacking); D3 filled but off-band; no salience call made |
| 4 | Differentiation and uniqueness | 3 | One direct-fetch competitor clearance (Origami: generic GRC, not file-level UCSPA judgment); one unresolved live risk (Verisk's own "Claims Compliance Solutions" page); no on-point patent |
| 5 | Performance improvement over existing solutions | 2 | No measured number; RATCHET (DWC's free aggregate floor) and the 5c one-sided-label problem both cut against a compounding story on the workers'-comp slice specifically |
| 6 | Size of market opportunity | 3 | 123,451-firm NAICS count is countable but bundles independent adjusters with TPAs and does not isolate the sub-300-employee band |
| 7 | Market / technical / execution risk | 2 | Two of the tuple's three named populations sit outside the cited instrument's scope; the auto/GL TPA duty-holder question is unresolved; the workers'-comp checker's 5-year cycle and blended rating are a slow, coarse feedback loop for the asset's cold start |

**Lowest criterion: 2 (tied, criteria 5 and 7). Sum: 20.**

## 7. VERIFIED / NOT VERIFIED

**VERIFIED (fetched and read directly):**
- Cal. Ins. Code § 790.035 penalty language and 10 CCR § 2695.1's workers'-comp/self-insured exclusion , 
  https://www.law.cornell.edu/regulations/california/10-CCR-2695.1
- Cal. Ins. Code § 1759 "administrator" definition (life/health/annuities only) , 
  https://california.public.law/codes/ca_ins_code_section_1759
- DWC PAR frequency, 2026 standard (1.58582), and no-penalty-below-standard language , 
  https://www.cwci.org/us_technical-issues/dwc-announces-2026-audit-standards/
- Origami Risk's Regulatory Compliance Management page content , 
  https://www.origamirisk.com/solutions/grc/compliance-management/
- US20030163778A1 patent status (abandoned) and claim scope , 
  https://patents.google.com/patent/US20030163778
- IBISWorld NAICS 52429 firm count (123,451) , 
  https://www.ibisworld.com/united-states/industry/third-party-administrators-insurance-claims-adjusters/1332/

**NOT VERIFIED (search-engine summary only, fetch failed, or not independently confirmed):**
- QBE Claims Compliance Analyst duties/salary, ATS page itself did not render for the fetcher
  (https://qbe.wd3.myworkdayjobs.com/qbe-careers/job/madison-wi-usa/claims-compliance-analyst--workers-compensation-_356023/apply);
  duties corroborated only via aggregator mirror (https://www.complyapply.com/jobs/537576387-claims-compliance-analyst-workers-compensation-at-qbe)
- DWC Audit Unit CY2024 figures (4,531 violations, $1,347,527 in penalties), search-engine summary only,
  source PDF (https://www.dir.ca.gov/dwc/AuditUnit/Audit-Annual-Report2024.pdf) returned unreadable
  compressed content
- Insurer strict liability for TPA UCSPA violations, search-engine summary only; direct source
  (apps.americanbar.org) unreachable (DNS failure)
- NAIC Market Regulation Handbook claims-standards checklist content, page confirmed to exist and be free,
  content unreadable (https://content.naic.org/sites/default/files/publication-mes-hb-market-handbook-examination.pdf)
- California DIR licensed-TPA roster count, page exists, content unreadable
  (https://www.dir.ca.gov/osip/TPARoster.pdf)
- Verisk "Insurance Claims Compliance Solutions" product claim, page confirmed to exist, content did not
  render (https://www.verisk.com/solutions/claims/compliance/), **unresolved, top follow-up**
- EvolutionIQ, Five Sigma, FurtherAI claims-adjacent AI vendors, searched, no page found making this
  candidate's specific file-level UCSPA judgment claim, but not all product pages were exhaustively fetched
