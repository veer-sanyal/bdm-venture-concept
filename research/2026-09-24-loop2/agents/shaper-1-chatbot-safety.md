**Verdict:** As written, this is not a strong company. The product already exists at the same price, free substitutes are spreading, and the Jev supplier terms don't fit a life-safety product for minors. One reshaped version is worth pitching: pre-release child-safety testing and evidence for consumer chatbots, built around California's new Adam's Law (SB 1119). It is a credible Burton D. Morgan entry, but only a medium-strength venture. Everything below is desk research, not customer validation. As you asked, I didn't read any local project files.

## Why the original doesn't hold

1. **The product already exists at the same price.** NOPE (nope.net) sells:
   - a per-turn classifier (Ocular) at $0.0001 per call;
   - a deeper check (Evaluate) at $0.003 per call, covering 9 risk types with severity and matched crisis resources;
   - Oversight, which reviews the bot's side of a conversation against 91 behaviours (dependency, manipulation, crisis mishandling) at $0.10 per conversation;
   - a free crisis-line lookup covering 222 countries.

   It cites the Columbia suicide scale, advertises "audit-ready output that supports SB 243-style reporting," and keeps a law tracker. Jev's cost edge (about $0.00013 per turn) is gone. The brief doesn't mention NOPE.
2. **Free and funded alternatives.**
   - OpenAI released a free, open-source Teen Safety Policy Pack in March 2026, written for gpt-oss-safeguard.
   - mpathic has raised $15M and runs a network of thousands of licensed clinicians who build test sets and monitor live conversations. That is the "clinician-labelled data" moat the brief proposes.
   - Alice sells an enterprise guardrail product (WonderFence).
   - The paper the brief cites (arXiv 2609.06263) credits the gain to clinically framed prompts on ordinary LLMs, so the gain doesn't need Jev.
3. **Jev is the wrong foundation for live minors' data.** I checked TypeSafe's agreement:
   - It forbids offering the service "as a standalone service" and bans distillation.
   - There is no SLA, and TypeSafe can suspend immediately.
   - Telemetry can be used "without restriction, including to improve the Services." SB 1119 limits using minors' personal information to providing the service, safety and legal compliance.
   - New signups were paused on 2026-09-22, so you may not be able to get an account.
4. **The market is smaller than the brief says.**
   - Romantic and NSFW companion apps took $162.8M in mobile spending in the first half of 2026; the top app (Zeta) took $33M.
   - Many apps will verify age and exclude minors rather than comply. Character.AI already bans open-ended chat for under-18s.
   - Nebraska's and Idaho's "conversational AI" laws exempt customer-service, narrow-purpose, business-to-business and voice-assistant bots. Nebraska's is enforced only by the Attorney General, with no private suits. "Every consumer chatbot" overstates it.
5. **Liability.** A live per-turn layer that misses a crisis shares the blame.

## The fact the brief missed: SB 1119, signed 2026-09-10

- **Dates:** in effect 2027-01-01; most duties start 2027-07-01.
- **Duties:**
  - A documented risk assessment before releasing any new or substantially changed bot.
  - Either determine each user's age or apply the protections to everyone.
  - Minor defaults: one-hour sessions, two hours a day, memory and push notifications off.
  - Parent notification or direct 988 access on a credible, imminent threat.
  - A public incident-reporting channel, and three years of records after serious incidents.
  - Testing with real children and parents by 2028-01-01.
- **Banned bot behaviour toward minors:** claiming to be sentient or human, romance, praise out of proportion to the context, encouraging emotional reliance, claiming special understanding of the child, relationship-framed purchases, and helping evade parental controls.
- **Penalties:** $5,000 per affected child for negligent violations and $15,000 for intentional ones, plus private suits.
- **Independent audits:** due by 2029-01-01. Companies under $500M revenue are exempt until 2032, so audits are not the near-term wedge.
- **Related laws:**
  - SB 813 and AB 1405 create a state registry of AI auditors. An audit counts as evidence in a lawsuit, but not as a defence.
  - SB 867 bans AI-companion toys for under-16s in California from 2027 to 2031, which closes the brief's toy expansion path there.

The banned-behaviour list is a set of yes/no questions about the bot's own reply. That is exactly what the split-question pattern is good at, and you can measure it by simulating conversations.

## The reshaped company

**Wedge, sold now for the July 2027 deadline: a risk-assessment test harness.**
- The operator points us at a staging copy of their bot.
- We run thousands of simulated multi-turn conversations with 13–15 and 16–17 personas: escalating crisis, romance-seeking, building dependency, role-play jailbreaks, parental-control evasion, and attempts to get past the age gate.
- Graders ask typed questions mapped to each clause of the law. Timers and counts run in code. Clinicians review a sample.
- Output: the documented risk assessment SB 1119 requires, a regression suite that reruns on every model or prompt change, and evidence behind SB 243's "evidence-based" requirement.

