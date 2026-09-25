## Investor assessment: AI-native commissioning for liquid-cooled AI data halls

This is desk research only. No customer has confirmed anything here.

### Claims checked against sources
- **$50.7B annual rate, up 27%: confirmed.** Census data for April 2026, reported by Bloomberg, shows $50.7B against $39.8B a year earlier. One secondary source says July reached about $75B. I couldn't confirm that against Census, and a revision to the series may explain the jump.
- **$200,000 per MW per month: roughly right, but at the top of the range.** CBRE's H1 2026 report puts small 250–500 kW deals above $215/kW/month. The 10 MW+ leases that AI halls actually sign price lower. CBRE also reports record primary-market vacancy of 1.4%, 7.5 GW under construction and 80% of it preleased. That supports the idea that delay is expensive.
- **Scarce commissioning agents: plausible but thinly sourced.** Uptime Institute's 2025 survey found nearly two-thirds of operators struggle to hire or keep staff, but that covers operators generally. Evidence specific to commissioning agents comes from recruiters. The public cases of AI halls running late point elsewhere: CoreWeave's Denton site with Core Scientific slipped on weather and design changes. A Tetra Tech expert names coolant contamination and sequencing, not paperwork, as the main liquid-cooling commissioning problem.

### Who else serves this customer
- **Commissioning software:**
  - CxAlloy is owned by Trinity Consultants, which bought OTTO in July 2024. OTTO does automated functional testing from building-management trend data.
  - CxPlanner sells "CxAI", which generates checklists and extracts tags from drawings. Its customer logos include commissioning firms.
  - Facility Grid and BlueRithm are the other workflow tools.
  - ArchiLabs, a YC-backed design platform, says it can generate commissioning test procedures.
- **Commissioning services:** engineering firms such as Syska Hennessy and Tetra Tech, plus LotusWorks. Vertiv sells liquid-cooling commissioning through all five test levels.
- **Hyperscalers do it themselves.** AWS employs its own commissioning engineers. Microsoft holds a patent (US10871754) on automated, time-synchronized commissioning with pass/fail grading, which is this product's core.
- **Nobody locks up the data or the buying channel for non-hyperscale owners.** Each project is bought separately, and the owner controls access to building-management and power-monitoring data during construction. Hyperscalers are effectively closed. The workflow data sits with CxAlloy, CxPlanner and Facility Grid.
- I found no company whose pitch matches this one almost exactly.

### 1. Strongest version
Reshape it in three ways:
- **Sell to the owner, not the contractor.** The commissioning agent must be independent of the contractor whose work it checks, so a contractor-paid agent is a conflict of interest.
- **Target owners without in-house commissioning programs.** These are neoclouds, newer developers, and bitcoin miners converting sites to AI hosting.
- **Narrow to the final two test levels of liquid-cooled halls.** That means functional tests and the integrated test: cooling-loop flushing and cleanliness, balancing water flow, leak checks, and staged heat-load tests.

The software would:
- merge building-management, power-monitoring, cooling-unit and load-bank data on one timeline;
- grade each test step live against the acceptance criteria;
- deliver a signed report within 24 hours.

Pricing stays a fixed fee per MW. A bonus tied to schedule could be added.

A second product is worth considering: a readiness check the contractor legitimately owns, run before the integrated test so the owner's test passes the first time.

### 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 3 | Delay is expensive: roughly $15–20M a month per 100 MW at the lease rate above. But the public delays trace to weather, design changes and contamination, not commissioning labor. |
| Value over today | 3 | CxAlloy with OTTO already does automated functional testing from building data, and CxPlanner already generates checklists with AI. What's new is live grading of the integrated test itself, and it isn't clear that is where the schedule is lost. |
| Market size | 3 | US data centers added about 12 GW in 2026, and 36 GW is scheduled for 2027 (Goldman Sachs). Commissioning typically costs 0.5–2% of about $11M/MW, which suggests roughly $0.6–2B a year in the US. That is my estimate; a hyperscaler share is done in-house, and this is services revenue. |
| Risk (5 = low) | 2 | A new firm signs off on halls worth hundreds of millions, carrying professional liability. Senior agents still have to be on site to witness tests, and demand depends on a construction boom. |

Total: 11 of 20.

### 3. What would kill it, and the fastest test
**Killer:** script writing, grading and report turnaround aren't on the integrated test's critical path. A witness has to be physically present, so one senior agent can't cover several simultaneous tests. The "several times the megawatts" leverage then collapses to saving a junior engineer's documentation hours, which isn't enough to make owners switch to an unproven signer.

**Fastest test:** ask 5 owner-side commissioning leads at neoclouds or developers for the day-by-day log of their last liquid-cooled integrated test. Count the days lost to script prep, witnessing, grading and report turnaround against days lost to physical fixes and waiting on load banks. If the first group is under about 10% of the test window, kill it. Also ask each lead whether they would hire a new agent at a fixed fee per MW.

VERDICT: PASS

Sources:
- [Bloomberg: data center construction spending tops $50B](https://www.bloomberg.com/news/articles/2026-06-01/us-construction-spending-on-data-centers-eclipses-50-billion)
- [Electrical Marketing: April data center spending $50.7B](https://www.electricalmarketing.com/economic-data/construction-industry/article/55383786/data-centers-still-sizzling-with-a-287-april-yoy-spending-increase-to-507-billion)
- [Crypto Briefing: July ~$75B (unverified)](https://cryptobriefing.com/data-center-construction-record-75b-pace/)
- [CBRE North America Data Center Trends H1 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026)
- [CBRE rental rate summary](https://www.cbre.com/insights/reports/global-data-center-trends-2026)
- [Goldman Sachs: US data center power demand](https://www.goldmansachs.com/insights/articles/us-data-center-power-demand-projected-to-double-by-2027)
- [Uptime Institute staffing survey](https://intelligence.uptimeinstitute.com/resource/survey-highlights-industry-staffing-crisis)
- [Tetra Tech on liquid-cooling commissioning](https://www.tetratech.com/experts/john-herboth-discusses-challenges-in-commissioning-liquid-cooled-ai-data-centers/)
- [CNBC: CoreWeave / Core Scientific delays](https://www.cnbc.com/2025/11/11/coreweave-stock-core-scientific-delays.html)
- [TheMinerMag: Denton weather delay](https://theminermag.com/news/2025-12-16/coreweave-core-ai-delay)
- [Trinity Consultants acquires OTTO](http://trinityconsultants.com/news/trinity-consultants-acquires-otto-software)
- [CxPlanner data centers](https://cxplanner.com/data-centers)
- [CxPlanner AI agents](https://cxplanner.com/commissioning-101/commissioning-ai-agents)
- [CxPlanner: commissioning cost](https://cxplanner.com/commissioning-101/what-does-commissioning-cost)
- [ArchiLabs](https://archilabs.ai/posts/avoid-commissioning-issues-automate-data-center-testing)
- [Microsoft patent US10871754](https://patents.google.com/patent/US10871754B2/en)
- [Amazon patent US11638368](https://patents.google.com/patent/US11638368B2/en)
- [Vertiv liquid cooling services](https://www.vertiv.com/en-us/about/news-and-insights/corporate-news/vertiv-announces-global-launch-of-liquid-cooling-services-portfolio--to-support-systems-for-ai-and-high-density-compute-applications/)
- [DC Geeks: commissioning agent salaries](https://dcgeeks.com/data-center-commissioning-agent-salary/)
- [Archdesk: AI data center costs and IST duration](https://archdesk.com/blog/ai-data-center-costs)
