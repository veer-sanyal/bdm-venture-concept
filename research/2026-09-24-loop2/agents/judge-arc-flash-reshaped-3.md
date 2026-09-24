I recommend passing. The problem is real, but most of the value goes to the facility owner, not the testing firm that would pay. Three platforms already hold parts of this workflow, one of them (ETAP) the study model itself. A lot of sites will have no usable study model to compare against, and the fee is steep next to what a study update earns.

## Claim check
- **The 89% figure holds, with caveats.** Schneider's own blog says 89% of 400 site audits had no one-line diagram *or only a partial one*. The blog page blocked a direct fetch, so this comes from its indexed text. The sample is Schneider's service customers, not a random set of sites. And it cuts against the pitch: a site without a current one-line often has no usable study model either. ([Schneider blog](https://blog.se.com/services/2025/07/07/getting-to-know-your-power-infrastructure-a-guide-to-the-big-picture/))
- **The 5-year rule holds, but the concept cites the wrong standard.** NFPA's own committee document quotes the 2023 NFPA 70B text: the arc flash study "shall be updated when changes occur" and "reviewed for accuracy at intervals not to exceed 5 years" (6.7.1 and 6.7.2). For the 2026 edition the committee proposed moving the arc flash requirement to NFPA 70E, calling it "more appropriately covered by NFPA 70E". It also dropped the separate 5-year review for coordination studies, because "update whenever changes occur" already covers it. The requirement stands, but it rests on 70E more than 70B. OSHA does not enforce 70B directly. ([NFPA 70B draft agenda](https://docinfofiles.nfpa.org/files/AboutTheCodes/70B/70B_F2025_EEM_AAA_SD_MeetingAgenda_0325.pdf))
- **Settings do drift from the study.** In one university renovation, Grumman|Butkus checked 156 breakers against the coordination study and had to correct 25 (17%) in the field. They say "every project we review requires some level of correction." That was during commissioning, not drift between studies. ([Grumman|Butkus](https://grummanbutkus.com/blog/why-and-how-to-verify-circuit-breaker-settings/))
- **A new tailwind, from a secondary source.** A consulting engineer's summary says the 2026 electrical code (NEC 110.16) now requires the assessment date on arc flash labels, which makes stale studies visible. ([Herzig](https://www.herzigengineering.com/post/2026necupdates))
- **Not checked:** the claim that testing firms visit every one to three years.

## Who else serves this customer
- **Condoit.** Raised a $4.25M seed with Southwire as a strategic investor. It sells to electrical service contractors and testers, claims 4M+ assets and 2,000+ facilities, and offers a "single-line [that] updates automatically as the building changes", export to SKM, and AI agents that "surface revenue opportunities". ([site](https://www.condoit.io/), [funding](https://www.finsmes.com/2024/04/condoit-raises-4-25m-in-seed-funding.html))
- **Egalvanic.** Its founder owns a testing company. It offers a "digital one-line aligned with real system conditions" and says it "integrate[s] with SKM, EasyPower, and ETAP." ([site](https://www.egalvanic.com/), [origin story](https://www.egalvanic.com/post/why-we-built-egalvanic-the-future-of-ai-driven-electrical-maintenance-and-reliability))
- **ETAP, owned by Schneider.** eProtect compares "As Designed" relay settings to "As Found", and the etapAPP field app lets users verify gear and accept or reject changes in the field. That already covers ETAP sites. ([eProtect](https://etap.com/solutions/eprotect), [etapAPP](https://etap.com/product/etapapp))
- **Megger PowerDB.** It holds most testing firms' test-report data. ([PowerDB](https://www.megger.com/en-us/products/powerdb-pro))
- **REALTIMEais** tracks study intervals for facility owners. ([REALTIMEais](https://realtimeais.com/nfpa-70b/nfpa-70b-chapter-6-system-studies/))

**Does an incumbent own the data or channel?** No single one owns both, but ETAP comes closest: it owns the model and already has the feature for ETAP sites, plus Schneider's field-service channel. Megger owns the test data. Condoit and Egalvanic are fighting over this exact buyer's field workflow. None pitches this exact product, so there is no near-identical company to treat as this team.

## 1. Strongest version
Sell to testing firms that also run power studies in-house, such as private-equity roll-ups like Shermco with 40+ locations ([Gryphon](https://www.gryphon-inv.com/news/shermco-industries-acquires-power-test-a-leading-neta-testing-company/)). Lead with SKM and EasyPower, since ETAP already covers its own sites.

The output would be a change package that imports straight into the model and a quote ready to send. The firm could then sell owners a fixed-fee annual "labels stay current" contract in place of a lumpy 5-year study. Start with sites that change often and carry high stakes: data centers, hospitals and large plants.

Price per visit or as a share of the update work sold, not $500 to $1,200 per site per year. Study updates start around a $5,000 minimum ([Zech](https://www.zechengineers.com/arc-flash-study-cost/)), so a per-site fee would cost the firm $2,500 to $6,000 over one 5-year cycle.

## 2. Ratings

| Area | Score | Evidence |
|---|---|---|
| Customer need | 3 | Drift is real (17% of breakers corrected), but the owner carries the risk while the firm sees it only as a chance to upsell. |
| Value over today | 3 | Today a technician logs as-found settings in PowerDB and an engineer diffs them at review time; ETAP already automates this for ETAP sites. |
| Market size | 2 | Only sites with an existing native model the firm can get hold of count, and the Schneider audit suggests many don't have one. Tens of millions of dollars of software revenue at most unless it takes a share of study work. |
| Risk (5 = low) | 2 | Access to model files, the proprietary SKM format, liability for wrong labels, and three platforms that could ship this as a feature. |

## 3. What would kill it, and the fastest test
**Killers:**
- Firms don't hold the native SKM, ETAP or EasyPower model for most sites they maintain. Studies are often done by a different engineering firm, and some firms withhold the files ([Arc Flash Forum](https://www.arcflashforum.com/viewtopic.php?f=2&t=1871&view=next)).
- Owners won't buy updates between 5-year reviews, so flags don't turn into billable work.
- Condoit, Egalvanic or ETAP ship the comparison as a feature.

**Fastest test:** call operations leads at 10 NETA-accredited firms (the testing firms' accreditation body) and ask one question. For your last 20 maintenance sites, how many do you hold a current native model file for? If the answer is under about 30%, the product as specified can't run. If it passes, run a manual comparison on 5 sites and count how many flags become purchase orders within 60 days.

VERDICT: PASS