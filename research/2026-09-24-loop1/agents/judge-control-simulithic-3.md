I'm judging the idea, not a team. The company whose pitch matches this almost word for word is **Simulithic** (YC Fall 2026, founded 2026, 2 founders, $500K raised, early access only, no named customers, no published pricing), so I treat Simulithic as this team. Its own site says it reproduces a break and hands the team "the steps, the environment, and the session" before users write in.

## What the research found

**The closest comparable was bought by the biggest incumbent.** Datadog acquired Propolis (YC Spring 2025) on January 29, 2026. Propolis ran "autonomous agents to discover real user journeys and continuously test outcomes." Datadog's stated plan is to point those agents at its traces, logs and Real User Monitoring (RUM) data, which records what real users do in the product, so they "infer user intent from how applications are actually used."

**Datadog then shipped the product.** On September 24, 2026 (today), it announced two things:
- **Journey Monitoring** combines RUM, synthetic tests and product analytics for flows like checkout, sign-in and onboarding. It finds the most common real-user paths on its own and alerts when a flow breaks its service-level objective.
- **Bits Testing** writes tests from a plain-language prompt. It adds "goal-based" tests, which check that the user reached an outcome instead of replaying a fixed script.

The announcement gave no pricing and did not say whether the tools are generally available.

**The buying channel is already priced this way.** Datadog bills browser tests at $12 per 1,000 runs on an annual contract, or $15 to $18 pay-as-you-go. That is the same axis as this idea's pricing, flows times frequency. Checkly's worked example comes to about $8,500 a month for 16 routes checked every 4 minutes from 4 regions.

**Other companies serving this customer:**
- **Checkly** raised a $20M Series B. It turns existing Playwright tests into production monitors.
- **Momentic** raised a $15M Series A in November 2025. It has 2,600+ users, including Notion, Retool and Webflow, and writes tests in natural language that fix themselves when the UI changes.
- **Meticulous** records real user sessions and replays them against each pull request.
- **Blok** raised $7.5M in 2025 for synthetic users on live products.
- **Spur** and **Autosana** (both YC) run agent-driven end-to-end tests.
- Sentry, LogRocket and Datadog RUM already alert when real users hit errors that throw an exception. That leaves only the silent failures to this idea.

**Some claims did not check out.** The pitch assumes customers usually report breaks first. I found no rigorous primary source for that. The mabl survey I found is from 2019 and does not report that share. Market-size reports for synthetic monitoring in 2025 range from $1.4B to $3.9B, which tells you the category definition is loose.

## 1. The strongest version

Drop "across devices, browsers and regions." Datadog, Checkly and BrowserStack already cover that. Keep **account state**, the one axis RUM cannot see. RUM records clicks. It does not know that a tenant is an enterprise customer on single sign-on, with a trial that expired yesterday, three feature flags on, and a restricted admin role.

The reshaped product:
- It is a deploy-verification service for B2B SaaS teams.
- It reads the customer's tenant configurations and feature-flag state, and creates seeded test tenants that mirror the real distribution of account types.
- After every deploy, agents run the revenue and onboarding journeys as each kind of account.
- Each failure comes with a reproduction bundle.
- Pricing is per deploy verified, not per flow times frequency. Monitoring every minute is Datadog's pricing model and cost structure. Checking right after each release is where scripted monitors are weakest.
- It sells first to teams that run Sentry or PostHog rather than Datadog RUM.

## 2. Ratings for that version

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 3 | Teams already pay real money for scripted journey checks (about $8,500 a month for 16 routes in Checkly's Datadog example). But I found no primary data on how many production breaks are silent and specific to one segment. |
| Value over today | 2 | Datadog's Bits Testing (goal-based tests) and Journey Monitoring (paths learned from RUM), announced September 24, 2026, cover most of the pitch. The only extra value is account-state coverage and the reproduction bundle. |
| Market size | 3 | Synthetic monitoring is $1.4B to $3.9B depending on the analyst. Expanding into QA spend is plausible, but Momentic, Meticulous and QA Wolf are already there. |
| Risk (5 = low) | 1 | The incumbent owns the behavior data (RUM), the budget line (Synthetics) and now the exact product (Propolis), and it can bundle this into existing contracts. |

## 3. What would kill it

1. **Bundling.** Datadog prices goal-based agent tests into existing Synthetics contracts. A standalone subscription then loses every Datadog customer.
2. **Side effects in production.** Agents that place real orders, charge cards or send emails get vetoed by security and finance. The workaround, test accounts, removes the "real account state" advantage unless the product builds those tenants itself.
3. **Unit cost.** This is my estimate, not a sourced figure: a 20-step run by an LLM agent likely costs somewhere between $0.10 and $0.50. A scripted Datadog run costs $0.012. Running continuously at that price loses money.
4. **False alerts.** Nondeterministic agents that page on-call wrongly get switched off within a month.

**The fastest test** is an incident audit, and it takes about a week. Ask 8 to 10 target teams, at least half of which do not use Datadog, for their customer-reported production incidents from the last 90 days. Sort each incident on three questions:
- Was it silent, meaning no exception fired?
- Was it specific to one account state or segment?
- Would an agent have reproduced it, and did the team's existing Sentry, Datadog or Checkly setup miss it?

Kill the idea if fewer than about a quarter of incidents meet all three, or if nobody offers a paid pilot on the evidence.

Datadog already owns this customer's behavior data and buying channel. It bought the closest startup eight months ago and shipped the feature today.

VERDICT: PASS

Sources:
- [Simulithic](https://www.simulithic.com/) and its [YC profile](https://www.ycombinator.com/companies/simulithic)
- [Datadog acquires Propolis (Datadog blog)](https://www.datadoghq.com/blog/datadog-acquires-propolis/) and [Propolis YC profile](https://ycombinator.com/companies/propolis)
- [iTWire: Datadog Journey Monitoring and Bits Testing](https://itwire.com/business-it-news/data/datadog-brings-ai-to-both-ends-of-the-user-journey-with-journey-monitoring-and-bits-testing)
- [Checkly: the real costs of Datadog Synthetics](https://www.checklyhq.com/blog/how-to-spend-ten-grand-12-bucks-at-a-time/) and [Checkly $20M raise](https://www.checklyhq.com/blog/announcing-20m-to-enable-engineers-to-detect-and-r/)
- [Momentic Series A](https://momentic.ai/blog/series-a)
- [Meticulous](https://www.meticulous.ai/)
- [Synthetic monitoring market (Research and Markets)](https://www.researchandmarkets.com/report/synthetic-monitoring) and [Precedence Research](https://www.precedenceresearch.com/synthetic-monitoring-market)
- [mabl DevTestOps survey post](https://www.mabl.com/blog/teams-happiest-customers-production-bugs-hours)
