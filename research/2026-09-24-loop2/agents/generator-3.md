I didn't read any local project files, as you asked, so METHOD.md and STATE.md played no part in this. Everything below is desk research, which isn't customer validation.

**What Jev is really good for.** Independent tests show Jev is 40–400x cheaper than frontier models but only about 4x cheaper than GPT‑5.6 Luna and about 12x cheaper than Haiku 4.5, and a fine‑tuned small classifier is cheaper still. Jev's real edge is somewhere else:
- it answers dozens of questions in one pass, fast;
- it gives probabilities that can be calibrated;
- it takes new questions without any training data.

So it makes a company possible only where the work is **continuous, many questions per event, fast, with rules that keep changing and few labels**. Four more filters shaped the list:
- **Avoid text written by an attacker.** Injected text in the state shifts Jev's answers.
- **Avoid health data.** TypeSafe won't sign a BAA (the agreement HIPAA requires for health data), and all processing is in the US.
- **Price on outcomes, not per judgment.** At $17 per million decisions, per‑judgment revenue is tiny.
- **Check what the real bottleneck is.** Often it's data or trust, not the cost of judging.

## Best idea: a safety and compliance check on every turn of consumer AI chat

**What it is.** An API that sits beside AI companion, character, wellness and teen‑facing chat apps. On every turn, one Jev call asks 25–40 typed questions:
- **About the user:** clinician‑style suicide‑risk items and a graded severity scale, self‑harm, eating‑disorder cues, signs the user is a minor, and whether it's role‑play.
- **About the bot:** claiming to be human or a licensed therapist, sexual content with a likely minor, guilt‑tripping the user to stay, giving method information, and whether a required crisis referral was actually given.

A rules engine for each state turns the probabilities into actions:
- add a 988 crisis‑line referral, swap the reply, or show a break reminder;
- send the rare risky turn to a frontier LLM and a human;
- keep an audit trail and generate required reports, such as California's annual report to its Office of Suicide Prevention, due from 1 July 2027.

**Customer need.** About ten states now require suicidal‑ideation detection, crisis referral and protections for minors:
- New York's law has been in force since November 2025.
- California's (SB 243) took effect in January 2026 and requires "evidence‑based methods". Anyone injured can sue for at least $1,000 per violation.
- Tennessee's took effect July 2026 and allows $5,000 per violation.
- Oregon's and Washington's start January 2027, and both let individuals sue.
- Idaho and Nebraska follow in July 2027.

Many of these apps run open‑weight models with no safety layer at all.

**Why only Jev makes this practical.**
- The checks run alongside the bot's reply in about 0.25–0.5 s.
- Real risk shows up in very few turns, so sending the uncertain ones to an LLM gets LLM quality at close to Jev cost. Independent tests found this at a quarter to half the cost.
- Checklist‑style clinical items suit the "split one judgment into small questions" pattern that lifted one task from 63% to 95%.
- New or changed state rules are new questions, not retraining.

**Value over alternatives.**
- Standard moderation APIs flag rule‑breaking reliably (F1 0.86) but grade severity badly: macro‑F1 0.395. Clinical framing lifts that to 0.562.
- OpenAI's free gpt‑oss‑safeguard models reason step by step, so they're slower, and they give yes/no answers.
- Alice (formerly ActiveFence) answers in under 150 ms but uses fixed, enterprise‑priced classifiers.
- An in‑house LLM judge on every turn costs a large share of the app's own inference bill.

**Market.** The starting market is small. Appfigures counted 337 companion apps making money in 2025 and $162.8M spent on romantic‑companion apps in H1 2026. The pitch has to be the growth path: from here to all AI used by teens, then to consumer‑facing AI agents generally.

**Weakest points.**
1. The starting market is small, and the March 2026 White House AI framework pushes to override state AI laws, though it spares child‑protection laws.
2. Liability, ethics and the reputation of some customers: a missed crisis is catastrophic.
3. Jev is unproven on grading clinical risk. Its calibration is off on unfamiliar tasks, role‑play is ambiguous, users can evade it, and it's weaker outside English.
4. Alice, the AI labs' own teen protections, and cost: even Jev isn't free at app scale. About 60M checks a day is roughly $3.8k/day, so you need a short first screen.
5. Dependence on TypeSafe. The fix is to distill the stable core checks into your own small model later.

**First moves.**
- Interview 20–30 of these companies (trust and safety or legal leads).
- Benchmark Jev against moderation APIs and an LLM on public labelled data such as VERA‑MH.
- Recruit a Purdue or IU psychiatry advisor so the method can credibly claim to be evidence‑based.
- Pilot with TypeSafe's zero‑data‑retention setting.

