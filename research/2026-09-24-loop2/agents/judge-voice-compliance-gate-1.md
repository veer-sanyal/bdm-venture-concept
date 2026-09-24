**The idea as pitched points at the wrong risk.** Every AI-call lawsuit I found is about whether the business was allowed to place the call at all: consent, the Do-Not-Call list, or ignoring "stop calling." A layer that edits what the agent says doesn't touch any of those. A narrower version, focused on the few areas where what the agent says does carry legal liability, is defensible, but the value it adds is thin and the voice platforms are already building it in.

## Checking the key claims

| Claim | Verdict |
|---|---|
| The FCC treats AI voices as "artificial voice" under the TCPA | **True.** FCC ruling 24-17, 8 Feb 2024. Since the Supreme Court's June 2025 *McLaughlin* decision, district courts aren't bound by FCC readings, but the statute's wording probably covers AI anyway. |
| $500 to $1,500 per violating call | **True, but only for calling without consent or calling Do-Not-Call numbers** (47 USC 227(b)(3)). The rules on what an artificial-voice call must say (stating who is calling, giving a callback number, 227(d) and 64.1200(b)) mostly have **no private right to sue**, according to most courts. So the scary per-call number mostly applies to the consent problem this product doesn't fix. |
| TCPA class actions hit a record in 2025 | **True for class actions** (1,636 filed through September versus 800 a year earlier, per Troutman Amin). Total TCPA filings were flat (+0.8%, 2,810 cases, per WebRecon). |
| There are lawsuits over AI calls | **True**: Mortgage One (Feb 2026), Finley v. Altrua, Lowrey v. Twilio/OpenAI (Dec 2025). All centre on consent, Do-Not-Call and ignored opt-outs. Only Mortgage One adds a content complaint (no upfront disclosure, fake "returning your call"). The Cider settlement ($5.95M) came from failing to recognise "please cease," which is about what the *caller* said, not the agent. |
| "Sales and service calls" | TCPA consent rules mostly don't apply to inbound calls, where the customer rings the business. The FCC's proposed rule requiring AI disclosure at the start of calls (24-84) is still not final. |

## Who else serves this customer, and who owns the buyer

- **Voice platforms own the builder's channel.** Retell (about $60M annual revenue) launched guardrails in February 2026 that block output categories including "regulated advice" before the caller hears it. The categories are preset; it can't yet load a custom rulebook. Vapi also ships guardrails.
- **Vertical AI voice companies own the lender's collections budget.** Salient ($60M Series A from a16z, $25M annual revenue) and Prodigal (ProAgent) sell compliance built in.
- **Gryphon owns the compliance officer's buying channel** for Do-Not-Call, consent and time-of-day checks before a call is dialed. It already covers AI agents and integrates with Genesys, but it doesn't check speech during the call.
- **Consent data** is owned by ActiveProspect (TrustedForm) and Verisk (Jornaya).
- **Voice-agent testing tools** (Cekura, Hamming, Coval, Roark) hold the builders' QA budget.
- **Norm Ai** ($1.2B valuation, July 2026) sells rulebook-as-code compliance checks to chief compliance officers and could extend into voice.
- **Lorikeet** is the closest match to the pitch: it checks each utterance before it's spoken. But it only does that inside its own full-stack agent, so it isn't this team.

I found no standalone company with this exact pitch.

## 1. Strongest version

A separate compliance control that sits between the language model and speech output on Retell or Vapi (both let you plug in your own model endpoint). Aim it only at areas where what's said creates liability:

- **Debt collection and loan servicing:** the required debt-collector disclosure, not revealing the debt to third parties, no misleading statements, lending-disclosure trigger terms.
- **Medicare and ACA insurance marketing:** the required third-party marketer disclaimer, banned phrases, recording retention.
- **State AI and recording disclosures:** California AB 2905 and the CIPA recording lawsuits.
- **Listening to the caller as well as the agent:** detect an opt-out during the call, force the agent to acknowledge it and add the number to the suppression list. That links the product to real TCPA exposure.

