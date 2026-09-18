# The "modernize a backward niche industry" thesis, tested

**2026-09-06.** Commissioned by Veer after a friend described two cases: a vending company that
services its own machines and "took over the market," and a stone tiling company where an MBA
founder used modern marketing to dominate a trade of generational mom-and-pops.

Five research streams plus a two-skeptic adversarial round. **Both source anecdotes were refuted.
The folk thesis was refuted. A narrow, mechanism-specific version survived, and it points at a
niche twenty minutes from campus.**

This file is evidence and selection input. It is NOT a ranked idea list: `STATE.md` binds this work
to D21 (generate freely, do not rank, select on soonest askable at the smallest price, output binary
keep/kill). Candidates below are sorted by REACHABILITY, never by promise.

---

## 1. The two anecdotes

**Vending: FALSE.** "Services its own machines" is not a modernization, it is the definition of a
vending operator as against a machine seller. NAMA/Technomic Industry Census: **11,450 operators
(2023), down from 15,250 in 2014**, roughly $2.3M average revenue. The largest US operator is
Canteen, a division of Compass Group. The "top four = 47.1%" statistic that powers this story comes
from a stale IBISWorld vintage whose number-one player was **Outerwall, i.e. Redbox DVD kiosks and
Coinstar**, because NAICS 454210 lumps DVD and coin kiosks in with food vending. Strip it out and
top-three food vending was about 21.5%. Anyone citing 47% concentration is citing a dead DVD company.
(Verification of the Outerwall reconstruction is second-hand; treat as strong but not primary.)

**Stone: EXAGGERATED, with a better true story underneath.** The fragmentation premise holds:
8,000 to 10,000 fabrication shops, nobody above roughly 5%. The likely referent is **MSI Surfaces**,
founded 1975 in a Fort Wayne basement, about $50M (2003) to $2.5B+ (2024). But the founder,
Manu Shah, held an **MS in Mechanical Engineering from Purdue (1968), not an MBA**; the documented
mechanism was **import supply chain and distribution scale, not marketing**; and the family told the
Orange County Business Journal in 2023 they hold **"less than 12% market share."**

An Indiana basement to $2.5B is a better story than the one that was told, and it is true.

---

## 2. Verdict on the folk thesis

**Refuted as stated.** "These operators are unsophisticated, so a modern operator takes the market."

| Evidence | Source |
|---|---|
| Small-business survival is ~78% at one year, **~49% at five years**. The incumbents you plan to out-execute already cleared a coin flip. ("90% of small businesses fail" is folklore.) | BLS Business Employment Dynamics |
| The **establishment base is not consolidating**: 2022 to 2023 across 27 screened industries, +0.8%, identical to +0.8% for all US industries. Despite ~800 HVAC companies acquired by PE since 2022. | Census CBP 2023 vs 2022, computed from primary files |
| Three "boring business" staples are already consolidated, not fragmented: **linen supply averages 61.5 employees per establishment** across only 905 establishments nationally; industrial launderers 46.6; pharmacies only 38.7% of locations under 10 employees. | Census CBP 2023 |
| Non-adoption is an **incentive** problem, not ignorance. Researchers gave away a strictly better cutting technology; take-up stayed low for 15 months because piece-rate workers lost income on the learning curve and misinformed owners. | Atkin, Chaudhry, Chaudry, Khandelwal & Verhoogen, NBER w21417 |
| Cash, not ignorance: median cash buffer is **18 days in repair and maintenance**, 20 in construction. A subscription with payback past three weeks is a genuinely bad trade for them. | JPMorgan Chase Institute, 597,000 accounts |
| "Buy a boring business and add AI" is a **consensus trade**, not a contrarian one. See section 5. | Multiple |

### The most important refutation: family ownership is not the defect

The single most-cited justification for this thesis, "family and founder firms are badly managed,"
**is not what the data says.** Bloom & Van Reenen (QJE 2007, n=732): family largest shareholder is
**+0.005, insignificant and positive**. Family shareholder plus family CEO is -0.105, insignificant.
Dropping founder-run firms changes little.

**The damage is specifically PRIMOGENITURE: CEO is the eldest son, -0.317 SD with full controls,
-0.590 without.**

So the one part of the original intuition that survives contact with the evidence is the phrase
"passed down from generation to generation," and it survives in a precise form: the measured defect
is **hereditary succession**, not family ownership, not founder management, and not small size.

---

## 3. The mechanism that actually governs (Sutton)

Sutton, *Sunk Costs and Market Structure* (MIT Press, 1991), splits industries by the kind of sunk
cost:

- **Exogenous only** (a truck, a shop, a license): free-entry equilibrium drives concentration down
  as the market grows, roughly C proportional to 1/sqrt(S). **A big market means many small firms,
  permanently.** Fragmentation is the equilibrium, not a failure to be corrected.
- **Endogenous** (spend you CHOOSE, to raise willingness to pay or cut unit cost): firms escalate
  against each other, producing the **non-convergence result, a lower bound to concentration that
  does not vanish however large the market grows.**

**Therefore: consolidating a fragmented industry means MANUFACTURING an endogenous sunk cost that
did not previously exist.** Absent that, buying forty small firms produces one firm with forty small
firms' economics. This is the sentence the whole concept has to answer.