## Runners-up

**1. Live compliance checks on regulated sales calls, for human and AI voice agents.**
- *Why it could work:* the market is the largest of the four. Assume 100 talk‑hours a month and a check every 5 s. That costs about $8 per seat per month with Jev, against roughly $70–100 with a mid‑price LLM and $500+ with a frontier model. Only Jev fits a $50–100 seat price. The pain is current: on 31 Aug 2026 CMS cancelled about 315k unauthorized enrollments and has removed 200+ agents this year.
- *Weakest:* it's already crowded. Balto already flags missed disclosures in real time with LLMs, and Gryphon, Observe.AI, Cresta, Level AI and AgentTech ($50 per seat) are all there. With no BAA, you'd have to avoid health‑heavy calls. Speech‑to‑text costs more than Jev does.

**2. Plain‑English text features with cheap history backtests for fraud and risk teams.**
- *Why it could work:* scoring 50M past events on 50 questions costs about $1k with Jev and takes hours, not days. That enables a "free backtest before you buy" sales pitch. The features are readable, and the phishing result (62.6% to 95%) shows the method.
- *Weakest:* fraudsters write the text, and injected text shifts Jev's answers. Teams with lots of labels will get better results from fine‑tuned models. Sift, Sardine or Alloy can add this themselves.

**3. Tools that stop marketplace users taking deals off‑platform.**
- *Why it could work:* ROI is easy to prove with a holdout group. One study cited by Everything Marketplaces found 18% of Airbnb guest–host interactions led to offline bookings, and Upwork's losses are estimated at about $84M. Phone and email filters are easy to evade.
- *Weakest:* it fails the "only Jev" test. Marketplace messages are asynchronous and LLMs are affordable at small and mid scale. SafetyKit ($27M raised; customers include Upwork, Etsy and Faire) already reviews all content.

## Dropped
- **Guards on AI agents' tool calls:** Jev's sensitivity to injected text is disqualifying when the attacker writes the input.
- **Grading LLM output:** crowded, and Jev can't explain its answers.
- **Product catalog enrichment:** LLMs already do it for a few cents per product.
- **Clinical trial matching and prior authorization:** health data with no BAA, and data access is the real bottleneck.
- **Company or supplier search:** an index built once with an LLM covers most criteria, and Exa, Clay and Grata are already there.
- **Synthetic survey panels:** the problem is whether the results are valid, not cost.
- **LLM cost routers:** gateways like Vercel AI Gateway already carry Jev and will add routing themselves.

Sources: [Jev docs](https://docs.typesafe.ai/llms.txt), [8‑day independent review](https://dev.to/gde/jev-after-eight-days-of-independent-tests-level-with-mid-price-llms-behind-the-frontier-1kln), [62.6%→95%](https://www.beri.net/article/typesafe-jev-typed-decision-model-calibration-decomposition-shadow-eval), [Arize](https://arize.com/blog/typesafe-jev-llm-judge/), [Jev vendor profile](https://vendortrustindex.com/vendors/jev), [Orrick chatbot laws](https://www.orrick.com/en/Insights/2026/04/2026-State-Chatbot-Laws-Key-Provisions-and-Regulatory-Trends), [chatbot law tracker](https://www.ailawsbystate.com/tools/companion-chatbot-tracker), [FPF on SB 243](https://fpf.org/blog/understanding-the-new-wave-of-chatbot-legislation-california-sb-243-and-beyond/), [moderation gap paper](https://arxiv.org/abs/2609.06263), [VERA‑MH](https://arxiv.org/abs/2602.05088), [gpt‑oss‑safeguard](https://openai.com/index/introducing-gpt-oss-safeguard/), [Alice guardrails](https://alice.io/blog/low-latency-ai-guardrails), [companion app revenue](https://techcrunch.com/2025/08/12/ai-companion-apps-on-track-to-pull-in-120m-in-2025), [AI policy framework](https://www.crowell.com/en/insights/client-alerts/white-house-national-ai-policy-framework-calls-for-preempting-state-laws-protecting-children), [CMS cancellations](https://healthexec.com/topics/healthcare-management/healthcare-policy/cms-kicks-760000-people-aca-plans-crackdown-unauthorized-broker-supported-enrollments), [Balto platform comparison](https://www.balto.ai/blog/top-ai-agent-assist-platforms-for-insurance-call-centers-2026/), [SafetyKit](https://www.safetykit.com/), [disintermediation](https://www.everythingmarketplaces.com/post/disintermediation-in-the-age-of-ai), [Exa Websets pricing](https://exa.ai/pricing?tab=websets).