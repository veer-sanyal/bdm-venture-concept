I did the research, and the answer is no: supplier search sold to mid-sized manufacturers is not a strong company as proposed. The data behind it is worth keeping, but the customer should flip. **Sell to the job shops, not the buyers:** each week, show a US contract manufacturer which companies are importing parts it could make, now that tariffs have narrowed the price gap. All of this is desk research. None of it is customer validation.

## Why the original version is weak

- **Buying the search:**
  - Standalone supplier-discovery companies are being bought and folded into bigger platforms. Coupa bought Scoutbee (Oct 2025), and Supplier.io bought Tealbook (Apr 2026).
  - Well-funded AI procurement agents already cover discovery, RFQs and follow-ups: Didero ($30M Series A, Feb 2026, 30+ customers), Keychain ($80.5M raised), Lumari and Vendra (both YC), Workus, Speya and Traza.
- **Free alternatives:**
  - Thomasnet is free for buyers.
  - Purdue MEP runs a supplier scouting service with a 30–45 day turnaround.
  - Sustainment ($12M Series A) already runs an Indiana supplier platform with Purdue MEP.
- **Need:** a mid-sized buyer looks for new suppliers only now and then. The generator's own note is also right: a one-time LLM-built index covers most criteria cheaply, so the search itself is not a moat.

## Don't build on Jev

- New signups were paused on 2026-09-22, so they may not be able to get access at all.
- §2.3(b) bans training a model on Jev's output, which rules out the usual way to cut costs later (training a cheaper model of your own).
- There is no SLA, and TypeSafe can suspend access immediately, so the whole company would rest on one vendor.
- §4.1 lets TypeSafe keep telemetry from customer data forever. Shops treat their customer lists as secret, and defense shops can't share controlled data this way.
- Jev only answers yes/no, and supplier specs are numeric.
- Speed doesn't matter much here: a nightly batch job is fine. Use ordinary LLMs for classification and data extraction.

## The reshaped company

**Customer.** US job shops and contract manufacturers with 10–249 employees: machining, fabrication, plastics, castings, electronics assembly.

**Pain.** The 2026 USA Reshoring Survey asked 249 manufacturers, 131 of them contract manufacturers:
- 32% of contract manufacturers are quoting reshoring work, up from 16% the year before.
- Only 45% of contract manufacturers are satisfied with how reshoring is going.

Secondhand figures from the same survey (not checked against the original):
- 94% of their lost orders go to imports on price.
- Imports compete on 38% of their quotes.

**The product.**
1. A shop uploads its equipment list, certifications and sample parts. An LLM turns these into a structured profile, including numeric limits like part size, tolerances and materials.
2. The index reads US sea import records, sorts shipments into part families (for example, "cast aluminum housings"), and attaches the tariff that now applies to each origin and tariff code.
3. Each week the shop gets a ranked list. Every entry names the importer, what it imports and from where, and the shipment records as evidence. It adds the tariff now applied, an estimated landed-cost gap, the buyer contacts, and a drafted total-cost-of-ownership pitch.
4. Shops log which leads turned into quotes and wins. Over time that outcome data is the moat.

**Why now.** Tariffs changed four times in 2026 (details under "Tariffs" below), and no shop can track which of its prospects just got more expensive.

**Why shops would pay.** They already pay for leads. About $57M of Xometry's 2025 services revenue came mostly from Thomasnet advertising, which is falling. MFG.com charges suppliers $2.5k–$20k a year. The closest existing offer is the Reshoring Initiative's manual Import Substitution Program. Its existence shows the job is real, but it doesn't publish prices.

**Start narrow, grow broad.**
1. Indiana shops, reached through Purdue MEP, the Indiana Manufacturers Association and local trade-group chapters.
2. Regional licenses for economic development groups and MEP centers.
3. A two-sided network, where importers post RFQs to shops they've already been matched with. That brings back the original buyer-side idea, with suppliers already on board.

## Against the four judging criteria

- **Customer need.** Stronger than buyer-side search, because it is tied directly to revenue. Still unproven: it needs interviews.
- **Value over alternatives.** Against ZoomInfo, Clay, Thomasnet and the free ImportYeti, the difference is matching at the part-family level plus a tariff-aware cost argument. A skilled user could copy it early by chaining ImportYeti and Clay, so it isn't defensible on day one.
- **Market size.** 2022 Census County Business Patterns counts 285,500 manufacturing establishments, 123,458 of them with 10–249 employees.
  - The core segments with 10–249 employees add up to about 32,500 establishments. That is an upper bound, since not all are contract shops.
  - At $6–12k a year that is roughly $200–400M. Reaching every import-exposed producer is about $1B.
  - This is the soft spot. The venture-scale answer depends on the network step.
- **Risk.** Covered in the next section.

## Main risks and how to test them

**Data coverage.**
- Public records cover sea freight only. Air and truck imports aren't public, and importers can ask for confidentiality.
- Freight forwarders often appear in place of the real importer.
- Parts nearshored to Mexico arrive by truck under USMCA, so they are both invisible and exempt from the new tariffs.
- **Kill test:** build lists by hand for 5 Indiana shops. Stop if owners rate fewer than 30% of the accounts as worth pursuing.

