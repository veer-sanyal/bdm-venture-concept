# MARKET SIZE: Supplier Quality Chargeback Defense

**Run 2026-09-12.** Evidence: `screens/2026-09-12-market-size/` (A supplier universe, B frequency and
dollars, C price anchors), every number there with URL, date and verbatim quote. Predictions written
before dispatch: `predictions/2026-09-12-market-size.md`. This file owns the sizing model; `STATE.md`
candidate 5 rung 6 and `CONCEPT.md` point here.

**Labels:** VERIFIED = fetched primary source. COMPUTED = my arithmetic on verified data, shown.
ESTIMATE = my arithmetic that stacks mismatched units, stated. ASSUMED = a placeholder the calls replace.

---

## The one-paragraph answer

**The customer count is solid. The dollars per customer are not published anywhere, so the market is a
range that the calls collapse.** There are **1,897 US firms (2,173 plants) with 20 to 499 employees** in
auto parts, appliances, farm and construction machinery, with **$68.6B** in combined receipts. On middle
assumptions (a chargeback a month at $5,000 all-in), those plants absorb about **$130M a year** in
quality chargebacks, but the revenue a defense product can capture from that is only **about $5M to $7M a
year** in the US. **Reaching a $100M revenue market would need about $680k of chargebacks per plant per
year, roughly 2.2% of an average plant's revenue, about three times the rate suppliers were charged for
warranty in the only published benchmark.** As scoped, this is a small market. The venture case depends
on expansion, and that expansion has to be shown with evidence.

## 1. How many customers: VERIFIED

Census SUSB 2022, US firms by enterprise size, 20 to 499 employees:

| NAICS | Industry | Firms | Plants (establishments) | Employees | Receipts |
|---|---|---|---|---|---|
| 3363 | Motor vehicle parts | 1,289 | 1,494 | 133,670 | $50.86B |
| 3352 | Household appliances | 60 | 67 | 5,137 | $2.04B |
| 333111 | Farm machinery | 318 | 351 | 22,583 | $8.65B |
| 333120 | Construction machinery | 230 | 261 | 16,296 | $7.01B |
| **Core total** | | **1,897** | **2,173** | **177,686** | **$68.57B** |

Receipts summed from the same SUSB file (COMPUTED; Census applies noise infusion to every cell). Average
receipts **$36.1M per firm, $31.6M per plant.** The same 1,289 figure was already in `STATE.md` from the
PPAP rung 6, so the count reproduces.

**Indiana:** 170 auto-parts plants with 20 to 499 employees (CBP 2023, establishment size: 48 + 35 + 47
+ 40), inside 281 total. Economic Census 2022: 251 firms, $27.75B shipments.

**Outside the band:** all of NAICS 3363 took **$276.5B** in receipts in 2022; the 20-499 band is $50.9B of
it. Most of the money sits with the 352 firms above 500 employees, which also have the staff and the
incumbent software.

**Tier-2/3 suppliers classified outside these codes (ESTIMATE, lower bound):** no source counts them. BEA's
2017 detail Use table gives the share of each industry's output bought directly by motor-vehicle makers.
Applying that share to each industry's 20-499 firm count treats dollars as if they were spread evenly
across firms, which they are not:

| Industry | 20-499 firms | Direct share to auto | Firm-equivalents |
|---|---|---|---|
| Foundries (3315) | 544 | 37.0% | 201 |
| Machine shops (332710) | 2,737 | 9.5% | 260 |
| Stamping, non-auto code (332119) | 473 | 10.2% | 48 |
| Plastics (326199; share is 326190 combined) | 1,811 | 5.5% | 100 |
| Heat treating (332811; share is 3328 combined) | 214 | 6.2% | 13 |
| Plating (332813; share is 3328 combined) | 616 | 6.2% | 38 |
| **Total** | | | **about 660** |

So the adjacent universe adds **roughly a third** (about 35%), not the multiple I predicted.

## 2. What one chargeback costs: fee schedules VERIFIED, all-in totals NOT PUBLISHED

**Published rates, from the issuers' own manuals:**

| Issuer | Admin fee | Labour rates | Other |
|---|---|---|---|
| Tenneco (Rev. 08/2025) | **$500** per incident (North America) | Sort, line stoppage, receiving inspection **$60/hr per employee**; changeover, investigation **$85/hr** | Re-PPAP **$1,000** per part number; failure to follow requirements $250 |
| Lear (May 2019) | 2-hour minimum per Quality Notice | Labour capped at **$75/hr** | $100 per shipment for ASN, logistics or packaging failures |
| Adient (Rev. 3.0, 2019) | $250 | | Auto-debit after 30 working days |
| Piston (P-PR200.12 Rev O) | $200 | $200 per shift sort | $200 minimum delivery notice |
| BorgWarner, Dana, Martinrea, Magna | **"Actual cost"** or "to be determined" | | No fixed number published |

