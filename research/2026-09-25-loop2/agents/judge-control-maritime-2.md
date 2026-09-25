# Judge, P5 (control: Maritime), judge 2 of 3 — loop 2, 2026-09-25

Saved by the orchestrator from the judge's final reply. Scores: need 4, value 2, market 4, risk 2 (total 12). VERDICT: PASS.

The judge found Maritime (maritime.sh, YC F26, three people) and treated it as this team.

## Claims checked
- "$1 per agent per month" holds only on the $500/month Scale plan (500 machines, 60 running at once); smaller plans $1.25–$1.50; base machine 1 vCPU, 2 GB RAM, 5 GB SSD; extra RAM $2–3/GB; always-on $20/month. Real revenue per agent comes from extras.
- Firecracker microVMs, 0.5 s boot, 0.6 s wake: plausible. Logos (Google, Samsung, TikTok) shown with no traction numbers; unverified.
- Others already sell automatic sleep/wake of persistent isolated machines: Fly.io Sprites (Jan 2026; no compute billing while asleep; $0.07/CPU-hour, $0.044/GB-hour); Cloudflare Sandboxes (GA April 2026; Figma a customer); Blaxel (indefinite standby at storage cost, <25 ms resume, $7.3M seed, in OpenAI Agents SDK); E2B (pause/resume with memory; $21M A; >1B sandboxes); Daytona ($24M A Feb 2026; doubled a $1M run rate in six weeks); Modal ($355M C at $4.65B); AWS Bedrock AgentCore Runtime (microVM per session; 1 GB persistent session storage in preview, 14 days).
- On Sprites a mostly idle agent (~10 active hours/month, 1 CPU / 2 GB) costs ~$1.60, so Maritime's price is about market; its addition is predictable flat pricing.
- No incumbent owns the data; the buying channel is partly owned (larger companies buy via AWS commitments or existing Cloudflare accounts; startups self-serve on credits).

## 1. Strongest version
The fleet layer for software companies giving each customer a persistent agent: one agent per account created and removed automatically; logged-in browser sessions and credentials that survive restarts; per-customer cost tracking; guaranteed wake time; a version inside the customer's own AWS/GCP account. Compute becomes a commodity underneath; the product is per-customer lifecycle and billing.

## 2. Ratings
| | Score | Evidence |
|---|---|---|
| Need | 4 | Daytona's run rate doubled in six weeks; E2B >1B sandboxes; Figma on Cloudflare. Many agent products don't need a machine per customer |
| Value | 2 | Sprites, Cloudflare, Blaxel, E2B, Daytona already offer persistence and sleep/wake at similar or lower cost |
| Market | 4 | Agent compute is a real budget (Modal $4.65B); at $1–2/agent, $100M ARR needs millions of paid agents |
| Risk | 2 | Cheap sleeping machines becoming standard; Cloudflare and AWS price near cost and own larger buyers' purchasing; hardware squeezes margins at $1 |

## 3. Kill and fastest test
Kill: buyers treat a per-customer persistent machine as a commodity and stay where they have accounts, credits or commitments, writing fleet logic themselves. Test: find 10 companies running ≥500 per-customer agents on E2B, Daytona, Sprites or Cloudflare; get last month's bill; reprice on the fleet version; ask for a paid migration commitment. Fewer than 3 commits in two weeks, or none saving ≥30% or gaining an unbuildable capability, means no opening.

Sources: [Maritime](https://maritime.sh/) · [pricing](https://maritime.sh/pricing) · [YC](https://www.ycombinator.com/companies/maritime) · [Sprites](https://fly.io/sprites/) · [Cloudflare Sandboxes GA](https://blog.cloudflare.com/sandbox-ga/) · [Blaxel pricing](https://blaxel.ai/pricing) · [E2B persistence](https://e2b.dev/docs/sandbox/persistence) · [Daytona A](https://www.prnewswire.com/news-releases/daytona-raises-24m-series-a-to-give-every-agent-a-computer-302680740.html) · [bex.co roundup](https://bex.co/blog/2026/09/11/ai-sandbox-funding-modal-daytona-e2b) · [AgentCore sessions](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-sessions.html) · [AgentCore storage](https://aws.amazon.com/about-aws/whats-new/2026/03/bedrock-agentcore-runtime-session-storage)
