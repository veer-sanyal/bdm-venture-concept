I'd pass. The problem is real, but the best version of this business is a useful product for a narrow market, and the companies that already hold the customer's account data and buying channel are well placed to add it themselves.

**Checking the claims against sources**
- **6.6M CFPB complaints in 2025, double 2024's 3.2M:** true ([CFPB 2025 annual report](https://files.consumerfinance.gov/f/documents/cfpb_2025-cr-annual-report_2026-03.pdf), [ABA](https://bankingjournal.aba.com/2026/04/cfpb-received-6-6m-consumer-complaints-in-2025/)). About 5.8M were about credit reporting.
- **But the complaints mostly don't reach this customer.** From January 2024 to June 2025, about 3.9M of the 4.8M credit reporting complaints were about Equifax, Experian and TransUnion ([CFPB 611(e) report](https://files.consumerfinance.gov/f/documents/cfpb_fcra-611e-report_2025-12.pdf)). Complaints against creditors and debt collectors were about 302K in 2025 ([WebRecon](https://webrecon.com/litigation-statistics/webrecon-dec-2025-stats-year-in-review)).
- **Much of the surge is people gaming the system.** The CFPB blames credit repair firms and AI agents for much of it. It added friction to its complaint portal in February 2026 and again in June 2026 (ID checks, and consumers must dispute with the bureau first and wait 45 days) ([American Banker](https://www.americanbanker.com/news/cfpb-implements-new-requirements-for-complaints-on-its-portal), [Consumer Finance Monitor](https://www.consumerfinancemonitor.com/2026/06/25/cfpb-announces-major-overhaul-of-consumer-complaint-system-a-shift-toward-integrity-standardization-and-statutory-compliance/)). An industry piece argues this pushes disputes toward bureaus and lenders rather than removing them ([insideARM](https://www.insidearm.com/news/00095267-cfpb-complaint-portal-changes-less-noise/)).
- **FCRA lawsuits up 37% in 2025:** true, 8,369 suits, up 37.4%. **Up 45% through July 2026:** true, 44.6% ([WebRecon](https://webrecon.com/litigation-statistics/webrecon-june-2026-stats), [Shipkevich](https://www.shipkevich.com/july-2026-litigation-update-fcra-filings-continue-to-climb-as-other-consumer-litigation-pulls-back-ytd-figures-still-high/)). I couldn't find a split of how many suits target lenders and collectors versus the bureaus.
- **"A thin investigation record loses suits":** this matches case law I know from memory but didn't re-check here. Hinkle v. Midland (11th Cir. 2016) held that a debt buyer confirming a debt without the underlying documents can be an unreasonable investigation.
- **Not confirmed:** whether the dispute volume that actually reaches lenders and collectors has grown. That is the real demand driver, and I found no public data on it.

**Who else serves this customer**
- **e-OSCAR**, owned by the credit bureaus, runs the dispute pipe. It now sells an API for receiving disputes and sending responses ([e-OSCAR](https://www.e-oscar.org/services-by-e-oscar)). That makes integration easier, and it doesn't draft responses.
- **Bridgeforce Data Solutions** is the closest competitor. It already audits every bureau dispute and analyst response, and sells to collection agencies among others. It is piloting an "AI Resolution Engine" that gathers each dispute's history and documents for an analyst. It doesn't draft responses or build investigation files ([product page](https://bridgeforcedatasolutions.com/product/), [disputes module](https://bridgeforcedatasolutions.com/disputes/)).
- **Collection software (Finvi's Artiva, Latitude, FICO Debt Manager):** these hold the account file and are how collection agencies buy software. From memory, not checked this session: they have e-OSCAR modules. This group owns the customer's data and buying channel.
- **Others:** offshore outsourcing firms and in-house analysts. FTI prototyped this automation in 2023, cutting about 10 minutes of work per dispute to about 1 ([AFSA](https://afsaonline.org/2023/01/16/how-automated-credit-dispute-handling-can-reduce-costs-by-90/)).
- **No exact match found.** My search budget ran out before I could rule one out completely.

**1. Strongest version**
Aim narrowly at debt buyers and the agencies collecting on their behalf. Their evidence gap is built in: they often lack the original creditor's documents, which is exactly the Hinkle exposure.

The product becomes the investigation file of record for every dispute a collector gets:
- disputes that come through the bureaus;
- disputes sent straight to the collector, including screening out credit-repair-firm submissions, which the rules (Reg V 1022.43) don't require them to investigate;
- debt-validation disputes under the debt collection rules, handled by the same team.

For each dispute it pulls the ownership chain and the account documents. It recommends deleting the entry whenever the evidence can't support verifying it, and produces a file defense counsel can use. Sell it through FCRA defense firms and collection agencies' liability insurers, with pricing tied to lower lawsuit exposure rather than hours saved.

**2. Ratings**

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | FCRA suits rose 37.4% in 2025 and 44.6% through July 2026, and Hinkle makes a thin record a jury question for debt buyers. |
| Value over what they use today | 3 | e-OSCAR plus their collection software plus analysts already works, and $1–3 per dispute may not beat offshore labor. The litigation-ready file is the only clear difference. |
| Market size | 2 | One customer is worth about $60K–$1.8M a year (5,000–50,000 disputes a month at $1–3). The collection industry is concentrated, so the core market is likely in the low hundreds of millions. That is my estimate. |
| Risk (5 = low) | 2 | It needs the collection software vendors' cooperation to reach account files. Bridgeforce is already inside the same compliance teams. Portal friction and bureau screening could reduce volume. And "AI verified it" gives plaintiffs a new argument that the investigation wasn't reasonable. |

**3. What would kill it, and the fastest test**
It dies if the dispute volume reaching collectors isn't actually growing, or if today's cost per dispute is already under $1 (offshore staff). It also dies if lawsuits aren't being lost over the investigation record.

Fastest test: in one week, call 10 compliance heads at debt buyers and collection agencies. Ask each for:
- monthly bureau dispute counts for 2023 versus 2026;
- their fully loaded cost per dispute today;
- the number of FCRA suits in the last 12 months and why they settled or lost;
- whether they would pay $1.50 per dispute for a one-month pilot on their own dispute archive.

Kill it if fewer than 3 show rising volume and cost above $1.50, and fewer than 2 agree to the paid pilot.

This is timely and real, but it's more a feature that Bridgeforce or a collection software vendor could add than a venture-scale company.

VERDICT: PASS
