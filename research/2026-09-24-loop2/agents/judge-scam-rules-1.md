I checked the concept against the web only, as you asked. I found no company that pitches exactly this, so I judged it on its own. The closest are SafetyKit, Zentropi, Sardine and an internal tool at Coinbase. My conclusion is to pass: the idea has become a feature that several existing products already ship, and the pool of buyers is small.

## Checking the concept's claims

- **Scam losses are large and growing (confirmed).** US consumers reported $15.9B lost to fraud in 2025, up from $12.5B in 2024. The FTC reports $3.5B lost to imposter scams and says nearly 30% of people who lost money were first contacted on social media ([FTC testimony, Mar 2026](https://www.ftc.gov/news-events/news/press-releases/2026/03/ftc-testifies-joint-economic-committee-agencys-efforts-combat-fraud); [FTC, Sept 24 2026](https://www.ftc.gov/news-events/news/press-releases/2026/09/ftc-seeks-public-comment-whether-update-rule-impersonation-government-businesses-address-platforms)). This is total consumer fraud; it is not broken out for marketplaces.
- **"Teams test rules slowly" (partly supported).** SafetyKit sells on "new policies in a few hours instead of months" ([SafetyKit](https://www.safetykit.com/news/launching-new-safety-policies-in-a-few-hours-instead-of-months)). Coinbase built an internal tool in which analysts describe a new scam in plain English and get back ranked signals ([Coinbase, June 2026](https://www.coinbase.com/blog/agentic-llm-powered-signal-discovery-for-fraud-detection); the page blocked my fetch, so this comes from search summaries). So the pain is real. But the best-staffed teams build their own tools, and mid-size teams already buy AI moderation.
- **"Mostly keyword lists" (not verified).** UK regulator guidance still tells higher-risk services to use keyword detection for fraud posts ([Ofcom codes](https://www.ofcom.org.uk/siteassets/resources/documents/online-safety/information-for-industry/illegal-harms/illegal-content-codes-of-practice-for-user-to-user-services-24-feb.pdf?v=391889)). I found nothing showing that keyword lists are how today's buyers mainly work.
- **Regulation will force buyers (weak).** Australia's scam-prevention law carries fines up to A$50M, but in December 2025 Treasury confirmed that online marketplaces and dating apps are excluded ([GASA](https://gasa.org/knowledge-base/blog/assessment-of-the-november-2025-australian-treasury-scam-prevention-framework-consultancy)). The FTC's rulemaking opened today, 24 September 2026. It is aimed mainly at ad-driven platforms and has not set any obligations yet.

## Who already serves this customer

**Rules-engine vendors own the fraud team's data and buying channel.**
- Sardine already lets analysts write rules in natural language, backtest them on history, and see precision, recall and how often a rule fires ([Sardine](https://www.sardine.ai/rules-engine)).
- Stripe Radar's assistant builds rules from plain English and backtests them ([Stripe docs](https://docs.stripe.com/radar/rules)).
- Oscilar offers natural-language rules plus backtests. Unit21 recommends rules from alert history using an LLM ([Unit21, Oct 2025](https://www.businesswire.com/news/home/20251027904277/en/Unit21-Unveils-AI-Rule-Recommendations-Tackling-the-Root-Cause-of-Financial-Crime-Detection-Inefficiency)).
- Sift has had workflow backtesting since 2023, and "Workflow Simulation" since 2026 ([Sift](https://sift.com/blog/introducing-workflow-simulation/)).
- The one thing these tools lack is questions asked about listing and message text. For any of them that is a short step.

**Trust-and-safety platforms own the content and moderator decisions.**
- SafetyKit ($31.5M raised) runs over 200 policies for marketplaces including Faire, Upwork and Eventbrite, and reads listings and chats ([OpenAI case study](https://openai.com/index/safetykit/); [marketplace page](https://www.safetykit.com/marketplace-moderation)).
- Zentropi turns a plain-English policy into a yes/no labeler and tests it against your own labelled data with precision and recall. Its Community tier is free ([Zentropi](https://zentropi.ai/)).
- Musubi learns from a customer's own moderator decisions to catch scams and fraud ([Musubi](https://www.musubilabs.ai/fraud)).
- Cinder has its own rules engine with LLMs built in ([Cinder](https://cinder.ai/product/platform)).

**Open-source options push the price toward zero.** OpenAI's gpt-oss-safeguard is a free, open-weight model that classifies content against any policy you write ([OpenAI](https://openai.com/index/introducing-gpt-oss-safeguard/)).

## 1. The strongest version

A measurement-and-promotion layer for text-borne scams, sold to mid-size classifieds, peer-to-peer resale, rental and ticketing marketplaces. These companies already run a rules engine (Sift, Sardine, SEON or their own) but have no machine-learning staff for text.

- **Wedge:** scams that try to move payment off the platform, advance-fee scams and fake shipping links.
- **Core output:** "Adding this rule catches X more scams and wrongly flags Y good users, at your fixed review capacity, compared with your current rules."
- **Cost and privacy:** after the backtest, compile the winning questions into small, cheap classifiers that run in the customer's own cloud.
- **Evidence ledger:** positioned for EU and UK regulators and for any future FTC rules.
- **Pricing:** land at $30–60k a year.

## 2. Ratings

| | Score | Evidence |
|---|---|---|
| Customer need | 3 | Losses are real and vendors claim policy launches go from months to hours, but the best-staffed teams (like Coinbase) build their own tools. |
| Value over today | 2 | Sardine and Stripe already offer natural-language rules with backtests, and Zentropi already offers plain-English yes/no labelers tested on your own data. What's left is thin: text features plus lift at the team's review volume. |
| Market size | 2 | TrustCon drew about 1,350 people from roughly 450 companies ([TSPA](https://www.tspa.org/)). At $30–100k a year, marketplaces alone come to roughly tens of millions of dollars. That is my estimate, not sourced. |
| Risk (5 = low) | 2 | The rules-engine vendors own the labels and the buying channel, and each is one feature away. There is also a method problem, below. |

**The method problem.** Past labels exist mostly for cases that current rules or user reports already surfaced. Any new catch is likely to sit in the unlabelled population, so "how many extra scams it would have caught" is hard to measure honestly.

## 3. What kills it, and the fastest test

**What kills it:**
- Buyers see this as a feature of Sardine, Sift, SafetyKit or Cinder and won't pay $30k or more for it separately.
- Lift numbers aren't trusted because of the label problem above.
- Running LLM questions on every message costs too much at marketplace volume.

**Fastest test (about 2 weeks):**
1. Approach 10 marketplace fraud or trust-and-safety leads.
2. Ask each to hand over about 5,000 labelled listings or messages, including cases that were cleared, plus 3 suspicions they currently have open.
3. Return the lift and false-flag numbers within 5 days.
4. Ask for a paid pilot at $25k or more, agreed before they see the results.

Kill the idea if fewer than 3 hand over data, or if none sign.

VERDICT: PASS