**Fixed fee schedules are the exception.** Most Tier-1s bill at actual cost, so the all-in total is
unknowable from the desk.

**An illustrative chargeback built from Tenneco's card (quantities invented):** admin $500 + sort 4
people x 2 shifts x 8 hours x $60 ($3,840) + line stoppage 20 people x 1 hour x $60 ($1,200) +
investigation 4 hours x $85 ($340) = **$5,880**, before any third-party sort invoice or premium freight.

**How often: NOT PUBLISHED.** No AIAG, MEMA/OESA, Deloitte, McKinsey, QAD or Plex source counts chargebacks
per supplier per year. The only number is one 2002 forum post (n=1). Call question 1 is the only way to
get it.

**Second pass, 2026-09-12, aimed at where numbers leak** (`screens/2026-09-12-market-size/D-courts-and-filings.md`,
`E-people-and-postings.md`). Still no count and no typical all-in figure. What it found:

| Record | What it shows | Limit |
|---|---|---|
| ATD Corp. v. DaimlerChrysler, 261 F. Supp. 2d 887 (E.D. Mich. 2003) | Single debits of **$94,000** (1997) and **$709,971.86** (2001) against a supplier's receivable | Supplier to the OEM directly, so larger than a Tier-2; court cases skew to big disputes |
| Short v. Mando American Corp. (11th Cir. 2015) | A Tier-1's outstanding chargebacks that **its suppliers refused to accept** grew from "hundreds of thousands of dollars" (2007) to **"several million dollars"** (2008) | No count; chargebacks are background to an employment case. **But it is direct evidence that suppliers do push back, at scale** |
| Core Molding Technologies 10-Q/10-K | Receivables reduced for chargebacks by **$179,000 to $2,344,000** at period ends, 2015-2021 | A balance at one date, not a year's volume; mixes quality with returns, price adjustments, premium freight and late-delivery line disruption |
| Alpine Machine Tool v. Rotair (Conn. Super. 1990) | Chargebacks of **$12,570.90 on a $9,750 contract**, 129% of the order | Aerospace, 1990 |

**Dead ends:** every dollar figure on a resume site was a template sample, not a real person. Bankruptcy
claims registers (Shiloh, Unique Fabricating, Dura) exist but render in JavaScript and were not read; a
browser session or PACER could still open them.

**What this changes in the model: nothing in the mid case.** It confirms the tail is real (single debits
in six figures exist) and that disputes happen, and it still gives no frequency.

**The only published benchmark near this, and it is a different charge:** suppliers' warranty claims ran
about **0.7% of product revenue** against 2.5% for final assemblers (Warranty Week, Q1 2003 to Q1 2004).
Meritor recovered warranty costs from WABCO at a flat **0.85%** of purchases (SEC 10-K/A FY2017). Used here
only as a plausibility ceiling.

## 3. The model: pool, then capturable revenue (ASSUMED inputs, COMPUTED outputs)

**Step 1, the chargeback pool.** Plants x chargebacks per year x average all-in amount.

| | Low | Mid | High |
|---|---|---|---|
| Chargebacks per plant per year (ASSUMED) | 4 | 12 | 30 |
| Average all-in amount (ASSUMED) | $2,000 | $5,000 | $10,000 |
| Charged per plant per year | $8,000 | $60,000 | $300,000 |
| As % of average plant receipts ($31.6M) | 0.03% | 0.19% | 0.95% |
| **Pool, 2,173 core plants** | **$17M** | **$130M** | **$652M** |

High sits above the 0.7% supplier warranty benchmark, so treat it as aggressive.

**Step 2, what a supplier gets back.** Recovered = charged x share defensible x win rate. ASSUMED 30%
defensible and 50% won, so **15% of what is charged comes back**: $1,200 / $9,000 / $45,000 per plant.

**Step 3, what we can charge.**

| Pricing | Anchor (VERIFIED) | Per plant per year | **US revenue, core** | With adjacent (+35%) |
|---|---|---|---|---|
| Contingency, 25% of recovered | OverDeduct 25%; freight audit 25-50% | $300 / $2,250 / $11,250 | **$0.7M / $4.9M / $24M** | $0.9M / $6.6M / $33M |
| Subscription, a third of recovered | EASE $8.6k-15.5k per site per year; Supplios $12k | $400 / $3,000 / $15,000 | **$0.9M / $6.5M / $33M** | $1.2M / $8.8M / $44M |

Subscription is capped at a third of what it recovers because a tool that returns under 3x its price does
not survive a renewal (a rule of thumb, ASSUMED). In the high case the $15k price lands right on EASE's
top tier, which is a sanity check that it could be charged.

## 4. What would have to be true for a venture-scale number

