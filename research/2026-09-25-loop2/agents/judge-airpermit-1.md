I researched this as a blind judge and read only METHOD.md in the repo, so no other project files shaped the scores. This is desk research, not customer validation.

## Claims checked against primary sources

**The enforcement statistic holds up.** I downloaded EPA's full ICIS-Air dataset (ECHO, dated Sep 20, 2026) and compared operating synthetic-minor facilities with formal actions since Sep 20, 2021:

| | Indiana | All US |
|---|---|---|
| Operating synthetic-minor facilities | 623 | 26,980 |
| With a formal action in 5 years | 176 (28.3%) | 7.4% |
| Actions | 237, almost all state agreed orders | |
| Median penalty | $1,400 (mean $7,054, 75th percentile $9,000) | |

- **Indiana is an outlier.** Its 28% is among the highest of the large states (NJ 27%, TN 18%, PA 17%, CO 14%). NY, IA, MI and OH are at 0.2–3%. The fear-of-enforcement pitch works in a handful of states, not nationally.
- **Most violations look like paperwork failures.** 740 of the 1,308 Indiana violation records are "FACIL" (facility-wide) rather than a pollutant. Published IDEM agreed orders cite missed quarterly deviation and compliance monitoring reports, with penalties of about $6,000–7,000. That is exactly what this product would prevent.
- **The Indiana customers are not mainly coaters.** By industry code, the largest groups are petroleum products, almost certainly asphalt plants (107), transportation equipment such as RV makers (60), fabricated metal (56), food (43), primary metals and foundries (43), grain wholesale (40), chemicals (38) and plastics (28).
- **The Indiana beachhead is small.** Covering all 623 synthetic minors at $9k is about $5.6M a year, before counting smaller-permit (MSOP) and registration holders.
- **The consultant fee range ($1,500–$20,000) is unverified.** No provider publishes prices. The IDEM annual FESOP fee is $6,100, a useful price anchor.

## Who else serves this customer

- **AirComply** (launched Sep 2, 2026): AI that reads the permit, tracks emissions and deadlines, and generates 20+ report types. It sells to consultants, facilities (priced per facility) and agencies, and offers reseller pricing to consulting firms. It is the closest software rival, but sells software, not a done-for-you service.
- **Encamp** (Indianapolis): serves 300+ enterprise customers across 32,000+ facilities and is the largest US Tier II filer. It launched its embedded AI, Scout, in May 2026. Enterprise-focused, not small plants.
- **Mapistry**: covers air, stormwater, spill plans and waste for mid-size and large manufacturers.
- **Legacy software**: ERA, VelocityEHS, Ecesis, EMTRACK, Sphera, Cority, Enablon. All are built for plants with environmental staff.
- **U.S. Compliance** (MN): sells outsourced EHS as "Compliance as a Service" to 2,200+ clients. This is the closest to the "we are your environmental department" model, but it is people-based and broad EHS.
- **Local consultants and free help**: Indiana firms such as Wilcox Environmental, and IDEM's free small-business assistance program (CTAP).

**Does anyone own the data or the buying channel?** No. The plant's purchase and safety-data-sheet data sits with its coating and chemical suppliers and in the plant's own files. The relationship sits with a fragmented set of local consultants. That leaves an opening, but consultants are both the competitor and the natural channel, which is why AirComply offers them reseller pricing. I found no company whose pitch matches this one almost exactly.

## 1. Strongest version

A fixed-fee, AI-run environmental department for plants holding synthetic-minor or small-source air permits, launched only in high-enforcement states (Indiana, then NJ, TN, PA).

- **Sales:** it sells from public lists. The IDEM permit database gives renewal dates and ECHO gives recent violators. The pitch is "never miss a quarterly report again, first quarter free."
- **Price:** set just under the consultant retainer it replaces. The IDEM FESOP fee ($6,100) is a price the plant already accepts.
- **Delivery:** an engineer reviews each filing. The software does the work between filings: reading the permit, taking in invoices and safety data sheets, running the 12-month rolling calculations, and chasing the plant for missing data.
- **Expansion:** the moat comes from adding more rule sets for the same plant: chemical inventory (Tier II), stormwater, spill plans, hazardous waste. That lifts revenue per plant toward $15–20k. Air alone is too small.
- **Optional:** buy one or two small local consultancies to acquire their books of clients.

## 2. Ratings

- **Customer need: 3.** The reports are legally required, and 28% of Indiana synthetic minors were penalized in 5 years. But the median fine is $1,400 and the national rate is 7.4%, so a missed report rarely costs much.
- **Value over today: 3.** AI makes reading permits and running calculations close to free and can beat consultants on price and reliability. But AirComply already sells the software, and plants still have to supply their own records.
- **Market size: 3.** About 27,000 US synthetic minors at about $9k is roughly $240M for air alone. Venture scale depends on expanding to the other permit types; the Indiana beachhead is about $5.6M.
- **Risk: 2.** It is a services business: it needs engineer labor and carries liability for drafted filings. It also depends on slow small-business sales and state-by-state rules, and must win against both AirComply-armed consultants and U.S. Compliance.

**Total: 11/20.**

## 3. What would kill it, and the fastest test

**What kills it:** plant managers treat a $1,400 fine every few years as cheaper than $6–12k a year. Or their current consultant already does this for about $3k. Or getting monthly records out of paper invoices and email turns each account into consultant-level labor, leaving service margins.

**Fastest test (about 2 weeks):**
1. Pull the 176 Indiana synthetic-minor facilities with recent formal actions from ECHO.
2. Call 50 plant managers or owners.
3. Offer to prepare their next quarterly report free, then $7,500 a year.
4. Ask each one what they pay now.

Fewer than 5 signed paid commitments or letters of intent, or a typical current spend under $4k, means pass.

This is close, and the test above could flip it. The need is real and verified. But it is thin where the pitch claims it is strongest, and the business leans toward services with a crowded software layer.

Sources:
- [EPA ECHO ICIS-Air downloads](https://echo.epa.gov/files/echodownloads/ICIS-AIR_downloads.zip)
- [AirComply](https://aircomply.com/), [AirComply pricing](https://aircomply.com/pricing.html), [Engineer Live on AirComply's launch](https://engineerlive.com/new-ai-platform-for-air-quality-permitting-and-compliance/)
- [Encamp Scout launch](https://www.prnewswire.com/news-releases/encamp-launches-compliance-platform-with-embedded-ai-accelerating-the-shift-to-proactive-ehs-management-302770998.html), [Encamp](https://encamp.com/)
- [Mapistry](https://www.mapistry.com/)
- [U.S. Compliance](https://www.uscompliance.com/blog/navigating-air-permits-a-guide-for-manufacturers-and-industrial-facilities/)
- [IDEM compliance due dates](https://www.in.gov/idem/ctap/compliance-due-dates/), [IDEM air permit timeframes and fees](https://www.in.gov/idem/airpermit/resources/timeframes-and-fees)
- [Wilcox Environmental Indiana compliance alert](https://www.wilcoxenv.com/air-permitting-annual-compliance-alert-indiana/)
- IDEM agreed orders (search results only; the pages themselves returned 404): [20450-A](https://www.in.gov/idem/oe/cause/AO/20450-A.htm), [24858-A](https://www.in.gov/idem/oe/cause/AO/24858-A.htm)
- [ERA Environmental](https://www.era-environmental.com/solutions/environmental/air), [VelocityEHS](https://www.ehs.com/solutions/environmental-compliance/air-emissions/), [Ecesis](https://www.ecesis.net/Air-Emission-Management-Software.aspx)

VERDICT: PASS