Supporting: Ellickson, "Does Sutton apply to supermarkets?" (RAND J. Econ. 2007) shows escalating
investment in firm-level distribution produces a natural oligopoly of four to six firms **regardless
of market size**, alongside a permanent competitive fringe of small stores. A roll-up does not
eliminate the fringe. It aims to be in the core.

Caution on the standard roll-up claim: **route-density economics is weaker than every deck asserts.**
Abrate, Erbetta, Fraquelli & Vannoni (500+ Italian municipalities) found density economies but
**diseconomies of size**: aggregating collection operations across municipalities did not lower
average cost. Everything asserting route density in pest control was vendor marketing.

### The diagnostic (use this, not "is it fragmented")

1. Is there an **endogenous sunk cost available to escalate**? If the only costs are a truck and a
   license, you are fighting the equilibrium.
2. Does the **scale unit sit above the local route**? If the whole cost curve lives inside a metro,
   a national platform buys overhead, not margin.
3. Did something **recently move the fixed-cost floor**? New compliance regime, credential, mandated
   intermediary, capital requirement.
4. Is quality unobservable to the buyer, and **did that just change**? If it changed via reviews or
   marketplaces, expect DE-consolidation. See Luca below.
5. Are customer needs **standardizable** into a repeatable SKU? (Porter)
6. Is the **customer** consolidating? Supplier consolidation follows.
7. Is labor scarce AND **can capital substitute**? If a licensed human must physically sign, scarcity
   caps the platform exactly as hard as it caps the independent.

**The counter-evidence to pre-empt.** Luca (HBS 12-016): a one-star Yelp increase raises revenue 5 to
9%, the effect runs **entirely through independents, zero for chains**, and **chain market share
DECLINED as Yelp penetration rose.** Cheap third-party information substitutes for brand. In local
consumer services, the recent change ran the opposite direction from consolidation.

---

## 4. Where the diagnostic points

Applying it to the niches the structural screen surfaced. Verdicts are inference from the
literature, not the literature's own claims.

| Niche | Verdict | Why |
|---|---|---|
| **Ag / industrial machinery repair (811310)** | **CHANGING. Best candidate.** | The binding constraint was OEM control of diagnostic software: Deere's Customer Service ADVISOR was the only tool capable of all repairs, dealer-restricted. **The FTC and five states secured a stipulated order on 2026-07-08 requiring Deere to give independents dealer-equivalent tools for ten years, remaining capabilities by 2026-12-31.** A barrier removed, two months ago, with a candidate endogenous sunk cost (tooling, software licences, trained techs) to escalate on. Risk: dealer groups are the incumbent consolidator. |
| **Stone / countertop fabrication (327991 / 238340)** | **CHANGING** | Cal/OSHA engineered-stone silica standard effective 2023-12-29, permanent 2024-12-19, against 542 confirmed California silicosis cases and 29 deaths as of April 2026. A compliant wet-cut, monitored, CNC shop is a fixed cost a garage shop cannot carry: a textbook manufactured endogenous sunk cost. Risks: an outright engineered-stone ban destroys the demand base instead of consolidating it, and there is NO data on actual shop closures. |
| **Electronic / precision equipment repair, biomed-dental-lab (811210)** | **CHANGING, but occupied** | FDA's 2024 servicing-vs-remanufacturing final guidance draws a fixed-cost line separating capable platforms from one-truck operators. And the customer is consolidating: health systems buy vendor-neutral clinical asset management. But TRIMEDX and Agiliti are already there and capitalized. |
| **Hood cleaning / building services (561790)** | **FAILS Q1** | Demand is NFPA 96 mandated, which is attractive, but **mandated demand is not a fixed cost.** Truck, pressure washer, crew: all exogenous. Scale is route-local. Approval is county-by-county. The only real lever is Q6, multi-site restaurant chains buying national coverage. |
| **Real estate appraisal (531320)** | **STRUCTURAL, and consolidated at the wrong layer** | The regulatory event happened 15 years ago (HVCC 2009, Dodd-Frank) and the value went to appraisal management companies, not appraisal firms. Production is still one licensed appraiser per report. Entering as a fabricator of appraisals is entering the fringe. |
| **Land surveying (541370)** | **UNCLEAR. Do not enter on this evidence.** | Q7 is live (aging licensed population) but the scarce input is a **licensed signature**, which capital cannot substitute for. Evidence base is trade-association quality. |
| **Vending (454210)** | **UNCLEAR, leaning STRUCTURAL** | Textbook exogenous sunk cost plus local route density: Sutton predicts persistent fragmentation, and Compass/Canteen's long presence has not eliminated the fringe. The genuine Q1 candidate is telemetry, cashless payment and unattended-retail formats. Whether that escalates far enough to bound concentration is exactly what the literature does not say. |

### Measured concentration (2022 Economic Census, CONCENFI receipts)

This is the right fragmentation instrument and it replaces employees-per-establishment. Computed
from the Census bulk file, not from a market-research estimate. Sorted most fragmented first.

