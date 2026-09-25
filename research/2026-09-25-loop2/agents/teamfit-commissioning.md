I can't recommend this as a two-undergrad company unless a credentialed senior commissioning agent joins as a partner. The service is only worth buying because of that person's signature, and neither founder can earn one in years, let alone a semester. What they can do this semester: recruit that partner, build the live grader on real test data, and answer the two main risks directly with customers. This is all desk research, not customer validation.

## What they need

**1. Credentials: they have to borrow them.**
- **The certification is out of reach.** ACG's Certified Commissioning Authority requires a PE or architect license, 3 years of commissioning experience and at least 3 projects. ACG also checks that the applicant's employer is an independent commissioning firm.
- **So is the entry-level one.** ACG's Commissioning Specialist needs 2 years of relevant experience plus 6 months at an ACG member firm under a certified agent.
- **The partner.** They need a PE and certified commissioning agent who has run full-load integrated tests on data centers. That person should be a co-founder with equity and a per-project fee, not an advisor. Without that signature there is nothing to sell.
- **Independence has a cost.** It rules out general contractors as customers, even though the original pitch named them. The firm contracts only with owners.
- **Insurance.** Owners will almost certainly require professional liability insurance. I couldn't find standard coverage limits.
- **Site safety training they can do this term.** OSHA 30 and NFPA 70E electrical-safety training, so the founders can be on site as technicians or observers.

**2. Skills (one founder on each).**
- **Building systems:** direct-to-chip liquid cooling (the two loops of a coolant distribution unit, supply temperature, flow, pressure, leak detection) and the power chain (UPS, transfer switches, generators). A Purdue mechanical or electrical engineering student would do. If both founders are software people, they need a faculty or grad-student advisor.
- **Data plumbing:**
  - Reading the standard building-control protocols (BACnet, Modbus, SNMP) and exported trend logs.
  - Reading the power-monitoring system's event logs and the load-bank vendor's logs.
  - Lining all of them up on one clock. Power-monitoring events are recorded to the millisecond, but building-system trends log every few seconds to a minute, so that alignment is the actual hard problem. This is my own engineering judgment, not a sourced claim.
  - Turning written control sequences and acceptance criteria into rules a computer can check.

**3. Access to real test data, before any customer.** The grader has to be trained and checked on real test scripts and raw data. Options:
- The senior partner's past projects, redacted.
- Purdue's research computing center, which has run direct-to-chip liquid cooling since 2009.
- Purdue's Cooling Technologies Research Center, an NSF industry-university center whose research agenda is set by its industry members.
- Aggreko. It rents 500 kW liquid-cooled load banks with built-in flow meters and runs remote monitoring and its own testing software. That makes it both the best source of load data and a possible competitor, since it already offers test plans and test documentation.

**4. First customers.** The judges' segment is real and building now:
- **TeraWulf, Lake Mariner:** told investors in its Q2 2026 call that building CB4 is in commissioning, with CB5 energizing in very early January.
- **Galaxy, Helios:** Phase I delivered 133 MW to CoreWeave on schedule.
- **IREN:** Microsoft has accepted IREN's Horizon 1.
- **Applied Digital, Ellendale:** leases to CoreWeave.

The catch: on these conversion sites the **tenant** (Microsoft, CoreWeave) decides whether the hall is accepted. So the gating question is whether the tenant will accept a report signed by an agent at a new firm, not just the owner.

In Indiana, Meta's $10B, 1 GW Lebanon campus (Turner is the general contractor, first capacity late 2027 to 2028) is useful for alumni contacts. It is not a first customer, because hyperscalers run their own commissioning programs.

## How to get it this semester (about 11 weeks)

| When | What |
|---|---|
| **By about Oct 9** | Recruitment push for the senior partner through the 7x24 Exchange Midwest, Chicagoland and Ohio chapters, and Purdue engineering and construction-management alumni with mission-critical commissioning titles. Start OSHA 30. |
| **Oct 21–28** | Two conferences: the Building Commissioning Association (Vancouver, Oct 21–23) and 7x24 Exchange Fall (San Antonio, Oct 25–28, themed on AI data centers, about 1,300 attendees). Apply for student passes or scholarships; some 7x24 chapters fund students. Goal: recruit the partner and book owner calls. |
| **Oct–Nov** | 15–20 calls with the construction or commissioning leads at neoclouds, miners and second-tier colocation developers. Ask three things: (a) on your last hall, how many days passed between the start of the integrated test and a signed report or tenant acceptance, and what caused the slippage; (b) would your tenant accept a signature from a new firm's certified agent; (c) what do you pay per MW for the last two test levels. |
| **Oct–Nov** | Build the grader on 2–3 real redacted test datasets. Measure how often it agrees with the human-graded report and the hours it saves. |
| **Nov–Dec** | One free shadow pilot: during an owner's real test, run alongside their existing agent and deliver a graded report within 24 hours. Aim to leave with a letter of intent for a paid per-MW pilot. |
| **Funding** | Purdue's new HIVE center, the $5K two-semester venture program, and the Purdue Innovates Accelerator (applications close Dec 20, 2026). |

