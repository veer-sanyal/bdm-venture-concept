I'd back this, but only in a narrower form than the pitch. The pain and the January 2027 deadline are real, and no one I found sells this exact service. The market is mid-sized, and the deadline changes less than the pitch suggests.

## Claims checked against sources

| Claim | What I found |
|---|---|
| Over 60% of 1.2M residents have Medicaid as main payer | **True.** KFF: 1.2M residents as of July 2024, over 60% Medicaid-primary. Medicaid paid 44% of $147B institutional long-term care spending in 2023. |
| Retroactive coverage drops from 3 months to 2 in January 2027 | **True.** The 2025 budget law (the "One Big Beautiful Bill Act") cuts it to 2 months for traditional enrollees such as the elderly and 1 month for expansion adults, effective Jan 1, 2027. The pitch leaves out that this only hurts cases filed late. A case filed promptly is covered back to its filing date however long the state takes. The cut punishes slow filing, not slow state processing. |
| Care worth about $9,300 a month (Genworth 2024) | **Partly true.** Genworth's 2024 median for a semi-private room is $111,325 a year, about $9,277 a month. But that is the private-pay price. What a home actually loses on an unpaid Medicaid month is its Medicaid daily rate minus the resident's own income contribution, which is lower. The pitch overstates the loss per month. |
| Indiana as the starting state | Indiana moved long-term care for people 60+ into managed care ("PathWays") in 2024. 496 Indiana homes are waiting on $462M in delayed state supplemental payments, so homes are short of cash and feel every unpaid month. It is still a small market, about 500 homes. |

## Who else serves this customer
- **Outside eligibility firms:** Senior Planning Services (22 states, including Indiana) and Medicaid Plus. Nursing-home billing outsourcers such as MCA Skilled and Richter also do eligibility work. These are labour-heavy human services.
- **Software:**
  - **MedicaidSoft:** fills in state forms, pulls up to 24 months of bank statements automatically, and has AI eligibility screening. It reports one Alabama home cutting unpaid pending balances from $600K to $300K in 33 days.
  - **CoreCare:** tracks pending cases and renewals for 1,500+ facilities, but only in Texas and Ohio. It reports a 60% cut in pending write-offs.
  - **Telos LTC:** 100+ Texas facilities, with electronic filing.
  - **RevSuite:** case tracking only, no AI.
- **Nearby AI player:** ExaCare ($30M Series A, 1,500+ facilities) covers admissions and billing. Its October 2025 announcement says nothing about Medicaid applications, but it is the likeliest to add them.
- **Data and buying channel:** PointClickCare, the dominant nursing-home records system, holds the census and resident-fund data and runs the app marketplace these vendors sell through. It does not appear to own this workflow. Regional chains' central business offices do the buying.
- **Near-identical pitch:** none found. Nobody sells an AI agent that chases families, does the full filing and charges per approval.

## 1. Strongest version
A service that takes over stuck or unfiled Medicaid cases for nursing homes and is paid only when a case is approved.
- **Buyer:** regional chains (10 to 100 homes) with a central business office, rather than single homes. It connects to PointClickCare to spot residents about to run out of money early.
- **Staffing:** AI does the family chasing, statement reading, transfer flagging and letter drafting. A small team of human specialists signs off and handles state caseworkers.
- **Pitch to buyers:** "file before the 2-month window closes," plus annual renewals so approved residents don't lose coverage.
- **Price:** per approved case, or a percentage of recovered revenue.
- **Geography:** Indiana plus neighbouring states through multi-state chains, not Indiana alone.
- **Cut from the pitch:** VA benefits and long-term-care insurance claims, which are different buyers and different workflows. Home-care Medicaid can come later; home-care agencies don't carry unpaid care the way nursing homes do, so the pain is weaker.

## 2. Ratings
- **Customer need: 4.** Vendors report single homes carrying $600K in unpaid pending balances, and the retroactive window shrinks by a third in January 2027.
- **Value over what customers use today: 3.** Form filling, bank-statement pulls and case tracking already exist (MedicaidSoft, Telos, CoreCare). What's new is full done-for-you work at lower cost, but families and state caseworkers remain the real bottleneck.
- **Market size: 3.** My rough estimate, not sourced: about 15,000 homes × roughly 30 new applications a year × about $1,500 per case, plus renewals, comes to about $0.7–0.9B nationally. Indiana alone is probably $10–20M.
- **Risk: 2.** State portals and caseworkers may not deal with an AI agent. Rules on who can act for the applicant and on automated calls and texts to families add friction. Per-approval pricing means waiting 45 to 90+ days to get paid and taking on the risk of cases that were never eligible. CoreCare, MedicaidSoft or ExaCare could bundle this into products homes already buy.

## 3. What would kill it, and the fastest test
**What kills it:** most unpaid days come from the state's processing time rather than slow filing or missing documents, or homes won't pay enough per approval to cover the cost of doing the work.

**Fastest test (two weeks):** approach 10 Indiana business-office managers or administrators through the state nursing-home association (IHCA). Ask each for the last 12 months of their pending-case log: date the resident became eligible, date filed, date approved, denial reasons and write-offs. Then offer to take their oldest stuck cases at a fixed fee per approval.
- **Kill signals:**
  - Fewer than 3 of 10 hand over cases.
  - Late filing or missing documents account for less than about 15% of pending dollars.
  - Homes won't pay more than about $750 per approved case.
- The same test gives the first evidence from real customers; so far the case rests on desk research.

Sources:
- [KFF: 5 Key Facts About Nursing Facilities and Medicaid](https://www.kff.org/medicaid/5-key-facts-about-nursing-facilities-and-medicaid/)
- [CAP: OBBBA Implementation Timeline](https://www.americanprogress.org/article/the-implementation-timeline-of-the-one-big-beautiful-bill-act/)
- [NHeLP: OBBBA Slashes Retroactive Coverage](https://healthlaw.org/resource/obbba-slashes-retroactive-coverage-for-medicaid-beneficiaries/)
- [Genworth/CareScout 2024 Cost of Care](https://investor.genworth.com/news-events/press-releases/detail/982/genworth-and-carescout-release-cost-of-care-survey-results)
- [Indiana Capital Chronicle: delayed Medicaid payments](https://indianacapitalchronicle.com/2026/04/08/providers-wait-for-hundreds-of-millions-in-delayed-medicaid-payments/)
- [Indiana PathWays FAQ](https://www.in.gov/pathways/frequently-asked-questions)
- [CoreCare](https://corecare.ai/)
- [MedicaidSoft for Care Facilities](https://www.medicaidsoft.com/care-facilities)
- [MedicaidSoft (HPSI)](https://hpsi.epictetus.medicaidsoft.com/)
- [Telos LTC](https://www.telosltc.com/)
- [RevSuite](https://www.revsuitesolutions.com/)
- [Senior Planning Services Indiana](https://www.seniorplanning.com/state/indiana)
- [Medicaid Plus](https://www.mymedicaidplus.com/nursing-facilities.html)
- [MCA Skilled](https://mcaskilled.com/snf-billing-outsourcing/)
- [Richter](https://www.richterhc.com/skilled-nursing-consulting-services)
- [ExaCare Series A](https://www.prnewswire.com/news-releases/exacare-ai-raises-30m-series-a-to-reimagine-admissions-and-launch-a-powerful-suite-of-ai-agents-for-skilled-nursing--home-care-302586587.html)
- [PointClickCare Marketplace](https://marketplace.pointclickcare.com/s/)

VERDICT: BACK