| NAICS | Receipts $B | **CR4** | CR8 | CR50 | Firms |
|---|---:|---:|---:|---:|---:|
| 238220 Plumbing/HVAC contractors | 297.6 | **4.7%** | 6.7% | 14.4% | 112,088 |
| **561790 Other services to buildings** (hood cleaning sits here) | 14.0 | **6.1%** | 7.8% | 15.5% | 17,444 |
| 541370 Surveying and mapping | 11.0 | **8.7%** | 11.6% | 25.4% | 7,225 |
| 811310 Commercial/industrial machinery repair | 54.6 | **10.6%** | 14.2% | 30.7% | 22,020 |
| 811210 Electronic and precision equipment repair | 16.7 | **12.1%** | 18.1% | 40.9% | 10,441 |
| 541191 Title abstract and settlement | 12.5 | **14.9%** | 21.1% | 38.8% | 6,790 |
| 562991 Septic tank and related | 6.3 | **15.5%** | 19.8% | 35.5% | 3,821 |
| 531320 Real estate appraisers | 7.9 | **17.8%** | 24.9% | 45.1% | 12,955 |
| 541940 Veterinary services | 62.8 | **22.4%** | 28.2% | 37.3% | 26,380 |
| 238290 Other building equipment (elevator) | 42.4 | **27.7%** | 32.6% | 49.0% | 6,611 |
| 561621 Security systems (fire ITM) | 31.3 | **34.7%** | 40.6% | 59.2% | 6,161 |
| 561492 Court reporting | 3.1 | **44.0%** | 52.8% | 67.1% | 2,989 |
| 562111 Solid waste collection | 65.8 | **45.8%** | 52.1% | 66.4% | 7,218 |
| 456110 Pharmacies | 543.9 | **71.0%** | 76.3% | 82.0% | 19,676 |
| **812332 Industrial launderers** | 12.0 | **86.8%** | 88.6% | 95.1% | **317** |

**There are 317 industrial laundry firms in the United States and four of them hold 86.8% of the
revenue.** Pharmacy HHI is 1,710.8, into the DOJ/FTC moderately-concentrated band.

**DISQUALIFIED on measured concentration:** veterinary (CR4 22.4% of a $62.8B industry made of
26,380 firms is the signature of a COMPLETED roll-up), pharmacy, court reporting (CR4 44.0% on a
$2.4B base), uniform/linen, solid waste (CR4 45.8% AND no recurring mandate).

Three caveats. For buried niches the CR is for the PARENT industry. The Economic Census excludes
nonemployer businesses, so firm counts UNDERSTATE fragmentation where the sole-proprietor tail is
large (appraisal, septic, court reporting). And the 2017 concentration tables were not retrievable,
so **nobody has checked whether CR4 is RISING in any of these.** That is the single most valuable
follow-up: it separates "fragmented and staying that way" from "being consolidated right now."

### The three candidates that pass BOTH filters

Filter: measured fragmentation AND a recurring compliance clock that is citable in the CFR AND no
funded vertical SaaS incumbent. All concentration figures are 2022 Economic Census, measured.

**1. ASBESTOS / LEAD ABATEMENT plus PHASE I ESA (NAICS 562910, 541620). Strongest overall.**

- **CR4 9.0% (562910) and 12.1% (541620); HHI 43.2 and 62.6.** The DOJ unconcentrated threshold is
  1500. These are an order of magnitude below it. 5,115 and 8,498 firms.
- Sizing is measured, not estimated: abatement is **$5.66B (asbestos $5.147B + lead paint $514.2M),
  24.9% of NAICS 562910**; environmental assessment is **$8.47B, 39.6% of NAICS 541620.**
- **The recurrence is verbatim in the CFR**, which is what makes it defensible in a Q&A:
  - **40 CFR 763.85(b)(1):** AHERA re-inspection of all known or assumed asbestos-containing
    building material **at least once every 3 years**, in every US public and non-profit K-12
    building, by an accredited inspector.
  - **40 CFR 763.92(b)(1):** periodic surveillance **at least once every 6 months.**
  - **40 CFR 745.89(a)(2)(i):** EPA RRP firm certification expires at **5 years.**
  - **40 CFR 312.20:** All Appropriate Inquiries must be conducted **within one year** of
    acquisition, and five components (interviews, lien search, records review, visual inspection,
    the environmental professional declaration) **within 180 days.** That is a re-issuance engine:
    a Phase I goes half-stale in 180 days and dies at one year, forcing a paid update on every deal
    that slips.
- **Roll-up has touched only the top.** TIC Solutions (formerly Acuren, absorbed NV5) is $1.53B
  against a combined $44B, under 4%. Montrose/Onterris $830.5M.
- **No funded vertical SaaS was found at all**, in sharp contrast to every other niche screened.
- Sutton check: accreditation, monitoring apparatus and compliance documentation ARE a chooseable
  fixed cost that amortizes across sites. **Passes Q1.**

**2. PROPANE DISTRIBUTION (NAICS 457210). Strongest compliance clock of anything screened.**

- **CR4 19.5%, HHI 132.8**, 4,083 firms, **41% of establishments under 5 employees.** Suburban
  Propane's own 10-K: the industry is "highly fragmented... thousands of smaller local independent
  marketers and farm cooperatives."
- **Propane is 43.8% of the code, $18.96B.** Do not cite the $43.3B code total; it is half heating oil.
- **The clock, verified verbatim:**
  - **49 CFR 180.205:** nobody may mark a cylinder with a requalification date without a current
    **Requalifier Identification Number**; records kept per location.
  - **49 CFR 180.209(e), (g):** DOT 4B/4BA/4BW/4E cylinders in propane service requalify on a
    **12-year** volumetric cycle, **10-year** repeating proof-pressure alternative, or **5-year**
    repeating external visual inspection, performed only by RIN holders.
  - **49 CFR 192.11:** NFPA 58 is **federally incorporated by reference** and prevails over Part 192
    in a conflict. Amended 89 FR 33280, Apr 29 2024.
