I recommend backing this company, but only in the narrowed form in section 1. It is a close call. The need is real and urgent, but the edge over incumbents is thinner than the pitch suggests.

## What checked out, and what didn't
- **Construction spending: confirmed.** Data center construction ran at a $50.7B annual rate in April 2026 (Census data, as reported by Bloomberg and Electrical Marketing). Growth was about 27–28% over the year, not exactly 27%.
- **The $200k per MW per month lease rate is the top of the range.** CBRE's average asking rent for small wholesale deals (250–500 kW) was $196/kW-month. Deals of 10 MW and up, which are what AI halls look like, ask about $160–185. Treat $200k as the ceiling.
- **The full-load integrated test before handover: confirmed.** It is standard practice as the final test level (called Level 5). Liquid cooling makes it harder. Uptime Institute (January 2026) says best practice for liquid-cooling commissioning is still immature, and some cooling-unit makers have little data center experience. One source (the Archdesk blog, not primary) puts the integrated test at 10–14 weeks for a liquid-cooled hall, against 4–6 for an air-cooled one.
- **Agent scarcity: only secondary evidence.** Recruiters report commissioning agent jobs open more than 120 days, and a DataX Connect survey shows commissioning pay up 16% since 2023. It points the right way but is not proven.
- **Market size: roughly $0.25–1.5B a year in the US.** Commissioning is typically 0.5–3% of construction cost. CBRE counts a record 7.5 GW under construction in the main markets, 80% already leased.

## Who else serves this customer
- **Commissioning firms that own the relationship:** Bureau Veritas (Primary Integration), Salute, Burns & McDonnell, Jacobs, Salas O'Brien, NV5 (Herman Cx), and Bowman (being bought by Bernhard Capital for about $1B).
- **Software sold to commissioning firms:**
  - CxAlloy (owned by Trinity Consultants) bought OTTO in 2024. OTTO already runs automated functional tests from building-system trend data.
  - CxPlanner's CxAI drafts test scripts.
  - AutoCXI runs scripted tests against the building-management system and reports pass/fail step by step.
  - Facility Grid and Bluerithm offer commissioning workflow tools, and Facility Grid has an AI checklist feature.
  - Load-bank vendors such as Aggreko supply the test load but not the grading.
- **No company matches this pitch closely.**
- **Who owns the channel and the data:**
  - The owner's standing contracts with established commissioning firms are the buying channel, and those firms own it.
  - The building and power data belongs to the owner and runs on Siemens, Schneider or JCI systems, so no rival holds it exclusively.
  - A new entrant has to win on trust, not on data access.

## 1. The strongest version
Be the owner's independent commissioning agent, not a service for the general contractor. Industry guidance and Womble Bond Dickinson both say the agent must be independent and hired by the owner. An agent paid by the builder it is checking loses its purpose, so selling to general contractors undermines the product.

Target the fast-growing developers and neoclouds that have no in-house commissioning team: CoreWeave, Crusoe, Lambda, Applied Digital, and colo developers building for them. Skip the hyperscalers, which run their own programs through standing contracts.

Start with the liquid-cooling scope: the cooling units and liquid loops, from component tests through the integrated test. Charge a fixed fee per MW and offer a schedule guarantee. The measure that matters is weeks taken out of the integrated test and the reports around it. At roughly $160–200k per MW per month in rent, one week saved is worth more to the owner than most of the fee.

The AI's leverage is on scripts, reviewing test data and drafting reports. A senior agent still has to be on site to witness, so expect about 2x more megawatts per agent, not "several times".

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Uptime says liquid-cooling commissioning is immature; one month's slip on a 60 MW hall costs about $14M in lost revenue (secondary source). |
| Value over today | 3 | CxAlloy/OTTO, AutoCXI and CxAI already automate parts of this. What's new is grading the whole integrated test and taking signing responsibility for it. |
| Market size | 3 | 0.5–3% of a $50.7B US build rate is about $0.25–1.5B a year, and it is services-shaped and follows the build cycle. |
| Risk (5 = low) | 2 | The company carries liability for signing off halls worth $1B or more. Incumbents hold the owner contracts, and 30–50% of US projects planned for 2026 are expected to slip or be cancelled. |

## 3. What would kill it, and the fastest test
**What would kill it:** owners won't hand integrated-test sign-off on a liquid-cooled hall to a new firm. If that happens, it becomes another labor-bound commissioning shop competing for the same scarce senior agents. A second risk is that the physical testing, not the paperwork, sets the schedule, so the software saves little time.

**Fastest test:** within 30 days, send a signed fixed-fee-per-MW proposal to the construction or commissioning leads at about 15 neocloud and colo developers building liquid-cooled halls. It should cover the liquid-cooling and integrated-test scope for one real upcoming hall, with a named senior agent. Back it with a blind re-run on one finished hall: the software grades that hall's old test data, and its findings are compared with what the human agent signed. Kill the idea if fewer than two developers sign a paid pilot or letter of intent. None of the research above counts as customer validation.

I didn't read local project files, as you asked. My web search budget ran out before I could check hyperscaler commissioning contracts or any AI programs at Bureau Veritas or Salute.

Sources:
- [Bloomberg: construction spending on data centers passes $50B](https://www.bloomberg.com/news/articles/2026-06-01/us-construction-spending-on-data-centers-eclipses-50-billion)
- [Electrical Marketing: April data center spending](https://www.electricalmarketing.com/economic-data/construction-industry/article/55383786/data-centers-still-sizzling-with-a-287-april-yoy-spending-increase-to-507-billion)
- [CBRE North America Data Center Trends H1 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026)
- [CBRE Global Data Center Trends 2026](https://www.cbre.com/insights/reports/global-data-center-trends-2026)
- [Uptime Intelligence: cooling units complicate commissioning](https://intelligence.uptimeinstitute.com/resource/coolant-distribution-units-can-complicate-commissioning)
- [Archdesk: integrated test durations and delay cost](https://archdesk.com/blog/global-ai-data-center-construction-2026)
- [CxAlloy acquires OTTO](https://www.cxalloy.com/cxalloy-acquires-otto/)
- [AutoCXI](https://autocxi.com/)
- [CxPlanner CxAI](https://cxplanner.com/blog/how-cxai-redefines-data-center-commissioning-across-levels)
- [Bureau Veritas acquires Primary Integration](https://group.bureauveritas.com/bureau-veritas-acquires-primary-integration-solutions-united-states)
- [Womble Bond Dickinson: performance guarantees](https://www.womblebonddickinson.com/us/insights/alerts/critical-performance-guarantees-data-center-construction-contracts-and-risk)
- [Introl: workforce shortage](https://introl.com/blog/data-center-workforce-shortage-340000-unfilled-positions-2026)
- [CxPlanner: what commissioning costs](https://cxplanner.com/commissioning-101/what-does-commissioning-cost)
- [DC Geeks: commissioning guide and costs](https://dcgeeks.com/what-data-center-commissioning/)
- [Benzinga: private equity and data center services](https://www.benzinga.com/markets/private-markets/26/09/61825637/private-equity-finds-a-new-way-to-bet-on-ai-data-center-services)
- [Aggreko: liquid-cooled load banks](https://www.aggreko.com/en-pg/case-studies/data-centres/precision-testing-with-liquid-cooled-load-banks)

VERDICT: BACK
