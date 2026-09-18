# K1. MSHA citation prediction for small surface aggregates operators (10-99). Blind screen return, 2026-09-08.

Budget: 21 searches, 18 fetch attempts (8 failed), plus curl reads of MSHA open-data files.

## THE CASE FOR
- **D1, a published price for the mistake plus the regulator's own outcome ledger.** 30 CFR 100.3 (amended 2025-01-10): "the operator of any mine in which a violation occurs... shall be assessed a civil penalty of not more than $90,649"; Table 14 runs "60 or fewer [points] $168", 100 points $4,152, 140+ $90,649. MSHA's Violations dataset (2026-09-04) at the 1,757 target mines: CY2024 10,335 citations at 1,471 of 1,757 mines (84%); CY2025 9,515 at 1,453.
- **K2 clean.** 30 U.S.C. 813(a): "of each surface coal or other mine in its entirety at least two times a year" and "no advance notice of an inspection shall be provided". 56.18002(a): "A competent person designated by the operator shall examine each working place at least once each shift"; (b) a record "shall be made before the end of the shift"; (d) retained one year. Unlike the dead machine-safety candidate, the written record is mandatory. No amnesty in Part 100; no pooling foreclosure.
- **1,757 active surface sand-and-gravel and stone mines with 10-99 employees, under 70 field offices** (MSHA Mines dataset).

## SCORED WEAKNESSES
- **Rung 1 (criteria 3, 6):** at the target mines the **median proposed penalty per citation is $147 (2024) / $151 (2025); p90 $861/$883. Per cited mine per year: median $882, p75 $2,132, p90 $6,822; median 4 citations.** Whole-segment proposed penalties: $6.02M (2024), $4.61M (2025). Abatement and withdrawal-order costs NOT VERIFIED.
- **Rung 1.5:** no granted claim on predicting MSHA citations (two searches). Clean.
- **Rung 2 (criterion 4):** free appeal: 100.6 "10 days within which to... request a safety and health conference with the District Manager"; 100.3(f) "a 10% reduction... where the operator abates the violation within the time set". Legislated-away: 2025 DOGE office closures reversed (search-level).
- **Rung 2.5 (criterion 3):** D2 NOT FOUND (J.J. Keller, G2, Catamount sell mock inspections, no price). D3 below. Clears only on D1 plus D4, with D1 at $882 per mine-year.
- **Rung 3 (criteria 4, 5):** GIVES: MSHA EFSMS "works closely with MSHA District enforcement offices to... help mine operators develop or revise training, safety and health programs"; Safety Pro in a Box, MSHA Academy with NSSGA, free checklists; Ogletree Deakins' free MSHA Citation Tracker (Pit & Quarry, 2024-05-28). PUBLISHES: every citation by mine ID, and the top-20 most-cited list. **RATCHET fires hard: the 2024 top-5 for this exact segment (56.14107(a) 678, 56.12004 610, 56.20003(a) 608, 56.14100(b) 548, 56.12032 344) is MSHA's published national most-cited list in the same order.** The conservative ranking is already free; the only paid output is "skip these under your office," which no operator may lawfully act on. CAPTURES: GoCanvas "Small Mines: Workplace Examination – Quarry/Pit" form, SafetyCulture templates. Residue: per-field-office deviation from the national list, NOT VERIFIED to exist.
- **Rung 4 (criterion 4):** Predictive Compliance (E&MJ, August 2010, via Wayback): "calculates the predicted penalty", "identify citation writing tendencies among different inspectors", "important decisions in the days leading up to a MSHA inspection"; Newmont cut "housekeeping citations from about six per inspection down to one"; 25 subscribers. Live site is a JS shell; deployments Newmont and Freeport, not small aggregates. G1 partial, G2 absent for the segment: SCORE. Buyer's guides exist.
- **Rung 5 (criterion 5):** 5a yes. 5b itemised (PART_SECTION, SIG_SUB, NEGLIGENCE, LIKELIHOOD, PROPOSED_PENALTY). **But neither the Violations nor the Inspections dataset carries an inspector identifier; only INSPECT_OFFICE_CD.** 5c: the "fixed on our say-so, not cited" branch is confounded.
- **Rung 6 (criterion 6):** 1,757 mines (not firms). At $882 median exposure, price must sit under roughly $50/month. Census SUSB NOT VERIFIED.

## KILL: NO KILL.

## D3 STATE: UNRUN at 10-99. CRH subsidiary postings (Helena Sand & Gravel safety coordinator; Callanan quarry manager $100,000-120,000, snippets) are FILLED AT THE CUSTOMER at the 100+ band.

## MUTATION (M0): (1) no inspector ID in public data, so the asset reformulates to field office; (2) the segment's cited-standard ranking equals the free national list, so the claim shrinks to per-office deviation, unverified. Neither rescues criteria 3 and 6: the $147 median citation is the fact. No principled mutation exists inside this segment.

## ADJACENCY: Nursing home survey readiness (same shape; CMS median fine $15,593 vs $147 here; rung-4 pattern transfers). OSHA citation contest (killed on magnitude; transfers directly). Machine safety (killed for no written record; does NOT transfer). EPA ECHO (amnesty does not transfer; free-program shape partially). Oil & gas (regulator gives away the record; transfers).

## PRACTITIONER QUESTIONS
1. When were you last cited, on what standard, and what did it cost including abatement and downtime?
2. Before an inspection, does anyone look at MSHA's most-cited list or your MDRS history? Who?
3. Do you know your field office's inspectors by name and what they tend to write?
4. Have you ever paid a consultant, law firm or software vendor for anything MSHA-related? How much?
5. What happens to your workplace exam records besides sitting for a year?
6. Have you had a 104(d) or 107(a) order, and what did the stoppage cost?

## VERIFIED: 30 U.S.C. 813(a); 30 CFR 100.3 (law.cornell.edu); 30 CFR 56.18002; 30 CFR 100.6; MSHA Mines dataset (https://arlweb.msha.gov/opengovernmentdata/DataSets/Mines.zip); Violations dataset statistics and top-10 standards (file dated 2026-09-04); schemas lacking an inspector field; Predictive Compliance claims (E&MJ Aug 2010 via Wayback); Ogletree tracker scope; Safety Pro in a Box; MSHA compliance-assistance page.

## NOT VERIFIED: 100.3 M/NM size-point tables; contest rate; abatement/withdrawal-order costs; mock-inspection prices; any D3 posting at a 10-99 producer; DOGE closure reversal; Census SUSB counts; whether per-office ordering differs from national; ABSORBS, FEE-SHIFT, COMPELLED shapes.
