I would pass. The rules in the pitch are real, but the product is aimed at a small group of products, and the metal data behind it is cheap to produce once and hard to charge for every year.

**How the claims held up**
- **Correct:**
  - Since April 6, 2026 the tariffs are charged on the product's full value. Products made almost entirely of metal pay 50% and "derivative" goods (manufactured products containing metal) pay 25%. [CBP CSMS 68253075](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/4117593), [Federal Register](https://www.federalregister.gov/documents/2026/04/09/2026-06960/strengthening-actions-taken-to-adjust-imports-of-aluminum-steel-and-copper-into-the-united-states)
  - To claim the under-15% exemption (HTS 9903.82.03), the importer must enter the combined metal weight in kilograms on each entry line.
  - Global Trade Alert's figure is $227B of 2024 imports across 326 product codes on the 25% list. [GTA](https://globaltradealert.org/blog/s232-metals-restructuring-april-2026)
- **What the pitch leaves out:**
  1. **Many listed products can never use the 15% exemption.** It is barred for anything classified in HTS chapters 72, 73, 74 and 76 (iron, steel, copper and aluminium goods). I pulled the [White House annex list](https://www.whitehouse.gov/wp-content/uploads/2026/04/ANNEXES-I-A-I-B-II-III-IV.pdf) and counted the 25% list: 55 codes are in those chapters and 356 are outside them.
  2. **Most of the eligible 356 codes are clearly above 15% metal.** They are mainly machinery, bearings, motors, transformers, tractors, trailers, railcars, knives and tools. Products that could sit near the line are few: fans, vacuum-cleaner parts, space heaters, microwave parts, some circuit-board and wiring parts. So $227B greatly overstates the market; I could not find a dollar figure for the near-line group.
  3. **Getting under the line does not mean paying nothing.** Excluded goods fall back to other tariffs: Section 122 until July 24, then new 10–12.5% Section 301 tariffs on 60 countries. [Fennemore](https://www.fennemorelaw.com/new-u-s-tariffs-replace-expiring-section-122-tariffs/), [NatLawReview](https://natlawreview.com/article/new-section-232-tariff-overhaul-winners-losers-and-unintended-consequences). I found no source saying whether those new 301 tariffs spare metal-tariff goods, so the net saving could be anywhere from about 12 to 25 points of product value.
  4. **The rules keep changing.** They were rewritten again in June 2026: 28 machinery codes moved to a new list, and the US-metal share needed for the 10% rate dropped from 95% to 85%. The lower rates are temporary and end December 31, 2027. [Holland & Knight](https://www.hklaw.com/en/insights/publications/2026/06/annexed-opportunity-proclamation-provides), [Plante Moran](https://www.plantemoran.com/explore-our-thinking/insight/2026/06/section-232-update)

**Who already serves this customer**
- **Supplier data on where metal was melted:** Assent, Z2Data and Sourcemap already sell this, including tracing back to the smelter and "audit-ready" files for customs. [Assent](https://www.assent.com/blog/prepare-for-section-232-tariffs/), [Z2Data](https://www.z2data.com/insights/why-you-need-supply-chain-visibility-for-section-232/), [Sourcemap](https://www.sourcemap.com/blog/how-supply-chain-mapping-can-save-25-in-tariffs)
- **Buying channel:** Customs brokers own it. Livingston, Expeditors and Flexport all publish guidance on these tariffs to their clients.
- **Metal weights:** Design owners' CAD software already calculates weight by material. Automotive suppliers already declare full material weights in IMDS, the industry's material database.
- **The same pitch:** Mallory Group sells nearly the same package (bill of materials, verified weights, supplier statements, a repeatable method, one audit file) as advisory work. [Mallory](https://www.mallorygroup.com/blog-posts/section-232-tariff-update-new-15-de-minimis-threshold-details-for-u-s-importers)
- **No exact match:** I found no company automating the weight calculation from CAD and bills of materials.

**1. Strongest version**
Drop the Indiana focus and the "reads CAD" angle. Sell a substantiation service per product to mid-market importers whose products fall in the eligible machinery, electrical and furniture chapters (HTS 82–94) and are mixed-material, meaning roughly 5–30% metal by weight. Go through customs brokers, who need the kilogram figure and the melt country on every entry. The paid moments are:
- Building the proof file when customs sends a request for information, or when counsel raises False Claims Act exposure.
- A one-time review to find products a redesign could move under 15%.
- Keeping each product's file current when a design or supplier changes.

Indiana is a weak starting point. Its big industries (RVs, auto parts, engines) are mostly metal-heavy or already covered by the separate auto-parts tariff.

**2. Ratings (5 is best; for risk, 5 means low risk)**
| Measure | Score | Evidence |
|---|---|---|
| Customer need | 3 | Weight reporting is mandatory to claim the exemption, and lawyers warn of False Claims Act risk, but it only matters for the few mixed-material products ([Foley](https://www.foley.com/insights/publications/2026/05/what-every-multinational-should-know-about-the-new-rules-for-section-232-tariffs-on-steel-aluminum-and-copper-derivatives/)). |
| Value over today | 2 | CAD mass properties plus a scale answer the weight question in hours per product, and Assent, Z2Data and Sourcemap already collect melt-country data. |
| Market size | 2 | Most of the $227B is either barred from the exemption or far above 15% metal; the near-line group is a thin list of appliance and electrical parts. |
| Risk | 2 | The rules changed in April and again in June, the lower rates end in 2027, and brokers and compliance vendors control the buying channel. |

**3. What kills it, and the fastest test**
- **What kills it:**
  - Too few products sit near the line to support a yearly per-product fee.
  - The weight is a one-time calculation, so the recurring fee has nothing to renew.
  - Brokers or Assent add a "metal weight" field and win by default.
- **Fastest test:**
  1. Use bill-of-lading data (Panjiva or ImportGenius) to pull about 30 Midwest importers of the near-line codes: fans, vacuum parts, space heaters, appliance parts, wiring parts.
  2. Offer each a paid $3–5k fixed-fee proof file for their top 5 products.
  3. If fewer than 3 pay within three weeks, kill it.
- **Question to add:** ask whether customs has ever sent them a request for information about an exemption claim. If none has, the audit-file value is theoretical.

This was desk research only. It is not customer validation. As you asked, I did not read the project files.

VERDICT: PASS
