## Live compliance checks on regulated sales calls: verdict and reshape

**Verdict:** As proposed, this is not a strong company: a per-seat product that watches human sales reps in real time, justified by Jev's low cost. The market is crowded, the product is already being bundled in for free, and the cost argument is wrong. The idea is strongest if you move the product to the AI agent's side of the call: check what an AI voice agent is about to say before the caller hears it, and keep a record that proves it for every call. Even that version has one serious risk (the voice-agent platforms building it themselves), and none of this is validated by customers yet. Everything below is desk research. I did not read the local project files, as you asked, although AGENTS.md says to read METHOD.md and STATE.md.

### What's wrong with the idea as proposed

1. **"Only Jev fits a $50–100 seat" is false.** Assume 72,000 checks per seat per month, each with a 1,500-token rulebook that can be cached plus 500 new tokens:

   | Model | Cost per seat per month |
   |---|---|
   | Jev ($0.042 per million tokens) | about $6 |
   | GPT-5 nano ($0.05, cached $0.005) | about $3 |
   | Gemini 2.5 Flash-Lite ($0.10) | about $5.50 |
   | GPT-5 mini | about $16 |

   The $70–100 figure only appears if you resend the whole transcript, uncached, every 5 seconds. Speech-to-text costs more than any of these: $15–46 per seat per channel at AssemblyAI's $0.15/hr or Deepgram's $0.29–0.46/hr.
2. **Compliance for human reps is already bundled or crowded.** AgentTech includes real-time compliance monitoring in a $50 seat that also covers the dialer and CRM. Balto, Sedric, Prodigal, Gryphon, Cresta and Observe.AI all already sell real-time disclosure checks.
3. **The "why now" doesn't match what the supplier allows.** The CMS action on 2026-08-31 cancelled about 315,000 *ACA Marketplace* policies tied to unauthorized broker enrollments. That is a problem of consent and identity, not of what reps say. It is also health data, and TypeSafe signs no BAA (HIPAA contract).
4. **Some of the supplier facts have shifted:**
   - The agreement was updated 2026-09-23. §4.3 now lets TypeSafe use telemetry (logs, hashes, statistics, metrics) "without restriction, including to improve the Services or TypeSafe's other products."
   - That wording matches the "capability" test in *Ambriz v. Google*. In February 2025 that court let a California wiretap (CIPA) claim proceed against an AI contact-center vendor because it *could* use call data to improve its own products.
   - Signups really are paused. But Jev is also on Vercel's AI Gateway (`typesafe-ai/jev`, same price), and Vercel lists TypeSafe as a zero-data-retention provider. Per-request zero data retention costs nothing extra on Vercel Pro, so "zero data retention is enterprise-only" doesn't hold on that route.
   - There is still no SLA and no BAA, TypeSafe can suspend immediately, and training a model on Jev's outputs is forbidden.

### The strongest version: a pre-speech compliance gate for AI voice agents

**Product.** A drop-in layer for teams that build their own agents on Retell, Vapi, LiveKit or Pipecat, in consumer lending, insurance and other telemarketing to consumers. It does three things:
- It checks every sentence the agent is about to say against a versioned rulebook of federal and state rules plus the client's own scripts. That covers TCPA caller identification at the start of the call, the telemarketing rule's ban on misrepresentation, AI-disclosure laws (California AB 2905, Utah, Maine), recording consent, and bans on guaranteed approval, unsupported rate quotes and false claims of government affiliation.
- It stops a violating sentence before speech and swaps in a pre-approved line. Jev can't write text, so replacements come from the approved script.
- It writes a record for every call of what was disclosed, when, and what was blocked, ready to hand to a regulator, a carrier or a court.

**Why this is a better fit than monitoring human reps:**
- The agent's words exist as text before they are spoken, so there is no speech-to-text cost on that side. The caller's side is transcribed by the voice platform anyway.
- The product can *prevent* a violation rather than nudge a rep after the fact.
- This is the one place where Jev's speed matters. Reported latency is 70–500 ms, mostly around 100 ms, which fits inside a voice agent's turn. A 1-second LLM does not.
- Only the agent's own words go to Jev. The consumer's words stay away from a supplier whose telemetry terms raise the CIPA problem above.

**Why now:**
- The FCC ruled in February 2024 that AI voices count as "artificial voice" under the TCPA, which means $500–1,500 per call.
- TCPA class actions hit a record 224 in September 2025, and AI-call suits have followed. *Cider* settled for $5.95M, and *Lowrey* names Twilio and OpenAI as defendants.
- Vapi handles about 62M calls a month and Retell about 50M.

