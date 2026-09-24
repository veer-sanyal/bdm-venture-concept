I'd drop this as an ad network. It doesn't make a strong company for Veer and Cole. The only part worth keeping is the check that decides when ads must not show, because a minor or a user in crisis is in the conversation. That check belongs inside entry 1 as one extra output, not in a separate company.

I followed your instruction not to read local project files, so I didn't check this against METHOD.md or STATE.md. Everything here is desk research, not customer validation.

## Why the ad network fails

- **Crowded, well-funded rivals.** Koah ($26M+ raised, Tomasz Tunguz on its board), Gravity ($38.5M), ZeroClick ($55M, from Honey's co-founder), Dappier, Kontext, Nexad, Thrad, ChatAds and about ten more. Google's AdSense for Search already serves ads in third-party chatbots. OpenAI's own ads went live on February 9, 2026. Two undergrads can't win a two-sided network against that.
- **Small prize for independent apps.** eMarketer forecasts US chatbot ad spend of about $0.96B in 2026 and about $5B by 2030. Most of that goes to ChatGPT, Copilot and Gemini. If independent apps got about 10% (my guess), that is about $500M of ad spend in 2030, split across all of the networks above.
- **The cost argument doesn't hold.** Jev costs $0.042 per million input tokens. One turn with about 1.5k tokens of conversation plus 255 offers at about 25 tokens each is about 8k tokens, or about $0.0003. That is 20–65% of the $0.0005–0.0015 revenue per turn, not 5–10%. The $0.001–0.002 LLM figure assumes a pricier model. Cheap models now cost $0.02–0.10 per million tokens, so Jev is at most about 2x cheaper. A simple pre-filter that cuts the list to about 10 offers makes the backend choice almost irrelevant. Jev is not an edge.
- **The Jev terms are dangerous in an ad-serving path:**
  - There is no SLA and TypeSafe can suspend immediately. A suspension cuts off revenue for every publisher at once.
  - §4.1 lets TypeSafe keep telemetry from third-party users' chats forever. That includes minors' conversations, which conflicts with COPPA and with the privacy promises advertisers now ask for. Zero data retention is enterprise-only.
  - §2.3(b) bans training on Jev output, so the team could never distill its own model to get off Jev.
  - §2.2 and §2.3(a) are unclear about an API sold to other developers. It would need a written answer from TypeSafe.
  - New signups are paused as of 2026-09-22. OpenRouter still offers Jev, but I'd expect the same terms to apply.

## Reshape I tested: independent brand-safety checks for chat ads

OpenAI set the standard: no ads to under-18s, and none near health, mental health or politics. OpenAI's ads chief has called third-party measurement "a natural evolution." So advertisers will want independent proof that ads on other networks meet the same bar.

It is still weak:
- DoubleVerify is already rebuilding its brand-safety product around AI (June 2026). IAS and Scope3 are also in the space. Spider AF already sells fraud detection for ChatGPT ads.
- Networks are reluctant to share chat content with outsiders.
- The fees are small. Verification usually earns around 1–2% of ad spend (my estimate), which is about $50–100M a year on $5B.

## The strongest version: merge into entry 1

The real need is the suppression signal, not the ads. Operators face real legal exposure:
- California SB 243 has been in force since January 1, 2026. It requires self-harm protocols and protections for minors, and anyone injured can sue for $1,000 per violation.
- California's SB 1119, the Adam Raine bill, was just signed. It adds parental alerts when self-harm is detected and time limits for minors.
- In Congress, the CHATBOT Act would ban targeted ads to minors, and the GUARD Act has cleared the Senate Judiciary Committee.

So entry 1 could return one per-turn result: minor likely, crisis, and "eligible to monetize: yes/no, which ad categories." That gives it a cheap way to reach customers. Every AI ad network has to show advertisers it meets OpenAI's standard, so they could offer the check to their publishers. The pitch becomes "one layer that makes an AI app legally compliant and safe to monetize," instead of "yet another ad network."

The team should build it on open-weight models they fine-tune and host themselves, and treat Jev as an optional backend at most.

## What to test with real customers

1. Ask 10–15 founders of indie AI chat or companion apps: would you pay for compliance plus a "safe to monetize" signal, and how much per 1,000 turns?
2. Ask 3–5 AI ad networks (Koah, Gravity, Kontext and others): would you integrate or resell a third-party eligibility check, and do advertisers ask for one?
3. Ask 2–3 agency buyers whether independent proof of "no minors, no crisis conversations" would change how much they spend on non-ChatGPT inventory.

If the networks say they'll build it themselves and the apps won't pay, the ad angle adds nothing to entry 1.

Sources:
- [Jev on OpenRouter](https://openrouter.ai/docs/guides/community/jev)
- [Jev deep dive (pricing, latency, 255 options)](https://flaviocopes.com/jev/)
- [TypeSafe signup pause](https://aifront-page.com/typesafe-ai-pauses-jev-ai-model-signups-demand-surge/)
- [Koah Series A](https://siliconangle.com/2026/02/24/koah-raises-20-5m-scale-adsense-ai-across-apps/)
- [Gravity $30.5M](https://thenextweb.com/news/gravity-ai-ads-30-5m-series-a-agent-to-agent)
- [ZeroClick (AdExchanger)](https://www.adexchanger.com/commerce/honey-co-founder-ryan-hudson-has-a-new-plan-for-an-ai-ad-network/)
- [Top AI ad networks list](https://www.getchatads.com/blog/top-eleven-ad-networks-for-ai/)
- [Google AdSense in chatbots](https://searchengineland.com/google-test-ai-chatbot-chats-ads-454891)
- [ChatGPT ads pricing](https://topgrowthmarketing.com/how-much-do-chatgpt-ads-cost/)
- [OpenAI ads policy (Techmeme/Axios)](https://www.techmeme.com/260209/p35)
- [OpenAI on third-party measurement (Digiday)](https://digiday.com/marketing/openai-ads-boss-david-dugan-on-third-party-measurement-its-a-natural-step/)
- [DoubleVerify agentic brand safety](https://www.mediapost.com/publications/article/415878/doubleverify-makes-brand-safety-agentic-deploys.html)
- [Spider AF for ChatGPT ads](https://natlawreview.com/press-releases/spider-af-launches-ad-fraud-detection-chatgpt-ads-third-party-visibility-ai)
- [eMarketer forecast via PPC Land](https://ppc.land/emarketer-says-us-ai-ad-spend-hits-68bn-by-2030-and-chatgpt-misses-most-of-it/)
- [LLM pricing, Sept 2026](https://benchlm.ai/llm-pricing)
- [SB 243 (Jones Walker)](https://www.joneswalker.com/en/insights/blogs/ai-law-blog/ai-regulatory-update-californias-sb-243-mandates-companion-ai-safety-and-accoun.html)
- [California SB 1119 (CalMatters)](https://calmatters.org/economy/technology/2026/09/california-enacts-laws-restricting-chatbots-protecting-kids-online/)
- [Federal chatbot bills (MultiState)](https://www.multistate.us/insider/2026/4/30/state-childrens-online-safety-laws-expand-beyond-social-media-in-2026)