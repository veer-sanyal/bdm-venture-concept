# G2. Dental lab remake prediction (independent US dental labs, 5-50 employees). Blind screen return, 2026-09-07.

**Adjacency ruling.** No dental relative on the dead list. Nearest shape is Scrap grade calls (predict the counterparty's grading before you ship; killed at rung 4 because every LMS captures the downgrade post hoc). Five-tuple differs on all five. Only the rung-4 lesson transfers: the after-the-fact join is a baseline LMS feature (verified below); the predictive half must be tested on its own.

## THE CASE FOR

- **Strongest demand tier: D1, the lab prices the mistake in its own policy.** Modern Dental USA: "If the workmanship or material is faulty, the appliance will be repaired or remade at no charge", two-year warranty; "The original dental restoration must be returned" (https://www.moderndentalusa.com/warranty). Les Dentz / 38 Smiles: "Eligible remakes will be done at no charge if received within 60 days of invoice date" (search summary, NOT VERIFIED). The remake is 100% the lab's cost and it comes back in a box.
- **Strongest rung-2 pass: the customer is the duty-holder.** The remake policy is the lab's own promise; the lab controls whether it cuts. No counterparty instrument, no portal ToU. K1 and K2 both pass cleanly.
- **Best magnitude number (D1 scale):** "the national average for dental laboratory remakes in the U.S. is 4%, with a range of 1% to as high as 6-7%" (Spear, Robert Winter, 2020-11-09, https://www.speareducation.com/resources/spear-digest/the-cost-of-laboratory-remakes/). Evident's own arithmetic: "the true cost of one 'no-charge' remake can easily exceed $400", lab direct cost "$75-$150 per case" (2025-07-17, vendor blog, NOT VERIFIED as market fact). SUSB 2022 receipts per firm in the 10-19 band: $641.4M / 376 = ~$1.7M (VERIFIED inputs, screener's division); 4% of that is ~$68k/yr of remade revenue at one mid-band lab.
- **Rung 5a is a genuine pass:** the outcome physically returns to the payer, with a slip.

## SCORED WEAKNESSES

- **Rung 1 (crit 7):** money is real but small per unit and already sunk into the lab's cost structure as "weather"; no fee floor, no external release.
- **Rung 1.5 (crit 4):** Google Patents rendered as a JS shell; one query surfaced no claim on per-dentist remake prediction (US7333874B2 covers clinic-lab design coordination). NOT FOUND, low confidence.
- **Rung 2 (crit 4, 5):** the instrument ships its own free remedy and labs already invoke it by hand: "If new impression was requested by Modern Dental but followed the Doctor's instruction to proceed without the new impression, the remake policy is null and void. Any further remake will be completed at full cost." The "call before cutting" lever is a standing clause, not a product.
- **Rung 2.5 (crit 3, 2):** D3 FILLED AT THE CUSTOMER but thin; partial incentive inversion: coordinators are paid for throughput and dentist retention, and LMT reports that when labs raise concerns "41% say the dentist generally sends a new impression and another 41% are usually told to 'do the best they can'" (Glidewell Chairside reprint of LMT, March 2011). Nearly half of calls resolve to "proceed anyway".
- **Rung 3 (crit 4, 5):** CAPTURES and UNDERCUT together take the rule-detectable half (missing margin, bad bite, incomplete Rx), leaving the judgment residue where a per-dentist model has least data.
- **Rung 4 (crit 4):** EviSmart QC: "Checks Every Case for Missing or Unclear Instructions Before It Hits Production", "Runs automated checks to catch missing scans, unclear Rx, or mismatched info" (https://evismart.com/all-modules/qc), available 2025-04-15. No per-dentist prediction claim, no named lab, no outcome. Mainstreet DentaLab: "Remakes are tracked by reason, doctor, and technician". TrazaLab Lab Solo $49/mo, Lab Pro $99/mo, "Validation Gate" with "rule-based checks before send and on order receipt", and explicitly "That history does not diagnose, predict, or guarantee the next outcome". Nobody states the differentiated claim; three vendors hold the data it needs. Buyer's guides exist: mature category.
- **Rung 5b/5c (crit 5, the crux):** attribution is contested and self-reported ("more than three-quarters of remakes in their laboratories are due to dentist error", labs speaking); chairside adjustments (Spear: "20 minutes of adjustment time = $125") never return to the lab, so the label set is truncated to hard refusals. 5c: the "call, dentist re-impresses" branch destroys its own counterfactual. Base rate 1-4% at a lab where one dentist sends perhaps 100 units/yr yields 1-4 events per dentist per year: no per-dentist model at the 5-50 band.
- **Rung 6 (crit 6):** SUSB 2022, NAICS 339116, US: 4,566 firms; 3,037 under 5; 802 at 5-9; 376 at 10-19; 287 at 20-99; 49 at 100-499; 15 at 500+ (https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_6digitnaics_2022.xlsx). The 5-50 band is at most 802+376+287 = 1,465 firms. At TrazaLab/Evident price points ($49-199/mo) that is a ~$0.9M-3.5M revenue ceiling at 100% share.

## KILL

**NO KILL.** K1: the lab controls the cut and eats the remake. K2: the remake policy binds the lab itself. K3: EviSmart QC has G1 for the rule-based half only, no G2, no outcome.

## D3 STATE

**FILLED AT THE CUSTOMER, band read at 10-19 (single posting), with a partial INCENTIVE-INVERTED flag.** Technics Dental Laboratory, Margate FL, Dental Lab Office Coordinator, $45,000-55,000/yr, "Enter and track incoming dental cases" (SimplyHired; employer size NOT VERIFIED). Pittman Dental (2023-05-31): "assigns each dentist an Account and Quality Control Manager". The role exists and is paid; its duties are intake and throughput, not prediction.

## RUNG 3 SHAPES

- GIVES: Dandy AI Scan Review, 2025-11-18, "included at no additional cost for existing Dandy Chairside users", detects "undercuts, margin obstructions, and occlusal clearance" chairside. A competitor lab gives the checker the tool.
- PUBLISHES: the 4% benchmark and LMT fault survey are published.
- CAPTURES: EviSmart QC and TrazaLab Validation Gate check the scan and Rx at intake; 3Shape margin marking search-summary only.
- ABSORBS: the lab's own no-fault policy already absorbs it; 25% of labs "don't charge for remakes initially" (LMT), Benchmark Castings charges 50% for clear dentist error.
- RATCHET: inverted here: the conservative answer (call, request new impression) is free and already in policy; the product's only sellable output is calls the rules miss, on 1-4 events per dentist per year.
- FEE-SHIFT, COMPELLED: not applicable.
- UNDERCUT: the LMS vendor the lab already pays (Evident, $199-999/mo tiers) ships QC as a module; the remake-by-doctor join is baseline (Mainstreet).

## MUTATION (M0)

**Forced, and the mutated form lands on an occupied square.** Forcing evidence: Modern Dental's void clause plus LMT's 41% "do the best they can" plus Benchmark's 50% charge. The money is not in predicting the remake; it is in DOCUMENTING the pre-cut warning so the remake converts from lab-fault (free) to dentist-fault (billable or warranty-void). That is a consent-to-proceed paper trail, not a model. TrazaLab already sells exactly that at $49-99/mo ("Defensible history", "Exportable audit of files, approvals, and access"). No principled mutation survives that keeps the predictive claim.

## PRACTITIONER QUESTIONS

1. K4 salience: when did a remake last come back, what did it cost you, and did you bill any of it?
2. When you call a dentist about a bad scan, what fraction say proceed, and do you then charge the remake?
3. Do you know your remake rate per dentist today, and from which report?
4. Do chairside adjustments ever reach you as data, or only as silence?
5. Have you seen EviSmart QC or TrazaLab, and what does your LMS already flag at intake?

## VERIFIED / NOT VERIFIED

**VERIFIED (fetched):** SUSB 2022 firm counts for 339116; Modern Dental warranty clauses; Spear 4% and $187.50/$125 (2020); LMT "three-quarters" and 41/41 split (2011 reprint); Evident $400 and $75-150 (vendor arithmetic, 2025-07-17); EviSmart QC page and 2025-04-15; EviSmart LMS $199/$499/$999; TrazaLab tiers and "does not predict"; Mainstreet remake-by-doctor; Dandy AI Scan Review date, free, scope; Pittman 3%/<1% and "Account and Quality Control Manager"; Technics posting $45-55k; Glidewell "40 hours of chair time" (2026-04-30, vendor).

**NOT VERIFIED:** JADA/PBRN remake-rate paper; 60-day no-charge windows; Indeed QC duty language; ZipRecruiter $18-31/hr; 3Shape scanner-side margin check; "80% of dentists do not complete the information legally required"; patent absence (one query); exited predecessor absence (one query); per-lab unit volume.
