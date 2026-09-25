I recommend a company that proves what's inside an imported product and where its metal was made, starting with Section 232 metal tariffs for mid-sized US manufacturers and distributors. All of this comes from web research, so none of it is customer validation yet. Interviews with importers and brokers are the next step.

## Best idea: evidence for Section 232 metal content and origin

**The work being paid for.** About 330,000 importers paid the IEEPA tariffs the Supreme Court struck down in February 2026. That gives a rough count of active US importers. They pay for customs work today in three ways:
- **Customs brokers:** the US brokerage market was about $5.2B in 2024.
- **Their own staff:** in-house trade compliance people, or often a logistics manager or controller doing it on the side.
- **Outside firms:** trade lawyers, Big 4 consultants, and refund and drawback firms paid only on contingency.

**The costly slice: Section 232 duties on steel, aluminum and copper in finished goods.** Mistakes here are the most expensive and happen on every shipment:
- **A cliff at 15% metal by weight.** Since April 6, 2026, a product whose weight is under 15% covered metal pays 0%. At or over the line it pays 25% or 50%, charged on the whole product's value, not just the metal.
- **Origin changes the rate.** Since June 8, 2026, the rate also depends on origin: 25% for most countries, 15% for 37 trade-deal partners, and 10% for goods made from at least 85% US metal.
- **Missing paperwork defaults to the worst case.** Global Trade Alert puts it as "missing data triggers worst-case defaults": full value, or up to 200% for aluminum when the smelting country is unknown.
- **The rules keep changing.** They changed in April and June. From September 14, CBP's entry system rejects filings that lack copper smelt and cast countries.
- **Mistakes go both ways.** Paying too much is silent, because CBP doesn't flag overpayment, and refunds are only possible within 300 days of entry or within 180 days of a later protest. Paying too little leads to penalties and False Claims Act cases. DOJ's trade-fraud task force has recovered over $1B, including a $549.5M aluminum settlement in May 2026. Many UFLPA forced-labor detentions are now automotive castings and components, and detained shipments are rarely released.

**What buyers use today, including the free options:**
- **Customs brokers and freight forwarders.** Compliance help comes bundled with the per-entry fee, but brokers file whatever the importer tells them.
- **Contingency recovery firms** such as Duty Discovery, Zollback and the IEEPA refund firms. They charge nothing up front, but they only look backward and only for overpayments.
- **AI classification tools:** Gaia Dynamics ($7M seed, about 800 accounts), Tarifflo, GingerControl ($2.1M seed) and Digicust.
- **Pax AI,** which sells automated entry audits.
- **Assent,** survey-based collection of supplier smelt and melt data, priced for large enterprises.
- **Law firms and consultants.**

**What AI can do that none of these can:**
1. **Work out metal weight from the importer's own engineering files.** It can compute the steel, aluminum and copper share of each product from bills of materials, drawings, CAD files and spec sheets. Brokers take the importer's word for it, and Assent waits for suppliers to fill in surveys. This fits Purdue engineering well.
2. **Collect supplier evidence automatically, in any language.** Agents can chase suppliers two or three levels down and read mill certificates in Chinese, Vietnamese or Spanish. They can then match heat numbers to shipments and build a file per product ready for a CBP request.
3. **Re-check every product each time a proclamation lands.** It can flag items near the 15% line and suggest redesign or sourcing changes that move them under it or into the 10% US-metal tier.
4. **Act before and after filing.** It can push the correct declaration to the broker before the entry is filed. Afterwards it can file refund corrections or protests before the windows close, and prepare voluntary disclosures before CBP finds a problem. Recovery-only firms have a reason not to point out underpayments. This product doesn't, which makes it the importer's own advocate.

**Path from narrow to broad.** Start with 232 metals. The same evidence about content and origin also feeds other 232 sectors, USMCA qualification, antidumping duty scope, forced-labor traceability, and the EU carbon border tax (which asks for the same melt and pour data). Together that makes a product-level record of trade facts that brokers pull from.

**Market.** Section 232 was about a third of the new 2025 tariff revenue. That puts 232 duties at tens of billions of dollars a year. The spend being replaced is brokerage, in-house compliance staff and consultants, which adds up to billions. These are rough estimates.

**Business model.** A subscription priced per active product or per entry line, with an optional share of recovered refunds.

**Weakest points:**
- **Policy risk is the biggest.** A trade deal or a new administration could cut 232 rates. The counterargument is that 232 has lasted since 2018 across both parties, and origin and content rules keep multiplying.
- **I found no count of importers who actually pay 232 duties.** That is the first number to get.
- **Tier-2 foreign mills may simply refuse to share data.**
- **If the product gets a weight wrong, the importer faces penalties.** A licensed broker or attorney needs to review the output, and the company needs errors-and-omissions insurance.
- **Well-funded neighbors could add a similar module.** Gaia and Assent are the likeliest.
- **Mid-sized manufacturers are slow buyers.**

**First validation step.** Interview about 20 Indiana manufacturers and 5 brokers. Ask each for their last 50 entries with 232 lines. Count how many lack evidence or sit near the 15% line, and ask what they would pay to fix it.

## Runner-up 1: change-order capture for specialty subcontractors

**Buyers.** There are about 511,000 specialty trade contractor establishments, with $1.28T in receipts in 2022. In a Dodge/Clearstory study, 77% had written off completed change-order work as bad debt. It takes about 48 days from signed work ticket to approved change order, and 53% of general contractors cite weak backup documentation as a reason to cut payments. Contract notice windows can be 48 hours, and missing one forfeits the claim.

**Incumbents.** Procore (free for subs when the general contractor pays), TracFlo, TrakSlip, Rhumbix, Clearstory, Document Crunch ($12.6M revenue), drawing-comparison tools like iFieldSmart and Articulate, and hourly claims consultants.

