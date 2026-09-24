**Recommendation: pass.** The law is real and the pitch mostly describes it correctly. But the risk assessment is one customers can write themselves, and the one mandatory outside check exempts almost every target customer until 2032. Many companion apps can also avoid the law by shutting teens out. The buyers who can't are few. And a well-funded incumbent (Alice) already sells this service to child-facing AI companies.

## Checking the pitch against the bill text

| Claim | Verdict |
|---|---|
| Signed September 2026 | True. Signed Sept 10, 2026 ([Governor](https://www.gov.ca.gov/2026/09/10/governor-newsom-signs-the-strongest-child-safety-chatbot-and-social-media-laws-in-the-nation/)) |
| Documented risk assessment before every new or substantially modified release | True (§21812(a)). The operator must "perform and document" it, citing public benchmarks. It is **not filed with any government body**, and the law doesn't require an outside party to do it ([bill text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB1119)). |
| Bans on claiming to be human, romance and encouraging emotional reliance | True (§21812(d)). It also bans excessive flattery, claiming a "special relationship", and pushing purchases framed as needed to keep the relationship. |
| Penalties of $5,000–$15,000 per child | Partly wrong. These are maximums ("not more than"), for negligent and intentional violations. Private suits require actual harm: over $1,000 in financial loss, or serious emotional distress. |
| Most duties start July 2027 | True |
| Not in the pitch | The independent audit is the only mandatory outside check. It is due Jan 1, 2029, but operators under $500M revenue are exempt until 2032. That covers nearly all target customers. A separate duty requires testing with real children and parents by Jan 1, 2028, which simulated personas can't satisfy ([ZwillGen](https://www.zwillgen.com/artificial-intelligence/adams-law-california-raises-the-bar-for-child-chatbot-protections/)). Separate California laws (SB 813, AB 1405) set independence rules and a registry for AI auditors ([CSA](https://labs.cloudsecurityalliance.org/research/csa-research-note-california-ai-chatbot-audit-mandate-202609/)). |

Two things are unclear in the law. Whether K-12 tutors count as "companion chatbots" is disputed; only colleges are expressly excluded. I couldn't find how "substantially modified" is defined, and that decides whether every prompt change triggers a new assessment.

## Who else serves this customer
- **Alice (formerly ActiveFence):** has raised about $280M and already works with 7 of the 10 largest AI model makers. It has a child-facing AI offering with pre-launch red-teaming (WonderBuild), guardrails that run in the live product, and ongoing regression testing (WonderCheck). Its page doesn't mention California's chatbot laws yet ([Alice](https://alice.io/industries/child-facing-platforms-and-products)). Alice owns the trust-and-safety buying channel at large platforms and model makers.
- **Circuit Breaker Labs:** the closest match to the pitch. It runs 100,000+ simulated multi-turn conversations, catches safety regressions and delivers an audit report. It focuses on mental health rather than minors-law compliance ([site](https://www.circuitbreakerlabs.ai/)).
- **mpathic:** a network of over 5,000 experts, mostly clinicians, who red-team by playing adolescents and other vulnerable users ([site](https://mpathic.ai/red-teaming-experts/)).
- **Free substitutes:**
  - OpenAI's open-source teen safety policy pack, built with Common Sense ([OpenAI](https://openai.com/index/teen-safety-policies-gpt-oss-safeguard/)).
  - Promptfoo, an open-source red-teaming tool OpenAI bought ([OpenAI](https://openai.com/index/openai-to-acquire-promptfoo/)).
  - Common Sense's Youth AI Safety Institute, with a $20M yearly budget and plans for open-source benchmarks ([Common Sense](https://www.commonsensemedia.org/press-releases/common-sense-media-launches-youth-ai-safety-institute)). The law asks assessments to cite public benchmarks, so these become the default.
  - Vals AI, which has a clinician-built multi-turn child-safety benchmark ([Vals](https://www.vals.ai/blogs/child-ai-safety)).

Does an incumbent own this customer? Alice owns the channel at large companies. For small apps that serve teens, the channel is outside counsel and, for edtech and wellness products sold to schools, district procurement. No one owns their data.

## 1. The strongest version
Narrow the target to AI products whose users are **mostly minors, so they can't solve the problem by shutting teens out**:
- AI tutors for school students and youth wellness bots sold to schools. Alongside is one example; its Kiwi chatbot is used in 200+ schools ([EdSource](https://edsource.org/2026/ai-chatbot-mental-health/765694)).
- AI toys, which California regulates under SB 867.

Character apps are a poor wedge: Character.AI already dropped open-ended chat for under-18s ([Bloomberg](https://www.bloomberg.com/news/articles/2025-10-29/character-ai-to-ban-children-under-18-from-talking-to-its-chatbots)).

The product would be a testing tool that reruns on every release. It would check each clause of California's laws plus the 13 other state chatbot laws passed in 2026; six of those ban emotional-dependence or romance behaviour ([Transparency Coalition](https://www.transparencycoalition.ai/news/watershed-year-for-chatbot-safety-measures-14-new-state-laws-enacted-so-far-in-2026)). Each run would produce the risk-assessment document automatically. Add the real child-and-parent usability testing due in 2028. Position it as audit preparation rather than the audit itself, so the independence rules don't block it later. Package it as evidence for school district procurement.

## 2. Ratings
- **Customer need: 3.** The pre-release duty from July 2027 is real, but operators can write the assessment themselves and never file it. The outside audit waits until 2032 for anyone under $500M revenue.
- **Value over what customers use today: 3.** Clause-by-clause reports that rerun on every change beat free benchmarks plus a law-firm memo. But Alice and Circuit Breaker Labs already sell simulated red-teaming with regression testing.
- **Market size: 2.** My rough estimate is a few hundred US operators that knowingly keep minors, at about $50–80k in first-year contract value, so tens of millions of dollars. The largest operators build this themselves or buy from Alice.
- **Risk: 2.** Alice can add a California report template quickly. The federal GUARD Act, which would ban AI companions for minors, passed the Senate Judiciary Committee in April 2026 ([Congress.gov](https://www.congress.gov/bill/119th-congress/senate-bill/3062/text)). Tutors may argue they're outside the law. And an AI grader making legal pass/fail calls creates liability for us.

## 3. What would kill it, and the fastest test
It dies if teen-serving AI companies meet the requirement with in-house evaluations, free benchmarks and a lawyer's memo for under $10k, or if they exit minors or argue they're out of scope.

**Fastest test:** within 30 days, offer 25 teen-serving AI companies (tutors, school wellness, AI toys, character apps that keep teens) a fixed-fee $15k "Adam's Law readiness assessment" with a $5k deposit. Lead with a free 500-conversation scan of their public bot that shows its failures. If fewer than 3 pay the deposit, kill it.

VERDICT: PASS