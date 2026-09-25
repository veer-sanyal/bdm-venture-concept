The claims check out, and the market is bigger than the pitch says. The concept is worth backing if it is narrowed: to AI-built liquid-cooled halls owned by developers and neoclouds, sold to the owner rather than the general contractor, with a schedule guarantee on top of the fixed fee.

## Claims against primary sources

- **Construction spend: understated.** $50.7B for April 2026 is what Census first reported. Census's own private-construction table (`privsa.xlsx`, released September 1, 2026) now shows April revised to $61.9B. July 2026 is $75.2B at an annual rate, up 6.2% on the month and **57.2% on the year** (July 2025 was $47.8B). Without data centers, nonresidential construction is shrinking.
- **About $200,000 per MW per month: the top of the range.** CBRE's average asking rate in H2 2025 was $196.25/kW/month for 250–500 kW deals. Deals of 10 MW and up ask about $160–185/kW. So a month's slip on a 100 MW hall costs roughly $16–20M in rent.
- **Commissioning agents are scarce: supported, but not extreme.** Per Data Center Frontier, Uptime's 2026 survey found more than half of operators struggle to fill roles, and liquid-cooling expertise is the tightest skill. But posted pay is ordinary: Oracle offers $88–141k for a senior data center commissioning engineer and Prime Data Centers $120–170k. That points to a shortage of experienced people, not a wage crisis.
- **The fee pool.** Commissioning usually costs 0.5–2% of construction (CxPlanner; secondary sources say 1–4%). On about $75B a year, that is roughly **$0.4–1.5B a year of US commissioning spend**, growing about 50%.

## Who else serves this customer

- **Commissioning software:** CxPlanner already writes IST scripts from a pasted sequence of operations. Facility Grid has an AI checklist builder and CxAlloy (owned by Trinity Consultants) and BlueRithm are established. None of them claims to read BMS or power-monitoring data live and grade each step, which is this concept's core.
- **Commissioning services are consolidating:**
  - Salute bought T5 Operations and now manages 15 GW or more. It runs a direct-to-chip liquid-cooling commissioning service with Applied Digital, Compass and SDC as customers.
  - Limbach bought CYMCOR, a commissioning-oversight firm, for $30M. That is about $12M revenue and $4M EBITDA expected in 2027, a services-firm multiple.
- **Load banks:** Aggreko rents liquid-cooled load banks and sells project-specific test programs.
- **No near-identical AI-native commissioning startup turned up.** Applied Kinetics (YC Fall 2026) does supplier chasing, not testing.

**Does an incumbent own the data or the channel?** No single one does. The data sits in each project's BMS and power-monitoring systems and reaches you through the contractor. The channel is owners' approved-vendor lists and relationships, which is a real barrier at the hyperscalers and much weaker at developers and neoclouds.

## 1. Strongest version

- **Customer:** developers and neoclouds building leased, liquid-cooled AI halls (the Applied Digital, Crusoe and Galaxy type), whose lease start depends on handover.
- **Scope:** Level 4 and Level 5 commissioning of the liquid systems: flush, fill, fluid quality, coolant distribution unit tests, and the integrated test with liquid load banks. By one secondary source, the integrated test alone stretches from 4–6 weeks to 10–14 weeks for liquid-cooled halls.
- **Buyer:** the owner. Selling to the general contractor clashes with the norm that the commissioning agent is independent of the builder.
- **Price:** a fixed fee per MW, with a bonus or penalty tied to integrated-test duration. The pitch is days of rent saved, not cheaper labor.
- **Fallback:** license the grading engine to capacity-constrained incumbents such as Salute.

## 2. Scores

| | Score | Evidence |
|---|---|---|
| Customer need | 4 | Each month of delay forfeits about $160–200k per MW in rent, and liquid halls roughly double integrated-test time. |
| Value over today | 3 | Script writing is already sold (CxPlanner). The new part is live grading, and it is unproven that it reduces senior witness hours, which are tied to physical presence. |
| Market size | 3 | About $0.4–1.5B a year of US commissioning spend on a $75B base growing 57%, so it is venture-scale only at meaningful share. |
| Risk (5 = low) | 2 | Sign-off liability, approved-vendor lists, services-level margins (CYMCOR sold at about 7.5x EBITDA), AI-capex cyclicality, and incumbents can buy the same AI tooling. |

## 3. What kills it, and the fastest test

**What kills it:** two things together. Owners won't let a new firm sign off on a $1–2B hall. And the software doesn't actually reduce senior witness time or test days, because the real bottlenecks are people standing in the rooms during tests and trades fixing deficiencies, not paperwork.

**Fastest test:** get one completed liquid-hall Level 4/5 package (scripts, test logs, BMS and power trend data, the human agent's pass/fail sheets) from a developer or commissioning agent. Replay it through the grader within two weeks. Measure how often it agrees with the human pass/fail calls and how many senior-agent hours it would have removed. In parallel, offer 10 developer commissioning leads a fixed per-MW price with a schedule guarantee on their next hall. It dies if fewer than 2 agree to a paid pilot, or if the replay saves less than about 40% of senior hours.

Competition is not the problem: the services market is fragmented, and the incumbents bill hourly, so a faster method cuts their revenue. The market is growing faster than the pitch claims. The need is real, and nobody sells the core capability (live grading).

Sources:
- [Census private construction table](https://www.census.gov/construction/c30/xlsx/privsa.xlsx)
- [Census July 2026 release](https://www.census.gov/construction/c30/pdf/release.pdf)
- [Electrical Marketing, April figure](https://www.electricalmarketing.com/economic-data/construction-industry/article/55383786/data-centers-still-sizzling-with-a-287-april-yoy-spending-increase-to-507-billion)
- [CBRE pricing](https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025)
- [Limbach CYMCOR 8-K](https://www.sec.gov/Archives/edgar/data/0001606163/000162828026052611/ex992-cymcorpprfinal8426.htm)
- [Data Center Frontier, services landscape](https://www.datacenterfrontier.com/hyperscale/article/55403740/ai-infrastructure-is-redrawing-the-data-center-services-landscape)
- [Salute liquid-cooling service](https://salute.com/resources/news/salute-launches-groundbreaking-direct-to-chip-liquid-cooling-operations-service-for-ai-hpc-data-centers-at-nvidia-gtc/)
- [CxPlanner integrated test page](https://cxplanner.com/commissioning-101/integrated-system-testing)
- [CxPlanner AI engine](https://cxplanner.com/ai-engine-for-cx-teams)
- [CxPlanner commissioning cost](https://cxplanner.com/commissioning-101/what-does-commissioning-cost)
- [DCD on Facility Grid](https://www.datacenterdynamics.com/en/dcd-broadcasts/dcddata-center-construction/dcdefficient-and-reliable-construction-methods/tech-showcase-how-ai-can-streamline-commissioning-for-mission-critical-facilities/)
- [Aggreko liquid-cooled load banks](https://www.datacenterdynamics.com/en/news/aggreko-expands-liquid-cooled-load-bank-fleet-by-120mw-in-response-to-rising-ai-demand/)
- [Archdesk on integrated-test duration](https://archdesk.com/blog/ai-data-center-costs)

VERDICT: BACK