**Conversion.**
- Half of shops face import quotes 30% or more below their own, and deals take 3–18 months to close.
- **Test:** 3 shops each send about 50 pitches. Measure how many RFQs come back within 6 weeks.

**Willingness to pay.**
- **Test:** ask for a $500 paid pilot before the competition.

**Policy swings.**
- The pitch has to hold up on total cost, not tariffs alone. 53% of contract manufacturers cite geopolitical risk as the reason their customers reshore, which helps.

**Competition.**
- Sustainment already has the Purdue MEP channel, Thomasnet has a new ad platform, and there is the Reshoring Initiative's program.

**Before the competition:** do 20 interviews with shop owners, asking how they found their last 3 customers and what they spend on Thomasnet, sales reps and trade shows. Then run the hand-built lists, measure RFQs, and ask for paid pilots. Those numbers are the evidence to put in front of the judges.

**Bottom line:** this is a credible competition entry and a plausible seed-stage company, but not an obvious venture-scale winner. Whether it gets there depends on the two-sided network.

**Tariffs, for reference:**
- **IEEPA tariffs:** the Supreme Court struck them down on Feb 20, 2026. A temporary 10% tariff (Section 122) replaced them.
- **Section 122:** it expired on July 24, 2026 and was replaced by new 10–12.5% tariffs on about 60 economies (Section 301). For China these stack on the existing 25%, for 37.5% total. Goods that qualify under USMCA are exempt.
- **Metals (Section 232), since April 6, 2026:**
  - 50% on primary metals.
  - 25% on products that are more than 15% metal, charged on the full customs value.
  - 10% where the metal was melted in the US.

Sources:
- [Didero Series A (TechCrunch)](https://techcrunch.com/2026/02/12/didero-lands-30m-to-put-manufacturing-procurement-on-agentic-autopilot/)
- [Coupa acquires Scoutbee](https://www.coupa.com/newsroom/coupa-announces-acquisition-of-ai-powered-scoutbee-to-drive-supplier-intelligence-and-discovery/)
- [Supplier.io acquires TealBook](https://www.sdcexec.com/sourcing-procurement/procurement-software/news/22963703/supplierio-supplierio-acquires-tealbook)
- [Keychain Series B](https://www.prnewswire.com/news-releases/keychain-raises-30-million-series-b-and-launches-keychainos-an-ai-operating-system-set-to-power-the-future-of-cpg-manufacturing-302532859.html)
- [Keychain funding total (Tracxn)](https://tracxn.com/d/companies/keychain/__6bDVqRxr4EF11CNy0BRig58k4CGIwROSkzQgaGRcwGM)
- [Vendra (YC)](https://www.ycombinator.com/companies/vendra)
- [Lumari launch](https://fondo.com/blog/lumari-launches)
- [Find My Factory funding](https://arcticstartup.com/find-my-factory-raises-e1-18-million/)
- [Traza pre-seed](https://venturebeat.com/orchestration/traza-raises-usd2-1-million-led-by-base10-to-automate-procurement-workflows-with-ai)
- [Sustainment and Purdue MEP](https://www.sustainment.com/mep-network-partnerships/purdue-mep)
- [Sustainment Series A](https://www.prweb.com/releases/sustainment-supply-chain-technology-platform-closes-12m-series-a-financing-led-by-unless-899419757.html)
- [Purdue MEP supplier scouting](https://mep.purdue.edu/services/supplier-scouting-network/)
- [Xometry FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1657573/000119312526066959/xmtr-20251231.htm)
- [Thomasnet pricing (third-party estimate)](https://www.topbubbleindex.com/blog/thomasnet-pricing-reviews/)
- [MFG.com (Wikipedia)](https://en.wikipedia.org/wiki/MFG.com)
- [2026 USA Reshoring Survey (The Fabricator)](https://www.thefabricator.com/thefabricator/news/shopmanagement/us-reshoring-momentum-builds-despite-policy-and-workforce-challenges)
- [Survey detail (Constiv, secondhand)](https://constiv.substack.com/p/reshoring-in-the-us-96-satisfied)
- [Reshoring Initiative Import Substitution Program](https://www.reshorenow.org/import-substitution-program/)
- [ImportYeti data coverage](https://www.importyeti.com/our-data)
- [Supreme Court IEEPA ruling (WilmerHale)](https://www.wilmerhale.com/en/insights/client-alerts/20260220-supreme-court-strikes-down-ieepa-tariffs-what-now)
- [Section 301 tariffs from July 24, 2026 (Honigman)](https://www.honigman.com/alert-3462)
- [Section 232 changes, April 2026 (C.H. Robinson)](https://www.chrobinson.com/en-us/resources/insights-and-advisories/client-advisories/2026q2/04-06-2026-us-expands-n-increases-sec232-tariffs-on-aluminum-steel-n-copper-effective-apr-6/)
- [Census County Business Patterns 2022](https://www2.census.gov/programs-surveys/cbp/datasets/2022/cbp22us.zip)
- [TypeSafe Master Customer Agreement](https://typesafe.ai/legal/mca)