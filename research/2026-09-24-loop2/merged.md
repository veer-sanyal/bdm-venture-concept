# Merged generator output, loop 2 (2026-09-24, Jev seed)

Desk research only; not customer validation. Three generators, same brief and seed, fresh contexts. Every idea a generator put forward as its best or a runner-up is listed; ideas a generator itself dropped are not. Each numbered entry, as written here, is exactly what its shaper receives.

**Convergence:** all three generators independently chose the same best idea (entry 1).

**Archive check:** no overlap with round 17's Jev lane (letters of credit, HTS broker check, grant allowability, consumer-report matching, pharmacy LASA, TPA claims files, H-1B RFE, export control, pesticide, refrigerant) or with any earlier candidate. The archive never examined chatbot safety, game NPCs, ad matching, sales-call compliance, fraud features or marketplace leakage. Supplier search appears only as market sizing for the chargeback concept.

**Jev supplier terms** (orchestrator's read of TypeSafe's Master Customer Agreement, typesafe.ai/legal/mca, 2026-09-24; appended to every entry):
- §2.2 allows integrating the API into "software applications developed and operated by Customer for the benefit of Customer's end users."
- §2.3(a) forbids offering the Services "as a standalone service."
- §2.3(b) forbids using Output to "train a model to imitate the output of the Services, or develop (or to facilitate the development of) a similar or competing product or service."
- There is no SLA, and TypeSafe may suspend immediately for a breach.
- §4.1: TypeSafe keeps telemetry derived from customer data in perpetuity.
- Zero data retention is enterprise-only, TypeSafe signs no BAA, and new signups were paused on 2026-09-22.

---

## 1. Per-turn safety and compliance layer for consumer AI chat and voice (generators 1, 2 and 3, each as best idea)

