The idea's core claims hold up, but the gap it targets is narrower than it looks. The 5-year review rule is real, and "data collection is 40-60% of the effort" traces to an industry poll. At least two small companies already sell photo capture tied to studies. I found no product that proves it turns photos into a study-ready model.

## 1. Regulation

- **NFPA 70E 130.5(G).** The incident energy analysis must be reviewed at intervals of no more than 5 years, and updated whenever a system change affects its results. "Reviewed" does not mean recalculated. ([Zech](https://www.zechengineers.com/blog/when-to-update-arc-flash-study/), [Leidos](https://www.leidos.com/insights/five-things-consider-your-five-year-arc-flash-update))
- **NFPA 70E-2024 labels.** Labels must now be durable enough for their environment. ([Brainfiller](https://brainfiller.com/electrical-safety-codes-and-standards/2024-nfpa-70e-major-changes/))
- **NFPA 70B-2023 moved from recommended practice to enforceable standard.** A documented electrical maintenance program (EMP) is now mandatory. Maintenance intervals come from equipment condition assessments. ([Miller Electric](https://mecojax.com/news/nfpa-70b-2023-shift-suggested-standardized-electrical-maintenance-and-what-2026-may-bring), [NFPA workshop paper](https://electricalsafetyworkshop.org/wp-content/uploads/sites/255/ESW-2023-18.pdf))
- **70B Chapter 6.** Single-line diagrams must be legible, accurate and up to date. Short-circuit and coordination studies must be reviewed at least every 5 years. ([Shaw Engineering](https://shawengr.com/single-line-diagrams-nfpa-70b/)) I could not get the exact section numbers without the standard itself.
- **NFPA 70B-2026** was published September 12, 2025. It reportedly requires updated diagrams and studies after any system change, before the changed system returns to service. The source is a vendor (REALTIMEais) that sells compliance software, so treat it with caution. ([REALTIMEais](https://realtimeais.com/nfpa-70b/nfpa-70b-2026-changes/))
- **OSHA does not enforce NFPA 70E directly.** It cites 1910.132, 1910.333, 1910.335 and the General Duty Clause, and uses 70E as evidence that the hazard is recognized and fixable. ([Bowtie](https://bowtie8.com/what-is-the-difference-between-nfpa-70e-and-osha-electrical-standards/), [NASP](https://www.naspweb.com/blog/debunking-a-common-myth-can-osha-cite-you-for-not-having-an-arc-flash-label/))
- **Insurers.** FM Global Data Sheets 5-19 (switchgear), 5-20 (electrical testing) and 5-32 (data centers) cover maintenance, testing and management of change. ([FM DS 5-20](https://www.fm.com/FMAApi/data/ApprovalStandardsDownload?itemId=%7BDEC14EBF-91D1-4265-8570-0A1683AE3905%7D)) **I could not verify** that any insurer explicitly requires an arc flash study.
- **Data centers.** I found no codified requirement specific to data centers. What exists is industry practice, such as the Schneider/ETAP 800 VDC arc flash white paper from August 2026. ([Schneider](https://www.globenewswire.com/news-release/2026/08/03/3337455/0/en/Schneider-Electric-releases-pioneering-study-assessing-arc-flash-risk-in-800-VDC-data-centers-aligning-with-world-s-leading-hyperscalers.html))

## 2. Is data collection the biggest cost?

- **The 40-60% figure** comes from an informal poll on Jim Phillips' Arc Flash Forum, reported in Electrical Contractor magazine. It is practitioner opinion, not a measured study. ([ECmag](https://www.ecmag.com/magazine/articles/article-detail/safety-how-much-effort); the page returned 403, so I have the quote only through search snippets)
- **DuraLabel says "fully one-half"** of study effort is data collection. ([DuraLabel](https://resources.duralabel.com/articles/arc-flash-hazard-analysis))
- **Counter-evidence.** In e-Hazard's small example, a $3k study, most of the hours went to modeling, not the field. In its large example, a roughly $70k food plant, the split was 15 days of data gathering, 5 weeks of modeling and 7 days of labeling. ([e-Hazard](https://e-hazard.com/how-much-does-an-arc-flash-study-cost/)) So modeling can be as large as, or larger than, collection.
- **Price by facility size:**
  - Zech: $3.5k-$6k small, $6k-$14k mid, $14k-$22k+ large. ([Zech](https://www.zechengineers.com/arc-flash-study-cost/))
  - Herzig: $7.5k-$15k small, $15k-$35k campus, $35k-$100k+ complex. ([Herzig](https://www.herzigengineering.com/post/arc-flash-study-cost-estimate))
  - The claimed $3.5k-$50k range is plausible, but the top end runs past $100k.
- **Labor.** Data-collection technicians earn about $23-$26/hr in wages. ([ZipRecruiter](https://www.ziprecruiter.com/Jobs/Arc-Flash-Data-Collection)) Site time runs 8-16 hours for a simple site and 40-60 hours for a large one (a search snippet attributed to one of the pricing blogs above). **Unverified:** what firms bill per day for data collection. No firm published it.

## 3. Who does the studies, and how big is the market

- **NETA-accredited firms (third-party electrical testing companies).** **I could not find a published count.** NETA publishes a directory but no total. ([NETA](https://www.netaworld.org/accreditation/overview))
- **Manufacturer service arms** sell studies directly. Eaton has a dedicated studies service ([Eaton](https://www.eaton.com/us/en-us/catalog/services/electrical-system-studies-arc-flash-and-coordination-analysis.html)). Schneider owns ETAP. I did not verify ABB's or Siemens' study offerings.
- **Facilities.** CBECS counted 5.9M US commercial buildings in 2018, and about 2% (roughly 118k) are over 100k sq ft ([EIA](https://www.eia.gov/todayinenergy/detail.php?id=46118)). **Unverified:** how many facilities have 480V+ gear. No source counts that.
- **Market size.** One estimate puts "Arc Flash Study Services" at $1.2B in 2024, growing to $2.8B by 2033 ([MarketIntelo](https://marketintelo.com/report/arc-flash-study-services-market)). That publisher is low quality, so treat the figure as a rough order of magnitude.

## 4. Competitors

| Player | What it does | Reads photos? | Funding or owner |
|---|---|---|---|
| ETAP | Market-leading power system modeling software. The free etapAPP captures and syncs field data, photos and one-lines. ETAP 2026 adds AI Auto-Complete, which suggests one-line connections, and a natural-language Copilot. | Attaches and geotags photos. **No photo-to-data extraction found.** | Schneider bought a controlling stake in 2021 ([ARC](https://www.arcweb.com/blog/schneider-electric-completes-investment-etap), [etapAPP](https://etap.com/product/etapapp), [ETAP 2026](https://etap.com/product-releases/etap-2026-release)) |
| EasyPower | Its OnSite app models one-lines in the field. The desktop links photos to one-line equipment in real time. | Links photos, no extraction | Bentley acquired it in February 2023 ([Bentley](https://investors.bentley.com/news-releases/news-release-details/bentley-systems-announces-acquisition-easypower-leader-power), [EasyPower](https://www.easypower.com/data-collection)) |
| SKM | PowerTools desktop software. Converts ETAP and EasyPower projects. | No | Private, founded 1972, no acquisition found ([PitchBook](https://pitchbook.com/profiles/company/444142-99)) |
| **eGalvanic** | Maintenance-tracking software (CMMS) for NFPA 70B, with a "digital one-line" and field photos. States it integrates "with SKM, EasyPower, and ETAP." | Photos yes, AI extraction not stated | About $1.9M raised, Milwaukee, founded 2019 ([site](https://www.egalvanic.com/), [Crunchbase](https://www.crunchbase.com/organization/egalvanic)) |
| **Arc Flash Intelligence (arcflash.ai)** | "AI-driven" platform with Photo To Report, Field Scan, a mobile field app, a calculation engine, labels and engineer validation. Plans include pay-as-you-go. | Claims a photo-to-report feature. I could not see how it works. | Unknown; Troy Knutson is linked to the company ([arcflash.ai](https://arcflash.ai/)) |
| CIMA+ | Canadian engineering firm. Trained an internal model on 4,300 photos that reached 91% component detection, and discussed selling it. | Yes, as an internal tool | Private firm ([CIMA+](https://www.cima.ca/en/blog/arc-flash-studies-through-artificial-intelligence/)) |
| REALTIMEais | 70B asset and maintenance software. Tracks 5-year study dates and integrates with ETAP. | No | Not found ([REALTIMEais](https://realtimeais.com/nfpa-70b-compliance-software/)) |
| Generic nameplate OCR (AutomaSnap, pro-Forms, TagWizard) | Read nameplates into ERP or CMMS systems | Yes, but not study-aware | ([AutomaSnap](https://automasnap.com/blog/ai-tools-batch-nameplate-data-extraction)) |

- **No YC or 2025-2026 venture round** turned up for arc-flash-specific AI in my searches.
- **Not checked:** Brady, PowerDB, Megger, Xendee, Facilio, Phase to Phase and "Arc Flash Pro". This is a gap in the competitor list, not evidence they have nothing.

## 5. Adjacent markets and their buyers

- **70B EMP software.** Facility and maintenance managers are the buyer, and eGalvanic and REALTIMEais are already there.
- **Live electrical digital twin for multi-site owners.** Corporate engineering or EHS leads are the buyer. ETAP, Bentley and ABB (with NVIDIA, June 2026) own the high end. ([search result](https://www.startus-insights.com/innovators-guide/digital-twin-startups-to-watch/))
- **Data centers.** Operators and commissioning agents are the buyer. Studies here are design-time and ETAP-heavy.
- **Insurers.** Loss-control engineers are the buyer. There is no verified mandate, so treat this as a speculative channel.

## 6. My read

**Best first customer:** a small or mid-size study firm (NETA shops or 5-50 engineer electrical engineering firms) that runs many $5k-$35k studies a year. They feel the labor cost directly. Facility owners buy the finished study, not a tool.

**What they might pay** (my speculation, not sourced): if collection plus transcription is about half of a $15k study, a firm might pay $300-$1,500 per study. That only holds if the tool demonstrably cuts engineer data entry, not just photo sorting.

**Biggest risk:** the data a study needs most often cannot be photographed. That includes trip-unit settings (often behind menus), cable lengths and sizes, and transformer impedance on hidden nameplates. The equipment also often has to be opened under PPE. The technician still goes to the site and the PE still verifies every value, so the savings may be limited to transcription.

**Second risk:** ETAP already has a free field app that syncs photos and one-lines. Adding photo extraction is a feature it could plausibly ship, and eGalvanic and arcflash.ai are already selling in this space.

**Test before building:** have three study firms time one project and split the hours into site time, transcription and modeling.
