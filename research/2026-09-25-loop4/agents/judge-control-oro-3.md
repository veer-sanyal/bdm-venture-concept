I didn't open any local project files, as you asked. The company in the brief already exists: ORO, which runs Subnet 15 on Bittensor. The description matches its site almost word for word (["the open arena for AI agents," a top agent that "earns rewards every day it holds the lead," a reasoning judge, 4.2M trajectories](https://oroagents.com/)), so I treated ORO as this team.

## Checking the key claims against primary sources

- **"AI agents are starting to shop for people."** Weaker than the pitch implies. OpenAI [scaled back Instant Checkout in March 2026](https://www.cnbc.com/2026/03/20/open-ai-agentic-shopping-etsy-shopify-walmart-amazon.html) after only [about 30 Shopify merchants went live](https://www.laioutr.com/en/blog/chatgpt-instant-checkout-merchant-adoption-agentic-readiness-2026). Walmart reportedly found that checkout inside ChatGPT converted about 3 times worse than sending shoppers to its own site ([Rye](https://rye.com/blog/openai-chatgpt-checkout-agentic-commerce), second-hand). The industry has regrouped around "find it in the AI, buy it on the retailer's site." Discovery is growing: [Shopify says orders from AI search rose about 13 times year on year](https://www.shopify.com/blog/agentic-commerce), which is its own claim. Agents actually finishing purchases on their own is not happening at scale yet.
- **"There is no good way to measure shopping agents."** False. There are plenty of benchmarks: [ShoppingBench (Alibaba, AAAI 2026)](https://arxiv.org/abs/2508.04266), [AgenticShop (WWW 2026)](https://doi.org/10.1145/3774904.3792724), [EComAgentBench](https://arxiv.org/pdf/2606.17698), WebMall, [Agentic Commerce World](https://arxiv.org/pdf/2608.02441), and a [September 2026 paper that checks each agent step against the store's state](https://arxiv.org/abs/2609.16093). What's missing is a single standard everyone uses.
- **"Problems generated fresh each day."** Not quite. ORO's own paper says tasks are rotated out of a growing bank of problems, with some held back for testing. They are not newly generated ([arXiv 2606.10064](https://arxiv.org/html/2606.10064v1)). The underlying store is Alibaba's ShoppingBench catalogue of 2.5M products. I couldn't find what licence it carries, which matters if the company plans to sell a model and data built on it.
- **"A judge scores the reasoning at every step."** Partly true. The paper says the judge is an AI model and its score is "correlational rather than gold."
- **"The best traces train the company's own model."** True, but the result undercuts the pitch. A small model (Qwen3-4B) trained on the subnet's traces went from 18.0% to 42.7% task success. That is **no better than the published baseline trained on cheap synthetic data (43.6%)** and below the stronger published method (48.7%). Only "the small minority" of the 12,000–27,000 daily runs are usable for training. The leaderboard settles on hand-written scripts (the top agent is about 1,850 lines of Python) rather than general agents.
- **Revenue from licensing.** I found no public evidence of customers or revenue. The subnet is funded by the network's token: about 3.4% of Bittensor emissions per [taostats](https://taostats.io/subnets/15).

## Who else serves this customer, and whether an incumbent owns it

- **Retailers:** yes, incumbents own this customer. [AWS now sells Amazon's shopping assistant to other retailers](https://www.aboutamazon.com/news/aws/aws-agentic-shopping-assistant-retailers) (Kate Spade went live after 2.5 months of testing). Shopify owns the merchant catalogue and the buying channel through [its Catalog API, the UCP standard it built with Google, and "agentic storefronts"](https://shopify.dev/docs/agents). Salesforce, Constructor and Bloomreach also sit here. Retailers will not license a separate commerce model from a subnet.
- **AI labs and agent builders buying training data:** nobody owns the commerce slice. There is a real market: [labs pay $200–2,000 per task and six-to-seven-figure contracts per quarter; Shopify is itself a buyer](https://epoch.ai/gradient-updates/state-of-rl-envs). But Scale, Surge, Mercor, Mechanize, Plato, HUD and others hold the buyer relationships ([Wing](https://www.wing.vc/content/who-will-win-the-rl-environment-market--and-why)). Prime Intellect offers an open environment hub, and [Autoppia's Subnet 36](https://github.com/autoppia/autoppia_web_agents_subnet) already runs a continuously generated web-agent arena on Bittensor.

## 1. The strongest version of the company

Drop retailers and drop the plan to license its own model. Sell two things to the dozen or so teams building shopping agents (AI labs, Perplexity, Klarna, payment networks, Shopify's and Google's agent teams) and to the data vendors that supply them:

- **A hard-to-cheat commerce training environment**, with held-back tasks and step-level checking against the store's real state.
- **Independent pre-launch certification.** Something like "your agent kept to the budget and made a sensible substitute when the item sold out in X% of cases."

The Bittensor miners become a token-subsidised red team. Their job is to find ways to game the scoring, which hardens the environment. They are not the product.

## 2. Ratings (5 is best; for risk, 5 means low risk)

| | Score | Evidence |
|---|---|---|
| Customer need | 3/5 | Labs are spending heavily on training environments, but in-chat checkout stalled at about 30 merchants, so there's little urgency to test agents that complete purchases. |
| Value over what customers use today | 2/5 | ORO's own paper shows its traces equal cheap synthetic data (42.7% vs 43.6%), not beat it. |
| Market size | 3/5 | Data and environment vendors reportedly earn about $8.5B a year combined, across 50+ vendors ([Troveo](https://www.troveo.ai/resources/rl-environment-companies), a secondary source). Commerce is a small slice, and retailers buy from AWS and Shopify. |
| Risk | 2/5 | Funding depends on the token price, the store catalogue is Alibaba's with an unclear licence, and the leaderboard rewards scripts that game the scoring. |

## 3. What would kill it, and the fastest test

**What kills it:** the teams building shopping agents won't pay for commerce environments or traces. They can generate synthetic data themselves, and the big players (OpenAI with Shopify, Google, Amazon) have real purchase data. The arena's traces are not measurably better.

**Fastest test:** send a priced offer to 10 named teams building shopping agents and 3 data vendors. Offer: a paid pilot (about $50k) for the held-out commerce environment plus a certification report. Kill the idea if fewer than 2 agree to a paid pilot or sign a letter of intent within 3 weeks. Desk research can't answer this; it needs real customer conversations.

I'm passing. The measured edge of the data is zero on the team's own numbers. Buying agents to complete purchases has stalled. The retailer customer belongs to AWS and Shopify. What's left is a crowded, token-funded vendor of training data.

VERDICT: PASS
