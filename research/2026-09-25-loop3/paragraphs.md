# Loop 3 paragraphs, as given to judges (2026-09-25)

Each judge received exactly one paragraph inside the METHOD judge prompt. Judges did not know which paragraphs are YC controls.

## Controls

**C-byteask (ByteAsk).** Pricing is from byteask.ai/pricing.

> C and C++ still run trading systems, cars, chips and operating systems, and general AI coding assistants do worst there. They propose changes that look right but fail to compile, break the build, or introduce memory errors that only show up at runtime. This company makes an AI coding agent built only for C and C++. It doesn't stop at a plausible diff. It builds, debugs and tests every change with the project's real compiler, debugger and test suite until the change holds, including memory and undefined-behavior checks. It runs from the terminal or inside VS Code, Neovim and Emacs, and can run fully on-premises for companies that can't send code out. Customers are engineering teams at firms with large C and C++ codebases. Individuals pay $16 to $200 a month; companies with more than 10 people buy team or enterprise plans.

**C-appliedkinetics (Applied Kinetics).** Pricing is not published; the last sentence gives the usual model for deployed enterprise agents.

> The build-out of power grids, generation and data centers depends on long-lead equipment such as transformers and switchgear. After a purchase order is placed, project teams spend their days chasing suppliers for dates, reconciling engineering revisions against open orders, and tracking approvals across email, spreadsheets and ERP systems. A missed revision or a slipped delivery can hold up a whole project. This company deploys AI agents that do that follow-through. They read incoming emails and revised specifications, update the purchase order in SAP, Oracle or NetSuite, ask suppliers to confirm, flag drawings that need revising, and track test and delivery dates. They report results and exceptions to the team in Microsoft Teams or Slack. Customers are utilities, developers, EPC contractors and equipment buyers in energy and data centers. Revenue comes from annual contracts per deployment.

**C-agentrelay (Agent Relay).** Pricing is not published; the last sentence gives the usual model for developer infrastructure with a hosted tier.

> Software teams now run several AI coding agents at once, such as Claude Code, Codex and OpenCode, but each agent works alone in its own session. Agents can't hand work to each other, humans can't see what every agent is doing, and long jobs die when a session ends. This company provides the infrastructure to run coding agents as a team. It gives them shared messaging and channels, session history, and access to tools such as GitHub, Linear and Slack. Teams can watch every agent, run checked and resumable multi-step workflows, and step in when a human decision is needed. It runs in the company's cloud, locally, or on the customer's own hardware, and its code is public on GitHub. Customers are software teams using multiple coding agents. Revenue comes from a hosted cloud service and enterprise self-hosted licenses.

## Candidates

Every number below was checked against its source on 2026-09-25 before judging (METHOD step 4).

**K-ltcmedicaid (AI caseworker for long-term-care Medicaid applications).** From the shaper's lead company. Checks:
- **KFF, [5 key facts](https://www.kff.org/medicaid/5-key-facts-about-nursing-facilities-and-medicaid/):** "nearly 15,000" facilities and 1.2 million residents, "over 60%" of whom had Medicaid as primary payer. This is a share of residents; the generators had said "63% of homes".
- **Medicaid Planning Assistance, [retroactive coverage](https://www.medicaidplanningassistance.org/retroactive-medicaid/):** from 1 January 2027, retroactive coverage for nursing-home applicants falls from 3 months to 2.
- **Genworth/CareScout 2024:** the national median for a semi-private room is $9,277 a month.
- **AALTCI:** long-term-care insurers paid $14.1B in claims in 2023 to about 353,000 people. This is not in the paragraph.
- **Dropped, not verifiable from a primary source:** the "10- to 30-day" deadline range and the $250,000 average provider loss (an agency blog).

> When a nursing-home resident's savings run out, someone has to file a long-term-care Medicaid application: five years of bank statements, an explanation for every flagged transfer, the state form, and quick answers to each caseworker request. Homes give this to business-office staff or pay outside eligibility firms, and while a case is pending the home carries care worth about $9,300 a month (Genworth 2024 median). Medicaid is the main payer for over 60% of the 1.2 million US nursing-home residents. From January 2027, federal law cuts retroactive coverage for these applicants from three months to two, so a slow filing means care the home may never be paid for. This company is an AI caseworker. It chases families by text and voice until the records arrive, reads the statements and flags transfers, fills and times the application, drafts explanation letters, answers requests before deadlines and handles renewals. It starts with Indiana nursing homes, then home-care Medicaid, VA benefits and long-term-care insurance claims. Homes pay per approved case.

**K-supplierwarranty (warranty chargeback defense for auto suppliers).** From the shaper's fallback company. This independently regenerates the archive's previously selected concept (Supplier Quality Chargeback Defense, CONCEPT.md); the shaper did not know that. Checks:
- **Warranty Week, [2023-12-14](https://www.warrantyweek.com/archive/ww20231214.html):** US-based auto suppliers paid $468M in warranty claims in Q3 2023. Suppliers pay "roughly a tenth of the industry's warranty costs, while their share of sales revenue exceeds a third."
- **Plante Moran, 2014:** "many OEMs simplifying warranty cost and sharing as 50/50—even when it's not clear that the supplier has any responsibility." Passed-through costs include ineligible parts, excessive labor and duplicate repairs.
- **Dropped:** the shaper's "deducted before the supplier reviews it". The cited Claimlane page does not say this; it is written from the OEM's side. Also dropped: "GM recovered $2.7B over the Bolt", which was not checked.

> Automakers charge parts suppliers for warranty repairs they attribute to the supplier's parts. US-based auto suppliers paid $468 million in warranty claims in one quarter of 2023 (Warranty Week). An accounting firm that audits suppliers reports that many automakers simply split warranty costs 50/50 "even when it's not clear that the supplier has any responsibility," and that the charges can include ineligible parts, excessive labor and duplicate repairs. Disputing a charge means a supplier's quality or warranty staff must match each claim to the returned-part analysis, test data and supply agreement. This company uses AI to read every charge, match it to that evidence, flag the charges most likely to be wrong, and draft the dispute with its supporting documents. It starts with Midwest auto and RV component suppliers, then other industries where buyers charge suppliers for quality failures. Suppliers pay a share of the charges reversed.
