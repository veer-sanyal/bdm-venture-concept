I built two companies, not three. The first is an AI-run commissioning service for new AI data centers. The second is a warranty-claims agent for heavy-truck dealers. Neither clearly clears the bar of 10.93. The commissioning company has the bigger market, but four software products already do much of the testing work. The warranty company has the cleaner advantage over today's options, but its market is small. This is all desk research, not customer validation.

## 1. AI-native commissioning for liquid-cooled AI data halls (strongest)

- **Customer.** Data center developers and the general contractors building for them, starting with liquid-cooled AI halls. These buyers pay for capacity and speed, not software. Commissioning firms bill by the hour and have little reason to buy a tool that cuts their hours.
- **Product.** A commissioning service run with AI, where a senior commissioning agent signs off and technicians do the field work:
  - it writes each test script from the project's own submittals, drawings and control sequences
  - during each test, it reads the building-management and power-monitoring data and grades every step against the pass criteria
  - it drafts the issue log and the reports
  - the goal is for one senior agent to cover several times the megawatts
- **Why now:**
  - US data center construction ran at a $50.7B annual rate in April 2026, up 27% in a year (Census, via Bloomberg).
  - A finished hall leases for about $196 per kW per month, roughly $200k per MW per month (CBRE). Every week of delay costs the owner real money.
  - A software vendor's blog says the full integrated test takes 10–14 weeks for a liquid-cooled hall, against 4–6 for an air-cooled one. That is a weak source.
- **Correction to generator 3: the software gap is gone.**
  - CxAlloy (owned by Trinity Consultants) added OTTO: automated functional testing and AI anomaly detection.
  - Facility Grid bought PingCx in August 2026. It runs functional tests on its own through the building automation system and claims commissioning time is cut in half.
  - Bluerithm ships IST scripts and an MCP server for AI agents. CxPlanner's CxAI generates test scripts from specs and datasheets.
  - Selling this as software would mean competing head-on with all four. That is why I made it a service. The open position is a firm paid a fixed fee per megawatt, whose AI does the script writing and data review so its senior agents only witness and sign.
- **Price and market.** Commissioning costs about 0.5–2% of construction (CxPlanner). That gives roughly $250M–$1B a year for US data centers alone, and about $80–120k per MW at $8–12M per MW. Analyst estimates put global data center commissioning at $2.2–5.2B in 2025; those sources are weak. It can grow into chip, pharma and battery plant validation, then monitoring buildings after handover.
- **Main risks:**
  - The team needs a senior commissioning agent or engineer and liability insurance.
  - Owners keep preferred-vendor lists.
  - Project data sits behind NDAs.
  - Existing firms can adopt the same tools; our edge is the pricing model, speed and liquid-cooling focus.
  - Demand is tied to the data center cycle.
- **Fastest test:**
  - Get one closed-out hall's commissioning package: scripts, trend data exports, issue log and hours.
  - Regenerate the scripts from its submittals and re-grade the recorded data.
  - Kill it if we miss more than 20% of the logged issues, or senior review hours don't fall at least 40%.
  - In parallel, call 10 developer construction leads. Ask what a week of handover is worth and whether they would add a new provider paid per MW.
- **Draft blind paragraph (about 130 words):** "US data center construction hit a $50.7 billion annual rate in April 2026, up 27% in a year, and a finished hall leases for roughly $200,000 per megawatt per month once handed over. Before handover, every power and cooling system must pass commissioning, ending in an integrated test that cuts utility power under full load, and experienced commissioning agents are scarce. We run commissioning as an AI-native service for data center developers and their general contractors, starting with liquid-cooled AI halls. Our software writes test scripts from the drawings, submittals and control sequences, reads building and power-monitoring data during each test to grade it against acceptance criteria, and drafts issue logs and reports, so each senior agent covers more megawatts. We charge a fixed fee per megawatt commissioned."

## 2. Warranty-claims agent for heavy-truck dealers, then equipment dealers

- **Why trucks rather than farm equipment first.** NADA's ATD 2025 profile (primary data) shows:
  - franchised truck dealers billed $5.41B of warranty work: $2.51B labor and $2.90B parts
  - warranty rose from 9.5% to 10.2% to 11.3% of service and parts sales over three years
  - the average warranty repair order is $13,816, against $8,035 for customer-pay
  - there are 42,366 technicians
  - one repair can mean separate claims to the truck maker and the engine, transmission and axle makers; Eaton alone publishes a different filing procedure for each truck maker.
- **Product.** The agent reads the repair order, technician notes, fault-code snapshots and photos. It writes each claim to that maker's rules and checks it before submission. A clerk clicks submit. It then tracks payment and drafts appeals of cuts and charge-backs.
- **Answer to the loop 1 kill (DMS vendors already file claims).** Dealer software sends claims; it doesn't write or defend them. In car dealers, WarrCloud raised $40M on top of the incumbent dealer software and signed a data-sharing deal with Toyota in September 2026. That suggests makers will work with a dealer-side vendor. The unfiled backlog is only the pilot hook; the business is the ongoing flow of claims.
- **Competitors:**
  - Pencilwrench (StoneEagle) writes repair descriptions for Freightliner, Kenworth and Peterbilt; this is the closest.
  - WarrantyWriter writes claim text.
  - Kebra (YC S26) recovers warranty revenue for field-service companies.
  - Outsourced claim processors, and Warranty Consulting Services for farm-equipment dealers.
  - Armatus already files retail-rate reimbursement claims for truck dealers in Pennsylvania.
  - Makers are adopting AI to review claims: Circuitry.ai, Tavant, Annata, ServiceCPQ.
