The concept matches **Simulithic** (YC F26, two founders) almost word for word, so I judged it as this team. Its YC listing says it "continuously uses your production product like your real users do", runs across devices, browsers, account states and environments, and catches failures that scripted end-to-end tests miss. It is pre-launch: the site offers "early access" through a call with the founders and shows no pricing and no customers. The site's title, "Simulate product changes before you ship", doesn't match the body copy, which is about monitoring live production. So the positioning hasn't settled yet.

## Who else serves this customer

- **Datadog owns this customer's data and buying channel in mid-market and enterprise.**
  - Since September 2023, a team can turn a recorded real-user session into a scheduled browser test with one click.
  - On June 9, 2026 it announced Bits Testing, now in preview. It is an AI agent that explores an app from a URL or a plain-English goal, finds the critical user journeys, and generates tests that adapt when the page changes.
  - A September 24, 2026 trade report says Datadog also announced Journey Monitoring. It links real-user data, scripted tests and product analytics to show where conversions fail. I could not confirm this on Datadog's own site.
  - The one gap left open: Datadog's own post on Bits Testing does not mention using real-user data to choose journeys.
- **Other AI testing tools can already run on a schedule against production:**
  - TesterArmy (YC Spring 2026) has 20+ companies using it in production.
  - QA.tech has raised $5M.
  - Momentic raised a $15M Series A in November 2025.
  - Spur (YC Summer 2024, $4.5M) sells ecommerce and travel sites testing that "emulates real consumer shopping behaviour". A 2025 press release says it has 30+ enterprise customers. That is the closest competitor to the narrowed version below.
- **Checkly** runs scripted browser checks starting at $24 a month. Datadog charges $12 per 1,000 browser test runs.
- **The companies that hold the real-user data** that "built from how real users behave" depends on are Datadog, Sentry (session replay plus Seer, its AI debugger), PostHog and FullStory.

## 1. Strongest version

Don't sell to every team that ships daily. Sell to consumer-facing companies (ecommerce, subscriptions, fintech) whose revenue flows are signup, checkout and payment. Cover the combinations of device, browser and region that internal teams never test:

- mobile Safari
- the in-app browsers inside Instagram and TikTok
- the bank's extra identity check on card payments (3-D Secure)
- regional payment methods
- non-US locales

Price by monitored revenue flow. The data should come from whatever tool the customer already uses to record sessions, which is Sentry or PostHog for teams not on Datadog. Each alert has to be a confirmed reproduction with steps, environment and a recording, never "the AI thinks something is off".

## 2. Ratings (that version)

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | In Baymard's cart-abandonment survey, 17% of shoppers who abandoned a checkout said the site "had errors / crashed". A Lightrun-sponsored survey of 200 enterprise reliability leaders (Jan–Feb 2026) found 43% of AI-generated code changes needed debugging in production after passing QA and staging. That one is a vendor survey. |
| Value over today | 2 | Datadog has turned real sessions into tests since 2023, and its agent now finds journeys on its own. The new part is the segment and environment mix drawn from real traffic, which a feature release could copy. |
| Market size | 3 | Analyst reports put synthetic monitoring at about $1.4–1.7B in 2025. That source is weak, but it is the budget this product would replace. A larger QA and testing budget sits next to it. |
| Risk (5 = low) | 2 | Datadog owns the data and the channel. Running fake users in production means fake orders, payments and bot-detection triggers, plus seeded accounts for every "account state". AI agents also raise false alarms, and false alarms get monitoring tools switched off. |

## 3. What kills it, and the fastest test

The idea fails if simulated users modelled on real behavior don't find confirmed bugs that the customer's existing checks (or Bits Testing's goal-based tests) miss, often enough and with few enough false alarms to be worth a subscription. It also fails if the product can't run safely against real payment and login flows.

The fastest test is a two-week shadow run with three design partners: consumer companies that already monitor checkout with Datadog or Checkly. Run Simulithic on each partner's checkout and signup flows alongside their current monitors. Count bugs the partner confirms that their monitors missed, and count false alerts.

- Pass: at least one confirmed bug per partner that their monitors missed, under one false alert a week, and at least one partner converting to paid.
- Fail: nothing new found, or noisy alerts. Either one kills the idea.

The customer need is real. But the input that sets this apart is real-user behavior, and it sits in other companies' products. The largest holder of that data, Datadog, has already shipped the neighboring product to the same buyer. Once the idea is narrowed to where it's strongest, Spur already sells it.

Sources:
- [Simulithic, YC profile](https://www.ycombinator.com/companies/simulithic) and [site](https://www.simulithic.com/)
- [Datadog: Bits Testing (June 9, 2026)](https://www.datadoghq.com/blog/bits-testing-test-coverage/)
- [Datadog: tests from Session Replay (Sept 2023)](https://www.datadoghq.com/blog/create-browser-tests-from-datadog-rum-session-replay/)
- [Developer-Tech: Datadog Journey Monitoring](https://www.developer-tech.com/news/datadog-autonomous-testing-monitoring-suite/)
- [TesterArmy, YC](https://www.ycombinator.com/companies/testerarmy)
- [QA.tech](https://qa.tech/)
- [Spur $4.5M](https://finance.yahoo.com/news/spur-raises-4-5m-first-130600285.html)
- [Momentic $15M](https://techcrunch.com/2025/11/24/momentic-raises-15m-to-automate-software-testing)
- [Checkly pricing](https://www.checklyhq.com/pricing/)
- [Datadog pricing](https://docs.datadoghq.com/account_management/billing/pricing/)
- [Baymard abandonment reasons](https://baymard.com/lists/cart-abandonment-rate)
- [VentureBeat on Lightrun survey](https://venturebeat.com/technology/43-of-ai-generated-code-changes-need-debugging-in-production-survey-finds)
- [Research and Markets: synthetic monitoring](https://www.researchandmarkets.com/report/synthetic-monitoring)
- [Sentry Seer](https://sentry.io/about/press-releases/sentry-expands-seer-ai-debugging-agent)

VERDICT: PASS
