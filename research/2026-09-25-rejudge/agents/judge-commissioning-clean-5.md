1. **The strongest version.** The core claims mostly hold up, but the company should sell to data center owners and developers, not to general contractors. It should also stop pitching script-writing, because that part is already sold as a feature.

   **What the claims check out as:**
   - **Construction spending: true, and understated.** Census data shows $50.7B annualized in April 2026, up from $39.8B a year earlier. That's about 27% (some coverage says 28%). Coverage of the July Census release puts it above $75B, up nearly 60%, though I couldn't open the Census release to confirm it.
   - **Lease rate: too high for the target customer.** About $196k per MW per month is right for small deployments of 250–500 kW. The big halls this company would commission lease for roughly $100–170k per MW per month. CBRE's H1 2026 report shows 1.4% vacancy (a record low), 7.5 GW under construction in major markets, and 80% of it pre-leased. It also says liquid-cooled retrofits can take more than six months to be ready for service. So every week of delay is expensive.
   - **Scarce commissioning agents: supported, but weakly.** The evidence comes from recruiters and market-research firms, not primary data.
   - **Who hires the agent: the pitch gets this wrong.** For the final two test levels (the system tests and the full-load integrated test), the commissioning agent is almost always independent and hired by the owner. That independence is the whole point, so the pitch's "and their GCs" doesn't work. General contractors run the earlier levels.

   **The company I would back:** an independent, owner-hired commissioning firm that only does those final two levels on liquid-cooled AI halls.
   - **Customers:** fast-moving neocloud and colocation developers (the kind behind CoreWeave's delayed Denton site, which cut its 2025 revenue outlook by more than $200M), not hyperscalers with locked-in contracts.
   - **Price:** a fixed fee per MW, with part of the fee at risk if the integrated test runs past an agreed number of days.
   - **Technical edge:** script-writing is already a feature in off-the-shelf tools. The company's edge would be the grading engine, which merges building-management, power-monitoring and load-bank data during the test and grades each step as it happens. Load-bank vendors log data and produce compliance reports, but I found no sign that they grade against control-system data.
   - **Second channel:** white-label test capacity for incumbent commissioning firms that are turning work away.

2. **Ratings.**

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Record-low vacancy, 80% pre-leasing, slow liquid-cooled readiness, and CoreWeave's >$200M guidance cut from one late hall make schedule very costly. This is desk research, not customer validation. |
| Value over today | 3 | Facility Grid already sells AI that drafts test scripts in under two minutes versus 4–8 senior hours per piece of equipment, and CxPlanner has similar agents. What's left is live grading and signing off more MW per senior agent, which is unproven. The scarce thing is the senior agent's time on site witnessing physical tests, and AI speeds up the paperwork, not the testing. |
| Market size | 3 | Commissioning costs about 1–3% of an $8–12M-per-MW build, roughly $80–360k per MW. On about 10 GW a year in the US, that's around $1–2B, and the independent agent's share of the final two levels is a slice of that. Big enough, but it's services revenue. |
| Risk (5 = low) | 2 | Liability for signing off a failed 100 MW hall. Owners give critical testing to agents with a track record. Anyone can buy the same software. It depends on access to building-management and power-monitoring data. And it's tied to the AI capex cycle. |

   **Do incumbents own the channel and the data?** Yes, both.
   - **Channel:** owners hire the independent agent directly, often under master agreements with firms like AECOM and WSP or specialist commissioning firms.
   - **Workflow data:** Facility Grid, CxAlloy (owned by Trinity Consultants), CxPlanner and Bluerithm hold the scripts, checklists and issue logs.
   - **Test data:** load-bank vendors (Crestchic, Avtron, Thermon) capture load data during the full-load test.

   I found no company whose pitch matches this one almost exactly. ArchiLabs (a Y Combinator company) publishes about automating commissioning tests by reading control-system data, but it is mainly a design and BIM tool.

3. **What kills it, and the fastest test.**
   - **What kills it:**
     - Developers won't let a new firm sign off the full-load test on a live hall.
     - Or the leverage is really about 1.5x rather than several times, because witnessing is physical.
     - Either way, incumbents buy the same AI off the shelf and this becomes an ordinary services firm.
   - **Fastest test (1–2 weeks):** pitch 10 commissioning or construction leads at neocloud and colocation developers. Offer the liquid-cooled final-level package at a fixed per-MW price with fee at risk on schedule, and ask for a letter of intent on a real hall due in the next 6–9 months.
   - **Kill it if** fewer than 2 would award it directly or through their current commissioning firm.
   - **Useful follow-up:** re-run one completed hall's full-load test data through the grading engine and compare it with the human issue log. That shows whether the leverage is real.

I'd pass for now. The need is real, but the only AI piece that isn't already for sale doesn't free up the real constraint, which is senior witnessing time. On top of that, owners buy on track record and liability. A signed letter of intent from the test above plus a strong retrospective leverage result would change my view.

Sources:
- [Bloomberg: US construction spending on data centers eclipses $50B](https://www.bloomberg.com/news/articles/2026-06-01/us-construction-spending-on-data-centers-eclipses-50-billion)
- [Electrical Marketing: April data center spending $50.7B](https://www.electricalmarketing.com/economic-data/construction-industry/article/55383786/data-centers-still-sizzling-with-a-287-april-yoy-spending-increase-to-507-billion)
- [Axios: data center construction spending surged in July](https://www.axios.com/2026/09/01/ai-data-center-constructon-spending)
- [yourNEWS: July spending up nearly 60%](https://yournews.com/2026/09/02/7183957/u-s-data-center-construction-spending-jumps-nearly-60-as-ai/)
- [CBRE North America Data Center Trends H1 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026)
- [datacenterHawk 2026 pricing guide](https://datacenterhawk.com/resources/fundamentals/colocation-data-center-pricing-a-2026-beginner-s-guide)
- [Build: hyperscale lease terms 2026](https://build.inc/insights/hyperscale-data-center-lease-terms-2026)
- [Facility Grid: approach to AI](https://facilitygrid.com/our-approach-to-ai/)
- [CxPlanner: commissioning AI agents](https://cxplanner.com/commissioning-101/commissioning-ai-agents)
- [CxPlanner: CxAI across commissioning levels](https://cxplanner.com/blog/how-cxai-redefines-data-center-commissioning-across-levels)
- [Facility Grid vs Bluerithm, CxAlloy, CxPlanner](https://facilitygrid.com/blog/best-commissioning-software-for-construction-how-facility-grid-compares-to-bluerithm-cxalloy-and-cxplanner/)
- [ArchiLabs: automate data center testing](https://archilabs.ai/posts/avoid-commissioning-issues-automate-data-center-testing)
- [Anvilfield: commissioning operations guide](https://anvilfield.com/field-guides/datacenter/datacenter-commissioning-operations-overview/)
- [Crestchic liquid-cooled load bank and VCS software](https://loadbanks.com/datacentre-600kw-liquid-cooled-load-bank/)
- [Thermon liquid load banks](https://thermon.com/products/data-center-products/liquid-load-banks/)
- [CNBC: CoreWeave data center delays](https://www.cnbc.com/2025/11/11/coreweave-stock-core-scientific-delays.html)
- [Astute Analytica: commissioning and testing services market](https://www.astuteanalytica.com/industry-report/data-center-commissioning-and-testing-services-market)
- [Dataintelo: data center commissioning market](https://dataintelo.com/report/data-center-commissioning-market)
- [iRecruit: construction cost per MW 2026](https://www.irecruit.co/insights/data-center-construction-cost-per-mw-2026-benchmarks-owners)
- [Data Center TALNT: liquid cooling specialists](https://www.datacentertalnt.com/blog/liquid-cooling-specialists-ai-data-center-builds)

VERDICT: PASS
