I'd pass. The regulatory change is real, but the pitch's link between the Illinois delay and unpaid care is wrong, and the core feature (reading five years of bank statements automatically) has been sold to large chains since 2017.

## Checking the key claims

- **Illinois 58 vs. 22 days: true, but narrow.** The July 2025 Illinois Auditor General audit sampled 50 long-term care applications from 2021–2023. Seventeen went to the state inspector general's office for an asset investigation and spent an average of 58 days there. The other 33 took an average of 22 days in total. Across all 50 the average was 41 days, down from 125 days in the previous audit, when investigations averaged 98 days. So this is one state and a small sample, and the number is already falling. That review is also the state's own work; a vendor can hand over a clean file but can't make the state's investigation go faster.
- **The retroactive coverage cut is correct.** CMS guidance SMD #26-001 (March 2026) confirms that section 71112 applies to applications made on or after January 1, 2027. Nursing home residents get at most two months of coverage before the application month, down from three.
- **The pitch's cause and effect is wrong.** Once someone is approved, coverage runs back from the application month. So the 58 days the state spends reviewing delays cash but doesn't erase coverage. Care goes unpaid for two other reasons:
  - the facility files more than two months after the resident needed Medicaid;
  - the application is denied for missing paperwork, and the refiling gets a new, later date.

  Florida has had no retroactive coverage for nursing home residents since 2019, which shows what that looks like in practice.
- **"Flag transfers before admission" doesn't fit how residents arrive.** Most come from a hospital, and the admission decision is made in hours. Nobody has five years of statements at that point.
- **The state already sees balances.** The federal Asset Verification System can return up to 60 months of account balances straight from banks. It gives balances, not transactions, so a caseworker still asks the family to explain large withdrawals. That explaining, and getting families to hand over paperwork, is the real bottleneck. Reading the statements is not.

## Who else serves this customer

- **Senior Planning Services** calls itself the leading Medicaid application company. It has run automated bank-statement analysis (through Ocrolus) for large nursing home chains since 2017 and handles the whole application. This is the closest service match.
- **Medicaid Plus and Brunelle** are regional firms that file applications, handle renewals, and take over stuck pending cases. Medicaid Plus advertises "No Cost to You" to facilities, meaning the family pays.
- **MedicaidSoft** is software for facilities: AI eligibility flags, state forms filled in automatically, and bank statements pulled through Plaid (up to 2 years). It is offered to members of HPSI, a nursing home purchasing group, which is a buying channel.
- **CoreCare** (Y Combinator-backed) claims 1,500+ facilities. Its revenue product tracks every Medicaid application and its forms. One 25-building Texas chain cut pending write-offs 60%, saving over $1M. It already sits with the revenue-cycle buyer and could add filing.
- **ExaCare** raised a $30M Series A and serves 1,500+ facilities with AI admissions and billing tools. It doesn't handle eligibility.
- **Who owns the data:** PointClickCare, the dominant nursing home records system, already holds the resident and billing data and tracks Medicaid-pending accounts. Nobody owns the family's bank records.
- I found no company whose pitch matches this one almost exactly.

## 1. The strongest version

A done-for-you "Medicaid conversion" service, sold to revenue-cycle leaders at 10–50-building chains, starting in two or three strict states such as Illinois, New York and New Jersey. It starts when a resident's payer changes in PointClickCare. The promise: file in the month the resident needs Medicaid, answer every caseworker request within 48 hours, and refund the fee on any denial for missing paperwork. It would still charge about $1,250 per approval, against a month of Medicaid care worth roughly $7–9K. The AI reading of statements is how it keeps costs down, not what it sells. What it sells is a guarantee of zero lost coverage months.

## 2. Ratings

| Area | Score | Evidence |
|---|---|---|
| Customer need | 4 | Pending write-offs are real money (CoreCare's 25-building case: over $1M), and the 2027 cut tightens the filing window. |
| Value over what customers use today | 2 | Senior Planning Services already sells automated look-back review to chains, some rivals are free to facilities, and the bottleneck is family paperwork, not reading. |
| Market size | 3 | About 14,700 nursing homes, with Medicaid paying for 63% of residents (KFF). My own estimate is a few hundred million dollars a year nationally, and only a fraction of that in 10–50-building chains. |
| Risk (5 = low) | 2 | Rules differ by state, it needs a lot of staff, families control the documents, CoreCare or PointClickCare could add it, and competitors that charge the family undercut the price. |

## 3. What would kill it, and the fastest test

It dies if chains lose little money to late filing and paperwork denials, or won't pay $1,250 when family-paid consultants or their own business-office staff do the work for free to them.

**Fastest test:** in one state, offer ten chain revenue-cycle leaders a paid pilot. We handle their next 20 Medicaid conversions at $1,250 per approval, with a full refund on any paperwork denial. In the same call, ask for last year's write-offs caused by late filing or refiling. If fewer than two sign within three weeks, or the losses come in under about $30K per building per year, kill it.

**Sources:**
- [Illinois Auditor General 2025 audit (full PDF)](http://www.auditor.illinois.gov/Audit-Reports/Performance-Special-Multi/Performance-Audits/2025_Releases/25-Medicaid-LTC-Eligibility-Perf-Full.pdf)
- [Illinois audit highlights](http://www.auditor.illinois.gov/Audit-Reports/Performance-Special-Multi/Performance-Audits/2025_Releases/25-Medicaid-LTC-Eligibility-Perf-Highlights.txt)
- [CMS SMD #26-001](https://www.medicaid.gov/federal-policy-guidance/downloads/smd26001.pdf)
- [Congressional Research Service summary of OBBBA health provisions](https://www.congress.gov/crs-product/R48569)
- [MACPAC on retroactive eligibility waivers](https://www.macpac.gov/wp-content/uploads/2019/08/Medicaid-Retroactive-Eligibility-Changes-under-Section-1115-Waivers.pdf)
- [Florida retroactive Medicaid elimination](https://www.lakelandlaw.com/retroactive-medicaid-in-florida-has-been-eliminated-is-this-good-or-bad/)
- [MACPAC on state asset verification](https://www.macpac.gov/wp-content/uploads/2020/10/State-Compliance-with-Electronic-Asset-Verification-Requirements.pdf)
- [Senior Planning Services and Ocrolus](https://www.prnewswire.com/news-releases/senior-planning-services-partners-with-ocrolus-to-improve-medicaid-application-processing-300466275.html)
- [Medicaid Plus](https://www.mymedicaidplus.com/nursing-facilities.html)
- [Brunelle Medicaid](https://brunellemedicaid.com/services/nursing-home-information/)
- [MedicaidSoft features](https://www.medicaidsoft.com/software-features)
- [MedicaidSoft for HPSI members](https://hpsi.epictetus.medicaidsoft.com/)
- [CoreCare](https://corecare.ai/)
- [CoreCare case study](https://corecare.ai/resources/how-focused-post-acute-care-partners-reduced-medicaid-write-offs-by-2m/)
- [CoreCare press releases](https://corecare.ai/press-releases/)
- [ExaCare Series A](https://www.prnewswire.com/news-releases/exacare-ai-raises-30m-series-a-to-reimagine-admissions-and-launch-a-powerful-suite-of-ai-agents-for-skilled-nursing--home-care-302586587.html)
- [PointClickCare eligibility verification](https://pointclickcare.com/resource/skilled-nursing-software/solution-sheets/eligibility-verification-solution-spotlight/)
- [KFF on nursing facilities and Medicaid](https://www.kff.org/medicaid/5-key-facts-about-nursing-facilities-and-medicaid/)

VERDICT: PASS