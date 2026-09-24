**Verdict: pass.** The requirement is real. But the $500–1,200 per site per year product is a thin layer between tools that already hold the test data and the study models, and too few sites can use it.

## Checking the claims

- **NFPA 70B:** accurate. The 2023 edition turned 70B into a mandatory standard. It requires one-line diagrams to be kept legible (6.2.1) and accurate (6.2.2). Short-circuit and coordination studies must be reviewed at least every 5 years (6.3.3, 6.4.3). The arc flash analysis must be updated "when changes occur… that could affect the results" (6.7.1) and reviewed every 5 years or sooner (6.7.2). NFPA 70E 130.5(G) says the same about arc flash. Two caveats:
  - A review is not a redo. The standards only require an update when something has changed.
  - Neither standard is law on its own. OSHA enforces 70B indirectly at best.
- **Schneider's 89%:** mostly accurate. Schneider's blog says 89% of 400 audited sites had no one-line diagram *or only a partial one*, and 79% had obsolete equipment. It does not say the sites were in the US. I could only see this through search results, because the blog blocked direct fetches.
- **The failure the product targets:** well documented. Changed trip settings invalidate labels. Studies built on catalog settings instead of the settings actually in the field are a known common error.
- **Pricing context:** a new study costs about $3.5k–22k+ per site; one source puts it at $12k–86k. Updates stay expensive mainly because the field check has to be repeated.

## Who already owns this customer's data and buying channel

Yes, incumbents own both, in pieces:
- **The test data:** Megger's PowerDB is test data management software built around NETA test forms. I couldn't find market-share figures for it.
- **The study models:** ETAP 21 includes a field data app (etapAPP 6.0) and a "relay settings change management" tool that syncs settings between a physical relay and the ETAP model (eProtect). EasyPower has its OnSite field app. SKM has SKM Mobile.
- **Closest analogue: Egalvanic.** Its founder owns a third-party testing company. It sells to contractors and testing companies. It "digitize[s] nameplate OCR, thermal images, and testing results at the point of inspection… integrating with engineering software (SKM/ETAP) to keep models current." It does not advertise diffing relay files against the model or linking each value to its source, so I treat it as a competitor, not this team.
- **Gimba:** a white-label NFPA 70B platform for contractors that imports SKM and ETAP study files. Contractors typically charge clients 2–3x what Gimba costs them.
- **REALTIMEais and NorthGrid:** electrical maintenance and compliance software that also covers arc flash.
- **The buyers are consolidating.** Blackstone agreed to buy Shermco for about $1.6B, and Shermco keeps acquiring NETA firms. The big testing roll-ups also do the studies themselves, so they can build or buy this.

## 1. Strongest version

Narrow it to **turning each maintenance visit into the 5-year study review**:
- Read the as-found data the technician already captures: PowerDB exports, relay setting files, and photos of trip-unit dials.
- Compare only the protective devices and settings against the study model.
- Produce a report the engineer signs off, listing the changes to the study and the labels that are now wrong, each linked to its source.
- Have it prepare the quote for the update work.

Sell it to mid-size NETA firms that do studies in-house, because they already hold the model files. Charge per report or take a cut of the update work it generates, not a flat annual fee per site. The pitch to the firm: required reviews become billable desk work with no second field trip.

## 2. Ratings

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 3 | 70B 6.7.1–6.7.2 require updates after changes, and 89% of audited sites lacked a complete one-line. But the pain is the facility's; for the testing firm it is upside, and enforcement is weak. |
| Value over today | 3 | Automatic comparison with sources is new. But ETAP already syncs relay settings to the model, and EasyPower OnSite, SKM Mobile and Egalvanic already move field data into models. |
| Market size | 2 | North American electrical testing services are about $2.78B (2024). Sites that have a current model *and* a regular testing contract are a small slice. At about $800 per site, this is plausibly a sub-$100M revenue ceiling (my rough estimate). |
| Risk (5 = low) | 2 | The model file often belongs to a different engineering firm. Four model formats need parsing: three proprietary study tools plus relay setting files. PowerDB and ETAP sit on each side of the data. The buyers are PE roll-ups that can build this themselves. There is liability for missed changes. |

## 3. What kills it, and the fastest test

**What kills it:** at most sites they maintain, the testing firms don't hold the current ETAP/SKM/EasyPower model, or they do but facilities won't pay for the flagged update work. Either way, there is nothing to compare against or no revenue to resell.

**Fastest test (about one week):** ask 10 operations leads at NETA-accredited firms for last quarter's list of 70B maintenance sites. Have them mark which sites they hold a current model file and as-found settings for. If fewer than about 30% qualify, stop. If more qualify, compare 10 of those sites by hand and count how many flags turn into a signed update order. All of the above is desk research; none of it is customer validation.

Sources: [Schneider blog (via search result)](https://blog.se.com/infrastructure-and-grid/power-management-metering-monitoring-power-quality/2022/04/25/danger-are-your-electrical-single-line-diagrams-out-of-date-or-missing/) · [Gimba on 70B Ch. 6](https://gimba.io/nfpa-70b-chapter-6-single-line-diagram-system-studies/) · [Gimba contractors](https://gimba.io/nfpa-70b-electrical-contractors/) · [NFPA 70E 130.5(G) summary](https://industrialmonitordirect.com/blogs/knowledgebase/nfpa-70e-arc-flash-label-requirements-and-analysis-update-intervals) · [ETAP 21](https://etap.com/product-releases/etap-21-release) · [etapAPP](https://etap.com/product/etapapp) · [EasyPower OnSite](https://www.easypower.com/resources/article/data-collection-part-3-mobile-data-collection-with-easypower-onsite) · [SKM data collection](https://www.skm.com/DataCollection.html) · [Megger PowerDB](https://us.megger.com/test-data-management-software-powerdb) · [Egalvanic](https://www.egalvanic.com/) · [Egalvanic origin](https://www.egalvanic.com/post/why-we-built-egalvanic-the-future-of-ai-driven-electrical-maintenance-and-reliability) · [Egalvanic article](https://www.egalvanic.com/post/electrical-maintenance-software-future-infrastructure) · [REALTIMEais](https://realtimeais.com/nfpa-70b-compliance-software/) · [NorthGrid](https://northgridtracking.com/) · [Blackstone/Shermco](https://www.blackstone.com/news/press/blackstone-announces-agreement-to-acquire-shermco-for-approximately-1-6-billion/) · [Testing market size](https://www.marketdataforecast.com/market-reports/north-america-electrical-testing-services-market) · [Study cost](https://bowtie8.com/how-much-does-an-arc-flash-study-cost/) · [Guidant on update cost](https://www.guidantpower.com/post/why-arc-flash-updates-still-cost-real-money-every-five-years-and-why-they-matter) · [Common study mistakes](https://www.trace-software.com/en/technical-the-5-common-mistakes-in-arc-flash-studies/)

VERDICT: PASS