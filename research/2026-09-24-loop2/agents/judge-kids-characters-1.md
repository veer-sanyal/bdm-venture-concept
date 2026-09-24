**Verdict in brief:** the law is real and forces toy makers to redesign. But the product that survives the law is a talking toy limited to recorded lines, which has already failed commercially once. Buyers have cheaper ways to comply, and the market is small and has a legal end date. I would pass.

## Checking the key claims against primary sources

- **The law: confirmed.** SB 867 is Chapter 189, signed September 10, 2026. It adds Business and Professions Code §22604.5, which bans making, selling, or offering to a retailer "any toy that includes a companion chatbot." A toy means a product for children under 16. The ban is repealed on January 1, 2031. The Toy Association and the author's office give January 1, 2027 as the start date; the text itself has no date, so it takes effect then by default.
  - **Definition:** a companion chatbot is an "AI system with a natural language interface that provides adaptive, human-like responses... and is capable of meeting a user's social needs, including by exhibiting anthropomorphic features and being able to sustain a relationship across multiple interactions."
  - **Enforcement:** the same private lawsuit right as SB 243, with damages of at least $1,000 per violation. There is no requirement that the seller knew. The California Retailers Association asked for a "knowingly" standard and did not get it.
- **"Filters and parental controls can't make an LLM toy comply": confirmed.** Ballard Spahr says a covered toy stays banned "even if the manufacturer added content filters, parental controls, or session limits." The only way out is to change the product so it no longer meets the definition.
- **Would recorded lines with no memory comply? Plausibly, but untested.** The Assembly committee analysis contrasts Hello Barbie, "which relies on pre-recorded responses," with today's LLM toys. That analysis is not binding, though. A plaintiff could still argue that an AI picking lines in response to a child counts as "adaptive, human-like responses."
- **New York is weaker support than it looks.** Its chatbot-toy ban (S9408A / A11144B) passed both houses and went to the governor on June 2. I found no signature. Its definition of an AI companion requires memory of past sessions *and* unprompted emotional questions *and* ongoing personal dialogue. So an LLM toy that simply drops memory already escapes New York; approved-lines-only adds nothing there.

## Who else serves this customer

- **Exact-match company:** the closest is historical. PullString (formerly ToyTalk, the maker of Hello Barbie) sold writer-authored dialogue plus speech understanding and an authoring tool. It raised $44M and was acquired by Apple in 2019 for about $30M plus earn-outs. Treat it as "this team" last time: the concept worked technically but was a small business. Hello Barbie itself was pulled from the market.
- **Buying channel:** most toy brands buy electronics from contract manufacturers and chip-module vendors. Espressif's ESP32 reference designs already wire toys to OpenAI or ByteDance's Doubao models. Chinese contract manufacturers such as Kinwin already advertise on-device intent recognition with "pre-defined dialogue trees." Sensory, whose customers include Hasbro, sells a no-code voice-command builder (VoiceHub).
- **Big character owners build in-house or stay out.** Hasbro's Sixth Wall studio runs on its own CharacterOS system, limits AI characters to ages 13 and up, and deliberately keeps them out of children's toys. Mattel delayed its OpenAI product and will aim it at "older customers and families."
- **Existing AI toy makers** have their own escape routes. Miko has a toggle that turns conversational AI off entirely. Curio relies on filters and parental controls.
- **Does an incumbent own the customer's data or buying channel?** No one owns the data on what children ask; each toy maker holds its own. The buying channel is owned by contract manufacturers and chip vendors for the long tail of brands, and by in-house teams at the big character owners.

## 1. The strongest version

Narrow the pitch from "an SB 867 compliance engine" to **the only way to put a licensed under-13 character into a talking product anywhere**. It would be a runtime that plays only approved, recorded lines and keeps no memory. The authoring studio would build in the character owner's line-by-line approval step. The compliance file would be written to pass retailer review.

