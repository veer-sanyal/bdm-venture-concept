**Verdict:** the pain is real but mostly lands on the big three bureaus. There is at least one incumbent already piloting this exact product. Nobody has published a per-dispute cost, so the market size below is an estimate.

## 1. Complaint and dispute volumes

- **CFPB complaints.** The CFPB received about 6.6M complaints in 2025, up from about 3.2M in 2024 and 1.6M in 2023. Credit reporting was 5.8M of them (88%), up 115% on 2024. Sources: [CFPB 2025 annual report](https://www.consumerfinance.gov/data-research/research-reports/2025-consumer-response-annual-report/), [Orrick](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/), [American Banker](https://www.americanbanker.com/news/cfpb-makes-changes-to-complaint-portal-citing-abuse). The claim checks out.
- **Is AI the cause?** Partly. The CFPB names four causes: credit repair organizations, social media influencers, "large language models and AI agents," and new businesses that dispute accurate information ([Orrick](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/), [CU Today](https://www.cutoday.info/Fresh-Today/CFPB-Overhauls-Complaint-Portal-After-Credit-Reporting-Cases-Surge-3-700)). Saying the surge is "driven by AI-written disputes" overstates it. AI is one of four named causes.
- **Complaints are mostly about the bureaus, not furnishers.** From Jan 2024 to Jun 2025, about 3.9M of 4.8M credit reporting complaints named the three largest bureaus ([CFPB FCRA 611(e) report, Dec 2025](https://files.consumerfinance.gov/f/documents/cfpb_fcra-611e-report_2025-12.pdf)). Complaints against creditors and debt collectors went from about 159k in 2024 to about 302k in 2025 ([WebRecon](https://webrecon.com/litigation-statistics/webrecon-dec-2025-stats-year-in-review)). That 302k is the number that matters for this product.
- **The CFPB is cutting complaint volume.** In June 2026 it added two-factor login and identity and address checks. Consumers must now wait 45 days after a bureau dispute before filing, and companies get new codes for closing frivolous complaints ([American Banker](https://www.americanbanker.com/news/cfpb-makes-changes-to-complaint-portal-citing-abuse)).
- **e-OSCAR volume (e-OSCAR is the bureaus' system for sending disputes to furnishers).** I could not find a current figure. The most recent official one is from 2012: about 8M consumers a year disputed 32 to 38M items, and 85% went to furnishers as ACDVs, the electronic dispute forms furnishers must answer. That is roughly 27 to 32M a year ([CFPB white paper](https://files.consumerfinance.gov/f/201212_cfpb_credit-reporting-white-paper.pdf)). One vendor survey of furnishers reports "non-seasonal dispute increases of 10–50%" in 2025 ([Bridgeforce](https://bridgeforcedatasolutions.com/fcra-litigation-and-complaints-eoy-update/)).
- **Direct disputes (consumers writing straight to the lender).** I found no volume figure anywhere.

## 2. Litigation and regulators

- **Lawsuit counts.** 8,369 FCRA suits were filed in 2025, up 37.4% ([WebRecon](https://webrecon.com/litigation-statistics/webrecon-dec-2025-stats-year-in-review)). Through July 2026 there were 6,305, up 44.6% year to date, with 1,134 in July alone ([Shipkevich citing WebRecon](https://www.shipkevich.com/july-2026-litigation-update-fcra-filings-continue-to-climb-as-other-consumer-litigation-pulls-back-ytd-figures-still-high/)). About 44% of plaintiffs had sued before, and class actions are about 1.3% of filings ([WebRecon](https://webrecon.com/litigation-statistics/webrecon-dec-2025-stats-year-in-review)).
- **Split between furnishers and bureaus.** Not published anywhere I could find.
- **Typical settlements.** Not verified. Law firm blogs say individual claims resolve for $1,000 to $5,000 plus the defendant paying the plaintiff's attorney fees ([BLG](https://www.blgwins.com/average-fcra-settlement-what-you-need-to-know/)). That is marketing copy, not data. One tail case: a furnisher that lost on "unreasonable investigation" paid over $100k in damages plus nearly $400k in fees ([Privacy World](https://www.privacyworld.blog/2020/05/beware-fcra-dangers-court-awards-400k-in-attorneys-fees-to-plaintiff-after-trial-win-but-defendant-avoids-potential-165mm-in-punitive-damages/)).
- **What courts want.** Defense counsel say furnishers win by showing "detailed investigation records" ([Bloomberg Law](https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/credit-reporting-litigation-to-rise-further-given-state-laws)). That is the product's best argument.
- **Federal regulators.** On May 12, 2025 the CFPB withdrew 67 guidance documents, including Bulletin 2014-01 on furnisher investigation duties ([Troutman](https://www.troutman.com/insights/regulatory-rollback-inside-the-cfpbs-fcra-guidance-withdrawal/)). Enforcement is paused or cut back ([Bloomberg Law](https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/credit-reporting-litigation-to-rise-further-given-state-laws)). In November 2025 the CFPB also said federal law overrides state credit reporting laws ([Holland & Knight](https://www.hklaw.com/en/insights/publications/2025/11/cfpb-confirms-federal-preemption-of-state-credit-reporting-laws)). Private lawsuits now carry the risk, not regulators.
- **State attorneys general.** I found no specific 2025 or 2026 action against furnishers.

## 3. How furnishers handle disputes today

- **Existing vendor, closest to this idea.** Bridgeforce Data Solutions sells the Data Quality Scanner, which has a Disputes Module and an "AI Agent Assist" built on Amazon Bedrock ([announcement](https://bridgeforcedatasolutions.com/bridgeforce-data-solutions-announces-first-ai-product/)). In May 2026 it previewed an "AI Resolution Engine for Credit Bureau Disputes," now in pilot ([Bridgeforce](https://bridgeforcedatasolutions.com/press-release-dqs-cdia/)). It also sells tools for overseeing outsourced dispute agents ([Bridgeforce](https://bridgeforcedatasolutions.com/credit-bureau-dispute-agent-training-vendor-oversight-dqs/)), which confirms that furnishers outsource this work. Its marketing is aimed at large issuers and servicers.
- **FTI Consulting** built a prototype for automating dispute checks. It claims a 90% cost cut, with one validation step taking one minute instead of about ten ([AFSA](https://afsaonline.org/2023/01/16/how-automated-credit-dispute-handling-can-reduce-costs-by-90/)).
- **e-OSCAR itself** now sells API access to furnishers for a setup fee plus tiered monthly pricing, with no public numbers ([e-OSCAR](https://www.e-oscar.org/services-by-e-oscar)).
- **Adjacent tools that are not direct competitors.** Quavo and FINBOA handle card and payment disputes under Reg E and Reg Z, not credit bureau disputes ([Quavo](https://www.quavo.com/), [FINBOA](https://www.finboa.com/)). Switch Labs and Hutchins sell Metro 2 reporting software, where Metro 2 is the file format furnishers send to the bureaus ([Switch Labs](https://metro2.switchlabs.dev/metro2/best-metro-2-reporting-software)).
- **Outsourcing firms (Firstsource, Conduent, iQor).** I could not confirm that any of them handles ACDVs for lenders. Firstsource's collections arm does show up as a furnisher ([Crediful](https://www.crediful.com/collection-agencies/firstsource-advantage/)).
- **AI startups.** Searches of YC listings and 2024 to 2026 funding news turned up no startup focused on furnisher-side dispute handling. The nearest is Disputed.ai, which handles merchant chargebacks and raised $1.1M ([FinTech Global](https://fintech.global/2025/03/14/disputed-ai-raises-1-1m-to-revolutionise-ai-powered-chargeback-management/)). Absence in search results does not prove the space is empty.
- **Cost per dispute and team headcount.** No public figure exists.

## 4. Bottom-up market size (my assumptions are labeled)

- **Furnishers.** About 10,000 in 2012 ([CFPB](https://files.consumerfinance.gov/f/201212_cfpb_credit-reporting-white-paper.pdf)). No current count is published.
- **ACDVs per year.** 27 to 32M in 2012 terms. Assumption: 1.5 to 2x that now, so 40 to 60M.
- **Cost per ACDV.** Assumption: about 10 minutes of analyst time (implied by FTI's one-minute-equals-10% claim) at $30 an hour fully loaded, so about $5. The real number could be anywhere from $2 to $15.
- **Labor spend.** Roughly $200M to $300M a year on bureau disputes. Direct disputes and CFPB complaint handling add an unknown amount.
- **What software could capture.** Assumption: 20 to 40% of that labor spend, so about $40M to $120M a year. A per-dispute fee of $1 to $2 across 50M ACDVs gives $50M to $100M.

So this is a solid niche business, not a large market, unless the product widens into furnisher compliance overall: data quality, complaint handling and litigation defense.

## 5. My read

**Best first customer.** A debt collector or debt buyer, or a subprime auto or installment lender, in the mid-market (roughly 5k to 50k disputes a month). These firms get disproportionately many template disputes, get sued often (44% of plaintiffs have sued before), run lean teams, and are small enough to buy without a year of bank vendor review.

**What they would pay.** About $1 to $3 per dispute, or $50k to $250k a year. The pitch is replacing an $8 manual review plus reducing lawsuits. Those prices are my estimate; I found no market data.

**Biggest risks.**
1. The incumbent is inside the pipe. Bridgeforce is already piloting AI resolution with the same customers, and e-OSCAR now sells its own API. Either can ship this as a feature.
2. Liability. If the product labels a dispute "frivolous" and gets it wrong, that decision becomes Exhibit A in a failure-to-investigate lawsuit. Plaintiff lawyers will attack automated "parroting" of records, which is exactly the product. It has to produce a defensible investigation record, not auto-verify disputes.
3. The problem may shrink. The June 2026 CFPB portal changes and possible bureau-side filtering could cut the flow of template disputes before a startup reaches scale.

**Numbers I could not verify.** Current e-OSCAR volume, direct dispute volume, cost per dispute, furnisher dispute headcount, typical settlements, the furnisher-versus-bureau split of lawsuits, and whether the named outsourcing firms handle ACDVs.
