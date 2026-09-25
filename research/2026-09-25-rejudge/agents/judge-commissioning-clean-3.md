**Verdict: PASS.** It could be a good services business, but it isn't a venture-scale bet in its current form. My web search allowance ran out partway through, so the list of competing firms and the Vertiv–PurgeRite deal are less checked than the market figures.

## Checking the claims

- **$50.7B annual rate in April 2026, up 27%: confirmed.** Bloomberg and trade press cite Census figures of $39.8B a year earlier, which is +27.4%. One outlet says +28.1%, probably measured against a revised base. I couldn't read the Census PDF directly.
- **$200,000 per MW per month: a little high for AI halls.** CBRE's average asking rate was $196.25/kW/month for 250–500 kW leases in H2 2025, rising about 4% in H1 2026. Leases of 10 MW and up, which is where AI halls sit, were about $160–185/kW. Vacancy in the main markets was a record-low 1.4%.
- **Commissioning agents are scarce: supported, but the evidence is thin.** Recruiters report agent job openings staying unfilled past 120 days, and contract commissioning engineers billing $145–225/hour. There are also reports of specialist test crews, not equipment, holding up energization. Most of this comes from recruiters and trade blogs, not from primary data.
- **Liquid-cooled halls take longer to test.** One trade source says the full-load integrated test runs 10–14 weeks in a liquid-cooled hall, against 4–6 weeks in a conventional one. I found this in one secondary source only.
- **What commissioning costs.** Commissioning usually costs 0.5–2% of construction, or about $50k–240k per MW. US spend on it is therefore roughly $0.5–1B a year. One market report puts the global testing-and-commissioning market at $2.2B in 2025.

## Who else serves this customer

- **Software that already writes test scripts.** CxPlanner (its CxAI feature), Facility Grid, CxAlloy and BlueRithm already hold the commissioning checklists, issue logs and records. Facility Grid says its AI drafts test scripts in under two minutes, where a senior person takes 4–8 hours per piece of equipment. So writing scripts and drafting reports is already a feature of existing tools, not an edge.
- **Automated grading of test data has been done before.** Lawrence Berkeley National Lab built a semi-automated tool for analysing functional test data. Microsoft holds a patent (US10871754) on automated electrical commissioning, which suggests hyperscalers build this for themselves. Load-bank makers such as Crestchic ship software that coordinates up to 240 liquid-cooled load banks and records the results.
- **The buying channel for big builds is taken.** Hyperscalers hire their own commissioning agent under long-term service contracts with established engineering firms. On liquid cooling, equipment makers are moving into testing: Vertiv bought PurgeRite for about $1B.
- **What's open.** No incumbent owns the live test data, and neoclouds and new developers still choose their agents deal by deal.
- **No exact match.** I found no company making this same pitch.

## 1. The strongest version

- **Customer.** Work for the owner as its independent commissioning agent, selling to neoclouds and developers building liquid-cooled halls of 20–200 MW. Don't sell to general contractors: the agent who signs off has to be independent of the builder, and the GC is the party being checked.
- **Product.** Put the edge in the last two stages, the functional tests and the integrated full-load test. The system takes in building-management, power-monitoring, cooling-unit and load-bank data live, grades each step as it runs, and sends failures to the right trade the same day.
- **Pricing.** Charge per MW, plus a bonus for handing over before the planned date. Handover speed is worth far more than the fee. At about $180/kW/month, each day saved on 100 MW is worth about $600k in rent. That compares with a total commissioning fee of roughly $5–15M for the same 100 MW.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Agent job openings stay unfilled past 120 days; vacancy is a record-low 1.4% (CBRE), so every day of delay costs rent. |
| Value over today | 2 | Script writing and reports are already sold by CxPlanner and Facility Grid; the live grading is new but not proven to shorten tests. |
| Market size | 3 | US commissioning spend is about $0.5–1B a year (0.5–2% of $50.7B); it's services revenue and moves with the AI build-out. |
| Risk (5 = low) | 2 | The agent who signs carries professional liability; hyperscalers run their own programs; a senior agent still has to be on site to witness. |

## 3. What would kill it

**The kill.** The pitch assumes one agent can cover several times the megawatts. That fails if the integrated test is held up by physical things rather than agent hours spent on analysis and paperwork. Those physical things are:
- the senior agent having to be on site to witness failure scenarios,
- defects the trades must fix,
- controls integration,
- load-bank logistics.

In that case the AI saves maybe 1.5x in agent hours, handover doesn't move, and the company is just a well-run commissioning firm using tools anyone can buy.

**Fastest test (about 2 weeks).** Get the daily logs and issue logs from 3–5 recent liquid-cooled integrated tests, through a commissioning firm or a neocloud's construction lead. Sort every lost day into one of two groups:
- waiting on the agent: availability, analysing data, writing up;
- waiting on fixes: defects, equipment, trades.

If agent-bound time is under about 15% of test days, the leverage claim and the schedule bonus don't hold, so pass for good. If it's above about 30%, run the grader on those same data sets afterwards and compare it with the human pass/fail calls.

## Sources

- [Bloomberg: US data center construction spending eclipses $50B](https://www.bloomberg.com/news/articles/2026-06-01/us-construction-spending-on-data-centers-eclipses-50-billion)
- [Electrical Marketing: April data center spending](https://www.electricalmarketing.com/economic-data/construction-industry/article/55383786/data-centers-still-sizzling-with-a-287-april-yoy-spending-increase-to-507-billion)
- [MLQ: Census data center construction](https://mlq.ai/news/v2/us-census-data-center-construction-hits-507b-annualized-rate-surpassing-office-spending/)
- [CBRE North America Data Center Trends H1 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026)
- [CBRE North America Data Center Trends H2 2025](https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025)
- [iRecruit: data center commissioning careers](https://www.irecruit.co/insights/data-center-commissioning-careers-trends)
- [Environment+Energy Leader: commissioning crews delay finished grid projects](https://www.environmentenergyleader.com/stories/commissioning-crews-now-delay-finished-grid-projects,134804)
- [Archdesk: why AI data centers are so expensive](https://archdesk.com/blog/ai-data-center-costs)
- [CxPlanner: what commissioning costs](https://cxplanner.com/commissioning-101/what-does-commissioning-cost)
- [CxPlanner: CxAI across commissioning levels](https://cxplanner.com/blog/how-cxai-redefines-data-center-commissioning-across-levels)
- [CxPlanner: commissioning AI agents](https://cxplanner.com/commissioning-101/commissioning-ai-agents)
- [Facility Grid: approach to AI](https://facilitygrid.com/our-approach-to-ai/)
- [LBNL: semi-automated functional test data analysis tool](https://datacenters.lbl.gov/publications/semi-automated-functional-test-data)
- [Microsoft patent US10871754](https://patents.google.com/patent/US10871754)
- [Astute Analytica: commissioning and testing services market](https://www.astuteanalytica.com/industry-report/data-center-commissioning-and-testing-services-market)
- [Data Center Knowledge: data center M&A outlook 2026 (Vertiv–PurgeRite)](https://www.datacenterknowledge.com/investing/data-center-m-a-outlook-robust-in-2026-despite-power-ai-risks)

VERDICT: PASS
