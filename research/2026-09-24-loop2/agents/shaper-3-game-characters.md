The idea as proposed isn't a strong company. The strongest version I can build keeps its core mechanism: AI works out what the user means, but the character only says lines people wrote. It drops the game market, the cost-cutting pitch, and TypeSafe as the supplier. It then points that mechanism at makers of AI toys and brand owners who license characters for kids. A California law signed on 2026-09-10 bans the way their products currently work, starting January 1, 2027. Everything below is desk research, not customer validation.

## Why the idea fails as proposed

- **Building on TypeSafe isn't workable.** I read the agreement myself (last updated 2026-09-23). §4.1(c) lets TypeSafe keep customer data "in perpetuity" to generate telemetry. §4.3 defines telemetry to include "classifications … and learnings," which TypeSafe may use "without restriction." The agreement has no service-level commitment, and TypeSafe can suspend immediately for a breach.
  - §2.3(a) says the service can't be offered "as a standalone service." A middleware API sold to studios is exactly what that clause risks.
  - §2.3(b) bans using Jev's outputs to train a model. That blocks the natural path to a cheap model running on the device.
  - Signups opened September 20 and paused September 22.
  - I could not confirm the claims about enterprise-only zero data retention or the lack of a BAA; neither is in the agreement itself.
  - A naming problem: "Jev" is TypeSafe's model, not the product. The company needs its own name.
- **Cheaper inference is not a defensible advantage.** Roblox's text generation API for creators is free during its beta. Krafton's PUBG Ally runs a 2B-parameter model on the player's own GPU. Jev's own launch coverage reports calls of about 100 ms (range 70–500) at $0.042 per million input tokens. My rough math, assuming 100k daily players × 30 decisions × 2k tokens: about $90k a year on Jev versus about $260k on a cheap LLM. That is roughly 3x, not 10–25x. I could not source the "$0.5–2M a year" figure.
- **Demand in games is weak.**
  - Inworld raised at a $500M valuation to build AI game characters, and has since repositioned as infrastructure for consumer apps.
  - In GDC's 2026 survey, 52% of developers said generative AI hurts the industry, up from 18% two years earlier. Writers and designers were among the most negative, at 63%.
  - Replica Studios, which had a SAG-AFTRA deal for AI voices, shut down in June 2025.

## The company I would build: bounded characters for children's products

**Product.** An engine that understands a child's free speech or text, then picks among lines and actions that writers approved and voice actors recorded. It can never say anything else. It comes with three pieces:
- An authoring studio where AI drafts candidate lines for writers to approve.
- Coverage analytics that show what kids asked that no line answers.
- A compliance dossier the customer can hand to retailers.

It runs on open-weight models on the device or on the customer's own servers. It deliberately has no memory of the child across sessions.

**Why now.**
- **SB 867, signed 2026-09-10.** From January 1, 2027 until 2031, it bans making or selling toys for children under 16 that contain a "companion chatbot." That means responses that are "adaptive, human-like" and able to "sustain a relationship across multiple interactions."
  - Ballard Spahr notes there is no way to comply through filters, testing or parental controls. The product has to be redesigned so it falls outside the definition.
  - The Assembly committee analysis contrasts LLM toys with Hello Barbie, which "relies on pre-recorded responses." It also says the bill doesn't prohibit "ordinary interactive toys."
  - California retailers asked for a "knowingly" liability standard. That suggests retailers will want proof of compliance.
- **SB 1119 ("Adam's Law"), also signed 2026-09-10.** Companion chatbots used by minors face core obligations from July 1, 2027, and independent audits certified under penalty of perjury. The engine's output is a finite list of lines, so an auditor can read every one.
- **Real buyers.**
  - China has 1,500+ AI toy makers, some exporting to the US (FoloToy). BubblePal has sold 200k+ units and licenses Peppa Pig and Ultraman.
  - Mattel and OpenAI delayed their product and aimed it at older users.
  - FoloToy's Kumma bear was pulled after telling testers about knives and sex.
- **Evidence the approach can work.** PBS KIDS' Elinor research used exactly this design: AI classifies the child's answer, then the character picks a scripted reply. Kids learned more and engaged more. The same research found kids stopped engaging when the character didn't seem to understand them, so understanding quality is the metric the product lives or dies on.

**Start narrow, grow broad.**
1. AI toys and licensed-character toys (toy makers and licensors).
2. Kids' learning apps.
3. All-ages games:
   - Roblox rates chatbot-style AI experiences "Restricted" (18+).
   - SB 243's video-game exclusion covers characters that stay on game topics, which this engine guarantees by design.
