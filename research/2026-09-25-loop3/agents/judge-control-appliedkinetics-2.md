I didn't read any local project files, as you asked. The web search budget ran out partway through, so a few points below come from general knowledge and are marked as unverified.

**The exact match (treated as this team):** Applied Kinetics, in YC's Fall 2026 batch, founded in 2026 with 2 people. Its pitch is nearly word for word the concept: agents that "chase suppliers, track equipment approvals and delivery dates," connected to SAP, Oracle, NetSuite, Outlook, Excel and SharePoint, and reporting in Teams or Slack. Its site shows a transformer drawing revision being pushed to a SAP purchase order line. It lists no customers.

**Claims checked against primary sources**
- **Lead times are real.** Wood Mackenzie's Q2 2025 survey puts power transformers at an average of 128 weeks and generator step-up transformers at 144 weeks. Switchgear averages 44 weeks.
- **The shortage is real.** Wood Mackenzie (August 2025) projected a 30% supply deficit for power transformers and 10% for distribution transformers in 2025. About 80% of US power transformer supply is imported.
- **Buyers now reserve factory slots before specs are final.** GE Vernova's Q1 2026 data center agreements covered 21 GW, of which only 2 GW were firm orders; the rest were reservations. A transformer broker quoted in POWER says he can deliver in 12 to 14 months "once engineering drawings were approved." So drawing approval, not just paperwork, sets the date.

**Who else serves this customer**
- **General-purpose procurement agents doing the same email-to-ERP work:**
  - Didero ($37M raised, including a $30M Series A in February 2026)
  - Lumari (YC Spring 2025; lists "Energy & Infrastructure" as a sector)
  - Traza ($2.1M seed)
  - Leverage
- **Other startups in the space, not on this job:** Build.inc ($8.5M seed) does pre-construction due diligence. Parspec ($31.5M raised) sells to electrical distributors.
- **Incumbents:**
  - SAP and Oracle hold the purchase order records. SAP's Joule agents so far cover intake, contracts and supplier onboarding, not chasing open orders.
  - Hexagon Smart Materials sells an Expediting & Inspection module to large EPC contractors.
  - Oracle Aconex and Procore hold supplier documents and submittals (from memory, not checked).
  - Third-party expediting and inspection firms do much of this work as a service (from memory, not checked).
- **Does an incumbent own the data or the buying channel?** Partly. The ERP owns the order records, and at large EPCs Hexagon and Aconex own the document and expediting workflow. No one owns the supplier email thread, which is where the work actually happens.

**1. Strongest version**
Don't sell general order chasing. Sell an owner-side desk for long-lead electrical equipment to data center developers, independent power producers and mid-size power EPCs. Leave utilities for later: they buy slowly and are locked into SAP.

The wedge is the loop that sits outside the ERP: drawing and spec revisions, approval turnaround, factory acceptance test dates, and delivery dates. Keeping that loop tight is what protects a reserved slot. Price it against schedule risk and owner's-rep fees, not against coordinator salaries.

Longer term, the moat is a cross-customer dataset of how reliably each equipment maker delivers against its promised dates. That becomes something developers and lenders would pay for.

**2. Ratings**
| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | 128 to 144 week lead times and a 30% deficit put this equipment on every project's critical path (Wood Mackenzie). |
| Value over today | 3 | Earlier warning and caught revisions help, but they don't create factory capacity. Today's spreadsheets plus coordinators plus Aconex/Hexagon mostly do the job. |
| Market size | 3 | My own estimate, not sourced: a few hundred to about 1,000 US buyer organizations with tens to hundreds of long-lead orders each, so roughly $100–300M for the core. It gets bigger only by expanding into all capital-project expediting. |
| Risk (5 = low) | 2 | Well-funded general players already do the email-to-ERP mechanics. Utilities are slow to give an agent write access to SAP. Pain eases as $1.8B+ of new transformer factory capacity comes online. |

**3. What kills it, and the fastest test**
It dies if either of these holds:
- Buyers say the constraint is factory slots, not follow-through.
- Each customer has too few long-lead orders and revisions to justify a six-figure annual contract, so a coordinator with a spreadsheet stays good enough.

Fastest test (about 2 weeks): get 10 procurement or project leads at data center developers and power EPCs to share one live project's long-lead tracker and supplier email threads. Run the agent over them. Count real date slips or revision mismatches it finds that the team hadn't logged, then ask for a paid pilot at $100k or more a year. If fewer than half the projects show a missed discrepancy, or nobody pays, stop.

**Why I pass:** The pain is real and the timing is good. But the core value is visibility over a constraint that is really factory supply, the reachable customer base is modest, and general agent companies with far more funding already do the mechanics. It would flip to BACK if the test surfaces missed revisions regularly and leads to paid pilots.

Sources:
- [Applied Kinetics site](https://appliedkinetics.ai/)
- [Applied Kinetics YC profile](https://www.ycombinator.com/companies/applied-kinetics)
- [Wood Mackenzie deficit release](https://www.woodmac.com/press-releases/power-transformers-and-distribution-transformers-will-face-supply-deficits-of-30-and-10-in-2025/)
- [POWER magazine, Transformers in 2026](https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/)
- [Global Data Center Hub, the four-year wait](https://www.globaldatacenterhub.com/p/the-four-year-wait-for-a-transformer)
- [TechCrunch on Didero](https://techcrunch.com/2026/02/12/didero-lands-30m-to-put-manufacturing-procurement-on-agentic-autopilot/)
- [Didero Series A](https://www.didero.ai/blog/series-a-announcement)
- [Lumari YC profile](https://www.ycombinator.com/companies/lumari)
- [Lumari site](https://lumari.ai/)
- [Traza funding (VentureBeat)](https://venturebeat.com/orchestration/traza-raises-usd2-1-million-led-by-base10-to-automate-procurement-workflows-with-ai)
- [Leverage AI](https://tryleverage.ai/ai-agents)
- [Build seed round (SiliconANGLE)](https://siliconangle.com/2026/06/30/build-raises-8-5m-accelerate-industrial-infrastructure-development-project-work/)
- [Parspec funding (Crunchbase News)](https://news.crunchbase.com/ai/construction-supply-chain-startup-parspec/)
- [Hexagon Smart Materials](https://aliresources.hexagon.com/procurement-fabrication-construction/intergraph-smart-materials-overview)
- [SAP Joule agents (ERP Today)](https://erp.today/sap-joule-agents-ariba-fieldglass-procurement-automation-2026/)

VERDICT: PASS
