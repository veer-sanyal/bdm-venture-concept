I recommend passing. The need is real, but the pitch's main causal claim is partly wrong, the stated price runs into a well-established alternative that costs the facility nothing, and the market reachable at this price is only about $100M.

## Checking the key claims against primary sources

- **"58 days vs about 22 days" in Illinois: true, but not a like-for-like comparison.** The 2025 Illinois Auditor General audit sampled 50 applications. 17 were sent to the state inspector general's office (OIG) for asset investigation and "spent on average 58 days at the OIG." The 33 without OIG involvement took "on average 22 days for DHS to make a determination." So 58 days is time at the OIG only, while 22 days is the whole decision. 7 of the 17 referrals came after eligibility had already been decided, a leftover from COVID-era rules. Illinois received 15,645 long-term care applications in 2023. The OIG decides which cases to refer and works its own queue, so a vendor can make files cleaner but cannot speed up the state's step.
- **Retroactive coverage drops to two months from January 2027: true.** The law cuts it from three months to two for traditional enrollees, which covers most nursing home residents, for applications filed on or after 1/1/2027.
- **"Delays now cost facilities unpaid care outright": mostly false as stated.** Coverage counts back from the month of application. Time the state takes after filing costs cash flow, not revenue. Money is lost in only three ways:
  - the application is filed late;
  - it is denied for missing documents and has to be refiled, which resets the retroactive window;
  - a transfer penalty was not foreseen at admission.
  
  The reform takes away one month, and only from facilities that file late.
- **The deadline is not new everywhere.** Florida, Arizona and Tennessee dropped retroactive coverage for nursing home residents around 2019. Florida is a seven-year natural experiment, and no AI product built for it is visible.
- **Missing documents drive denials.** Pennsylvania elder-law practitioners call "failure to provide verification" probably the most common reason long-term care applications are denied. The industry's bad debt runs about 1.41% of revenue, with Medicaid-pending accounts a main cause.

## Who else serves this customer

- **Senior Planning Services (SPS):** runs applications for 1,000+ facilities in 22 states, including large chains. The facility refers the resident and the family retains SPS, so the facility appears to pay nothing; the site doesn't state fees. SPS has used Ocrolus "Medicaid-Genius" to automate reading five years of bank statements since about 2017.
- **CoreCare (YC S20):** tracks pending applications and renewals, with connections to PointClickCare, MatrixCare and state systems. Its site says 1,500+ facilities and its YC profile says 1,000+.
- **Telos LTC:** software that calculates gift penalties and e-files applications, sold through the PointClickCare marketplace. 100+ Texas facilities.
- **Others:** Stotler Hayes (a law firm that represents providers only), Medicaid Plus, Brunelle and many regional consultants. Chains also have their own in-house business-office staff.
- **Who owns the data and the buying channel:** PointClickCare owns the records and billing data and the integration marketplace. SPS and CoreCare already hold the Medicaid-pending relationship at many chains.
- **Near-identical pitch:** none found. Ocrolus is closest, but it is a tool rather than a service paid per approval.

## 1. The strongest version

A tech-enabled service for mid-size chains (roughly 3,700 facilities) that clears a resident's finances before admission and guarantees an application good enough to avoid a missing-documents denial.

- **At admission:** a five-year look-back screen that finds transfers that would trigger a penalty, so the chain can admit, cure the transfer or plan the payer before the resident arrives.
- **After filing:** file on the day of admission to protect the application date, then AI plus human specialists answer every caseworker request so no application is denied for missing documents.
- **Price:** a share of pending revenue recovered, or a fee with a guarantee against write-offs, rather than a flat $1,250.
- **Where to start:** states with long pending times and zero or short retroactive coverage (IL, PA, NJ, FL), selling to the chain's CFO or head of revenue cycle, delivered inside PointClickCare.

## 2. Ratings

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | Missing documents are a leading denial cause and bad debt runs about 1.4% of revenue; the retroactive cut is confirmed for 1/1/2027. |
| Value over what customers use today | 2 | SPS already automates look-backs for 1,000+ facilities at no apparent cost to the facility; the state's OIG queue can't be sped up by a vendor. |
| Market size | 2 | About 3,700 facilities × ~20 applications a year (extrapolated from Illinois's ~15.6k) ≈ 74k applications plus renewals ≈ $100M a year; all nursing homes ≈ $400M. |
| Risk (5 = low) | 2 | Rules differ state by state, collecting old bank statements stays manual, much of the work is services, advising on curing transfers risks unauthorized practice of law, and SPS sets a zero-cost price anchor. |

## 3. What would kill it, and the fastest test

**What kills it:** chains' losses to documentation problems and missed filing windows turn out too small, or already handled by SPS, in-house staff or CoreCare, to justify paying about $1,250 per approval.

**The fastest test:** a two-week "pending-AR autopsy" at 5 chains with 10 to 50 buildings, including at least one in Florida. Pull 12 months of Medicaid-pending write-offs and denials from PointClickCare and assign each dollar to one of three causes: late filing, missing-document denial, or penalty not foreseen at admission. Then ask each chain for a paid pilot at the proposed price.
- **Kill** if the losses we could address are under about $50k per building per year, or if fewer than 2 of the 5 sign.
- Florida has had no retroactive coverage since 2019, so it shows what the rest of the country looks like after 2027.

## Sources
- [Illinois OAG 2025 LTC eligibility audit digest](https://www.auditor.illinois.gov/Audit-Reports/Performance-Special-Multi/Performance-Audits/2025_Releases/25-Medicaid-LTC-Eligibility-Perf-Digest.pdf)
- [2025 audit highlights](http://www.auditor.illinois.gov/Audit-Reports/Performance-Special-Multi/Performance-Audits/2025_Releases/25-Medicaid-LTC-Eligibility-Perf-Highlights.txt)
- [NAMD OBBBA memo](https://eohhs.ri.gov/sites/g/files/xkgbur226/files/2025-07/NAMD-Memo-OBBBA-Medicaid-Policies.pdf)
- [Akin OBBBA timeline](https://www.akingump.com/a/web/ib9LfesVkHtsk8FVF9eqwA/akin-obbba-health-provisions-timeline.pdf)
- [CRS R48569](https://www.congress.gov/crs-product/R48569)
- [Florida AHCA retroactive eligibility report](https://ahca.myflorida.com/content/download/5861/file/Retroactive_Eligibility_Report_20200110.pdf)
- [Justice in Aging brief](https://www.justiceinaging.org/wp-content/uploads/2019/09/Medicaid-Retroactive-Coverage-Issue-Brief.pdf)
- [SPS healthcare](https://www.seniorplanning.com/healthcare)
- [SPS–Ocrolus partnership](https://www.prnewswire.com/news-releases/senior-planning-services-partners-with-ocrolus-to-improve-medicaid-application-processing-300466275.html)
- [CoreCare](https://corecare.ai/)
- [CoreCare YC](https://www.ycombinator.com/companies/corecare)
- [Telos LTC](https://www.telosltc.com/)
- [Stotler Hayes](https://stotlerhayes.com/)
- [PA elder law on verification denials](https://www.paelderlaw.net/top-3-reasons-nursing-home-medicaid-benefits-are-denied/)
- [GMA bad-debt benchmark](https://www.gma-cpa.com/blog/how-does-your-skilled-nursing-facilitys-bad-debt-expense-as-a-percentage-of-revenue-measure-up)
- [ASPE SNF ownership brief](https://aspe.hhs.gov/sites/default/files/documents/fd593ae970848e30aa5496c00ba43d5c/aspe-data-brief-ownership-snfs.pdf)

VERDICT: PASS