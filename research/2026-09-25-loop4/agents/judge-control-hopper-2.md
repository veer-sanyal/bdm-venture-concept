**Who this is.** The pitch matches **Hopper** (withhopper.com, YC 2026) almost word for word: "post-trains STT, TTS, and speech LLMs on your production calls, then serves and improves them against your live traffic." So I treat Hopper as this team. Its site lists no customer names. The founders come from voice inference at Salient and inference kernels at Meta Reality Labs. As you asked, I did not read any local project files.

**How the headline claims hold up against primary sources**
- **"80 ms vs 600 ms for GPT-4.1":** The 80 ms figure is for **Gemma 4 31B**, an open model served on dedicated capacity. It is not a model post-trained on a customer's calls. Hopper's own blog measured GPT-4.1 at about 510–600 ms with a standard client, and 197–319 ms with Hopper's own client. Artificial Analysis puts GPT-4.1 at about 0.92–1.09 s, so the 600 ms number is fair to OpenAI. But the comparison sets a dedicated small open model against a shared frontier API. Baseten or Together could match it with a dedicated deployment.
- **"$0.50 vs $2 per million input tokens":** The $2 list price is correct. But **GPT-4.1's cached input is also $0.50**, and voice agents resend the same system prompt every turn, so a lot of their input hits the cache. The same Gemma 4 31B costs **$0.20 on Together and $0.09 on DeepInfra**, so Hopper charges a premium over commodity prices. Smaller API models are cheaper still: GPT-4.1-mini is $0.40, GPT-4.1-nano $0.10, Gemini 2.5 Flash-Lite about $0.10.
- **The real value is the post-training, not the headline numbers.** Adapting speech recognition to a domain clearly helps. One contact-center paper cut character error rate from 23.3% to 9.0% on general telephony and from 17.0% to 3.8% on domain terms. Hopper has published no such lift of its own.

**Who else serves this customer**
- **Inference clouds:** Baseten (about $600M run-rate, $13B valuation, building multi-model voice infrastructure and fine-tuning Qwen3-TTS), Together (speech-to-text, LLM and speech synthesis hosted together, under 500 ms end to end, Deepgram and Cartesia on its platform), Fireworks (reinforcement fine-tuning plus a voice-agent stack), and CoreWeave, which bought OpenPipe.
- **Speech vendors:** Deepgram (custom-trained models for enterprise customers), Cartesia, ElevenLabs, and speech-to-speech models such as OpenAI's gpt-realtime-mini.
- **Voice platforms that do it themselves:** PolyAI (its own Raven model and Dialog-RSN-1), Bland (runs everything on its own servers and GPUs), Retell (offers fine-tuning on call transcripts), Vogent (models fine-tuned on phone calls).
- **Who owns the data and the buying channel:** The call recordings sit with the voice-AI platforms (Retell, Vapi, Bland, PolyAI) and with contact-center software vendors (NICE, Genesys, Five9). GPU spend is bought through the inference clouds, and model choice often runs through LiveKit Inference. Hopper has to sell to the people who own the data, and the biggest of them are already building this in-house.

**1. Strongest version**
A done-for-you closed loop for **mid-sized voice-AI platforms and vertical voice-agent companies** (for example auto lending, healthcare intake, logistics). These run roughly 1–20 million minutes a month: too big to ignore margins, too small to staff a speech-ML team. Hopper would:
- Start with speech recognition and the language model, where gains show up in measurable ways: names, account numbers, addresses, and task completion on narrow call flows. Speech synthesis is the weakest differentiator and can come later.
- Retrain continuously on call outcomes and serve all three models side by side under a latency guarantee.
- Price per minute, with part of the fee tied to measured gains, instead of competing on price per token.

