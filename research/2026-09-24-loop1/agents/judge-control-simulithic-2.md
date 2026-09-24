The pitch is sound, but the core is now a feature that Datadog, the incumbent monitoring vendor, launched this week. What would make it different, users modeled on real behavior and real account states, rests on a claim nobody has shown: that these simulated users catch breakages the team's existing tests miss.

## What the research found

**The claims.** The problem is real, and Datadog's own launch is the best proof. On Sept 24, 2026 it announced Journey Monitoring and Bits Testing. Datadog says they are built to check that users can complete "business-critical flows like checkout, sign-in and onboarding" ([iTWire](https://itwire.com/business-it-news/data/datadog-brings-ai-to-both-ends-of-the-user-journey-with-journey-monitoring-and-bits-testing), [DASH 2026 roundup](https://www.datadoghq.com/blog/dash-2026-new-feature-roundup-keynote/)).

On cost, PagerDuty surveyed 500 IT leaders at companies with over 1,000 employees in 2024. They reported customer-facing incidents up 43% in a year, at about $794k per incident ([PagerDuty](https://www.pagerduty.com/newsroom/study-cost-of-incidents/)). That is self-reported, and the survey does not say who spots incidents first. I found no primary source for the pitch's central claim, that customers discover these breakages before the team does. It is a plausible anecdote, not a proven fact.

**Does an incumbent own the data or the buying channel? Yes, for Datadog customers.**
- Datadog holds the real-user session data (RUM, its real user monitoring product).
- It already turns a real user session into a synthetic browser test with one click ([docs](https://docs.datadoghq.com/synthetics/guide/rum-to-synthetics/)).
- It already owns the budget line this product would bill against, at $12 per 1,000 browser test runs ([Datadog pricing](https://docs.datadoghq.com/account_management/billing/pricing/)).
- Bits Testing adds AI agents that set a goal and find their own path to it, so tests keep working when the interface changes.

Outside Datadog accounts, the behavior data sits with product analytics vendors (PostHog, Amplitude) and session replay tools. That is open ground for a partnership, but nobody has taken it yet.

**Near-exact match, treated as this team.** [TesterArmy](https://www.ycombinator.com/companies/testerarmy) (YC Spring 2026) is an AI agent that uses a web or mobile app the way a real user does. It monitors production on a schedule, runs on every pull request, and files bug reports with recordings. What it lacks from this pitch is simulated users built from real behavior data.

**Other companies serving this customer.**
- [Propolis](https://news.ycombinator.com/item?id=45762012) (YC X25) sells "swarms of synthetic users" for $1k a month. Its founders called test data and account state "one of our biggest challenges".
- [Checksum](https://checksum.ai/) generates end-to-end tests from real user sessions.
- [Meticulous](https://www.meticulous.ai/) records production sessions and replays them as tests.
- [Spur](https://pulse2.com/spur-4-5-million-raised-to-advance-quality-analysis-ai-agent-technology/) (YC S24) raised $4.5M. Its customers include HelloFresh.
- [Momentic](https://www.techbuzz.ai/articles/momentic-raises-15m-series-a-to-automate-software-testing-with-ai) raised a $15M Series A. Its customers include Notion and Retool.
- [QA Wolf](https://techcrunch.com/2024/07/23/qa-wolf-secures-36m-to-grow-its-app-qa-testing-suite) has raised $57M. Its median contract is about $83k a year ([Vendr](https://www.vendr.com/marketplace/qa-wolf)).
- [Checkly](https://www.checklyhq.com/blog/announcing-20m-to-enable-engineers-to-detect-and-r/) has over 1,000 customers for code-based synthetic monitoring.
- [Decipher](https://www.ycombinator.com/launches/O4O-decipher-ai-that-discovers-issues-and-opportunities-in-your-product) watches real sessions for breakages after they happen.

## 1. The strongest version

Sell a coverage gap product, not "AI users". It would:
1. Connect to the customer's product analytics (PostHog, Amplitude or Segment).
2. Rank the combinations real users actually hit (journey, segment, device, account state) by revenue.
3. Show how few of them existing tests cover.
4. Create matching sandbox accounts through the customer's API, for example an enterprise admin mid-onboarding or a lapsed card on a paid plan. Agents run each combination against production on a schedule.
5. File a ticket that reproduces the bug, with the steps, the environment and the session.

Aim at B2B SaaS and e-commerce companies that run on product analytics plus Checkly or nothing, not Datadog's digital experience customers. Price by covered journey times how often it runs, as the pitch proposes.

The one hard, unsolved problem worth owning is account state and test data. Datadog, Propolis and TesterArmy all run agents from a URL or a goal. None of them creates realistic account states.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Datadog built two products this month for "can users complete checkout, sign-in, onboarding". Whether customers find these breaks first remains unproven. |
| Value over what customers use today | 2 | Datadog already turns real sessions into tests and runs goal-based agents, and Checksum builds tests from real sessions. What is left is segment and account-state coverage. |
| Market size | 3 | QA Wolf's ~$83k median contract and Checkly's 1,000+ customers show real spend. Analyst estimates for synthetic monitoring run from $1.6B to $3.9B ([IMARC](https://www.imarcgroup.com/synthetic-monitoring-market)), which is soft and inconsistent. |
| Risk (5 = low) | 2 | Datadog owns the data and the budget line. At least six funded seed or Series A companies sell nearly the same thing. Agents running on live production also produce false alarms and create junk data. |

## 3. What would kill it, and the fastest test

**What kills it.** Simulated users could find few real breakages that the team's current tests, error monitoring and support queue don't already surface. Or they could find them at a false-alarm rate that makes engineers mute the alerts. Then the product is a Datadog checkbox with extra setup cost, because someone has to create the test accounts.

**Fastest test: a two-week audit of support tickets, with nothing built.** Get 8 to 10 target companies to export 90 days of customer-reported bugs from Zendesk or Intercom, plus their list of existing tests and error alerts. Sort each ticket by three questions:
1. Was it a broken user journey?
2. Was it specific to a segment, device or account state?
3. Did the existing tests and error monitors miss it?

If the median company has fewer than about 2 of these a month, the need is too thin to support a monthly subscription. If the count is high, run agents on those exact cases to check that they catch them.

VERDICT: PASS
