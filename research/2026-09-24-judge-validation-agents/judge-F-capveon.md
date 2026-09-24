I'd pass on this. The claims mostly check out, but the problem is already largely solved. Reading public budgets, capital plans and board minutes to find projects before they go to bid is now a feature that at least eight products sell, and the companies that own the customer's budget and buying channel already ship it.

## Checking the concept's claims

- **"The job is won before the bid, and the spec often names a competitor."** Mostly true, with one correction. The federal procurement rule that applies to projects paid for with federal money (2 CFR 200.319) treats "specifying only a brand name product" as restricting competition. It allows "brand name or equivalent" wording. In practice, specs list two or three acceptable manufacturers followed by "or equal." Being on that list is what matters, and the engineer writes it during design. [LII, 2 CFR 200.319](https://www.law.cornell.edu/cfr/text/2/200.319)
- **"12 to 18 months ahead."** Plausible. Each state runs a revolving loan fund for water projects (an SRF) and publishes an Intended Use Plan listing the projects it will fund. Rhode Island's plan only accepts projects due to start construction within two years. Connecticut asks each applicant for its expected procurement month. These are structured public sources with a long lead time. [RI SFY25 IUP](https://health.ri.gov/sites/g/files/xkgbur1006/files/publications/plans/SFY25-DWSRF-IUP.pdf), [CT DWSRF instructions](https://portal.ct.gov/dph/-/media/departments-and-agencies/dph/dph/drinking_water/pdf/2025-01-14-dwsrf-eligibility-application-instructions.pdf)
- **"The signals are buried and nobody reads them."** False. The competitors below already read them.

## Who already serves this customer

| Company | What it already does |
|---|---|
| Deltek GovWin IQ | Over 1.4 million pre-RFP opportunities taken from capital plans and budgets, plus searchable board minutes and agendas. Claims coverage of 95% of state and local spending. [Deltek](https://www.deltek.com/resources/articles/govwin-board-docs/) |
| GovSpend Meeting Intelligence | Uses AI to transcribe public meetings at thousands of agencies, with keyword alerts. [GovSpend](https://govspend.com/meeting-intelligence/) |
| Starbridge | Monitors minutes, budgets and plans across 320,000+ agencies. Raised $52M, including a $42M Series A led by Craft Ventures in October 2025. Used by 160+ enterprise sales teams. [TechCrunch](https://techcrunch.com/2025/10/22/david-sacks-craft-leads-42-million-series-a-in-govtech-startup-starbridge/) |
| Dodge Construction Network | Leads at the planning stage, 400+ field staff, and SpecShare, which shows manufacturers which projects' specs name them or their competitors. [Dodge](https://www.construction.com/find-projects-first/), [SpecShare](https://www.construction.com/specshare/) |
| ConstructConnect | 825,000+ projects tracked from concept onward, with keyword search inside specs. Pitched directly to product manufacturers. [ConstructConnect](https://www.constructconnect.com/blog/how-can-building-product-manufacturers-find-early-stage-construction-projects) |
| Bluefield Research | Line items for about 34,000 capital projects from 725 water utilities' capital plans, covering 2025 to 2036. Sold as a corporate subscription. [Bluefield](https://www.bluefieldresearch.com/data/utility-capital-improvement-plan-2/) |
| FirmoGraphs / Water AI | Water only. Uses AI to track utility capital plans, SRF programs and funding, and sells to suppliers. [Water AI](https://water-ai.us/), [FirmoGraphs](https://www.firmographs.com/focus-industries/water) |
| CityMinutes.ai | Same method (planning and council minutes, 8 to 24 months early) for real estate and building products. Proof the extraction is easy to copy. [CityMinutes](https://cityminutes.ai) |

**Does an incumbent own the data or the channel?** Yes, both.
- **Budget:** Dodge, ConstructConnect and Deltek already hold the lead-data line in manufacturers' budgets.
- **Relationships:** In water, the relationship with the consulting engineer sits with independent manufacturer's reps, who are paid on commission to get their lines specified. Reps usually hear about a project when the engineer is hired, which is the same moment this product would flag it. I found job postings describing this rep role but no study measuring how early reps hear about projects. That gap is exactly what the test below checks.

## 1. The strongest version

Narrow to municipal water and wastewater process equipment: pumps, blowers, screens, UV systems, membranes, valves. This is where a spec locks in the most money per project, and the funding records are the most structured. Drop contractors, who already get bid feeds and gain little from knowing earlier. Drop roads, where Dodge and ConstructConnect are strongest.

The product tracks who writes the spec, not just which projects exist:
- **The trigger** is the board vote approving a design contract with an engineering firm, matched against the SRF funding lists. That vote is the day spec writing starts, and it names the engineer of record.
- **The alert** tells the rep firm covering that territory: the engineer, the scope, the funding source and the expected bid date.
- **The follow-up** reads the published bid specs later and records whether the manufacturer made the acceptable-manufacturers list. Over time this builds a record of which engineers name which brands, showing where each manufacturer wins and loses.
- **The buyer** is the manufacturer's regional sales leader, priced per territory and product line, and pushed down to its rep firms.

## 2. Ratings for that version

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | The need is real and people pay for it: Dodge built SpecShare and keeps 400+ field staff, and Starbridge raised $52M on the same early-signal idea. |
| Value over what customers use today | 2 | Deltek already sells 1.4M pre-RFP items from capital plans plus board minutes, and Bluefield sells line items for 725 utilities. The only new pieces are the engineer-of-record link and the spec follow-up, and SpecShare already does the follow-up for building products. |
| Market size | 2 | WEFTEC 2025, the main US water trade show, had 1,173 exhibitors ([ExpoGPS](https://www.expogps.com/trade-shows/weftec-2025-af89ac19)). At $15k to $25k a year, water alone tops out around $20M to $30M ARR. Widening to roads and utilities walks into Dodge's strongest ground. The $625B 20-year need figure ([EPA 7th DWINSA](https://www.epa.gov/system/files/documents/2023-04/Final_DWINSA%20Public%20Factsheet%204.4.23.pdf)) is what utilities spend, not what this product can earn. |
| Risk (5 = low) | 2 | Incumbents already hold the budget line and the data. Using AI to read the documents gives no moat, as CityMinutes and FirmoGraphs show. The reps are a middle layer that may already know about the projects. |

## 3. What kills it, and the fastest test

**What kills it:** reps and regional managers already hear about nearly every project when the engineer is hired, through their relationships and the feeds they already have. If so, the early alerts are not new information, and the business shrinks to a slightly better version of GovWin.

**The fastest test takes about a week and needs no software.**
1. Pick one state and assemble by hand, from board minutes and the SRF funding list, every water or wastewater design contract awarded in the last six months. Expect 30 to 60 projects.
2. Show the list to five rep firms and two regional sales managers at manufacturers covering that state.
3. Ask two questions: which ones were you already tracking, and on which ones do you not yet know the engineer of record?

If they already knew about more than 80%, pass for good. If they missed a third or more, mostly at small and mid-size utilities, the engineer-of-record version has a real opening, and the next question is whether they would pay per territory.

VERDICT: PASS
