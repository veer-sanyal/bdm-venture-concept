I could not find this company in public sources. No site, dataset, press item or benchmark matches the pitch (650 people, nine languages, 4,000 hours, speech-to-speech RL environments plus robotics collection), so none of its operating claims could be checked against a primary source. The closest companies each match only one part: David AI (licensed speech data for AI labs), oto (full-duplex speech data) and XDOF (robot teleoperation data). I treated all three as competitors, not as this team.

**Checking the claims**
- **The 650-person bench is really a part-time crowd.** 50 hours a day from 650 people is about 5 minutes of audio per person per day. Word-level transcription takes roughly 6–10 times real time, which puts actual labor at about 40–60 full-time people. That looks like a managed crowd, which is weak ground for "better than crowd marketplaces."
- **The business is small today.** Licensed conversational speech lists at $60–95 per hour ([SpeechData.ai](https://www.speechdata.ai/datasets/english-usa)). At that price, 4,000 hours is about $0.24–0.38M of lifetime revenue, and 50 hours a day is roughly $1.1–1.7M a year. For comparison, David AI raised $80M, reports more than $8M in annual revenue, and says it sells to "most of the leading AI labs" ([David AI](https://www.withdavid.ai/news/announcing-our-50m-series-b), [JustAINews](https://justainews.com/applications/voice-and-speech-recognition/david-ai-lands-50m-series-b-to-power-real-world-audio-ai/)). XDOF is approaching $50M a year with 20 customers ([TechCrunch](https://techcrunch.com/2026/09/04/xdof-just-three-months-out-of-stealth-is-in-talks-for-a-series-b-at-a-1-2b-valuation/)).
- **Plain transcription is being automated.** Meta's Muse Voice Transcribe costs $0.18 per audio hour at 3.1% word error rate ([VentureBeat](https://venturebeat.com/technology/meta-prices-muse-voice-transcribe-at-0-18-an-hour-with-real-time-diarization-for-20-speakers-a-steal-for-enterprises)). Human labor only earns its price on hard cases.
- **The benchmark gap is real.** The main public transcription leaderboard tests English only and does not measure word-level timing ([Artificial Analysis](https://artificialanalysis.ai/speech-to-text/streaming)).
- **Consent now has real value.** In May 2026, voice-data class actions under Illinois' biometric privacy law were filed against Apple, Amazon, Meta, Microsoft, Nvidia, Samsung, Alphabet, Adobe and ElevenLabs ([Sigma Law](https://sigmalawgroup.com/blog/2026-08-22-bipa-voiceprint-ai/)).

**Who else serves this customer, and whether anyone owns the channel**
- **Speech:** Scale already sells full-duplex collection, multilingual coverage, voice preference ranking by human raters, trained voice actors and red-teaming ([Scale](https://scale.com/blog/not-in-text-alone)). Other sellers are David AI, oto ([oto.earth](https://www.oto.earth/)), Abaka, Appen, Defined.ai, Shaip and SpeechData.ai.
- **Robotics:** XDOF, Scale, micro1, Mecka, Encord, Claru, Luel, Awign and truelabel. Generic first-person video is flooding the market. Build AI released a large factory video dataset free for commercial use under Apache 2.0 ([Labellerr](https://www.labellerr.com/blog/egocentric-datasets-robotics/)). One trade blog reports raw footage trading at $2–5 per hour.
- **The channel:** It is not locked, because labs buy from several vendors. But one secondary source says over 75% of training-data spend goes to Scale, Surge, Mercor and Handshake ([Pebblous](https://blog.pebblous.ai/blog/ai-data-supply-oligopoly/en/)). The specialist speech slot at the labs is largely held by David AI.

**1. Strongest version**
Drop robotics. It is a different operation, the market is flooded with footage, and XDOF, micro1 and Scale are far ahead. What remains is a multilingual speech lab focused on where models fail:
- **Wedge:** a public benchmark that covers the gaps above: nine languages, word-level timing, code-switching, overlapping speech and interruptions. It shows each lab exactly where its model breaks.
- **What it sells:** targeted consented collection for those failures, plus paid sessions where trained native speakers interrupt and stress-test a lab's speech-to-speech model.
- **Pricing:** per delivered hour, plus per-program fees for the live sessions.
- **Timing:** full-duplex voice models have just shipped (OpenAI's GPT-Live in July 2026, with an API in September), and the lawsuits make provenance a selling point.

**2. Ratings**
| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Full-duplex voice models are shipping, and the May 2026 lawsuits push labs toward consented voice data. |
| Value over what customers use today | 2 | Scale already sells full-duplex data, voice feedback and trained voice actors. David AI sells to most labs. "Quality report plus consent records" is standard in vendor marketing. |
| Market size | 3 | Total lab data spend is in the billions (Mercor alone passed $2B a year: [BigGo](https://finance.biggo.com/news/865c23cb-3e0d-4c21-aa0d-6bf2a7fc8d1a)), but speech is a slice. The leading speech specialist reports only about $8M a year, from roughly 20–30 speech-to-speech buyers. |
| Risk (5 = low) | 2 | Transcription costs $0.18 per hour and falling. Simulated users may replace human interrupters. The team is about 1/50 the size of the specialist it competes with. |

**3. What would kill it, and the fastest test**
It dies if labs will not pay a premium for live human interrupter sessions and failure-case data in these languages, because simulated users, Scale or David AI are good enough.

The fastest test is direct outreach:
- Run the benchmark on 3–4 named speech-to-speech models.
- Send each lab's voice post-training lead a pack of that lab's own failure clips.
- Attach a fixed-price pilot of about $30–50K for 100 hours of live interrupter sessions in their weakest language.
- Contact about 10 labs over 3 weeks. Two or more signed paid pilots means continue. Zero, or "we get this from Scale or David," means kill.

That outreach would be the first customer evidence. Everything above is desk research, which is not customer validation.

The need is real, but the specialist slot is held by a well-funded company, basic transcription is being automated, and the robotics half is flooded with cheap footage. What is left is a thin wedge with no shown advantage over existing vendors.

VERDICT: PASS