## Two cautions

- **The paperwork-is-the-bottleneck risk is real.** Published surveys blame handover delays mostly on equipment lead times (switchgear at 45–80 weeks, transformers over 120). A claim that integrated testing on liquid-cooled halls takes 10–14 weeks comes from a vendor's own modeling, not independent data. Call question (a) settles this.
- **Kill point.** If no qualified agent commits by the end of October, change the pitch: sell the live grader as software to existing independent commissioning firms. That drops the sign-off risk but competes more directly with Facility Grid and CxPlanner.

Sources:
- [ACG Certified Commissioning Authority requirements (O*NET)](https://www.onetonline.org/link/certinfo/11013-B)
- [Apply for CxA certification (ACG)](https://www.commissioning.org/applyingforcxacertification/)
- [ACG Certified Commissioning Specialist](https://www.commissioning.org/certified-commissioning-specialist/)
- [Aggreko 500 kW liquid-cooled load bank](https://www.aggreko.com/en-us/news/aggreko-expands-data-center-testing-solutions-in-north-america-with-500-kw-liquid-cooled-load-bank)
- [Aggreko data center commissioning services](https://www.aggreko.com/en-us/sectors/data-centres/data-centre-commissioning)
- [Purdue RCAC on direct-to-chip liquid cooling](https://rcac.purdue.edu/news/6967)
- [Purdue ME on data center cooling research (CTRC)](https://engineering.purdue.edu/ME/News/2023/from-micro-to-macro-cooling-data-centers-from-the-inside-out)
- [Meta Lebanon, Indiana campus (Indiana Capital Chronicle)](https://indianacapitalchronicle.com/2026/02/11/details-on-long-expected-meta-data-center-campus-unveiled/)
- [Indiana data center tracker](https://ailawtracker.org/data-centers)
- [TeraWulf, Cipher and IREN 2026 update (24/7 Wall St.)](https://247wallst.com/investing/2026/07/30/terawulf-and-cipher-digital-are-up-50-in-2026-while-iren-lags-behind-is-it-time-to-buy-iren-for-a-catch-up-trade/)
- [IREN: Microsoft accepts Horizon 1 (24/7 Wall St.)](https://247wallst.com/investing/2026/08/21/iren-jumps-6-but-then-gives-up-gains-as-microsoft-accepts-horizon-1-terawulf-ticks-up-cipher-digital-drops-5/)
- [Galaxy Helios Phase I delivered to CoreWeave](https://www.prnewswire.com/news-releases/galaxy-completes-phase-i-of-its-helios-data-center-campus-delivering-133-megawatts-of-critical-it-load-to-coreweave-302818664.html)
- [Applied Digital and CoreWeave leases (JSA)](https://www.jsa.net/applied-digital-secures-7b-in-landmark-15-year-ai-infrastructure-leases-with-coreweave/)
- [Archdesk: AI data center construction and delays](https://archdesk.com/blog/global-ai-data-center-construction-2026)
- [SGS digital commissioning](https://www.sgs.com/en/news/2026/02/digital-commissioning-in-data-centers-reducing-handover-risk-through-real-time-visibility)
- [Anvilfield IST field guide](https://anvilfield.com/field-guides/datacenter/integrated-systems-test-ist-commissioning/)
- [7x24 Exchange Fall 2026 conference](https://www.datacenterfrontier.com/colocation/event/55405470/724-exchange-fall-2026-conference)
- [BCxA Annual Conference](https://www.bcxa.org/conference/)
- [7x24 Exchange chapters](https://www.7x24exchange.org/chapters/)
- [Purdue HIVE](https://engineering.purdue.edu/Engr/AboutUs/News/Features/2026/2026-0622-purdue-hive-student-entrepreneurship-center)
- [Purdue Innovates Accelerator](https://purdueinnovates.org/incubator/accelerator/)
- [CxPlanner on commissioning cost](https://cxplanner.com/commissioning-101/what-does-commissioning-cost)