- **No venture-funded propane vertical SaaS found.** Signal worth noting: Suburban, the number three
  player, disclosed in FY2025 that it "embarked on a multi-year technology modernization initiative."
  The third-largest operator is still building its own stack in 2025.
- Sutton check: RIN credentialing and requalification infrastructure is escalatable. **But scale is
  route-local (Q2 risk),** which is the same trap that caught hood cleaning.

**3. DENTAL INSTRUMENT STERILIZATION MONITORING. Narrowest, and completely unclaimed.**

- **CDC Guidelines for Infection Control in Dental Health-Care Settings (MMWR RR-52(17)), verified
  at source: biological (spore) indicators "should be used at minimum weekly"** per steam
  sterilizer, plus a test before patient use whenever a sterilizer is new or serviced.
- **The denominator is measured: 135,665 offices of dentists** (CBP 2023), plus 204,617 physician
  offices, 10,042 ambulatory surgical centers, 5,777 hospitals.
- **Weekly is the highest-frequency mandate found anywhere in this research.**
- **No PE platform and no venture-funded software found on this lane.** Closest public comparable is
  Mesa Labs at $249M total company revenue.
- Sutton check: it is **lab-mediated**, so the scale unit genuinely sits above the local route.
  **Passes Q2**, which propane and hood cleaning do not.
- Honest weakness: the service itself is not measurably captured in US statistics because the work
  is overwhelmingly done in-house. The residual NAICS bucket that could hold it is only $272.8M.
  Small ticket, high frequency, and that is exactly why nobody has rolled it up.

### The two frameworks disagree on the next candidate, and the disagreement is the answer

**Commercial kitchen exhaust hood cleaning** ranks first on the compliance-and-fragmentation screen:
CR4 **6.1%**, 1.01 establishments per firm (the lowest in the set), **96% of establishments under 20
employees**, NFPA 96 mandating cleaning monthly to annually by cooking volume with immediate action
above 0.002 in grease depth, **+22% establishments and +20% employment 2019 to 2023** (the fastest
growth in the set), consolidation so far **franchise-led not PE-led**, and **no funded vertical SaaS
found at all**.

**And it FAILS Sutton Q1.** Truck, pressure washer, crew: all exogenous sunk costs. Scale is
route-local. AHJ acceptance is county-by-county. There is nothing to escalate on, which is exactly
why it has stayed fragmented and why it will keep staying fragmented.

**Resolution, and it maps onto the two shapes:** hood cleaning is a good business to OPERATE and a
bad business to ROLL UP or to build venture-scale software for. The screen and the theory are both
right, about different questions. Use this as the worked example of why "fragmented plus mandated
demand" is not sufficient.

Note also: **US kitchen exhaust cleaning has no separately measured market size.** The 2022 NAPCS
table identifies duct cleaning ($843.6M) and chimney cleaning ($681.4M) but has no KEC line; it
falls into "Other specialized cleaning services, NEC," $8.248B. Do not fabricate a KEC market size.

### The best measured niche sizing in the entire file

**Biomedical / medical equipment servicing.** 2022 NAPCS product line: "Maintenance and repair
services for precision electronic medical equipment" = **$3.936B inside NAICS 811210, which is 75%
of that product line's US total, implying a US total of about $5.25B (2022).**

That is a **Census-measured size for the actual niche**, not a market-research estimate. Nothing
else in this file has an equivalent, and market-size credibility is rubric criterion 3.

Caveats: CR4 12.1%, so genuinely fragmented, but the outsourcing incumbents (TRIMEDX, Agiliti,
Sodexo HTM, Crothall) are already there and capitalized. And 42 CFR 482.41 does NOT itself prescribe
a maintenance interval; the frequency requirement comes from NFPA 99 Chapter 10 and Joint Commission
EC.02.04.03, **neither of which was verified.** Pull the TJC standard text before relying on it.

### Two candidates that fail on inspection

- **Portable toilets fail the compliance filter.** OSHA 29 CFR 1926.51 Table D-1 mandates a
  toilet-to-worker RATIO (1 per 20 workers, then per 40, then per 50), **not a servicing frequency**.
  Recurring revenue comes from the rental contract, not a mandated interval. Establishments per firm
  is 1.87, the multi-unit signal of an industry already consolidating.
- **Title work splits into two different industries and the brief conflates them.** The
  **underwriting** layer is $21.187B and 99.8% of it sits in NAICS 524127, which is the famously
  four-family-concentrated one. The **abstract and settlement** layer is $12.5B at CR4 14.9% and is
  genuinely fragmented. Two businesses, two verdicts.

### Local reachability (the D21 criterion)

| Niche | Indiana | Tippecanoe |
|---|---|---|
| Commercial & industrial machinery repair (811310) | 822 | **13** |
| Electronic & precision equipment repair (811210) | 344 | 7 |
| Other services to buildings (561790) | 299 | 6 |
| Land surveying (541370) | 161 | 6 |
| Farm & garden machinery wholesale (423820), the DEALER channel | **329** | - |