- **Customers:** character owners and their main toy licensees, not the whole AI-toy long tail.
- **Pricing:** a fee per product plus a royalty per unit sold.
- **Near-term wedge:** paid conversions of existing LLM toy products so they can be sold in California for holiday 2027.
- **Moat:** the analytics on questions no line answers. That data drives new content packs, which fight the pattern where children abandon AI toys after about two weeks.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 3/5 | The ban has no filter-based way to comply, and retailers are liable without knowledge. But brands have cheaper outs, such as Miko's AI-off toggle or dropping memory. |
| Value over what customers use today | 2/5 | Contract manufacturers already sell intent recognition with scripted dialogue trees. What is left (AI-drafted lines, gap analytics, a compliance file) is features, not a platform. |
| Market size | 2/5 | China's whole online AI-toy market in 2025 was 740M yuan on 1.6M units; the leader, BubblePal, sold about 300k units. At a few dollars per unit, and with most of the legal pressure in California until 2031, revenue stays small. |
| Risk (5 = low) | 2/5 | Scripted, memory-less toys run out of things to say; Chinese AI toys see 20–40% return rates and kids abandon them in about two weeks. There is also legal ambiguity, a 2031 sunset, and the engine is easy to copy. |

## 3. What would kill it, and the fastest test

**What kills it:** buyers won't pay. Either stripping memory or switching AI off in California is good enough for them, or scripted toys lose on retention the way Hello Barbie did.

**Single fastest test (about 3 weeks):** offer a paid conversion pilot, around $25k to make one product California-sellable, to the roughly 15–20 brands now selling conversational AI toys in US retail. That list includes Curio, Miko, FoloToy, Haivivi/BubblePal, Skyrocket, Snorble, KEYi/Loona and Elato. Kill the idea if fewer than 3 sign a paid pilot or letter of intent before holiday-2027 line reviews close.

Sources:
- [SB 867 bill text](https://leginfo.legislature.ca.gov/faces/billTextClient.xhtml?bill_id=202520260SB867)
- [Assembly Privacy Committee analysis](https://apcp.assembly.ca.gov/media/1168)
- [Ballard Spahr](https://www.ballardspahr.com/insights/alerts-and-articles/2026/09/california-ai-toy-bill-brings-software-behavior-into-product-safety)
- [Toy Association](https://www.toyassociation.org/PressRoom2/News/2026-News/california-governor-signs-ai-toy-and-chatbot-bills-into-law.aspx)
- [NY S9408](https://www.nysenate.gov/legislation/bills/2025/S9408)
- [Hasbro Sixth Wall](https://www.businesswire.com/news/home/20260603297922/en/Hasbro-Launches-Sixth-Wall-a-New-AI-Studio-Building-the-Next-Generation-of-Character-Experiences) and [coverage](https://ground.news/article/hasbro-launching-an-ai-studio-that-will-let-companies-license-its-stable-of-characters)
- [Mattel delay](https://www.axios.com/2025/12/15/mattel-openai-toys-kids)
- [PullString acquisition](https://techcrunch.com/2019/02/15/apple-buys-pullstring-toytalk/)
- [Two-week wall](https://hellochinatech.com/p/chinas-ai-toys-two-week-wall)
- [China AI toy market](https://moojing-global.com/news-research/china-ai-toys-market-growth-2025)
- [Kinwin](https://kinwintoys.com/ai-powered-plush-toys-2026/)
- [Sensory VoiceHub](https://sensory.com/product/voicehub/)
- [Espressif LLM solution](https://docs.espressif.com/projects/esp-techpedia/en/latest/esp-friends/solution-introduction/ai/llm-solution.html)
- [Miko metrics](https://inc42.com/company/miko/latest/)
- [KQED on Miko and Curio](https://www.kqed.org/news/12070850/steer-clear-of-ai-companion-toys-for-kids-another-advocacy-group-warns)

VERDICT: PASS