I checked the pitch against the web and read no local files. It matches **ORO**, Bittensor Subnet 15 almost exactly, so I treated ORO as this team. The site describes the same sold-out-phone example, daily problems, a step-by-step reasoning judge, and traces used to train its own model. Founders are Shardul Bansal and Seth Schilbe, and the subnet was registered on Jan 21, 2026 ([oroagents.com](https://oroagents.com/), [GitHub](https://github.com/ORO-AI/oro), [OpenTAO](https://opentao.ai/beginner/subnets/15-oro/)).

## How the key claims hold up
- **Sandboxed stores:** mostly true. Validators run agents in Docker sandboxes against ShoppingBench, a catalog of 2.5M real products. ShoppingBench is an academic benchmark (AAAI 2026), not ORO's own; GPT-4.1 solves under 50% of its tasks ([arXiv 2508.04266](https://arxiv.org/abs/2508.04266)).
- **"Fresh problems each day":** only partly true. ORO's own paper describes a growing bank of problems that are written up front and rotated, with a guard against paraphrased copies leaking into training. They are not newly generated each day ([arXiv 2606.10064](https://arxiv.org/html/2606.10064v1)).
- **"Judge scores reasoning at every step":** partly true. The judge gives one quality number per run, which multiplies the outcome score. The authors call it "correlational rather than gold."
- **Best traces train a good commerce model:** weak. A small model (Qwen3-4B) trained on the traces reached 42.7%, versus 43.6% for the same model trained on synthetic GPT-4.1 data, and below the 48.7% published result with an extra training stage. The paper also admits most winning agents are fixed Python scripts that use the LLM only as a classifier, so few traces show real agent behaviour.
- **Traction:** the site claims 4.2M trajectories collected since March. I found no customers or revenue, and the paper mentions no commercial use. The site lists Y Combinator as an investor, but I found no YC listing.
- **Subsidy:** SN15 gets about 3.4% of network emissions. I estimate that at roughly $30k a day (about 120 TAO a day at a TAO price near $250). This is paid in token, not by customers ([CoinGecko](https://www.coingecko.com/en/coins/oro-3)).

## 1. Strongest version
Drop retailers as the customer. Retailers don't need a shopping agent; they need to be chosen by other companies' agents. Sell two things to the roughly 10–20 teams training shopping agents (Amazon, Google, OpenAI, Perplexity, Shopify, Walmart, Klarna, Instacart and startups):
- **Commerce training environments:** licensed sandbox stores, task sets and automatic scorers they can train agents in.
- **Hard, verified failure cases:** runs where agents broke, found by miners who are rewarded for breaking agents rather than for topping a leaderboard.

The token rewards become a cheap way to generate hard tasks and red-teaming. A possible later add-on: an independent reliability score for shopping agents, sold to card networks and merchants deciding which agents to let pay.

## 2. Ratings
| Area | Score | Evidence |
|---|---|---|
| Customer need | 2 | OpenAI pulled back from Instant Checkout because of merchant operations (inventory, tax, checkout), not agent reasoning. Walmart saw in-chat checkout convert about 3x worse ([DC360](https://www.digitalcommerce360.com/2026/03/06/openai-shifts-checkout-plans-agentic-commerce-strategy/), [Checkout.com](https://www.checkout.com/blog/openai-agentic-commerce-shift)). |
| Value over today | 2 | ORO's own result matches, but does not beat, cheap synthetic GPT-4.1 data, and most winning runs are scripts rather than real agent behaviour ([arXiv 2606.10064](https://arxiv.org/html/2606.10064v1)). |
| Market size | 2 | Buyers are a handful of labs and platforms. The training-environment market leans to coding and enterprise software ([Wing](https://www.wing.vc/content/who-will-win-the-rl-environment-market--and-why)). Compute subnets earn 78–82% of Bittensor's $28–35M revenue ([CryptoBriefing](https://cryptobriefing.com/bittensor-subnets-annualized-revenue/)). |
| Risk (5 = low) | 2 | Miners already game the scoring with scripts, rewards are paid in token, no paying customer is disclosed, and buyers can build this themselves. |

**Do incumbents own the data or the buying channel? Yes.**
- Shopify built its own version: ShopGym turns real storefronts into sandboxes and generates fresh tasks ([arXiv 2605.16116](https://arxiv.org/abs/2605.16116)). Its president cites "billions of transactions" as the data advantage.
- Google, Shopify, Walmart and Target co-developed Google's Universal Commerce Protocol, which connects agents to merchant stores ([Google](https://blog.google/products/ads-commerce/agentic-commerce-ai-tools-protocol-retailers-platforms/)). OpenAI and Stripe run the Agentic Commerce Protocol ([Stripe](https://stripe.com/newsroom/news/stripe-openai-instant-checkout)).
- On the retailer side, many "agent-readiness" audit tools already exist, often free ([AgenticTrack](https://www.agentictrack.ai/)).
- Scale, Surge, Mercor and a crowd of environment startups already sell environments to the labs.
- The open benchmarks (ShoppingBench, Sierra's τ-bench retail, EComAgentBench, WebMall) are free.

## 3. What kills it, and the fastest test
**Kill condition:** no agent builder pays cash for ORO's environments or traces, because in-house or synthetic data is as good. The paper already suggests it is, and Shopify has shown it can build the same thing in-house.

**Fastest test:** offer paid pilots ($50–100k) for the environment and failure-case data to 10 named shopping-agent teams, together with a blind comparison. Train the same model on ORO data and on synthetic data of equal cost, then score both on the buyer's own held-out tasks. If fewer than 2 sign within 6 weeks, or ORO's data doesn't clearly win, it's dead. Everything above is desk research, not customer validation.

VERDICT: PASS
