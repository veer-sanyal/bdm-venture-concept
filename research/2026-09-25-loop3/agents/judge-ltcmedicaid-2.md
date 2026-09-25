I'd back this, with medium conviction. The core claims check out, but two of them are weaker than the pitch makes them sound. A company already sells nearly this exact product (Reap, getreap.com), so per your instructions I've counted it as this team, not a competitor.

I followed your instruction not to read local project files, which meant skipping the repo's AGENTS.md step of reading METHOD.md and STATE.md. My web search allowance ran out near the end. Market-size and fee numbers marked "estimate" are my own and not sourced.

## Claims checked against sources
| Claim | Result |
|---|---|
| About $9,300 a month (Genworth 2024) | **True.** It's the semi-private room median, $111,325 a year. A private room is $127,750. But a home that's paid after approval gets the Medicaid rate, not this price, so $9,300 overstates what's at risk. |
| Medicaid is main payer for over 60% of 1.2M residents | **True.** KFF, July 2024 data. |
| Retroactive coverage drops from 3 months to 2 from Jan 2027 | **True.** It covers applications filed on or after Jan 1, 2027, for non-expansion enrollees. But the pitch overstates the effect. Once an application is filed and approved, the home is paid back to the filing date. The cut only hurts when filing comes more than 2 months after the resident became eligible. It adds modest pressure to file quickly; it doesn't force homes to buy. |
| Indiana as the first market | Plausible. About 496 homes are waiting on $462M in delayed payments. Indiana is also ending nursing-home managed care in July 2027, which changes billing but not who decides eligibility. There were also reports of an application backlog at the state's welfare agency (FSSA) in 2025. |

## Who else serves this customer
- **Reap: near-exact match, treated as this team.** Its AI agent "Ruby" does the whole list: Medicaid applications, reading bank statements (claims 99.1% accuracy), five-year transfer review, answering caseworker requests, deadlines and renewals in all 50 states. It integrates with PointClickCare. Its site shows 12 buildings and 1,846 residents. It may have raised $3.79M from Ludlow, but that figure could be mixed up with another company named Reap Tech, so treat it as unverified.
- **Software:**
  - MedicaidSoft was built by elder-law attorneys. It fills state forms, pulls bank statements and screens eligibility with AI. It claims to cut the backlog of pending cases by 20–50% and has a dedicated page for members of HPSI, a nursing-home purchasing group.
  - CoreCare tracks eligibility for 1,500+ facilities, mainly in Texas and Ohio.
  - AR Proactive tracks pending cases but doesn't file them.
- **Service firms:** Senior Planning Services (22 states, including Indiana), Medicaid Plus (PA, NJ, DE, MD), Medicaid Solutions LLC in Indiana, and elder-law attorneys. Medicaid Plus advertises "No Cost to You" to facilities and charges families instead. A per-approved-case fee has to beat that price of zero.
- **Who owns the data and the buying channel:** PointClickCare owns most homes' records and runs the marketplace where add-ons are bought, and it already tracks pending status and retroactive dates. It's a partner today but could build this itself. Purchasing groups like HPSI are the second channel. No incumbent owns the case work itself.

## 1. Strongest version
An AI back office for multi-facility nursing-home operators, priced on outcomes. Two changes to the pitch:
- **Narrow the promise** to "no case sits in pending": the file goes in within X days of the resident running out of money, it gets approved, and renewals don't lapse. The fee is per approved case, with a refund if a denial was caused by paperwork.
- **Land with the bank-statement review tool.** Reap already sells one standalone ("Analyze"). Use it to get in the door, then take over the whole case.

The goal is to replace the outside eligibility firm and most of the business-office workload. Then expand into payer verification and collections for the same homes, which is the only route to a large company. Keep home-care Medicaid as the next step, since it needs the same five-year review. Drop VA benefits and long-term-care insurance claims: they have different buyers and workflows. VA also restricts charging fees for help with initial claims (from my own knowledge, not checked this session).

## 2. Ratings
- **Customer need: 4.** Operators hire dedicated "Medicaid Pending Specialist" staff (a PACS job listing), and a whole industry of firms and software exists to handle these cases.
- **Value over current options: 3.** Full-service firms already exist, some free to the home. The gain is speed and cost, not something new.
- **Market size: 3.** About 750k Medicaid residents nationally. New applications plus renewals come to roughly $0.5–0.8B a year (estimate). It only gets big by expanding into the rest of the back office and home care.
- **Risk: 2.** Every state has its own forms and portal, free-to-home competitors undercut the price, and state backlogs plus uncooperative families can delay approvals regardless of the product.

## 3. What would kill it, and the fastest test
**It dies if:**
- the real bottleneck is families not cooperating or state caseworker backlogs, not the home's staff time, so faster automated filing doesn't change approval dates or write-offs; or
- homes won't pay per case while family-paid firms cost them nothing.

**Fastest test (about 2 weeks):** Get the last 12 months of pending cases and denial write-offs from 5–10 Indiana operators. Ask each for a letter of intent at a stated per-approved-case price, around $1,500 (an assumed figure, not sourced). If write-offs are small (roughly under $50k per facility a year) or no one signs, pass.

Sources:
- [Morgan Lewis on the Medicaid changes in the One Big Beautiful Bill Act](https://www.morganlewis.com/pubs/2025/07/one-big-beautiful-bill-act-key-final-medicaid-changes-explained)
- [KFF: 5 key facts about nursing facilities and Medicaid](https://www.kff.org/medicaid/5-key-facts-about-nursing-facilities-and-medicaid/)
- [Genworth 2024 Cost of Care survey](https://investor.genworth.com/news-events/press-releases/detail/982/genworth-and-carescout-release-cost-of-care-survey-results)
- [Indiana Capital Chronicle on delayed payments](https://indianacapitalchronicle.com/2026/04/08/providers-wait-for-hundreds-of-millions-in-delayed-medicaid-payments/)
- [Indiana ending nursing-home managed care](https://distilinfo.com/2026/03/16/indiana-drops-managed-care-for-medicaid-ltc/)
- [Reap](https://getreap.com/)
- [Analyze by Reap](https://analyze.getreap.com/)
- [Reap funding snippet (Tracxn)](https://tracxn.com/d/companies/reap/__sHerJoqJYN2RV7oQW0HfiXNquMdPY2JGaU88nE_EnAg)
- [MedicaidSoft for care facilities](https://www.medicaidsoft.com/care-facilities)
- [MedicaidSoft for HPSI members](https://hpsi.epictetus.medicaidsoft.com/)
- [CoreCare](https://corecare.ai/)
- [AR Proactive](https://www.arproactive.com/works-with-pointclickcare)
- [Medicaid Plus](https://www.mymedicaidplus.com/nursing-facilities.html)
- [Senior Planning Services, Indiana](https://www.seniorplanning.com/state/indiana)
- [PACS "Medicaid Pending Specialist" job listing](https://www.disabledperson.com/jobs/75332459-medicaid-pending-specialist)

VERDICT: BACK