**Three source vintages appear in this file and they are not interchangeable.** 2022 Economic Census
(concentration and receipts), Census CBP 2023 (establishment counts with payroll), BLS QCEW 2024
(UI-covered employers). All measured. **Cite one, name which, never blend.**

### More candidates killed on measured evidence

- **Garage doors: the obvious NAICS is the wrong one, and the niche is the most crowded screened.**
  Residential garage door installation is **238350 Finish Carpentry (CR4 4.4%, HHI 9.1)**, not
  238290, which is 41% elevators. Census kind-of-business code 8351 puts **90.5% of residential
  garage door revenue in 238350 and only 5.9% in 238290.** Genuinely atomistic at the operator level,
  but: **KKR agreed to buy A1 Garage Door Service for roughly $2B on 2026-09-02**, Oak Hill took
  Guild Garage for over $800M at ~16x in March 2026, plus Gridiron, Soundcore, Trivest and
  Neighborly/KKR platforms. The manufacturer layer is already consolidated across Griffon, Sanwa,
  ASSA ABLOY and Nucor. ServiceTitan already ships a garage-door SKU.
- **Sign manufacturing (339950): genuinely fragmented, zero compliance clock.** CR4 10.0%, HHI 45.2,
  85.5% of establishments under 20 employees. But every regulatory event is **one-time per sign**
  (zoning permit, UL 48 listing, NEC Article 600 inspection). Demand is cyclical retail and franchise
  remodel, not compliance-clocked. The shop-software layer is already PE-consolidated (Inktavo,
  backed by PSG and Blue Star, which bought SignTracker in 2023).
- **Powder coating (332812): the CR4 is a data artifact.** Reported CR4 is 32.9%, but the top four
  firms book $5.92B on **8 establishments and 1,212 employees**, i.e. $4.88M revenue per employee
  against a $354K industry average. That is enterprise-level tax receipts landing on a few
  establishments. **The honest read from the same table is employment CR4 of 2.4%.** Killer:
  Steelhead Technologies raised **$84M from Mainsail in Dec 2025** on top of a $6M Series A and owns
  exactly this customer. And powder coating has **no compliance annuity** (it is a dry process,
  which is precisely why it avoids the VOC permitting that binds electroplating in 332813).
- **Pest control (561710): CR4 31.1%, and its compliance is licensure of the OPERATOR** (40 CFR
  171.107, five-year ceiling), not a recurring mandated service event on the customer. The recurring
  revenue is contractual, not regulatory. Software lane closed by a post-IPO public company.
- **Interpretation/translation (541930): CR4 35.1%, CR8 47.9%, CR50 74.7%.** Most consolidated
  screened. The one real gap is structural and strange: **52,354 sole proprietors, 95% of all firms
  in the industry, averaging $25,683 in receipts, sitting entirely outside the agency layer.**
- **Pool service: the best-measured niche and the software lane is taken.** Pool cleaning is
  **42.5% of NAICS 561790, a hard $5.94B**, CR4 6.1%, HHI rounds to zero, 5.0 employees per
  establishment. But Skimmer already claims 30,000+ pool pros, which is more than the 17,342
  employer firms, meaning it is already deep into the nonemployer tail.
- **Water treatment has NO federal statistical existence.** There is no NAPCS product line anywhere
  for residential or commercial water conditioning. And its apparent regulatory wedge is being
  **loosened**: on 2026-05-18 EPA proposed giving systems two more years (to 2031) on PFOA/PFOS and
  **rescinding the PFHxS, PFNA, HFPO-DA and Hazard Index regulations entirely.** Those rules also
  bind the water utility, never the dealer.

### Nonemployer Statistics is where route fragmentation actually lives

CBP and the Economic Census count only employer firms, so every fragmentation claim built on them
**understates these niches by roughly an order of magnitude**:
- Pool service: **141,015 nonemployer firms** against 17,342 employer firms. 89% of the universe.
- Building equipment contractors: **347,463 nonemployers** against 107,004 employer firms.
- Interpretation: **52,354 nonemployers** against 2,728 employer firms.
- Building finishing (where residential garage doors live): **669,136 nonemployers**, ~21x the
  employer firm count, with roughly equal revenue.

**NAICS hygiene, and one trap that silently returns nothing.** **The vending and fuel-dealer
renumbering was the 2022 NAICS revision, not 2017:** 454210 became **445132** (vending) and 454310
became **457210** (fuel dealers). **County Business Patterns has NOT migrated: the 2022 AND 2023 CBP
files still publish on 2017 NAICS.** So a join between CBP and the Economic Census on 445132 or
457210 returns zero rows without erroring. Use 454210/454310 for CBP, 445132/457210 for the Economic
Census. Separately: **codes 811110 and 811114 do not exist** (auto repair splits into 811111, 811121,
811191, 811192, 811198), and pharmacy moved 446110 to 456110. Anyone citing "811110" copied a
market-size figure rather than computing one. Useful tell when reading a competitor deck.

**Grain bin cleaning, hoof trimming, and drainage tile have NO separable NAICS code.** They do not
appear in QCEW or CBP at any published aggregation. Real evidence of under-coverage, AND it means
any TAM number on them would be an unsourced guess. Do not put one in a deck.

## 5. Crowding: the thesis is a consensus trade