**Pricing and economics.** Roughly $500 a month plus $0.01–0.02 per minute monitored. Jev costs about $0.001–0.002 per minute at around 10 checks a minute, so gross margins are high.

**Market (my rough estimates, not sourced).** Regulated calls to US consumers run to something like tens of billions of minutes a year. If 20% moves to AI by around 2030, that is about $130–260M a year at $0.01–0.02 a minute. You then grow into chat, SMS and email agents, into human reps, and into a dashboard for carriers and lenders who oversee many sellers. The part you could serve today is small, probably single-digit millions, so the pitch is a bet on AI voice growth: $4.8B in Q1 2026, forecast to grow about 42% a year.

**Competition and moat.**
- The biggest threat is platforms building it in. Retell shipped guardrails in February 2026, but with generic categories such as "regulated advice," not rules by industry and state.
- Testing and monitoring vendors (Hamming, Coval, Cekura) can extend into this.
- Sedric and Prodigal already score AI conversations for compliance. Vertical voice-AI vendors (Salient, Skit, Domu) build compliance in themselves.
- Your moat would have to be three things: rules for every state and industry, being an *independent* check that a compliance team trusts more than a vendor's own claim, and the per-call evidence record. None of that is proven.

**How to handle the supplier:**
- Build it so any model can be swapped in. Jev is the fast path, with a second path through Groq or a small model you host yourselves.
- Decide in advance, rule by rule, whether a timeout blocks the sentence (high-risk claims) or lets it through.
- Train your own model only on human-reviewed labels, never on Jev's outputs, and get a lawyer to check how that plays against §2.3(b).
- Sell it as an application with rulebooks and records, never as a raw classification API, which could count as offering Jev "as a standalone service."
- Leave health out until you have a model covered by a BAA.

**Main risks:** platforms absorbing the feature; false positives that block legitimate speech and ruin calls; added latency; liability if the gate misses something (sell it as "a control plus evidence," not as "compliant"); and a small market today.

### What to validate before the competition (desk research is not validation)
- Interview about 15 people who build voice agents for regulated clients and about 10 compliance officers at lenders, insurers or credit unions using AI voice agents. Local credit unions and Indianapolis insurers are close by.
- **Kill it if** most of them say their platform's guardrails are enough, or none will run a paid pilot at $0.01 a minute or more.
- **Proceed if** at least 3 will let you put the gate in front of a live agent, and it adds less than 150 ms at the 95th percentile with a false-block rate they accept.

### Sources
- [TypeSafe Master Customer Agreement](https://typesafe.ai/legal/mca)
- [TypeSafe signup pause (X)](https://x.com/typesafeai/status/2102281508950307159)
- [Jev specs (flaviocopes)](https://flaviocopes.com/jev/)
- [Jev access via Vercel (flaviocopes)](https://flaviocopes.com/jev-api-key/)
- [Vercel AI Gateway zero data retention](https://vercel.com/docs/ai-gateway/security-and-compliance/zdr)
- [CMS press release](https://www.cms.gov/newsroom/press-releases/cms-cracks-down-fraud-waste-abuse-federal-health-insurance-marketplacer)
- [Fierce Healthcare on the CMS cancellations](https://www.fiercehealthcare.com/regulatory/cms-cancel-aca-coverage-760k-crack-down-brokers-latest-anti-fraud-push)
- [Balto](https://www.balto.ai/blog/best-real-time-compliance-monitoring-software-for-contact-centers-2026/)
- [AgentTech](https://agenttech.io/solutions/ai-powered-dialer)
- [Sedric](https://www.sedric.ai/debt-collection)
- [Retell changelog](https://www.retellai.com/changelog)
- [Coval vs Cekura](https://www.coval.ai/blog/coval-vs-cekura)
- [Henson Legal on AI voice compliance](https://www.henson-legal.com/ai-voice-compliance)
- [Marshal state AI-disclosure table](https://marshalos.com/compliance/ai-disclosure-laws-by-state)
- [TCPA litigation statistics](https://www.leadgen-economy.com/blog/tcpa-litigation-statistics/)
- [Goodwin on Ambriz v. Google](https://www.goodwinlaw.com/en/insights/publications/2025/02/alerts-practices-dpc-ftec-ai-voice-products-subject-to-california-invasion-of-privacy-claims)
- [Voice AI statistics](https://www.ringly.io/blog/voice-ai-statistics-2026)
- [GPT-5 nano pricing](https://pricepertoken.com/pricing-page/model/openai-gpt-5-nano)
- [Gemini pricing](https://ai.google.dev/gemini-api/docs/pricing)
- [Deepgram pricing](https://www.happyrobot.ai/hub/deepgram-pricing)
- [AssemblyAI pricing](https://www.assemblyai.com/pricing)