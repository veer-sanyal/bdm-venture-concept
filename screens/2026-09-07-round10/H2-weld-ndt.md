# H2. Weld NDT rejection prediction (structural, vessel, pipe fabricators, 30-300). Blind screen return, 2026-09-08.

Budget reached (24 searches, ~20 fetches).

## THE CASE FOR

**Strongest demand tier reached: D2, plus an instrument-priced escalation that behaves like D1 in kind.**
- The fabricator bears the whole cost of the mistake, in an owner spec's own words. SUNY SUCF sample piping spec 3.03B: "Any unacceptable defects encountered during the radiographic examination shall be repaired at no additional cost to the Owner. All repairs will be re-inspected. All costs associated with retesting failed welds and testing of additional welds as a result of failed welds will be the responsibility of the Contractor." And: "If a welder fails 10% of the Owners visual inspection and/or radiographic examination the Owners testing agency shall bring this to the attention of the Owner." (https://sucf.suny.edu/sites/default/files/docs/HTHW-InteriorPipingSpecification.pdf, Sept 2021)
- The code itself ratchets the penalty. ASME VIII UW-52(d)(2): two additional spots on a failed spot; if either fails, "the entire increment of weld is rejected". Spot location "shall be chosen by the Inspector."
- D2 prices: third-party RT $10 to $40 per shot film plus $95 to $200/hr technician, UT $15 to $75 per weld (NDTIntel 2026 guide). Rate card: certified technician $140/hr, film $35 to $150 each, "A MINIMUM OF 4 HOURS WILL BE CHARGED" (Steel Inspection & Testing Ltd, effective 2026-05-01).
- Magnitude, vendor-sourced: "Most pipe fab shops... have a repair rate of 3-5%"; 6,000 welds/yr at 3% is "around $180,000/year in repair costs" (Novarc blog, 2023-01-10). Implied ~$1,000 per repair is the screener's arithmetic.

**Strongest rung-2 pass: the duty holder is the customer.** AWS D1.1:2020 1.5.2: "The Contractor shall be responsible for WPSs, qualification of welding personnel, the Contractor's inspection, and performing work in conformance with the requirements of this code." No K2.

**Best market count (rung 6), VERIFIED from Census SUSB 2022:** firms with 20 to 299 employees: NAICS 332312 = 957, 332313 = 560, 332410 = 105, 332420 = 273; total 1,895 firms.

## SCORED WEAKNESSES