| Entity | Capital | Note |
|---|---|---|
| **Thrive Holdings** | **$2B at a $12B valuation** (2026-08-12) | SoftBank, D1, Altimeter. OpenAI took a stake Dec 2025. **70+ businesses owned.** |
| General Catalyst "Creation" | $1.5B inaugural fund | 10+ co-created roll-ups |
| Long Lake (HOA) | ~$670M, 30 acquisitions, ~$100M EBITDA in under two years | GC, Thrive, Elad Gil |
| Crete Professionals Alliance | $500M AI accounting roll-up | ~30 firms |
| Metropolis (parking) | $1.6B equity plus debt | Bought SP Plus, ~$1.5B EV |

Named committed capital comfortably exceeds $5B. Elad Gil's public thesis is verbatim the one being
tested. **Saturated verticals: accounting (>35% of the top 30 US firms had sold a stake by June
2026), HVAC/plumbing/electrical (22 consolidators, 21 PE-backed, ~800 companies since 2022), fire
and life safety (129 PE acquisitions in 2023 alone), veterinary (corporate ownership ~8% in 2011 to
~50% by 2025).**

**But read the crowding correctly, because the naive reading is wrong.** These vehicles **buy firms;
they do not sell to firms.** They are non-competing with a software concept, they are the best
possible software customers (budget, mandate, one decision maker), and they are a plausible exit.
Absence of capital would be the worse signal. And none of them is buying a $400k-revenue machinery
repair shop in Tippecanoe County: institutional minimum deal size is the gap.

**Search funds are crowded too, and the tell is subtle.** Stanford 2026 study: aggregate IRR 33.9%,
4.75x ROIC. But the acquisition rate fell from 58% lifetime to **~50% for the 2021-2024 cohort**
while new fund formation held at record highs. More searchers, same deal flow, fewer closing.

---

## 6. Do not cite these. They will end a Q&A.

1. **The silver tsunami.** The whole edifice traces to ONE Census graphic published 2020-09-25
   reporting **data year 2018**, employer businesses only, 4.1M responding owners, 55+ = 51% of
   **OWNERS**. Project Equity's 2.9M firms / 32M employees / $6.5T is a **two-page marketing
   infographic with zero footnotes, no methodology and no data year**, from an employee-ownership
   advocacy nonprofit; their own press release says 2.3M, unreconciled. Exit Planning Institute's
   "only 20-30% of businesses that go to market actually sell" **does not appear in the report it is
   attributed to** (the full 2023 National State of Owner Readiness Report was pulled and text
   searched); EPI sells exit-planning certification.
   **The measured counterweight:** Census BDS shows the firm population GREW from 5,281,916 (2018) to
   5,593,727 (2023), **+5.9%, straight through the window the wave was forecast to hit.**
   **And the decisive test:** BizBuySell closed transactions ran 9,092 (2023), 9,546 (2024),
   **9,586 (2025, +0.4%)**. Under 10,000 a year, FLAT for three years, while the wave was cresting.
   A demographic wave converting into transactions produces a CLIMBING series. It is not climbing.
   Honest reading: most boomer-owned businesses will not sell. They close, wind down, or transfer
   inside a family. (Note: no government statistic counts ownership transfers at all, which is
   exactly why the advocacy numbers went unchallenged.)
2. **"70-90% of M&A fails."** The Christensen HBR 2011 article asserts it with no source.
3. **"90% of small businesses fail."** BLS says ~49% survive five years, and it cuts AGAINST you.
4. **The 17% management-consulting productivity effect applied to US micro-businesses.** Bloom et al.
   QJE 2013 is **17 firms, 28 plants, 20 experimental (14 treatment, 6 control)**, mid-size Indian
   textile mills near Mumbai, all family owned and managed, **26% take-up**, treated with consulting
   that would have been priced at **$250,000 per firm**. Randomization was at the FIRM level, so the
   effective inference N is **17, not 28**. **The 95% confidence interval on the TFP effect runs
   [+1.4%, +120%] and the permutation p-value is .061.** "17%" is the midpoint of a very wide band.
   The one large US RCT (Fairlie, Karlan & Zinman, AEJ:EP 2015) found "no evidence of broader or
   longer-run effects on business ownership, business performance."
   Related figures that are NOT measured: the **$325,000 profit per plant per year is IMPUTED** (the
   authors never observed profits and say so), and the follow-up's **"+35% productivity after 8
   years" is doubly extrapolated** (the measured effect is +51% looms per employee, converted via an
   elasticity estimated on a separate survey of 113 other firms).
5. **"Well-managed firms are 45 to 69% more productive."** That is a RAW cross-sectional correlation
   with no capital, materials, industry or country controls (AMP 2012). **The controlled figure is
   +4.0% TFP per standard deviation of management** (Bloom & Van Reenen 2007, Table I col 4).
6. **"Management explains 20% of productivity variation, more than R&D, ICT and human capital
   combined."** Wrong paraphrase, and it inverts the comparison in management's favour. The AER 2019
   abstract says "a similar, or greater, percentage as that accounted for by R&D, ICT, **or** human
   capital" - individually. The working-paper decomposition: management 18.1%, R&D 16.9%, skills
   11.1%, IT 7.5%, **all four jointly 32.5%**. Also: if you say TFP, the MOPS figure is 18.1%, not
   "20%+", which is labor productivity.
