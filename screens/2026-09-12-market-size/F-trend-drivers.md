# F. Trend drivers: US automotive (and appliance / heavy equipment) supplier quality chargebacks

Research date: 2026-09-13. Scope per instructions: chargebacks only (sorting, line-down, premium freight, rework, recall/warranty cost recovery deducted from supplier receivables). No subagents used; every fetch below was done directly and read, not taken from a search-engine summary unless explicitly marked "search summary only" (which is then NOT VERIFIED per rule 4). Excluded per instructions: `predictions/`, Census business-count files.

Convention: dollar figures are nominal unless marked "real" / inflation-adjusted. A verbatim quote is given wherever the source is prose; for tables pulled from PDFs/APIs, the raw values are given instead since there is no sentence to quote.

---

## A. US light vehicle production (assemblies)

Publisher: Federal Reserve Board, G.17 Industrial Production release, series MVATOTASSS ("Motor Vehicle Assemblies: Total Motor Vehicle Assemblies"), distributed via FRED. Units: millions of units, seasonally adjusted annual rate (SAAR), monthly. No single published "annual total assemblies" table was located from the Fed itself in machine-readable form in this session (the G.17 PDF could not be parsed, see "not found" below), so the annual figures below are **my own arithmetic mean of the 12 published monthly SAAR values for each year**, computed from the full monthly series fetched directly from FRED. This is disclosed as a calculation, not a Fed-published annual figure.

| Year | Value (avg. monthly SAAR, millions of units) | Source type | URL | Date fetched | VERIFIED/NOT |
|---|---|---|---|---|---|
| 2015 | 12.09 | Primary (Fed/FRED), my average | https://fred.stlouisfed.org/series/MVATOTASSS | 2026-09-13 | VERIFIED (raw monthly data) |
| 2016 | 12.09 | Primary (Fed/FRED) | same | 2026-09-13 | VERIFIED |
| 2017 | 11.13 | Primary (Fed/FRED) | same | 2026-09-13 | VERIFIED |
| 2018 | 11.30 | Primary (Fed/FRED) | same | 2026-09-13 | VERIFIED |
| 2019 (pre-pandemic baseline) | 10.89 | Primary (Fed/FRED) | same | 2026-09-13 | VERIFIED |
| 2020 | 8.85 | Primary (Fed/FRED) | same | 2026-09-13 | VERIFIED |
| 2021 | 9.17 | Primary (Fed/FRED) | same | 2026-09-13 | VERIFIED |
| 2022 | 10.00 | Primary (Fed/FRED) | same | 2026-09-13 | VERIFIED |
| 2023 | 10.72 | Primary (Fed/FRED) | same | 2026-09-13 | VERIFIED |
| 2024 | 10.55 | Primary (Fed/FRED) | same | 2026-09-13 | VERIFIED |
| 2025 | 10.29 | Primary (Fed/FRED) | same | 2026-09-13 | VERIFIED |
| 2026 YTD (Jan-Jul, 7 months, not annualized) | 10.60 | Primary (Fed/FRED) | same | 2026-09-13 | VERIFIED |

Read: assemblies never returned to the 2015-2016 level (~12.1M) even before COVID; 2019 was already down to 10.9M. The 2020 COVID collapse (as low as 0.09M SAAR in April 2020) and the 2021-2022 chip shortage kept output below 10M for three straight years. 2023-2026 sit in a 10.0-10.7M band, still roughly 12% below 2015-2016 and about flat versus 2019. This is a declining-to-flat production base, which matters because chargeback dollars often scale with unit volume through parts flow even if per-unit or per-defect chargeback rates are rising.

