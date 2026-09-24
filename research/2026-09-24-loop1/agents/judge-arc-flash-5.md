## Arc flash study automation: investor evaluation

### What the research confirmed

**Regulation.** The claims mostly hold, but one is overstated.
- NFPA 70E 130.5(G) says the arc flash risk assessment must be reviewed at intervals of no more than 5 years, and updated after major modifications. The requirement is to review, not necessarily to recalculate ([Zech](https://www.zechengineers.com/blog/when-to-update-arc-flash-study/), [e-Hazard](https://e-hazard.com/how-often-do-i-need-an-arc-flash-study-performed/)).
- On Jan 1, 2023, NFPA 70B changed from a "Recommended Practice" to a "Standard", so its "should" became "shall". It requires accurate single-line diagrams, and studies reviewed at least every 5 years ([Wikipedia](https://en.wikipedia.org/wiki/NFPA_70B), [Miller Electric](https://mecojax.com/news/nfpa-70b-2023-shift-suggested-standardized-electrical-maintenance-and-what-2026-may-bring)).
- "Enforceable" overstates it. NFPA documents are consensus standards. They bind only where OSHA's General Duty Clause, a local code authority or an insurer applies them.

**Cost.** Studies run $3,500 to $6,000 for a small site and $35,000 to $100,000+ for a large one ([Herzig](https://www.herzigengineering.com/post/arc-flash-study-cost-estimate), [Leaf](https://leafelectricalsafety.com/blog/how-much-does-an-arc-flash-study-cost)).
- In e-Hazard's ~$70k food-plant study, time split into 15 days of field data gathering, 5 weeks of modeling and 7 days of labeling. The author says data gathering and building the one-line is usually the most expensive part ([e-Hazard](https://e-hazard.com/how-much-does-an-arc-flash-study-cost/)).
- The labor claim holds.

**Labor.** Certified test technicians (NETA is the electrical testing trade body) are scarce. Data center work is pulling them away, and a retirement wave is due by 2030 ([NETA World](https://netaworldjournal.org/2025/08/steveparkers/fall-2025-features/workforce-development-for-neta-testing-companies/)).

### Who else serves this customer

**The incumbents own both the data and the buying channel.** ETAP (Schneider Electric, 80% bought in 2021 with the rest due in 2025), EasyPower (Bentley, bought 2023) and SKM (independent) sell the modeling licenses that these firms renew every year. The model file lives in their formats.
- ETAP and EasyPower already offer field apps. etapAPP is free and syncs one-line diagrams and nameplate data. EasyPower's app links photos to equipment ([etapAPP](https://etap.com/product/etapapp), [EasyPower](https://www.easypower.com/data-collection)). Neither says it reads nameplates from photos. Entry is still by hand.
- ETAP 2026 (May 2026) ships an AI Copilot and one-line "Autocomplete" ([ETAP](https://etap.com/product-releases/etap-2026-release)). EasyPower 2026 added automatic one-line layout.
- Both incumbents are already putting AI into this exact workflow. Adding photo extraction to their apps would be a short step.

**Egalvanic** (Milwaukee, founded 2019, ~$1.9M raised, ~10 staff) is the closest outsider. It sells mobile field capture, a digital one-line, arc flash labels and integration with SKM, EasyPower and ETAP to contractors, engineers and testing companies ([site](https://www.egalvanic.com/), [Crunchbase](https://www.crunchbase.com/organization/egalvanic)). Its pitch is a 70B maintenance system with quoting built in, not "photos in, ready-to-run model out". I count it as a competitor, not this team.

**FlashTrack** (Facility Results) is a standard data collection interface that works with SKM, EasyPower and ETAP ([link](https://facilityresults.com/flashtrack-interface/)).

I found no startup that matches this pitch closely.

### 1. Strongest version

Narrow the customer to independent engineering firms and NETA testing firms that bid studies at a **fixed price**. Firms billing time and materials lose revenue when labor drops, so they are the wrong first customer.

Start with the recurring **5-year review**, not first-time studies:
- The firm already has the stamped model.
- Technicians re-photograph the gear.
- The product compares the photos against the existing model and flags what changed: new breakers, changed trip settings, swapped transformers.
- It then exports only the delta into ETAP, SKM or EasyPower.

This fits better than first-time studies for three reasons:
- A review against a known model is a far easier vision problem than building the connection map from scratch.
- It matches exactly what 70E and 70B require.
- It keeps the firm's customers on a 5-year cycle.

Price per device or per facility-year, not per study. Keep reading trip-unit screens and relay settings as the core skill, because that is the tedious manual copying incumbents have not automated.

### 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | One ~$70k study used 15 field days plus 5 weeks of modeling, and techs are scarce (e-Hazard, NETA World). |
| Value over today | 3 | The incumbents' apps already digitize capture. On a $3.5k to $6k study the saving is a fraction of a day, while on large studies it could plausibly be $10k+. Cable lengths and how equipment connects are not visible in photos. |
| Market size | 2 | A low-quality report puts global study services at ~$1.2B ([Marketintelo](https://marketintelo.com/report/arc-flash-study-services-market)). If US studies average ~$15k, that is tens of thousands of studies a year, so $500 to $1,500 each caps revenue near $40M to $100M. |
| Risk (5 = low) | 2 | Schneider/ETAP and Bentley/EasyPower sell the seat, own the import formats and ship AI in their 2026 releases. One misread trip setting means a stamped label with the wrong PPE on it. |

### 3. What kills it, and the fastest test

**What kills it:**
- Extraction accuracy is not high enough for engineers to stop re-checking every value, so no time is saved and the liability stays.
- Firms won't pay on top of free incumbent apps.
- ETAP or EasyPower adds photo extraction to its free app.

**Fastest test (about two weeks, no product build).** Ask two or three firms for the photos from 3 to 5 recently finished studies, along with the final stamped models. Firms routinely keep both. Run the extraction on the photos and score each field against the stamped model. Then have the engineer of record estimate the hours saved and state a price for the next fixed-bid study.
- Needed to pass: above roughly 98% accuracy on protective-device settings, plus a signed per-study price.
- Missing either means there is no company here.

This is a solid bootstrapped business, or an acquisition target for Bentley or Schneider. At per-study pricing the market is too small for venture scale, and the incumbents control both the model format and the renewal relationship with the buyer.

VERDICT: PASS
