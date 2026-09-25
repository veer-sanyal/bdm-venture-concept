I'd pass on this as written, though it is close. The weak points are value and risk, not competition. Nobody sells this exact product, but the money only works if paperwork and grading hold up handover, and I found no evidence that they do.

## Checking the key claims

- **$50.7B annual rate in April 2026: confirmed.** Bloomberg, Electrical Marketing and MLQ all report it from Census data. It was $39.8B a year earlier, so growth was 27–28% depending on the outlet. Census's headline press release doesn't break out data centers; the figure sits in its detailed tables.
- **$200,000 per MW per month: that's the high end.** CBRE's H1 2026 report quotes $190–235 per kW per month in Northern Virginia and $200–230 in Chicago, but only for small 250–500 kW leases. For leases over 10 MW, CBRE gives only percentage increases, and big leases are usually priced lower. A late 50 MW hall still loses well over $1M in rent a week.
- **Agent scarcity: plausible, but the evidence is weak.** The sources are recruiters (for example, "nearly 60% of operators report difficulties" finding qualified commissioning engineers, and senior pay up to about $310k). I found no primary survey.
- **Commissioning spend:** about 0.5–3% of construction cost. Build cost is roughly $11M per MW (Turner & Townsend), with liquid-cooled halls about 7–10% more. That puts commissioning at roughly $55k–$330k per MW.

## Who else serves this customer

- **Commissioning firms** such as CAI and Primary Integration Solutions hold the owner relationships through master service agreements. Limbach bought CYMCOR for about $30M in August 2026, and T5/EverOn and Salute also offer commissioning oversight.
- **Commissioning software:**
  - CxPlanner's CxAI drafts test scripts from specs and equipment lists, but I found no live data grading.
  - ArchiLabs (a YC company) says it generates test procedures from design data and produces pass/fail reports from building-management data.
  - CxAlloy, Facility Grid, Bluerithm and Cadence track commissioning work.
- **Equipment makers** own the liquid-cooling startup work. Vertiv closed its roughly $1.1B purchase of PurgeRite (liquid-loop flushing) in December 2025 and sells commissioning for liquid cooling.
- **Load-bank rental firms** such as ComRent and Aggreko already hand over their own test data and power-quality reports.
- **Build.inc** (Index, $8.5M) automates work before construction, not commissioning.
- **No company matches this pitch closely.**

**Does an incumbent own the data or the buying channel?** Nobody owns the data. It sits in the owner's building-management and power-monitoring systems and in whatever commissioning platform they use, and it can be exported. The channel is held by incumbents: owners hire an independent commissioning agent through standing relationships. ASHRAE Guideline 0 and the AABC Commissioning Group (ACG) certification rules require that agent to be independent of the contractor. So selling to general contractors, as the pitch proposes, is a conflict of interest. The buyer has to be the owner.

## 1. Strongest version

This is an independent owner's commissioning agent for the last two test levels: system-by-system functional tests and the final full-load integrated test. It serves liquid-cooled AI halls for second-tier developers, such as neoclouds and former bitcoin miners converting sites for AI tenants. These owners have no in-house commissioning program and face a tenant deadline.

- **What it sells:** results graded the same day as each test, and a handover package the tenant accepts on the first submission.
- **How the leverage works:** junior technicians run the tests on site while a senior agent watches the graded data remotely and signs off. The senior agent is not reading every trend log by hand.
- **Price:** a fixed fee per MW, plus a bonus for handing over on schedule.
- **Drop the general contractor channel** because of the independence rule.
- **Later expansion:** recommissioning of operating sites, then chip fabs and pharma plants.

## 2. Ratings (total 12 of 20)

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | 80.4% of capacity under construction is pre-leased and primary-market vacancy is 1.4% (CBRE H1 2026), so every late week costs rent. Shortage evidence comes from recruiters. |
| Value over today | 3 | CxPlanner already drafts scripts. Test pace is often set by physical sequencing and upstream delays (a two-week energization slip costs four to six weeks of commissioning), not by paperwork. |
| Market size | 3 | 0.5–3% of the $50.7B annual rate is about $0.25–1.5B a year in the US. Venture scale needs the expansion markets. |
| Risk (5 = low) | 2 | Owners pick their agent through independence rules and standing relationships, and a new firm signing off a hall worth hundreds of millions carries liability. Witnessing tests still takes a senior agent's time, so "several times the megawatts" is unproven. |

## 3. What would kill it, and the fastest test

**What kills it:** documentation and grading turn out not to be what holds up handover, or tenants won't accept a new firm's sign-off. In either case it becomes a cheaper commissioning agent competing in a relationship market, with little leverage.

**Fastest test:** one week of calls with 5–8 construction or commissioning leads at second-tier AI developers. Ask each one about their last hall:
1. How many calendar days passed between the last integrated test and the tenant's acceptance?
2. How much of that went to writing, grading and review, and how much to physical fixes?
3. Who chose the commissioning agent: the owner or the tenant?

If documentation accounts for less than about a week, or the tenant chooses the agent, the idea dies.

This is desk research only, not customer validation.

**Sources:**
- [Bloomberg](https://www.bloomberg.com/news/articles/2026-06-01/us-construction-spending-on-data-centers-eclipses-50-billion)
- [Electrical Marketing](https://www.electricalmarketing.com/economic-data/construction-industry/article/55383786/data-centers-still-sizzling-with-a-287-april-yoy-spending-increase-to-507-billion)
- [MLQ](https://mlq.ai/news/v2/us-census-data-center-construction-hits-507b-annualized-rate-surpassing-office-spending/)
- [CBRE H1 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026)
- [Turner & Townsend](https://www.turnerandtownsend.com/insights/data-centre-construction-cost-index-2025-2026/)
- [CxPlanner CxAI](https://cxplanner.com/blog/how-cxai-redefines-data-center-commissioning-across-levels)
- [ArchiLabs](https://archilabs.ai/posts/avoid-commissioning-issues-automate-data-center-testing)
- [Data Center Frontier](https://www.datacenterfrontier.com/hyperscale/article/55403740/ai-infrastructure-is-redrawing-the-data-center-services-landscape)
- [Vertiv/PurgeRite](https://investors.vertiv.com/news/news-details/2025/Vertiv-Completes-Acquisition-of-PurgeRite-Expanding-Leadership-in-Liquid-Cooling-Services/default.aspx)
- [ACG requirements](https://www.commissioning.org/certificationrequirements/)
- [Independence and Guideline 0](https://commissioningmanager.com/article/what-is-a-third-party-commissioning-agent/)
- [Build.inc](https://thenextweb.com/news/build-8-5m-agentic-real-estate-ai-infrastructure)
- [ComRent](https://www.comrent.com/post/data-center-load-bank-testing)
- [Delay cascade (CMiC)](https://cmicglobal.com/resources/article/data-center-construction-trends)
- [Shortage figure (iRecruit)](https://www.irecruit.co/insights/data-center-commissioning-updates-2026)
- [Pay (Data Center Geeks)](https://dcgeeks.com/data-center-commissioning-agent-salary/)

VERDICT: PASS