- **Rung 0.** The headline magnitudes (3-5% repair rate, $180k/yr) are a robot vendor's blog selling the fix. Criterion 3 magnitude NOT VERIFIED from a non-vendor source; scores 1 until verified.
- **Rung 1.** Money controlled by the customer, but the unit is small: ~$1,000 per cut-out against a $15 to $75 per weld pre-screen UT, and a shop's own CWI already decides which welds to pre-check. Criterion 5.
- **Rung 1.5.** No granted claim found reading on "historical NDT outcome joined to welder/joint/lot predicts rejection." Nearest: US12465993B2 (Hitachi, 2025-11-11) predicts internal defects from thermal cameras in real time. Clean not-found, two searches deep.
- **Rung 2, RATCHET inside the instrument.** UW-52 already prescribes the escalation and hands spot selection to the Inspector. The only output anyone would pay for ("these welds will pass, skip them") is one the customer cannot act on; the conservative output is what the code's own note already tells them to do. Heaviest weakness, criterion 5.
- **Rung 2, unit mismatch.** Every instrument acts at the WELDER level (UW-52: "a sufficient number of spot radiographs shall be taken to examine the welding of each welder"; SUCF: 10% per welder). The candidate predicts at the WELD level, finer than anything the counterparty acts on. Criterion 2.
- **Rung 2.5.** D3 UNRUN. D1 proper does not exist. Criterion 3.
- **Rung 3, by shape.** GIVES: Novarc publishes repair-rate economics to sell robots; Kemppi/Fronius bundle data management with power sources. PUBLISHES: the code publishes the sampling and escalation logic. CAPTURES: the checker's report itemises by weld and welder, and the fabricator's MIS ingests it: Tekla PowerFab Go, "The Test Results column shows the percentage of failed test records". ABSORBS: none found. FEE-SHIFT: n/a. COMPELLED: the owner's testing agency is compelled by spec to report failing welders. UNDERCUT: the welder-level repair report is a feature inside platforms the customer already buys. Criterion 4.
- **Rung 4.** WeldNote: "Monitor the repair percentages of welders and WPS', either in a Project basis or globally for your whole company" (https://weldnote.com/en/weld-tracking.html). WeldEye/Weldindustry (Kemppi Group): "Defect rate per welder per inspection method"; weldeye.com: "Automatic welding deviation alerts before and after welding" and "reduce weld repair rate by up to 40%", no named customer. MatriX by Pinnacle: customers Unithai, Eversendai Offshore, PAENAL (large offshore). Buyer's-guide roundups exist. No incumbent states the pre-shoot weld-level prediction; the welder-level answer is universal. Criterion 4, and criterion 2 for a claim narrowed below the incumbents'.
- **Rung 5.** 5a passes. 5b passes. 5c fails half: a flagged weld reworked before shooting is never graded; a passed weld is graded only if the Inspector's spot lands on it. Criterion 5.
- **Rung 6.** 1,895 firms in band; share running RT/UT volume weekly NOT VERIFIED. Criterion 6.

## KILL

**NO KILL.** K3 not reached: WeldNote/WeldEye state the welder-level claim on their own pages (G1) but no named deployment in the US 30-300 band with a shown outcome.

## D3 STATE

**UNRUN.** Indeed, ZipRecruiter and Lever all 403. One instrument-level observation: the SUCF spec assigns the per-welder failure-rate watch to the Owner's testing agency, which is FILLED AT COUNTERPARTY shaped and must be checked against real postings.

## MUTATION (M0)

The evidence forces a mutation and the mutated form lands on an incumbent. Every instrument and every incumbent acts at the WELDER level; the honest reformulation is "welder trending toward the spec's 10% before the Owner's agency flags him," which WeldNote and WeldEye already sell. The alternative customer, the NDT firm, owns cross-shop data but bills re-shoots, so it is incentive-inverted. No principled mutation survives.

**Adjacency ruling.** WPS/PQR (dead, rung 1): same customer, different asset, mistake and checker clause; its rung-4 evidence transfers directly (WeldNote/WeldEye/WeldOffice installed at this customer). Scrap grade calls (dead): same shape; incumbents capture the reject after the fact, and rung 6 (an employee, the CWI, already does the task) is where it likely dies. PPAP pooling: does not transfer; single-shop asset.

## PRACTITIONER QUESTIONS

1. When did a third-party RT reject last cost you a cut-out, and what did it cost in hours and schedule?
2. Who in your shop decides which welds get pre-checked by your own UT before the owner's agency shoots, and on what basis?
3. Do you have a repair-rate-by-welder report today (PowerFab, WeldNote, WeldEye, spreadsheet), and did it ever change a decision?
4. Has an owner's agency ever invoked a 10%-type welder clause on you? What happened?
5. Does your NDT firm ever let you pick or influence spot locations?

## VERIFIED / NOT VERIFIED

**VERIFIED:** SUCF spec clauses; UW-52 text as reproduced in a vendor PDF marked "FOR REFERENCE ONLY" (not the ASME book); D1.1:2020 1.5.2, 1.5.3 and Clause 8 headings (https://pubs.aws.org/Download_PDFS/D1_1_D1_1M_2020_index_PV.pdf); NDTIntel 2026 rates (https://www.ndtintel.com/guides/pdf/ndt-inspection-rate-guide-2026.pdf); Steel Inspection & Testing rate card (https://www.steelinspection.com/servicerates2.html); Novarc blog figures (vendor marketing, https://www.novarctech.com/resources/blog/industry/the-importance-of-improving-repair-rates/); SUSB 2022 firm counts; WeldNote, WeldEye, Weldindustry, MatriX, Weldex, Tekla PowerFab Go quotes (https://support.tekla.com/doc/tekla-powerfab/2023/go_inspection_test_records); US12465993B2 claim 1.

**NOT VERIFIED:** any non-vendor repair-rate benchmark; the $1,000-per-repair figure (derived); D1.1 8.6 cost-allocation text (search summary of a walled forum); Fronius WeldCube "Rework Station"; QA/QC Manager comp bands; AISC certified-fabricator and National Board stamp counts; share of band firms with weekly NDT volume; any exited predecessor.
