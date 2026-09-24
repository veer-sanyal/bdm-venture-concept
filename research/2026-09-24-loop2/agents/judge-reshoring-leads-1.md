I'd pass. The problem is real, but this version runs into three things at once: the market is small, public shipping records are weaker than the pitch needs, and the tariff trigger has kept moving.

**What the claims check against**
- **Mostly true: "32% quoting reshoring, double last year."** This comes from the 2026 USA Reshoring Survey (Reshoring Initiative with Regions Recruiting). It covered 249 manufacturers: 118 OEMs and 131 contract manufacturers. 32% of the contract manufacturers were quoting reshoring work, up from 16%, and 79% said customers had raised reshoring with them.
- **True but thin: "45% satisfied."** I found it only in a secondary write-up of the survey, not the Reshoring Initiative's own pages. It's 12% extremely plus 33% somewhat satisfied, from roughly 40 to 50 respondents.
- **Overstated: "they lose most of it to imports on price."** The data says 38% of quotes faced an import competitor, and price was the reason in 94% of those losses. Half of the shops losing on price faced import quotes 30% or more below theirs. Nothing shows shops lose *most* of this work.
- **Only partly true: "import costs jumped after the 2026 tariff changes."**
  - For many goods, costs fell. The Supreme Court struck down the IEEPA tariffs on Feb 20, 2026. They were replaced by a Section 122 tariff (10%, briefly announced at 15%), which the trade court ruled unlawful in May and which expired July 23. From July 24, new Section 301 tariffs of 10–12.5% cover 60 countries.
  - The real jump is in metal. Since April 6, 2026, the Section 232 tariffs on steel, aluminum and copper parts apply to the full customs value, at 50% or 25%. That hits machined, fabricated and cast parts directly.
  - Tariffs also hurt the shops: 57% of contract manufacturers say the 2025 steel and aluminum tariffs made them less competitive.
- **The data can't fully deliver the pitch.**
  - Only sea shipments are public. Air, truck and rail records are not, so imports from Mexico and Canada are mostly invisible.
  - Importers can ask customs to hide their names.
  - Shipping records carry no value, and product codes are guessed from the description. So "tariff now applied" and "landed-cost gap" can only ever be estimates.

**Who else serves this customer**
- **The same service, done by hand:** the Reshoring Initiative's Import Substitution Program says it "identifies and qualifies major importers of what you produce," and sells custom versions to MEP centers (the government-backed manufacturing extension centers) and economic development agencies. MEP centers also run free supplier-scouting.
- **Raw shipment data:** ImportYeti (free), ImportGenius, Panjiva, Descartes Datamyne.
- **AI sales-lead tools:** SUPPLYCO sells buying-signal leads to contract manufacturers but lists no import data. Vunve and EximAgent write outreach from customs records, but for exporters.
- **Quoting software:** Uptool ($6M seed) and Paperless Parts.

No company matched this pitch closely enough to treat as the team. The incumbent that matters is Xometry/Thomasnet. It owns the buyer channel (sourcing searches, a marketplace, 500k supplier listings) but not this matching data. No one owns the importer-to-shop match.

**1. The strongest version**
- **Customer:** metal parts only (machining, fabrication, castings and forgings). That's where the April 2026 metal tariff change actually closes a 30%+ price gap. Drop plastics and electronics, where 2026 tariffs mostly fell.
- **Product:** the weekly list, filtered to imports from Asia and Europe that face both the metal tariff and the China tariffs.
- **Pricing:** a platform fee of about $3–6k a year plus a commission of about 3% on won work, like the manufacturer's reps shops already pay.
- **Sales channel:** sell through MEP centers, state development agencies and trade groups (the national machining association, the fabricators' association, the foundry society). They already pay for import-substitution work, which avoids selling to shops one at a time.
- **Moat:** a record of which shipment, part and shop matches actually won.

**2. Ratings**

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 3 | Reshoring quoting doubled to 32%, but the metalworking index for August 2026 shows backlogs steady and lead times long, and labor is the top constraint. Many shops are short of capacity, not leads. |
| Value over what customers use today | 3 | Better than ImportYeti plus a manual Import Substitution study, but the tariff and cost-gap figures are estimates because shipping records lack value and exact product codes. |
| Market size | 2 | Thomasnet's paid supplier services, selling to 500k suppliers, made only $59.6M in 2024 and shrank 13%. Roughly 30k target shops at $9k is about $270M in theory. |
| Risk (5 = low) | 2 | Three tariff regimes in six months, two struck down in court. The core data misses Mexico, Canada and air freight, and can hide importer names. |

**3. What kills it, and the fastest test**

It dies if importers in the pitches don't reply with RFQs, because the price gap remains or the matches are wrong. Then shops won't renew.

The fastest test is a 4-week hand-run pilot with 10 metal shops. Build their lists yourself from ImportYeti or ImportGenius plus a tariff lookup, and have each shop send about 50 pitches. Kill it if fewer than 30% of leads are parts the shop agrees it can make, or fewer than 2 RFQs come back per 100 pitches, or fewer than 3 of the 10 shops prepay to continue.

Sources:
- [2026 survey figures via Supply Chain Dive](https://www.supplychaindive.com/news/more-oems-plan-reshoring-investments-despite-tariff-cost-uncertainty/829667/)
- [Contract manufacturer detail (secondary write-up)](https://constiv.substack.com/p/reshoring-in-the-us-96-satisfied)
- [Quality Magazine](https://www.qualitymag.com/articles/99885-the-results-are-in-2026-reshoring-survey-momentum-builds-despite-policy-and-workforce-challenges)
- [WilmerHale on the IEEPA ruling](https://www.wilmerhale.com/en/insights/client-alerts/20260220-supreme-court-strikes-down-ieepa-tariffs-what-now)
- [Section 122 status](https://gingercontrol.com/blog/section-122-tariffs-explained)
- [Honigman on the new Section 301 tariffs](https://www.honigman.com/alert-3462)
- [Federal Register Section 301 notice](https://www.federalregister.gov/documents/2026/07/28/2026-15181/notice-of-actions-in-section-301-investigations-of-acts-policies-and-practices-of-various-economies)
- [C.H. Robinson on the Section 232 changes](https://www.chrobinson.com/en-us/resources/insights-and-advisories/client-advisories/2026q2/04-06-2026-us-expands-n-increases-sec232-tariffs-on-aluminum-steel-n-copper-effective-apr-6/)
- [19 CFR 103.31](https://www.law.cornell.edu/cfr/text/19/103.31)
- [Federal Reserve paper on shipping-record data](https://www.federalreserve.gov/econres/feds/files/2021066pap.pdf)
- [Import Substitution Program](https://www.reshorenow.org/isp/)
- [SUPPLYCO](https://www.supplyco.ai/industries/contract-manufacturing)
- [Uptool](https://www.prnewswire.com/news-releases/uptool-launches-from-stealth-with-ai-platform-to-accelerate-us-manufacturing-302678518.html)
- [Vunve](https://www.vunve.com/en)
- [ImportYeti](https://www.importyeti.com/)
- [Xometry results](https://investors.xometry.com/news-releases/news-release-details/xometry-reports-record-second-quarter-2025-results/)
- [Gardner metalworking index, August 2026](https://www.mmsonline.com/articles/metalworking-index-softens-in-august-but-production-strengthens)
- [MEP supplier scouting](https://www.nist.gov/mep/supply-chain/supplier-scouting)

VERDICT: PASS