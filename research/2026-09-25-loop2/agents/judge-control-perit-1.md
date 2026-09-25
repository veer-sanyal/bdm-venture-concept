I found the company. Perit AI (legal entity Zyno AI Inc, YC Fall 2026, founded 2026, 47 employees, San Francisco) matches the pitch almost exactly, so I treated it as this team. Some of the pitch holds up, but it is weaker than it reads. I did not read the repo's method or history files, because this brief was already the agent prompt and reading them could bias the judgement.

## Checking the claims against primary sources

| Claim | What I found |
|---|---|
| 650 transcribers and aligners, 9 languages, 4,000+ hours, about 50 hours a day | The numbers appear only on perit.ai and nowhere else. They add up to roughly 80 working days of output, which fits a 2026 start. The "bench" is freelancers paid per approved unit ($20 per approved audio hour for speech contributors), which is closer to a managed crowd than to staff. YC lists 47 employees. |
| Nine languages covering "exactly the cases models fail" | The nine are German, French, Italian, Spanish, Portuguese, Hindi, Chinese, Korean and Japanese. All are widely spoken and already have lots of training data. Any real edge is in accents, noisy rooms and support-call audio, not rare languages. |
| First-person video and teleoperation collection | Offered, but I found no evidence any has been delivered. The robotics page is all "we can collect" and "a pilot ships in two weeks". The 4,000 hours is speech only. |
| Transcription benchmarks | They exist: PERIT-STT and PERIT-ALIGN, 23 models from 12 providers, last run 2026-09-24. But Artificial Analysis already ranks 61 speech-to-text models, and AssemblyAI and Deepgram publish their own. Perit's only distinct angle is scoring word timing. |
| Speech-to-speech RL environments with trained interrupters | One line on the site ("Live speech-to-speech calls with people trained to interrupt") and no detail anywhere. Unproven. |
| Consent and licensing records | The default license is a non-exclusive perpetual license for internal model development; exclusivity costs extra. The site also shows SOC 2, ISO 27001/27701 and HIPAA badges with no auditor, dates or status, which is doubtful for a company founded this year. |
| Pricing | No per-hour price is published. Every project is custom-quoted within 48 hours. |

## Who else serves this customer

- **Speech data (direct incumbent): David AI.** Founded 2024 by two ex-Scale AI people, about $80M raised, $50M Series B from Meritech and NVIDIA in Oct 2025, eight-figure revenue run rate. It sells two-speaker conversations recorded on separate channels (Converse) and multilingual data in 15+ languages (Atlas). It says it serves leading speech-to-speech labs and most of the "Magnificent Seven" big tech companies. This is the specialist slot Perit would need.
- **Human data generalists:** Scale, Surge, Mercor and Handshake. One secondary source puts them at over 75% of vendor revenue. Surge already sells live-chat rating to labs. Mercor is around $2B gross run rate.
- **Robotics data:** Build AI (100k hours), Lightwheel (300k+ hours), Awign (1,000+ hours a day), plus Mecka ($8M raised), Claru, Luel, Objectways and Appen. One vendor-blog estimate puts a fully annotated 5,000-hour first-person video set at $150–200K, about $30–40 an hour, which makes it commodity work.

**Does an incumbent own the data or the buying channel?** Partly. Labs buy from several vendors, so the channel is not locked. But the specialist speech-vendor slot at labs and big tech is held by David AI, and the generalists already have the lab relationships for live human rating.

## 1. The strongest version

Drop robotics: Perit arrives late, has delivered nothing, and is up against collectors running 100k+ hours. Make it a speech company that finds where voice models fail and sells the data to fix it, for the roughly 20 teams building speech-to-speech and speech-recognition models: frontier labs, ElevenLabs, Deepgram, AssemblyAI, Sesame, Kyutai and similar.

- The wedge is live, interruption-heavy conversations between trained people and the customer's model, sold per session-hour as both an evaluation and an RL environment. Research papers say real two-way (full-duplex) conversation data is scarce and teams fall back on synthetic interruptions.
- The benchmarks become the sales tool.
- Word-level alignment and verifiable consent are the quality proof. Consent matters more after the April 2026 breach at Mercor, where about 3TB of voice recordings plus ID scans from about 40,000 contractors leaked.

## 2. Ratings for that version

- **Customer need: 4.** David AI reached an eight-figure run rate within about 18 months selling conversational audio to labs, and recent papers rely on synthetic interruption data because real data is scarce.
- **Value over what customers use today: 2.** David AI already sells two-speaker conversational data in 15+ languages and Surge already runs live rating. Word alignment and trained interrupters are features, not a new category, and the interruption product has no evidence of delivery.
- **Market size: 3.** Human data spend is billions, but speech is a thin slice (the category leader is at eight figures), the buyers are about 20 teams, and robotics data is priced as a commodity.
- **Risk: 2.** Buyers are few and work is project-by-project, there is a funded specialist incumbent, labs could generate interruptions synthetically instead, and most traction claims are self-reported (the compliance badges have no evidence behind them).

## 3. What would kill it, and the fastest test

**What kills it:** speech-to-speech teams say they already get conversational data from David AI or make interruptions synthetically, and won't pay extra for live human interruption sessions. What's left is commodity transcription at a crowd-vendor margin.

**Fastest test:** send the PERIT-STT and PERIT-ALIGN results to speech-model leads at 10 teams (labs plus ElevenLabs, Deepgram, AssemblyAI, Sesame and so on). Offer each a fixed-price, two-week pilot of about 100 hours of live interruption sessions. The bar is at least 2 signed paid purchase orders within 3 weeks, at a per-hour price above what they pay David AI. Nothing in this desk research counts as customer validation; only signed orders do.

Sources: [perit.ai](https://perit.ai/), [perit.ai/research](https://perit.ai/research), [perit.ai/pricing](https://perit.ai/pricing), [perit.ai/physical-intelligence](https://perit.ai/physical-intelligence), [perit.ai/about](https://perit.ai/about), [perit.ai/compliance](https://perit.ai/compliance), [YC profile](https://www.ycombinator.com/companies/peritai), [David AI](https://www.withdavid.ai/), [David AI Series B](https://techfundingnews.com/david-ai-raises-50m-series-b-audio-data-ai/), [Artificial Analysis speech-to-text leaderboard](https://artificialanalysis.ai/speech-to-text/non-streaming), [Pebblous on market concentration](https://blog.pebblous.ai/blog/ai-data-supply-oligopoly/en/), [Mercor revenue](https://finance.biggo.com/news/865c23cb-3e0d-4c21-aa0d-6bf2a7fc8d1a), [Mercor breach](https://blog.rdcl.is/2026/04/30/tb-of-voice-samples-were.html), [first-person video providers](https://www.labellerr.com/blog/top-egocentric-data-providers-robotics/), [first-person video pricing](https://unidata.pro/blog/egocentric-data-collection-for-robot-training/), [Mecka AI](https://www.upstartsmedia.com/p/mecka-ai-robotics-data-startup), [FLEXI full-duplex benchmark](https://arxiv.org/pdf/2509.22243)

VERDICT: PASS