- **Market is the weak spot.** I estimate about 1% of warranty collected, around $26k per dealership a year. That comes to about $55M for truck dealers, and perhaps $150–200M after adding equipment, RV and marine dealers. Judges will likely score market a 2 or lower.
  - One expansion: construction-equipment dealers in South Dakota say they are paid "60% or less" of their retail rate on warranty work and are lobbying to be covered by the state law that protects farm dealers.
- **Fastest test.** Get three Indiana truck dealers to pull 90 days of warranty claims with outcomes. Measure the dollars cut, denied or charged back as a share of what was submitted, and clerk minutes per claim. Ask each maker's rep whether a third party may prepare claims. Kill it if losses are under 2% and clerks aren't backed up.
- **Draft blind paragraph:** "Franchised medium- and heavy-duty truck dealers in the US billed $5.4 billion of warranty work in 2025, about $13,800 per warranty repair order. To get paid, a dealer files with the truck maker and often separately with the engine, transmission and axle makers, each with its own portal, labor-time codes and evidence rules. Claims are cut or charged back for thin documentation even when the repair was right, and manufacturers are adopting AI to review them. We sell to truck dealer groups, then farm and construction equipment dealers. Our agent reads the repair order, technician notes, fault-code snapshots and photos, writes each claim to that maker's rules, flags missing evidence before submission, queues it for the clerk to submit, tracks payment and drafts appeals. Dealers pay about 1% of warranty dollars collected."

## Dropped
- **Fleet-side warranty recovery** (a reshape I tried): Fleetio's AI Service Advisor, Motive and Nordoon already do it.
- **Proof of metal origin:** Assent, Z2Data, Flexport and Gaia are there, and the rules changed in April, June and July 2026.
- **AI quality engineer (PPAP and 8D reports):** the space is crowded, and outsourced PPAP services were an earlier kill.
- **Supplier compliance desk:** low urgency, and buyer-side platforms give suppliers free portals.
- **Pesticide compliance, cost segregation, sales-tax recovery:** kept dropped for the generators' own reasons.

## Corrections to the merged file (keep these out of any pitch)
- "CxAlloy advertises no AI" is out of date. It added OTTO.
- "3.5 months to hire a commissioning agent" comes from an uncited table on Introl's blog.
- A search snippet said dealers face an audit if warranty exceeds 2% of machine sales. The page it cited doesn't contain that.
- I found no measured rejection rate for truck or equipment dealers.
- The longer emissions warranty in EPA's 2027 truck rule is proposed for rollback. Don't use it as a reason why now.

I wrote no files. Per METHOD.md, the orchestrator saves this report.

Sources:
- [ATD 2025 financial profile (NADA)](https://www.nada.org/media/5008/download)
- [Warranty Week, 2025 truck and equipment claims](https://www.warrantyweek.com/archive/ww20260521.html)
- [Facility Grid acquires PingCx](https://facilitygrid.com/blog/facility-grid-acquires-pingcx-and-launches-unified-building-lifecycle-platform/)
- [PingCx](https://www.pingcx.com/)
- [CxPlanner AI engine](https://cxplanner.com/ai-engine-for-cx-teams)
- [CxPlanner on commissioning cost](https://cxplanner.com/commissioning-101/what-does-commissioning-cost)
- [Bluerithm for data centers](https://bluerithm.com/industry/data-center-commissioning-software/)
- [CxAlloy](https://www.cxalloy.com/commissioning-project-management/)
- [Data center construction spending (Bloomberg)](https://www.bloomberg.com/news/articles/2026-06-01/us-construction-spending-on-data-centers-eclipses-50-billion)
- [CBRE North America data center trends H1 2026](https://www.cbre.com/insights/books/north-america-data-center-trends-h1-2026)
- [Archdesk on AI data center construction](https://archdesk.com/blog/global-ai-data-center-construction-2026)
- [Astute Analytica market estimate](https://www.astuteanalytica.com/industry-report/data-center-commissioning-and-testing-services-market)
- [Introl workforce shortage](https://introl.com/blog/data-center-workforce-shortage-340000-unfilled-positions-2026)
- [Pencilwrench](https://www.pencilwrench.com/)
- [Kebra](https://www.ycombinator.com/companies/kebra)
- [WarrCloud and Toyota data sharing](https://www.cbtnews.com/warrcloud-announces-data-sharing-with-toyota)
- [Armatus Dealer Uplift](https://www.dealeruplift.com/retail-warranty-reimbursement/)
- [South Dakota construction-equipment warranty testimony](https://citizenportal.ai/articles/7972875/south-dakota/2026-legislature-sd/dealers-press-lawmakers-to-strip-construction-equipment-exception-from-warranty-law-manufacturers-warn-of-legal-cost-risks)
- [Fleetio AI Service Advisor](https://www.automotive-fleet.com/news/fleetio-launches-service-advisor-ai-to-streamline-repair-approvals)
- [Nordoon](https://www.nordoon.ai/customer-stories/automated-warranty-recovery-fleet-maintenance-ai-agents)
- [Foley on Section 232 changes](https://www.foley.com/insights/publications/2026/05/what-every-multinational-should-know-about-the-new-rules-for-section-232-tariffs-on-steel-aluminum-and-copper-derivatives/)
- [EPA truck emissions warranty proposal (TT)](https://www.ttnews.com/articles/epa-trucks-emissions-warranty)
- [Eaton claim procedures by truck maker](https://www.eaton.com/us/en-us/support/warranty-returns/eaton-commercial-vehicle-warranty/dealer-warranty/freightliner-warranty-claims.html)
