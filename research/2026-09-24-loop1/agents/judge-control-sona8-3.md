I found a company whose pitch matches this one almost word for word: **Sona8**, a YC Fall 2026 company. It was founded in 2026, has 4 people in San Francisco, and its founders came from BCG and from AI research at TUM. Its YC page repeats the concept, including the 20-minute link, the "why is this step still manual" follow-ups, and the maps by site and team ([YC profile](https://www.ycombinator.com/companies/sona8)). Per your rule I treat Sona8 as this team. I judged the idea only, not the founders. It lists no customers, pricing or traction.

## Checking the claims

- **Transformations fail when frontline staff are left out.** Supported. McKinsey's transformation survey found that when a transformation didn't engage line managers and frontline staff, only 3% reported success. When those groups were engaged, success was 26% and 28%. The McKinsey page timed out, so I got these numbers from [consultancy.uk](https://www.consultancy.uk/news/13096/actively-engaging-frontline-staff-is-key-for-successful-transformation) ([McKinsey original](https://www.mckinsey.com/capabilities/people-and-organizational-performance/our-insights/successful-transformations)).
- **An AI interviewer can do this job.** Supported. In Geiecke and Jaravel's paper, accepted at the Review of Economic Studies, trained PhD students rated anonymized AI-led interview transcripts about as good as those of an average human expert interviewer ([SSRN](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=4974382)).
- **Scale and cost.** Supported. Superintelligent's voice agent interviewed 150 employees at a Fortune 100 client in two weeks for $500 in total ([Fractional AI case study](https://www.fractional.ai/case-study/automating-enterprise-discovery-superintelligents-ai-interview-agent)).
- **"Consultants spend weeks on interviews."** Only vendor marketing backs this, for example RubusAssess's "15–22 days down to 2–3". I found no primary source. It is plausible but unverified.

## Who else serves this customer

These all sell nearly the same product:
- **Horizon.** $3.5M seed led by NXTP in January 2026 ([Gunderson](https://www.gunder.com/en/news-insights/client-news/uruguayan-ai-startup-horizon-raises-35-million-usd-seed-investment)). Its site says it ran 1,581 interviews in 4 days at Mercado Libre, with a 93.2% completion rate, and lists PwC as a client ([customers](https://usehorizon.ai/customers)). It reports 12,000 interviews and 6x revenue growth in 2025.
- **Ontora.** YC-backed, targets companies of 300 to 3,000 employees, and cites 200+ employee conversations turned into an AI roadmap ([site](https://ontora.com/)).
- **Foaster.** YC Spring 2026. It sells the same thing as a service, with consultants reviewing the output ([YC](https://www.ycombinator.com/companies/foaster)).
- **RubusAssess** (formerly Mabel). Sold to independent consultants under their own brand, with 20–30 minute private links. It already offers a follow-up round of interviews ([site](https://rubusarc.ai/consultants)).
- **Superintelligent**, plus smaller tools such as Process Mapper, Maplo and ClearWork.

In the adjacent customer-interview market, Listen Labs raised a $69M Series B at a $500M+ valuation and reports eight-figure annualized revenue within nine months ([VentureBeat](https://venturebeat.com/technology/listen-labs-raises-usd69m-after-viral-billboard-hiring-stunt-to-scale-ai)). A secondary source reports Salesforce in talks to buy it for about $2B. That is unconfirmed ([Enterprise DNA](https://enterprisedna.co/resources/news/salesforce-listen-labs-2b-ai-customer-research-september-2026/)).

## Does an incumbent own the data or the buying channel?

- **The data:** no one owns it. What employees say about work done outside any system is not in the tools incumbents already sell.
  - Process-mining tools like Celonis and Skan read system logs and screen activity, so they miss manual and offline steps.
  - Employee survey platforms (Qualtrics, Workday Peakon, Perceptyx) own the HR survey channel and the employee roster, but not the transformation buyer. None has launched a comparable interview product that I found.
- **The buying channel:** partly owned. For the upfront interviews, consulting firms own the client relationship. They are both the channel and a possible builder of their own version; McKinsey's internal AI platform Lilli already covers 40,000+ consultants. The follow-up interviews after rollout have no clear owner.

## 1. The strongest version

The strongest version measures adoption during a change program, not just discovery at the start. Five funded competitors already do discovery, and its price is heading toward Superintelligent's $500 for 150 interviews.

- **Customer:** the internal owner of a large operational change at a multi-site company, such as an ERP migration, a shared-services consolidation or an integration after an acquisition. Plants, warehouses, clinics and operations centers are where system logs miss the most.
- **Product:** a baseline interview before rollout, then re-interviews of the same people at 30, 60 and 90 days. The output is a site-by-site list of where the change did not happen, and why.
- **Pricing:** a subscription for the length of the program, not per engagement.
- **Distribution:** consulting firms, systems integrators and private-equity operating partners resell it under their own brand, so the consulting channel carries it instead of competing with it. Private-equity firms buy again with each new acquisition.
- **Long-term aim:** the before-and-after record of each person's workflow becomes the company's living operating map. This is Sona8's own "enterprise context layer" goal.

## 2. Ratings for that version

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | In McKinsey's survey, transformations that left out line managers and frontline staff reported 3% success, versus 26–28% when those groups were engaged. |
| Value over what customers use today | 4 | 1,581 interviews in 4 days at Mercado Libre (Horizon), versus a few dozen consultant-run interviews, and AI transcripts rated about equal to an average human expert. |
| Market size | 3 | Discovery is a small line item inside engagements. Listen Labs reaching eight-figure revenue in the next-door market shows buyers will pay for AI interviews at scale, but the market for measuring change adoption is not proven. |
| Risk (5 = low) | 2 | At least five near-identical products are already shipping, and the core is easy to copy (Geiecke's interview platform is open source). German works councils can veto any system that could monitor employees ([Orrick](https://www.orrick.com/en/Insights/2024/09/AI-and-German-Co-Determination-What-Employers-Need-to-Know)). |

## 3. What would kill it, and the fastest test

**What kills it.** The product is used for one diagnostic and never renewed. The upfront interviews become a cheap commodity, and consulting firms either build their own or pay little, because interviews are hours they bill. Then the company becomes the sixth tool in a price war. A second risk is that employees don't speak candidly to an agent their employer deployed, which would make the maps worthless.

**The fastest test.** Offer 10 transformation leads who are already two or more months into a multi-site rollout a paid 60-day adoption readout across every site, priced for the length of the program. The test passes if, within three weeks:
- at least 3 sign a paid contract, and
- in those pilots, more than 60% of invited employees complete an interview without their manager pushing them, and most interviews name a specific broken step.

If both fail, what's left is a discovery product with no defensible advantage.

I backed it because the need is well documented and buyers are proving demand, with Horizon's revenue up 6x, 12,000 interviews in 2025 and PwC as a client. The adoption-tracking version has a recurring buyer that no incumbent controls. The backing depends on that follow-up loop selling, since interviewing alone is already crowded and cheap.

VERDICT: BACK
