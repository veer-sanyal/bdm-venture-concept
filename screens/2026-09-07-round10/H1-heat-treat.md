# H1. Pre-ship hardness / case-depth failure prediction for US commercial heat treaters (30-250). Blind screen return, 2026-09-08.

**ADJACENCY RULING.** Dead lane "Private-by-operating assets sold to US automotive Tier-2/3 suppliers" is a relative. Five-tuple differs on customer (a sub-tier processor serving many industries), asset (the treater's own furnace chart), document set, and checker (the treater's customer, not the OEM). Its evidence transfers only to loads run under automotive POs and to cross-customer POOLING; the claim here is single-shop, so it is a scored weakness, not a kill. "Scrap grade calls" is the sibling shape; its rung-4 lesson transfers. PPAP and WPS/PQR do not.

## THE CASE FOR

- **Strongest demand tier: D3 FILLED AT THE CUSTOMER.** The Monty, Commercial Heat Treating Salary Guide (2018-03-02): Quality Manager "between $70 and $90k, but can easily creep into six-figures"; Plant Metallurgist "$75-95k". A live posting, H&S Heat Treating: Material Science/Heat Treat Engineer, "$85,000 - $95,000, negotiable", duties include "Supervising the calibration and maintenance of testing equipment, including furnace control systems."
- **Strongest rung-2 pass: the instrument binds the treater, and it is a records-access regime, not a derived-data regime.** Collins A-9000 Rev M (2019-07-01) §4.3.1: records "shall be available to Collins, its customers, and/or regulatory agencies, upon request, at any time during the retention period" (10 years). Grep for "proprietary", "derived", "aggregat": zero hits. K2 does not fire.
- **Best D1-shaped number: the industry's own instrument prices the mistake.** MTI Statement of Limited Liability (2011, used verbatim by member shops): "SELLER'S LIABILITY SHALL NOT EXCEED TWICE THE AMOUNT OF THE CHARGES FOR THE WORK DONE ON ANY MATERIAL."
- **Rung 5c is structurally good:** the load is hardness-tested regardless, so a label returns for both answers (subject to per-load frequency caveat).

## SCORED WEAKNESSES

- **Rung 1 (criteria 3, 5):** The mistake as written ("scrapping the customer's parts with the treater liable") is contractually false by default. MTI: "no liability on the Seller in contract or tort ... for any special, indirect or consequential damages"; "No claims will be allowed for shrinkage, expansion, deformity, or rupture of material in treating". The treater's exposure per failed load is its own re-run plus a refund capped at 2x a processing charge. Re-run cost: NOT VERIFIED.
- **Rung 1.5 (criterion 4):** No granted claim found reading on a per-load batch prediction from chart plus mill cert. Nearest: US 12,291,757 (austenite prediction, continuous strip) and US 12,085,341 (predicting heat treatment SYSTEM failures). Titles only, NOT VERIFIED. Academic prior art dense.
- **Rung 2 (criteria 4, 5):** Pooling across customers foreclosed for automotive-PO work by the dead lane's terms. No amnesty, free appeal or legislated-away.
- **Rung 2.5 (criterion 3):** D1 is a CAP set by the seller's side, not a checker's fee. D2 NOT FOUND. D4 none. D5 UNRUN. Clears weakly on D3 + D1-shaped cap.
- **Rung 3 (criterion 5, heaviest):** GIVES: SSi SuperDATA bundles "Alarm and Event Viewers", "deviation alarms", "Gap reporting", "AMS 2750 and CQI-9 Compliant"; removes real-time chart-deviation detection. PUBLISHES: AMS 2759, CQI-9 and AC7102 publish the process windows. CAPTURES: Yokogawa SMARTDAC+ AI app note (2022) detects "temperature abnormalities caused by burner failure, poor furnace seal" "before a quality defect occurs" inside the recorder. ABSORBS: MTI has absorbed the scrap cost away from the treater onto its customer. RATCHET: the conservative answer, test a coupon from every load before shipping, is already required and cheap; the less-conservative output (ship or skip on a prediction) is unusable under Nadcap. FEE-SHIFT: none. COMPELLED: none. UNDERCUT: paid simulators (DANTE, DEFORM-HT, Thermo-Calc DICTRA) predict at recipe design time.
- **Rung 4 (criterion 4):** HRC Digital (2026) makes nearly the claim on its own page: "Model how temperature, time, atmosphere, part geometry, and load configuration affect hardness, case depth, distortion, and microstructure", "plant-specific machine learning models"; no named customer, no outcome: G1 without G2, SCORE. Bluestreak already holds the join: "integrated quality hub, nonconformances, customer complaints, corrective actions, specifications management ... data collection"; customer quote: "reduced our re-work because we can now tie quality management initiatives directly to individual equipment operators". No predictive claim. Exited predecessor: NOT SEARCHED.
- **Rung 5 (criterion 5):** 5a passes (MTI five-business-day notice; NCR and parts return). 5b partial: hardness itemised but cause not labelled. 5c good, conditional on per-load testing, NOT VERIFIED from the standard's text.
- **Rung 6 (criterion 6, heavy):** SUSB 2021, NAICS 332811 US: 583 firms, 745 establishments, 18,335 employees; 20-99 employees: 167 firms; 100-499: 47 firms. The 30-250 band is a subset of 214 firms.

