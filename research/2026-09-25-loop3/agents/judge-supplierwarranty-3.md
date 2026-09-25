I rate the concept as pitched a pass. The main problem is that the biggest Detroit automakers bill suppliers by formula, so most individual charges have no evidence to match against and can't be disputed one at a time.

Two limits on this research. The web search limit (200 per session) ran out partway through, so I only have primary documents for Stellantis's terms, not GM's or Ford's. The competitor scan is also thinner than I'd like. As you asked, I didn't read the local project files.

## Checking the key claims

- **"US suppliers paid $468M in warranty claims in one quarter of 2023": the number is right, but it doesn't measure what the pitch says.** [Warranty Week (Dec 2023)](https://www.warrantyweek.com/archive/ww20231214.html) confirms $468M for Q3 2023. But that figure is total warranty claims paid by publicly listed US parts companies. The biggest payers in the [2025 data](https://www.warrantyweek.com/archive/ww20260604.html) are Cummins ($730M), O'Reilly ($250M), Wabtec and Brunswick. Those are an engine maker's own warranties, an auto-parts retailer, a rail company and a boat maker. Very little of it is automakers charging suppliers.
- **The accounting-firm quote is real but 12 years old.** It comes from [Plante Moran, April 2014](https://www.plantemoran.com/explore-our-thinking/insight/2014/06/warranty-claims-a-hidden-financial-risk-for-auto-suppliers).
- **The 50/50 split isn't sloppiness. It is written into the contracts.**
  - Stellantis's [Global Warranty Terms](https://www.esupplierconnect.com/irj/go/km/docs/SC_Suppliers/Anonymous%20Site/GLOBAL_Reference_docs/Global_Warranty_Terms_effective_1_1_2022.pdf) and its [North America procedures](https://www.esupplierconnect.com/irj/go/km/docs/SC_Suppliers/Anonymous%20Site/GLOBAL_Reference_docs/Warranty_Terms_Implementation_Procedures_for_NA.pdf) start every supplier at a 50% share. That share is then reset by analysing a sample of 30 returned parts, and the new share applies to every claim in that part group.
  - If the supplier misses the analysis deadline, the part counts as the supplier's fault.
  - Stellantis takes the charge straight out of the money it owes the supplier each month. The North America procedures give the supplier 5 business days to dispute a debit.
  - The global terms say disputes "may in no case call into question" that percentage or the supplier's liability.
  - [Foley & Lardner (2022)](https://www.mondaq.com/unitedstates/contracts-and-commercial-law/1174320/oems-expanding-suppliers-responsibility-for-ordinary-warranty-claims) and the [National Law Review (2023)](https://natlawreview.com/article/warranty-and-pricing-disputes-between-suppliers-and-oems-trends-pitfalls-and) describe the same formula approach, where the automaker doesn't have to show the part was defective. GM brought in a 50/50 rule in [2010](https://www.providers-administrators.com/news/gm-provision-to-split-warranty-costs-50-50-concerns-suppliers) and a [new chargeback process in 2021](https://wolfsonbolton.com/news-updates/2021/september/client-alert-gm-imposes-new-warranty-chargeback-process/).
- **So the core workflow doesn't fit.** "Match each claim to the returned-part analysis" assumes every claim has an analysis behind it. Under these contracts only the 30 sampled parts are ever analysed. What a supplier can still challenge on an individual claim is the arithmetic and the attribution: duplicates, the wrong part or supplier code, cost errors, and charges already billed under a recall or campaign.

## Who else serves this customer

- **Nobody I found owns the supplier's buying channel for this.**
  - Warranty software vendors (Tavant, SAP, Syncron, Bruviti, Circuitry.ai, Intellinet) sell to automakers to help them recover *more* from suppliers.
  - Claimlane helps retailers and brands charge their suppliers back.
  - Suppliers today use their own quality engineers, Plante Moran-style advisers, and Detroit law firms for the large disputes.
- **The automakers own the data.** Charges and supporting claim details sit in the automakers' own systems (for Stellantis: SAWRP+, SWRS and PRAS+; also GM SupplyPower and the Ford Supplier Portal). The supplier's side of the evidence sits in its quality-management software.
- **The "other industries" expansion already has players.** Retail deductions and chargebacks for consumer-goods suppliers already have tools such as HighRadius, iNymbus and SupplyPike. I didn't verify their current status because the search limit ran out.
- **Paying on results works in a neighbouring market.** Dealer warranty-reimbursement firms such as jlwarranty charge contingency fees on the dealer-to-automaker side.

## 1. The strongest version

The company should defend the supplier's liability percentage, not dispute claims one by one.

- **Win the sample.** Track every returned part in the 30-part sample against the automaker's deadline. Build the evidence for each "no trouble found" (tested and found no defect), assembly-plant or adjoining-component call, and push reclassifications within the 30-day window.
- **Audit every monthly debit.** Check each debit against the contract's cost formula, the part group, duplicates, and overlaps with recalls and campaigns, and file within the 5-day window.
- **Charge a share of the savings.** Take a percentage of the reduction in the liability share times the billed amount, plus a share of reversed debits.

One point off a supplier's share applies to a whole model year of claims, so this is where the money is. Target customers are mid-size Tier 1 and Tier 2 suppliers with Stellantis, GM and Ford exposure. RV is unverified: RV component suppliers often deal with dealers directly rather than being charged by the RV maker.

## 2. Ratings

| Area | Score | Evidence |
|---|---|---|
| Customer need | 3 | Stellantis starts suppliers at 50% and counts late analyses as the supplier's fault. [Cooper-Standard's 2025 annual report](https://automotiveintel.substack.com/p/youre-selling-the-part-and-financing) flags warranty costs "over which we have little or no control." |
| Value over today | 2 | Contracts bar disputes over the liability share, allow 5 days to dispute a debit, and have no per-claim evidence to match. The real lever is lab analysis of returned parts, which is engineering work, not drafting documents. |
| Market size | 2 | Suppliers pay about [10–17% of automaker claims](https://www.warrantyweek.com/archive/ww20190418.html). US-based car and light-truck makers paid $2.94B in Q3 2023, so roughly $1.2–2B a year is charged to suppliers. Only a fraction of that can be reversed, which caps contingency revenue in the tens of millions. |
| Risk (5 = low) | 2 | The automakers own the data systems and set the contract terms. Suppliers fear losing future contracts if they dispute. |

## 3. What would kill it, and the fastest test

**What kills it:**
- Automaker charges turn out to be accurate once the liability share is fixed.
- Suppliers won't file disputes for fear of losing future business.
- The automakers' systems can't be exported cleanly.

**The single fastest test:** get 3 Midwest Tier 1 or Tier 2 suppliers to share their last 12 months of warranty debit files from Stellantis or GM, plus their warranty terms and sample-analysis records. Audit them in 2 weeks.
- Kill it if contract-valid errors come to less than about 3% of dollars charged.
- Also kill it if fewer than 2 of the 3 would file those disputes on next month's debit.

VERDICT: PASS
