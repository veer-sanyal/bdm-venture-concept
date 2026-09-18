# A. Supplier universe market sizing: Tier-2/Tier-3 manufacturing suppliers with automotive/appliance/heavy-equipment exposure

Desk research, primary government sources only. All files below were fetched directly (Census bulk data files, BEA detail Use table, IEDC PDF, CAR PDF) and parsed locally, not read from search snippets. Method notes and caveats follow each section. No em dashes used anywhere in this file (en dashes only, in ranges).

Data quality note that applies to every SUSB figure below: Census applies statistical noise infusion for disclosure avoidance to SUSB cells (every row in the file carries a "G" noise flag). Small differences between a published subtotal (e.g. "<500 employees") and the sum of its component bins (which I computed) are attributable to this, not to error. I flag the two rows where it produced a visible gap.

---

## 1. NAICS 3363 and 6-digit sub-industries: US firms and establishments by employment-size class

**Source**: US Census Bureau, Statistics of US Businesses (SUSB), "US & states detailed sizes" table, 2022 (released 4/10/2025).
**URL**: https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_naics_detailedsizes_2022.xlsx
**Dataset year**: 2022 (latest SUSB detailed-size-class release; 2021 vintage exists at the equivalent 2021 URL but 2022 is newer)
**Source type**: government dataset (primary, Census Bureau)
**Scope as published**: firms and establishments, United States total (state code "00"), all legal forms combined, enterprise employment size class. "Firm" = an entire enterprise (may span multiple establishments); "establishment" = each physical location.
**Status**: VERIFIED (file fetched and parsed directly)

Published size-class bins in the source: 01 Total, 02 <5, 03 5-9, 04 10-14, 05 15-19, 06 <20 (subtotal), 07 20-24, 08 25-29, 09 30-34, 10 35-39, 11 40-49, 12 50-74, 13 75-99, 14 100-149, 15 150-199, 16 200-299, 17 300-399, 18 400-499, 19 <500 (subtotal), 20 500-749, 21 750-999, 22 1,000-1,499, 23 1,500-1,999, 24 2,000-2,499, 25 2,500-4,999, 26 5,000+.

The requested "20-99" and "100-499" bands are not published directly; I summed the component bins and show the arithmetic. "500+" = published Total minus published "<500 employees."

| NAICS | Description | Total Firms / Estabs | <20 Firms / Estabs | 20-99 (sum of bins 07-13) Firms / Estabs | 100-499 (sum of bins 14-18) Firms / Estabs | 20-499 subtotal Firms / Estabs | 500+ (Total minus <500) Firms / Estabs |
|---|---|---|---|---|---|---|---|
| 3363 | Motor Vehicle Parts Manufacturing | 3,616 / 4,640 | 1,975 / 1,978 | 793 / 841 | 496 / 653 | 1,289 / 1,494 | 352 / 1,168 |
| 336310 | Motor Vehicle Gasoline Engine and Engine Parts Mfg | 637 / 699 | 456 / 457 | 84 / 86 | 37 / 46 | 121 / 132 | 60 / 110 |
| 336320 | Motor Vehicle Electrical and Electronic Equipment Mfg | 501 / 557 | 281 / 281 | 108 / 112 | 49 / 57 | 157 / 169 | 63 / 107 |
| 336330 | Motor Vehicle Steering and Suspension Components Mfg | 229 / 277 | 117 / 117 | 40 / 41 | 29 / 33 | 69 / 74 | 43 / 86 |
| 336340 | Motor Vehicle Brake System Mfg | 132 / 166 | 65 / 65 | 18 / 24 | 22 / 24 | 40 / 48 | 24 / 50 |
| 336350 | Motor Vehicle Transmission and Power Train Parts Mfg | 365 / 464 | 186 / 186 | 74 / 75 | 49 / 55 | 123 / 130 | 56 / 148 |
| 336360 | Motor Vehicle Seating and Interior Trim Mfg | 304 / 434 | 121 / 122 | 75 / 80 | 53 / 78 | 128 / 158 | 55 / 154 |
| 336370 | Motor Vehicle Metal Stamping | 543 / 717 | 152 / 152 | 186 / 194 | 132 / 165 | 318 / 359 | 73 / 206 |
| 336390 | Other Motor Vehicle Parts Mfg | 1,101 / 1,326 | 597 / 598 | 208 / 226 | 145 / 195 | 353 / 421 | 151 / 307 |

