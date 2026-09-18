# G. Census SUSB series, 2017 to 2022: supplier counts and receipts, 20-499 employees

Pulled 2026-09-13 by the main session from the Census SUSB "US & states detailed sizes" files, US total
rows (state 00), enterprise size bins 07 to 18 summed (20-24 through 400-499 employees). Receipts are
published only in Economic Census years (2017, 2022). All cells carry Census noise infusion; a bin count
below 12 means Census suppressed some cells, so that row's subtotal is understated.

Files:
- https://www2.census.gov/programs-surveys/susb/tables/2017/us_state_naics_detailedsizes_2017.xlsx
- https://www2.census.gov/programs-surveys/susb/tables/2019/us_state_naics_detailedsizes_2019.xlsx
- https://www2.census.gov/programs-surveys/susb/tables/2021/us_state_naics_detailedsizes_2021.xlsx
- https://www2.census.gov/programs-surveys/susb/tables/2022/us_state_naics_detailedsizes_2022.xlsx

2012 not included: the 2012 table uses a different file (`us_6digitnaics_2012.xls`) in the old .xls
format, which needed a library not installed. Not pursued; 2017 to 2022 covers two Economic Census years.

## Core four industries, 20-499 employees

| | 2017 | 2019 | 2021 | 2022 | 2017 to 2022 |
|---|---|---|---|---|---|
| Firms | 1,944 | 1,924 | 1,908 | 1,897 | **-2.4%** |
| Plants (establishments) | 2,182 | 2,151 | 2,161 | 2,173 | **-0.4%** |
| Receipts, nominal | $55.32B | n/a | n/a | $68.56B | **+23.9%** |

## By industry

| NAICS | Industry | Firms 2017 | Firms 2022 | Change | Receipts 2017 | Receipts 2022 | Change | Total firms, all sizes 2017 to 2022 |
|---|---|---|---|---|---|---|---|---|
| 3363 | Motor vehicle parts | 1,334 | 1,289 | -3.4% | $42.85B | $50.86B | +18.7% | 4,010 to 3,616 (-9.8%) |
| 336310 | Engine parts | 130 | 121 | -6.9% | $3.11B | $3.07B | -1.3% | 706 to 637 |
| 336320 | Electrical | 168 | 157 | -6.5% | $4.18B | $4.51B | +7.9% | 565 to 501 |
| 336330 | Steering and suspension | 69 | 69 | 0% | $2.58B | $2.12B | -17.8% | 220 to 229 |
| 336340 | Brakes (bins suppressed) | 49 | 40 | n/a | $2.11B | $2.10B | n/a | 139 to 132 |
| 336350 | Transmission and powertrain | 119 | 123 | +3.4% | $4.27B | $5.59B | +30.9% | 390 to 365 |
| 336360 | Seating and interior | 112 | 128 | +14.3% | $3.59B | $4.11B | +14.5% | 307 to 304 |
| 336370 | Metal stamping | 331 | 318 | -3.9% | $9.91B | $12.13B | +22.4% | 597 to 543 |
| 336390 | Other parts | 365 | 353 | -3.3% | $13.04B | $17.23B | +32.1% | 1,268 to 1,101 |
| 3352 | Household appliances (bins suppressed) | 48 | 60 | +25.0% | $0.79B | $2.04B | n/a | 258 to 304 |
| 333111 | Farm machinery | 309 | 318 | +2.9% | $5.76B | $8.65B | +50.2% | 1,054 to 1,024 |
| 333120 | Construction machinery | 253 | 230 | -9.1% | $5.92B | $7.01B | +18.4% | 651 to 574 |

**Read:** across all sizes, auto parts lost about 10% of its firms, mostly below 20 employees. The
20-499 band barely shrank. Receipts grew in nominal dollars in most sub-industries; engine parts were
flat. Inflation adjustment is not applied here; see `F-trend-drivers.md`.