Corroborating but NOT independently fetched (search-summary only, flagged per rule 4): S&P Global Mobility (Mobility Global, formerly S&P Global Mobility/Wards Intelligence) August 2026 monthly forecast commentary, fetched directly, states North America 2026 production was "revised up by 22,000 units for 2026 and 224,000 units for 2027," and describes North America as "resilient" (https://www.mobilityglobal.com/en-us/automotive-insights/blog/2026-light-vehicle-production-forecast, dated 18 August 2026, author Mike Wall). This is a revision to a prior forecast, not an absolute annual production level, so it is directional corroboration only. VERIFIED as a quote; NOT a production total.

NOT VERIFIED / NOT FOUND: An OICA (International Organization of Motor Vehicle Manufacturers) US total production table for 2015-2025 was searched but the OICA production-statistics page would not render its data tables through automated fetch in this session; secondary citations (thedailyautomotive.com, visual-nerd.com) reported US 2023 ~10.6M and 2024 ~10.56M total vehicles via OICA, but I could not open OICA's own table to verify these numbers directly, so they are NOT VERIFIED. The Fed G.17 PDF itself (https://www.federalreserve.gov/releases/g17/current/g17.pdf) returned corrupted/uncompressed stream data to the fetch tool and could not be read; the FRED series above was used instead as the equivalent primary data.

---

## B. Census value of shipments, NAICS 3363 (Motor Vehicle Parts Manufacturing)

Source: U.S. Census Bureau Economic Census, table EC1731BASIC (2017) and EC2231BASIC (2022), pulled directly from the Census Bureau's own data API (data.census.gov), NAICS code 3363, geography = United States. RCPTOT = "Total value of shipments and receipts," reported in thousands of dollars in the raw data (converted to $ below).

| Year | Value of shipments (RCPTOT), nominal | Establishments | Employment | Annual payroll | Source type | URL | Date | VERIFIED |
|---|---|---|---|---|---|---|---|---|
| 2017 | $261.32 billion | 4,991 | 581,858 | $31.02 billion | Primary (Census Economic Census) | https://data.census.gov/table/ECNBASIC2017.EC1731BASIC (data pulled via data.census.gov/api/access/data/table, id=ECNBASIC2017.EC1731BASIC) | 2026-09-13 | VERIFIED (raw API JSON read directly) |
| 2022 | $278.24 billion | 4,846 | 575,338 | $33.20 billion | Primary (Census Economic Census) | https://data.census.gov/table/ECNBASIC2022.EC2231BASIC | 2026-09-13 | VERIFIED (raw API JSON read directly) |

Nominal change 2017 to 2022: +6.47%. Over the same period, BLS CPI-U (FRED series CPIAUCNS, annual average of the 12 published monthly index values, computed directly by me from the raw series) rose from 245.12 (2017 average) to 292.66 (2022 average), a **+19.4% increase**. That means the value of shipments for NAICS 3363 **fell by roughly 10.8% in real (inflation-adjusted) terms** between the two Economic Census years, despite a nominal increase. This is exactly the kind of "number that jumps without a stated cause" the instructions ask to flag: the nominal figure alone would read as growth; deflated, it is a real decline. Employment and establishment counts also fell slightly over the same window (Census counts of establishments are explicitly excluded from my count per instructions; these are shown only because the Economic Census report bundles them with the shipments figure).

The Census Bureau's own ASM (Annual Survey of Manufactures) years between 2017 and 2022, and any 2023 AIES (Annual Integrated Economic Survey, the ASM's successor) release, could not be pulled for NAICS 3363 specifically in this session (see NOT FOUND below).

As an annual, NAICS-3363-specific cross-check between Economic Census years, the BEA/BLS Integrated Industry-Level Production Account "sectoral output" series for NAICS 3363 (a gross-output concept, methodologically related to but not identical with Census "value of shipments") gives a full annual time series:

| Year | Sectoral output, NAICS 3363, nominal $ millions | Source type | URL | Date | VERIFIED |
|---|---|---|---|---|---|
| 2015 | 235,871 | Primary (BEA/BLS via FRED, series IPUEN3363T300000000) | https://fred.stlouisfed.org/series/IPUEN3363T300000000 | 2026-09-13 | VERIFIED |
| 2016 | 235,713 | same | same | same | VERIFIED |
| 2017 | 235,380 | same | same | same | VERIFIED |
| 2018 | 244,186 | same | same | same | VERIFIED |
| 2019 | 234,453 | same | same | same | VERIFIED |
| 2020 | 201,584 | same | same | same | VERIFIED |
| 2021 | 219,452 | same | same | same | VERIFIED |
| 2022 | 252,570 | same | same | same | VERIFIED |
| 2023 | 266,023 | same | same | same | VERIFIED |
| 2024 | 263,480 | same | same | same | VERIFIED |
| 2025 | 259,934 | same | same | same | VERIFIED |

Note this series is NOT the Census "value of shipments" (it is gross output from BEA/BLS's integrated production accounts), so treat the 2017 ($235.4B) and 2022 ($252.6B) figures here as a different, though closely related, measuring stick than the Economic Census RCPTOT figures above; they are not meant to be summed or reconciled to each other, only compared directionally. On this series, 2023-2024 nominal output is the highest in the 1987-2025 history of the series, but 2025 dipped from 2024.

A second, broader corroborating series: Census's own monthly M3 survey (Manufacturers' Shipments, Inventories, and Orders), series AMVPVS, "Manufacturers' Value of Shipments: Motor Vehicles and Parts" (this groups NAICS 3361 vehicles + 3363 parts together, excluding 3362 bodies/trailers, and is seasonally adjusted, nominal $ millions). Annual sums (mine, from the published monthly SA figures):

| Year | Annual sum, $ millions (nominal) | Source | URL | VERIFIED |
|---|---|---|---|---|
| 2015 | 638,950 | Census M3 via FRED (AMVPVS) | https://fred.stlouisfed.org/series/AMVPVS | VERIFIED |
| 2017 | 633,229 | same | same | VERIFIED |
| 2019 | 660,499 | same | same | VERIFIED |
| 2020 | 575,836 | same | same | VERIFIED |
| 2022 | 740,503 | same | same | VERIFIED |
| 2024 | 784,921 | same | same | VERIFIED |
| 2025 | 796,493 | same | same | VERIFIED |
| 2026 (Jan-Jul only, not annualized) | 504,820 | same | same | VERIFIED |

This combined-vehicles-and-parts series shows steadier nominal growth than the 3363-only series (+24.6% 2015 to 2025), but again, cumulative CPI-U over that decade is well above 24.6%, so this too reads as roughly flat-to-down in real terms; I have not computed the full-decade CPI figure precisely (only the 2017-2022 comparison above was computed) so I am not asserting a precise real-terms number here, only flagging the direction.