**Arithmetic check**: for each row, <20 + 20-99(sum) + 100-499(sum) should equal the published "<500" bin. It matches exactly for 3363, 336310, 336320, 336330, 336350, 336360, 336370, 336390 (published <500 values: 3,264 / 577 / 438 / 186 / 309 / 249 / 470 / 950 firms respectively, all equal to my summed components). For **336340** the published "<500" firms figure is 108 but my summed components give 105 (a 3-firm gap); this is noise-infusion, not an arithmetic error on my part. Reported both ways above so the gap is visible.

**Verbatim column headers from source file** (row 3 of the sheet): `State | State Name | NAICS | NAICS Description | Enterprise Size | Firms | Establishments | Employment | ... | Annual Payroll... | ... | Receipts...`. Example verbatim row (3363, Total): `('00', 'United States', '3363', 'Motor Vehicle Parts Manufacturing', '01: Total', 3616, 4640, ...)`.

---

## 2. NAICS 3352, 333111, 333120: US firms and establishments by size class

Same source, dataset year, and method as Section 1.

| NAICS | Description | Total Firms / Estabs | <20 F/E | 20-99 (sum) F/E | 100-499 (sum) F/E | 20-499 subtotal F/E | 500+ F/E |
|---|---|---|---|---|---|---|---|
| 3352 | Household Appliance Manufacturing | 304 / 363 | 214 / 214 | 39 / 39 | 21 / 28 | 60 / 67 | 28 / 80 |
| 333111 | Farm Machinery and Equipment Mfg | 1,024 / 1,118 | 669 / 672 | 233 / 245 | 85 / 106 | 318 / 351 | 37 / 95 |
| 333120 | Construction Machinery Mfg | 574 / 666 | 288 / 289 | 163 / 169 | 67 / 92 | 230 / 261 | 56 / 116 |

**Arithmetic check**: 333111 and 333120 reconcile exactly to their published "<500" bins (987 and 518 firms). **3352** shows a small gap: published "<500" firms = 276, my summed components = 274 (2-firm gap, same noise-infusion caveat as above).

**Status**: VERIFIED (same file as Section 1).

---

## 3. Tier-2/Tier-3 exposure outside NAICS 3363 (the hard part)

### 3a. Raw universe size of the adjacent NAICS codes (context only, not automotive-specific)

Same SUSB 2022 source and method as Sections 1-2. These are **total** firm/establishment counts for the whole industry, not an automotive share; automotive share is addressed separately in 3b-3d below.

| NAICS | Description | Total Firms / Estabs | <20 F/E | 20-99 (sum) F/E | 100-499 (sum) F/E | 500+ F/E |
|---|---|---|---|---|---|---|
| 332119 | Metal Crown, Closure, and Other Metal Stamping (except Automotive) | 1,044 / 1,145 | 521 / 522 | 355 / 374 | 118 / 159 | 50 / 90 |
| 332710 | Machine Shops | 17,130 / 17,433 | 14,254 / 14,277 | 2,368 / 2,486 | 369 / 448 | 139 / 222 |
| 326199 | All Other Plastics Product Manufacturing | 4,545 / 5,566 | 2,381 / 2,387 | 1,223 / 1,299 | 588 / 823 | 353 / 1,057 |
| 3315 | Foundries | 1,173 / 1,367 | 538 / 539 | 377 / 389 | 167 / 216 | 91 / 223 |
| 332811 | Metal Heat Treating | 563 / 725 | 327 / 328 | 164 / 189 | 50 / 103 | 22 / 105 |
| 332813 | Electroplating, Plating, Polishing, Anodizing, and Coloring | 1,896 / 2,005 | 1,246 / 1,251 | 513 / 545 | 103 / 147 | 34 / 62 |

Note on NAICS 332119: its own Census title is "**except Automotive**"; the 6-digit code by definition excludes stamping done specifically for automotive (that falls under 336370, Motor Vehicle Metal Stamping, already counted in Section 1). So 332119 establishments are, by Census's own classification logic, *not* primary automotive stampers; any automotive exposure they have is secondary/incidental (e.g., a firm classified here on its primary product line but also runs automotive stamping jobs), which is exactly the ambiguity the BEA Use-table exercise in 3b is meant to probe.

