The claims mostly hold up, but the pitch leaves out two facts about the law that shrink the business. The risk assessment can be done in-house by the company itself. The part of the law that does require an outside party, the independent audit, doesn't apply to the pitch's target customers until 2032.

## Checking the claims against the law

The primary source is the chaptered bill text (Ch. 190).

| Claim | What I found |
|---|---|
| Signed September 2026 | **True.** Signed 10 Sept 2026 as Chapter 190. |
| Risk assessment before every new or substantially changed release | **Partly true.** It's required before a new chatbot or a "substantially modified" one, meaning a change that "materially changes its functionality or performance". Not every prompt tweak counts. |
| The assessment must be done by an outside party | **Not required.** The company can do it itself. It must include a summary of results for each "covered harm", its method, citations to publicly available benchmarks, and the fixes it made. It is kept on file for the life of the product plus 5 years and is **not filed with the Attorney General**. |
| Bans on claiming to be human, romance, encouraging emotional reliance | **True.** Section 21812(d)(5) also bans excessive praise, asking for purchases framed as keeping the relationship going, discouraging a child from telling professionals about health or safety, and getting around parental controls. |
| $5,000 to $15,000 per affected child | **True, with limits.** It's "not more than" $5,000 for negligent violations and $15,000 for intentional ones. Only the Attorney General and other public prosecutors can collect it. |
| Private suits | **Narrower than implied.** Families get actual damages plus attorney's fees, and only for some sections. Financial harm must exceed $1,000 per child, and emotional harm must be "serious emotional distress". There is no statutory per-violation amount. |
| Most duties start July 2027 | **True.** 1 July 2027. |
| Left out of the pitch | Independent audits are due 1 Jan 2029, then every two years, signed by the lead auditor under penalty of perjury. **Companies with under $500M in revenue are exempt from audits until 2032.** The law applies only once a company knows a user is a child through its age checks, so a company can leave the market by blocking minors, as Character.AI did in November 2025. School (K-12) products are not excluded. Only colleges and workplace deployments are. |

Two policy risks:
- **Court challenge.** In March 2026 the Ninth Circuit left in place the injunction against a similar California requirement, the impact assessment in the Age-Appropriate Design Code Act. I found no lawsuit against SB 1119 yet.
- **Federal preemption.** The December 2025 executive order on state AI laws carves out child safety, which lowers this risk.

## Who else serves these customers

I found no company with a near-identical pitch.

- **Common Sense Media's Youth AI Safety Institute.** Common Sense sponsored the law. The institute launched in May 2026 with a $20M a year budget, funded partly by Anthropic, the OpenAI Foundation and Pinterest. It already runs simulated teen conversations (over 3,100 exchanges in one study) with Stanford psychiatrists reviewing transcripts, and it is writing youth-safety standards. It rates products publicly and does not sell assessments, but it will set the benchmark companies cite.
- **KORA.** A free, open-source child-safety benchmark: synthetic multi-turn conversations across 25 risks, a sample checked by humans, and it can run inside a company's release pipeline. That is most of the proposed product's technology, and the statute asks companies to cite exactly this kind of public benchmark. Its limit is that it tests the underlying model, not the full product.
- **OpenAI's free teen-safety policies**, built with Common Sense and evryone.ai, which cover romantic roleplay among other risks.
- **Alice (formerly ActiveFence).** Pre-launch red-teaming, live filtering, and periodic retesting for drift and regressions. It has a child-safety background and works with TikTok, Amazon and 7 of the 10 largest AI model makers.
- **Circuit Breaker Labs.** Automated red-teaming of therapy and companion bots; Grow Therapy is a customer. The open **VERA-MH** benchmark covers similar ground.
- **Who controls the buying channel:** no one owns this customer's data. But for school software, buying decisions already run through privacy certification bodies (iKeepSafe, 1EdTech, PRIVO, kidSAFE) and BBB National Programs' AI Chatbot Accountability Initiative. The written assessment itself will default to outside law firms such as ZwillGen. Large platforms buy from Alice or build in-house.

## 1. The strongest version

