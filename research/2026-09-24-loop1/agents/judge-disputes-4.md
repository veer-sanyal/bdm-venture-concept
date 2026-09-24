I checked the pitch's main numbers against primary sources and they hold. I'd still pass: the market is small, pricing only matches offshore labor, and upstream filtering may cut dispute volume. I hit the session's web-search limit before I could fully sweep for a company pitching exactly this, so that check is incomplete.

## Claim check

| Claim | Finding |
|---|---|
| CFPB complaints doubled to 6.6M in 2025 | True. The CFPB's 2025 annual report shows 6.6M, up from about 3.2M in 2024. About 5.8M (88%) were about credit reporting. Most of those were aimed at the three credit bureaus, not at lenders or collectors. Complaints against creditors and collectors were about 302k (up from 159k), per WebRecon. |
| FCRA suits up 37% in 2025 | True. WebRecon counts 8,369 suits in 2025, up 37.4%. |
| Up another 45% in the first seven months of 2026 | True. WebRecon via Shipkevich shows 44.6% year to date through July. |
| 30-day duty to investigate every dispute | Only half right. Disputes that come through the bureaus (ACDVs, the standard dispute form the bureaus send to lenders and collectors) must be investigated. For disputes sent straight to the lender, 12 CFR 1022.43(b)(2) says no investigation is required if the lender reasonably believes a credit repair firm prepared the dispute. Consumers can only sue over the investigation of a bureau-forwarded dispute, not a direct one. So the "lender's inbox" half of the product carries little lawsuit risk. |
| A thin investigation record loses suits | Supported by case law I cited from memory, not from this search. In Johnson v. MBNA (4th Cir. 2004), the court held that the investigation must be reasonable, not a quick computer match. In Hinkle v. Midland (11th Cir. 2016), a debt buyer verified disputes from its own data without the original creditor's documents, and the court said a jury should decide whether that was reasonable. |

Two facts the pitch leaves out:
- Collection accounts are the most disputed item on credit reports. About 5% of them get disputed, and they account for about 40% of disputes the bureaus handle (CFPB 2012 and 2021 reports).
- The bureaus now screen out more disputes before they reach lenders and collectors. TransUnion sends third-party complaints without enough documentation to a separate channel. Experian's rate of resolving complaints in the consumer's favor fell from about 20% to under 1%. Since February 2026 the CFPB portal requires consumers to attest to the truth of a complaint and show ID. Bills in Congress also target credit repair firms and repeat disputes. More complaints does not mean more disputes reach the customer.

