I'd pass on this as pitched. The only part competitors don't already offer is measuring error rates independently. That's a real idea, but it looks like a monitoring business, and the finance buyer has no evidence of pain yet. This is desk research only; I haven't validated anything with customers.

## Checking the key claims

- **AI agents issue refunds without a human: true.**
  - Fin (formerly Intercom) connects to Stripe and Shopify through its "Procedures" workflows.
  - Gorgias's AI agent can cancel orders and refund automatically, remove items and refund the amount, and refund price differences.
  - Decagon runs refunds with its checks written in code.
- **Vendors are paid per resolution and grade their own work: true, from primary sources.**
  - Zendesk: resolutions "are also verified by a large language model."
  - Fin: $0.99 per outcome. A customer going quiet for 24 hours counts as an "assumed resolution" and is billed. Neither vendor's documentation says what happens when the action itself was wrong.
  - Sierra is paid per outcome, and a refund that gets issued closes the conversation, so the vendor is paid when its agent refunds.
- **"Nobody measures how often these actions are wrong": only partly true.**
  - Decagon runs a supervisor model on every live conversation and reviews all conversations afterwards.
  - Zendesk QA scores every AI-agent conversation.
  - Cekura sits above Sierra and Decagon and counts resolutions independently so customers can check their invoices.
  - What nobody publishes is a statistically measured error rate for each action type, linked to outcomes such as chargebacks. That gap is real.
- **Hard limits and human approval are already built into the agent products.** Fin has deterministic checks plus human-approval steps for refunds and goodwill payments. Decagon enforces its refund checks in code. Gorgias restricts actions by order state. Hard limits are the basic feature buyers already expect, not something that sets this apart.
- **Agents do make mistakes.** On the tau-bench retail benchmark, even GPT-4o scored under 50% on a single attempt and under 25% when it had to succeed 8 times in a row. That's a benchmark, not production data.

## Who else serves this customer

- **Agent vendors, which own the data and the execution path:** Fin (Salesforce signed to buy it for $3.6B on 15 Jun 2026), Zendesk, Decagon, Sierra, Gorgias. They control the conversation data and the refund API call. A native Shopify refund inside Gorgias or Fin never passes through an outside control point.
- **Refund-abuse vendors, which own the risk team's budget and are already in the refund path:** Riskified announced on 15 Sep 2026 that its identity signals will feed human and AI support agents inside Zendesk (available November 2026) to curb refund abuse. Riskified also has an "AI Agent Policy Builder" for rules on refund-claim abuse. Forter has a Dispute Agent.
- **Independent monitoring:**
  - Isara: the closest pitch. It tells support leaders at fintech and iGaming companies it independently flags unauthorized refunds and says vendor dashboards have "little incentive" to show errors. But it only monitors after the fact and doesn't cap what the agent can do, so I treated it as the closest competitor rather than this team.
  - Cekura: tests and monitors agents from the outside.
  - Raindrop: general agent monitoring, $50M raised as of Sep 2026.
  - Rippit (formerly MaestroQA) and Zendesk QA: conversation quality scoring.
- **Certification:** AIUC-1 certifies the agent vendors themselves (Fin and Ada hold it), and AIUC links insurance to it.

## 1. The strongest version

**What it is.** An independent tool that lets a company give its AI agent bigger refund limits once the error rate is proven low. It's sold jointly to the operations leader, who wants more automation, and the controller, who has to sign off.

**Where to aim it.** Subscription and fintech companies whose AI agent issues material credits: fee reversals, goodwill payments, subscription credits. Say over $1M a year. Mid-market e-commerce refunds are small and Gorgias already limits them.

**What to lead with.** The measurement, not the gate:
- random audits, done partly by human reviewers at first
- a link to outcome data such as chargebacks, repeat contacts and repeat refunds
- a measured error rate and dollar loss for each action type
- a check of the vendor's per-resolution invoice

Offer the gate as an optional proxy only where the agent calls a custom API. The pitch to the operations leader is "this is how finance lets you raise the limit," which lines their incentive up with the buyer's.

## 2. Ratings for that version

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 2/5 | I found no survey or public incident showing finance leaders asking for this. Isara, the closest product, names one reference customer (Commerce7). |
| Value over what customers use today | 2/5 | Limits and human approval are built into Fin, Decagon and Gorgias. Checking every conversation and the invoice is already offered by Zendesk QA, Decagon and Cekura. Only the per-action error rate and the rules for raising limits are new. |
| Market size | 2/5 | Fin has about 8,000 customers in total. Only some of them let the agent move money on its own. My rough estimate is a few thousand buyers at about $40k, which puts the ceiling around $100–200M. |
| Risk (5 = low) | 2/5 | Fin is being bought by Salesforce, and Riskified is going into Zendesk's refund flow. Refunds made through native integrations skip any outside gate. |

## 3. What would kill it, and the fastest test

**What kills it:** in the mid-market, the refund dollars an agent wrongly issues each year are smaller than the $20–60k price. Or finance accepts the vendor's own limits and QA as good enough.

**Fastest test (about 2 weeks):** find 5–10 subscription or fintech companies whose AI agent issues credits. Ask each for 90 days of agent-issued refunds from Stripe, Shopify or Chargebee, plus the transcripts. Audit a random sample of about 200 per company by hand. Report the error rate and the yearly dollar loss for each, then ask the controller for a paid pilot at $20k or more.
- If the measured loss comes in under the price, or fewer than 3 companies sign, stop.
- If controllers didn't even know how much their agent refunds, that's a better signal than any interview.

VERDICT: PASS