4. Any brand or regulated setting where every sentence needs approval in advance.

**Business model (hypothesis to test).** A per-unit or per-active-user license, plus paid seats in the authoring studio for licensors.

**What gives it an edge.** Understanding of how children actually speak, tuned over time. Coverage data across many products. Fitting into licensors' existing approval of every line.

**How it scores on the judging criteria.**
- **Need:** a hard legal deadline with no filter-based way out.
- **Value over alternatives:** LLM toys are banned for under-16s in California. Fixed-script toys lose kids once they aren't understood. An in-house intent classifier is the main competitor.
- **Market:** starts small. Size estimates for the AI toy market range from $2.7B to $18B, so treat them as unreliable.
- **Risk:** see below.

## Risks that could kill it

1. **The law may still cover it.** A court might read "adaptive" to include choosing among pre-written lines. This is the whole company, and it needs a lawyer's opinion. The Toy Association says it will issue compliance guidance.
2. **PullString, the company behind Hello Barbie, is a close precedent.** It raised $44M for authored conversational characters and sold to Apple for about $30M plus earn-outs. Hello Barbie also drew privacy backlash and remembered what kids said for weeks.
3. **Toy makers might just build intent matching in-house,** or drop AI from California-bound products.
4. **Toy lines lock 12–18 months ahead,** and the customer base is concentrated in a few large firms.
5. **Children's-data rules.** COPPA's separate-consent and retention rules have been in force since 2026-04-22. This is another reason not to send children's data to a supplier that keeps telemetry forever.

## Next validation step

Veer and Cole should interview 15–20 people before the pitch. The targets are compliance and licensing leads at toy makers and licensors, AI toy exporters, and a children's-product lawyer. The questions: what will you ship in California on 2027-01-01, and would you pay for a certifiably bounded design?

## Sources
- [TypeSafe MCA](https://typesafe.ai/legal/mca)
- [Jev deep dive (latency, pricing, signup pause)](https://flaviocopes.com/jev/)
- [SB 867 text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB867)
- [SB 867 Assembly committee analysis](https://apcp.assembly.ca.gov/system/files/2026-06/sb-867-padilla-apcp-analysis.pdf)
- [Ballard Spahr on SB 867](https://www.ballardspahr.com/insights/alerts-and-articles/2026/09/california-ai-toy-bill-brings-software-behavior-into-product-safety)
- [Toy Association on SB 867 / SB 1119](https://www.toyassociation.org/PressRoom2/News/2026-News/california-governor-signs-ai-toy-and-chatbot-bills-into-law.aspx)
- [CSA note on SB 1119 audits](https://labs.cloudsecurityalliance.org/research/csa-research-note-california-ai-chatbot-audit-mandate-202609/)
- [SB 243 text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB243)
- [Roblox generative AI rules](https://create.roblox.com/docs/generative-AI)
- [Roblox Text Generation API](https://devforum.roblox.com/t/text-generation-api-beta-expanding-access/3952348)
- [PUBG Ally on-device model](https://developer.nvidia.com/blog/how-krafton-built-pubg-ally-a-co-playable-character-powered-by-nvidia-ace/)
- [Inworld repositions to consumer apps](https://gamesbeat.com/inworld-runtime-is-1st-ai-runtime-for-consumer-apps/)
- [GDC 2026 survey](https://gdconf.com/article/gdc-2026-state-of-the-game-industry-reveals-impact-of-layoffs-generative-ai-and-more/)
- [Replica Studios shutdown](https://multilingual.com/replica-studios-shutdown-2025/)
- [Kumma bear pulled](https://www.cnn.com/2025/11/19/tech/folotoy-kumma-ai-bear-scli-intl)
- [Mattel/OpenAI delay](https://sherwood.news/tech/report-openai-and-mattel-hit-pause-on-ai-toys/)
- [China AI toy market](https://hellochinatech.com/p/china-ai-toys-35-billion-industry)
- [PBS KIDS Elinor study](https://www.the74million.org/article/kids-cartoon-characters-that-use-ai-to-customize-responses-help-children-learn/)
- [PullString acquisition](https://techcrunch.com/2019/02/15/apple-buys-pullstring-toytalk/)
- [COPPA amended rule](https://www.finnegan.com/en/insights/articles/coppas-amended-rule-is-now-in-full-effect-what-operators-need-to-know.html)
- [Where Winds Meet NPC exploits](https://www.pcgamer.com/games/rpg/wuxia-mmo-where-winds-meet-is-full-of-ai-chatbot-npcs-and-people-are-doing-all-the-standard-obscene-stuff-to-them-i-made-him-think-that-my-character-was-pregnant-with-his-child/)