7. **Any causal reading of the management-productivity correlation.** In the WMS panel the
   coefficient falls from 0.148 cross-sectionally to **0.028 with firm fixed effects, an ~80% drop**.
   And Bender, Bloom, Card, Van Reenen & Wolter (JOLE 2018) find **~13% of the correlation is the
   human capital of the highest-paid workers and a similar amount runs through pay premiums** - so
   roughly a quarter is worker sorting, not management doing work. That result comes from the
   founders of the literature, which is both to their credit and a reason to discount the raw numbers.
8. **"Founder-owned firms are the worst managed" sourced to Bloom & Van Reenen 2007.** It is not in
   that paper. It IS in Bloom, Genakos, Sadun & Van Reenen (AMP 2012, Figure 7, n=9,085 manufacturers
   plus 658 retailers), which ranks founder-owned/founder-CEO firms LAST, below family-CEO firms.
   Two cautions: the scores are readable only off a bar chart (axis runs 2.7 to 3.2), so do not quote
   decimals; and the authors say openly they are "still trying to understand this phenomenon."
   **Cite AMP 2012 for founder-CEO, BVR 2007 for primogeniture. They are different findings in
   different papers and conflating them is checkable.**
9. **Any CRM / field-service-software penetration statistic.** No independent statistical agency
   measures it. Census ABS asks about "specialized software" without naming CRM or FSM; BTOS asks
   only about AI; the Fed SBCS asks about credit; BLS has nothing. Every "X% of home service
   businesses have no online booking" traces to SEO content with no methodology.
10. **Do not blend the AI-adoption surveys.** Fed SBCS says 46%, Census BTOS says ~19.8%. SBCS asks
   whether the business OR ANY EMPLOYEE uses AI at all; BTOS asks about AI used in PRODUCING GOODS OR
   SERVICES in the last two weeks. Averaging them is credibility-ending.


### And these three were in this file's own first draft, killed by the skeptic round

- **Roto-Rooter "under 0.4% of a $191.4B plumbing market."** Broken comparison. The denominator is
  NAICS 238220, which includes HVAC installation and new-construction rough-in. Roto-Rooter does
  drain cleaning and repair. Cut.
- **Floor & Decor "approximately 5% of a $17 billion market" as a CEILING.** That is the 2017 S-1.
  By its 2022 Investor Day the company put itself at roughly 10% of a $41B market on about 4x the
  revenue. Share doubled. It is bull evidence.
- **Mister Car Wash taken private at $7.00 against a $15.00 IPO price, as proof modernization fails.**
  The $7.00 was a **29% premium to the 90-day VWAP**, from Leonard Green, the existing controlling
  sponsor, in a squeeze-out under shareholder investigation for being too low. Correct reading:
  operating result and equity result decoupled. Revenue went $124M (2010) to $1.05B (2025); the
  equity outcome was 2021 IPO-vintage multiple compression plus leverage plus a related-party buyer.
  That is a point about venture-scale EXIT risk, not about whether modernization works.

---

## 7. The bull evidence, kept honest

The first draft of this file was over-corrected bearish. The skeptic round caught it.

- **Copart is the strongest counterexample and it was missing.** A fragmented industry of independent
  local salvage yards, taken to roughly **47-50% North American share** (Copart plus IAA is 80-90%),
  with essentially one lever: moving the auctions online, 2003. Tens of billions of market cap.
  Same mechanism the winners section identifies, and it did not hit a low ceiling.
- **ServiceTitan at roughly $7.5B public** is proof that selling software into mom-and-pop trades
  produced a multi-billion-dollar outcome. It is not only a crowding datapoint.
- **Atkin et al. is a product spec, not bear evidence.** Read whole: a majority of firms adopted
  **once a worker pay-incentive program was introduced.** The barrier is solvable by redesigning the
  incentive. **The thing that sells is the thing that does not cost the technician income during the
  learning curve.** That is a sharper product principle than anything else in this file.
- **What actually moved numbers in the verified winners** was never "modern management practices."
  It was converting transactional demand into recurring or contracted demand: Mister Car Wash's
  subscription 62% to 76% of wash sales; SCI's preneed contract financing to ~18% North American
  share; Rollins FY2025 +11.0% = **6.9pp organic** plus 4.1pp acquired.
- **One genuinely under-assumed opening:** ADA Health Policy Institute, US Dentist Workforce 2025.
  **16.1% of US dentists were DSO-affiliated in 2024** (up from 7.2% in 2015), **but over 25% of
  dentists within ten years of graduation are.** The headline number is far lower than vet or
  accounting, and the young-dentist gap is a real structural signal.

### The BCG figure, with the context that changes it

Small platforms 52.4% IRR vs 20.3% standalone; large platforms invert, 12.5% vs 16.2%. **But: 121
transactions, ~90% European, exits 1998-2012, median deal size $198M at entry, and "small platform"
means under $70M enterprise value, larger than anything a student holdco will ever own.** And in the
same table, **deals with more than two add-ons underperformed standalone, 19.9% vs 23.1%** which is a
direct strike against ANY roll-up thesis including the narrow one.

Also: IRR is duration-sensitive (a 2-year 2.0x is 41% IRR; a 7-year 3.0x is 17%), and citing a
**median** MOIC against a venture concept is a category error. Venture is a tail business; the same
statistic would have argued against every venture outcome that ever mattered.