**Why this fixes the Jev problems:**
- The conversations are synthetic, so no real minors' data goes to TypeSafe.
- It isn't in the live crisis path, so a TypeSafe outage delays a test run rather than a crisis response.
- The grader can be swapped between Jev, open replicas and gpt-oss-safeguard.
- A lawyer still needs to read the standalone-service clause. Never train on Jev output.

**Expansion:**
1. A runtime SDK for what only code can do: session and daily timers, reminders, the parent-notification workflow, incident intake and record holds. Checks on the bot's replies would run on an open model inside the operator's own cloud. It would plug into existing detectors (NOPE, OpenAI) rather than compete with them.
2. Audit-readiness tools once the auditor registry opens, and links to AI insurers.

**Buyers:**
- Consumer AI products that keep minors: tutors with persistent characters, teen wellness apps, story and character apps. Whether tutors count as "companion chatbots" needs legal confirmation.
- Adult companion apps that need SB 243 evidence and proof their age gate works.
- Law firms and consultancies writing risk assessments, as a sales channel.

**Market:** near-term US revenue is likely tens of millions of dollars, not billions. It grows as other states copy SB 1119 and the EU and UK tighten rules. Pricing of $15–40k per assessment plus $2–5k a month for regression runs is my guess, not tested.

**Remaining risks:**
- Operators may exclude minors rather than comply.
- mpathic, NOPE's public test suites, Spring Health's open VERA-MH and law firms compete for the same work.
- Simulated personas are not real teens, so you need a licensed clinical advisor and a published method.
- A federal children's-safety package could displace state rules that cover the same ground.
- Two undergrads will need extra credibility to sell to general counsels.

## What to do next

Talk to 15–20 people before building:
- heads of trust and safety or legal at teen-accessible AI apps;
- 3–5 lawyers who will write SB 1119 risk assessments;
- 2 clinicians.

Ask whether they will keep minors, who will write their assessment, what counts as evidence, and what they would pay. Drop the idea if most operators plan to exclude minors and lawyers expect memo-only assessments with no testing.

I ran out of web searches before checking Australia's rules and whether Common Sense Media offers certification, so those are unchecked.

**Sources:**
- [SB 1119 bill text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB1119)
- [Mondaq on Adam's Law](https://www.mondaq.com/unitedstates/it-and-internet/1844304/adams-law-california-raises-the-bar-for-child-chatbot-protections)
- [ZwillGen on Adam's Law](https://www.zwillgen.com/artificial-intelligence/adams-law-california-raises-the-bar-for-child-chatbot-protections/)
- [Cloud Security Alliance note on the audit mandate](https://labs.cloudsecurityalliance.org/research/csa-research-note-california-ai-chatbot-audit-mandate-202609/)
- [CalMatters on the September 2026 bills](https://calmatters.org/economy/technology/2026/09/california-enacts-laws-restricting-chatbots-protecting-kids-online/)
- [SB 813 (govbuddy)](https://www.govbuddy.com/california/bills/sb-813/)
- [Toy Association on SB 867](https://www.toyassociation.org/PressRoom2/News/2026-News/california-governor-signs-ai-toy-and-chatbot-bills-into-law.aspx)
- [NOPE](https://nope.net/)
- [NOPE docs](https://docs.nope.net/)
- [TypeSafe MCA](https://typesafe.ai/legal/mca)
- [TypeSafe signup pause](https://x.com/typesafeai/status/2102281508950307159)
- [Jev deep dive](https://flaviocopes.com/jev/)
- [Foundry on mpathic](https://foundry.vc/blog/2026/02/our-investment-in-mpathic/)
- [OpenAI teen safety policies](https://openai.com/index/teen-safety-policies-gpt-oss-safeguard/)
- [arXiv 2609.06263](https://arxiv.org/abs/2609.06263)
- [Orrick 2026 state chatbot laws](https://www.orrick.com/en/Insights/2026/04/2026-State-Chatbot-Laws-Key-Provisions-and-Regulatory-Trends)
- [multistate.ai companion chatbot laws](https://www.multistate.ai/updates/vol-105-state-ai-companion-chatbot-laws)
- [Companion app revenue (Yahoo Finance)](https://finance.yahoo.com/technology/ai/articles/much-boyfriend-spending-ai-girlfriends-164036900.html)
- [ThroughLine](https://www.throughlinecare.com/)
- [Federal preemption status (CASRAI)](https://casrai.org/news/federal-ai-moratorium-state-preemption-fight-2026)
- [Alice rebrand](https://www.calcalistech.com/ctechnews/article/hyk5chss11x)