**Status**: VERIFIED.

### 3b. BEA Input-Output Use Table: computed automotive purchase shares (my calculation, arithmetic shown)

**Source**: US Bureau of Economic Analysis, "The Use of Commodities by Industries, Before Redefinitions (Purchasers' Prices)," Detail level (402 industries), 2017 column.
**URL**: https://apps.bea.gov/industry/Release/XLSX/IOUse_Before_Redefinitions_PUR_Detail.xlsx (retrieved via BEA's Interactive Data Application, Input-Output > Make-Use-Imports Before Redefinitions > Use table, Detail)
**Dataset year**: 2017 (this is BEA's most recent full "Detail" 402-industry benchmark table; annual updates after 2017 exist only at coarser Summary/Sector level, which cannot separate 332xxx sub-industries from other metals)
**Source type**: government dataset (primary, BEA)
**Status**: VERIFIED (file fetched directly)

**What I computed and how**: for each upstream commodity row, I summed the dollar cells in the columns for all motor-vehicle-and-parts-manufacturing industries (BEA detail codes 336111, 336112, 336120, 336211-336214, 336310, 336320, 336350, 336360, 336370, 336390, 3363A0) and divided by that row's own "Total Commodity Output" column (BEA code T007). This measures **direct** purchases by motor-vehicle-industry columns as a share of the upstream commodity's total output; it does NOT capture indirect/multi-tier flows (e.g., a machine shop selling to an appliance maker who sells to auto), so it is a lower bound on true automotive exposure, not a full count of "how many suppliers sell into automotive."

Important mapping caveat: BEA's 402-industry classification does not always match 6-digit NAICS 1:1.
- BEA code 332119 = NAICS 332119 exactly (clean match).
- BEA code 332710 = NAICS 332710 exactly (clean match).
- BEA code 331510 + 331520 (Ferrous + Nonferrous metal foundries) together = NAICS 3315 exactly (clean match, summed).
- BEA code 332800 ("Coating, engraving, heat treating and allied activities") = NAICS 332811 + 332812 + 332813 combined. I could NOT isolate 332811 or 332813 alone from this table.
- BEA code 326190 ("Other plastics product manufacturing") = NAICS 326191 + 326199 combined. I could NOT isolate 326199 alone from this table.

| Upstream commodity (BEA code / NAICS match) | 2017 sales to all 336xxx (motor vehicle & parts) columns, $M | 2017 Total Commodity Output, $M | Computed share to motor-vehicle-industry buyers | Arithmetic |
|---|---|---|---|---|
| 331510+331520 Foundries (= NAICS 3315, exact) | $12,074M | $32,598M | 37.0% | (5,298+6,776)/(18,682+13,916) |
| 332119 Metal stamping except automotive (= NAICS 332119, exact) | $1,450M | $14,187M | 10.2% | 1,450/14,187 |
| 332710 Machine shops (= NAICS 332710, exact) | $3,613M | $38,090M | 9.5% | 3,613/38,090 |
| 332720 Turned product, screw/nut/bolt mfg (adjacent, not in the requested list but relevant) | $8,079M | $40,160M | 20.1% | 8,079/40,160 |
| 332800 Coating/engraving/heat treating (= NAICS 332811+332812+332813 combined, NOT isolable to 332811 or 332813 alone) | $1,676M | $26,845M | 6.2% | 1,676/26,845 |
| 326190 Other plastics products (= NAICS 326191+326199 combined, NOT isolable to 326199 alone) | $7,840M | $141,737M | 5.5% | 7,840/141,737 |

This table answers the "share of output" half of item 3 directly from a government dataset, with the mapping limits stated. It does **not** answer "how many establishments" sell into automotive; BEA's Use table has no establishment counts, only dollar flows.

### 3c. Center for Automotive Research (CAR): stated cross-NAICS method, but employment not establishment counts

**Source**: Center for Automotive Research, "Contribution of the Automotive Industry to the Economies of All Fifty States and the United States" (2010).
**URL**: https://www.cargroup.org/wp-content/uploads/2017/02/CONTRIBUTION-OF-THE-AUTOMOTIVE-INDUSTRY-TO-THE-ECONOMIES-OF-ALL-FIFTY-STATES-AND-THE-UNITED-STATES.pdf
**Dataset year**: report published 2010; underlying industry-composition data sourced from "Census data at the 7-digit NAICS level, 2002 and 2007, County Business Patterns 2006" per the report's own source note. This method is roughly two decades old and has not been updated in a public CAR report since.
**Source type**: industry research institute (nonprofit), with an explicitly stated method (not a vendor pitch)
**Status**: VERIFIED (PDF fetched and text-extracted directly)

Verbatim quote on scope: "In this report, the automotive supplier industry is defined as a large group of independent, non-OEM, parts producers that sell their finished goods to both domestic and international OEMs, as well as after-market parts replacement retailers. For the purpose of this study, the automotive supplier group includes employees beyond NAICS 3363 (the industry classification code for motor vehicle parts) to account for products developed by other manufacturing industries that are used in the production of vehicles."

CAR's cross-NAICS table (their Table B.1, "Sectors Comprising Auto Parts Manufacturing Industry"; note these are 7-digit Census **product class** codes, not standard 6-digit establishment NAICS, meaning CAR isolated the auto-specific product lines inside broader industries using product-level shipment data rather than whole-establishment counts):

| Code (7-digit product class) | Description | Employment (CAR estimate) |
|---|---|---|
| 3261.991 | Transportation plastics products (boats, rail, aerospace too, not just autos) | 62,000 |
| 3262.1 | Tires | 52,000 |
| 3262.203 | Hoses for motor vehicles | 6,000 |
| 3325.106 | Motor vehicle hardware | 12,000 |
| 3345.145 | Motor vehicle instruments | 7,000 |
| 3351.10 | Lighting | 2,000 |
| 3359.114 | Batteries | 11,000 |
| 3362.115 | Other truck and vehicle bodies for sale | 12,000 |
| 3363 | Auto Parts | 522,000 |

Verbatim source line under the table: "Sources: Bureau of Economic Analysis, Input/Output Matrices, Census data at the 7-digit NAICS level, 2002 and 2007, County Business Patterns, 2006, Bureau of Labor Statistics, Quarterly Census of Employment and Wages (QCEW), Annual Survey of Manufacturers, Rubber Manufacturers Association, Battery Council International."

This is the clearest example found of a named institution stating a cross-NAICS automotive-supplier method. It gives **employment**, not a count of establishments/firms, and the underlying data is 15-20 years stale. I did not find a more recent CAR report that repeats this cross-NAICS breakout (their 2024 report, "Economic Contribution of the U.S. Automotive Industry," checked directly, covers investment tracking and macro employment contribution but does not restate or update Table B.1 or give a supplier count).

### 3d. Indiana Economic Development Corporation (IEDC): a bare count, no stated method

**Source**: Indiana Economic Development Corporation, "Advanced Manufacturing" fact sheet (PDF).
**URL**: https://www.iedc.in.gov/docs/default-source/iedc-assets/iedc_advmanf.pdf
**Dataset year**: undated infographic; the one sourcing note on the page ("SOURCE: Dun & Bradstreet, November 2020") is attached to the "Major Companies & Industry Footprint" company list, and it is ambiguous whether it also covers the "500+" stat, since the document does not repeat a source note next to that specific figure.
**Source type**: consultancy/vendor-style state marketing collateral (a state economic development agency's promotional one-pager, not a research methodology document)
**Status**: VERIFIED (PDF fetched, text-extracted directly)

Verbatim (from the infographic's icon panel, PDF text extraction): "2ND IN OVERALL AUTOMOTIVE PRODUCTION" / "MAJOR OEM ASSEMBLY PLANTS" / "**500+ AUTOMOTIVE PARTS SUPPLIERS**." No definition is given anywhere in the document of what counts as a "supplier" (establishment vs. firm vs. distributor; in-state HQ vs. any Indiana location; direct-to-OEM vs. any tier). This should be treated as marketing collateral, not a citable count for sizing work.

### 3e. MEMA / OESA supplier counts: NOT FOUND with a stated method

I fetched mema.org (OESA's URL, oesa.org, 301-redirects to mema.org), its "About MEMA" page, and its "Original Equipment Research and Insights" listing page directly. None state a supplier/member count with a definition of what is included. A search snippet (not independently verified, so excluded from the table below) claimed OESA has "430-member companies," attributed to an idealist.org nonprofit-directory page describing OESA, not to MEMA/OESA itself; I could not confirm this on any MEMA/OESA-owned page, so I am not reporting it as a verified figure. MEMA's own "About" page states "more than 4.8 million jobs" for the sector, which is an employment claim, not a supplier count, and carries no stated methodology on that page.

**Status**: NOT FOUND (checked mema.org, oesa.org->mema.org redirect, MEMA About page, MEMA OE Research & Insights listing; no verifiable primary-sourced count located).

### 3f. Conexus Indiana supplier count: NOT FOUND

I fetched conexusindiana.com's Advanced Industries Councils page directly. It lists individual member organizations by category (including "Automotive Company") but states no aggregate count or definition anywhere on the page.

**Status**: NOT FOUND (checked conexusindiana.com/all-advanced-industries-councils/ directly).

---

## 4. Indiana: NAICS 3363 establishments by size class, plus IEDC supplier count

### 4a. Establishment counts by size class (County Business Patterns)

**Source**: US Census Bureau, County Business Patterns, state-level complete file.
**URL**: https://www2.census.gov/programs-surveys/cbp/datasets/2023/cbp23st.zip (file `cbp23st.txt`)
**Dataset year**: 2023 (most recent CBP state file; released per Census's June 26, 2025 CBP 2023 press release)
**Source type**: government dataset (primary, Census Bureau)
**Scope as published**: **establishments only** (CBP does not publish a "firms"/enterprise count at this level; that's a SUSB-only concept), Indiana (FIPS 18), all legal forms of organization combined, by establishment (not enterprise) employment-size class.
**Status**: VERIFIED (file fetched directly; note SUSB's own state x 6-digit x size-class cross tab is NOT published at this granularity, see "what could not be found" below; CBP is the correct source for this specific ask)

| NAICS | Description | Total Estabs | <5 | 5-9 | 10-19 | 20-49 | 50-99 | 100-249 | 250-499 | 500-999 | 1000+ |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 3363 | Motor Vehicle Parts Mfg | 281 | 26 | 21 | 30 | 48 | 35 | 47 | 40 | 25 | 9 |
| 3352 | Household Appliance Mfg | 9 | 5 | N | N | N | N | N | N | N | N |
| 333111 | Farm Machinery and Equipment Mfg | 31 | 11 | N | 4 | 10 | N | N | N | N | N |
| 333120 | Construction Machinery Mfg | 17 | 5 | N | 3 | 4 | N | 3 | N | N | N |

"N" = Census suppressed that cell (not disclosable at that size band; the underlying counts still roll up into the published Total Estabs). Verbatim source row for 3363 (raw CSV line, fields renamed for readability): `fipstate=18, naics=3363//, lfo=-, est=281, n<5=26, n5_9=21, n10_19=30, n20_49=48, n50_99=35, n100_249=47, n250_499=40, n500_999=25, n1000=9`.

### 4b. Indiana NAICS 3363: firms, establishments, and value of shipments (Economic Census, cross-check)

**Source**: US Census Bureau, 2022 Economic Census, Manufacturing Summary Statistics table EC2231BASIC.
**URL**: https://www2.census.gov/programs-surveys/economic-census/data/2022/sector31/EC2231BASIC.zip
**Dataset year**: 2022
**Source type**: government dataset (primary, Census Bureau; quinquennial Economic Census, not an annual survey)
**Status**: VERIFIED (file fetched directly)

Verbatim data row (Indiana, NAICS 3363): FIRM=251, ESTAB=291, RCPTOT=$27,749,361 thousand (= **$27.75 billion**), EMP=61,306, YEAR=2022.

Note the Economic Census firm/establishment counts for Indiana (251 firms / 291 establishments, 2022) differ modestly from the CBP establishment count above (281 establishments, 2023) because they are different surveys, different years, and use somewhat different disclosure/collection rules; both are legitimate primary counts, just not directly poolable.

### 4c. IEDC supplier count

Already covered in 3d above: "500+ AUTOMOTIVE PARTS SUPPLIERS," undated IEDC infographic, no stated definition, Dun & Bradstreet November 2020 sourcing note attached to an adjacent list rather than clearly to this figure. Reported here again because item 4 asks for it directly.

---

## 5. NAICS 3363: value of shipments, latest available (Economic Census, since ASM was discontinued)

**Source**: US Census Bureau, 2022 Economic Census, Manufacturing Summary Statistics table EC2231BASIC.
**URL**: https://www2.census.gov/programs-surveys/economic-census/data/2022/sector31/EC2231BASIC.zip
**Dataset year**: 2022
**Source type**: government dataset (primary, Census Bureau)
**Status**: VERIFIED (file fetched directly)

Verbatim data row (United States, NAICS 3363, GEOTYPE=01): FIRM=3,814, ESTAB=4,846, RCPTOT=$278,236,415 thousand (= **$278.24 billion**), YEAR=2022.

Note on why this is Economic Census rather than ASM: the Annual Survey of Manufactures was discontinued after survey year 2021 (its data collection ended in late 2022); the Census Bureau folded ASM-type content into a new Annual Integrated Economic Survey (AIES) starting with 2023 as the reference year. I did not verify a specific published 2023 AIES value-of-shipments figure for NAICS 3363 (see below); the 2022 Economic Census is itself the more authoritative source for this specific data point regardless (Economic Census is the benchmark that ASM/AIES estimates are built to track between quinquennial years), so I used it directly rather than chase the newer, less-established AIES series.

Also note: national firm/establishment counts differ slightly between this Economic Census table (3,814 firms / 4,846 establishments) and the SUSB 2022 table in Section 1 (3,616 firms / 4,640 establishments) for the same year and NAICS code. This is a known, documented difference in how the two Census products construct their business universe (SUSB is built from the Business Register combining CBP and nonemployer data with its own disclosure-avoidance noise; the Economic Census counts are drawn from actual census responses/administrative records with a different edit and imputation process). I am reporting both, not reconciling them, per the instruction not to estimate silently.

---

## What could not be found and why

1. **A published SUSB cross-tab of state x 6-digit NAICS x enterprise employment size class.** I initially expected the SUSB "detailed sizes" file to give Indiana's NAICS 3363 by employment-size class directly (which is what "SUSB ... and/or CBP" in the prompt anticipated might work). On inspection, SUSB's state-level rows in that file only go down to roughly sector level; the full enterprise-size-class breakdown by detailed NAICS exists only for the US total. I substituted CBP's state file (Section 4a), which publishes establishment-level (not enterprise-level) size classes by state and 6-digit NAICS, and is explicit about the difference (establishment vs. enterprise size class) in its own field documentation.

2. **A verified MEMA/OESA supplier count with a stated method.** Checked mema.org, the oesa.org->mema.org redirect, MEMA's About page, and its OE Research & Insights listing directly; none publish a member/supplier count with a stated scope. A "430-member companies" figure appeared in a search snippet sourced to a third-party nonprofit directory (idealist.org), not to MEMA/OESA itself, so I excluded it rather than report an unverified number.

3. **A verified Conexus Indiana automotive supplier count.** Checked conexusindiana.com's Advanced Industries Councils page directly; it lists member companies by name/category with no aggregate count or definition anywhere on the page.

4. **An automotive-specific national or Indiana supplier count with an explicit, current, and public methodology.** The closest things found are: (a) CAR's 2010 report, which has a genuinely stated cross-NAICS method but reports employment (not a count of firms/establishments) and is built on 2002-2007 vintage data; (b) BEA's 2017 detail-level Use table, from which I computed direct-purchase shares myself (arithmetic shown in 3b) but which has no establishment-count dimension at all and cannot see multi-tier (indirect) supply relationships; (c) IEDC's undated "500+" infographic figure, which is marketing collateral with no stated definition of "supplier." None of the three is a rigorous, current, methodologically transparent count of the Tier-2/Tier-3 automotive supplier universe outside NAICS 3363; that number does not appear to exist in a citable primary or clearly-methodological form as of this search. Any figure combining these into a single "Tier-2/3 automotive supplier count" would be my own estimate stacked on mismatched vintages and units (employment vs. establishments vs. dollars), which the brief explicitly instructs against; I have not produced one.

5. **2023 Annual Integrated Economic Survey (AIES) value-of-shipments figure for NAICS 3363.** Not pursued once the 2022 Economic Census figure (Section 5) was in hand, since it is the more authoritative of the two for this specific year and the AIES is a newly-launched survey series I did not have time to verify against a primary AIES table within this session's scope. Flagging as unexplored rather than silently omitting it.