NOT FOUND: A clean ASM (2018-2021) or AIES (2023) value-of-shipments figure specific to NAICS 3363. The Census Bureau's API requires a registered key for the ecnbasic/asm endpoints when queried directly (api.census.gov returned "A valid key must be included with each data API request" to an unauthenticated call), and data.census.gov's own browser-facing API (which does not require a key) only exposed ECNBASIC (Economic Census) tables for 2017 and 2022 in the session; the equivalent ASM table IDs for 2018-2021 were not identified in the time available. This is marked NOT FOUND rather than estimated.

---

## C. NHTSA recalls

Source: NHTSA 2025 Annual Report Safety Recalls, published March 2026 (the most current annual report; it contains a full 2005-2025 time series, so the 2024 report was not separately needed). PDF fetched and parsed directly in-browser with pdf.js (Akamai/edge WAF blocked direct curl/WebFetch access to nhtsa.gov; the Browser tool's own fetch, run from the rendered page, was not blocked). URL: https://www.nhtsa.gov/sites/nhtsa.gov/files/2026-03/2025-annual-recalls-report.pdf

Two internal NHTSA tables matter here: the "Vehicle Recall Summary by Year" (light-vehicle recalls, i.e., what the report's own headline chart uses and explicitly says "excludes recalls related to tires, child seats, and equipment") and the "Equipment Recall Summary by Year" (aftermarket/equipment-supplier-attributed recalls, a distinct NHTSA category). The equipment table is the closest direct NHTSA-published proxy for "recalls attributed to equipment/supplier defects"; NHTSA does not publish a single sentence stating a supplier-defect percentage, so the percentages below are my own arithmetic (equipment recalls / all recalls, both from NHTSA's own published counts, TOTAL column, Defect+Compliance combined).

| Year | Vehicle-only recalls (#) | Vehicles affected (vehicle-only) | Equipment-only recalls (#) | Vehicles/units affected (equipment-only) | All recalls (#, all 4 categories) | Equipment recalls as % of all recalls (my calc) | VERIFIED |
|---|---|---|---|---|---|---|---|
| 2015 | 862 | 49,856,960 | 91 | 35,792,219 | 970 | 9.4% | VERIFIED |
| 2016 | 919 | 50,196,715 | 91 | 25,303,256 | 1,031 | 8.8% | VERIFIED |
| 2017 | 810 | 30,728,178 | 72 | 10,553,117 | 897 | 8.0% | VERIFIED |
| 2018 | 912 | 29,522,841 | 110 | 8,542,590 | 1,033 | 10.6% | VERIFIED |
| 2019 | 880 | 38,597,607 | 71 | 14,393,658 | 963 | 7.4% | VERIFIED |
| 2020 | 784 | 31,838,229 | 85 | 24,320,668 | 883 | 9.6% | VERIFIED |
| 2021 | 987 | 28,879,609 | 91 | 4,976,947 | 1,093 | 8.3% | VERIFIED |
| 2022 | 932 | 31,038,367 | 97 | 735,532 | 1,050 | 9.2% | VERIFIED |
| 2023 | 894 | 34,826,172 | 94 | 4,271,800 | 1,000 | 9.4% | VERIFIED |
| 2024 | 950 | 29,365,837 | 109 | 3,677,600 | 1,073 | 10.2% | VERIFIED |
| 2025 | 891 | 29,262,623 | 82 | 1,115,572 | 997 | 8.2% | VERIFIED |

All figures above are read directly off NHTSA's own "All Recalls Summary by Year," "Vehicle Recall Summary by Year," and "Equipment Recall Summary by Year" tables (report pages 15-17). Read: total recall count is roughly flat/cyclical across the decade (883 to 1,093 per year, no clear trend), and equipment-attributed recalls (the closest NHTSA category to "supplier/equipment defect") bounce around 7-11% of all recalls with no clear directional trend either up or down; 2025's 8.2% is mid-range, not a new high or low.

Electric-vehicle-specific recalls (a subset, page 3 of the same report, NHTSA's own chart): 2021: 15 recalls / 150,364 vehicles; 2022: 26 / 1,279,897; 2023: 44 / 428,394; 2024: 46 / 2,481,247; 2025: 71 / 1,027,524. Source: same PDF, page 3. VERIFIED. Read: EV-specific recall counts have risen every year since 2021 even as EV sales growth stalled in 2025 (see Section E), consistent with a still-maturing, higher-defect-rate technology base.

NOT FOUND as a direct NHTSA statement: any sentence in the report where NHTSA itself states a percentage of recalls "caused by" or "attributed to" supplier/equipment defects. The equipment-recall percentage above is my own division of NHTSA's own published counts, not a quoted NHTSA claim, and is labeled as such.

---

## D. Warranty (Warranty Week)

Source: Warranty Week (warrantyweek.com), a paid industry newsletter that aggregates 10-K/10-Q warranty accrual and claims-paid disclosures across automakers and suppliers. Fetched directly, verbatim quotes below.

| Year | Metric | Value | Source type | URL | Date published | VERIFIED |
|---|---|---|---|---|---|---|
| 2024 | Global automaker warranty accruals (40 OEMs, 35 full reporters + 5 estimated) | "$72.5 billion... an 11% increase from 2023" | Trade press / industry newsletter | https://www.warrantyweek.com/archive/ww20251030.html | 2025-10-30 | VERIFIED (verbatim quote confirmed) |
| 2025 | US auto parts & powertrain suppliers: claims paid | $2.18 billion | Trade press | https://www.warrantyweek.com/archive/ww20260604.html | 2026-06-04 | VERIFIED |
| 2025 | US auto parts & powertrain suppliers: accruals | $2.09 billion | same | same | 2026-06-04 | VERIFIED |
| 2025 | US auto parts & powertrain suppliers: reserves held | $4.94 billion | same | same | 2026-06-04 | VERIFIED |
| 2024 to 2025 | Supplier claims, accruals, reserves | "Total warranty claims, accruals, and reserves all increased for the auto parts manufacturers from 2024 to 2025." | same | same | 2026-06-04 | VERIFIED (verbatim) |
| 2022 | Powertrain suppliers: claims paid / accruals | $974 million / $904 million | Trade press | https://www.warrantyweek.com/archive/ww20230413.html | 2023-04-13 | VERIFIED |
| 2022 | Other (non-powertrain) parts suppliers: claims paid / accruals | $798 million / $827 million | same | same | 2023-04-13 | VERIFIED |
| 2019 (H1 only) | All auto parts suppliers, claims, first half | "claims are up to $926 million, an astonishing 18% increase over the first half of 2018" | Trade press | https://www.warrantyweek.com/archive/ww20190912.html | 2019-09-12 | VERIFIED (verbatim) |
| 2019 (H1) | Powertrain suppliers' share of total supplier claims | "their share of the total is now approaching 60%, when it had been roughly half-and-half as recently as 2015" | same | same | 2019-09-12 | VERIFIED (verbatim) |
| 2015 | Non-powertrain ("other") suppliers, claims paid | "The $1.215 billion claims total for the other suppliers in 2015" | Trade press | https://www.warrantyweek.com/archive/ww20160407.html | 2016-04-07 | VERIFIED (verbatim) |
| 2015 | Powertrain suppliers' share of accruals | "just over 40% of the $2.24 billion industry total for accruals came from the powertrain suppliers" (implies ~$896M powertrain / ~$1.34B other, on a $2.24B total) | same | same | 2016-04-07 | VERIFIED (verbatim) |

Read: warranty claims and accruals (a related but distinct cost category from chargebacks: warranty is what OEMs pay/reserve for field failures; chargeback/warranty-recovery is what gets debited back to a supplier) have grown steadily in dollar terms across the whole 2015-2025 window, for both OEMs and suppliers, with no down years reported in the sources fetched. Within the supplier group, powertrain suppliers (engine/transmission/driveline) have taken a rising share of total supplier warranty cost (roughly 50% in 2015 to "approaching 60%" by mid-2019), while "other" (non-powertrain) suppliers' share has been "slowly shrink[ing]" per Warranty Week's own language (2023-04-13 article, quoted in Section E's search evidence). This is a warranty-cost trend, not a chargeback-count or chargeback-dollar trend; I did not find a source that reports supplier chargeback dollars as its own tracked series (see Section G).

NOT VERIFIED (search-summary only, not independently fetched and confirmed in full): a claim that in 2018 powertrain suppliers paid $911 million and other suppliers paid $708 million in full-year claims; this number appeared in a search-engine summary of the ww20190912.html page but was not present in the verbatim text returned when I fetched that page directly (the fetch returned H1 2018 vs H1 2019 comparisons, not full-year 2018 figures). Marked NOT VERIFIED rather than repeated as fact.

---

## E. Electric vehicles

### E1. Current US EV adoption pace (2025-2026)

| Period | EV share of new light-vehicle sales | Units | Source type | URL | Date | VERIFIED |
|---|---|---|---|---|---|---|
| Full-year 2024 | 8.1% | ~1.30 million | Cox Automotive (Kelley Blue Book brand) | https://www.coxautoinc.com/insights/q4-2025-ev-sales-report-commentary/ | fetched 2026-09-13 (article dated post-2025) | VERIFIED |
| Full-year 2025 | 7.8% ("the second-best year on record for EV sales in the U.S.") | ~1.29 million (described as "just shy of 2024's 1.30 million," down 2% YoY) | Cox Automotive | same | same | VERIFIED (verbatim) |
| Q3 2025 (peak) | 10.6% | n/a | Cox Automotive | https://www.coxautoinc.com/insights/q1-2026-ev-sales-report-commentary/ | fetched 2026-09-13 | VERIFIED (verbatim: "well below the peak of 10.6% in Q3 2025") |
| Q4 2025 | 5.8% | n/a | Cox Automotive | same | same | VERIFIED |
| Q1 2026 | 5.8% ("unchanged from Q4 2025") | 216,399 ("lower by 7.8% compared to the previous quarter"; "fell by 27% year over year") | Cox Automotive | same | same | VERIFIED (verbatim) |

Read: US EV adoption did not just slow, it reversed sharply after the Q3 2025 peak (10.6%), coincident with the removal of federal EV purchase incentives at the start of October 2025 (per Cox Automotive's own framing, "government-backed sales incentives revoked at the start of October," found in the Q4 2025 article). By Q1 2026 the share (5.8%) was roughly half the Q3 2025 peak and below full-year 2024/2025 averages. This directly affects the "EVs reduce chargeback-generating parts count" driver: the pace of the transition that would erode ICE-specific supplier content (engines, transmissions, exhaust, fuel systems) has slowed materially in the US market over the last four fetched quarters, even though the multi-year direction (more EV models, more parts consolidation) is intact.

### E2. Parts/supplier content impact of EV transition

| Claim | Detail | Source type | URL | Date | VERIFIED |
|---|---|---|---|---|---|
| Fewer moving parts in EV powertrains | "the electric motor had three moving parts, compared to an ICE's 113" | Secondary reporting citing industry/Deloitte-style analysis | via Roll Call (see below) / general search, not independently re-fetched at primary source | n/a | NOT VERIFIED at primary source (only via search-summary and Roll Call's own framing) |
| Parts suppliers 2023 sales, SEMA aftermarket segment | "$52 billion" in sales; "$337 billion" economic output; EVs "~10%" of 15M+ annual US sales as of the article's writing | Trade press, quoting SEMA CEO Mike Spagnola, Alliance for American Manufacturing president Scott Paul, U-M EV Center director Alan Taub | https://rollcall.com/2024/05/29/auto-parts-suppliers-fear-a-crash-with-shift-to-evs/ | 2024-05-29 | VERIFIED (verbatim quotes and figures as reported by Roll Call) |
| "is naturally going to change things up" (fewer parts under EVs) | Direct quote, Scott Paul, Alliance for American Manufacturing | same | same | 2024-05-29 | VERIFIED (verbatim) |
| Global Automotive Supplier Study 2025: EV-related margin/cost strain on electronics suppliers | "growing amount of content demanded by OEMs has been offset by significant R&D expenditures, increasing costs of electronic parts, and high product launch expenses" | Primary industry study (Roland Berger / Lazard) | https://www.rolandberger.com/en/Insights/Publications/Global-Automotive-Supplier-Study-2025.html | 2025-05-02 | VERIFIED (verbatim) |
| Supplier concern over future EV-propulsion sourcing constraints | 29% of surveyed OE suppliers rate EV propulsion a "Significant Concern" for future sourcing constraints (2nd only to semiconductors) | Primary trade-association survey (MEMA), n=104 respondents | https://www.mema.org/system/files/Q4%202025%20MEMA%20Supplier%20Barometer%20-%20Supply%20Chain%20Globalization%20Sustainability-Final-No%20appx.pdf | 2026-01-29 (Q4 2025 data) | VERIFIED (read directly from PDF, page 14) |

McKinsey's "Work the core: how auto suppliers can get fit for the EV transition" was located by search but the page failed to load (two 60-second timeouts) in this session; its widely cited claims (fewer engine/transmission combinations under EV, 3-4 vs 10-20 for ICE) are NOT VERIFIED here because I could not fetch and read the primary page myself. PwC's "Merge ahead" EV supply-chain page returned HTTP 403 and was also NOT VERIFIED.

---

## F. Tariffs and cost pressure 2025-2026

| Claim | Detail | Source type | URL | Date | VERIFIED |
|---|---|---|---|---|---|
| MEMA tariff exposure survey (n=139 supplier-member respondents, March 6-10, 2025) | "78% of supplier respondents are exposed to steel tariffs, while 63% are exposed to aluminum tariffs." "Over 80% of suppliers are exposed to steel and aluminum derivative tariffs..." "97% of supplier respondents expressed concerns about increased distress among sub-tier suppliers due to the announced tariffs." "78% of suppliers reported that they do not have excess available capacity in the U.S. to domestically manufacture parts currently sourced through global supply chains." | Primary (trade association, named survey, named spokesperson) | https://www.mema.org/news/mema-statement-ongoing-impact-steel-and-aluminum-tariffs | 2025-03-12 | VERIFIED (verbatim, fetched directly) |
| Named executive quote | Bill Long, MEMA President and CEO: "As an industry, we recognize the importance of strong domestic supply chains... it is essential that trade policies allow suppliers to remain competitive in a global market." | same | same | 2025-03-12 | VERIFIED (verbatim) |
| MEMA OE Supplier Barometer Index (SBI), Q4 2025 (n=104) | "Q4 SBI Score = 44; up from Q3 level of 39... the fifteenth straight quarter of building pessimism." Cost pressure diffusion index (>50 = accelerating): "Costs" = 91 (12-month change) / 75 (1-month change), the highest of all measured indicators (new orders, production, employment, etc., all in the 30s-50s range). | Primary (trade association survey) | https://www.mema.org/system/files/Q4%202025%20MEMA%20Supplier%20Barometer%20-%20Supply%20Chain%20Globalization%20Sustainability-Final-No%20appx.pdf | 2026-01-29 | VERIFIED (read directly from PDF pages 2, 5, 8) |
| Supplier distress / watch-list trend | "Suppliers face renewed supplier distress brought on by weakening financial metrics arising from tariff pressure, and while the percentage of direct material suppliers on a 'watch' list rose only 50 bps from 2024, it ends a 3-year streak of improvement." Watch-list reasons (2025, % of respondents): financial metrics 48%, delivery performance 35%, capacity constraints 10%, quality 6%, management-related 0%. | same | same | 2026-01-29 | VERIFIED (verbatim + table, PDF pages 3, 12) |
| Named supplier comment on OEM tariff-cost-recovery disputes (anonymized respondent, MEMA survey free-text) | "Despite 'agreements' with OEMS for tariff recovery at different levels, [Two OEMS] differ and delay resulting in very little money coming in." | Primary (trade association survey verbatim respondent comment) | same | 2026-01-29 | VERIFIED (verbatim, PDF page 13) |
| Reshoring/localization | "On average, the percentage of North American produced products made in the U.S. rose 6 ppts. from last year to 73%, while Mexico made products fell 13 ppts to 24%." "Customers are producing more locally (77% responding at least minimal increase)... suppliers are running into labor/talent, cost and capacity issues in their localization efforts, coupled with customers' being unwilling to pay for local content." | same | same | 2026-01-29 | VERIFIED (verbatim, PDF page 3) |
| Marelli Holdings Chapter 11 (major Tier 1 supplier to Stellantis, Nissan, Tesla) | Filed June 2025. CEO David Slump cited "industry-wide market pressures," COVID-19 aftermath, and global tariffs; tariffs "severely affected" the company's import/export-dependent model. Over $700M unsecured debt restructuring; $1.1B DIP financing; largest unsecured creditors Stellantis ($454M) and Nissan ($313M). | Trade/business press | https://www.cbtnews.com/tariffs-debt-push-stellantis-and-nissan-supplier-into-bankruptcy/ | 2025-06-13 | VERIFIED (fetched directly) |
| First Brands Group Chapter 11 (Raybestos, Centric, Cardone, Autolite, FRAM) | Filed September 28, 2025. Reason, per direct fetch: "weeks of turmoil sparked by creditor concern" over "opaque off-balance sheet financing," ~70% of revenue processed through factoring, and a paused refinancing that triggered a quality-of-earnings review. Liabilities $10-50B range; DIP financing $1.1B. **Tariffs are not mentioned as a cause in this source.** | Trade press | https://www.ttnews.com/articles/first-brands-bankruptcy-parts | 2025-09-29 | VERIFIED (verbatim; explicitly checked for and did not find a tariff linkage) |
| First Brands US government tariff claim | A separate, later claim that the U.S. government filed a "$286 million tariff claim" against First Brands over alleged import-duty underpayment | Trade press (search-summary only; the mdm.com source page returned HTTP 403 on direct fetch and could not be independently confirmed) | https://www.mdm.com/news/top-distributor-sectors/automotive/u-s-government-files-286m-tariff-claim-against-bankrupt-auto-parts-supplier-first-brands/ | reported ~2025-2026 | NOT VERIFIED |
| Global Automotive Supplier Study 2025 (Roland Berger + Lazard) | "Global EBIT margins were 5.3% in 2021 and 2023, two percentage points lower than in 2016/17" (a ~25% relative decline). "More than 40% of the 25 largest automotive suppliers by market capitalization are now rated as non-investment grade." Chinese suppliers 5.7% EBIT margin (2024) vs. European 3.6%, South Korean 3.4%. | Primary industry study | https://www.rolandberger.com/en/Insights/Publications/Global-Automotive-Supplier-Study-2025.html | 2025-05-02 | VERIFIED (verbatim) |
| Bain Automotive Profitability dashboard | Q4 2025: OEM EBIT margin 3.6% (down 60%+ from 2021 peak; full-year 2025 average 2.7%); supplier EBIT margin 6.9%, "sixth consecutive quarter outperforming OEMs." Historical baseline: "For two decades leading up to 2019, automotive suppliers' EBIT margins were on average 1 to 2 percentage points higher than those of original equipment manufacturers." "Many are expanding performance and cost-reduction programs to protect profitability, initiatives that are increasingly felt by suppliers." | Primary (Bain analysis on S&P Capital IQ data) | https://www.bain.com/insights/automotive-profitability-how-oem-and-supplier-margins-are-faring-interactive/ | dashboard dated 2026-05-21 | VERIFIED (verbatim) |

Read: this is the strongest and most current (2025-2026) evidence in the whole file. Tariffs are named as the #1 industry threat in MEMA's own Q4 2025 survey, cost-pressure is the fastest-accelerating indicator MEMA tracks, two major Tier 1 suppliers filed Chapter 11 in 2025 (one explicitly tariff-linked, one explicitly not), and OEMs are running "cost-reduction programs" that Bain's own dashboard says are "increasingly felt by suppliers." A verbatim supplier comment inside the MEMA survey directly describes OEMs delaying and shorting agreed tariff-cost-recovery payments, i.e., a live, named-in-substance (if not named-by-company) dispute over cost recovery from OEM to supplier, which is structurally the same mechanism as a chargeback dispute even though the underlying cost driver here is tariffs rather than a quality defect.

---

## G. Direct statements on whether chargebacks / quality-cost recovery are rising or falling

This is the section the task explicitly wants isolated and flagged for vendor bias. Findings:

| Source | What it says | Type | URL | Date | VERIFIED |
|---|---|---|---|---|---|
| Dealership Guy (newsletter, citing "Warranty Weekly / Xtime / Cox Automotive" as its own sourcing) | "OEMs are now asking these suppliers to cover more of the repair costs under warranty," a shift from "how it used to work when OEMs often just paid the claim themselves." Cites suppliers covering "$2B" in repairs in 2024 (up 3% YoY) and setting aside "$4.7B more for future claims" (up 6%). Quotes a named dealer service manager, Brian Bradley: "My dealerships have had a massive uptick since the beginning of the year (like 60-80%), while our customer pay is decreasing because of our obligation to the manufacturer." | Trade/industry journalism (not a vendor selling chargeback software; treated as independent) | https://news.dealershipguy.com/p/surging-warranty-costs-are-pressuring-dealer-profits-and-top-operators-aren-t-waiting-to-adapt-2025 | 2025-07-22 | VERIFIED (verbatim); direction stated: **increasing** |
| MOTOR magazine / MAPconnected ("Supplier Recovery Models: Industry Benchmark") | Describes a "benchmarking discussion" naming Ford, GM, Stellantis, Volkswagen, Cummins, Kia, and Logisnext Americas discussing supplier-recovery methodology, but explicitly does **not** state whether recovery activity itself is trending up, down, or flat. | **Vendor marketing.** MAPconnected sells supplier-recovery/warranty-recovery software; this article is its own content placed in a trade magazine. Labeled as such per instructions; treated as NOT evidence of trend direction, only as confirmation that named OEMs are actively running supplier-recovery programs. | https://www.motor.com/2026/07/supplier-recovery-models-industry-benchmark/ | 2026-07-07 | VERIFIED as a source, but explicitly gives no trend direction; and its content is vendor-authored |
| Claimlane blog ("Supplier Chargebacks: Recover Warranty Costs") | General claims that suppliers "lose 1-2% of annual revenue" to chargebacks and that "5-15% of supplier invoices face some form of retailer chargeback deduction." | **Vendor marketing.** Claimlane sells warranty/chargeback-recovery software. No year-over-year trend data, no named source for the percentages. | https://www.claimlane.com/resources/blog/supplier-chargebacks-recovering-warranty-costs | undated | NOT VERIFIED as evidence; labeled vendor marketing per instructions |
| Chargeflow blog ("Supply Chain Chargeback Management: 5 Effective Tips for 2026") | General chargeback-management advice content. | **Vendor marketing.** Chargeflow is an e-commerce/retail chargeback-dispute automation vendor; this content is generic and not automotive-specific. | https://www.chargeflow.io/blog/supply-chain-chargeback | undated | NOT VERIFIED as evidence; labeled vendor marketing |
| WarrantyHub blog ("Warranty Supplier Recovery: How Manufacturers Recoup Supplier Costs") | General claim that "most manufacturers never collect most of the recoverable warranty costs caused by supplier failures." | **Vendor marketing.** WarrantyHub sells warranty-recovery software. | https://warrantyhub.com/blog/warranty-supplier-recovery/ | undated | NOT VERIFIED as evidence; labeled vendor marketing |
| MEMA Q4 2025 Supplier Barometer, respondent free-text comment | "Despite 'agreements' with OEMS for tariff recovery at different levels, [Two OEMS] differ and delay resulting in very little money coming in." | Primary (unprompted respondent comment inside a trade-association survey, not vendor content) | https://www.mema.org/system/files/Q4%202025%20MEMA%20Supplier%20Barometer%20-%20Supply%20Chain%20Globalization%20Sustainability-Final-No%20appx.pdf | 2026-01-29 | VERIFIED (verbatim); shows active OEM-supplier friction over cost recovery, though for tariffs specifically, not quality |
| Warranty Week (2023-04-13 article) | "the companies that manufacture powertrain components such as engines and transmissions have seen their share of the warranty expenses rise, while the other parts suppliers have seen their share slowly shrink" | Trade press / industry newsletter (paid research service, not a chargeback-software vendor) | https://www.warrantyweek.com/archive/ww20230413.html | 2023-04-13 | VERIFIED (verbatim); direction stated for the powertrain-vs-other supplier split, not for the aggregate |

No source located in this session, primary or vendor, that publishes an actual time series of automotive supplier chargeback dollars or chargeback counts the way NHTSA publishes recalls or Warranty Week publishes warranty accruals. The evidence on Section G is therefore indirect: warranty-cost-shifting (dealershipguy.com, Warranty Week) and tariff-cost-recovery friction (MEMA survey) both point toward suppliers absorbing more OEM-side cost recovery over 2024-2026, but this is inferred from adjacent, named, dated sources, not from a chargeback-specific published series, and the vendor-marketing sources that talk about chargebacks directly are self-interested and are not being counted as evidence of a trend.

---

## Direction by driver

- **A. Production (assemblies):** Flat-to-down. 2023-2026 averages (10.0-10.7M SAAR) sit below the 2015-2016 level (~12.1M) and roughly at the 2019 pre-pandemic baseline (10.9M). Source: Fed G.17/FRED MVATOTASSS, my calculated annual averages.
- **B. Parts industry value of shipments (NAICS 3363):** Down in real terms, up in nominal terms. Census Economic Census RCPTOT rose nominally +6.5% 2017 to 2022 but CPI-U rose 19.4% over the same span, implying a real decline of roughly 10-11%. Source: Census Economic Census EC1731BASIC/EC2231BASIC via data.census.gov API, and BLS CPI-U via FRED.
- **C. Recalls:** Flat/cyclical, no clear trend. Total recall counts ranged 883-1,093/year over 2015-2025 with no directional drift; the equipment-attributed share (closest NHTSA proxy for supplier-defect recalls) ranged 7.4%-10.6% with no trend either. EV-specific recalls are the one sub-category that rose every year 2021-2025. Source: NHTSA 2025 Annual Recall Report, tables read directly.
- **D. Warranty costs:** Up. Global OEM accruals +11% in a single year (2023 to 2024, to $72.5B); US supplier claims, accruals, and reserves all rose again 2024 to 2025; powertrain suppliers' share of total supplier warranty cost has been rising since at least 2015. Source: Warranty Week, multiple dated articles fetched directly.
- **E. EV transition:** Directionally still a headwind for ICE-specific suppliers (fewer parts, MEMA members flag EV propulsion as their #2 sourcing-constraint worry), but the pace has stalled and reversed in the US: EV share peaked at 10.6% in Q3 2025 and fell to 5.8% by Q1 2026 after the October 2025 removal of federal incentives. Source: Cox Automotive, MEMA Barometer, both fetched directly.
- **F. Tariffs / cost pressure / supplier distress:** Sharply up, and the most current, best-evidenced driver in this file. Tariffs are MEMA's #1 named industry threat for 5 straight quarters of measurement; MEMA's own cost-pressure index (91/100) is the fastest-accelerating indicator it tracks; two major Tier 1 suppliers filed Chapter 11 in 2025; OEM margins are compressing faster than supplier margins per Bain, with OEM "cost-reduction programs" explicitly described as "increasingly felt by suppliers." Source: MEMA surveys (both fetched directly), Roland Berger/Lazard, Bain, and two supplier bankruptcy case write-ups.
- **G. Chargebacks/quality-cost-recovery specifically:** Likely up, but the evidence is indirect, not a tracked series. One independent (non-vendor) source states directly that "OEMs are now asking suppliers to cover more of the repair costs" (July 2025). A named respondent inside MEMA's own survey describes OEMs "differ[ing] and delay[ing]" on cost-recovery agreements. Every source that talks about "chargebacks" by that specific word is vendor marketing (Claimlane, Chargeflow, WarrantyHub, and the MOTOR/MAPconnected placement) and is excluded from the trend call per instructions. No primary, chargeback-specific published time series (comparable to NHTSA's recalls or Warranty Week's warranty accruals) was found to exist at all.

---

## What could not be found and why

- **A direct Fed/G.17 annual assemblies table**: the official PDF (federalreserve.gov/releases/g17/current/g17.pdf) returned corrupted/undecoded PDF stream text to the fetch tool and could not be read as text; the equivalent FRED monthly series was used and averaged instead, with the substitution disclosed.
- **OICA US total production 2015-2025**: the OICA production-statistics page's data tables did not render through automated fetch; only secondary citations of OICA data were found, and these are marked NOT VERIFIED rather than treated as fact.
- **ASM (2018-2021) and AIES (2023) value-of-shipments for NAICS 3363 specifically**: the Census Bureau's api.census.gov endpoint requires a registered API key, which was not available in this session ("A valid _key_ must be included with each data API request"); data.census.gov's own key-free browser API only had the two Economic Census (2017, 2022) tables identified and pulled in the time available. This is a genuine gap in the annual time series between the two Economic Census points, not an estimate filled in to cover it.
- **McKinsey's "Work the core" EV-supplier-transition article and PwC's "Merge ahead" EV supply-chain page**: both were located by search but could not be fetched (two 60-second timeouts on McKinsey; HTTP 403 on PwC). Their widely cited figures (fewer engine/transmission variants under EVs) are therefore NOT VERIFIED in this file even though they are probably accurate; I chose not to repeat search-engine-summary versions of their claims as fact per the no-search-summary rule.
- **A primary, chargeback-specific dollar or count time series**: does not appear to exist in the public domain the way NHTSA recalls or Warranty Week's warranty series do. Every source using the word "chargeback" that was found is vendor content selling recovery/dispute-automation software (Claimlane, Chargeflow, WarrantyHub) or a vendor-authored trade-magazine placement (MOTOR/MAPconnected). This is reported as a finding in itself: the absence of a tracked chargeback series is a real data gap, not a search failure, since MEMA (which tracks nearly everything else in this file in detail) does not appear to publish one either based on what was reviewed here (the Q4 2025 Barometer covers financial distress, watch lists, and tariff recovery disputes, but not chargebacks by name).
- **A precise real-terms figure for the AMVPVS (Motor Vehicles and Parts) 2015-2025 nominal growth**: I computed the nominal change (+24.6%) but did not compute the full 2015-2025 CPI-U cumulative change (only 2017-2022 was computed), so no real-terms percentage is asserted for that specific series; only the direction ("likely roughly flat to down in real terms, given the CPI-U pattern seen in the adjacent 2017-2022 window") is flagged, and it is explicitly marked as unconfirmed arithmetic rather than a verified figure.
- **2018 full-year Warranty Week supplier split figures** ($911M powertrain / $708M other, cited in a search-engine summary): could not be confirmed in the verbatim text of the source page when fetched directly, so it is marked NOT VERIFIED rather than repeated as fact.
- **The $286 million First Brands tariff claim**: found only via search-engine summary; the source page (mdm.com) returned HTTP 403 on direct fetch and could not be independently read, so it is marked NOT VERIFIED. Separately, and more importantly, First Brands' bankruptcy itself was verified to be about off-balance-sheet financing irregularities and alleged fraud, not tariffs, per a directly fetched source (Transport Topics, 2025-09-29) that explicitly does not mention tariffs as a cause. This is flagged because conflating First Brands with the tariff-driven Marelli bankruptcy would overstate the tariff driver's evidence base.
