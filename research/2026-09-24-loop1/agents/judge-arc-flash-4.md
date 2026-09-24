I checked the concept's claims against the standards text and vendor pages, and looked for other products sold to the same buyer. Three live products already do most of what the concept describes, at a fraction of its price. My verdict is PASS.

## Claims against sources

| Claim | Finding |
|---|---|
| Review at least every 5 years, update after changes | True. NFPA 70E 130.5 requires review at intervals not over 5 years and an update after major changes ([Leidos](https://www.leidos.com/insights/five-things-consider-your-five-year-arc-flash-update), [Delta Wye](https://deltawye.com/arc-flash-study-requirements/)). |
| The 2023 revision made one-lines and maintenance programs "enforceable" | Overstated. NFPA 70B-2023 changed "should" to "shall" and requires current one-line diagrams plus studies at least every 5 years ([Eaton](https://www.eaton.com/content/dam/eaton/services/eess/eess-documents/eaton-nfpa-70b-white-paper-wp027024Xen.pdf), [Miller Electric](https://mecojax.com/news/nfpa-70b-2023-shift-suggested-standardized-electrical-maintenance-and-what-2026-may-bring)). But federal OSHA has not adopted 70B. It binds only where a jurisdiction, regulation, contract or insurer adopts it. Otherwise OSHA can use it only as evidence in a General Duty Clause citation ([ReliaMag](https://reliamag.com/guides/nfpa-70b-compliance/), [EC&M](https://www.ecmweb.com/test-measurement/article/55399475/the-importance-of-nfpa-70e-to-osha-violations-and-fines)). |
| Studies cost $3,500 to over $100,000 | True. Zech puts small sites at $3,500 to $6,000 and mid-size at $6,000 to $14,000 ([Zech](https://www.zechengineers.com/arc-flash-study-cost/)). Leaf quotes up to $100,000 to $500,000 for very large sites ([Leaf](https://leafelectricalsafety.com/blog/how-much-does-an-arc-flash-study-cost)). |
| Most labor is copying data by hand | Mostly true. Practitioners on arcflashforum.com put data collection at 40 to 60% of study effort (per [EC&M magazine](https://www.ecmag.com/magazine/articles/article-detail/safety-how-much-effort), from search snippets; the page itself blocked my fetch). |

## Who already serves this customer

- **70Ez** ([70ez.com](https://www.70ez.com/)) is the closest match. It sells to engineering and testing firms. Technicians photograph nameplates, AI extracts the values, technicians confirm or flag them, and the data exports to SKM, ETAP or EasyPower. It claims to cut data collection "from two days to two hours". Price is $199/month (one user, SKM export only) or $499/month (8 users, all export formats). It lacks one-line drawing, trip-unit screen reading and video, so I treated it as a competitor, not as this team.
- **AmpSketch** ([ampsketch.com](https://ampsketch.com/arc-flash-data-collection/)) was built by a licensed PE. AI reads nameplates including trip settings, it draws the one-line as data comes in, and it flags missing values (transformer impedance, interrupting ratings, feeder lengths) while the tech is still on site. It exports PDF only. Price is $69/month, or $199 for a single project.
- **The modeling vendors themselves:**
  - ETAP (part of Schneider Electric) has a free field app, etapAPP, with photo capture linked to the model ([etap.com](https://etap.com/product/etapapp)). It also has an AI assistant called Electric Copilot and generates one-line diagrams automatically when converting files ([ETAP what's new](https://etap.com/products/whats-new)).
  - EasyPower (now owned by Bentley Systems) has a tablet app, EasyPower OnSite ([easypower.com](https://www.easypower.com/data-collection)). A 2026 release builds one-lines from CSV files "without manual entry", which makes photo reading a small feature for them to add ([EasyPower LinkedIn](https://www.linkedin.com/posts/easypower-llc_easypower-2026-import-data-activity-7475559243408928768-l1wi)).
- **Others:** FlashTrack (Facility Results) does structured collection for all three tools. CIMA+, an engineering firm, built an in-house model that identifies fuses in survey photos with 91% accuracy ([CIMA+](https://www.cima.ca/en/blog/arc-flash-studies-through-artificial-intelligence/)). Arcflash.ai, eGalvanic and REALTIMEais sell NFPA 70B platforms to facility owners.

Incumbents already own this customer's data and buying channel. The study lives in ETAP, SKM or EasyPower files, and those vendors hold the firm's software budget. Schneider and Eaton also run their own study businesses. The export target is controlled by companies that already ship field apps and could add photo reading.

## 1. The strongest version

Narrowing to a per-study data entry tool loses on price. The stronger version is a service that keeps a site's model current, sold through testing firms on their NFPA 70B maintenance visits.

- On each maintenance visit, which happens every one to three years, the technician videos the gear.
- The tool compares what it reads, especially as-found trip-unit settings, against the existing ETAP or SKM model. It outputs a list of changes and a settings-drift report: breakers set differently from what the study assumed.
- The firm resells this to the facility as an "always current" study, priced per site per year. The 5-year update becomes a review of those changes, not a rebuild.
- Start with data centers and hospitals, where equipment changes often and settings drift matters most.

This version uses the parts nobody else sells: trip-unit screen reading, cross-checks for inconsistent values, and comparison against the existing model. It also moves revenue from a one-time study to a recurring per-site fee.

## 2. Ratings (for that version)

- **Customer need: 4.** Data collection is 40 to 60% of study effort (EC&M survey), and 70E requires a review every 5 years.
- **Value over what customers use today: 2.** AmpSketch already reads nameplates and trip settings, draws the one-line and flags gaps for $69/month. 70Ez already exports to all three tools for $499/month. The PE still has to verify every value before stamping, which caps the time saved.
- **Market size: 2.** This is my own estimate, not a sourced figure. Roughly 100,000 to 200,000 US studies a year at $1,000 each gives a $100 to 200M ceiling at the proposed price. Live market pricing ($69 to $499 per firm per month) points to a small fraction of that. The recurring version raises the ceiling but still depends on facilities paying for continuous compliance, and outside places that adopt 70B nothing forces them to.
- **Risk: 2** (5 is low risk). A misread trip setting produces a wrong PPE label under a PE stamp. ETAP and EasyPower are one feature away. Two live products have already set prices 5 to 20 times below the proposed $500 to $1,500 per study.

## 3. What would kill it, and the fastest test

It dies if firms will not pay much more than the $69 to $499/month they already can. That happens if AI extraction saves fewer engineer hours than the fee, because every value still needs human verification, or if ETAP or EasyPower adds photo reading to their free field apps.

The fastest test is a paid backtest with 2 to 3 NETA-accredited testing firms:
1. Collect their photo and video archives from studies they have finished, plus the final SKM or ETAP models as the answer key.
2. Run the pipeline on the archives.
3. Measure what share of trip-unit settings and nameplate fields come out correct and export cleanly.
4. Measure how many engineer hours of re-keying and checking it removes per mid-size study.
5. Then ask for $750 per study, or per site per year, against their current tool.

At 70Ez's quoted rate of $150 to $250 per engineer-hour, $750 needs 3 to 5 saved engineer-hours per study. If the backtest saves less than that, or no firm pays above the 70Ez price, the business does not work. This takes about two weeks.

VERDICT: PASS
