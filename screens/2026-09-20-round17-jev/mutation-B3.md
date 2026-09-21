# Mutation test: Candidate 3, "Claims File Compliance Severity Grading" (screen-B3.md)

Fresh mutation agent, round 17. No new fetches performed this session, every quote below is inherited from
screen-B3.md's own already-fetched citations (same URLs), re-applied against M1/M4/M5b/M6. Where the screen
itself marked something NOT VERIFIED, it stays NOT VERIFIED here; nothing has been upgraded.

## 1. ANSWER

**SPLIT. One resulting formulation is MUTATION; the other is NONE (fails M4, rejected at this stage rather
than forwarded).**

The screen's own rung-2 finding, that the cited instrument expressly excludes two of the tuple's three
named populations, is real forcing evidence and does split the tuple. But testing the screener's two
proposed splits separately against M4 shows they are not symmetric: narrowing to the DOI/P&C slice escapes
the candidate's heaviest documented weakness; isolating the workers'-comp slice walks directly into it.
Only the first is a mutation worth writing to `predictions/`.

## 2. WHAT CHANGED, ELEMENT BY ELEMENT

**Original tuple (ideation-B.md lines 129-139):** Customer, TPAs handling workers' comp, auto, or GL
claims for self-insured employers and small regional insurers, sub-300 employees. Asset, ledger scoring
each closed file's UCSPA compliance posture, correlated against market-conduct exam/DOI complaint outcomes.
Document set, claim file timeline/correspondence log. Mistake, a claim handled outside UCSPA standard
that partial QA sampling missed. Checker, state DOI market-conduct examiner (§ 790.035) **and** the
self-insured client auditing the TPA's contractual SLA compliance.

**Formulation (a), DOI/P&C-only:**
- Customer: TPAs handling **auto or GL claims for small regional (insured, non-self-insured) insurers only**,
  sub-300 employees. Workers' comp and self-insured employers are dropped from scope. (Entity type, TPA , 
  is unchanged; only the served line-of-business and payer-type are narrowed.)
- Asset: same ledger shape, correlated only against DOI market-conduct exam findings/complaint dispositions
  for auto/GL lines.
- Document set: unchanged.
- Mistake: unchanged in shape, scoped to auto/GL files.
- Checker: state DOI market-conduct examiner applying § 790.035 / 10 CCR § 2695.1 **only**, the
  self-insured-client SLA-audit checker is dropped along with that customer slice.

