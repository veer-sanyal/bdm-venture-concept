I researched this on the web only and did not open any project files, as you asked. Everything below is desk research. None of it shows that customers want this.

## Checking the concept's claims

- **Notice volume: correct.** A record 10,098 PAGA notices were filed in 2025 ([NatLawReview](https://natlawreview.com/article/lwda-theres-new-sheriff-town)). Ankura counts 8,762 for June 2025 to May 2026. That is 7% below the level before the reform, so the reform has not reduced filings much ([Ankura/Mondaq](https://www.mondaq.com/unitedstates/constitutional-administrative-law/1821956/the-2025-to-2026-paga-trend-update-%7C-2-years-out-from-the-2024-reform-where-are-paga-filings-headed)).
- **$2.2B in settlements: correct as quoted, but inflated.** The figure comes from CABIA, an employer group: 2,420 settlements, with $740M going to lawyers ([CABIA](https://cabia.org/research-data/paga-summary/), [GV Wire](https://gvwire.com/2026/04/15/california-goes-after-vexatious-paga-law-firms-how-much-have-they-cost-employers/)). It is drawn from the state's case filings, and it probably includes the class-action portions of combined PAGA and class settlements. PAGA penalties alone are a smaller share.
- **The 15% cap: correct in the statute, rarely used in practice.** Labor Code §2699(g) caps penalties at 15% if the employer took "all reasonable steps" before the notice. Its examples include "periodic payroll audits and took action in response" ([leginfo](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=2699)). But across 652 settlements from June to August 2026, only 1.6% to 4% even mentioned the cap, and very few actually used it in pricing the settlement ([CA Employment Law Report](https://www.californiaemploymentlawreport.com/2026/09/five-settlements-five-lessons-what-augusts-california-wage-and-hour-resolutions-tell-employers/)). I found no court ruling applying it.
- **Why checking every shift matters.** In *Donohue v. AMN Services* (2021), a healthcare staffing case, the California Supreme Court held that time records showing missed or short meal periods create a presumption of violation, and it banned rounding meal punches ([Justia](https://law.justia.com/cases/california/supreme-court/2021/s253677.html)). Break premiums must also be paid at the "regular rate", which includes bonuses and shift differentials ([Craigie](https://craigielawfirm.com/2026/07/31/remember-to-calculate-and-pay-workers-regular-rate-for-meal-and-rest-break-penaties/)).
- **The healthcare wedge fits.** Healthcare is one of the top three industries by PAGA notices, and senior living and post-acute care notices rose 28.4% year over year (Ankura). California nursing homes employ about 156,000 people ([FRED/BLS](https://fred.stlouisfed.org/series/SMU06000006562310001SA)).

## Who already serves this customer

- **The timekeeping and payroll vendors already own the punch data.** SmartLinx is built for nursing homes and already applies meal-break rules and sends real-time alerts ([SmartLinx](https://www.smartlinx.com/why-smartlinx/intelligent-compliance/)). UKG can pay meal premiums automatically from punches ([CloudApper/UKG](https://ukg.cloudapper.ai/time-capture/california-meal-rest-break-compliance-ukg/)). WellSky and Axxess serve home health.
- **Electronic health record (EHR) vendors hold the login data.** PointClickCare, MatrixCare and Netsmart run nursing-home health records, so each customer's EHR vendor has to cooperate before logins can be compared with punches.
- **Employment defense firms own the buying channel.** Ogletree, Littler, Fisher Phillips and similar firms decide how clients handle PAGA risk. They sell sampled audits as billable hours, and Ogletree already publishes on AI-driven preventive compliance ([Ogletree](https://ogletree.com/insights-resources/blog-posts/beyond-the-data-part-i-using-ai-tools-to-turn-workforce-data-into-preventive-compliance/)). Data-expert firms such as Ankura and Econ One do after-the-fact audits.
- **Scaled Comp is the closest product.** It tests every shift against meal, rest, overtime and wage-statement rules, sells monthly audit runs to build a reasonable-steps record, and charges $5,000 to $15,000 for a baseline audit ([Scaled Comp](https://www.scaledcomp.com/for-businesses-hr-teams)). It differs from this concept in three ways: it looks back at past records rather than checking before payroll, it has no off-the-clock matching against health-record or badge data, and it is not specific to healthcare. So it is a competitor, not the same pitch.
- **Worksana** is a time clock that pays break premiums automatically and records a reason for each missed break, but it serves dairy and field crews ([Worksana](https://worksana.com/features/break-compliance/)).
- I found no company making the same pitch.

## 1. The strongest version of this company

Recast it as a pre-payroll check for California home health and multi-site nursing home operators. Its core is the math that timekeeping software gets wrong:

- the regular rate on break premiums and overtime when shift differentials and bonuses apply;
- California's healthcare-specific rules: the 8/80 overtime option, 12-hour alternative schedules and waivers of the second meal break;
- for home health, travel time between visits and the overtime rate for staff paid per visit.

Every flag gets resolved before payroll closes, either by paying the premium or by recording an attested reason. Unresolved flags are the danger: they would give plaintiffs evidence that the employer knew. The main pitch should be preventing the underlying wage claims, not the 15% cap. Health-record and badge matching comes second, added where the EHR vendor will provide login data. Sell through defense firms and employment-practices liability insurers.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Healthcare is a top-three PAGA industry, and senior and post-acute notices rose 28% year over year (Ankura). |
| Value over what customers use today | 3 | UKG and SmartLinx already auto-pay premiums and send alerts. The new parts are the regular-rate math and cross-system off-the-clock matching, and the cap is being "argued but not handed out" (1.6% to 4% of settlements). |
| Market size | 2 | About 156,000 nursing-home workers plus home health and clinics, perhaps 0.5 million employees. At $4 to $6 per employee per month that is roughly $25M to $40M a year even at full share. Spreading to all California hourly employers makes it only a few hundred million, and the product is tied to California law. |
| Risk (5 = low) | 2 | Timekeeping vendors own the data and can copy the feature. Access to health-record logs depends on the EHR vendor. Flags left unresolved become plaintiff evidence. The cap is untested in court. AB 1331, a workplace-surveillance bill, is on the Governor's desk ([leginfo](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB1331)). |

## 3. What kills it, and the fastest test

**What kills it:** operators decide the payroll rules they already have are "good enough." Or the underpayments found on a clean dataset are small next to the price, since the cap is rarely applied and sampled audits by counsel already count as a "periodic payroll audit." Or SmartLinx and UKG ship regular-rate premium math as a checkbox feature.

**The single fastest test (two to three weeks):** have two defense firms each introduce five multi-site nursing home or home health clients. Run one quarter of their punch, payroll and pay-code exports through the regular-rate and premium engine, then measure two things:

1. the dollars underpaid per employee per month that their current system missed;
2. whether at least 3 of the 10 sign a paid pilot at about $5 per employee per month.

Kill it if the missed underpayment is under about $5 per employee per month, or if fewer than 3 sign.

Overall, a real problem is being solved by a feature, not a company. The incumbents already own the data and the channel, the market is small and limited to California, and the main legal hook, the 15% cap, is almost never applied in practice.

VERDICT: PASS