The customer to sell to is the lender's or insurer's compliance officer; agencies and builders are only the distribution route. The selling point is independence: examiners prefer a control the agent vendor didn't write for itself.

## 2. Ratings

- **Customer need: 3.** Class actions roughly doubled in 2025, but the AI suits are about consent and Do-Not-Call, not the agent's wording.
- **Value over what customers use today: 2.** Retell's guardrails, Salient/Prodigal's built-in compliance and Gryphon's pre-dial blocking already cover most of it. What's left is a custom rulebook plus an independent per-call record.
- **Market size: 2.** Retell's roughly $60M revenue at about 7¢ a minute implies under a billion minutes a year. Even with Vapi added and a generous share from regulated industries, 1 to 2¢ a minute is only about $10M in reachable revenue today. It is growing fast.
- **Risk: 2.** Platforms can add custom rules cheaply. A missed violation creates liability for the vendor. Checking every sentence adds delay to live speech, and false blocks break the conversation. Federal pressure is easing (the FCC under Carr, the *McLaughlin* ruling).

## 3. What would kill it, and the fastest test

**What kills it:**
- Compliance buyers find few content violations in real calls, because scripted flows already force the disclosures and their exposure sits in consent.
- Or Retell/Vapi let customers write their own guardrail rules.

**Fastest test:** offer a paid audit of the last 1,000 production call transcripts to 15 builders or compliance leads in collections and Medicare. The idea survives only if:
- violations turn up in more than 1% of calls, and
- at least 3 of the 15 sign a pilot at $500 a month or more within three weeks.

Everything above is desk research; none of it is customer validation.

Sources: [FCC 24-17](https://docs.fcc.gov/public/attachments/FCC-24-17A1.pdf), [47 USC 227](https://www.law.cornell.edu/uscode/text/47/227), [TCPAWorld on 227(d) content claims](https://tcpaworld.com/2021/12/03/content-claims-gain-steam-court-reverses-earlier-ruling-determining-no-private-right-existed/), [Troutman Amin class action counts](https://natlawreview.com/article/woah-tcpa-class-actions-just-spiked-283-september-2025-and-out-control), [WebRecon 2025](https://webrecon.com/litigation-statistics/webrecon-dec-2025-stats-year-in-review), [Mortgage One](https://www.nationalmortgagenews.com/news/ai-marketing-calls-spur-suit-against-lender), [Lowrey](https://tcpaworld.com/2025/12/31/openai-liable-for-robocalls-texts-new-tcpa-complaint-claims-openai-and-twilio-are-liable-for-user-initiated-robotexts-violating-the-tcpa-and-this-could-change-everything/), [McLaughlin](https://www.supremecourt.gov/opinions/24pdf/23-1226_1a72.pdf), [FCC NPRM 24-84](https://docs.fcc.gov/public/attachments/FCC-24-84A1.pdf), [Retell changelog](https://www.retellai.com/changelog), [Gryphon 2026 launch](https://www.prnewswire.com/news-releases/gryphon-ai-unveils-1h-2026-strategic-product-launch-redefining-contact-compliance-as-a-unified-grc-control-layer-302754900.html), [Lorikeet](https://www.lorikeetcx.ai/articles/best-enterprise-voice-ai-compliance-2026), [Salient](https://finance.yahoo.com/news/salient-ai-loan-processing-startup-175739561.html), [Prodigal](https://www.prodigaltech.com/proagent), [Norm Ai](https://enterprisedna.co/resources/news/norm-ai-120m-series-c-compliance-agents-enterprise-2026/), [Retell revenue (Sacra)](https://sacra.com/research/retell-ai-60m-yr-up-650-yoy/), [Vapi valuation](https://techcrunch.com/2026/05/12/vapi-hits-500m-valuation-as-amazon-ring-chose-its-ai-platform-over-40-rivals/), [CIPA AI lawsuits](https://www.wsgr.com/en/insights/us-federal-court-allows-cipa-class-action-against-ai-customer-service-provider-to-proceed.html), [CA AB 2905](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202320240AB2905), [inbound calls outside TCPA](https://www.henson-legal.com/newsroom/ai-voice-tcpa-compliance-guide)

VERDICT: PASS