**Formulation (b), workers'-comp PAR-only:**
- Customer: TPAs (or, per DWC's own audited-entity list, the insurer/self-insured employer directly)
  handling workers' comp claims in California, sub-300 employees.
- Asset: ledger correlated against DWC Audit & Enforcement Unit Profile Audit Review (PAR) ratings instead
  of DOI market-conduct citations.
- Document set: unchanged in shape.
- Mistake: reframed as a claim contributing to a location's blended PAR rating, not a discrete per-act
  citation.
- Checker: DWC Audit & Enforcement Unit, Labor Code §§ 129/129.5, PAR methodology, once per five years per
  adjusting location, one blended aggregate rating, 2026 standard 1.58582, no penalty below standard.

Both formulations change **Checker** (a defining tuple element) and narrow **Customer** without changing the
payer's entity type, so both clear the low bar of "not merely positioning", the question is whether either
also clears M4.

## 3. M1, FORCING EVIDENCE, QUOTED, AND WHEN IT ARRIVED

Arrived this screen (round 17), fetched directly, not in the original ideation write-up: 10 CCR § 2695.1,
implementing Cal. Ins. Code §§ 790.03/790.035, states the Fair Claims Settlement Practices Regulations apply
"except as specifically provided" for **"(1) Workers' compensation insurance; ... (3) Self insured or self
funded plans which are bona fide ERISA plans ... to the extent not covered by insurance; and (4) Any other
self funded or self insured plan, to the extent it is not covered by insurance"**
(https://www.law.cornell.edu/regulations/california/10-CCR-2695.1). The original tuple cited § 790.035 as
the governing instrument for all three named populations (workers' comp, auto, GL, for both self-insured
employers and small insurers); this text shows two of the three are carved out outright. That is the forcing
fact, not the verdict, not a re-reading of the same citation, a different provision the ideation write-up
never engaged.

The second piece, also fetched this screen, is what makes the two resulting halves un-symmetric rather than
interchangeable: DWC's own published 2026 PAR standard, **"1.58582,"** with **"audit subjects with PAR
performance ratings of 1.58582 or lower will be required to pay any unpaid compensation, but no
administrative penalties will be assessed"**, on a cycle of **"at least once every five years"** per
adjusting location (https://www.cwci.org/us_technical-issues/dwc-announces-2026-audit-standards/). This is
what forces (b), specifically, into the ratchet, it is not present at all in the § 790.035 per-act penalty
structure that governs (a).

## 4. M4, THE ORIGINAL HEAVIEST WEAKNESS, AND WHETHER EACH FORMULATION ESCAPES IT

The screen's rubric ties criteria 5 and 7 at 2 (lowest, sum 20). Their stated content:

- **Criterion 5:** "No measured number; RATCHET (DWC's free aggregate floor) and the 5c one-sided-label
  problem both cut against a compounding story **on the workers'-comp slice specifically**."
- **Criterion 7:** "Two of the tuple's three named populations sit outside the cited instrument's scope; the
  auto/GL TPA duty-holder question is unresolved; **the workers'-comp checker's 5-year cycle and blended
  rating** are a slow, coarse feedback loop for the asset's cold start."

Both criteria's stated weaknesses point at the same place: the workers'-comp/DWC-PAR checker specifically,
plus the instrument-scope confusion caused by bundling three populations under one wrong citation.

**Formulation (a) escapes both cleanly on the parts that were forced by the wrong-instrument bundling.**
Dropping workers' comp removes DWC PAR, and therefore RATCHET, from the candidate entirely; it is simply
not the checker anymore. Dropping self-insured employers and workers' comp removes two of the three
exclusions in § 2695.1's list, leaving a sole named population (auto/GL claims for insured, non-self-insured
small regional insurers) that is **not** among the four excluded categories in the quoted text, the
remaining population is squarely inside the cited instrument's coverage instead of two-thirds outside it.
What (a) does **not** escape: the auto/GL "any person" duty-holder question (whether a P&C-claims TPA is
bound by § 790.03/790.035 directly, or only its insurer principal) stays open, it is narrower now (one
open question instead of a mis-cited instrument plus an open question) but not resolved. And 5c's one-sided
base-rate problem (external confirmation only arrives on the citable tail) is structural to any
market-conduct-exam checker and persists regardless of formulation. Net: (a) escapes the ratchet and the
wrong-instrument scope problem, leaves the duty-holder ambiguity and the base-rate problem on the sheet , 
consistent with M4's bar of escaping *the* named weakness, not every weakness.

**Formulation (b) fails M4.** It does resolve the duty-holder question, DWC's own PAR literature "audits
insurance companies, self-insured employers, and third-party administrators" by name, so standing to be
graded is no longer ambiguous for this slice. But the RATCHET is not diluted by isolating this slice, it is
concentrated: in the original bundled tuple, DWC PAR governed at most one of three named populations; in
(b) it is the *entire* checker. A five-year-per-location cycle graded on one blended number, with a
published floor beneath which individual mistakes cost nothing, is the weakness the screen already flagged
as the worst thing about the workers'-comp slice, building the whole candidate on exactly that slice does
not reformulate around the weakness, it walks into it at full strength. It also reproduces the frequency
problem METHOD.md Part 1 already names by rule (C-70): "a checker who grades once a decade cannot support a
learning loop however expensive the verdict", five years is the same shape of problem, not a technicality.
A mutation that trades an *unresolved* weakness (duty-holder) for a *confirmed, quantified* one (the
1.58582 floor, at full concentration) is not an escape.

## 5. M6, STAGE 0 RE-ANSWERED FOR EACH FORMULATION

**(a) DOI/P&C-only.** Customer segment: nameable, TPAs handling auto/GL claims for small regional
(insured) insurers, sub-300 employees. Band: unchanged, sub-300 employees. Countable source: no better than
before, the only figure on the board, IBISWorld's NAICS 52429 (123,451 U.S. businesses,
https://www.ibisworld.com/united-states/industry/third-party-administrators-insurance-claims-adjusters/1332/),
already bundled independent adjusters with TPAs and was never line-of-business-specific; narrowing to
auto/GL-only makes it looser, not tighter, though this was already a scored rung-6 weakness, not a stage-0
failure. Room gate: unaffected, still a software ledger a TPA runs on its own files, not a services
engagement; no funding/revenue/IP caps implicated. **Passes stage 0**, with the market-size weakness carried
forward unresolved (same status as before, not worse in kind).

**(b) Workers'-comp PAR-only.** Customer segment: nameable, workers'-comp TPAs (or directly-audited
insurers/self-insured employers) in California, sub-300 employees. Band: unchanged. Countable source: same
absence, no workers'-comp-specific TPA count was found or verified this session either. Room gate:
formally unaffected (still a product, not a service). **Passes stage 0 on paper**, but a stage-0 pass does
not rescue a formulation that already fails M4, the room gate tests eligibility, not whether the checker
can fund a learning loop, so this pass carries no weight against the finding above.

## 6. WHICH FORMULATION THE EVIDENCE FAVOURS AT RUNG 1

**(a), the DOI/P&C-only formulation.** It is a genuine, forced mutation: the customer narrows, the checker
narrows, and both changes are traceable to a specific fetched exclusion the original write-up never engaged,
not to the verdict. It should be written to `predictions/` (M3) and sent to a blind rung-1 re-screen. Its
open items for that re-screen: independently resolve the auto/GL "any person" duty-holder question (not
resolved this session, search budget was exhausted first), and look for a TPA-specific or auto/GL-specific
countable source rather than the bundled NAICS 52429 figure.

**(b) should not be forwarded.** It resolves standing but concentrates the candidate's worst documented
weakness (the DWC PAR ratchet and five-year cycle) into 100% of the checker instead of roughly a third of a
bundled one. Recording it here, tested and rejected at the mutation stage, is the M4-mandated outcome, not
a rescue attempt, and not an invitation to try a third framing of the same workers'-comp slice.

## 7. VERIFIED / NOT VERIFIED

All items below are carried over unchanged from screen-B3.md's own record, no new fetches were made this
session, per the mutation brief's scope (this repo only, no subagents).

**VERIFIED (fetched and read directly, per screen-B3.md):**
- 10 CCR § 2695.1 exclusion text (workers' comp; self-insured/self-funded plans) , 
  https://www.law.cornell.edu/regulations/california/10-CCR-2695.1
- DWC PAR frequency ("at least once every five years"), 2026 standard (1.58582), no-penalty-below-standard
  language, https://www.cwci.org/us_technical-issues/dwc-announces-2026-audit-standards/
- Cal. Ins. Code § 1759 "administrator" definition (life/health/annuities only, not property/casualty) , 
  https://california.public.law/codes/ca_ins_code_section_1759

**NOT VERIFIED (unresolved before this mutation test and still unresolved, not addressed this session):**
- Whether a P&C-claims TPA is bound by § 790.03/790.035 directly as "any person," or only its insurer
  client is, the single open item that would most affect formulation (a)'s duty-holder standing.
- Any TPA-specific or auto/GL-specific countable population size (California licensed-TPA roster at
  https://www.dir.ca.gov/osip/TPARoster.pdf returned unreadable in the screen; not re-attempted here).
- Verisk's "Insurance Claims Compliance Solutions" competitor claim (https://www.verisk.com/solutions/claims/compliance/)
 , still unresolved from the screen, applies to both formulations equally since neither changes the
  competitive-differentiation question.