**2. Ratings for that version**
| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | Bland built "self-hosted everything" to get under 400 ms and $0.09 a minute, and PolyAI built its own model. The pain is real enough that scaled players spend engineering on it. |
| Value over what customers use today | 3 | Domain tuning cuts error rates by 60–78% in the literature, but Hopper's own headline numbers are an unfair comparison, and the same base model is 2.5–5× cheaper elsewhere. |
| Market size | 3 | Volume is large (Retell has about 50M calls a month, Vapi 1B calls cumulative, ElevenLabs over $500M ARR). But model spend is only about $0.02–0.07 a minute, and Hopper's pitch shrinks it further. This is my own rough estimate. |
| Risk (5 = low) | 2 | The largest data owners do this in-house, well-funded inference clouds already sell fine-tuning plus serving, and the standalone post-training companies OpenPipe and Predibase ended in acquisitions. |

**3. What would kill it, and the fastest test**
- **Kill:** Post-training on a customer's own calls gives no lasting improvement in task completion or error rate over plain Gemma or Qwen served cheaply on Together or Baseten. Hopper would then be reselling commodity inference at a markup, into a market where the largest customers build their own.
- **Fastest test (2–4 weeks):** Take 3 mid-sized voice platforms with about 1,000 labeled production calls each. In shadow mode, run Hopper's post-trained stack against both the customer's current stack and vanilla Gemma 4 31B on Together. Measure error rate on key details, task completion, 95th-percentile end-to-end latency, and cost per minute. Success means at least one customer signs a **paid commitment to move 10% or more of live traffic**. Without that, pass. So far this is all desk research; none of it validates demand from customers.

**Bottom line:** The need is real, but the difference over inference clouds that already bundle fine-tuning and serving is thin. The headline numbers mostly show the speed and price of serving an open model rather than any benefit from training on the customer's calls. And the customers who own the most data are building this themselves. Competition alone is not why I pass; I pass because the thing that would set Hopper apart, lasting gains from each customer's own calls, is unproven.

Sources:
- [Hopper home](https://withhopper.com/)
- [Hopper LLM client blog](https://withhopper.com/blog/llm-client-voice-agents)
- [OpenAI pricing](https://developers.openai.com/api/docs/pricing)
- [Artificial Analysis GPT-4.1](https://artificialanalysis.ai/models/gpt-4-1/providers)
- [Artificial Analysis Gemma 4 31B](https://artificialanalysis.ai/models/gemma-4-31b/providers)
- [Together Gemma 4 31B](https://www.together.ai/models/gemma-4-31b)
- [DeepInfra Gemma 4 pricing](https://deepinfra.com/blog/gemma-4-pricing-benchmarks-cost-scenarios)
- [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Domain-adaptive ASR for telephony (arXiv 2608.24916)](https://arxiv.org/pdf/2608.24916)
- [Baseten TTS](https://www.baseten.co/solutions/text-to-speech/)
- [Baseten Qwen3-TTS](https://www.baseten.co/blog/cost-efficient-high-performance-qwen3-tts/)
- [Together Voice](https://www.together.ai/solutions/voice)
- [Fireworks RFT](https://fireworks.ai/blog/fireworks-rft)
- [CoreWeave acquires OpenPipe](https://www.coreweave.com/news/coreweave-to-acquire-openpipe-leader-in-reinforcement-learning)
- [Deepgram model docs](https://developers.deepgram.com/docs/model)
- [PolyAI Raven v2](https://poly.ai/blog/polyai-raven-v2-large-language-model)
- [Bland self-hosted](https://www.bland.ai/blogs/api-wrappers-vs-self-hosted-ai-voice-whats-best-for-enterprises)
- [Retell $50M ARR](https://app.dealroom.co/news/feed/retell-ai-reaches-50m-arr-powers-50m-monthly-calls-as-voice-ai-trend-gains-momentum)
- [Vapi Series B](https://www.globenewswire.com/news-release/2026/05/12/3292882/0/en/vapi-raises-50m-series-b-as-it-reaches-1-billion-calls-powering-the-next-generation-of-enterprise-voice-ai.html)
- [Vogent](https://www.vogent.ai/)
- [LiveKit Inference](https://livekit.com/blog/introducing-livekit-inference)
- [gpt-realtime-mini pricing](https://www.eesel.ai/blog/gpt-realtime-mini-pricing)

VERDICT: PASS
