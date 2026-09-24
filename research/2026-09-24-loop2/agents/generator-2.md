**Best idea: a compliance layer that US chatbot safety laws now require of consumer AI apps.** Working name: Harbor. Every message in a consumer chat app gets checked in real time, using the whole recent conversation, against about 40 small questions. Deterministic code then applies each state's rules and keeps the audit trail.

I used only web sources and read no local files. Everything below is desk research, not customer validation.

## Best idea: Harbor

**Why the need is real (desk evidence).** California's SB 243 took effect Jan 1, 2026. It requires consumer "companion" chatbots to:
- detect expressions of suicidal ideation and refer those users to crisis services;
- give minors extra protections: blocking sexual content and reminding them to take breaks;
- report annually from July 1, 2027. Individuals can sue for $1,000 per violation.

Other states have followed:
- About 14 more state chatbot laws passed in 2026, and roughly 98 bills are pending across 34 states.
- Several laws cover all users, not only companion apps. Rhode Island's penalties reach $15,000 a day, and Washington and Oregon allow private suits.
- Some laws demand "evidence-based" detection without defining it.
- The December 2025 executive order that challenges state AI laws explicitly exempts child-safety laws.
- The UK is moving to bring chatbots under its Online Safety Act.

**What the product does.**
- **One Jev call per turn:** it reads the last few turns plus the bot's draft reply and answers about 40 small questions. Examples: is this first person, current or past, is there a plan, is there a timeframe, is it passive ideation, is it fiction or role-play, are there signs of a minor, sexual content, the bot claiming to be human or a licensed professional, manipulation to keep the user engaged.
- **Rules live in code:** per-state rule packs decide the action. Options are a crisis referral (for example through ThroughLine, the helpline network OpenAI and Anthropic use), blocking or rewriting the reply, switching to minor mode, or inserting a disclosure.
- **Timers and counts are also code:** break reminders and report tallies run in code, because Jev can't handle time or counting.
- **Unclear cases escalate:** they go to an LLM such as OpenAI's gpt-oss-safeguard, then to a human.
- **Outputs:** audit logs, the auto-generated state reports, the protocol page each operator must publish, and a validation report to back the "evidence-based" claim.

**Why Jev makes it possible.** These figures are my estimates from list prices:

| | Cost per turn | Heavy user (100 messages a day) | Speed |
|---|---|---|---|
| One Jev call (~3k tokens, ~40 questions) | ~$0.00013 | ~$0.40 a month | ~0.3 s, alongside the reply |
| Mid-price LLM answering the same 40 questions | ~$0.002 | ~$6 a month | 1.5–3 s |

- The LLM cost is more than many companion and tutor apps earn per user, so checking every turn with an LLM wasn't practical.
- The cheap options that do exist check one message at a time, have no compliance workflow, and miss context:
  - OpenAI's free moderation API
  - Llama Guard
  - jevmod, an open-source Jev tool: 0.99 AUROC on single-message self-harm, but no conversation context and no law handling.
- An FPF analysis found that LLMs themselves miss passive or ambiguous ideation. Breaking the judgment into small questions is exactly where Jev showed its 63%→95% gain.

**Start narrow, grow broad.**
1. Start with small and mid-size consumer AI apps that have no trust-and-safety team: companion and character apps, AI tutors for teens, wellness bots, AI toys, and games with AI characters.
2. Then cover every consumer-facing chatbot as the laws widen, and follow the UK and EU rules.
3. Then extend to moderating human user content and checking agent actions.

**Where the moat comes from.** Every customer gets the same model, so the moat has to come from elsewhere:
- clinician-labelled conversations and the calibrated thresholds built on them;
- a published validation that lawyers and AI insurers (such as AIUC) can point to;
- rule packs kept current as laws change, like Vanta does for SOC 2;
- the ability to swap models. An open reproduction of Jev (openjev) reached 0.845 agreement against Jev's 0.883.

**Weakest points.**
- **Market size and quality:** companion apps made only about $120M+ a year outside Character.AI, the segment is fragmented and partly NSFW, and the big players build in-house. You still need a bottom-up count of paying operators.
- **Liability:** a missed suicide could bring a lawsuit against you, not just the operator. You would need a clinical advisor, contracts, insurance and "decision support" framing, and VCs will press on this.
- **Commoditized detection:** the classifier alone is nearly free. Incumbents like ActiveFence and Checkstep already sell compliance engines and could copy the workflow.
- **Jev's own weaknesses:**
  - it trails frontier models on hard labels, and passive ideation is a hard label;
  - role-play and injected text shift its answers, and injection is exactly what users will try;
  - it works best in English;
  - calibration needs labelled data, and clinical data is ethically hard to get.