**What AI adds.** These tools track changes once someone notices them. AI can catch the changes nobody noticed, by reading every drawing revision, RFI answer, email and daily log against the sub's bid scope. It can then send notice within the contract window and assemble the backup automatically.

**Weakest.** It's a crowded category, subs are slow to adopt technology, recovered dollars are hard to attribute to the product, and Procore could bundle something similar.

## Runner-up 2: independent 100% claims review for self-funded employers

**Buyers.** 67% of covered workers are in self-funded plans, and the employer carries the fiduciary duty for paying claims correctly. Most plans review fewer than 5% of claims, while a full review typically recovers 1–3% of claims spend.

**Incumbents.** The claims administrators themselves (who have a conflict of interest), benefits brokers paid by commission, sample-based audit firms, and ClaimInformatics, Klaims.ai and Benosphere.

**Weakest.** Getting the claims data takes administrator cooperation, their contracts can limit audits, several competitors already exist, and brokers act as gatekeepers.

## Dropped
- **Customs refund and overpayment recovery:** too crowded (Tarifflo, Pax, Duty Discovery, Zollback), and the IEEPA refunds are a one-time event.
- **Lease operating-cost (CAM) audits and commercial property tax appeals:** there are already $79 AI tools and cheaper contingency firms, so AI would mostly be doing the same job cheaper.
- **Nursing-home reimbursement coding (MDS/PDPM), dealership warranty claims and roofing insurance supplements:** each already has AI entrants with traction (for example PointClickCare, Forge AI and XBuild), and I found no clear capability gap.

Sources:
- [Skadden on the IEEPA ruling](https://www.skadden.com/insights/publications/2026/02/the-supreme-court-ends-ieepa-tariffs)
- [Jackson Walker on the IEEPA refund order appeal](https://www.jw.com/news/insights-ieepa-refund-order/)
- [BDO on the April 2026 Section 232 changes](https://www.bdo.com/insights/tax/section-232-metals-tariffs-expanded-and-recalibrated-what-importers-need-to-know)
- [Global Trade Alert, June 2026 Section 232 update](https://globaltradealert.org/blog/s232-metals-update-june-2026)
- [Global Trade Alert on metal-content rules](https://globaltradealert.org/reports/Section-232-Metal-Content-Calculus-Explained)
- [FifthRow on Section 232 in 2026](https://www.fifthrow.com/blog/section-232-tariff-2026-full-value-metal-duties-hts-codes-and-compliance-strategies)
- [UHY on September copper reporting](https://uhy-us.com/insights/news/2026/april/section-232-tariff-changes-could-raise-costs-for-importers-of-steel-aluminum-and-copper-products)
- [Morgan Lewis on the Perfectus FCA settlement](https://www.morganlewis.com/pubs/2026/05/doj-announces-major-fca-settlement-relating-to-evaded-customs-duties)
- [EDRM on the DOJ task force passing $1B](https://edrm.net/2026/07/doj-and-dhs-issue-trade-fraud-guide-as-task-force-tally-exceeds-1-billion/)
- [Holland & Knight on forced-labor guidance](https://www.hklaw.com/en/insights/publications/2026/07/new-compliance-tools-cbp-issues-comprehensive-forced-labor-guidance)
- [Kharon on UFLPA enforcement](https://www.kharon.com/resources/use-cases/forced-labor/uflpa-enforcement-and-compliance-strategy)
- [Penn Wharton tariff revenue, Sept 2026](https://budgetmodel.wharton.upenn.edu/p/2026-09-09-effective-tariff-rates-and-revenues-updated-september-9-2026/)
- [US customs brokerage market size](https://finance.yahoo.com/news/united-states-customs-brokerage-market-173900825.html)
- [Gaia Dynamics $7M seed](https://www.prnewswire.com/news-releases/gaia-dynamics-raises-7m-to-expand-ai-platform-keeping-businesses-ahead-of-tariffs-and-trade-risk-302880240.html)
- [GingerControl seed](https://www.trysignalbase.com/news/funding/gingercontrol-secures-21m-seed)
- [Assent on Section 232](https://www.assent.com/blog/prepare-for-section-232-tariffs/)
- [Duty Discovery launch](https://www.prnewswire.com/news-releases/financial-recovery-strategies-and-profittrust-partner-to-launch-duty-discovery-bringing-ai-powered-customs-duty-recovery-to-importers-nationwide-302878027.html)
- [Tarifflo duty recovery](https://news.marketersmedia.com/ai-platform-by-tarifflo-inc-recovers-millions-in-overpaid-us-import-duties/89193635)
- [Zollback launch](https://www.zollback.com/blog/tariff-refunds-for-smbs)
- [Dodge/Clearstory change-order research](https://www.clearstory.build/construction-blog/2026-sc-change-order-report)
- [Census, NAICS 238](https://data.census.gov/profile/238_-_Specialty_Trade_Contractors?codeset=naics%7E238)
- [Document Crunch Series B](https://www.documentcrunch.com/news/series-b)
- [Billd on notice deadlines](https://billd.com/blog/construction-contract-negotiation-part-2/)
- [KFF 2025 employer survey](https://www.kff.org/health-costs/2025-employer-health-benefits-survey/)
- [Benosphere on the 5% review problem](https://benosphere.com/blog/self-funded-claims-audit-5-percent-problem)
- [CAMAudit software](https://www.camaudit.io/cam-audit-software)
- [Ownwell $50M](https://www.housingwire.com/articles/ownwell-property-tax-appeal-funding/)
- [XBuild supplements guide](https://blog.x.build/blog/what-is-an-insurance-supplement-roofing-contractor-guide)
