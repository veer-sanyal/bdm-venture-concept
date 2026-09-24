I couldn't read METHOD.md or STATE.md because you told me not to open local project files, so this plan doesn't follow the repo's process. Everything below comes from desk research, which isn't customer validation. My web search budget also ran out partway through, so a few figures are unverified and marked that way.

# The strongest company: a drift monitor for arc flash studies, sold to testing firms

## The pitch
Every NFPA 70B maintenance visit becomes a check on the site's arc flash study. The software flags when a site no longer matches its study. That gives the testing firm billable update work, and it keeps the owner's labels valid between five-year studies.

All five investors pointed the same way: sell to testing firms, bill per site per year, compare each visit against the last model, and treat device-library matching as the hard part. My research adds four things they didn't cover.

**1. Much of the data already exists as structured records, not just photos.** During 70B maintenance, NETA technicians record the as-found and as-left trip settings in their test reports. Many relays and modern trip units can also export their settings as files. So the engine should take in test reports, relay setting files and photos, and use photos only to fill gaps and cross-check. That raises coverage and accuracy on the fields that matter most, the protective-device settings. Photo reading of trip-unit screens and nameplates alone is exactly where all five investors saw the kill risk. (I'm stating this from domain knowledge. Checking it is step 1 of the test below.)

**2. The pitch becomes "find the study work hidden in your own test reports."** If a breaker was found at a different setting than the study assumed, the arc flash label on that gear may be wrong. The firm can show that to the client and sell the update. The product then earns the firm money instead of cutting its billable hours. That answers Investor 5's worry about firms that bill by the hour, and "saves hours but engineers re-check everything" stops being fatal.

**3. There is a large backlog of sites with no usable baseline.** Schneider Electric audited 400 sites from 2017 to 2022 and found 89% had no one-line diagram or only a partial one ([ESFI/Schneider 70B guide](https://www.esfi.org/wp-content/uploads/2024/05/NFPA-70B-Step-by-Step.pdf)). NFPA 70B Chapter 6 requires one-line diagrams to be kept legible, accurate and dated. It also requires the short-circuit, coordination and arc flash studies to be updated after major changes and reviewed at least every five years (same source). So building the first model (per study) comes first, and monitoring for drift (per site per year) follows.

**4. Build for trust, not for a raw accuracy number.** Link every extracted value to the photo crop or report line it came from. Send low-confidence values to a person. Measure the silent error rate: wrong values the engineer never sees flagged. The engineer reviews and stamps flagged changes instead of re-keying everything.

## Growth path from narrow to broad
1. **Drift reports for 3–5 independent NETA firms**, per site per year. They are the fastest buyers.
2. **First-model builder** for sites with no baseline, exporting to ETAP, SKM and EasyPower.
3. **A neutral, versioned model of each facility**, like version control for electrical models. Large firms and roll-ups carry it across their offices. Shermco alone has 700+ technicians and 41 locations ([Shermco](https://www.shermco.com/about-us/)).
4. **Sell to multi-site owners directly** (data centers, hospitals) with a portfolio view of which labels are still valid. Later, add coordination and load-flow updates, and as-built models from acceptance testing on new data center construction.

## Competition
- **Incumbents are adding AI, which is the main risk.**
  - ETAP 2026 shipped an AI copilot and "AI Auto-Complete" that suggests elements and connections in the one-line diagram ([ETAP 2026](https://etap.com/product-releases/etap-2026-release)).
  - etapAPP is free and already captures photos and links them to the model, with accept/reject change tracking. It shows no photo reading yet ([etapAPP](https://etap.com/product/etapapp)).
  - EasyPower's field tools link tablet photos to one-line equipment ([EasyPower](https://www.easypower.com/data-collection)).
  - Our defence is that we work across all three tools. We also take in test-report and relay data, which comes from the testing firm's own workflow and which the modeling vendors don't hold.
- **eGalvanic** is the closest direct competitor. It is maintenance-management software for NETA firms and contractors, with AI nameplate reading, arc flash readiness, one-line documentation and SKM/ETAP/EasyPower integrations ([eGalvanic](https://www.egalvanic.com/asset-tracking-software)). Arc Flash Intelligence ([arcflash.ai](https://arcflash.ai/)) is similar. So a plain "living asset register" is already taken. Don't build maintenance-management software. Own the engineering-grade comparison against the model: trip settings, library matches and export files. eGalvanic could end up a partner rather than a rival.
- **CIMA+**, an engineering firm, ran an applied AI research project to read study photos into model data ([CIMA+](https://www.cima.ca/en/blog/arc-flash-studies-through-artificial-intelligence/)). That supports the need, and it confirms firms keep photo archives.

## Market size
Treat this as an estimate to check, not a finding. Studies run $3,500–6,000 for small sites, $6,000–14,000 mid-size and $14,000–22,000+ for large ones ([Zech](https://www.zechengineers.com/arc-flash-study-cost/)). One industry source says AI targets "the data-gathering half" of the work ([PowerSafe](https://www.powersafe-engr.com/post/ai-in-arc-flash-analysis-what-the-future-looks-like)).

If about 1M US facilities are on a five-year cycle, that's roughly 200k studies a year, a $2B+ services market. At $500–1,200 per site per year across 300k maintained sites, the per-site product alone is worth about $150–350M a year. Owner portfolios and the other study types are how this becomes venture scale.

## One fastest test (about two weeks, no product needed)
From 1–2 independent NETA firms, collect:
- 5 stamped models;
- the maintenance test reports from visits after each model was stamped;
- the photos and any relay setting files.

Then measure four things. Continue only if all four pass:
1. **Coverage:** at least 80% of protective-device fields come from test reports, setting files or photos.
2. **Silent errors:** below 0.5% on settings after cross-checks.
3. **Drift found:** real differences between the study and the site at 1 in 3 sites or more.
4. **Payment:** the firm signs a paid pilot of $500 or more per site per year on 10 or more sites, or $750 or more for a first-model build.

These thresholds are my proposal. They combine the investors' tests with the new drift measure.

## Open items
- I couldn't verify 70Ez or its $69–$499/month and $150–$250/hour figures.
- I couldn't confirm the total number of NETA-accredited firms or who owns the roll-ups.
- I couldn't check whether PowerDB-style test reports can actually be exported.

Ask one NETA firm about all three in the first meeting.