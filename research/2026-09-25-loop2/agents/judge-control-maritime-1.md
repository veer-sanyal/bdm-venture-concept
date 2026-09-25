# Judge, P5 (control: Maritime), judge 1 of 3 — loop 2, 2026-09-25

Saved by the orchestrator from the judge's final reply. Scores: need 4, value 2, market 3, risk 2 (total 11). VERDICT: PASS.

The judge found Maritime (maritime.sh, YC F26) and treated it as this team.

## Claims checked
- Firecracker microVM per agent on bare metal; idle machines saved to disk and restored on the next message; claims 0.5 s start, 0.6 s wake.
- "$1 per agent" is a parked agent's price: Starter $20 for 20 (5 running), Growth $100 for 100 (25 running), Scale $500 for 500 (60 running, 12%); extra agents $1–1.50; always-on $20/month. Works only if most agents sleep; Maritime's blog says agents are idle 96.5% of the day.
- Logos (Google, Samsung, TikTok, MIT) with no numbers or case studies.
- Need real: Daytona $24M A (Feb 2026), $1M ARR within two months of relaunch; E2B says 94% of the Fortune 100 signed up, >1B sandboxes; Modal $355M at $4.65B.

## Who else serves this customer
| Company | Offer |
|---|---|
| Fly.io Sprites | "Computers for agents"; persistent Linux machines, no charge while idle apart from storage; checkpoint/rollback |
| Blaxel (YC, $7.3M seed) | Indefinite standby, no idle compute, ~25 ms resume |
| E2B, Daytona | Pause and resume, same sandbox ID |
| Cloudflare Sandboxes | GA April 2026, active-CPU billing |
| AWS AgentCore Runtime | MicroVM per session; CPU billing stops while waiting |
| OpenClaw hosting | Vessel, DigitalOcean, Hostinger |

No incumbent owns the data (moderate SDK switching cost); the self-serve developer channel belongs to Fly, Cloudflare, Vercel and AWS.

## 1. Strongest version
A fleet manager for companies giving each end-user a long-lived, mostly idle agent (OpenClaw-style personal assistants, per-client coding or ops agents): base-image updates across 100,000 agents, per-user secrets, a wake webhook or email per agent, per-user metering for rebilling, guaranteed wake time, an in-customer-cloud option. The $1 price is a starting point, not the moat.

## 2. Ratings
| | Score | Evidence |
|---|---|---|
| Need | 4 | Daytona $1M ARR within 2 months; Fly rebuilt its homepage around agent computers; a small OpenClaw hosting market exists |
| Value | 2 | Sprites and Blaxel keep state forever and charge storage only while idle; Maritime's 12% running cap shifts risk to the customer |
| Market | 3 | Funded at billion-dollar level (Modal), but $100M/yr at ~$1/agent needs >7M paid agents; heavy users move to compute pricing |
| Risk | 2 | Commodity infrastructure from Fly, Cloudflare, AWS and funded peers; oversold flat pricing loses money as agents get more active; bare metal ties up capital |

## 3. Kill and fastest test
Kill: most agent products keep per-customer state in a database and never need a VM per user; existing fleets choose Fly, Blaxel, Cloudflare or AWS; rising active time breaks the $1 price. Test (~2 weeks): 10 companies running ≥1,000 persistent per-user agents (starting with OpenClaw hosts); get cost per agent and active hours; ask for a paid 1,000-agent pilot. Fewer than 3 commits, existing cost under $1 on Sprites/Blaxel, or active hours breaking the margin means dead.

Sources: [Maritime](https://maritime.sh/) · [pricing](https://maritime.sh/pricing) · [YC](https://www.ycombinator.com/companies/maritime) · [cost blog](https://maritime.sh/blog/the-real-cost-of-running-ai-agents) · [Fly.io](https://fly.io/) · [Sprites](https://fly.io/sprites/) · [Blaxel](https://blaxel.ai/blog/perpetual-sandbox) · [Daytona A](https://www.prnewswire.com/news-releases/daytona-raises-24m-series-a-to-give-every-agent-a-computer-302680740.html) · [E2B A](https://e2b.dev/blog/series-a) · [AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/) · [Cloudflare GA](https://developers.cloudflare.com/changelog/post/2026-04-13-containers-sandbox-ga/) · [bex.co survey](https://bex.co/blog/2026/09/08/ai-agent-sandbox-providers-comparison) · [bex.co roundup](https://bex.co/blog/2026/09/11/ai-sandbox-funding-modal-daytona-e2b) · [OpenClaw VM-per-user](https://dev.to/kinthai/openclaw-multi-tenancy-why-a-vm-per-user-does-not-scale-and-what-does-1o2l)
