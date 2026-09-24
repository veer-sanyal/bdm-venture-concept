1. **The strongest version**

The broad pitch is to simulate real users on every flow, all day. It walks straight into Datadog. On 2026-09-24 (today), Datadog announced two previews that together make up this pitch:

- **Journey Monitoring** reads real user traffic to find the high-volume paths users take to an outcome, and puts conversion, uptime and errors for each critical flow in one view.
- **Bits Testing** runs goal-based agents that "continuously test journeys". It checks whether the outcome was reached instead of replaying a script, and it finds the path again when the page changes.

The narrow version worth arguing for goes after the flows real-user monitoring can't watch. Real-user monitoring (RUM) records what actual visitors do on the site, so it only sees a broken flow once real people hit it. That leaves out:

- enterprise SSO onboarding
- an admin inviting users
- password reset
- plan upgrades and downgrades
- any page a particular role, plan or feature-flag setting unlocks

These flows get little traffic but cost a lot when they break. The product would keep a fleet of production test accounts, one for each combination of role, plan, entitlement and region. It would run the flows on real devices on a schedule and hand over a reproduction when one breaks.

The hard part to copy is keeping that grid of account states alive and seeded. It would be sold to B2B SaaS companies with an enterprise tier, where a broken SSO setup can stall a contract. It would work with whatever analytics tool the customer already uses, so it doesn't depend on Datadog RUM.

The closest outside match is Propolis (YC X25). It pitches swarms of browser agents that simulate users and file bug reports with reproduction steps, for $1,000 a month with unlimited use. Its agents explore the app on their own and are not built from real user behavior. The Launch HN thread didn't name any customers. Commenters there asked how it differs from a few prompted browser tabs, called the price "enterprisey", and flagged email/OTP, OAuth redirects and shared state across parallel runs. Those are exactly the account-state problems the narrow version has to solve.

2. **Ratings for the narrow version**

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Microsoft's study of 152 high-severity Teams incidents (SoCC '22 best paper) found automated monitors caught only about 55%. External users reported 29%. |
| Value over what customers use today | 2 | Datadog Bits Testing already does goal-based, self-adjusting journey tests. Checkly sells scripted browser checks at $4 to $6.50 per 1,000 runs. Momentic ($15M Series A, used at Notion and Retool), QA Wolf ($56M to $76M raised), Checksum (tests built from real sessions) and Meticulous (replays real sessions) cover the neighboring ground. The account-state grid is the only clear gap. |
| Market size | 3 | Analyst reports put synthetic monitoring at about $1.4B to $1.7B in 2025, growing 8% to 15% a year. These are low-quality sources. Budget for QA automation adds to it. |
| Risk (5 = low) | 2 | The incumbent owns the behavior data and the budget. Running an LLM agent costs far more than a scripted check at fractions of a cent per run. Unreliable agents mean false alarms, which make teams ignore a monitoring product. Bot detection and MFA also get in the way of production test accounts. |

Datadog owns this customer's data and buying channel. The "built from how real users behave" part needs RUM and session-replay data. Datadog, LogRocket (its Galileo AI already watches every session for struggle) and PostHog hold that data, and so does Lucent (YC), which watches session replays around the clock. Synthetic monitoring for daily-shipping teams is bought inside the observability contract. Datadog already turns a session replay into a browser test with one click. It now gives journey health, discovered from RUM, to customers who pay for its RUM, Synthetics and Product Analytics products.

3. **What kills it and the fastest test**

It dies if customers treat a monitor for each role, plan and permission combination as a feature of their existing tool. That happens if Datadog, Checkly or Momentic adds "run this journey as each of these test accounts." It also dies if agents raise enough false alarms that teams mute them. Pricing by number of flows and how often they run is the same per-run model Checkly and Datadog already sell cheaply, so it doesn't protect margins.

The fastest test takes about a week. Get 10 B2B SaaS teams to export their last 90 days of bugs that customers reported in production. Tag each one: would a scheduled run as a specific role, plan or flag setting have caught it first? If fewer than about a third qualify, or fewer than 3 of the 10 will pay for a pilot on those flows, the narrow version has no wedge. A wedge here means a starting problem painful enough that teams will pay a new vendor to fix it.

Competition isn't the reason to pass. The problem is that the idea's differentiator runs on data the incumbent already owns. The incumbent's preview matches the broad pitch on the day of this review, and the gap that remains is narrow and easy for others to add.

Sources:
- [Datadog DASH 2026 roundup (Bits Testing Agent and Journey Monitoring previews)](https://www.datadoghq.com/blog/dash-2026-new-feature-roundup-keynote/)
- [iTWire on the Datadog Journey Monitoring and Bits Testing announcement, 2026-09-24](https://itwire.com/business-it-news/data/datadog-brings-ai-to-both-ends-of-the-user-journey-with-journey-monitoring-and-bits-testing)
- [Datadog docs: generate synthetic browser tests from session replay](https://docs.datadoghq.com/synthetics/guide/rum-to-synthetics/)
- [Ghosh et al., "How to Fight Production Incidents?", SoCC '22 (PDF)](https://www.microsoft.com/en-us/research/wp-content/uploads/2022/09/3542929.3563482.pdf)
- [Launch HN: Propolis (YC X25)](https://news.ycombinator.com/item?id=45762012)
- [Checkly pricing](https://www.checklyhq.com/pricing/)
- [Momentic Series A](https://momentic.ai/blog/series-a)
- [QA Wolf funding (Tracxn)](https://tracxn.com/d/companies/qawolf/__0arZFs-m4dJSTSCQDJ1NTQnSVKyhKFvcJVpWfwhqfw4/funding-and-investors)
- [Checksum](https://checksum.ai/)
- [Meticulous](https://www.meticulous.ai/)
- [LogRocket Galileo](https://logrocket.com/products/galileo-ai)
- [Lucent (YC)](https://www.ycombinator.com/launches/Pfq-lucent-ai-that-automatically-watches-your-session-replays)
- [Synthetic monitoring market size (Precedence Research)](https://www.precedenceresearch.com/synthetic-monitoring-market)

VERDICT: PASS
