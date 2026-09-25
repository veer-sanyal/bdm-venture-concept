I'm treating Perit AI (YC F26) as this team, not a competitor. Its site matches the pitch almost exactly. It lists the same nine locales, a transcription leaderboard and a word-alignment leaderboard, "live speech-to-speech calls with people trained to interrupt", and eight physical-data tracks (first-person video, depth, teleoperation, handheld gripper, hand pose, tactile and two more). It also says "consent on every file."

**Checking the key claims**
- **Nine languages: true.** German, French, Italian, Spanish, Brazilian Portuguese, Hindi, Mandarin, Korean and Japanese. All are widely spoken languages. Luel, a competitor, covers rare ones such as Tibetan, Darija and Dzongkha, where supply is actually short.
- **Output so far:** the site says 4,000+ hours of audio delivered. The physical-data tracks name no customers or case studies. The site claims SOC 2, ISO 27001 and HIPAA compliance; I could not verify any of these.
- **"Labeling marketplaces use crowd workers, not practitioners": false in 2026.**
  - micro1 (about $500M annualized revenue) sells video of "domain experts performing real-world tasks" in repair, assembly and logistics.
  - Luel ($31.2M seed, 500K+ contributors, $2M ARR) records skilled work such as gemstone carving, with signed consent records per item.
  - Human Archive ($8.2M seed) records cleaners and kitchen staff with tactile gloves and motion-capture suits.
  - Build AI released about 1M hours of factory-worker first-person video free for commercial use (Apache 2.0).
- **"Scraped web data doesn't cover it": only partly true.** Bulk first-person video now costs "a few dollars an hour" or is free. Teleoperated robot demonstrations ($50–200/hr) and tactile data are still scarce.
- **Benchmarks are not unique.** Perit's leaderboard ranks 22 models (Qwen first at 1.53% word error rate), but Perit runs it on its own data, so it isn't independent. Artificial Analysis, the Hugging Face Open ASR leaderboard and Olewave's FA-Bench already cover transcription and word timing.
- **Speech data is a commodity.** Nexdata, Datatang and Magic Data sell licensed multilingual two-way conversation recordings, including interruptions. Perit's own listed price of $20 per approved audio hour is commodity pricing.

**Does an incumbent own the customer or buying channel?** No one owns it outright. Labs spread purchases across vendors on purpose, especially since Meta's investment in Scale. But the expert-network vendors already hold the lab contracts and can add voice or physical data easily: Scale (customers include Physical Intelligence and Generalist), Surge, Mercor, micro1 and Luel. Big robotics companies such as Tesla and Figure also collect their own teleoperation data.

**1. Strongest version**
Drop the attempt to be a general data vendor across every format. Focus on human-run testing and training for real-time voice models that listen and speak at the same time (OpenAI's GPT-Live is one; the category is called full-duplex):
- live calls from trained callers who work in the relevant field (contact-centre QA leads, claims handlers, ward clerks), in the nine languages, set up to interrupt and talk over the model;
- private, unpublished test sets the labs can't have trained on;
- the public leaderboard used as the way to get in front of buyers.

Buyers would be roughly 20–30 voice-model teams (OpenAI, Google, ElevenLabs, Deepgram, AssemblyAI, Sesame, Qwen and others), then companies deploying voice agents. Physical data becomes optional custom work, because that market is crowded and prices are collapsing.

**2. Ratings for that version**

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Real-time voice models have shipped, and handling turn-taking and interruptions is still an open problem; at least 5 new 2026 benchmarks target it (Full-Duplex-Bench v3, HumDial and others). Each frontier lab reportedly spends about $1B a year on human-generated data. |
| Value over what customers use today | 2 | Licensed two-way conversation recordings (Datatang, Magic Data, Nexdata), audit-ready consent (Luel) and practitioner networks (micro1, Mercor) already exist. SpeechGym simulates callers at $0 API cost. |
| Market size | 3 | Data collection and labeling was about $4.9B in 2025 and robotics companies spend over $100M a year on real-world data. But the voice-model slice is a few dozen buyers. |
| Risk (5 = low) | 2 | Few buyers and commodity pricing ($20/hr audio; bulk first-person video now free). Better-funded vendors can copy this in weeks, and synthetic simulated callers compete directly with human ones. |

**3. What would kill it, and the fastest test**
It dies if voice labs treat human interruption calls and private test sets as an interchangeable commodity. Then they buy on price from Datatang or Luel, or use simulated callers, and won't pay a premium for practitioners.

Fastest test: in the next 3–4 weeks, offer 10 named voice-model teams a paid pilot of $25–50K. It would cover the live-call interruption setup plus a private test set in 2–3 of the languages, priced at 3x or more the commodity rate per hour.
- Kill it if fewer than 2 sign.
- If 3 or more sign, the voice wedge is real.

The idea's core claim, that current vendors use crowd workers rather than practitioners, is no longer true. Luel, micro1, Mercor and Human Archive already offer the practitioner, consent and multilingual angle, and the benchmarks and first-person video are commoditizing. The narrowed voice version is a real but small niche that the larger expert networks could copy quickly. There is money to be made here, but I don't see a lasting advantage.

VERDICT: PASS

Sources:
- [Perit homepage](https://perit.ai/), [Perit physical intelligence](https://perit.ai/physical-intelligence), [Perit STT leaderboard](https://perit.ai/research/benchmark/speech-to-text/leaderboard), [Perit pricing](https://perit.ai/pricing), [YC: Perit.AI](https://www.ycombinator.com/companies/peritai)
- [micro1 robotics](https://www.micro1.ai/data-engine/robotics), [MIT Tech Review on gig robot-data workers](https://www.technologyreview.com/2026/04/01/1134863/humanoid-data-training-gig-economy-2026-breakthrough-technology/)
- [Luel seed announcement](https://www.luel.ai/resources/blog/luel-seed-31m-general-catalyst-lightspeed), [StartupHub on Luel](https://www.startuphub.ai/ai-news/claudes-corner/2026/claudes-corner-luel-yc-w2026)
- [TechCrunch on Human Archive](https://techcrunch.com/2026/05/26/human-archive-taps-into-indias-services-startups-to-collect-data-for-physical-ai/), [Build AI Egocentric-10K on Hugging Face](https://huggingface.co/datasets/builddotai/Egocentric-10K), [Mike Kalil on Build AI](https://mikekalil.com/blog/build-ai-ecocentric-100k-dataset/)
- [DreamVu 2026 robot-data landscape](https://www.dreamvu.ai/blog/robot-training-data-companies-2026), [Scale AI physical AI](https://scale.com/blog/physical-ai)
- [Olewave FA-Bench](https://github.com/olewave/fa-bench/), [Artificial Analysis STT](https://artificialanalysis.ai/speech-to-text), [HF Open ASR Leaderboard](https://huggingface.co/spaces/hf-audio/open_asr_leaderboard)
- [Nexdata](https://www.nexdata.ai/), [Magic Data full-duplex corpora](https://magichub.com/large-scale-multilingual-full-duplex-conversational-speech-datasets-accelerating-voice-ai-industrialization-with-magic-data/)
- [SpeechGym](https://arxiv.org/pdf/2608.26432), [Full-Duplex-Bench-v3](https://arxiv.org/pdf/2604.04847)
- [TechCrunch on RL environments](https://techcrunch.com/2025/09/21/silicon-valley-bets-big-on-environments-to-train-ai-agents/), [HeroHunt labeling industry overview](https://www.herohunt.ai/blog/the-ultimate-ai-data-labeling-industry-overview/)
