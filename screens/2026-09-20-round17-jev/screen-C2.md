# Blind screen: Candidate 2 - Prescription-Entry Look-Alike/Sound-Alike Check

Independent community pharmacies (<300 staff). Asset: private ledger of {technician entry -> source
e-prescription -> pharmacist-verification outcome}. Checker: state Board of Pharmacy + PBM claims audit.

---

## 1. THE CASE FOR

The strongest demand tier reached is **D1, VERIFIED**, carried over from ideation and not re-fetched
(quotes read correctly): California Business & Professions Code section 125.9 caps board fines at
**"five thousand dollars ($5,000) for each inspection or each investigation"**
([FindLaw](https://codes.findlaw.com/ca/business-and-professions-code/bpc-sect-125-9/)), the ceiling 16
CCR section 1775.1 applies to pharmacy citations
([Cornell LII](https://www.law.cornell.edu/regulations/california/16-CCR-1775.1), confirmed this session:
**"The fine for violating the Pharmacy Law or regulati[ons] shall not exceed the amount specified in
Section 125.9"**). Frequency context is VERIFIED: NCPA's 2024 Digest puts average annual volume at
**"59,644 [prescriptions] per store"**
([NCPA](https://ncpa.org/newsroom/news-releases/2024/10/27/ncpa-releases-2024-digest-report)).

The strongest rung-2 pass, newly confirmed this session: **16 CCR section 1775 does bind the customer as
"person or entity,"** not merely the individual pharmacist license, and the instrument ships its own free,
self-invocable remedy - a citation may be contested by informal office conference, no fee found:
**"Within 14 calendar days after service of a citation, the person or entity cited may submit a written
request for an informal office conference"** ([Cornell LII, 16 CCR
1775.4](https://www.law.cornell.edu/regulations/california/16-CCR-1775.4)). This is a rung-2 SCORE
(free appeal shape), not a kill, but it is real and cheap for the customer to invoke on their own,
independent of anything this product would sell.

Best available D3 signal (title-level, not customer-verified - see D3 STATE below): "Data Entry Pharmacy
Technician" is a real, populated job title nationally, average **"$40,220 a year... approximately $19.34
an hour"** per ZipRecruiter
([ZipRecruiter](https://www.ziprecruiter.com/Salaries/Data-Entry-Pharmacy-Technician-Salary)), confirming
a funded seat exists for the task the mistake occurs inside - but not for the checking task itself, which
is the pharmacist's existing, already-funded verification duty (see D3 STATE).

---

## 2. THE SCORED WEAKNESSES

- **Rung 1 / D1 magnitude - criterion 3.** The $5,000 CA ceiling is a per-inspection/investigation cap,
  not a per-error charge, and inspections are infrequent relative to 59,644 scripts/year; the Pennsylvania
  analog for adjacent documentation/dispensing violations is **"$100"** per event (49 Pa. Code section
  43b.7, already quoted in ideation) - two orders of magnitude below the CA headline. NOT VERIFIED: how
  often ANY single independent pharmacy is actually cited (frequency of the triggering event itself, as
  opposed to script volume). Weakens **criterion 3**.

- **Rung 1.5 patent - criterion 4.** Google Patents surfaced **US12488870B2, "Systems and methods for
  automatically predicting incorrect drug dispensed events in a pharmacy,"** assignee **Walmart Apollo,
  LLC**, filed 2023-01-31, published 2025-12-02
  ([Google Patents](https://patents.google.com/patent/US12488870)). Its own claim language: LASA pair
  identification is **"based on a 1-year time period of reported events data... including both actual
  events and near miss events,"** using Bi-Sim/soft-Bisim and Editex similarity - i.e., a historical,
  event-data-driven LASA model, close in shape to this candidate's asset. It predicts incorrect-dispensed
  events generally rather than explicitly comparing a technician's keystroke-level entry against the
  source e-prescription text, and it is Walmart's internal system, not a product licensed to independent
  pharmacies running PioneerRx/QS1/BestRx - so this is a **capability an incumbent already holds, not yet
  a distribution threat to this segment**, per Part 3's capability-vs-distribution split. Carried forward
  as a finding, not a kill (rung 1.5 never kills). Weakens **criterion 4**.

- **Rung 2 - PBM pooling clause still NOT VERIFIED - criteria 4 and 5.** This session searched CVS
  Caremark's provider manual; the only confidentiality language found governs the manual and portal
  content itself (**"providers may not disclose, sell, assign, transfer, or give information contained in
  the manual to any third party"**) and audit-record production duties, not the pharmacy's own pre-claim
  internal tech-entry/verification data the ideation file's asset is built from
  ([PAAS
  National](https://paasnational.com/notable-updates-from-the-2026-caremark-provider-manual/); manual PDF
  at [caremark.com](https://www.caremark.com/content/dam/enterprise/caremark/pdfs/pharmacists-and-medical-professionals/2026_caremark_provider_manual.pdf)).
  This is consistent with the ideation file's own flag but does not resolve it - the actual dispensing
  software vendor's (PioneerRx/QS1/BestRx/Liberty) end-user license terms, which would govern whether the
  pharmacy may extract and pool its own verification-screen correction logs, were not located this session.
  **Still an open flag, NOT VERIFIED either way**, per the ideation file's own honest flag.

- **Rung 3 - PUBLISHES shape fires, ALL SCORE, weakens criterion 4.** The Institute for Safe Medication
  Practices publishes a free, nationally maintained **"List of Confused Drug Names"** with tall-man
  lettering recommendations ([ISMP PDF via
  ECRI](https://online.ecri.org/hubfs/ISMP/Resources/ISMP_ConfusedDrugNames.pdf)), and multiple pharmacy
  management systems already ship generic LASA alerting built on lists of this kind - Liberty Software's
  own product page states plainly: **"Look alike, sound alike alerts and check points, black box warnings,
  morphine equivalent dosing alerts, 5-point checks and other innovative check points"**
  ([libertysoftware.com](https://libertysoftware.com/pharmacy/)) - though it does not say whether this is
  the pharmacy's own historical data or the generic national list (residue: the customer already has a
  national-drug-pair alert for free; what remains unaddressed is entry-vs-source, pharmacy-specific
  deviation *scoring*).

- **Rung 4 - the heaviest single weakness on this candidate, criteria 2 and 4.** A funded competitor,
  **PillPilot** (founded 2025, New York;
  [PitchBook profile](https://pitchbook.com/profiles/company/1167931-63)), sells directly into this exact
  customer list and PMS surface. Its own product page states: **"fills the Data Entry screen the way your
  best tech would. Every field is checked a second time after it lands,"** and it lists integration with
  **"PioneerRx, PrimeRx, EnterpriseRx, BestRx, Liberty, QS/1, ComputerRx"** - the identical PMS roster
  named in the ideation file's own outcome-observation section
  ([pillpilot.com](https://www.pillpilot.com/)). This is NOT a K3 CANDIDATE - the vendor's own page does
  not use LASA/DUR vocabulary, does not claim to score deviation using a pharmacy's own historical
  catch/miss pattern, names no specific pharmacy customer (only anonymous quotes - **"The queue cleared
  itself by lunch in the first week"** and **"I can show the state board exactly what happened on every
  script"** - both unattributed, on the vendor's own site, so G2 and G3 both fail). But it is a real,
  funded, segment-matched, PMS-matched competitor doing an adjacent version of the same check, which
  narrows this candidate's differentiated claim to a thin technical distinction (score-the-deviation vs.
  double-check-the-field) that a customer conversation, not a desk search, would have to defend. Weakens
  **criteria 2 (JTBD clarity narrows) and 4 (differentiation)**.

- **Rung 4 - AI-assisted LASA vendors exist but sell to hospital/health-system pharmacy, not this
  segment.** MedAware's own press material: partnership described as **"Ballad Health's acute care
  pharmacy team is the first to natively utilize MedAware within an Epic pharmacy workflow"**
  ([PR Newswire](https://www.prnewswire.com/news-releases/medaware-partners-with-ballad-healths-pharmacy-team-to-bring-personalized-medication-risk-monitoring-to-rural-healthcare-302292638.html)) -
  Epic is a hospital/health-system EHR, not an independent-pharmacy PMS, so this is a segment mismatch, not
  a G2 hit for this candidate's customer. AESOP Technology's press release makes LASA-detection claims but
  names no customer segment, no deployment, and no outcome beyond a cited research study
  ([PR
  Newswire](https://www.prnewswire.com/news-releases/a-safer-tomorrow-aesop-technologys-battle-against-look-alike-sound-alike-medication-errors-301964307.html)) -
  recorded as NOT VERIFIED / insufficient for G1-G3. Neither reaches K3-candidate strength for this
  segment; both are recorded as rung-4 color, not competitors that solve the mistake here.

- **Rung 5c - base-rate / label-for-both-answers, criterion 5.** The candidate's own outcome observation
  (pharmacist catches-and-corrects, or doesn't) does produce a label on both branches inside one
  pharmacy's own workflow, unlike a decline-only recommender - this is a genuine strength, not a
  weakness, but it was NOT explicitly analyzed in the ideation file and is recorded here as a scored point
  rather than assumed. No adverse finding.

- **0c-ii, funded seat that already does this - criterion 5.** The checking task this product assists is
  not empty of a funded seat: it is the pharmacist's own, already-licensed, already-paid verification duty
  (state law already requires a pharmacist to verify every entry before dispensing). This candidate does
  not create a new checker; it augments an existing, legally mandatory one. That is compatible with the
  ladder (0c-ii asks whether a funded seat makes the WHOLE task redundant, not whether one exists at all),
  but it means the product's "AI decides" framing (Part 1, Stage 6) is thinner than candidates where no
  human currently does this at all - **weakens criterion 5** (compounding-moat/AI-native story is an
  assistance layer on a mandatory human check, not a new decision).

---

## 3. KILL

**NO KILL.** K1 does not fire - the customer (the pharmacy, "person or entity cited") controls nothing
about release of the fine, but the money is real and named in the instrument; this is a magnitude
weakness (criterion 3), not a K1, because no fee floor exceeding the disputed amount was found. K2 does
not fire - 16 CCR 1775/1775.1 names **"the person or entity cited,"** which reads as binding the pharmacy
itself, not a counterparty. K3 CANDIDATE does not fire - PillPilot is the closest competitor found and
fails G2 (no named deployment) and G3 (no independent-source outcome); Walmart's patent (rung 1.5) never
kills by rule; MedAware and AESOP are segment mismatches (hospital/health-system, not independent
pharmacy PMS). K4 is untested - no call was made this session (screening is desk-only per the brief).

---

## 4. D3 STATE

**Two D3s must be recorded separately here, and the ideation file did not distinguish them:**

- **For the mistake's site (data entry): FILLED AT THE CUSTOMER.** "Data Entry Pharmacy Technician" is a
  real, nationally populated job title, average **"$40,220 a year"**
  ([ZipRecruiter](https://www.ziprecruiter.com/Salaries/Data-Entry-Pharmacy-Technician-Salary)) - band
  read at the title level, NOT VERIFIED at a specific independent-pharmacy posting (every major job board
  403s on fetch, per METHOD's own toolchain note; this is a tooling limit, not a finding about the world).
- **For the check this product performs (verification): FILLED AT THE CUSTOMER, and it is a licensed,
  materially higher-paid seat** - the pharmacist's own verification duty, which state pharmacy practice
  acts already require and which this candidate's own outcome-observation section relies on
  ("the pharmacist's own verification step... does the pharmacist catch and correct the tech's entry
  before dispensing"). This is the state the ladder does not have a clean name for: not EMPTY, not
  FILLED-TASK-ABSENT (the task is squarely in the pharmacist's duties), and not INCENTIVE-INVERTED. It is
  closest to FILLED AT THE CUSTOMER - the good-news state - but for a *different, more expensive* seat
  than the one where the mistake occurs, which is why 0c-ii is recorded as a scored weakness above rather
  than a clean pass.

---

## 5. MUTATION

**NONE.** No evidence gathered this session forces a different formulation. The PillPilot finding
narrows the differentiated claim (score deviation using the pharmacy's own historical catch/miss pattern,
vs. PillPilot's generic "check the field again") but does not force a pivot to a different customer,
asset, or mistake - it is a competitive pressure to sharpen the claim in the pitch, not new evidence that
the tuple is wrong. The Walmart patent similarly narrows the claim's novelty without changing the
customer or the asset. No principled mutation exists on the evidence gathered here.

---

## 6. RUBRIC SCORES

Criteria (Part 8's table, restated from STATE.md's THE ROOM, the seven bullets under the published
rubric): (1) Clarity of target customer, (2) Clarity of JTBD, (3) Significance and magnitude of unmet
need, (4) Differentiation and uniqueness, (5) Performance improvement over existing solutions, (6) Size
of market opportunity, (7) Market/technical/execution risk. VERIFIED evidence only; no call was made, so
criterion 3 is capped at 4 regardless (it does not reach the cap here on its own evidence).

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Clarity of target customer | 4 | Independent pharmacies <300 staff is specific and verifiable (NCPA counts them at 18,984) |
| 2 | Clarity of JTBD | 3 | Clear on its face, narrowed by PillPilot selling an adjacent "check the entry again" job into the identical PMS list |
| 3 | Significance and magnitude of unmet need | 2 | D1 is VERIFIED but small and capped (CA $5,000 ceiling, PA analog $100) and NOT VERIFIED at real per-pharmacy citation frequency |
| 4 | Differentiation and uniqueness | 2 | PillPilot (funded, segment- and PMS-matched) plus a Walmart Apollo patent on historically-driven LASA prediction both narrow the claim; neither is a K3 CANDIDATE, but both are real weaknesses |
| 5 | Performance improvement over existing solutions | 3 | Passes 5c cleanly (labels both branches); undercut by augmenting an already-mandatory, already-funded pharmacist check rather than replacing an absent one |
| 6 | Size of market opportunity | 3 | 18,984 independent pharmacies, $94.9B independent-pharmacy market (NCPA), but per-customer annual dollar tied to a capped, infrequent citation event |
| 7 | Market, technical and execution risk | 3 | Subscription-into-existing-PMS model avoids the services-delivery trap (rule 1), but faces a funded direct competitor already inside the same PMS integrations |

**Lowest criterion: 2 (tied, criteria 3 and 4). Sum: 20.**

---

## 7. VERIFIED / NOT VERIFIED

**VERIFIED (fetched and read this session):**
- [Cal. Bus. & Prof. Code section 4314, FindLaw](https://codes.findlaw.com/ca/business-and-professions-code/bpc-sect-4314/) - citation authority text
- [16 CCR section 1775.1, Cornell LII](https://www.law.cornell.edu/regulations/california/16-CCR-1775.1) - fine ceiling tied to section 125.9
- [16 CCR section 1775.4, Cornell LII](https://www.law.cornell.edu/regulations/california/16-CCR-1775.4) - free 14-day informal-conference appeal right
- [US12488870B2, Google Patents](https://patents.google.com/patent/US12488870) - Walmart Apollo LLC LASA/historical-event patent, claim language quoted
- [Liberty Software product page](https://libertysoftware.com/pharmacy/) - generic LASA alert claim quoted
- [PillPilot product page](https://www.pillpilot.com/) - claim, PMS integration list, and anonymous testimonials quoted
- [NCPA 2024 Digest coverage, ncpa.org](https://ncpa.org/newsroom/news-releases/2024/10/27/ncpa-releases-2024-digest-report) - 59,644 scripts/store/year (re-confirmed, established fact)
- [NCPA independent pharmacy count coverage](https://ncpa.org/newsroom/news-releases/2024/10/27/ncpa-releases-2024-digest-report) - 18,984 independent pharmacies, $94.9B market
- [MedAware / Ballad Health press release, PR Newswire](https://www.prnewswire.com/news-releases/medaware-partners-with-ballad-healths-pharmacy-team-to-bring-personalized-medication-risk-monitoring-to-rural-healthcare-302292638.html) - Epic/acute-care segment, confirming segment mismatch
- [AESOP Technology press release, PR Newswire](https://www.prnewswire.com/news-releases/a-safer-tomorrow-aesop-technologys-battle-against-look-alike-sound-alike-medication-errors-301964307.html) - claim present, no segment/deployment/outcome
- [ZipRecruiter, Data Entry Pharmacy Technician Salary](https://www.ziprecruiter.com/Salaries/Data-Entry-Pharmacy-Technician-Salary) - title-level national comp band
- [ISMP List of Confused Drug Names, via ECRI](https://online.ecri.org/hubfs/ISMP/Resources/ISMP_ConfusedDrugNames.pdf) - free national LASA list, PUBLISHES shape
- [PillPilot, PitchBook profile](https://pitchbook.com/profiles/company/1167931-63) - founded 2025, real funded entity

**Carried over from ideation-C.md as established, not re-fetched (quotes read correctly on inspection):**
- Cal. Bus. & Prof. Code section 125.9 ($5,000 cap language)
- 49 Pa. Code section 43b.7 ($100 fine)

**NOT VERIFIED (searched, not found or inconclusive):**
- Whether PBM provider-manual confidentiality clauses (CVS Caremark checked; OptumRx not reached) extend to
  a pharmacy's own pre-claim internal verification-screen data, as opposed to claims/audit data - the
  specific gap the ideation file itself flagged
- Whether the pharmacy dispensing-software vendors' (PioneerRx/QS1/BestRx/Liberty) own end-user terms of
  use restrict pooling of verification-screen correction logs
- Real per-independent-pharmacy frequency of board citations for this specific violation type (only
  aggregate script volume is verified)
- A named, independent-pharmacy-segment customer deployment for PillPilot or any AI-LASA vendor, with a
  stated outcome in words other than the vendor's own (searched; none found)
- Any exited/paused predecessor specific to this exact mechanism (searched; none found - PrescribeIT's
  2026 shutdown is a Canadian e-prescribing network fee dispute, unrelated to this candidate, and is not
  cited above as relevant)
