## Strongest version

**A dispute desk for collection agencies and debt buyers.** The software is one queue for every consumer challenge a collector receives:

- **Bureau-forwarded disputes.** These arrive as ACDVs (the bureaus' coded dispute forms) and would be pulled through e-OSCAR's API. e-OSCAR is the dispute system the bureaus own. It publishes that API and a third-party service provider addendum, so a vendor can get access ([e-OSCAR](https://www.e-oscar.org/services-by-e-oscar), [vendor management](https://www.e-oscar.org/vendor-management)).
- **Direct disputes** that consumers send to the collector.
- **FDCPA validation requests** (a consumer's demand that a collector prove the debt).
- **CFPB portal complaints.**

For each one it:
1. Matches the dispute to the account file.
2. Flags disputes that Reg V (the FCRA's implementing rule) lets the collector treat as frivolous or credit-repair-generated.
3. Drafts a verify, correct or delete answer that cites the evidence.
4. Sends it to a human for sign-off.
5. Keeps an investigation file that defense counsel can use.

Start with collections. The CFPB's 2011 bureau data put debt in collections at almost 40% of disputes, and it is five times as likely to be disputed as mortgage information ([CFPB, Key Dimensions](https://files.consumerfinance.gov/f/201212_cfpb_credit-reporting-white-paper.pdf)). Expand to subprime lenders, then card issuers. Sell on fewer lawsuits and faster clearance, not on replacing staff.

## Claim check

- **6.6M complaints, doubled.** True. The CFPB counted about 3.2M in 2024 ([CFPB 2025 annual report](https://files.consumerfinance.gov/f/documents/cfpb_2025-cr-annual-report_2026-03.pdf), [ABA](https://bankingjournal.aba.com/2026/04/cfpb-received-6-6m-consumer-complaints-in-2025/)). The pitch leaves out that the complaints fall almost entirely on the three bureaus.
  - FTC data cited by Bridgeforce: bureaus drew 96% of complaints, and furnishers drew 88K versus 1.26M for bureaus in 2024.
  - Furnishers reported non-seasonal dispute increases of 10–50% in 2025, not a doubling ([Bridgeforce](https://bridgeforcedatasolutions.com/fcra-litigation-and-complaints-eoy-update/)).
  - The CFPB's June 2026 overhaul is built to cut this volume. Consumers must now dispute with the bureau first and wait 45 days before complaining ([Consumer Finance Monitor](https://www.consumerfinancemonitor.com/2026/06/25/cfpb-announces-major-overhaul-of-consumer-complaint-system-a-shift-toward-integrity-standardization-and-statutory-compliance/)).
- **FCRA suits up 37% in 2025.** True: +37.4%, from 6,092 to 8,369 filings ([WebRecon](https://webrecon.com/litigation-statistics/webrecon-dec-2025-stats-year-in-review)).
- **Another 45% in the first seven months of 2026.** True: +44.6% through July ([Shipkevich](https://www.shipkevich.com/july-2026-litigation-update-fcra-filings-continue-to-climb-as-other-consumer-litigation-pulls-back-ytd-figures-still-high/)). I found no split of suits by defendant type, so the share that names furnishers rather than bureaus is not established.
- **30-day deadline and thin records losing suits.** Supported. Automated confirmations and surface reviews are often found insufficient when a suit challenges them ([Nelson Mullins](https://www.nelsonmullins.com/insights/blogs/driving-forward-developments-in-transportation-law-and-innovation/all/fair-credit-reporting-act-disputes-when-furnisher-investigations-fall-short), [Orrick on the FTC/CFPB position](https://infobytes.orrick.com/2022-09-16/ftc-cfpb-say-furnishers-must-investigate-indirect-disputes/)).

## Who else serves this customer

- **Bridgeforce** comes closest. Its DQS Disputes Module (2024) audits dispute answers against 380+ rules but does not draft them ([Bridgeforce](https://bridgeforcedatasolutions.com/credit-bureau-disputes-module/)). Its consulting arm co-built an automated workflow for direct and indirect disputes with an unnamed tech partner ([Bridgeforce](https://bridgeforce.com/services/credit-reporting-disputes/)).
- **Collection platforms** hold the account data and the workflow: Finvi (Velosidy, Katabat), Latitude, C&R Debt Manager, Beyond ARM.
- **Outsourcing firms and in-house offshore teams**, such as Genpact, Firstsource and EXL, do the manual work today.
- **AI collections vendors** only touch disputes at intake: Prodigal, CollectWise, Skit. Sei AI writes about FCRA furnisher disputes and argues for requiring human judgment on each determination ([Sei](https://www.seiright.com/blog/fcra-furnisher-accuracy-ai-decisioning-servicing)).
- I found no near-exact match. One gap: my search budget ran out before I could check whether Aktos, Finvi or Latitude already ship a module that answers ACDVs.

**Incumbent control.** No one owns this exact job. The channel and the data sit with others, though. The bureaus own e-OSCAR, and the collection platforms own the system of record, so either could bundle this in. The buying channel is compliance leads reached through ACA International, RMAI and platform partnerships.

## Ratings

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | FCRA filings rose 37.4% in 2025 and 44.6% year to date in 2026. Furnishers see 10–50% more disputes. That is less than the complaint headline suggests, but it is real. |
| Value over today | 3 | FTI puts a manual dispute at about 10 minutes ([AFSA/FTI](https://afsaonline.org/2023/01/16/how-automated-credit-dispute-handling-can-reduce-costs-by-90/)). Offshore labor at roughly $10 an hour loaded costs about $1.70 a dispute, my estimate, so $1–3 is about cost parity. The upside rests on the lawsuit-defense file, which is unproven. |
| Market size | 2 | In 2011, 32–38M disputed items came through the bureaus, about 40% of them collections. Even at 2–3x today's volume and $2 each, the furnisher dispute pool is low hundreds of millions of dollars. The 5K–50K a month band probably holds a few hundred buyers at $60K–$1.8M a year. |
| Risk (5 = low) | 3 | The e-OSCAR API and vendor addendum make access feasible. The risks are platforms bundling the feature, volume shrinking if bureau and CFPB filtering works, and plaintiffs attacking "AI verified it" the same way they attack automated confirmations. |

## What kills it and the fastest test

**What kills it.** Mid-size collectors already clear disputes offshore for under $2 each and do not trace their FCRA suits back to thin files. The product then becomes a cost swap at parity, which the collection platforms can copy.

**Fastest test.** Get three agencies or debt buyers in the 5K–50K a month band to share three numbers:
- monthly dispute count,
- fully loaded cost per dispute,
- FCRA 1681s-2(b) suits (a consumer suing a furnisher over its dispute handling) and what they cost over the last 12 months.

Then ask each for a paid pilot at $2 a dispute. It is dead if the suit cost per 10,000 disputes is small next to handling cost, or if fewer than two of the three sign.

The need is real and litigation is rising. The furnisher side of the pain is smaller than the pitch's complaint numbers imply, and the market is narrow until it reaches lenders and card issuers.

VERDICT: BACK