- **Supplier risk:** default limits are 1,200 requests a minute. Zero data retention is enterprise-only, with no HIPAA or BAA mentioned. Signups were paused on Sept 22 because of demand.
- **Regulatory churn:** "evidence-based" is undefined, a federal ban on companion apps for minors could shrink the segment, and privacy laws restrict processing inferred mental-health data.

## Runner-ups

**1. Per-turn ad and sponsored-offer matching for independent AI apps.**
- **Why it could work:** the decision is needed on every turn, but revenue comes only on the turns that show an ad. At $5–15 CPM with an ad on about 1 in 10 turns, revenue is roughly $0.0005–0.0015 per turn. An LLM decision at about $0.001–0.002 costs as much as that; Jev is about 5–10% of it. One call can pick among up to 255 offers and check suitability.
- **It pairs with Harbor:** the same engine would suppress ads in crisis conversations or when a minor is detected.
- **Weakest:** a two-sided network is hard to start. OpenAI launched ads in ChatGPT in February 2026. Users and regulators push back on ads in chat, especially to minors. Funded rivals include Koah ($20.5M) and Dappier. Jev's option-order bias affects fairness to advertisers.

**2. "Approvals that learn" for AI agent actions** (for example, support agents issuing refunds).
- **Why it could work:**
  - Each proposed action gets one Jev call with about 20 risk questions; amounts and dates are checked in code.
  - Confident cases run automatically and the rest go to a human.
  - Human decisions retune the thresholds to hold a target error rate, so the agent earns more autonomy over time.
  - Evidence so far: the pi-warden tool held 42 of 17,000 calls and about 88% of those holds were right.
- **Weakest:** crowded (guardrail startups raised about $456M in 12 months) and easy for agent platforms to build in. Customer messages are text an attacker controls, which hits Jev's injection weakness directly.

**Dropped:**
- Medical-device complaint triage: Flinn.ai and Smarteeva already do it, and LLMs were already affordable.
- Drug-safety screening in patient-support calls: IQVIA and Authenticx already do it.
- K-12 student monitoring: GoGuardian already monitors students' AI chats.
- LLM evals, sales-signal tools and social listening: crowded, and Jev isn't decisive there.

**First checks before believing any of this:**
1. Interview 15–20 consumer AI app founders, trust-and-safety leads and their lawyers. Ask whether they're in scope, what they do today, what they pay, and whether they've had demand letters.
2. Run a shadow test on a labelled conversational self-harm set. Compare Jev (split into small questions) with OpenAI moderation and an LLM judge on passive ideation and role-play cases.

Sources:
- [TypeSafe launch blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev), [models page](https://docs.typesafe.ai/models.md), [known failure modes](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md)
- [Firecrawl on Jev](https://www.firecrawl.dev/blog/what-is-jev), [flaviocopes deep dive](https://flaviocopes.com/jev/)
- [jevmod](https://github.com/ohernandezdev/jevmod)
- [Transparency Coalition: 14 state laws](https://www.transparencycoalition.ai/news/watershed-year-for-chatbot-safety-measures-14-new-state-laws-enacted-so-far-in-2026), [Orrick](https://www.orrick.com/en/Insights/2026/04/2026-State-Chatbot-Laws-Key-Provisions-and-Regulatory-Trends), [FPF on "evidence-based" detection](https://fpf.org/blog/mandating-evidence-based-suicide-detection-in-chatbots/), [Limina on SB 243 penalties](https://www.getlimina.ai/en/blog/california-sb-243-companion-chatbot-law), [Baker Botts](https://ourtake.bakerbotts.com/post/102mipe/ai-chatbot-regulation-78-state-bills-58-lawsuits), [King & Spalding on the executive order](https://www.kslaw.com/news-and-insights/new-state-ai-laws-are-effective-on-january-1-2026-but-a-new-executive-order-signals-disruption)
- [ThroughLine](https://www.usnews.com/news/top-news/articles/2026-04-02/crisis-contractor-for-openai-anthropic-eyes-a-move-to-combat-extremism), [gpt-oss-safeguard](https://openai.com/index/introducing-gpt-oss-safeguard/), [UK Online Safety Act and chatbots](https://www.lewissilkin.com/insights/2026/02/23/online-safety-reforms-to-be-fast-tracked-amid-rising-ai-risks-102mk2r), [AIUC](https://aiuc.com/)
- [Companion app revenue](https://www.roborhythms.com/ai-companion-app-market-2026/), [ads in AI chat](https://www.getchatads.com/blog/top-eleven-ad-networks-for-ai/), [GoGuardian AI chat monitoring](https://www.globenewswire.com/news-release/2025/09/17/3151750/0/en/GoGuardian-Beacon-Strengthens-Student-Safety-with-Critical-AI-Chat-Oversight-for-the-2025-26-School-Year.html), [medtech complaint AI](https://superkind.ai/blog/ai-medical-devices), [AI safety funding](https://newmarketpitch.com/blogs/news/ai-safety-funding-news)