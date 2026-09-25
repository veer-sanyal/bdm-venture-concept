I followed your instruction and read no local project files, including the METHOD.md and STATE.md that AGENTS.md points to. The session ran out of web searches partway through, so two things are unchecked: whether equipment makers (Siemens Energy, Hitachi Energy, Eaton) offer buyers their own order-tracking portals, and how the big cloud companies' own equipment-buying programs are set up.

## The claims hold up
- **Lead times are real and long.** Large power transformers took about 128 weeks to arrive in Q2 2025, and generator step-up transformers about 144 weeks (Wood Mackenzie, reported by POWER). Wood Mackenzie also estimates US supply fell 30% short of demand for power transformers in 2025, with shortages lasting "well into the 2030s". Switchgear is running 40 to 65 weeks. The only two 2026 figures I found were in a DOE lab report ("up to four years", which I saw only second-hand) and a vendor blog (about 160 weeks for substation transformers). Neither was checked against the source.
- **The follow-up work is a real paid job.** Kiewit, a large contractor, posted "Project Expeditor – Power Market" roles in Houston two days ago at $64k to $90k a year.
- **A counterpoint.** A broker quoted by POWER argues the bottleneck is partly how utilities and contractors run procurement (approval rules, vendor lists, internal hierarchy), not only factory output. That helps the pitch on process, but it also means an agent cannot make a factory build faster.

## The same company already exists
**Applied Kinetics** (appliedkinetics.ai, YC Fall 2026) has almost this exact pitch: agents that "chase suppliers, reconcile engineering changes, and track milestones", connect to SAP, Oracle, NetSuite, Outlook, Excel and SharePoint, and live in Teams and Slack. It targets equipment makers, power and energy teams, and data centers. Per YC it was founded in 2026 with two founders (ex-Crusoe and ex-IBM agents), and shows no customers or pricing. I treated it as this team.

## Who else serves this customer
- **General AI procurement agents:** Didero ($30M Series A in Feb 2026, about $37M raised in total, Microsoft's fund M12 invested), plus Lumari (YC, explicitly "expedite purchase orders"), Leverage, Procure AI ($13M) and Lio ($30M). They serve manufacturers and distributors, and none shows energy or data-center customers.
- **Close neighbours:**
  - Build (build.inc) tracks equipment risk for data-center developers mostly before orders are placed.
  - Gigawatt sells an AI procurement suite to utilities, but the chasing stays with the utility's staff.
  - Hexagon Smart Materials has an expediting module that large contractors use.
  - Oracle Aconex and Unifier handle documents and changes.
  - SAP's new Joule agents (Sapphire, May 2026) have nothing aimed at supplier order confirmations or delivery chasing.

**Does an incumbent own the data or the buying channel?** Partly. The ERP owns the purchase-order record, and at large contractors Hexagon or Aconex owns the documents and expediting records. Nobody owns the email-and-drawing follow-up layer, which still sits with people and spreadsheets. The main channel risk is that SAP or Hexagon adds an agent, not that one already exists.

## 1. Strongest version
An AI expediting desk for **owner-furnished electrical equipment** (the transformers, switchgear and similar gear the owner buys and hands to the contractor) on data-center and substation programs.
- **Buyers:** data-center developers, power producers and power contractors. Sell on schedule risk, priced per program, rather than on saving expeditor hours. Contractors on cost-plus contracts pass expediting cost through to the owner, so labour savings alone sell weakly.
- **Wedge:** the loop that general agents handle badly:
  - equipment makers' approval drawings against the latest engineering revisions;
  - release for manufacture;
  - factory test dates;
  - delivery dates tied back to the project schedule (Primavera P6).
- This is low-volume, high-value, engineering-heavy work, unlike the high-volume direct-materials ordering the general agents target.
- **Expansion:** later, the same layer for all custom-built capital equipment (LNG, chip fabs, mining).

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Lead times of 128 to 144 weeks, and Kiewit is hiring power-market expeditors now. |
| Value over what they use today | 3 | Today it's expeditors, spreadsheets and Hexagon/Aconex. Agents catch slips and missed revisions sooner but can't shorten factory lead time. |
| Market size | 3 | A few hundred US accounts (contractors, developers, utilities) at roughly $100–250k a year each gives several hundred million to about $1B. That is my estimate. Other capital-equipment sectors would widen it. |
| Risk (5 = low) | 2 | Well-funded general agents (Didero, Lumari) could add an energy offering, customers may refuse to let agents write to SAP or email suppliers, utility sales cycles are slow, and urgency fades if the shortage eases. |

## 3. What would kill it, and the fastest test
**Killers:**
- Customers learn about slips late but can't act on them anyway, so a tracker is "nice to have".
- IT won't let agents send emails to suppliers or update ERP records, which reduces the product to a dashboard.

**Fastest test (about 2 weeks):** ask 10 procurement leads at power contractors and data-center developers for three things:
1. One live project's long-lead equipment list.
2. 90 days of supplier email from that project.
3. A paid shadow pilot on it.

Run the agent over the old emails and count the schedule-affecting events (slipped dates, drawings not updated to the latest revision) it would have caught, and how many days earlier. Kill the idea if fewer than 3 of the 10 grant access and agree to pay, or if early detection averages under about a week.

VERDICT: BACK

Sources:
- [Wood Mackenzie deficit release](https://www.woodmac.com/press-releases/power-transformers-and-distribution-transformers-will-face-supply-deficits-of-30-and-10-in-2025/)
- [POWER: Transformers in 2026](https://www.powermag.com/transformers-in-2026-shortage-scramble-or-self-inflicted-crisis/)
- [Build: DC transformer procurement](https://build.inc/insights/data-center-transformer-procurement-2026)
- [Applied Kinetics](https://appliedkinetics.ai/)
- [YC: Applied Kinetics](https://www.ycombinator.com/companies/applied-kinetics)
- [TechCrunch: Didero $30M](https://techcrunch.com/2026/02/12/didero-lands-30m-to-put-manufacturing-procurement-on-agentic-autopilot/)
- [YC supply chain companies (Lumari)](https://www.ycombinator.com/companies/industry/supply-chain)
- [Procure AI seed](https://www.procure.ai/blog/seed-funding-announcement)
- [Lio Series A](https://techcrunch.com/2026/03/05/lio-ai-series-a-a16z-30m-raise-automate-enterprise-procurement/)
- [Leverage AI](https://tryleverage.ai/ai-agents)
- [SAP Sapphire 2026 spend management](https://news.sap.com/2026/05/enabling-autonomous-spend-management-ai-connected-processes/)
- [Hexagon procurement](https://aliresources.hexagon.com/procurement)
- [Gigawatt utilities](https://gigawatt.ai/blog/ai-for-supply-chain-management-in-utilities/)
- [Oracle Aconex](https://www.oracle.com/construction-engineering/aconex/)
- [Kiewit Project Expeditor listing](https://to.indeed.com/aa7nkwlxrl8m)
