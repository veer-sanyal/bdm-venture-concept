I'd back a narrower version of this company: a voice-first data vendor. The data would be phone and full-duplex conversations recorded by people who actually do the job, in languages other than English, sold with live "caller who interrupts" training environments. Robotics data would come later, as an expansion. The pitch as written is broad, and the robotics-video half of it is already commoditising.

**Who this is.** The pitch matches Perit.AI (YC F26) almost exactly, so I treated it as this team. Its site lists nine locales, speech, first-person video, depth, teleoperation, gripper demos, hand pose and tactile data. It also lists transcription and word-alignment benchmarks and "live speech-to-speech calls with people trained to interrupt" ([perit.ai](https://perit.ai/), [YC page](https://www.ycombinator.com/companies/peritai)). I followed METHOD.md's blind-judge rule and did not read the other project files.

**Checking the key claims against primary sources:**
- **Confirmed:**
  - The nine locales are listed: DE, FR, IT, ES, PT-BR, HI, ZH, KO, JA.
  - Its stated volume is 4,000+ audio hours delivered, 50 hours a day, and 650+ transcribers and aligners.
  - Each recording carries its own consent, stored with the file. The standard licence is perpetual and non-exclusive, with exclusive terms on request ([request-data](https://perit.ai/request-data)).
- **Weaker than pitched:**
  - **Benchmarks are English only.** The alignment leaderboard is led by Perit's own fine-tuned model, which is a conflict of interest ([benchmarks](https://perit.ai/benchmarks)).
  - **Little public detail on the voice environments.** They get one line on the site.
  - **No customers are named.** The SOC 2, ISO and HIPAA badges are logos on the site, not audit reports.
- **"Practitioners, not crowd workers" doesn't hold up:**
  - Scale, Surge, Mercor, Handshake and micro1 all sell expert networks.
  - Perit's own contributors pick tasks on their own devices and are paid per approved task, which is a crowd-style model.
  - The practitioner claim is real in one place: its benchmark graders "worked the desk the call came from."
- **Price:** Perit lists speech at $20 per approved hour. Documented off-the-shelf conversational speech sells for about $60–95 an hour ([SpeechData.ai](https://www.speechdata.ai/guides/how-to-buy-speech-data)). That gap is a cost edge, and it is also a sign the product is a commodity.

**Who else serves this customer:**
- **The big four:** Scale, Surge, Mercor and Handshake take more than 75% of training-data and RL-environment revenue ([Pebblous](https://blog.pebblous.ai/blog/ai-data-supply-oligopoly/en/)). micro1 is at a $500M gross run rate ([TechCrunch](https://techcrunch.com/2026/08/20/ai-data-startup-micro1-reaches-500m-gross-run-rate-amid-ai-training-boom/)).
- **Robotics data, including first-person video:**
  - Scale names Physical Intelligence, Generalist and Cobot as robotics customers ([DreamVu](https://www.dreamvu.ai/blog/robot-training-data-companies-2026)).
  - Human Archive raised $8.2M and has headsets, tactile gloves and motion-capture suits ([TechCrunch](https://techcrunch.com/2026/05/26/human-archive-taps-into-indias-services-startups-to-collect-data-for-physical-ai/)).
  - Build AI released 100k+ hours of open factory footage.
  - Others include Claru, Shaip, iMerit, Egolab and Objectways.
  - DoorDash pays its 8M US couriers to film chores and record Spanish conversations ([TechCrunch](https://techcrunch.com/2026/03/19/doordash-launches-a-new-tasks-app-that-pays-couriers-to-submit-videos-to-train-ai/)).
- **Commoditisation:** Stellaris says entry barriers are low and expects 30–50 vendors to shrink to 5–10 ([Stellaris](https://www.stellarisvp.com/blog/physical-ai-has-a-massive-data-problem)).

**Does an incumbent own the channel?** Partly. The big four hold the master contracts with the labs, but labs buy from several vendors at once. Purchases run campaign by campaign, often starting with a pilot. Labs also drop vendors: Meta paused work with Mercor after its data breach. That leaves room for a specialist, but not for someone selling the same thing as the big four.

## 1. Strongest version
A human-data vendor for voice models, built on real conversations recorded by working operators:
- **Recordings:** support agents, clinic front desks, dispatchers and similar roles, in the nine current locales and more.
- **Training environments:** paid, trained people talk over the model live, and each exchange is scored by graders who have done the job.
- **Benchmarks:** a multilingual transcription and word-alignment leaderboard, independently run, used to win customers.

Full-duplex voice is a new frontier for the labs. Examples are OpenAI's GPT-Live and Sierra's τ-voice benchmark ([Sierra](https://sierra.ai/blog/tau-voice-benchmarking-real-time-voice-agents-on-real-world-tasks)). Live human interruption is hard to fake with synthetic data. The same recruiting and consent operation can later expand into robotics data for specific trades, rather than generic household video.

## 2. Ratings (for that version)
| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Sean Cai says labs "still don't have enough good quality data vendors" ([MTS](https://x.com/MTSlive/status/2060447529133867339)). Voice benchmarks now explicitly test overlap and interruption ([τ-Voice](https://arxiv.org/html/2603.13686v1)). |
| Value over what customers use today | 3 | Perit is 3–5x cheaper than market speech data ($20 vs $60–95 an hour). But the big four already sell expert networks, so the practitioner edge is only proven in grading. |
| Market size | 4 | Each frontier lab reportedly spends about $1B a year on human-generated training data. micro1 went from $100M to $500M run rate in 8 months. The voice slice has no public figure, which is the soft spot. |
| Risk (5 = low) | 2 | Buyers are concentrated: 91% of Mercor's revenue comes from foundation-model labs ([BigGo](https://finance.biggo.com/news/865c23cb-3e0d-4c21-aa0d-6bf2a7fc8d1a)). Barriers to entry are low, and the big four can add voice cheaply. |

Total: 13 out of 20.

## 3. What would kill it, and the fastest test
**Killer:** Labs won't pay more for practitioner or interruption data than for native-speaker crowd audio. Speech then trades at the price floor, and Perit becomes an Indian cost-arbitrage vendor selling against Scale, micro1 and DoorDash with no moat.

**Fastest test:** Pitch the paid interruption environment plus practitioner call data in one non-English locale to about 8 voice teams (OpenAI, Google, Meta, xAI, ElevenLabs, Sesame, Kyutai, Cartesia). Ask at least $60 an hour, three times Perit's list price, for a 5% pilot. If two or more sign paid pilots within four weeks, labs will pay a premium. If they only buy at $20, it's a commodity.

**Why back:** Competition alone doesn't sink it, and the category keeps producing very large outcomes. The voice-first wedge is concrete, the unit costs are low, and the team already runs the operation at volume. The main risk is commoditisation, and the four-week pilot test above checks it directly.

VERDICT: BACK
