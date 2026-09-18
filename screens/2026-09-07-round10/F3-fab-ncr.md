# F3. Fabrication NCR prediction for steel / misc-metals fabricators (20-299). Blind screen return, 2026-09-07.

**Adjacency ruling.** Closest dead relative: WPS/PQR (killed rung 1, commodity deliverable). Same customer and welding domain, but the five-tuple differs on asset (NCRs and rejections, not procedure paper), mistake (a written-up piece, not a missing qualification) and checker (the owner's special inspector, not AWS forms). Its magnitude evidence does not transfer; its rung-4 names (WeldNote, WeldEye, C-spec) are welding-record tools, none tested for the predictive claim. Construction closeout (sub side) shares only the free-bundle shape, tested below.

## THE CASE FOR

- **Strongest demand tier: D3, FILLED AT THE CUSTOMER.** A steel fabricator's direct-hire posting (OptiStaffing, Tigard OR), "Quality Control Supervisor – Certified Welding Inspector – Steel Fabrication", "$80,000 - $110,000/year DOE", duties: "Identify and document Non-Conformance Reports (NCRs), maintain logs, and submit them" and "Serve as a liaison between QC, production, QA, and third-party/DOT inspectors." The buyer already pays a salary for exactly the join this product automates, and the stated purpose is not incentive-inverted.
- **Strongest rung-2 pass: the fabricator is the conformance duty-holder.** NC OSFM interpretation (2012 code, 1704.3): "AWS D1.1 requires that the fabricator have its own quality control procedures and personnel. The fabricator's QC personnel are responsible for determining conformance of the welds... The special inspector acts as the owner's agent for verification by auditing the fabricator's QC program." And the code forces the label back: IBC 1704.2.4, "Discrepancies shall be brought to the immediate attention of the contractor for correction."
- **Best D1/D2/D3 number:** D3 above. No D1 exists.
- **Segment is countable:** Census CBP 2022, NAICS 332312 establishments with 20-249 employees = 682 + 323 + 176 = 1,181; NAICS 332323 20-249 = 447. 1,628 establishments in band.
- Incumbent MES does not make the claim: Tekla PowerFab's own Inspections page contains neither "predict" nor "nonconformance" nor "NCR"; FabStation's page does not contain "predict."

## SCORED WEAKNESSES

- **Rung 1 (criterion 3, 5).** Magnitude NOT VERIFIED. No cost per NCR, per rework hour, or per back-charge was found on any fetched page; GST Manufacturing's June 2026 article on bad-weld cost contains "no specific dollar figures." Criterion 3 scores 1 until a magnitude is verified.
- **Rung 1.5 (criterion 4, carried to G1/G3).** ITW US11347191B2, active to 2038-05-24, claims a welding analytics platform that learns to "predict and/or identify... defects and discontinuities" and "passing or failing the WPS or compliance with production specifications." Different asset (machine data, not inspector NCRs), but a granted claim on predicting weld failure from data. Also US11301976 (inspection support system learning pass/fail from NDT images), NOT fetched.
- **Rung 2 (criterion 1, 6): the code exempts approved fabricators from the checker.** IBC 1704.2.5.1 (up.codes, 2024 edition): "Special inspections during fabrication are not required where the work is done on the premises of a fabricator approved to perform such work without special inspection." The mybuildingpermit.com 2012 tip sheet names AISC first among accepted approvals. CASE Guide (STRUCTURE, May 2006): "When a fabricator has been approved, it is common practice for no inspections to be performed in the shop." So for the certified upper half of the band the named checker never enters the shop. F&R (2026-04-02) notes the exemption is jurisdiction-variable. The five-tuple's checker is intact only for uncertified shops and for field inspection.
- **Rung 2 (criterion 3): the priced instrument prices the INSPECTOR, not the mistake.** UH master spec 05 12 00 §1.05: "Should the fabricator not be so approved, the fabricator shall reimburse the Owner for the cost of the special inspections."
- **Rung 2.5 (criterion 3).** D1 EMPTY; D2 NOT VERIFIED (CWI rates "$75 to $125 per hour" search summary only); D3 FILLED AT THE CUSTOMER; D4 EMPTY (AISC pages 403); D5 UNRUN (forums 403). Only one tier clears.
- **Rung 3 (criterion 5).** GIVES: Tekla PowerFab Inspections is bundled in the MES the segment runs, "a digital log of every inspection and its result... helps in identifying the root causes"; residue: it logs, it does not predict. PUBLISHES: AWS D1.1 acceptance criteria; AISC 207 NCR records (NOT VERIFIED). CAPTURES: FabStation, "overlay their assemblies with your detailers model to catch errors before welding", deployments Beauce Atlas, Canam, Banker Steel (all above band); removes dimensional and fit-up errors, leaves weld-profile and coating. ABSORBS: not found. **RATCHET, heaviest:** the code already requires "a visual inspection of all welds is made prior to completion or prior to shipment" (NC OSFM quoting 1704.3 Exc. 2); the only saleable output, "this piece will pass, skip it," cannot lawfully be acted on. The residue is NDT prioritisation. FEE-SHIFT: none. COMPELLED: 1704.2.4 compels the inspector to hand the discrepancy to the contractor free, after the fact.
- **Rung 4 (criterion 4).** No incumbent makes the claim on its own page. Buyer's-guide artifacts exist, category mature. Exited predecessor: AVEVA FabTrol "officially withdrawn" 2022-09-01 (NOT VERIFIED), an MES, not a QC predictor. Reason (iii) suspected: no budget line beyond the QC salary already spent.
- **Rung 5 (criterion 5).** 5a passes (1704.2.4). 5b: reports go "to the building official and to the registered design professional," field discrepancies go to "the contractor," so the fabricator's copy arrives via back-charge, often lump-sum. 5c fails for the "will pass" label at approved shops: no inspector looks, so silence is the only label.
- **Rung 6 (criterion 6).** 1,628 establishments in band, establishments not firms, and 332312 includes bridge and metal-building fabricators; AISC-certified count NOT VERIFIED.

## KILL

**NO KILL.** K1: the shop controls its own rework money; no fee floor. K2: the fabricator is the conformance duty-holder (NC OSFM, AWS D1.1). K3: no vendor page makes the claim with a deployment and outcome.

## D3 STATE

**FILLED AT THE CUSTOMER**, read at the target band from a single direct-hire fabricator posting ($80-110k, Tigard OR); band size of the employer NOT VERIFIED.

## MUTATION (M0)

**Forced.** IBC 1704.2.5.1 plus UH §1.05 split the segment on the checker. For approved/AISC-certified shops the special inspector is absent from the shop, so the gradeable external write-up is the FIELD one: misfit at erection, erector or GC back-charge. That is a different five-tuple (checker = erector/GC, document = back-charge and field NCR, mistake = misfabrication reaching site), and FabStation already sits on its dimensional half. For uncertified shops the original five-tuple holds and the priced item is the inspector's hours the shop reimburses. The evidence forces picking one half, and RATCHET forces the output from "skip this piece" to "put the NDT and the second look here."

## PRACTITIONER QUESTIONS

1. Is your shop approved without special inspection in the jurisdictions you ship to, and when did a third-party inspector last write up a piece inside your shop?
2. Last back-charge from an erector or GC for a misfabricated piece: amount, itemised or lump, and could you trace it to a detail, welder or WPS?
3. Where do NCRs live today: PowerFab Inspections, Excel, paper travelers?
4. Rework hours per month, and does anyone total them?
5. Would you act on "this piece is high risk" by adding UT/MT, or by nothing?

## VERIFIED (page fetched)
- IBC 1704.2.5, 1704.2.5.1: https://up.codes/s/special-inspection-of-fabricated-items
- IBC 1704.2.4: https://up.codes/s/report-requirement
- 2012 IBC 1704.2.5.2 and AISC approval: https://mybuildingpermit.com/sites/default/files/documentation/Approved%20Fabricators_0.pdf
- CASE Guide "common practice for no inspections": https://dcstructural.com/pdfs/technical/200605_case_guide_to_special_inspections_part_2.pdf
- NC OSFM fabricator QC responsibility: https://www.ncosfm.gov/building/17043-special-inspections-fabrication-and-erection-structural-steel/open
- SEAC/RMSCA: https://www.seacolorado.org/docs/Weld_Inspections_in_Building_Construction.pdf
- UH 05 12 00 §1.05: https://www.uh.edu/facilities-planning-construction/vendor-resources/owners-design-criteria/master-specs/pdf/05-12-00-structural-steel-framing.pdf
- F&R: https://www.fandr.com/the-steel-fabrication-shop-and-special-inspections/ ; https://www.fandr.com/steel-plant-fabricator-approval-and-ibc-section-1704-2-5-1/
- D3 posting: https://jobs.optistaffing.com/jb/Quality-Control-Supervisor-Steel-Fabrication-Jobs-in-Tigard-OR/12580881
- Tekla PowerFab Inspections: https://support.tekla.com/doc/tekla-powerfab/2026/pdc_inspections
- FabStation: https://www.fabstation.com/
- ITW US11347191B2: https://patents.google.com/patent/US11347191B2/en
- GST article: https://www.gstmanufacturing.com/post/the-hidden-cost-of-a-bad-weld-what-structural-inspectors-actually-look-for
- CBP 2022 counts (cbp22us.txt rows 332312, 332323): https://www2.census.gov/programs-surveys/cbp/datasets/2022/cbp22us.zip

## NOT VERIFIED
CWI "$75 to $125 per hour"; IBC 1704.2 "owner... shall employ" exact text; AISC 207 NCR requirement; AISC certified-fabricator count; forum quotes (403); FabTrol withdrawal date; US11301976 claims; employer size of the Tigard posting.
