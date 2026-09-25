I'd back an AI tool that handles environmental permit compliance for small and mid-sized manufacturers, starting with air permits in Indiana. The main caveat is that a startup called AirComply is already building nearly the same product. This is all desk research, not customer validation. It's also thinner than I wanted: the session's web search budget ran out after the first few queries. After that I could only open specific pages, so some market numbers below are my own estimates and are marked that way. I didn't read any local project files, as asked.

## Best idea: turn an air permit into a finished compliance workload

**The work being replaced.** Every permitted plant has a permit that runs to many pages of limits, monitoring and recordkeeping rules. Someone has to:
- turn that permit into a list of obligations and deadlines;
- calculate emissions every month from production logs;
- draft the deviation reports and the semiannual and annual compliance reports.

Small and mid-sized plants mostly pay outside consultants for this, or give it to a stretched environmental, health and safety (EHS) manager working in spreadsheets. AirComply puts the first step alone at 30–40 hours by hand, and a major-source ("Title V") permit renewal at 100–150 hours.

**The product.** The plant uploads its permit. It gets back a register of every obligation, a compliance calendar, templates for the records it must keep, emission calculations built from its own production data, and drafts of the reports. A person at the plant, or its consultant, reviews and signs each one. It would be priced as a yearly subscription per facility, set well below a consultant retainer.

**The narrow way in.** Target smaller permitted plants: those holding "synthetic minor" permits, which cap emissions to stay under the major-source line, and smaller Title V plants. Start in Indiana, which has a very high share of manufacturing and is where Purdue has industry ties. Then expand:
1. stormwater and water permits;
2. hazardous-chemical inventory (Tier II) and waste reporting;
3. process-safety and OSHA programs;
4. the full compliance system of record for mid-market plants.

**Why it could work:**
- **The need is forced by law.** Clean Air Act penalties can run six figures a day, and consulting hours are expensive.
- **Reading permits and drafting reports is work large language models do well.** The emission math itself is plain arithmetic.
- **No software company holds these plants' data or buying channel.**
  - ERA Environmental aims at major emitters, priced per emission unit.
  - Encamp sells to large companies (300+ customers, including Amazon) and covers chemical-inventory and waste reporting, not air.
  - At small and mid-sized plants the data sits in spreadsheets and with consultants.
- **The spend is real.** The US Bureau of Labor Statistics counts 93,400 environmental scientists and specialists, about 30% of them at consulting or engineering firms, with a median wage of $82k. Adding in-house EHS staff and billing mark-ups, I estimate spend across all environmental, health and safety compliance work in the billions a year. That figure is my estimate, not a sourced number.
- **Consultants can be a channel as well as a competitor.** One reviewer could oversee the output of several junior staff.

**What's weakest:**
- **AirComply exists.** It has launched an AI product built on Anthropic's models, aimed at plants, consultants and regulators. It shows no customers yet. The story therefore can't be "nobody is doing this"; it has to win on getting to customers first, through Indiana, one industry, or a done-with-you service.
- **Consultancies are adding AI themselves** (Turtle, for example), and large compliance software suites will follow.
- **Liability and trust.** A company official legally certifies these reports, so buyers will want a human to sign off.
- **Small plants have small budgets and buy slowly.**
- **The air slice is unsized.** I couldn't verify the number of permitted plants. From memory it's roughly 15,000 Title V plants plus tens of thousands of smaller permitted sites.
- **The federal EPA is deregulating.** Most enforcement sits with states, though.

## Runner-up: Medicaid long-term-care applications for assisted living and home care

AI would collect documents from families, review five years of bank statements for asset transfers that can disqualify applicants, fill in each state's application, and track cases still waiting for approval. The payoff is faster cash for providers carrying residents whose applications are still pending. Indiana's move of long-term care into managed care in 2024 could be a local way in, but I couldn't verify how much disruption it caused.

- **Why keep it:** the return on investment is clear and easy to pitch, and the work is heavy on documents.
- **Weakest:** CoreCare already serves more than 1,500 nursing homes, links to PointClickCare (their main record system), and tracks these pending applications. So nursing homes, the obvious first market, are effectively taken. That leaves assisted living and home care, where buyers have less money. Rules vary by state, and this slice is probably under $1B.

## Checked and dropped
- **Duty drawback** (refunds of duties on imports that are later exported): about $11–15B a year goes unclaimed, but Zollback, Passport, LightSource, Pax AI and Gaia Dynamics are all already in it.
- **Refunds of the tariffs the Supreme Court struck down in February 2026:** customs set up a claims portal in April and 56,497 importers had signed up for refunds by April 9. It's a one-time windfall, not a company.
- **Property tax appeals:** Ownwell raised $50M, and Avalara launched an AI property tax product in May 2026.
- **New rule requiring importers to file product-safety certificates electronically** (from the Consumer Product Safety Commission, effective July 8, 2026): customs brokers and testing labs already hold the data and the customer relationship.

**Next step:** 15–20 interviews with Indiana plant environmental managers and air consultants. The questions to answer: what they pay consultants each year, which reports take the most time, and whether they would trust an AI draft with human sign-off.

Sources: [Zollback](https://www.zollback.com/blog/tariff-refunds-for-smbs), [Stinson on tariff refunds](https://www.stinson.com/newsroom-publications-supreme-court-invalidates-ieepa-tariffs-recent-developments-accelerate-refund-process), [Ownwell funding](https://www.housingwire.com/articles/ownwell-property-tax-appeal-funding/), [Avalara AI property tax](https://techedgeai.com/avalara-unveils-ai-powered-property-tax-platform-to-speed-enterprise-compliance/), [CPSC eFiling](https://www.cpsc.gov/Newsroom/News-Releases/2026/CPSC-Implements-Mandatory-eFiling-for-Certificates-of-Compliance-Targeting-Dangerous-Foreign-Imports), [AirComply](https://aircomply.com/), [Engineer Live on AirComply](https://engineerlive.com/new-ai-platform-for-air-quality-permitting-and-compliance/), [ERA Environmental](https://www.era-environmental.com/solutions/environmental/title5), [Encamp](https://www.encamp.com/), [Turtle](https://www.turtle.com/solutions/technology/ai-environmental-consulting/), [BLS environmental specialists](https://www.bls.gov/ooh/life-physical-and-social-science/environmental-scientists-and-specialists.htm), [CoreCare](https://corecare.ai/), [Sparkco](https://sparkco.ai/blog/medicaid-pending-applications-guide-for-skilled-nursing-facilities)
