**Verdict:** No strong company exists in the idea as proposed. A narrower version is plausible but not yet strong. Desk research can't show whether anyone would buy it, so it isn't ready to be the Burton D. Morgan pick without customer interviews.

## What doesn't hold up

- **The 88% figure is not an accuracy number.** The pi-warden README says "the action guard held 42 calls and my next message approved 5, so 37 stood." "Stood" only means the developer didn't approve the action in his next message. It is one developer's own coding-agent sessions, not support refunds.
- **A newer version of the same README is less favourable.** It says "2 of 13 labeled holds stood, the other 11 cleared on retry," so most of the holds that were actually labeled were wrong. It also says "the 27 calls the maintainer later regretted … were ordinary edits and commits, not the kind a pre-call hold can see coming." Nothing measures how many bad actions got through.
- **Anyone can build this layer.** Jev is available on OpenRouter to anyone with a key, even though TypeSafe paused its own signups on Sept 22. It costs about $0.042 per million input tokens and answers in about 0.1–0.5 seconds. Hobbyists shipped Jev-based guards (pi-warden, jev-sentinel) within days.
- **Agent platforms have already built it in.** Intercom Fin has human approval steps for refunds. Decagon has a supervisor model, a model that screens manipulation attempts, and Watchtower, which reviews every conversation. Riskified sits inside Zendesk to catch refund abuse.
- **The closest predecessor gave up on this.** HumanLayer (YC F24) sold exactly this kind of approvals API and pivoted to CodeLayer, a tool for running coding agents. Other guard startups, such as OpenBox and CodeIntegrity (about $5M seed rounds each), are also in the space.
- **I confirmed the TypeSafe terms** (last updated Sept 23, 2026):
  - §2.3(b) bars developing "a similar or competing product or service," and Jev is sold as a "Decisions API," so an approvals product is uncomfortably close.
  - TypeSafe "may immediately suspend" access, and I found no SLA.
  - §4.1 keeps telemetry (defined to include "classifications… and learnings") forever. On the plus side, it doesn't train on customer data without consent.

## Strongest reshape: independent controls for AI agents that move money

**The insight.** Better call-time judging is not what holds agent autonomy back. The problem is that nobody can say how often the actions that ran without a human were wrong. And the agent vendor, paid $0.99 per resolution in Fin's case, is grading its own work. The product sells separation of duties to the finance and ops leaders who own the losses.

**The starting niche.** Refunds, credits and goodwill payments issued by AI support agents at mid-market e-commerce, subscription and fintech companies, whichever agent vendor they use.

**The product has five parts:**
1. **Code-enforced limits.** Caps on amount, frequency, customer tenure and order state are the only thing that can approve an action.
2. **A cheap judge.** It checks for agent mistakes, for example a refund that doesn't match the conversation, the order or the policy. It can only send a case to a human, never approve one. Jev is the first choice, with a fallback model tested from day one.
3. **Holds go to a queue** in Slack or the help desk.
4. **Error measurement.** Random audits of auto-approved actions, plus outcomes (chargebacks, items never returned, reversals, customers writing back), give an honest error rate with a confidence range for each action type.
5. **An autonomy dial and evidence export.** A cap rises only when the upper end of that error range is below the target. Reports go to controllers, auditors and insurers. AIUC, which certifies and insures AI agents, raised a $40M Series A on Sept 15.

**How it grows broad.** Refunds → all concessions an agent can grant → payables, access approvals and claims → the system of record for internal controls over autonomous agents.

**Prompt injection.** Customer text can only make a case more likely to go to a human. So the worst case is capped at the code limits for the time before the next audit sample. That bounds the loss; it doesn't solve injection.

**Handling Jev.** It must not carry the business:
- If Jev is down, everything goes to humans.
- Send it minimal, pseudonymized data.
- Never train on Jev's outputs; train only on human decisions and real outcomes.
- Keep the product's value outside Jev, so it isn't a resold "standalone service."
- Get TypeSafe to confirm in writing that this isn't a "competing product."
- Offer a no-Jev mode for security reviews that object to the permanent telemetry.

**Risks judges will press on:**
- Intercom or Decagon could add error-rate reporting. Independence may not be enough to win against them.
- It's unclear whether a separate budget exists for this.
- Chargebacks take months, which slows proof.
- Security reviews at larger companies are hard for student founders.

**Market size is my assumption only.** 5,000–20,000 companies with money-moving agents by 2028, at $20–60k a year each.

## Kill tests (customer validation)

Interview 15–20 CX-ops or finance leads at companies whose AI agent can issue refunds. Kill the idea if any of these happen:
- Fewer than 5 say they cap agent refunds because nobody knows the error rate.
- Most say their vendor's built-in approvals are enough.
- Nobody will share a month of refund logs for a free retrospective audit report.

If someone does share logs, run that audit by hand first and see whether a controller would pay for it.

Sources: [pi-warden (older README)](https://github.com/MacLeodMike/pi-warden), [pi-warden (current README)](https://github.com/DevMortimer/pi-warden), [TypeSafe MCA](https://typesafe.ai/legal/mca), [TypeSafe signup pause](https://x.com/typesafeai/status/2102281508950307159), [Jev on OpenRouter](https://openrouter.ai/docs/guides/community/jev), [Jev deep dive](https://flaviocopes.com/jev/), [Fin approvals](https://www.intercom.com/help/en/articles/14468561-human-in-the-loop-approvals-for-fin-procedures), [Fin pricing](https://fin.ai/help/en/articles/13975800-fin-pricing-outcomes), [Decagon Watchtower](https://decagon.ai/product/watchtower), [HumanLayer pivot](https://starlog.is/articles/ai-agents/humanlayer-humanlayer/), [Riskified + Zendesk](https://ir.riskified.com/news-releases/news-release-details/riskified-brings-identity-risk-intelligence-zendesk-helping), [agent-security funding](https://softwarestrategiesblog.com/2026/03/28/agentic-ai-security-startups-funding-mna-rsac-2026/), [AIUC Series A](https://runtimewire.com/article/aiuc-raises-40m-ai-agent-certification-insurance), [EU AI Act delay](https://www.gibsondunn.com/eu-ai-act-omnibus-agreement-postponed-high-risk-deadlines-and-other-key-changes/).