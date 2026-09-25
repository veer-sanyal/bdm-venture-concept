I recommend passing. The rules the pitch describes check out against the primary sources. But the proof has to cover much less than the $227B figure suggests, the customs broker already owns the buyer, and the rules have changed five times in 16 months. I did not read any local project files.

## Checking the key claims

| Claim | What the sources show |
|---|---|
| Tariff charged on full value since April 2026 | **True.** Proclamation of April 2, in force April 6 ([Federal Register](https://www.federalregister.gov/documents/2026/04/09/2026-06960/strengthening-actions-taken-to-adjust-imports-of-aluminum-steel-and-copper-into-the-united-states), [CBP CSMS 68253075](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/4117593)). |
| Up to 50%, and 25% for most manufactured goods | **True, but there are more tiers.** Mostly-metal goods (Annex I-A) pay 50% and derivative goods (Annex I-B) pay 25%. There is also a temporary 15% list (Annex III), a new list for mobile machinery with rates by country (Annex I-C, added June 8), and a 10% rate for goods made with US metal. The US-metal share needed for that 10% rate was cut from 95% to 85% by weight ([Thompson Hine](https://www.thompsonhinesmartrade.com/2026/04/president-trump-makes-major-changes-to-section-232-tariffs-on-aluminum-steel-and-copper/), [CSMS 68855869](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/41aa83d)). |
| Under 15% metal by weight pays nothing | **True with two limits the pitch skips.** (a) Goods classified in HTS chapters 72, 73, 74 and 76 can never use it. (b) Only the metal named for that product's list counts ([annex text, note 16(c)](https://www.whitehouse.gov/wp-content/uploads/2026/04/Metals-ANNEXES-I-A-I-B-II-III-IV.pdf)). For example, power tools (8467.22/.29/.81/.89) are listed only as aluminum goods, so their steel does not count. That makes the weight calculation genuinely tricky. |
| Metal weight in kg on every entry line | **Partly true.** The kg figure is required only on lines that claim the exemption (code 9903.82.03). Every covered line must still report the country where the metal was melted and poured (steel) or smelted and cast (aluminum). |
| $227B (Global Trade Alert) | **True:** 2024 imports under Annex I-B, 326 products ([GTA](https://globaltradealert.org/blog/s232-metals-restructuring-april-2026)). But most of that is engines, tractors, bearings, gears, motors, transformers and rail equipment, which are far above 15% metal. |
| Enforcement pressure | **Real.** Customs information requests (CF-28s) are rising. In May 2026 the Justice Department announced a $549.5M customs-fraud settlement over aluminum extrusions, and a $19M one that included evaded steel tariffs ([ArentFox](https://www.afslaw.com/perspectives/investigations-blog/doj-secures-record-550-million-settlement-over-alleged-aluminum), [Morgan Lewis](https://www.morganlewis.com/pubs/2026/05/doj-announces-major-fca-settlement-relating-to-evaded-customs-duties)). Law firms tell clients to keep bills of materials, weight calculations and supplier certificates on file ([Foley](https://www.foley.com/insights/publications/2026/05/what-every-multinational-should-know-about-the-new-rules-for-section-232-tariffs-on-steel-aluminum-and-copper-derivatives/)). |
| Gaps in CBP guidance | CBP has not said whether packaging counts toward product weight, how much batch-to-batch variation is tolerated, or what proof it will accept. |

## Who else serves this customer

- **Customs brokers own the filing and the buyer.** Mallory Alexander and similar firms already sell SKU reviews for the 15% threshold as part of brokerage ([Mallory](https://www.mallorygroup.com/blog-posts/section-232-tariff-update-new-15-de-minimis-threshold-details-for-u-s-importers)). The Big 4 and law firms sell the same advice.
- **Supplier data platforms own outreach to suppliers.** Assent and Z2Data already chase melt, pour, smelt and cast origin, mill certificates and material composition ([Assent](https://www.assent.com/blog/prepare-for-section-232-tariffs/), [Z2Data](https://www.z2data.com/insights/why-you-need-supply-chain-visibility-for-section-232/)). Electronics makers also already have per-part material weights on file through their supplier declarations.
- **CAD and product-data systems own the design data.** Tools like SolidWorks and Creo report mass by material natively. For the target customer, who designs in-house, the as-designed metal weight takes an engineer minutes.
- **Nearest adjacent product:** LightSource's AI Tariff Tracker assigns tariff codes from BOMs and drawings for Amazon, Medtronic, BRP and others. It does not compute metal weight or build a proof file ([LightSource](https://lightsource.ai/blog/announcing-ai-tariff-tracker)). GingerControl also does classification only.
- I found no company whose pitch matches this one. The data and the buyer are split between the broker (filing), Assent/Z2Data (supplier data) and CAD/product-data systems (design). No one yet owns the "prove it's under 15%" proof file.

## 1. The strongest version

Don't sell per-product compliance to Indiana designers in general. Sell a certified proof service for the 15% line, through customs brokers, for goods outside chapters 72–76 whose listed metal is roughly 5–30% of product weight. Likely categories:

- power tools and outdoor power equipment, where only aluminum counts
- small appliances, fans and vacuum parts
- HVAC parts
- insulated cable (aluminum and copper lists combined)
- circuit boards for power supplies and transformer parts (Annex III, aluminum only)
- trailer and RV components (8716.90) and some auto parts

What it does:
- applies each list's own metal rule
- checks the design-data weight against weighed production samples
- re-certifies whenever the design or supplier changes
- builds a proof file ready for a CF-28 response
- recommends redesigns to get under 15%, which is the high-value service

Pricing: a fixed or success-based fee per SKU for the first certification, then a yearly fee per SKU for change control. Elkhart's RV and trailer component importers are a reasonable local start, since trailer parts are on the list. Indiana as a geography is otherwise arbitrary. Drop melt-origin chasing, which Assent and Z2Data already do, or offer it only as a thin add-on.

## 2. Ratings

- **Customer need: 3.** For a product that is truly near the line, 25% of full value is a large amount, and enforcement risk is real. But the $227B list is mostly metal-heavy machinery for which the threshold is irrelevant.
- **Value over what customers use today: 3.** The per-list metal logic, checking actual production weight and change control are real improvements. But the designer's own CAD gives the base weight in minutes, and brokers already bundle threshold reviews.
- **Market size: 2.** The number of products close enough to 15% to change their tariff is a small fraction of the $227B; I found no data on how small. A yearly fee per product on that slice looks like a services-sized market, not a venture-sized one.
- **Risk: 2.** The rules changed in February 2025, June 2025, August 2025, April 2026 and June 2026. Annex III and Annex I-C expire at the end of 2027. The 15% rule could be moved or removed by a single proclamation.

## 3. What would kill it, and the fastest test

**What would kill it:**
- Too few SKUs sit near 15% of their listed metal, so there is nothing to certify.
- Brokers give threshold reviews away with brokerage.
- A proclamation changes or removes the threshold.
- CBP accepts rough supplier-questionnaire figures, so a precise proof file is never needed.

**Fastest test (2–3 weeks):** Ask 3 customs brokers, Indiana ones included, two things:
1. How many 9903.82.03 claims (the under-15% exemption) have they filed since April 6?
2. Which clients import lines on the lists outside chapters 72–76 in the categories above?

Then try to pre-sell 10 paid proof files for a single SKU each (around $1,500) through them. Weak interest from brokers, or fewer than 5 paying buyers, means pass for good. This would count as customer validation; everything above is desk research.

VERDICT: PASS
