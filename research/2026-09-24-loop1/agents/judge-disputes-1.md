**Bottom line: I'd pass.** The problem is real and the regulations back it, but the paying customer set is small, the cheapest alternative is to delete the disputed account from the credit report, and the dispute surge behind the pitch is already being choked off at the source.

## How the pitch's claims check out

- **"CFPB complaints doubled to 6.6 million in 2025."** True: 6.6M, up from 3.2M in 2024 ([ABA Banking Journal](https://bankingjournal.aba.com/2026/04/cfpb-received-6-6m-consumer-complaints-in-2025/), [CFPB annual report](https://files.consumerfinance.gov/f/documents/cfpb_2025-cr-annual-report_2026-03.pdf)). It overstates what reaches this customer, though:
  - About 5.8M (88%) were about credit reporting, and most named the three big bureaus. The CFPB's own report says about 3.9M of 4.8M credit reporting complaints from January 2024 to June 2025 were about Equifax, Experian and TransUnion ([CFPB 611(e) report, Dec 2025](https://files.consumerfinance.gov/f/documents/cfpb_fcra-611e-report_2025-12.pdf)).
  - Complaints against creditors and collectors were about 302k in 2025, according to WebRecon.
  - The CFPB blames credit repair firms and AI agents for "duplicative and spurious" complaints ([Orrick](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/)). That supports the "bulk AI disputes" story.
  - A complaint is not a dispute. Furnishers (the lenders and collectors that report accounts to the bureaus) receive disputes as ACDVs, the bureaus' standard electronic dispute form, sent through e-OSCAR, the bureaus' shared dispute system. Nobody publishes current ACDV counts. The last public figure is 91M disputed items in 2016.
- **"FCRA lawsuits rose 37% in 2025 and 45% in the first seven months of 2026."** Close enough. The counts are 8,369 suits in 2025, up 37.4% ([WebRecon](https://webrecon.com/litigation-statistics/webrecon-dec-2025-stats-year-in-review)), and up 44.6% year to date through July 2026 ([Shipkevich](https://www.shipkevich.com/july-2026-litigation-update-fcra-filings-continue-to-climb-as-other-consumer-litigation-pulls-back-ytd-figures-still-high/)). Two caveats:
  - Neither source splits cases by defendant, so the share aimed at furnishers rather than bureaus is unknown.
  - About 44% of plaintiffs had sued before, so much of this is lawyer-driven volume.
- **"30 days" and "a thin record loses suits."** Both hold for disputes that arrive through the bureaus.
  - The deadline is 30 days (45 if the consumer adds information), set by FCRA §611(a)(1). It reaches furnishers through §623(b) and, for disputes sent straight to the furnisher, 12 CFR 1022.43(e).
  - In the 11th Circuit's Hinkle v. Midland (2016), a jury could find willfulness where the debt buyer marked debts "verified" without any documents. In 2025 the 4th Circuit widened furnisher duties to disputes that can be objectively checked ([CFS Law Monitor](https://www.consumerfinancialserviceslawmonitor.com/2025/03/fourth-circuit-issues-ruling-on-furnishers-duty-to-investigate-legal-disputes-under-fcra/)).
- **The "lender's inbox" half is weaker than pitched.**
  - Disputes sent straight to the lender carry no private right to sue (FCRA §1681s-2(c)).
  - Furnishers may skip any they reasonably believe came from a credit repair firm (12 CFR 1022.43(b)(2), [eCFR](https://www.law.cornell.edu/cfr/text/12/1022.43)).
  - The litigation value sits almost entirely in disputes that come through the bureaus.

## Who else serves this customer

- **Bridgeforce Data Solutions** sells a Disputes Module that analyzes ACDV data against the account's reporting history and flags data-quality errors. It also has an "Agent Assist" add-on for dispute agents and tools to oversee outsourced dispute staff ([Bridgeforce](https://bridgeforcedatasolutions.com/agent-assist-essentials-announcement/)). It already has the compliance buyer's attention at larger lenders.
- **Salient** (a16z, $60M raised, about $25M ARR, subprime auto servicing) says it is expanding into credit disputes and complaints ([fintech.global](https://fintech.global/2025/07/29/ai-loan-servicing-platform-salient-secures-60m/)). Prodigal, Sei AI and Aktos cover collector workflows next door.
- **The collection systems where account data lives:** Latitude by Genesys, Finvi and C&R Software.
- **Outsourcing firms** that work dispute queues by hand.

I found no company pitching this product almost exactly.

**Who owns the data and the buying channel.** The dispute feed belongs to the bureaus through e-OSCAR. It offers paid API access and allows middleware vendors after a 7-stage onboarding process ([e-OSCAR](https://www.e-oscar.org/services-by-e-oscar)), so the channel is open but gated. The account files sit in the collection system of record. No incumbent yet sells AI-drafted responses with a litigation-ready file.

## 1. The strongest version

Drop the inbox half and the "bulk AI disputes" framing. Sell only the disputes that arrive through the bureaus, because that is where the right to sue, and therefore the budget, sits.

- **Customers:** subprime lenders that must keep reporting (auto, card, installment), plus debt buyers.
- **Product:** a certified e-OSCAR middleware layer that:
  - matches each dispute to the account record, and for purchased debt to the ownership documents (bill of sale, charge-off statement);
  - decides verify, modify or delete, and deletes when the documents aren't there rather than verifying;
  - writes a per-dispute investigation file that defense counsel can use;
  - scores each dispute's litigation risk (repeat plaintiffs, known consumer-law firms) and routes the risky ones to a human.
- **Pricing:** per dispute, plus a tier tied to the customer's FCRA settlement spend.
- **Expansion:** complaint responses, Metro 2 reporting accuracy (the industry's standard file format for reporting accounts to bureaus), and debt validation disputes under the FDCPA, the federal debt collection law.

## 2. Ratings (5 is best; for risk, 5 means low risk)

- **Customer need: 4.** There is a legal duty with a 30-day clock, FCRA suits are up 37.4% in 2025 and 44.6% so far in 2026, and Hinkle shows a thin file supports a willfulness finding.
- **Value over what customers use today: 3.** FTI Consulting estimates automation cuts dispute handling from about 10 minutes to about 1 ([AFSA](https://afsaonline.org/2023/01/16/how-automated-credit-dispute-handling-can-reduce-costs-by-90/)). But Bridgeforce and outsourcing firms already cover part of the job, and a debt buyer can simply delete the disputed account.
- **Market size: 2.** I estimate roughly 150 US firms handle 5k to 50k disputes a month. At about 15k a month and $2 each, that is about $360k per customer and about $55M in total. Even with every furnisher included, the dispute fee pool is likely in the low hundreds of millions.
- **Risk: 2.** Since February 2026 the CFPB has required identity checks, attestation and a 45-day wait after a bureau dispute before a complaint can be filed ([American Banker](https://www.americanbanker.com/news/cfpb-makes-changes-to-complaint-portal-citing-abuse)). Bureaus are also filtering template disputes as frivolous. The volume may be near its peak, and a wrong AI "verify" creates exposure for willful violations.

## 3. What would kill it, and the fastest test

**What would kill it.** Target customers don't pay more for a better investigation, because:
- debt buyers just delete disputed accounts or stop reporting, which costs them almost nothing;
- lenders get "good enough" from Bridgeforce, their collection system, or an outsourcing firm at under $1 a dispute;
- falling dispute volume would add to either problem.

**The fastest test.** Offer a paid 30-day pilot at $2 per dispute on the live dispute queue to 10 target firms: 5 subprime lenders and 5 debt buyers. In each call, ask for today's full cost per dispute and last year's settlement spend on FCRA suits against furnishers.
- Kill it if fewer than 2 sign within three weeks.
- Kill it if the typical cost is under $1.
- Kill it if the typical answer is "we just delete."

VERDICT: PASS
