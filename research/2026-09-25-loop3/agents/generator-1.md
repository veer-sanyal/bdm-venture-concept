I'd have them build an AI agent that finds, documents and collects the change orders commercial subcontractors currently lose. The runners-up worth keeping are warranty claim recovery for car dealers, tariff exposure for mid-size manufacturers that import, and disputing ocean container fees. All of this is desk research from the web. None of it is customer validation, and the key numbers still have to be measured on real projects.

## Best idea: change-order recovery for commercial subcontractors

**What it is.** Specialty subcontractors (electrical, mechanical, plumbing, drywall and so on) do most of the work on commercial jobs. Their scope changes all the time, through RFI answers, drawing revisions, a general contractor's email saying "please proceed," or extra work noted in a daily report. Most contracts require written notice within about 7–14 days, or the claim is lost. The agent would read the project's email, RFIs, drawing revisions, meeting minutes and field logs, and flag each change. It would then draft a notice that meets that contract's terms, gather the backup (hours, materials, photos) and price the change. Finally it would track the change until approved and pass it to billing.

**How it fits the seed:**
- **Work paid for by hand.** Subcontractor project managers and project engineers do this today, and outside claims consultants and lawyers are hired after a claim is lost. North American claims consulting alone is about $890M a year.
- **Size.** Specialty contractors had $1.28T in revenue across 510,803 establishments (2022 Economic Census). My rough estimate is 40,000+ firms with 20 or more employees; that figure needs checking.
- **Money lost.** Industry sources say contractors lose 2–3% of revenue to changes they never track or bill. If that holds, the loss is roughly $25–38B a year, against typical margins of 3–6%. Subcontractors also wait about 56 days to be paid on a pay application (Rabbet), and 64% say they are regularly paid late (Billd 2025).
- **The costliest slice.** A missed notice deadline makes the claim worthless, and it happens often: every project has dozens of changes. Arcadis puts the average US construction dispute at $60.1M, with failure to meet contract obligations a leading cause.
- **No incumbent on the subcontractor's side.**
  - Procore is bought by general contractors, and its agents create change records for them. A general contractor's system won't argue the subcontractor's case, which is the structural gap here.
  - Siteline ($18M raised) handles subcontractor billing and has a change-order log, but it records changes rather than finding them.
  - Document Crunch ($21.5M Series B) mostly sells contract review to general contractors.
  - An article on YC's Summer 2026 construction and proptech batch names no company doing this for subcontractors.

**Why the pitch works.** The pitch can open with a free "leak audit" of a subcontractor's active projects: find changes that are unbilled but still inside their notice window. That makes the first sale, and it also tests whether the 2–3% figure is real. Pricing can be a contingency fee on recovered changes or a small fee on active contract value.

**Start narrow, grow broad.** Start with mechanical and electrical subcontractors in the Midwest with $20–300M in revenue. Then add pay applications, retainage release, backcharge disputes, lien rights and insurance premium audits, so it becomes the subcontractor's whole back office from contract to cash. Later expand to other trades and to general contractors. Purdue's Construction Management program is a natural way to reach customers.

**Weakest points:**
1. The 2–3% loss figure comes from vendor blogs and hasn't been verified. It is the claim the pitch rests on.
2. Siteline, Procore or Document Crunch could add a similar feature.
3. Spotting changes by comparing drawing revisions is hard, and a false flag costs the PM time.
4. Subcontractors adopt software slowly and worry about looking claim-happy to the general contractor.
5. It will be hard to prove how much of a recovered change the product should get credit for.

## Runners-up

**1. Warranty claim recovery for franchised car dealers.**
- **Why it could work:** Automakers paid dealers $28B in warranty revenue in 2024, up 19.9%. Only 75–85% of claims are approved on the first submission, one vendor claims 5–15% of warranty revenue is lost, and failed automaker audits can mean six-figure chargebacks. There are about 16–17k dealers, each paying warranty administrators to do this by hand.
- **Weakest:** It breaks the seed's rule. The dealer management systems (CDK, Reynolds) hold the data and the buying channel, automakers' portals resist automation, and small AI players such as Forge AI already exist.

**2. Tariff exposure for mid-size manufacturers that import, starting with the Section 232 metals rules.**
- **Why it could work:** Since April 2026, derivative products pay 25% on their full value, products made with US-melted metal pay 10%, and unknown metal origin can trigger 200%. Customs duties reached $167B in fiscal 2026 through August. The supplier origin data sits in email and mill certificates, and no software company holds it. It suits Indiana's many manufacturers.
- **Weakest:** The rules change overnight. The Supreme Court struck down the IEEPA tariffs in February 2026, and the Section 122 tariffs expired in July. The field is also crowded: Gaia Dynamics raised $7M this month, and Zollback and Flexport are active. Filing requires a licensed customs broker.