## Who already serves this customer
- **The bureaus own the dispute channel.** e-OSCAR, the system that carries disputes between bureaus and lenders, belongs to Equifax, Experian, TransUnion and Innovis. It offers an API and a $90 registration.
- **Collection-software vendors own the account data and the sales relationship.** These are Finvi, Latitude by Genesys, C&R Software and FICO. Any of them could add a dispute module.
- **Direct competitors:**
  - Bridgeforce DQS Disputes Module checks dispute responses against Metro 2 rules (the bureaus' standard reporting format) and sells to collectors and debt buyers.
  - Experian DataArc 360 checks the quality of the data lenders report.
  - ICE Credit Bureau Management does this for mortgage servicers.
  - BureauRelay tracks disputes against the 30-day deadline, with no AI and no e-OSCAR link.
  - Outsourcing firms handle disputes manually. In a 2023 prototype, FTI Consulting estimated about 10 minutes per manual dispute and a 90% cut from automation.
- **No exact match found.** Nobody I found combines AI-drafted responses with a lawsuit-ready file.

## 1. Strongest version
Sell only to debt buyers and large third-party collectors, and handle only bureau-forwarded disputes. That is where the lawsuit exposure and the dispute volume both sit.

Build around the Hinkle problem. A debt buyer's weak spot is verifying a debt from a spreadsheet without the original paperwork. The product would pull each account's chain-of-title documents (bill of sale, original creditor statements) and cite them in every response. It would decide verify, correct or delete, and keep an investigation file that defense counsel can export when a suit arrives. Direct disputes get sorted into "credit repair firm, no investigation required" or "real dispute." Price per dispute, plus a fee per file exported for litigation, so the price follows the value of avoided suits and not labor cost.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | FCRA suits rose 37.4% in 2025 and 44.6% through July 2026, and Hinkle makes a debt buyer's data-only check a question for a jury. |
| Value over current tools | 3 | FTI puts manual handling at about 10 minutes per dispute. At offshore wages that is about $1 to $2, so $1 to $3 only matches labor, and Bridgeforce already checks responses. The lawsuit-ready file is the only new thing. |
| Market size | 2 | Nobody publishes current dispute volumes, so this is my estimate. A few hundred firms handle 5,000 to 50,000 disputes a month. At about 15,000 disputes × $2 × 12 months per firm, that is roughly $50M to $150M a year, even allowing for collections being 40% of disputes. |
| Risk (5 = low) | 2 | The bureaus and regulators are filtering credit repair and AI disputes upstream, the bureaus control the dispute channel, collection-software vendors own the account data, and an AI "verify" that turns out wrong creates the liability this product exists to prevent. |

## 3. What kills it, and the fastest test
**What kills it:** most FCRA suits against these customers turn on something other than how the investigation was documented. Examples are a wrong balance, a debt not marked as disputed, or a mixed-up identity. Those suits also tend to settle for nuisance value whatever the record shows. If that is true, the investigation file adds nothing, and the product is just labor savings at labor prices.

**Fastest test:** Pull the last 30 FCRA complaints filed against two or three large debt buyers from PACER or CourtListener. Midland/Encore, PRA and LVNV are good candidates. Count how many allege an unreasonable investigation after a bureau-forwarded dispute and describe a thin investigation record. It takes one day and needs no customer. If fewer than about a third match, pass for good.

## Sources
- [ABA Banking Journal: CFPB received 6.6M complaints in 2025](https://bankingjournal.aba.com/2026/04/cfpb-received-6-6m-consumer-complaints-in-2025/)
- [CFPB 2025 Consumer Response Annual Report](https://files.consumerfinance.gov/f/documents/cfpb_2025-cr-annual-report_2026-03.pdf)
- [WebRecon Dec 2025 stats and year in review](https://webrecon.com/litigation-statistics/webrecon-dec-2025-stats-year-in-review)
- [Shipkevich: July 2026 litigation update](https://www.shipkevich.com/july-2026-litigation-update-fcra-filings-continue-to-climb-as-other-consumer-litigation-pulls-back-ytd-figures-still-high/)
- [eCFR 12 CFR 1022.43, direct disputes](https://www.ecfr.gov/current/title-12/chapter-X/part-1022/subpart-E/section-1022.43)
- [CFPB 2021 report, Disputes on Consumer Credit Reports](https://files.consumerfinance.gov/f/documents/cfpb_disputes-on-consumer-credit-reports_report_2021-11.pdf)
- [ProPublica on bureau relief rates](https://www.propublica.org/article/credit-report-mistakes-cfpb-experian-transunion)
- [American Banker on the CFPB portal changes](https://www.americanbanker.com/news/cfpb-implements-new-requirements-for-complaints-on-its-portal)
- [FTI Consulting via AFSA on automated dispute handling](https://afsaonline.org/2023/01/16/how-automated-credit-dispute-handling-can-reduce-costs-by-90/)
- [Bridgeforce Disputes Module](https://bridgeforcedatasolutions.com/credit-bureau-disputes-module/)
- [BureauRelay dispute management](https://bureaurelay.com/features/dispute-management)
- [e-OSCAR getting started](https://www.e-oscar.org/gettingstarted)
- [Finvi on frivolous and duplicative disputes](https://finvi.com/blog/frivolous-disputes-and-duplicative-disputes-a-case-of-reconcilable-differences/)

VERDICT: PASS
