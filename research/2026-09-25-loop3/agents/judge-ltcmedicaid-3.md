I didn't open any local project files, as you asked, although the repo's AGENTS.md says to read METHOD.md and STATE.md first. This is all web research. Nothing here is customer validation. I hit the session's web-search limit before the competitor scan was finished, so a company that exactly matches this pitch could still exist.

## How the claims hold up
- **$9,300 a month:** The number is right but it measures the wrong thing. Genworth's 2024 median for a semi-private room is $111,325 a year, about $9,277 a month. That is the private-pay price. What a home actually loses is the Medicaid rate minus the resident's own income contribution, which is less.
- **Medicaid pays for over 60% of 1.2 million residents:** Correct. KFF puts it at 63% as of 2024.
- **Retroactive coverage drops from three months to two in 2027:** Correct. Section 71112 cuts it to two months for everyone outside the ACA expansion group, starting with applications submitted on or after January 1, 2027. But it only costs money when the home files late. Coverage starts from the application date, so a slow caseworker delays cash but doesn't lose it. In practice the change adds about one month of exposure on late filings.
- **"Five years of bank statements":** Five years is how far back the state looks for transfers (60 months in 49 states). It isn't necessarily the stack of statements you file up front. I couldn't confirm Indiana's specific document rules.
- **Indiana context:** Indiana moved people 60 and over into a managed-care program (PathWays) in 2024. Its nursing homes are also squeezed by $462M in delayed supplemental payments to 496 homes.

## Who else serves this customer
- **MedicaidSoft** is the closest match, but it sells software rather than doing the work. It has guided family intake, AI eligibility flags, state forms filled automatically, and a tool that pulls bank statements (via Plaid) and flags look-back transfers. It is sold through the nursing-home purchasing group HPSI. That covers most of the pitch's technical pieces.
- **Outsourced eligibility firms** already do the whole job. Richter works nationally. Regional firms such as Medicaid Plus advertise "No Cost to You" to the facility, which means the price homes expect to pay is close to zero.
- **ExaCare** raised a $30M Series A. Its admissions and reimbursement AI agents run in 1,500+ facilities, including Majestic Care, and it is well placed to add Medicaid-pending work.
- **PointClickCare** owns the data. It has about 60% of the nursing-home software market, and its billing system already tracks each Medicaid-pending account, its expected decision date and its retroactive window.
- **Cova** (a Y Combinator company) is an AI-run home-care agency. It overlaps with the planned home-care expansion, not with nursing homes.

## 1. The strongest version
Don't sell software. Be an AI-run eligibility firm for multi-facility nursing-home operators, paid per approved case:
- **Entry point:** take over each operator's oldest stuck Medicaid-pending cases and its denials. A case denied for missing documents is where the application date, and the money, is actually lost.
- **Then:** forecast when each private-pay resident will run out of money and file on the right date, which the 2027 rule makes more important. Handle every annual renewal.
- **Data:** pull the pending lists from PointClickCare's partner marketplace.
- **Scope:** drop VA benefits and long-term-care insurance, which have different buyers. Treat home-care Medicaid as a later step, since Indiana's waiver has a waitlist of 11,791.

## 2. Ratings
- **Customer need: 4.** Pending receivables are a core pain for the business office. A CPA benchmark puts nursing-home bad debt at 1.41% of revenue and links it to Medicaid eligibility problems.
- **Value over what they use today: 2.** Eligibility firms already offer this at "no cost" to the facility, and MedicaidSoft already has the AI transfer-flagging. What's left to add is persistent texting and calling of families, and faster turnaround on caseworker requests.
- **Market size: 3.** My rough estimate, not sourced: a few hundred thousand applications a year nationally plus renewals, at a per-case fee, is a market under $1B. Indiana alone is roughly a $10–20M wedge.
- **Risk: 2 (fairly high).** The price anchor is near zero, and PointClickCare and ExaCare sit on the data and the buying relationship. Charging only on approval also leaves the startup carrying the loss on cases that were never eligible. On top of that, rules differ by state and by county.

## 3. What would kill it, and the fastest test
**The killer:** the money homes lose is mostly waiting on the state or on residents who were never eligible. It isn't families slow to send documents or late filings, which is what an AI caseworker can fix. If so, operators won't pay more than today's near-free eligibility firms.

**Fastest test:** offer 10 Indiana operators to take their 10 oldest pending or denied cases, paid only on approval. In the same offer, ask for their Medicaid-pending aging report and their last 12 months of eligibility-related write-offs. Pass if at least 3 sign and hand over files within 2 weeks, and the reports show most of the stuck dollars waiting on family documents. If the stuck dollars are mostly waiting on the state, stop.

Why I'm passing: the need is real, but the added value over existing firms and software is thin, the 2027 rule change adds only about a month of exposure, and the incumbents hold the data and the buying channel.

Sources: [King & Spalding on the OBBBA](https://www.kslaw.com/news-and-insights/the-one-big-beautiful-bill-act-explained-a-detailed-review-of-key-changes-for-the-healthcare-industry), [KFF on nursing facilities and Medicaid](https://www.kff.org/medicaid/5-key-facts-about-nursing-facilities-and-medicaid/), [Genworth 2024 Cost of Care](https://investor.genworth.com/news-events/press-releases/detail/982/genworth-and-carescout-release-cost-of-care-survey-results), [MedicaidSoft features](https://www.medicaidsoft.com/software-features), [MedicaidSoft for HPSI members](https://hpsi.epictetus.medicaidsoft.com/), [Richter](https://www.richterhc.com/medicaid-consulting), [Medicaid Plus](https://www.mymedicaidplus.com/nursing-facilities.html), [ExaCare Series A](https://www.prnewswire.com/news-releases/exacare-ai-raises-30m-series-a-to-reimagine-admissions-and-launch-a-powerful-suite-of-ai-agents-for-skilled-nursing--home-care-302586587.html), [PointClickCare market share](https://intuitionlabs.ai/articles/pointclickcare-ehr-long-term-care), [Cova (Y Combinator)](https://www.ycombinator.com/companies/cova), [GMA nursing-home bad-debt benchmark](https://www.gma-cpa.com/blog/how-does-your-skilled-nursing-facilitys-bad-debt-expense-as-a-percentage-of-revenue-measure-up), [Indiana Capital Chronicle on delayed payments](https://indianacapitalchronicle.com/2026/04/08/providers-wait-for-hundreds-of-millions-in-delayed-medicaid-payments/), [Indiana Medicaid long-term care](https://www.in.gov/medicaid/providers/clinical-services/long-term-care/), [Medicaid look-back period](https://www.medicaidplanningassistance.org/medicaid-look-back-period/)

VERDICT: PASS