- **Customers:** only those who can't drop their minor users, because minors are their product:
  - school AI tools that students talk to directly (MagicSchool's Raina, SchoolAI, Khanmigo, Flint)
  - teen and school mental-health apps (Alongside, Sonar)
  - AI products built for kids and AI toys

  Leave out character and companion apps. Their cheapest way to comply is to block minors.
- **Sell through outside counsel**, so test results are protected as legal work in the wrongful-death style lawsuits that follow cases like Adam Raine's.
- **Product:** build on KORA rather than against it. Add three things it lacks: tests of the full product (memory, time limits, parental controls, crisis routing), a pass/fail check for each banned behaviour in 21812(d), and clinician review. Rerun in the release pipeline on every model or prompt change.
- **Pricing:** mainly a subscription at about $3,000 to $5,000 a month with the assessment write-up included, not a $15,000 to $40,000 one-off, because the law doesn't force anyone to buy an outside assessment.
- **Later:** map the same tests to Oregon, Washington and New York law, and to the UK and Australian rules, then offer evidence packs for the 2029 audits at companies over $500M (Roblox, Duolingo, Snap). The team would have to choose between being the tester and being the auditor.

## 2. Ratings

| Area | Score | Evidence |
|---|---|---|
| Customer need | 3 | A real legal duty starts July 2027 with per-child penalties, but companies can do the assessment themselves, and small companies are exempt from audits until 2032. |
| Value over what customers use today | 2 | KORA (free, multi-turn, human-checked sample) and OpenAI's free teen policies already cover most of the core; the added value is clause mapping and clinician review. |
| Market size | 2 | By my rough estimate, a few hundred companies in scope keep minors, so about $10M to $30M a year in California. The other state laws I found (Orrick's April 2026 survey) don't require a pre-release assessment. |
| Risk (5 = low) | 2 | The similar California impact-assessment requirement is still blocked in court, companies can exit by blocking minors, and Common Sense's standards could make the product a commodity. |

## 3. What would kill it, and the fastest test

**It dies if** in-scope companies meet the assessment duty with free benchmarks plus a lawyer's memo and won't pay more than $15,000. It also dies if companies block minors, or if a court blocks the assessment provision.

**Fastest test (2 to 3 weeks):** pitch a paid $15,000 Adam's Law pre-assessment, delivered in Q1 2027, to about 20 named companies that can't drop minors, meaning the school AI tools and teen mental-health apps listed above. Also pitch 3 privacy law firms as a referral channel. If fewer than 3 companies sign paid letters of intent, kill it. Everything above is desk research, and none of it is customer validation.

Sources:
- [SB 1119 bill status](https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB1119) and [SB 1119 bill text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB1119)
- [Governor's press release](https://www.gov.ca.gov/2026/09/10/governor-newsom-signs-the-strongest-child-safety-chatbot-and-social-media-laws-in-the-nation/)
- [ZwillGen analysis](https://www.zwillgen.com/artificial-intelligence/adams-law-california-raises-the-bar-for-child-chatbot-protections/)
- [SB 243 companion chatbot definition (Section 22601)](https://law.justia.com/codes/california/code-bpc/division-8/chapter-22-6/section-22601/)
- [Common Sense statement on signing](https://www.commonsensemedia.org/press-releases/governor-newsom-signs-adams-law-setting-first-real-safety-standard-for-kids-and-chatbots)
- [Youth AI Safety Institute launch](https://www.commonsensemedia.org/press-releases/common-sense-media-launches-youth-ai-safety-institute) and [its mental-health app assessment](https://institute.commonsensemedia.org/risk-assessments/ai-mental-health-apps)
- [KORA benchmark](https://korabench.ai/blog/2026-02-03/introducing-kora)
- [OpenAI teen safety policies](https://openai.com/index/teen-safety-policies-gpt-oss-safeguard/)
- [Alice (ActiveFence) generative AI products](https://www.activefence.com/solutions/generative-ai/)
- [Circuit Breaker Labs](https://www.circuitbreakerlabs.ai/)
- [BBB AI Chatbot Accountability Initiative](https://industryselfregulation.org/incubator/ai)
- [Orrick survey of 2026 state chatbot laws](https://www.orrick.com/en/Insights/2026/04/2026-State-Chatbot-Laws-Key-Provisions-and-Regulatory-Trends)
- [Cooley on the March 2026 Ninth Circuit ruling](https://www.cooley.com/news/insight/2026/2026-03-30-netchoice-v-bonta-ninth-circuit-narrows-injunction-against-californias-ageappropriate-design-code-act)
- [Gibson Dunn on the executive order](https://www.gibsondunn.com/president-trump-latest-executive-order-on-ai-seeks-to-preempt-state-laws/)
- [CNBC on Character.AI's under-18 ban](https://www.cnbc.com/2025/11/24/characterai-to-ban-teens-from-open-ended-chats-human-interaction-is-crucial-psychotherapist-says.html)

VERDICT: PASS