**3. Disputing ocean container fees (demurrage and detention) under the Federal Maritime Commission's billing rule.**
- **Why it could work:** US importers paid about $4.2B in demurrage in 2024. About 31% of charges are disputed and 44% of those are won, so roughly 14% is avoidable. Under the rule, an invoice missing required fields doesn't have to be paid, and disputes have a 30-day window.
- **Weakest:** The pool is small, around $0.6B a year recoverable, and little of it is labor spend that AI would replace. Freight forwarders and tracking platforms hold the data, and a 2025 appeals ruling struck down the part of the rule on who can be billed.

## Considered and dropped

| Idea | Why dropped |
|---|---|
| Defense-contractor cybersecurity certification (CMMC) | The Defense Department suspended Phase 2 in July 2026 |
| Duty drawback | Zollback and old-line brokers are there, and it depends on tariff policy |
| Retailer deductions for consumer-goods brands | Glimpse raised $35M |
| Property tax appeals | Ownwell raised $50M and has a commercial product |
| Nursing-home Medicaid applications | PointClickCare holds the data, and CoreCare and ExaCare are already in |
| Construction contract review | Document Crunch |

Sources:
- [Census NAICS 238 profile](https://data.census.gov/profile/238_-_Specialty_Trade_Contractors?codeset=naics%7E238)
- [Aezion on disputed change orders](https://www.aezion.com/blogs/disputed-change-order-costs)
- [Rabbet on slow payments](https://rabbet.com/blog/how-slow-payments-impact-the-entire-construction-industry)
- [Arcadis 2025 Construction Disputes Report](https://media.arcadis.com/-/media/project/arcadiscom/com/expertise/global/contract-solutions/2025/2025-15th-annual-construction-disputes-report-final-19jun25.pdf?rev=8569d68da4d44425ab37c911e699640c)
- [Growth Market Reports, claims consulting market](https://growthmarketreports.com/report/construction-claims-consulting-service-market)
- [Siteline change-order log](https://www.siteline.com/blog/change-order-log)
- [Document Crunch raise](https://app.dealroom.co/news/feed/document-crunch-raises-21-5m-for-ai)
- [Engineering.com on Procore agents](https://www.engineering.com/procore-expands-ai-tools-with-construction-workflow-agents/)
- [MarketScale on YC Summer 2026 construction batch](https://www.marketscale.com/industries/engineering-and-construction/ycs-summer-2026-cohort-floods-construction-and-proptech-with-ai-back-office-tools)
- [Claimlane on dealer warranty management](https://www.claimlane.com/resources/blog/dealership-warranty-management)
- [Forge AI blog](https://www.forgedrive.ai/blog)
- [Foley on 2026 Section 232 rules](https://www.foley.com/insights/publications/2026/05/what-every-multinational-should-know-about-the-new-rules-for-section-232-tariffs-on-steel-aluminum-and-copper-derivatives/)
- [Global Trade Alert on Section 232](https://globaltradealert.org/reports/Section-232-Metal-Content-Calculus-Explained)
- [USAFacts on tariff revenue](https://usafacts.org/answers/how-much-revenue-does-the-federal-government-collect-from-tariffs/country/united-states/)
- [Gaia Dynamics seed round](https://www.prnewswire.com/news-releases/gaia-dynamics-raises-7m-to-expand-ai-platform-keeping-businesses-ahead-of-tariffs-and-trade-risk-302880240.html)
- [Zollback launch](https://www.zollback.com/blog/tariff-refunds-for-smbs)
- [Mallory on demurrage and detention](https://www.mallorygroup.com/blog-posts/demurrage-vs-detention-definitions-charges-and-how-to-dispute)
- [Cubic demurrage and detention playbook](https://www.gocubic.io/guides/cost-optimization/demurrage-detention-dispute-playbook-2026)
- [FMC on the appeals court decision](https://www.fmc.gov/articles/u-s-court-of-appeals-issues-decision-in-case-on-demurrage-and-detention-billing-practices/)
- [FCA Counsel on the CMMC pause](https://www.fcacounsel.com/blog/dod-cmmc-level-2-pause)
- [Steptoe on IEEPA refunds](https://www.steptoe.com/en/news-publications/global-trade-and-investment-law-blog/status-of-ieepa-tariff-refunds-following-us-supreme-court-decision.html)
- [Glimpse](https://www.tryglimpse.com/post/how-to-dispute-unfi-deductions)
- [HousingWire on Ownwell](https://www.housingwire.com/articles/ownwell-property-tax-appeal-funding/)
- [CoreCare](https://corecare.ai/)
