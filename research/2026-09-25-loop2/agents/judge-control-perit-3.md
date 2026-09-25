**Pitch match:** Perit AI (YC F26, perit.ai) makes this exact pitch, down to the numbers. Its site says 4,000+ audio hours delivered, 650 transcribers and aligners (250 + 400), 9 locales (DE, FR, IT, ES, PT, HI, ZH, KO, JA), 50 hours delivered each working day, and "95%+ QA-sample accuracy". It also lists live speech-to-speech RL environments, published speech-to-text and word-alignment leaderboards, and robot data services (egocentric video, teleoperation, UMI gripper, tactile, bring-your-own-rig). As you instructed, I treat Perit as this team, not as a competitor.

## Claim check against primary sources
- **Operating numbers:** Perit's own site states all of them. Nobody independent confirms them. 4,000 hours at 50 hours a day is about 80 working days, so the speech line is only a few months old at this rate.
- **"$20 per audio hour" is not the customer price.** It is what contributors are paid. Customer prices are quoted per project (the pricing page lists locale, annotation depth, turnaround and exclusivity as the drivers). The "per delivered hour" model is real, but no public price exists to size margins from.
- **Revenue:** a search snippet attributed to Perit's YC or LinkedIn profile says "works with six major AI labs… multiple millions in ARR". The YC page I fetched did not show this. Treat it as unverified.
- **Certifications:** the site shows SOC 2 Type II, ISO 27001 and 27701, and TPN Gold badges. For a company founded in 2026 that is implausibly fast, because a Type II audit needs a months-long observation period. Diligence should ask for the actual reports.
- **Benchmark:** 22 speech-to-text models ranked on held-out audio (the top result is Qwen3-ASR at 1.53% word error rate). Hugging Face's Open ASR leaderboard and Artificial Analysis already publish similar rankings, so this works as lead generation, not as a product.
- **Voice RL environments:** customers point their model at the environment over a websocket. Real people play scenarios across 10 sectors and 6 scenario families ("interrupted mid-answer", "bad line" and so on). Scoring covers task success, p95 latency and recovery after the user barges in. No customers are named.

## Who else serves this customer
- **Speech data: David AI** (Scale alumni, YC). About $80M raised, including a $50M Series B led by Meritech and NVIDIA. It reports an eight-figure revenue run rate and sells to "leading AI labs and several Mag 7" companies. It offers two-speaker channel-separated conversations and 15+ languages, off-the-shelf or custom. This is the closest competitor, and it is ahead.
- **General human data: Scale, Surge, Mercor, Handshake.** They take over 75% of spending on this kind of data. Mercor reports a gross run rate above $2B and Handshake above $1B.
- **Custom speech collection:** Appen, LXT, Shaip, Defined.ai.
- **Egocentric and robot data:** Human Archive (YC W26), Luel (YC), Datoric and many others. Build AI released Egocentric-1M, a million hours under Apache 2.0, free for commercial use. Generic first-person video is becoming a commodity.

**Does an incumbent own the channel?** No single incumbent owns this customer's data or buying channel. The large vendors hold the master contracts and most of the budget, and David AI owns the "audio data vendor" slot at labs. But labs buy from many vendors: Anthropic reportedly uses more than a dozen for RL environments. Perit's line "No frontier lab owns a piece of Perit" is a real angle after Meta took 49% of Scale. That comes from my own background knowledge; I did not re-check it in this research.

## 1. The strongest version
Drop generic egocentric video; that market is flooded and partly free. Keep robotics only as crew-for-hire on the customer's own rigs (bring-your-own-rig, teleoperation, tactile).

The strongest version is a neutral vendor of speech failure cases and live conversational RL for voice models. It has two parts:
- **Recurring live-duplex evaluation and RL.** Trained people interrupt, change their mind and call over bad lines, and every model checkpoint is run through it. This is the part synthetic data and pre-recorded datasets cannot copy. Demand is rising: OpenAI launched GPT-Live in July 2026 to handle turn-taking, and recent arXiv papers study how full-duplex models fail under interruption (DuplexJail, FLEXI).
- **Targeted collection and transcription in scarce locales, with word-level timing and consent attached to every item.** This is the cash engine. The benchmark stays a lead-generation tool.

## 2. Ratings
| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | David AI reached an eight-figure run rate within about a year selling audio to labs and Mag 7 companies, and full-duplex voice went mass-market with GPT-Live in July 2026. |
| Value over today | 3 | Consent and quality reports on every delivery are now standard (David AI, Luel and Datoric all offer them). Only the live human interruption environment is clearly different. |
| Market size | 4 | Human data spending is about $10B a year and growing over 50% a year. Audio and robotics are a slice of that, but a slice worth hundreds of millions. |
| Risk (5 = low) | 2 | Services-heavy business with low margins, dependent on a handful of lab buyers, facing a well-funded direct competitor (David AI) and possible replacement by synthetic self-play. |

## 3. What kills it, and the fastest test
**What kills it:** labs decide live human duplex sessions are not worth paying for, or not worth paying for again. Two ways this happens:
- Synthetic interruption and self-play gets good enough, or the labs build the environment in-house.
- Speech collection then drifts into a per-hour price war with David AI and the large vendors. Without a differentiated product, this is a services business with no moat.

**Fastest test:** offer the live-duplex environment to about 6 voice teams (OpenAI, Google, Meta, xAI, Mistral or Kyutai, ElevenLabs or Sesame) as a paid one-week pilot on their current checkpoint. Success means at least 2 pay and at least 1 re-orders on its next checkpoint within 30 days. Do not count sales of collected hours toward this test: those only show demand for the commodity side.

**Bottom line:** the demand is proven by others, and the market has room for another neutral voice data vendor. My backing depends on the live-environment wedge passing the test above. Desk research is not customer validation; that pilot is what gives it.

Sources: [Perit homepage](https://perit.ai/), [Perit pricing](https://perit.ai/pricing), [Perit RL environments](https://perit.ai/rl-environments), [Perit STT leaderboard](https://perit.ai/research/benchmark/speech-to-text/leaderboard), [Perit compliance](https://perit.ai/compliance), [YC: Perit.AI](https://www.ycombinator.com/companies/peritai), [David AI Series B](https://techfundingnews.com/david-ai-raises-50m-series-b-audio-data-ai/), [David AI](https://www.withdavid.ai/), [Pebblous: vendor concentration](https://blog.pebblous.ai/blog/ai-data-supply-oligopoly/en/), [Mercor run rate](https://app.dealroom.co/news/note/mercor-doubles-to-2b-gross-revenue-run-rate-as-ai-labs-buy-expert-data), [Handshake ARR](https://app.dealroom.co/news/note/handshake-s-arr-crosses-1b-as-ai-training-revenue-surges), [Human Archive, TechCrunch](https://techcrunch.com/2026/05/26/human-archive-taps-into-indias-services-startups-to-collect-data-for-physical-ai/), [Egocentric providers](https://www.labellerr.com/blog/top-egocentric-data-providers-robotics/), [OpenAI GPT-Live, TechCrunch](https://techcrunch.com/2026/07/08/openai-releases-new-voice-models-for-more-natural-live-conversations/), [DuplexJail](https://arxiv.org/pdf/2609.09420), [FLEXI](https://arxiv.org/pdf/2509.22243), [Artificial Analysis STT](https://artificialanalysis.ai/speech-to-text/non-streaming)

VERDICT: BACK