## KILL

**NO KILL.** K1: the customer controls its own re-run decision. K2: the treater is the duty-holder (A-9000 §4.3, Nadcap AC7102). K3: HRC Digital's claim lacks a deployment and an outcome.

## D3 STATE

**FILLED AT THE CUSTOMER.** Band read: industry-wide (The Monty guide, 2018) plus one commercial treater of unstated size in Ontario. Not verified at 30-250 US specifically.

## MUTATION (M0)

**YES, forced.** MTI caps the treater's exposure at 2x a processing charge and pushes the parts' value onto the treater's customer; SUSB gives 583 firms total. The party that bears BOTH the re-run and the scrap, and owns the furnace chart, is the captive (in-house) heat treat department inside a part maker (gear, bearing, fastener, forging). Same asset, mistake and checker, larger and better-motivated buyer. Caveat: automotive captives sit under the dead lane's terms. Captive count NOT VERIFIED.

## PRACTITIONER QUESTIONS

1. How many loads per month fail the customer's hardness or case-depth check, and when was the last one?
2. What does one re-run cost you in furnace hours, gas and labour?
3. Do you test a coupon from every load before shipping, and how often does the customer's lab disagree with yours?
4. Have you ever paid a claim above 2x charges, or signed a customer's terms overriding MTI?
5. Of your last ten failures, how many traced to the chart, to the mill cert, to loading density, to quench?
6. Do you run Bluestreak or SSi SuperDATA, and would you re-temper on a flag before the coupon test?

## VERIFIED (page read)
- MTI Statement of Limited Liability: https://generalmetalheat.com/wp-content/uploads/2024/02/MTI-STATEMENT-OF-LIABILITY-2011.pdf ; https://petersheattreat.com/terms-conditions/
- Collins A-9000 Rev M §4.3: https://www.rtx.com/collinsaerospace/-/media/CA/suppliers/hutc/a-9000-rev-m.pdf
- The Monty salary guide: https://themonty.com/commercial-heat-treating-salary-guide/
- H&S Heat Treating posting: https://imt.scouterecruit.net/jobs/268224-material-science-heat-treat-engineer-metallurgy
- SUSB 2021 NAICS 332811: https://www2.census.gov/programs-surveys/susb/datasets/2021/us_state_6digitnaics_2021.txt
- HRC Digital: https://www.hrc-digital.com/
- Bluestreak: http://www.heat-treat-software.com/ ; https://www.go-bluestreak.com/home
- SSi SuperDATA: https://supersystems.com/software/superdata/
- Yokogawa SMARTDAC+ AI: https://www.yokogawa.com/library/resources/application-notes/heat-treatment-ai-equipment-quality-easy-predictive-detection
- Kacsik on AC7102 (secondary): https://www.kacsik.com/blog/understanding-nadcap-heat-treating-checklist-ac7102

## NOT VERIFIED
Re-run cost per load; outside-lab test price; AMS 2759 per-load record text; CQI-9 per-load hardness frequency; US 12,291,757 and US 12,085,341 claim scope; Indeed and ZipRecruiter figures; Ipsen PdMetrics; Vira-Tech (404); DANTE / DEFORM-HT / Thermo-Calc capabilities; captive heat-treat department count. Exited-predecessor search and D5 not run.
