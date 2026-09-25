## Assessment: practitioner-sourced speech, video and robotics training data for AI labs

**Closest match.** The company whose pitch most nearly matches this one is **Datoric** (YC Summer 2026, two people, San Francisco). It sells licensed, consented speech, egocentric video, UMI and robot-teleoperation data, tactile-glove data and voice RLHF data to model teams. Each recording is linked to a consent record, and datasets ship with licensing documentation. It claims 300k+ contributors and "nearly seven figures in revenue" over one 30-day period. Its public pages don't show nine languages, the transcription and word-alignment benchmarks, the interrupt-trained voice environments, or practitioners as contributors. Its contributors look like crowd workers, not practitioners. So I treat it as probably this team, not a competitor, and I don't count its traction as proof of the practitioner premium. The only word-alignment benchmark I found is FA-Bench, run by **Olewave**, a speech-data vendor founded in 2015. Olewave sells only speech data, so it is not the whole pitch.

**Claims checked against sources**
- **Labs are short of this data.** Largely true. David AI, a speech-data specialist, raised $80M in 10 months, including a $50M Series B led by Meritech with NVIDIA in October 2025. DoorDash launched a Tasks app in March 2026 that pays couriers to record unscripted Spanish conversations and film chores. Mecka says it has signed contracts worth about a $100M annual run rate.
- **Web data doesn't cover it.** Partly true. Plain egocentric video is now almost free: Build AI released first-person factory video under Apache 2.0 at 100k hours, and reports say it reached about 1M hours by April 2026. Undifferentiated egocentric footage went from a few dollars an hour to roughly nothing. Teleoperation on a specific robot still sells for $50–200 an hour.
- **Crowd workers vs practitioners.** This is a real distinction, but others already claim it. nxted.ai recruits verified tradespeople, and Build AI and Cortex record factory and workplace workers.

**Who else serves this customer.** Scale, Surge, Mercor and Handshake are reported to hold more than 75% of roughly $8.5B in human-data revenue. That figure comes from a secondary source, a July 2026 X post by Deedy Das; I couldn't open it. In speech: David AI, Appen, Defined.ai and LXT. In robotics and egocentric data: Scale Physical AI, XDOF ($70M), Lightwheel (about $2B valuation), Mecka, Config, Human Archive ($8.2M), Build AI and Encord. DoorDash controls a supply channel of about 8M couriers.

**Does an incumbent own this customer?** No single incumbent owns the data or the buying channel. Labs buy from several vendors, project by project, which is how a two-person company could reach about $1M in a month. But the general vendors already hold the procurement relationships, and David AI is the default specialist for speech.

### 1. Strongest version
Start with voice and focus on live, human-in-the-loop voice environments rather than a catalog of recordings. The product is licensed, natural conversational speech in the nine languages, plus live full-duplex RL and evaluation environments staffed by people trained to interrupt, talk over the model and push back. The public transcription and word-alignment benchmarks bring customers in: publish where top models fail, then sell private evaluations and targeted collection to fix those failures.

The live environments are a recurring service that can't be scraped or released for free. That is why they beat footage. Keep robotics only as custom projects where scarcity still sets the price, such as teleoperation, tactile and hand-pose data from real tradespeople. Drop generic egocentric video, since its price has already gone to about zero.

### 2. Ratings
- **Customer need: 4.** David AI raised $80M in 10 months, DoorDash built a whole app for this supply, and Datoric reports nearly $1M of revenue in 30 days.
- **Value over what customers use today: 3.** Live interrupting humans and practitioner data fill a real gap, but I found no evidence that labs pay more for practitioner data than for crowd data from David AI, DoorDash or Scale.
- **Market size: 4.** Human-data spend is roughly $8.5B a year (secondary source). Mecka alone says it has about $100M a year in signed contracts. The speech and robotics slice is plausibly over $1B and growing.
- **Risk: 2.** The raw material is being commoditised (about 1M free hours from Build AI, 8M DoorDash couriers). Revenue will be lumpy, project-based and concentrated in a few labs, and synthetic voice data from companies like ElevenLabs could substitute.

### 3. What would kill it, and the fastest test
**What kills it:** labs won't pay a meaningful premium for practitioner or trained-interrupter data over crowd data. The price per hour then falls to crowd rates, and the company becomes one more commodity collection shop with a few concentrated customers.

**Fastest test:** build one sample package: about 20 hours of full-duplex calls with trained interrupters in two non-English languages, plus a public benchmark result showing where leading models fail. Take it to about 10 voice-model teams at labs and voice-AI companies. Ask for a paid pilot at 2x or more the crowd rate: at least $100 per hour, or a $25–50k environment pilot. If fewer than two sign within about four weeks, the premium isn't there. Everything above is desk research; only that test counts as customer validation.

VERDICT: BACK

Sources:
- [Datoric YC profile](https://www.ycombinator.com/companies/datoric), [Datoric Launch YC](https://www.ycombinator.com/launches/S9z-datoric-trustworthy-data-for-the-next-generation-of-models), [datoric.com licensing and provenance pages](https://www.datoric.com/licensing)
- [Olewave FA-Bench](https://www.olewave.com/en/news/fa-bench-evaluating-phone-and-word-level-timestamp-accuracy-in-forced-aligners/)
- [David AI $50M Series B (TFN)](https://techfundingnews.com/david-ai-raises-50m-series-b-audio-data-ai/), [Sacra on David AI](https://sacra.com/c/david-ai/)
- [TechCrunch on DoorDash Tasks](https://techcrunch.com/2026/03/19/doordash-launches-a-new-tasks-app-that-pays-couriers-to-submit-videos-to-train-ai/)
- [TechCrunch on Human Archive](https://techcrunch.com/2026/05/26/human-archive-taps-into-indias-services-startups-to-collect-data-for-physical-ai/)
- [DreamVu: robot training data landscape, 2026](https://www.dreamvu.ai/blog/robot-training-data-companies-2026)
- [Humanoids Daily on Build AI at 100k hours](https://www.humanoidsdaily.com/news/build-ai-scales-to-100-000-hours-as-data-scaling-becomes-robotics-new-frontier)
- [nxted.ai](https://nxted.ai/capture)
- [Deedy Das X post on AI training-data vendors](https://x.com/deedydas/status/2076124392711696455)
