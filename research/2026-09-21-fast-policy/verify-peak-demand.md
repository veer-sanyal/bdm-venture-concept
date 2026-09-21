# Verify: peak-demand load policy for single commercial buildings

Researcher pass, 2026-09-21. Budget: ~9 searches, ~8 primary-page fetches (extended past the ~6-search budget for one claim that changes the decision: whether incumbent BAS already forecasts, not just thresholds).

## Strongest support

A real published tariff shows the charge is large, is set by a single 15-minute interval, and a single miss can cost money for up to 11 months after, which is exactly the shape of problem a fast per-minute policy is suited to.

**OPPD (Omaha Public Power District) Rate Schedule 231, "General Service – Small Demand," effective 1/1/2026 (Resolution No. 6743)**, applies to "non-Residential Customers... that meet or exceed a Billing Demand of 50 kilowatts" and covers accounts up to 3,000 kW (a mid-size grocery, school, or small manufacturer's range):
- Demand charge: **"$8.62" per kW-month**, minimum billing demand "18 kW per month."
- Interval rule, quoted exactly: **"Demand, for any billing period, will be the kilowatts computed from the readings of OPPD's Meter for the 15-minute interval of the Customer's highest use during the same billing period."**
- Ratchet, quoted exactly: **"If the Demand is less than 85% of the Customer's highest 15-minute kilovolt-ampere Demand, the kilowatt Demand will be increased under this Schedule by 50% of the difference..."** and separately: **"The Customer's Demand must be equal to or greater than the larger of the following: 85% of the highest 15-minute Power Factor-adjusted Demand during the Summer billing months of the preceding eleven (11) months, or 60%... during the Non-Summer billing months of the preceding eleven (11) months, or 18 kilowatts."**
  (Source: oppd.com rate manual, Exhibit A, pp. 32–33; https://www.oppd.com/media/321584/2026-5-may-resolution-6767-update-to-service-regulations.pdf and business-rates page https://www.oppd.com/business/business-rates/)

Read together: one bad 15-minute interval doesn't just cost that month's kW × $8.62, under the ratchet it can set an elevated demand floor for up to eleven more months. For a ~200 kW building, missing one interval by 20 kW is roughly $172 that month, compounding through the ratchet. This is a real, non-trivial, recurring dollar stake tied to a single 15-minute window, the structural condition the product needs to exist.

**Caveat:** this is one utility, one schedule. Demand-charge design (ratchet length, $/kW level, interval length) varies by utility; I did not find a national average from a primary source (see NOT VERIFIED below).

## Closest substitute: what the customer does today, and what stays unsatisfactory

This is the section that most changes the picture. The premise given, "today such buildings... use a fixed kW threshold", is **not accurate for buildings that already have a real BAS**, per a primary vendor document:

**Johnson Controls Metasys "Demand Limiting and Load Rolling" (DLLR) Technical Bulletin** (currently hosted on JCI's live docs portal, docs.johnsoncontrols.com, i.e., a shipping, current feature, not a historical artifact):
- It runs **"once each minute"**, the same cadence the concept proposes.
- It does **not** just compare current draw to a fixed number. Quoted: **"DL projects the consumption for the Demand Interval... DL projects demand for the Demand Interval. If projected demand is over the currently active peak demand target, DL calculates the required correction. This correction is the goal for DL load shedding."**
- The projection is a real forecast: an exponential-smoothing model of forecast error (constant K = 0.01) combined with a 95%-confidence z-bound (Z = 1.96) projects total uncontrolled energy several minutes ahead, then computes the worst-case projected shed needed and sheds loads by priority (1–4) until the projected interval stays under target.
- It sheds/restores prioritized loads automatically, respecting comfort overrides, minimum on/off times, and shed-time limits, i.e., the same category of flexible-load control (HVAC, in particular) the concept describes.

Schneider Electric's PM8000 line also documents a "Sliding Window Demand Module" for the same purpose (found via search; primary page returned HTTP 403 on fetch, so **not independently quoted**, treat as a named-but-unverified second incumbent).

**What stays unsatisfactory about this substitute, based on what the documentation itself shows:**
1. It optimizes to a **user-set fixed kW target**, not to "the probability this interval sets this month's actual peak", it has no concept of the month's evolving maximum, only a static target someone must set and periodically revise as load patterns change.
2. It uses one input stream (the load-group meter) and a linear/statistical forecast, it does not ingest refrigeration defrost schedules, EV charger session state, or weather as separate typed signals the way the proposed JSON-schema approach would.
3. Configuration (Load Groups, priorities, targets) happens in Metasys's own operator workstation software, this is controls-integrator work, not something a building owner with no energy manager does themselves. That gap (shipped-but-uninstalled/uncommissioned) is plausibly where the real opening is, not "no such feature exists," but "the feature exists in the BAS silicon/software the building already has, and is very commonly never turned on."

**Demand-response aggregators (CPower, Voltus, Enel X)** are a different substitute with a different, narrower failure mode:
- They require interval-meter access, confirmed for at least a subset of utilities, e.g., **Southern California Edison's "Green Button Connect program lets registered third parties retrieve authorized customer interval, billing, meter, and rate data via a RESTful API using OAuth 2.0"** (nectarclimate.com summary of SCE's program), but a related summary states **"Currently only the CA IOUs and ComEd have a Connect My Data process in place,"** meaning standardized interval-data API access is not universal across utilities.
- They have minimum-enrollment thresholds that exclude many single small/mid buildings: search results describe **"at least a 15-minute interval or smart meter (per ERCOT)"** plus a **"minimum load reduction offer is 100 kW for some ERCOT programs"** and Michigan programs requiring **"1MW+ of load"** to enroll through CPower, often requiring aggregation across multiple sites of one entity.
- Structurally, DR events are dispatched by the utility/grid operator for *system* peaks (a handful of times a year, paid as an incentive), which is a different event from the building's own *monthly billing* peak that a demand charge taxes every month. Aggregators do not solve the demand-charge problem for buildings too small to qualify or whose bill is driven by self-peaks uncorrelated with grid events.

## Important objection

The core mechanism the concept proposes, read meter + load state every minute, forecast whether the interval will set the peak, shed prioritized flexible loads pre-emptively, **already ships as a stock feature inside the largest BAS platforms** (Johnson Controls Metasys, apparently also Schneider Electric/ION), not as a hypothetical "fixed threshold" strawman. The founders would be adding a smarter (nonlinear, multi-signal, calibrated) forecast on top of infrastructure incumbents already control, not creating a category no one occupies. Since the underlying model (Jev, or any equivalent) is explicitly a commodity any incumbent can buy, same pricing ($0.042/MTok input, per typesafe.ai's own blog: **"Input tokens: $0.042 / MTok ($42 per billion tokens)"**) is available to JCI or Schneider as it is to a two-person startup, the durable edge has to come from something other than "we have a better model": most plausibly, faster/simpler commissioning for buildings that never got DLLR configured, or reaching buildings whose BAS/controls are too old to run DLLR at all (see decisive unknown).

A second, harder-nosed objection: swapping a deterministic, safety-bounded shed algorithm (fixed target, configured priorities, respects comfort overrides) for a probabilistic trigger introduces a new judgment call, what probability threshold fires a shed, for an owner who by definition has no energy manager to tune it. That is a new failure surface, not a removed one.

## Decisive unknown

**How much additional peak-avoidance value (in $/kW-month) a Jev-grade calibrated, multi-signal forecast captures over the incumbent linear/exponential-smoothing forecast already embedded in commissioned BAS demand-limiting features (JCI DLLR and equivalents), net of the cost and access friction of reaching buildings whose BAS lacks this feature, has it uninstalled, or has no digital control surface at all (older pneumatic/relay systems).**

No source found, vendor, academic, or operator, quantifies "predictive AI shedding vs. the linear-forecast baseline already common in commercial BAS" in dollar terms; the machine-learning peak-shaving literature that was found (ScienceDirect, MDPI, arXiv results) measures savings from adding storage/EVs/optimization on top of *no* existing demand-limiting baseline, not the marginal lift over an already-forecasting incumbent. That comparison is the single fact that would flip the decision: if the linear baseline already captures most of the achievable peak-shaving (because commercial HVAC/refrigeration loads are largely periodic and schedule-driven, hence easy to forecast linearly), a fancier model adds little; if it leaves a large, systematic gap (e.g., can't anticipate an EV charger session start or a refrigeration defrost spike because those aren't in its single input stream), the gap is real and sellable.

A related, more basic unknown, not fully resolvable from documents: what a **general-purpose LLM (e.g. a frontier chat model) given the identical JSON interval trace and asked the same yes/no question** would output. This is inference, not observed: a general-purpose model can already be prompted with this JSON and produce a probability-like answer today, nothing about the task requires Jev's non-generative architecture in principle. Jev's stated advantage over that baseline is speed (70–500ms vs. multi-second) and cost (near-zero output tokens) at high call volume (once-per-minute, per building, indefinitely), not new capability. Whether that speed/cost gap matters for a task running once per minute (not once per millisecond) is itself unresolved, the once-a-minute cadence in both the JCI incumbent and the proposed product suggests latency may not be the binding constraint, which would blunt Jev's main differentiator for this specific use case.

## Smallest useful next test

**Who to approach:** call or visit a facilities/property manager or owner-operator at one real mid-size building in the target class (a standalone grocery, church, school, or small manufacturer, 50–500 kW range, on a demand-metered commercial tariff, with no dedicated energy manager). Ask two concrete things: (1) do they know their monthly demand charge and how it's calculated, tests whether "nobody manages this" is true; (2) what building automation or controls they have (Trane, JCI, Honeywell, Distech, or none), and whether a controls contractor has ever mentioned or configured a demand-limiting feature, tests whether the substitute is "already installed but off" versus "genuinely absent."

**Real case to observe:** find one building that already has JCI DLLR (or an equivalent linear demand-limiting algorithm) actually configured and running, with at least 6 months of 15-minute interval data. Reconstruct, from the raw interval trace, the theoretical best achievable peak given the building's flexible loads, and compare it to what the linear system actually achieved.

**What result would change the decision:** if the gap between the incumbent's actual result and the theoretical optimum is small (roughly under 5% of the monthly demand-charge line, a few to a few tens of dollars for a 100–500 kW building on an $8.62/kW tariff), a smarter forecast has little room to add value and the concept should not be pursued as stated. If the gap is large and systematic, traceable to specific blind spots like EV charging sessions or defrost cycles the linear model can't see, and if most buildings in this class turn out to have DLLR-equivalent features absent or uncommissioned rather than tuned and running, that combination is the case for pursuing it, and it would need to be re-scoped around "activate/replace dormant or absent BAS demand-limiting," not "beat a fixed threshold."

## Source list

**VERIFIED (fetched primary page, quoted directly):**
- OPPD Rate Schedule 231 (General Service – Small Demand), effective 1/1/2026, Resolution 6743, demand charge, 15-minute interval rule, ratchet clause. https://www.oppd.com/media/321584/2026-5-may-resolution-6767-update-to-service-regulations.pdf (Exhibit A pp. 7, 9, 32–34)
- OPPD Business Rates summary page (Schedule 231 headline figures). https://www.oppd.com/business/business-rates/
- Johnson Controls Metasys "Demand Limiting and Load Rolling" Technical Bulletin, currently hosted on JCI's docs portal. https://docs.johnsoncontrols.com/bas/api/khub/documents/N0IO2oKfG0EUvD5xQn8l_g/content
- TypeSafe AI blog, "Introducing System One Models & Jev", pricing, latency, calibration-not-empirical language. https://typesafe.ai/blog/introducing-system-one-models-and-jev

**VENDOR CLAIM / SEARCH-SUMMARIZED, not independently opened and quoted (treat as lower confidence):**
- Schneider Electric PM8000 "Sliding Window Demand Module" exists and is named for demand management, page returned HTTP 403, content not independently verified. https://productinfo.se.com/pm8000/.../IONRef_SlidingWindowDemandModule_0000097940
- SCE Green Button Connect OAuth 2.0 interval-data API description, and the claim that only CA IOUs and ComEd currently support "Connect My Data", sourced from a third-party aggregator summary (nectarclimate.com), not SCE's own page directly.
- CPower/Voltus/Enel X minimum-enrollment thresholds (100 kW ERCOT, 1 MW+ Michigan/MISO), from search-engine synthesis of multiple vendor/program pages, not one primary page opened directly.
- General claim that "peak demand charges often account for 30% to 50% of a commercial electricity bill" and BAS-savings percentages (5–15%, up to 29% DOE), search-engine synthesis, no single primary source opened; do not rely on these numbers without re-verification.

**NOT VERIFIED (explicitly could not confirm):**
- Any operator- or vendor-reported dollar figure comparing predictive/AI-based peak shedding against a fixed-threshold or linear-forecast baseline for this building class specifically.
- Whether Jev's or any non-generative model's calibration holds on building-load time series, the founder brief already states this is unproven, and nothing found here changes that.
- National or typical demand-charge $/kW figures beyond the one OPPD schedule quoted; do not generalize $8.62/kW to other utilities without checking their own tariff sheets.