---

## 8. The narrow thesis that survives

> In a niche where **(a)** an endogenous sunk cost is available to manufacture and escalate;
> **(b)** the fixed-cost floor has RECENTLY moved by a dated, citable event; **(c)** the scale unit
> sits above the local route; **(d)** quality was not just made observable by reviews or marketplaces
> (which de-consolidates); and **(e)** institutional capital is absent at the deal size in question,
> a disciplined operator can compound a durable business.

Two shapes, both requested, and they are not symmetric:

**Be the operator.** Truest to the source anecdotes. Real businesses get built this way. But it is an
operating or acquisition strategy, the financing system screens explicitly for operating experience
(SBA 7(a) acquisition lenders typically want 2+ years of management or industry experience), and it
is not what a venture CONCEPT competition judges. Expected shape is $10M to $100M of enterprise value
over a decade, not a venture outcome.

**Sell to the operators.** Fits the competition and the winner precedent. **But the naive version is
already refuted:** ServiceTitan public at ~$7.5B, Housecall Pro's $125M from Permira, Jobber's $100M
Series D and BuildOps at $1B all sell CRM, dispatch and marketing automation into exactly this
customer. That category is not unserved, it is saturated. **The unmet need in the same data is
INTEGRATION**: ServiceTitan's own commercial research shows 4 to 6 software providers per firm,
**only 20% on a single integrated platform, 49% still on spreadsheets.**

**The hybrid is what the evidence actually supports:** operate or embed in one niche long enough to
own the workflow, then sell the layer. It is the only shape that generates the customer evidence the
rubric weights AND escapes the "student with a CRM" objection.

---

## 9. What the skeptic round says to do instead

Both skeptics converged on the same finding, and it outranks everything above.

**This file has 40+ citations, zero interviews, zero named customers and no product.** Every open
question in it is resolvable only by more reading, which means the research generates more research
and never terminates. The concept submission is due **2026-09-27**. `STATE.md` already says the next
physical action is one walk-in or call to a named owner, and D21 says select on soonest askable at
the smallest price.

**The research is done. It has produced one dated, checkable, locally reachable lead and a diagnostic
to test it with. The next artifact is not another document.**

**The niche to call is asbestos/lead abatement and Phase I ESA.** It wins on every filter that
survived the skeptic round: CR4 9.0% and 12.1% with HHIs of 43 and 63, recurrence written verbatim
into the CFR on 6-month, 3-year, 5-year and 180-day clocks, roll-up under 4% of the combined market,
no funded vertical SaaS found anywhere, and an endogenous sunk cost (accreditation and compliance
apparatus) that actually passes Sutton Q1. Locally reachable: **270 Indiana establishments and 8 in
Tippecanoe County for environmental consulting, 171 and 3 for remediation** (QCEW 2024).

Ten calls, five questions:
1. What is your backlog in days, and did you turn work away last month? (Tests demand vs labor
   directly, which is the thing the NFIB survey cannot settle. This is the question that decides
   whether any version of the thesis is live.)
2. Have you raised prices in the last year? (If capacity binds and they have not, the constraint is
   not binding or the owner is not optimizing. Either answer is decisive.)
3. What software do you run, how many separate systems, and where do they fail to talk?
4. **How do you track AHERA 3-year re-inspections and 6-month surveillance across your school
   district clients, and what happens when one slips?** (Tests whether the CFR clock is a real
   operational pain or already solved by a spreadsheet nobody minds.)
5. **How often does a Phase I go stale at the 180-day mark and have to be re-issued, and who eats
   that cost?** (Tests the re-issuance engine, which is the actual revenue mechanism.)

**One reachability check before dialing, worth four minutes:** Firmly, the fintech startup where
Veer interned and shipped features, is his only `prior-employment` origination surface, and
prior-employment is the stronger origination mode on resources and revenue. `STATE.md` asks him to
name three humans there who would take a 20-minute call. If they do not exist, that surface is dead
and should stop being cited as access.

Ten calls settle more than this entire file. They are also rejectable, dated, and under an hour,
which is exactly the shape of action this search should prefer.

---

## Sources with the strongest standing

Census CBP 2023 (primary file), Census BDS 2023, Census ABS 2023 table AB2300CSCBO (primary
microdata), BLS QCEW 2024, Census BTOS via NBER w32319, Bloom & Van Reenen QJE 2007, Bloom et al.
AER 2019, Bloom et al. QJE 2013, Atkin et al. NBER w21417, Sutton 1991, Ellickson RAND 2007, Luca
HBS 12-016, Abrate et al. 2012, FTC v. Deere stipulated order 2026-07-08, Cal/OSHA section 5204,
ADA HPI US Dentist Workforce 2025, Yale SOM Oct 2025, Stanford GSB 2026 Search Fund Study, SEC
filings for Rollins, SCI, Mister Car Wash, ServiceTitan, Floor & Decor, Chemed, Extra Space.

**Unverified, do not put in front of judges without a source:** "The Deployment Company (OpenAI +
Anthropic)" and "Ode (Anthropic + Blackstone)"; the "~22 of ~26 winning concepts" figure; the vending
Outerwall reconstruction; Rentokil technician-retention and Guild Garage deal terms; the claim that
the four software-open verticals are open BECAUSE PE decided software was not the prize (unfalsifiable
as stated).
