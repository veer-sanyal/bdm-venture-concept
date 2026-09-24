## The company that matches this pitch

Sona8 (YC Fall 2026, 4 people, San Francisco) describes nearly the same product: a voice agent, a link for each employee, about 20 minutes, follow-ups like "why is this step still manual," consulting firms buying for the opening interviews, and transformation and corp dev teams using it to track rollouts. The founders came up with it after running more than 70 stakeholder interviews on one consulting project ([YC profile](https://www.ycombinator.com/companies/sona8)). Per your instructions I treat Sona8 as this team.

## Checking the key claims

- **"Consultants spend weeks on interviews and hear from only a few people."** This is plausible, but the only numbers come from vendors. Ontora says the work takes "4 months and 50-100 manual interviews" ([YC](https://www.ycombinator.com/companies/ontora)), and the Sona8 founders report 70 on their own project. I found no independent benchmark.
- **"Hearing from more of the frontline matters."** McKinsey's research supports this in general: roughly 30% of transformations succeed, and organizations that listen to frontline employees and act on what they say are more likely to adopt new ways of working ([McKinsey](https://www.mckinsey.com/capabilities/transformation/our-insights/going-all-in-why-employee-will-can-make-or-break-transformations)). The page timed out when I fetched it, so the "80% more likely" figure comes from a search summary, not a direct read.
- **"An AI can run a useful interview."** Published research supports this. In an N=571 study, voice interviews produced about twice as many words as text, and respondents rated the AI interviewer as more engaging than a standard survey ([arXiv 2606.20064](https://arxiv.org/html/2606.20064v1)). Two caveats: earlier work found AI interviews less rich than expert human ones, and the study says it is unclear whether it works for technical or sensitive topics. Process work inside an employer is both.
- **The interview itself is cheap to run.** Superintelligent's agent interviewed 150 employees at a Fortune 100 company in two weeks for about $500 total, and ran thousands of interviews in its first month ([Fractional AI case study](https://www.fractional.ai/case-study/automating-enterprise-discovery-superintelligents-ai-interview-agent)). That figure appears to be run cost, not the price charged. Either way, anyone can build the agent, so the value has to come from the analysis and the follow-up loop.

## Who else serves this customer

- **Near-identical startups.** Ontora (YC Spring 2026) has 5 design partners, 150+ inbound demo requests and $700K raised; its customers include a PE firm and roll-ups of 800 to 1,000+ employees. Foaster (YC Spring 2026) is an AI-native consultancy built on the same employee interviews. Superintelligent already runs a white-label consulting partner program, with interview agents, a database of 5,000+ use cases and reports branded as the consulting firm's own work ([besuper.ai/partner](https://besuper.ai/partner)).
- **Employee listening vendors own the channel to employees.** Qualtrics shipped AI follow-up questions in its employee experience product in March 2026. When prompted, 40% of respondents expand their answer, producing about 4x the words with no increase in drop-off; adidas and Verizon are early users ([Reworked](https://www.reworked.co/employee-experience/qualtrics-updates-employee-experience-suite-with-conversational-feedback-and-predictive-analytics/)). Perceptyx and Viva Glint already run pulse surveys after interventions. These vendors hold the HR contract and the works-council approvals for "ask every employee something."
- **Process mining vendors own the process data.** The market was $1.1B in 2024 and Celonis has a 47% share ([Gartner via AIMultiple](https://research.aimultiple.com/process-mining-trends/)). Celonis has Task Discovery (tracking manual clicks and messages) in private preview. SAP Signavio sits inside SAP's own transformation offer.
- **AI research interview platforms have more money.** Listen Labs has raised $69M and Outset $51M. They sell mainly for market research, but their products could be pointed at employees.

Do incumbents own this customer's data or buying channel? Yes, on both sides. Inside the enterprise, HR's listening vendor owns the link to every employee, and Celonis or Signavio own the process data. On the consulting side, the firm itself controls the purchase and today bills discovery as labor.

## 1. The strongest version

Narrow it to **before-and-after measurement for ERP and operations transformations, sold to mid-tier system integrators and PE operating teams.** SAP ERP 6.0 mainstream maintenance ends December 31, 2027, and more than half the installed base has not migrated yet ([SAP Community](https://community.sap.com/t5/enterprise-resource-planning-blog-posts-by-sap/maintenance-timelines-for-sap-erp-6-0/ba-p/13524564)). The product would do two things:

1. It captures the work that happens outside the ERP system (spreadsheets, workarounds, handoffs) and exports it as BPMN, the standard process-model format, into Signavio or Celonis. That makes it a complement to those tools, not a rival.
2. It re-interviews the same people after go-live and measures adoption by site.

Price it per program, not per engagement. The repeat interviews with the same people are the one piece a one-off diagnostic or a generic survey add-on does not have. Drop MBB as a target: they have built in-house tools like McKinsey's Lilli and treat discovery as billable work.

## 2. Ratings

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | The founders ran 70+ interviews on one project, and Ontora reports 150+ inbound demo requests within months. |
| Value over what customers use today | 3 | Qualtrics already gets follow-up answers from 40% of respondents at survey scale. Voice adds depth (2x the words of text) and a process map, not a new category. |
| Market size | 3 | The closest software comparison, process mining, is $1.1B across a whole enterprise category. Per-engagement discovery tooling is a slice of a $120B top-tier consulting market that prefers to bill labor. |
| Risk (5 = low) | 2 | The agent costs about $500 per 150 interviews to run, so it is easy to copy. Three YC companies do this in 2026 alone, Superintelligent already white-labels to consultancies, and the EU AI Act bans inferring emotion from voice at work (Art. 5(1)(f), fines up to 7% of turnover). |

## 3. What would kill it, and the fastest test

The two ways it dies:

- **Employees don't show up or don't talk honestly.** If completion falls below about 40%, or answers stay polite and generic because the employer is listening, the output is no better than a Qualtrics survey with follow-ups.
- **The buyer won't pay.** The consultancy either bills the interviews as analyst hours or builds or white-labels a cheap agent. The transformation team then gets the same feature through its existing HR listening contract.

The single fastest test: on one live engagement at a mid-tier SI or PE portfolio company, send links to about 200 employees at one site. Within 5 business days, measure three things:

1. The completion rate.
2. How many material process problems the engagement lead says were not already in their own interview notes.
3. Whether the lead signs a paid order for the next engagement at the proposed per-program price.

If completion is under 40%, there are fewer than 3 new findings, or the lead won't pay, it is dead.

## Bottom line

The problem is real, but the interview agent is cheap for anyone to build. The two budgets that would pay for it are each controlled by someone else: HR's listening vendor inside the enterprise, and the consulting firm on the engagement side. At least four funded teams are already competing on the same cheap interview agent, and none of them owns a channel. The repeat-interview version for ERP programs is the best angle, but Signavio already sits inside SAP's own transformation offer.

VERDICT: PASS
