## Venture assessment: AI-run commissioning for data centers

I checked the pitch's claims, looked for rivals, and scored the strongest version I could build. My verdict is pass: the market is real, but the company's advantage is thin and can't be proven yet.

### What the claims look like against sources

- **Construction spending:** accurate. The Census Bureau's series put US data center construction at a $50.7B annual rate in April 2026, the first month above $50B. Reports give the year-on-year rise as 27% to 28.1% ([Bloomberg](https://www.bloomberg.com/news/articles/2026-06-01/us-construction-spending-on-data-centers-eclipses-50-billion), [Electrical Marketing](https://www.electricalmarketing.com/economic-data/construction-industry/article/55383786/data-centers-still-sizzling-with-a-287-april-yoy-spending-increase-to-507-billion), [DCK](https://www.datacenterknowledge.com/build-design/data-centers-become-largest-segment-of-us-office-construction)). The Census page I could reach didn't show the data center line, so these figures come from reports of the Census release.
- **$200,000 per MW per month:** plausible but on the high side. CBRE's asking rent was $196.25 per kW per month for 250–500 kW deals in late 2025, and it expects more than $215 in 2026 ([CBRE midyear 2026](https://www.cbre.com/insights/books/us-real-estate-market-outlook-midyear-review-2026/data-centers)). Leases of 10 MW or more usually go for less, but I couldn't find a primary dollar figure for them. CBRE also reports record-low 1.4% vacancy and 7,481 MW under construction in primary markets ([CBRE H1 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026)).
- **Agent shortage:** supported, though the numbers come from industry surveys and recruiters. Uptime Institute's 2026 survey found more than half of operators struggling to hire ([DCF](https://www.datacenterfrontier.com/hyperscale/article/55403740/ai-infrastructure-is-redrawing-the-data-center-services-landscape)). A recruiter reports commissioning roles open past 120 days and pay up 16% since 2023 ([iRecruit](https://www.irecruit.co/insights/data-center-commissioning-careers-trends)).
- **"Each agent covers several times the megawatts":** doubtful. On owner-run data center projects, the owner's commissioning agent witnesses 100% of tests ([Construct & Commission](https://constructandcommission.com/level-5-data-center-commissioning-step-by-step-guide/)). AI can cut the hours spent writing scripts, reviewing data and writing reports. It can't cut the hours spent standing in the hall. My guess is 1.5 to 2 times the coverage, not "several times." That is my reasoning, not a sourced figure.

### Who already serves this customer

**Software:**
- Facility Grid (growth investment from Nexa Equity in 2025, 150+ customers including data centers) already drafts test scripts from specs with AI. It says this takes a test script from 4–8 hours per piece of equipment to under 2 minutes ([DCD showcase](https://www.datacenterdynamics.com/en/dcd-broadcasts/dcddata-center-construction/dcdefficient-and-reliable-construction-methods/tech-showcase-how-ai-can-streamline-commissioning-for-mission-critical-facilities/), [BusinessWire](https://www.businesswire.com/news/home/20250812197767/en/Facility-Grid-a-Leading-Commissioning-and-Operational-Readiness-Software-Provider-Receives-Growth-Investment-from-Nexa-Equity)).
- CxAlloy, owned by Trinity Consultants, bought OTTO in 2024. OTTO runs functional tests automatically from building-system trend data and flags anomalies with AI ([CxAlloy](https://www.cxalloy.com/cxalloy-acquires-otto/)).
- BlueRithm and CxPlanner have AI checklist tools and cover liquid-cooling test workflows ([BlueRithm](https://bluerithm.com/the-best-commissioning-software-for-data-centers/), [CxPlanner](https://cxplanner.com/blog/cx-for-liquid-cooling)).

**Service firms:**
- Bureau Veritas owns Primary Integration and agreed in April 2026 to buy Lotusworks. Lotusworks had €131M revenue and 750 staff; the price was €375M, 15 times its expected 2026 operating profit ([BV](https://group.bureauveritas.com/newsroom/bureau-veritas-acquires-lotusworks-reinforcing-its-position-in-data-centers)).
- Salute, Jacobs and Burns & McDonnell are other major commissioning providers. Limbach bought the commissioning firm CYMCOR for about $30M.

**Near-identical company:** I found none.

**Does an incumbent own the data or the buying channel?** For hyperscalers, largely yes. The service firms hold long-term framework agreements with them (Bureau Veritas describes Lotusworks's business that way). The equipment makers own the building-management and power-monitoring systems, though the project contract gives the commissioning agent access to the data. Nobody owns the newer AI builders: neoclouds such as Crusoe and bitcoin miners converting to AI, such as Applied Digital and IREN.

### 1. The strongest version

An independent commissioning agent hired by the owner, not software sold to others. It would do only the equipment-level and integrated tests (levels 4 and 5) on liquid-cooled halls for the newer AI builders, mostly in secondary markets where commissioning firms are thin.

- **The edge:** grading each step live during the integrated test, and issuing a signed report within 24 hours instead of days.
- **Pricing:** a fee per MW plus a bonus for handing over on schedule. A fee around 1% of construction cost matters much less to the buyer than a month of lost rent, about $20M on a 100 MW hall at $200k per MW per month.
- **Narrowing:** drop general contractors as buyers for this work. Being paid by the builder whose work you certify breaks the agent's independence. Contractor-side quality checks could be a separate product.
- **Long-term moat:** test data from many projects on how cooling units, chillers and UPSs behave under full load, reused for day-2 operations and warranty claims.

### 2. Ratings

These rest on desk research only. No customer has confirmed any of it.

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | Commissioning roles stay open past 120 days, over half of operators can't hire, and a late handover costs about $200k per MW per month. |
| Value over what customers use today | 2 | Facility Grid already drafts scripts in minutes and CxAlloy/OTTO already grades tests from trend data. Only live grading of the integrated test is new, and the 100% witness rule caps how far it stretches each agent. |
| Market size | 3 | Commissioning costs 0.5–2% of construction, so roughly $250M–$1B a year in the US. The Lotusworks sale shows service firms sell at 15 times operating profit. |
| Risk (5 = low) | 2 | Tenants and lenders must accept an unknown agent's signature. Growth depends on hiring the same scarce senior agents. Incumbents are adding the same AI, and data center building is cyclical. |

### 3. What would kill it, and the fastest test

**What would kill it:**
- Tenants, lenders or insurers won't accept a new agent's sign-off.
- Owners insist on full in-person witnessing, so each agent covers little more than today.
- Late handovers come from physical fixes, retests and late equipment rather than slow paperwork, so faster grading doesn't move the date.

**Fastest test (about 2 weeks):** Put a concrete offer to the construction or commissioning heads at 10 neocloud and converted-miner builders. The offer: independent level 4–5 commissioning on their next liquid-cooled hall at a fixed fee per MW, a named senior agent signing, graded integrated-test reports within 24 hours, and a bonus tied to handover. Count how many confirm their tenant and lender would accept a new agent and will sign a letter of intent, or a paid shadow run alongside their current agent on a live hall. Fewer than 2 of 10 kills it.

**What would change my mind:** a builder commits to a hall on these terms, and a shadow run shows one senior agent can really cover at least 2.5 times the megawatts with the software.

VERDICT: PASS