**For $100M a year of US revenue:** $100M / about 2,930 plants (core plus adjacent) = **$34k per plant per
year** -> x3 = $102k recovered -> / 15% = **$680k charged per plant per year = 2.2% of an average plant's
receipts.** That is about three times the supplier warranty benchmark, and for quality chargebacks alone
it is not believable without a call saying so.

**So the levers, each a claim to test rather than a fact:**
1. **Frequency and size are higher than mid.** Call question 1. If three suppliers say monthly and
   five figures, the high column is real and this is a $25M to $45M US market.
2. **All customer debits, not only quality.** Delivery and logistics debits are VERIFIED to exist on the
   same mechanic (Lear $100 per ASN failure, Tenneco $250 failure-to-follow, Piston $200 delivery notice),
   but they are small per incident. Call question 4c.
3. **Warranty chargebacks.** Suppliers carry about a tenth of the industry's warranty cost (Warranty Week,
   2023). That is the largest pool near this, but it sits with large Tier-1s and is often settled by
   formula (Meritor's flat 0.85%), which leaves less to dispute. NOT VERIFIED as disputable.
4. **Larger suppliers (500+).** Most of the receipts, but they already have staff and software.
5. **Mexico and Canada supply bases.** Not sized.

## 5. Rubric consequence

**Criterion 6 stays at 2, and on desk evidence alone it leans toward 1.** The count is now countable,
which a 5 requires, but the dollars per customer make the wedge small. **What moves it is not more desk
work: it is call question 1 (frequency and all-in size) and 4c (other debits on the same channel).** The
pitch should present the pool ($130M mid), the capturable revenue honestly, and the expansion with
whichever of levers 1-3 the calls confirm.

## 6. Growing or shrinking? (added 2026-09-13)

Evidence: `screens/2026-09-12-market-size/G-census-series.md` (Census counts and receipts, main session)
and `F-trend-drivers.md` (production, recalls, warranty, EVs, tariffs). Predictions:
`predictions/2026-09-13-market-trend.md`.

**Short answer: the market is flat in size and the pain behind it is rising right now.**

| Driver | Direction | Evidence |
|---|---|---|
| **Customer count** | **Flat** | Core four industries, 20-499 employees: 1,944 firms (2017) to 1,897 (2022), -2.4%; plants 2,182 to 2,173. Auto parts lost ~10% of ALL firms, almost entirely below 20 employees (SUSB) |
| **Their revenue** | **Flat after inflation** | Core band receipts $55.3B to $68.6B, +23.9% nominal; CPI-U +19.4% (245.12 to 292.66), so about +3.8% real. Auto parts band alone +18.7% nominal, about flat real. Whole auto-parts industry -10.8% real (Economic Census $261.3B to $278.2B), so small and mid suppliers held share while the industry shrank |
| **Vehicle production** | **Flat to down** | Fed G.17 assemblies 10.0-10.7M a year 2023-2026, vs 10.9M in 2019 and ~12.1M in 2015-16 |
| **Recalls** | **No trend** | NHTSA: 883 to 1,093 recalls a year 2015-2025; equipment-attributed share 7.4%-10.6%, no drift |
| **Warranty costs** | **Up** | Global OEM accruals $72.5B in 2024, +11% (Warranty Week, verified verbatim); US supplier claims and accruals rose again 2024-2025 |
| **Cost pressure on suppliers** | **Sharply up** | MEMA Q4 2025 Barometer (n=104): tariffs the #1 threat, cost index 91, the highest indicator it tracks; a supplier verbatim: OEMs *"differ and delay resulting in very little money coming in"* on agreed tariff recovery. Marelli and First Brands filed Chapter 11 in 2025 |
| **EVs** | **Headwind for engine suppliers, stalled** | Engine-parts band firms -6.9%, receipts flat 2017-2022; US EV share 10.6% (Q3 2025) to 5.8% (Q1 2026) after incentives ended (Cox Automotive) |
| **Chargebacks themselves** | **No series exists** | Every source using the word is vendor marketing. Closest independent: a July 2025 trade newsletter citing Warranty Week that OEMs *"are now asking these suppliers to cover more of the repair costs"* (warranty, not quality chargebacks) |

**What this means for the pitch:**
- **Do not claim a growing market.** The customer base and the physical volume are flat; a judge from HG
  Ventures or New Eagle will know it.
- **Claim a rising "why now."** Customers under margin pressure push more cost onto suppliers, and
  suppliers are fighting back on cost recovery in 2025-2026. That belongs on criterion 3 (unmet need), not
  criterion 6. **Caveat to say out loud: the cost-recovery friction on record is about tariffs and
  warranty, not quality chargebacks; the link is an inference until a call confirms it.**
- **One call question does both jobs:** "Is your customer charging back more than two years ago?"