- **Product.** An API beside companion, character, wellness, tutoring and teen-facing chat or voice apps.
  - On every turn, one Jev call over the recent conversation and the bot's draft reply asks 20 to 40 typed questions.
    - About the user: graded suicide-risk items modelled on the Columbia scale, self-harm, eating-disorder cues, signals of a minor, role-play or fiction.
    - About the bot: claims to be human or a licensed professional, sexual content with a likely minor, manipulative engagement, method information, whether a required crisis referral was given.
  - Per-state rule packs in code turn probabilities into actions: 988 or crisis-line referral (for example ThroughLine, used by OpenAI and Anthropic), block or rewrite, minor mode, break reminders, disclosures.
  - Timers and counts run in code, since Jev cannot count.
  - Uncertain turns go to an LLM (for example gpt-oss-safeguard), then to a human.
  - Outputs: audit logs, the required annual reports (California's to its Office of Suicide Prevention from 2027-07-01), each operator's published protocol, and a validation report supporting "evidence-based".
- **Need (laws).**
  - California SB 243 took effect in January 2026. It requires evidence-based detection of suicidal ideation, crisis referral and protections for minors, with a private right of action at $1,000 per violation.
  - Other states:
    - New York: in force since November 2025.
    - Tennessee: July 2026, $5,000 per violation.
    - Connecticut: October 2026.
    - Hawaii: July 2026.
    - Oregon and Washington: January 2027, private suits.
    - Georgia and Rhode Island: Rhode Island up to $15,000 a day.
    - Idaho and Nebraska: July 2027.
  - About 14 to 16 state chatbot laws in 2026; 98 to 126 bills pending.
  - Several laws cover all chatbots, not only companions. The December 2025 executive order and the March 2026 White House framework push to preempt state AI laws but spare child safety.
  - UK Online Safety Act reforms reach chatbots.
- **Why Jev.**
  - Cost:
    - About $0.00013 per turn, against about $0.002 for a mid-price LLM.
    - For 100k daily users at 40 turns each, about $250 a day against about $7,500.
    - A heavy user costs about $0.40 a month against about $6.
  - Speed: 0.25 to 0.5 s fits a voice turn.
  - Split-question pattern: the 63%→95% result suits checklist-style clinical items.
  - New state rules become new questions, with no retraining.
  - Moderation APIs flag reliably (F1 0.86) but grade severity poorly (macro-F1 0.395; 0.562 with clinical framing; arXiv 2609.06263).
  - gpt-oss-safeguard is too slow for real time by OpenAI's own account.
  - jevmod, an open-source single-message Jev self-harm check, has no conversation context and no law handling.
- **Market.**
  - About 337 companion apps earned revenue in 2025, and the top 10% took 89%.
  - About $120M+ a year outside Character.AI; $162.8M spent on romantic-companion apps in H1 2026.
  - Large players build in-house.
  - Growth path: all teen-facing AI (tutors, toys, games), then every consumer chatbot as laws widen, then voice agents, human-to-human moderation and agent checks.
- **Moat ideas from the generators.**
  - Clinician-labelled conversations and the calibrated thresholds built on them.
  - A published validation that lawyers and AI insurers (for example AIUC) accept.
  - Rule packs kept current across states, like Vanta for SOC 2.
  - Swapping models: open Jev replicas exist (openjev 0.845 agreement against Jev's 0.883; Bosun on Qwen).
  - Crisis-line integration.
  - A Purdue or IU clinical advisor.
- **Weakest.**
  - A small, fragmented, partly NSFW starting market.
  - Liability for a missed crisis.
  - Jev is unproven on clinical grading. Role-play and injected text shift it, it is weaker outside English, and calibration drifts on unfamiliar tasks. One test found 71% on ambiguous cases.
  - Incumbents: Alice (formerly ActiveFence; under 150 ms, enterprise-priced), Hive, Checkstep, OpenAI's free moderation, and the labs' own teen protections.
  - Federal preemption.
  - Privacy law on inferred mental-health data.
  - Sending minors' crisis disclosures to a nine-day-old API with telemetry retention.
  - One generator proposed later distilling the core checks into an in-house model. §2.3(b) appears to forbid training on Jev output.
- **Jev supplier terms:** see the header.

## 2. Reliability layer for teams building on Jev (generator 1, runner-up)

- **Product.** The parts every Jev adopter rebuilds, sold once:
  - question decomposition, and fitting how to combine the answers;
  - calibration against labelled examples;
  - option-order shuffling and averaging (answers shift with order);
  - injection defences;
  - routing unsure items to an LLM;
  - an audit trail of every automated decision.
- **Why it could work.**
  - Reported adoption by about 13% of paid Vercel AI Gateway teams within 24 hours.
  - The independent gains came from exactly this work: 63%→95% only after decomposition and fitting on 1,000 labels; routing cut cost to 25–50% of all-LLM.
  - Jev is confidently wrong on unfamiliar tasks.
  - It could become the record auditors expect for automated decisions.
- **Weakest.** TypeSafe publishes these patterns and could ship them. Langfuse already supports Jev-as-judge. Developer tools are hard to validate for a VC panel.
- **Jev supplier terms:** see the header; §2.3(a) and (b) bear directly on a product built around Jev itself.

## 3. Decision engine for game characters choosing among authored lines and actions (generator 1, runner-up)

- **Product.** Jev picks among lines and actions the game's writers authored, for free-to-play and user-generated games.
- **Why it could work.** Developers call LLM inference cost "the wall": an estimated $0.5–2M a year for a 100k-player game. Jev cuts that 10–25x at about 250 ms. Authored lines keep writers and voice actors in control after the actors' union disputes over AI.
- **Weakest.** It doesn't prove AI characters make games more fun. Jev can't generate dialogue. On-device small models are free. Games are hit-driven and studio sales cycles are long.
- **Jev supplier terms:** see the header.

## 4. Supplier search for mid-sized manufacturers (generator 1, runner-up; generator 3 dropped company and supplier search)

- **Product.** Precompute answers to thousands of yes/no capability questions for every supplier website, then search interactively with evidence. This is the pattern behind Jev's one reported production use, Metaview's recruiting search going from minutes to seconds.
- **Why it could work.** Tariffs are forcing resourcing, and Indiana manufacturing is reachable from Purdue.
- **Weakest.**
  - Competitors: Didero ($30M Series A), Matchory, Scoutbee, Keychain and Thomasnet; generator 3 adds Exa, Clay and Grata.
  - Supplier specs are numeric (tolerances, capacities), which Jev can't handle.
  - Data freshness is the real moat and it's hard.
  - A one-time LLM-built index covers most criteria cheaply.
- **Jev supplier terms:** see the header.

## 5. Per-turn ad and sponsored-offer matching for independent AI apps (generator 2, runner-up)

- **Product.** One Jev call per turn picks among up to 255 offers and checks suitability. It pairs with entry 1 by suppressing ads in crisis conversations or when a minor is detected.
- **Why it could work.** At $5–15 CPM with an ad on about 1 in 10 turns, revenue is about $0.0005–0.0015 per turn. An LLM decision at $0.001–0.002 eats that; Jev costs 5–10% of it.
- **Weakest.** A two-sided network is hard to start. OpenAI launched ads in ChatGPT in February 2026. There is pushback on ads in chat, especially to minors. Funded rivals: Koah ($20.5M), Dappier. Jev's option-order bias affects fairness to advertisers.
- **Jev supplier terms:** see the header.

## 6. Approvals that learn, for AI agent actions (generator 2, runner-up; generators 1 and 3 dropped agent tool-call guards over injection)

- **Product.** Each action an agent proposes (for example a support refund) gets one Jev call with about 20 risk questions; amounts and dates are checked in code. Confident cases run automatically and the rest go to a human. Human decisions retune thresholds to hold a target error rate, so autonomy grows over time.
- **Why it could work.** pi-warden held 42 of 17,000 calls, and about 88% of those holds were right.
- **Weakest.** Guardrail startups raised about $456M in 12 months, and agent platforms can build this in. Customer messages are attacker-controlled text, which hits Jev's injection weakness.
- **Jev supplier terms:** see the header.

## 7. Live compliance checks on regulated sales calls, for human and AI voice agents (generator 3, runner-up)

- **Product.** Jev checks the live transcript every few seconds for missed disclosures and prohibited claims.
- **Why it could work.**
  - Assuming 100 talk-hours a month and a check every 5 s: about $8 per seat a month with Jev, against $70–100 with a mid-price LLM and $500+ with a frontier model. Only Jev fits a $50–100 seat price.
  - CMS cancelled about 315k unauthorized enrollments on 2026-08-31 and has removed 200+ agents this year.
- **Weakest.** Balto already flags missed disclosures in real time with LLMs. Gryphon, Observe.AI, Cresta, Level AI and AgentTech ($50 a seat) are also there. With no BAA, health-heavy calls are out. Speech-to-text costs more than Jev.
- **Jev supplier terms:** see the header.

## 8. Plain-English text features with cheap history backtests, for fraud and risk teams (generator 3, runner-up)

- **Product.** Dozens of readable yes/no features per event, and a free backtest on history before purchase.
- **Why it could work.** Scoring 50M past events on 50 questions costs about $1k and takes hours. The phishing result (62.6%→95%) shows the method.
- **Weakest.** Fraudsters write the text, and injection shifts Jev. Teams with many labels do better with fine-tuned models. Sift, Sardine or Alloy can add this themselves.
- **Jev supplier terms:** see the header.

## 9. Stopping marketplace deals from moving off-platform (generator 3, runner-up; the generator says it fails its own "only Jev" test)

- **Product.** Detect attempts to move a deal off the marketplace.
- **Why it could work.** ROI is easy to prove with a holdout group. One cited study found 18% of Airbnb guest–host interactions led to offline bookings, and Upwork's losses are estimated at about $84M. Phone and email filters are easy to evade.
- **Weakest.** Messages are asynchronous and LLMs are affordable at this scale. SafetyKit ($27M raised; Upwork, Etsy, Faire) already reviews all content.
- **Jev supplier terms:** see the header.
