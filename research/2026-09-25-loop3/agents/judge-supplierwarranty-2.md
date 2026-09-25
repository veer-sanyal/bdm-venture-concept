I rate this a pass. The pain is real, but the pitch misreads its headline number, and the way automakers write their contracts removes much of the per-charge dispute the product is built around. Supplier-side competition is not the problem.

## What the primary sources show

- **The $468M figure is real but describes something else.** Warranty Week's number for Q3 2023 is the total warranty cost reported by 62 US-listed "auto parts" companies, including Cummins, O'Reilly and Wabtec ([WW, Dec 2023](https://www.warrantyweek.com/archive/ww20231214.html)). Much of that is those companies' own product warranties to their customers, not charges from automakers. It also leaves out private and foreign suppliers. The 2024 full-year figure is $2.06B ([WW, Apr 2025](https://www.warrantyweek.com/archive/ww20250403.html)). A closer measure of what automakers charge suppliers: in 2012 they recovered about $1.37B from suppliers, against a theoretical $2.7B ([WW, 2013](https://www.warrantyweek.com/archive/ww20130411.html)).
- **The Plante Moran quote is accurate but dates from 2014** ([source](https://www.plantemoran.com/explore-our-thinking/insight/2014/06/warranty-claims-a-hidden-financial-risk-for-auto-suppliers)). Its list of 50/50 splits, goodwill repairs on ineligible parts, excessive labor and duplicate repairs matches what lawyers still describe ([NatLawReview](https://natlawreview.com/article/warranty-and-pricing-disputes-between-suppliers-and-oems-trends-pitfalls-and)).
- **Stellantis's Global Warranty Terms change the picture** ([PDF](https://fcagroup.esupplierconnect.com/irj/go/km/docs/SC_Suppliers/Anonymous%20Site/GLOBAL_Reference_docs/Global_Warranty_Terms_effective_1_1_2022.pdf)):
  - Everyday warranty charges are not decided claim by claim. They equal a percentage (the "Technical Factor") times the repair costs.
  - That percentage starts at 50%, which is where the "50/50" comes from, and is capped at 50%.
  - It is then recalculated from a small sample of returned parts that the supplier analyzes. Each part is weighted by category: 0.5 if the part was faulty, 0.25 if no fault was found, 0.25 if another part caused the damage.
  - If the supplier misses the analysis deadline, the part counts as faulty.
  - Disputes must be raised within 30 days of the invoice, and they "may in no case call into question the Technical Factor."
  - Lawyers describe the same model industry-wide: a flat split or a sample extrapolated to all claims, with no root-cause proof needed ([Mondaq](https://www.mondaq.com/unitedstates/contracts-and-commercial-law/1174320/oems-expanding-suppliers-responsibility-for-ordinary-warranty-claims)).
  - GM changed its chargeback process in 2021 in ways expected to raise supplier charges ([Wolfson Bolton](https://wolfsonbolton.com/news-updates/2021/september/client-alert-gm-imposes-new-warranty-chargeback-process/)). I could not get GM's or Ford's primary terms.

## Who already serves these customers

- **Automakers own the data and the channel.** Claim detail sits in their supplier portals, and they deduct charges straight from what they owe the supplier.
- **SAP is the closest supplier-side incumbent.** Its supplier warranty product ingests automaker quality data and tracks the Technical Factor agreements ([Detering](https://www.deteringconsulting.com/blog/sap-automotive-supplier-fast-start)). It organizes the work but does not win money back. Large Tier 1s run it with their own warranty teams.
- **Law firms and accountants** handle recalls and large disputes.
- **Other vendors sell to the other side.** Tavant-style tools, ServiceCPQ, Claimlane and Intelli work for automakers recovering money from suppliers.
- **The closest match is Vendormint, in retail.** It disputes retailer deductions for suppliers for a 30% contingency fee ([Vendormint](https://vendormint.com/)), which shows the pricing model works there.

I found no company doing this for manufacturing suppliers. That scan is incomplete, though: my web search limit ran out partway through. RV industry warranty practices are also unverified.

## 1. The strongest version

This is dispute and recovery for mid-size Tier 1 and Tier 2 industrial suppliers, covering every charge an automaker deducts from them. It would lead with defending the warranty percentage rather than disputing single charges:

- Manage each returned-part sample to its deadline.
- Draft the analysis reports that push parts from "faulty" into "no fault found" or "caused by another part." Under Stellantis's example 25-part sample, each part moved lowers the percentage by 1 point on every future claim.
- Check each invoice within the 30-day window for claims outside the part's group, labor overcharges, extra parts added to the repair, duplicates and out-of-warranty claims.
- Later, extend to quality and containment charges, premium freight and self-billing price errors.
- Start with Tier 2s, who get charges passed down from Tier 1s with less evidence and have less staff to fight them.

## 2. Ratings

| Area | Score | Evidence |
|---|---|---|
| Customer need | 3 | Lawyers report these disputes "heating up," but charges are formula-based by contract, which limits how many single charges are provably wrong. |
| Value over what customers use today | 3 | Suppliers use in-house engineers, SAP and outside counsel. AI helps meet the 30-day and sample deadlines, but the biggest lever is physical teardown of parts, not reading documents. |
| Market size | 2 | Supplier warranty spend is about $2B a year even including their own warranties. If maybe 10% is wrong and reversible, a ~25–30% fee yields tens of millions a year in US auto. |
| Risk (5 = low) | 2 | The percentage cannot be disputed on the invoice. Automakers deduct first, settle disputes "within a reasonable period," and score suppliers on warranty, so suppliers may fear retaliation. Using portal logins may breach portal terms. |

## 3. What kills it, and the fastest test

**What kills it:** the money that is both wrong and still disputable inside contract windows turns out to be a few percent of charges. Or suppliers won't file disputes because they fear for future contracts.

**Fastest test:** get 3–5 Midwest Tier 1 or Tier 2 warranty managers to export the last 6–12 months of automaker warranty charges and their percentage agreements. Have someone scrub them by hand or with AI in two weeks. Count the dollars that were wrong and could still have been disputed in time, and ask whether each supplier would actually file.
- Kill it below about 5% of charges, or if suppliers refuse to file.
- It becomes interesting above about 10%, if they would sign a contingency agreement.

VERDICT: PASS
