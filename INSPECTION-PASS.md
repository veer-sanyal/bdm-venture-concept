# First-time inspection pass for small contractors

## ⚠⚠⚠ VERIFICATION SWEEP 2026-09-06 (late). READ THIS BEFORE ANYTHING BELOW.
Eleven agents. Two findings invert prior conclusions. Everything below this block predates them.

### 1. THE DATA CEILING IS NOT 6 JURISDICTIONS. The product does not need bulk open data.

**VERIFIED end-to-end, anonymously, no login, no API key, no bulk dataset.** Per-permit inspection
history with result codes is publicly retrievable on **Accela Citizen Access**, **CentralSquare
eTRAKiT** and **CentralSquare CityView**. Real values retrieved from live production portals:

| Portal | Jurisdiction | Values actually returned |
|---|---|---|
| Accela ACA | Fremont CA (BLD2021-00494) | `Pass`, **`Fail - Not Ready`**, `Cancelled - Time Constraint`, `Cancelled - Contractor/Owne`, `Pass - CO Not Required`, **with inspector names and dates** |
| Accela ACA | Pima County AZ | `Partial`, `Not Ready`, `Pass` (9 pages) |
| Accela ACA | Pinellas County FL | `Correction Notice`, `Approved`, `Cancelled` |
| Accela ACA | Pasco County FL | `Continued`, `Fail`, `Pass` |
| Accela ACA | Cleveland OH | `Work in progress`, `No Entry` |
| eTRAKiT | Los Altos CA (56 inspections) | `APPROVED, CORRECTION NOTICE, CANCELLED, PARTIAL APPROVAL, NOT READY` |
| CityView | cvportal.us permitId=65008 | Passed x22, Failed x18, Canceled x1, Not Required x18 |

**The full product loop was run end-to-end on Pasco, anonymously:** Accela's public "Search by Licensed
Professional Information" takes a license number (`CCC1327410` returned 74 permits in Pinellas, 53 in
Pasco), each row carrying the capID triple needed to pull that permit's inspection history. There is
even a native "Download results" export. Per-inspection detail is a plain GET returning status, status
history, inspector, and **verbatim inspector comments**. 19 of 20 sampled Accela agency codes returned
HTTP 200 anonymously. Pagination works (`__EVENTARGUMENT=Page$2`) - full history, not page one.

**No legal barrier found.** robots.txt is **404 on all nine portal hosts checked**, including
`aca-prod.accela.com`. Accela's terms contain no automated-access prohibition. And where authorization
IS wanted, Accela ships it as a feature: `POST /v4/citizenaccess/citizens/delegates` lets a citizen
"designate other citizen users as their delegates and grant the delegates permissions to access their
data."

**Tyler EnerGov / Civic Access (CSS) - VERIFIED as a FOURTH platform.** Read from the live app's own
label API on `raleighnc-energovpub.tylerhost.net` (CSS v2024.4.3.19), not inferred and not rendered:
- The permit record has an **Inspections tab** (`PermitTabs.inspections`), deep-linkable as
  `#/permit/<guid>?tab=inspections`.
- The **"Existing Inspections"** grid columns are **Description / Request Date / Scheduled Date /
  Inspector / Status**, plus a separate **"Previous Inspections"** view.
- Per-inspection detail carries `Inspection Status:`, `Completed Date:`, `Comments`, `Is Reinspection`,
  the literal string `Passed`, and a **Checklist grid with a Passed column (Yes / No / N/A)**.
- Permit status reason codes include **`'Inspection Not Passed'`**.
- **Inspections is a first-class module in the portal's PUBLIC RECORDS search**, filterable by Status.
- API base `/apps/selfservice/api`, with a route **literally named
  `POST /energov/entity/inspections/search/unauth`**. A GET returns HTTP 405 ("does not support http
  method 'GET'"), so the route exists and does not challenge for auth. The request model includes
  **`IsFailed`** as a first-class filter alongside `ModuleId`, `EntityId`, `IsExistingInspection`.
- **No API key mechanism exists in the bundle at all. No Swagger. No rate-limit headers, no CDN or WAF
  (raw IIS 10 / ASP.NET). robots.txt is 404 on every tylerhost.net portal tested. `FooterHtml` is null
  on Raleigh and Wake County, so no terms link renders.** Tyler publishes no developer portal -
  `developer.tylertech.com`, `api.tylertech.com` and `docs.tylertech.com` all fail DNS, and the product
  page never mentions an API.
- Caveat on wording: the field is **`Status`**, not "Result", and the **status vocabulary is per-agency
  configuration**, not a shipped constant. NOT VERIFIED which values any given city uses.

**⚠ THE ONE UNRESOLVED GATE, and it is the same shape as the Accela postback trap below.** CSS **hides
the Inspections tab entirely and silently falls back to another tab** when the API returns 403 - the
string is `'Not authorized to view inspections.'` **Whether an anonymous caller receives rows is
per-TENANT configuration, not a product constant.** One POST to
`/apps/selfservice/api/energov/entity/inspections/search/unauth` with
`{ModuleId:1, EntityId:<a real permit guid>, IsExistingInspection:true, PageNumber:1, PageSize:100}`
settles it in a single call. **NOT YET RUN** - it is an unauthenticated call into a live municipal
system, and the Accela path already proves feasibility. Veer's call.

**Incidental, flagged and deliberately NOT acted on:** that portal's unauthenticated
`GET /apps/selfservice/api/globalsetting/getglobalsetting` returns the site's
**`GoogleRecaptchaSecretKey` in plaintext to any anonymous caller.** That is a real misconfiguration on
a city's live system. **Do not build on it.** Responsible disclosure to the city's IT department would,
however, be a legitimate first contact with a govtech buyer.

### THE PLATFORM BOUNDARY, now closed. Four yes, three no.

| Platform | Public per-inspection RESULT? | Verdict |
|---|---|---|
| **Accela Citizen Access** | **YES** - Pass / Fail-Not Ready / Partial / Correction Notice / Cancelled, plus inspector name and verbatim comments | **USE** (proven end-to-end, 7 agencies) |
| **CentralSquare eTRAKiT** | **YES** - APPROVED / CORRECTION NOTICE / CANCELLED / PARTIAL APPROVAL / NOT READY | **USE** |
| **CentralSquare CityView** | **YES** - Passed / Failed / Canceled / Not Required | **USE** |
| **Tyler EnerGov** | **YES** at schema level - `Status` column, `Passed`, Yes/No/N/A checklist | **USE**, one POST from full confirmation |
| **Camino / Clariti Launch** | **YES** but nearly nobody has it on | **MARGINAL** - see below |
| **OpenGov PLC** | Probably, but **DELIBERATELY WALLED** | **DO NOT SCRAPE** - see below |
| **Cloudpermit** | **NO. Proven across all 510 US tenants** | **DEAD** |
| **Clariti Enterprise** | **NO - login only** | **DEAD** |

**⚠ OPENGOV IS AN ETHICAL LINE, NOT A TECHNICAL ONE, AND IT IS THE OPPOSITE OF THE OTHERS.** Where
Accela, eTRAKiT, CityView and Tyler all return **404 on robots.txt**, OpenGov's citizen portals return,
verbatim:
```
User-agent: *
Disallow: /
```
on `somervillema`, `cambridgema` and `boulder`. On top of that, public search is gated behind
**Cloudflare Turnstile** (`plc-rails-search-turnstile-enforce: true` in the page's own LaunchDarkly
payload), and typing a query fires **zero** network requests until a token is issued. Their developer
terms also forbid using the materials "to create a competing product or service."
**This is the most deliberately anti-automation posture of the seven platforms, and it is explicit.
Do not scrape OpenGov. The Turnstile was NOT solved and must not be.** Their client bundle does carry a
`PublicInspection` component and the exact vocabulary ("an overall Pass/Fail/Partial Pass/Not Inspected
status"), so the data is probably there - but the correct route is the API, and the API is
agency-onboarded (Entity Admin role required per city). If it ever matters, **a human opening
`durangoco.portal.opengov.com/search` once by hand settles what renders.** That is a person's five
minutes, not a scraper's.

**CLOUDPERMIT IS A PROVEN NO, and the proof method is worth keeping.** Its unauthenticated
`/api/command/public-records/config?branding=<slug>` returns each agency's explicit publication
whitelist. Pulled for **all 510 US tenants**: 277 returned a config, 148 carry a whitelist, and the
**complete union of publicly exposed fields across every US tenant is 13 attributes** - category names,
`domain/state`, case id, description, work types, dates, applicants, owners. **Zero tenants expose any
inspection attribute.** Record lifecycle state (`submitted`, `in-review`, `permit-issued`,
`construction-started`) is the ceiling. Their Inspections API exists but is contract-gated: "A contract
will be provided for adding API services."

**CAMINO / CLARITI LAUNCH is real but tiny.** Anonymous deep-linkable record pages carry a genuine
**Inspections** section, and the shipped public GraphQL query returns
`{ title, scheduledDate, statusLabel, statusColor, completed }` per inspection - `statusLabel` being the
result. But probing organization ids 1-259 found **exactly 6 orgs with the public portal enabled**.
Syracuse and Pleasant Hill both have it OFF. Not a coverage story yet; worth re-checking later.
(Note `getcamino.com` is now a parked domain; the live infrastructure is `app.oncamino.com`,
`claritilaunch.com`, `api.app.oncamino.com`.)

**AND THE CRITICAL STRUCTURAL FINDING ACROSS ALL FOUR OF THESE VENDORS: there is no
applicant-delegated API anywhere.** OpenGov requires the **Entity Admin role at each city**; Cloudpermit
requires a contract; Camino requires an account-manager-designated Developer Manager per agency; Clariti
publishes no API at all. **No OAuth-consent or act-on-behalf-of pattern exists in any of them.** So "the
contractor authorizes us to read his own permits" is NOT a route through these platforms - it only works
via Accela's `citizens/delegates` mechanism or via public portal pages. **That materially narrows the
'we just need the customer's own history' framing: it holds on the four USE platforms and nowhere else.**

**NOT VERIFIED:** OpenGov, Cloudpermit, Clariti. (Camino is no longer separate - camino.ai states
"Camino Technologies is now a Clariti Software company.") Documented rate limits: NOT VERIFIED on any
platform, not probed.

**The Construct API is gated; the portal is not.** `GET /v4/records/{recordId}/inspections` and
`/v4/inspections/{ids}/histories` are App Type "All" with citizen scope, but `GET /v4/agencies` -
documented as no-auth - returns HTTP 400 demanding `x-accela-appid`, and the agency/environment pair
requires contacting Accela Support. **Use the portal path.**

### ⚠ THE FAILURE MODE THAT WOULD HAVE BITTEN SILENTLY
**CONFIRMED ON TWO INDEPENDENT VENDORS. This is the single most important engineering finding here.**
Naive HTTP fetching returns a **silent false negative** on both major platforms:
- **Accela** renders "There are no completed inspections on this record" on EVERY record until the
  async postback is triggered - including permits marked Finaled.
- **Tyler EnerGov** returns an unrendered Angular shell (literal `{{vm.greetingText}}` template syntax),
  no permit data at all.

**Both look like a clean, empty inspection history.** A product built on naive fetching reports spotless
records for contractors who actually failed. The error is invisible, and it runs in the direction that
flatters the customer - which is the direction nobody reports as a bug. **Design against it explicitly,
with a per-jurisdiction probe that asserts a known-failed permit still reads as failed.**

The Accela completed-inspection grid lives in an UpdatePanel filled by a `btnRefreshGridView` async
postback. **A plain GET returns "There are no completed inspections on this record" on EVERY record -
including permits marked Finaled.** Triggering the postback requires the full hidden-field set plus the
`ACA_CS_FIELD` CSRF token (omit it and you get "Invalid viewstate"). **A naive scraper silently reports
clean inspection records for contractors who actually failed** - an invisible error that runs in the
flattering direction. Design against it explicitly, with a per-jurisdiction probe.

**The real ceiling is per-DEPLOYMENT, not per-vendor, and it is a scraping-engineering ceiling.**
Coral Springs eTRAKiT gates search behind reCAPTCHA; Routt County CityView returns an image CAPTCHA;
Carrollton's CityView renders no Inspections section at all. Identical URL shapes on the same product
resolve to full data in one city and a wall in the next, **and no directory anywhere tells you which**.
Coverage gets built city by city. That is a different company than "we read open data."

**Do NOT quote a market-share fraction.** Accela claims "over 900 agencies," Government Technology
(Feb 2026) says "more than 600" - a 50% discrepancy between two sources. The 2022 Census of Governments
gives 90,837 local units but **publishes no count of permit-issuing jurisdictions**. No numerator, no
denominator. The one reproducible floor: GitHub code search for `aca-prod.accela.com` yields **107
distinct agency codes** (ATLANTA, AUSTIN, CCSF, DALLASTX, DENVER, KINGCO, SACRAMENTO, SANDIEGO...).

### 2. "NOBODY SELLS FAILURE REDUCTION TO CONTRACTORS" IS FALSE. Stop saying it.

Four vendors sell against inspection failure, to contractors, today:
- **Inspected.com** - "Same-Day Virtual Inspections for Contractors," "Eliminate return trips,"
  **from $99**; blog: "verify readiness through virtual inspections before the official arrives"
- **InspectPilot AI** - "Built for LA General Contractors. Nobody Else." Priced against
  **"$1,200 per failed inspection."** Same buyer, same city, same vocabulary as this whole analysis
- **Constructable.ai** - Inspections tool that "let[s] your team run internal field reviews before the
  inspector arrives" (and says out loud it is not a portal to the building department)
- **Zepth** - markets "Authority Inspections: Pass First Time, Every Time"

And worse than any competitor: **Salt Lake City publishes a free "Inspection Success Checklist" and
pushes a free inspections app.** The price floor for static readiness content is zero.

**THE NARROW CLAIM THAT SURVIVES**, tested against 14 construction-management platforms, 7 permit-tech
players, 7 trade associations, 3 code publishers, 8 municipal-software vendors, the contractor
marketplaces and the 2024-26 funding set:

> **Nobody sells a jurisdiction-aware go/no-go on a specific job the day before a specific municipal
> inspection.**

Everything found is one of five things, none of which is that: **reference** (ICC, UpCodes, NFPA),
**transaction** (PermitFlow, iPermit, Permits.com, Accela), **self-authored QC** (all 14 CM platforms -
you write your own list), **absorption** (iPermit and Inspected clean up the failure after it happens),
**static content** (free city and trade checklists, same list for every job).

**Differentiate on the VERB, not the pain.** Inspected *replaces* the trip. InspectPilot *reports* the
failure. iPermit *cleans up* the failure. **None of them predicts it.** "Avoid wasted inspector trips"
is taken vocabulary and is not differentiation.

**PermitFlow is the fast-follower risk.** Their Research Agent already claims to "Identify inspection
requirements with unmatched accuracy," their Scheduling Agent books with the AHJ, and pass/fail verdicts
flow back from every jurisdiction they touch. They have every input for this product and shipped none of
it - the entire `/inspections` page is throughput language ("90% reduction in workload," "5X faster"),
zero outcome language. Their logos are Lennar, Toll Brothers, NVR. **Differentiate on the segment they
will not serve at a $54M-Series-B price point, not on the feature.**

**UpCodes is the other clock.** 800k AEC users, shipped AI-native Plan Review 2026-06-03 against "11
million locally adopted building codes." Design stage only today. If they extend from drawings to field
evidence, this is dead by feature release.

**The unanswered buyer question, and it is the real weakness.** "The contractor pays to avoid a $50-150
re-inspection fee" is thin against free city PDFs. The working precedent in this industry is
**IBHS FORTIFIED**: photo evidence during construction, third-party review, a designation that carries
insurance money - and it works because **someone other than the contractor pays for the attestation**.
Nobody sells attested pass rate to insurers, lenders, or GCs hiring subs either. BuildZoom is the proof:
400M permits, a public contractor score, **and no inspection outcome on the profile**.

### 3. THE TRANSITION MATRIX REPLICATES. 5 of 5 testable jurisdictions.

Computed locally from full CSV exports, sorting each permit's inspections by date and counting
consecutive pairs.

| Jurisdiction | P(wasted \| prev wasted) | P(wasted \| prev pass) | Lift |
|---|---|---|---|
| **Cleveland OH** (building permits) | 36.9% (14,966/40,577) | 3.5% (7,705/222,541) | **10.65x** |
| LA (prior work) | 44.3% | 7.9% | 5.6x |
| **Marin CA** | 32.1% (5,185/16,146) | 6.1% (6,630/108,275) | **5.24x** |
| **Montgomery MD** 2023+ (CANCELLED proxy) | 25.4% (12,038/47,388) | 7.1% (16,764/237,130) | **3.59x** |
| **Corona CA** (strict NOT READY) | 26.1% (3,216/12,327) | 8.1% (5,563/68,784) | **3.23x** |
| **College Station TX** (proxy) | 17.6% (6,232/35,490) | 6.1% (19,507/317,970) | **2.86x** |
| Calgary | - | - | 1.08x |

**Calgary is the outlier AND the one jurisdiction with no not-ready bucket** - consistent with "the
effect is invisible where the code does not exist," not with "the effect is not real." The effect
survives even on a crude CANCELLED-only proxy in Montgomery, which has no not-ready code at all.

### 4. THE NOT-READY BUCKET: real in 4 of 9, not universal

| Jurisdiction | Rows | Not-ready-like share |
|---|---|---|
| LA (prior work) | 8.29M | 13.6% |
| **Corona CA** `9cmf-hjdi` | 131,415 | **9.70%** (`NOT READY` 12,696 + `NOT READY WITH FEE` 45) |
| **Cleveland OH** (building only) | 475,017 | **9.64%** - and it is literally coded **`Useless Trip/ Work Not Ready`** |
| **Marin CA** `yfwm-p533` | 183,398 | **7.70%** |
| **Montgomery MD** `hyxh-ndxj` | 7,660,621 | **NONE.** PASSED/FAILED/WAIVED/CANCELLED/blank only |
| **San Francisco** `vckc-dh2h` | 703,230 | **NONE.** Literally three values: PASSED 74.6%, blank 15.8%, FAILED 9.6% |
| College Station TX `6npd-u87q` | 513,685 | ~0.8% |
| Norfolk VA `bnrb-u445` | 576,191 | 0.41% - but separately codes **`Wrong Inspection Type Requested`** (452) |
| Framingham MA `ipef-acke` | 83,441 | ~0.9% |

A city coded a result value **"Useless Trip"**. The concept is real enough to have a name in the
incumbent vocabulary. But **do not say "one in four" as a universal** - it holds in about four of nine.

Socrata catalog swept in full (439 datasets across 5 queries): 61 inspection datasets with a result
column across 29 domains; filtered to building/permit, **~10-12 US jurisdictions, not 6**. Framingham MA
and Norfolk VA are additions. Cleveland never appears because it is ArcGIS-hosted, not Socrata. ArcGIS
Online swept too (404 items, 153 candidate services) - nearly all are inspection zones, Survey123 forms
or monthly aggregates, not outcome records.

### 5. NOBODY SELLS INSPECTION-LEVEL OUTCOMES. Verified against nine vendors.

**Shovels.ai** - pulled the live OpenAPI spec (`api.shovels.ai/spec/v2/openapi.production.yaml`,
250,291 bytes). **All 33 paths, no `/inspections` endpoint.** `api.shovels.ai/v2/inspections/search`
404s. "inspect" appears 63 times and **every occurrence is one of four derived fields**:
`inspection_pass_rate`, `avg_inspection_pass_rate`, `permit_min_inspection_pr`,
`contractor_min_inspection_pr`. The bulk EDL tier has four tables (Permits, Contractors, Employees,
Residents) - **no inspections table**. Their own dictionary marks both fields **"Created by Shovels."**
They compute a ratio from per-inspection granularity upstream and sell only the ratio.
Pricing: Free 500 credits; **Basic $599/mo / 25,000 credits; Pro $999/mo / 50,000**; "a credit is one
record retrieved." Their own coverage numbers contradict each other ("~2,000 jurisdictions" in docs vs
"2,770+" on solutions).
**Cheapest test available, free:** `GET /meta/coverage` returns per-field fill rates on a free key.
Measure inspection-field coverage yourself before paying anyone.

| Vendor | Evidence | Verdict |
|---|---|---|
| Construction Monitor | Machine-readable API dictionary (79KB). **`grep -i inspect` = ZERO.** 13 endpoints, 61 fields | permit-level only |
| CoreLogic / **Cotality** (rebranded 2025-03-24) | Field list published, `grep -i inspect` = 0. States verbatim **"Includes building permit data sourced from BuildZoom"** | permit-level only |
| HouseCanary | Fetched the full 3.5MB OpenAPI spec. **`grep -i permit` = exactly one hit, the word "permitted" in rate-limit prose** | **no permit data at all** |
| ATTOM | `/property/buildingpermits` exists; **no inspection endpoint** in the resource list | permit-level only |
| BuildZoom / Gryd | Public data dictionary, full field list, **zero inspection fields**. 380M+ permits | permit-level only |
| BuildFax / Verisk | Acquired Oct 2019. 2025 ProMetrix sheet sells permit history explicitly to **"reduce your dependence on surveys"** - the industry's alternative to inspection data is sending a human | permit-level only |
| Dodge | `grep -i inspect` = 0. Pre-construction bid leads | not inspection data |
| Zonda | **`grep -i permit` = 0.** The two "inspect" hits are New Relic JavaScript | no permit data |
| PermitData.net | Publishes `record_type: inspection` - **but no result field**, and verifiable coverage is a Florida 90-day demo | partial |

**Market structure note: this oligopoly resells itself.** Cotality sources permits from BuildZoom.
Construction Monitor sits under Hubexo. BuildFax was absorbed into Verisk. Several "different vendors"
are partly the same pipe, **and none go one level below issuance.**

**The honest read on the gap:** two companies (Shovels, PermitData) solved the ingestion problem and
both chose to expose permit-level output. That is either a moat you would have to rebuild, or nine
sophisticated companies' shared verdict on what buyers pay for. **A judge will ask exactly that. Have
the answer before the room does.**

---

**2026-09-06.** The only candidate in this project whose incumbent absence was **verified from primary
sources** rather than inferred, and the only one supported by **original data analysis** rather than
citation. It is also the only one that answers the 0-for-26 problem, because the asset is a model,
not labor.

## ⚠⚠ COMPUTED CORRECTION 2026-09-06. The product changes shape. Read this first.

### The Calgary deficiency numbers I published were MISCOUNTED

**The row grain is a deficiency LINE, not an inspection.** 2,526,565 rows resolve to **1,105,444
distinct inspections**, of which **328,878 failed (29.7%)**, spread over 878,777 failure lines.
**The counts I quoted ("soil bearing report 16,744 times") were ALL-ROW counts, contaminated with
passes and boilerplate.** Four of the top ten strings are passes or admin text: **"No infractions
noted" (16,421) is a PASS.**

### Concentration collapses, and the strong-form fallback is DEAD

Restricted to actual failures: **571,606 distinct deficiency strings across 878,777 failure lines**,
about one unique string per 1.5 failures.

| Top N reasons | Share of failures |
|---|---|
| 5 | **8.5%** |
| **10** | **10.8%** |
| 20 | 12.9% |
| 100 | 18.2% |
| **5,000** | **30.3%** |

**And the #1 and #2 entries, 6.4% of all failure mass, are "Correct items and RECALL inspection" and
"Correct and RECALL inspection." Procedural, zero content, unputtable on a checklist.**

**"The top 10 things that fail in your city" misses 89% of failures. There is no short list.**
(Normalizing to code clause does not rescue it: top 30 clauses = 7.0%.)

### ⚠ THE 43-49% INSPECTOR FIGURES COULD NOT BE REPRODUCED, TWICE

Two independent agents recomputed Marin and **neither saw anything close.** Pooled across all
inspection types, high-volume inspectors: **DAA 13.2%, ELP 12.0%, PDC 8.1% ... MGW 3.2%, dlee2 0.5%,
gganeva 0.3%.** Restricted to BUILDING FINAL at n>=100, a separate agent got **H&P 25.2% down to
MCW 2.1%, with GPG at 4.1%** - against the original claim of **GPG at 43.1%.** Same inspector, an
order of magnitude apart.
**Treat 43-49% as WRONG until reproduced. The ratio spread is real (roughly 4x to 12x depending on
filter); the LEVELS were not.** This was load-bearing and it must not go in a deck.

### What actually survives, ranked, all computed

**1. Readiness, not compliance. The most robust finding.**
LA, 8,287,570 real site-visit attempts (excluding scheduled/cancelled/admin). 2025: **Not Ready
11.9%, No Access 1.7%, Corrections Issued 14.0%.** **Flat for twelve years** (not-ready 11.9-14.7%).
That is **~1.27M wasted inspections in LADBS alone.** Replicates in Marin at **9.7%**. Calgary has no
comparable bucket, folding readiness into "Not Acceptable."
Plus Calgary's **DOCUMENTS checklist touches 14.5% of failed inspections** - paperwork not on site.
**More than a quarter of inspections go wrong, and roughly half of that is logistics, not construction.**

**2. Repeat-offender detection. This BEATS the inspector effect.**
LA 2024 transition matrix, 250,000 inspections in permit order:

| Prior outcome | P(next = corrections) | P(next = wasted trip) |
|---|---|---|
| Pass | 10.1% | **7.9%** |
| Corrections | 24.6% | 23.1% |
| Wasted trip | 7.2% | **44.3%** |

**A wasted trip predicts another at 44.3% versus 7.9% after a pass. A 5.6x lift, larger than the
inspector effect the whole concept was built on.** Dispersion ratio 2.06-2.25 against binomial, so
failures genuinely cluster. **The worst decile of permits holds 43.3% of all corrections; 36.6% of
permits never get one.**
**Calgary does NOT replicate this** (1.08x), plausibly because its mandatory "correct and RECALL"
process makes the next visit a targeted re-check rather than a fresh draw. **Jurisdiction-dependent.**

**3. Inspection type as base rate. Free and universal.**
Calgary: **Gas Final 60.8%, Gas Rough 56.0%, FP Rough 38.3%, Final 32.9%, Framing 28.8% ...
Foundation 9.9%. A 6.1x spread with no personnel data at all.** LA corrections span 29.9% to 3.1%.
**Combined prior-state x next-type gives a 5.8x spread from two variables every jurisdiction
publishes** (worst cell: prior wasted, next Final, n=5,219, **67.8%**).

**Dead signals:** seasonality (0.8pp across the year), day of week (1.7pp), sub-jurisdiction geography
(1.24-1.54x).

### The product this becomes

**A readiness and scheduling product, not a code-compliance product.**

> "One in four inspections goes wrong, and half of those never needed to. If your last inspection was
> a wasted trip, your next has a 44% chance of being another. We tell you the day before whether you
> are actually ready: work complete, documents on site, right inspection called, for the specific type
> you booked."

**It sells on rescheduling delay, not code expertise - and that is an easier buyer conversation**,
because you no longer have to convince a contractor you know the code better than he does.

**Honest risks.** It is **thinner than the inspector story**: it promises *whether*, not *why*.
**Shovels already sells contractor pass rates**, so if differentiation collapses to contractor history
you are late. **No single jurisdiction supports the whole product** - LA has wasted trips and
stickiness but no deficiency text; Calgary has deficiency text but neither. Defensibility is **months,
not years**, with no proprietary input.

**And the real scarcity is not inspector identity.** The Socrata catalog returns 266 hits for
"building inspection," but **essentially only Calgary and LA publish per-inspection outcomes at scale.**
**Inspection outcome data of ANY kind is the scarce asset.**

### Do these two things before building anything

1. **Resolve the Marin inspector discrepancy.** It is load-bearing and two agents failed to reproduce it.
2. **Check whether "wasted trip" exists as a category in the 3-5 launch jurisdictions.** It exists in
   LA and Marin, not Calgary. **If it is an LA-schema artifact rather than a real operational category,
   signal 2 collapses and you are left with inspection-type base rates, which genuinely is a weekend of
   work.**

## ⚠ DATA FOUNDATION CORRECTED 2026-09-06. It is ~1000x narrower than claimed.

**The claim "every city publishes a record of every inspection it has ever done, who inspected, what
type, pass or fail, and why it failed, and nobody reads these" is SUBSTANTIALLY OVERSTATED.** Four of
its five assertions are false. Corrected version:

> About a dozen US jurisdictions publish inspection-level records with outcomes as open data, out of
> 10,000+ permit jurisdictions. Roughly half name the individual inspector. Most cover 2013 onward,
> not all history, and most omit the failure reason. **Shovels.ai has already normalized inspection
> pass rates across 2,770 jurisdictions and sells them from $599/month**, but only in aggregate: no
> raw rows, no inspector identity.

**Two of the four jurisdictions the thesis was built on do not contain the key field.**

| | Rows (verified) | Inspector? | Failure reason? | Coverage |
|---|---|---|---|---|
| Marin County CA `yfwm-p533` | 183,398 | **YES**, 121 codes | No | 2014-01-02 on |
| LA City `9w5z-rg2h` | 11,691,152 | **NO** | **NO** | 2013-01-01 on |
| Calgary `8ced-xbvn` | 2,526,565 | **NO** | **YES** (free text) | 1999 on |
| Mecklenburg NC | not open data | n/a | n/a | n/a |

**The two datasets carrying 98.6% of the row volume have no inspector column.** The moat rested
entirely on Marin, which is 1.3% of the corpus.

### But the original analysis also UNDERCOUNTED, and that is the good news

Confirmed live US jurisdictions publishing inspection outcomes **with individual inspector identity**:

| Jurisdiction | Rows | Inspector form | Note |
|---|---|---|---|
| **Montgomery County MD** `hyxh-ndxj` | **7,660,621** | `inspby`, 837 initials | **42x Marin.** Dates dirty (1950-2048) |
| **Cleveland OH** (ArcGIS) | 1,093,159 | **full names** | 2015 on |
| **San Francisco** `vckc-dh2h` | 703,230 | **full names**, 78 distinct | **Has `inspector_district`**, so the effect can be CONTROLLED for geography. Marin cannot |
| College Station TX `6npd-u87q` | 513,685 | `inspector` | 2010 on |
| Marin County CA | 183,398 | initials | 2014 on |
| Corona CA `9cmf-hjdi` | 131,415 | `inspector` | 2017 on |

Excluded: **San Diego County and Kansas City resolve only on non-production STAGING Socrata domains**
whose public equivalents 404. Building on those is a dependency on someone's misconfiguration.
**Framingham MA is DEAD**, stopped 2020-06-29 and was never removed, which is the real retention risk.

**Honest coverage: 6 live jurisdictions against 10,000+ US permit jurisdictions, roughly 0.07%.**
Combined population 3-4 million. **None of the top ten metros.** No NYC, Chicago, Boston, Austin,
Seattle, Denver, Dallas, Phoenix, Philadelphia or Houston.

### The combination the pitch assumed does not exist anywhere

**No US jurisdiction confirmed has BOTH inspector identity AND failure reason.** Calgary has the reason
and no inspector. The six US ones have the inspector and only a result code. **"Why it failed, and
which inspector" is not available in open data anywhere.**

### The one claim that holds is UNDERSTATED, and it is now computed

Marin, BUILDING FINAL, inspectors with n>=100, fail rate = NOTAPPROV / total:

**H&P 25.2% · ELP 22.6% · DAA 21.7% (n=2,217) ... MGW 3.0% (n=2,176) · MCW 2.1%**

**Full spread 2.1% to 25.2% = 12x. Comparing the two highest-volume inspectors, 7.2x.** The claimed
3-6x was conservative.
**Diligence caveat that will be raised:** this is uncontrolled for district, project size and
contractor mix. Marin has no district field. **SF does, which makes SF the dataset to defend the
number on.**

### "Nobody reads these" is flatly false

**Shovels.ai** covers 2,770+ jurisdictions, all 50 states, ~85% of US population, 178M permits.
It exposes `inspection_pass_rate` on permits and `avg_inspection_pass_rate` on contractors, from
**$599/month**. It does **not** expose raw inspection records, failure reasons, or any inspector
identity, and has no inspections resource group in its API.
**Build-vs-buy answer: buy Shovels for national pass-rate baseline, build the inspector layer only
where it exists.**

### Getting the other 9,994 jurisdictions

Possible, not cheap, and not at scale by a small team. Most municipalities run Accela, Tyler EnerGov,
Cityworks PLL, CentralSquare or eTRAKiT, so one scraper amortizes across many cities. Records requests
work for the database table, not for documents, though Pennsylvania's UCC explicitly permits
withholding inspection reports. **The inspector field EXISTS in the underlying software (Accela's
`inspector`, EnerGov's `inspectorfirstname`), so when it is missing from a public dataset that was a
PUBLISHING decision, not a data limitation** - which means records requests could plausibly recover it
in far more places than publish it, one negotiation at a time. Estimate days to weeks per jurisdiction.

**Lower-bound caveat:** SF did not appear in the Socrata federated sweep despite being on Socrata, so
every count above is a floor. The true number is probably somewhat higher than 6-8, but there is no
evidence it approaches hundreds.

### What this does to the pitch

**The honest framing is a Bay Area plus DC-suburbs plus Cleveland wedge with a striking finding, not a
national data play.** Saying "every city" in front of anyone who has worked in govtech loses the room,
and the genuinely good finding underneath goes down with it.

**Open question that decides the geography, answerable only by filing a few test records requests:**
is inspector identity legally withheld as personnel information, or merely not published? No survey or
caselaw was found either way.

## The verification that unblocked it

The load-bearing claim through this whole project was "the funded permit players sell ISSUANCE, not
inspection PASS," and it was flagged repeatedly as inference. **It is now VERIFIED, from the
companies' own product pages.**

- **PermitFlow** ($54M Series B led by Accel, 2025-12-02, ~$500M valuation, ~$91M total). Its release
  says "AI Agents for Inspections," which is exactly why this needed checking. Its `/inspections` page
  names four agents: **Research** (identify requirements), **Scheduling** (handle bookings),
  **AHJ Tracking**, **Closeout** (compile results). **Zero occurrences of pass rate, first-time pass,
  readiness checklist, failure prevention, re-inspection, correction notice, or inspector-specific
  guidance.** "Inspections" there means **logistics**: booking the appointment and filing the result.
  It never touches whether the work will pass.
- **GreenLite** ($78M total; $28.5M Series A Craft Sep 2024, $49.5M Series B Insight Sep 2025) sells
  **plan review of drawings before construction.** Different phase entirely.
- **Pulley** ($4.4M seed) is permit application and entitlement. Issuance.
- **Symbium, Camino, OpenCounter** all sell to the **municipality**. Wrong customer.
- **Shovels.ai** ($6.5-8.3M) is the real edge case: its API does expose contractor pass-rate metrics
  across 178M permits and 2,770+ jurisdictions. But it sells **data to software companies**, B2B2C.
  **It is a potential supplier, not a competitor.** It sells the raw signal; nobody sells the outcome.

**Nobody sells inspection-failure reduction, re-inspection avoidance, or per-inspector failure history
to contractors.**

## The failure rate, computed from municipal open data, not cited

Search budget was exhausted, so the agent pulled the raw datasets and computed these directly.

| Jurisdiction | Dataset | Result |
|---|---|---|
| **Marin County CA** | Socrata `yfwm-p533`, 183,375 inspections | **18.68% repeat visits caused by the contractor (2024)**, 16.64% (2025) |
| **LA City (LADBS)** | `9w5z-rg2h`, 6.81M true outcomes | **Only 43.6% pass on first look.** 31.1% produce NO progress: Corrections 13.5%, **Not Ready 15.2%**, No Access 2.4% |
| **Calgary** | `8ced-xbvn`, 2.53M inspections | "Not Acceptable" **34.8%** |
| **Mecklenburg County NC** | Re-inspection fee ordinance | Uses **20% as the break-even failure rate**, charges **$90 per failed inspection**, and **PAYS a $90 credit per inspection saved below 20%** |

**Four independent jurisdictions converge on 17-35% of inspections requiring a repeat visit. And a
government has already priced a saved inspection at $90.**

## The proprietary signal, and it is the whole business

Marin publishes the **inspector name** on every record. Same county, same code, same two years,
**controlling for inspection type**:

| Inspection type | Worst inspector | Best inspector |
|---|---|---|
| BUILDING FINAL | GPG **43.1%** | MGW **11.9%** |
| FRAMING | GPG **48.0%** | MGW **10.6%** |
| ROUGH ELEC | GPG **33.0%** | RLB **10.9%** |
| ROUGH PLBG | GPG **48.7%** | RLB **7.5%** |

**The ordering is stable across all four types.** GPG worst every time, RLB/MGW best every time. That
is a persistent inspector effect, not a workload-mix artifact. **Who shows up changes your odds by
3 to 6x, it is knowable in advance from free public data, and nobody packages it.**

## And most failures are paperwork, not workmanship

Calgary's top deficiency reasons: soil bearing report required prior to frame inspection (16,744),
real property report required by final (10,523), concrete verification required by framing (10,091),
RPR required by final (9,978). Plus LA's **15.2% "Not Ready"**, where the inspector drove out for
nothing.

**That share is fully preventable without touching the physical work**, which is exactly the
automatable wedge and exactly why an unlicensed founder can serve it.

## The concept

**Customer:** residential and light-commercial GCs, electricians, plumbers and HVAC subs pulling
20-200 permits a year. **This is PipeLine's exact customer**, the one that won the 37th's $10,000.

**Delivered:** a per-permit, **per-inspector** readiness pass. What this specific inspector fails,
which documents must be physically on site at this milestone, and a go/no-go on calling the
inspection at all.

**Priced** per permit or per avoided re-inspection. **$90 is a government-set precedent for the value
of one saved inspection.**

**What it costs today:** $94-$225 in fees (Houston $127.56 all-in, NYC DOB $225, Wake County $150,
Goochland VA $100, Mecklenburg $90) **plus the far larger cost of idle follow-on trades and schedule
slip.**

**Verification: same day.** The inspector passes you or does not.

## The product mechanics

**Input.** Permit number, jurisdiction, inspection type, scheduled date. Read from the permit portal
or entered in ten seconds.

**The engine.** Ingest that jurisdiction's public inspection history once. It yields three things no
contractor has: **per-inspector fail rates by inspection type** (the 3-6x effect), **the actual
repeating deficiency reasons** (Calgary's "soil bearing report req'd prior to frame inspection"
appears 16,744 times), and **assignment patterns** so we can predict who is likely to show up.

**Output, BEFORE the inspection is called.** A readiness check: the likely inspector and their fail
rate for this exact inspection type, that person's top repeating deficiency reasons, a checklist of
the documents that must be physically on site, and a **go / no-go recommendation.**

**The wedge that needs no code expertise: the "not ready" case.** 15.2% of LADBS inspections are the
inspector driving out for nothing. Preventing that requires only "is the work actually finished and
are the papers here," which an unlicensed founder can absolutely determine. That is the beachhead.

**The feedback loop is the moat.** After every inspection we record what happened. It improves the
model AND becomes the proof of value: "you passed 9 of 10 this quarter, up from 6 of 10."

**Known open question:** how reliably can the assigned inspector be predicted before the visit?
Marin publishes the inspector on historical records, which is how the effect was measured, but
assignment prediction is an inference from route and geography patterns. **Test this early; the
per-inspector pitch weakens badly if the inspector is unknowable in advance.**

## Why this one answers the 0-for-26 problem

Every other candidate in this project is labor priced per unit delivered, which is 0-for-26 in front
of these judges. **This is not.** The asset is an accumulated per-inspector, per-jurisdiction failure
model that compounds with every outcome observed and is invisible to anyone who has not done the
aggregation. That is a data product with a workflow position, which is precisely the shape that wins.

**Honest limit on the moat:** the raw inputs are public, and **Shovels already sells derived pass
rates**. So the defensibility is the accumulated per-inspector model plus the workflow position, not
data access. Say that before a judge finds it.

**Liability is deliberately NOT transferred** - doing so would require licensure Veer does not have.
That caps the price and keeps the business legal for an unlicensed founder. It is a real constraint
and a fair trade.

**Margin verdict: survives.** Sold against a $127-$225 fee plus schedule cost, the buyer is paying for
a guaranteed outcome, not per document processed. It is not a document-processing repricing target,
and document processing is where the compression already happened (a Philippine BPO FTE at ~$6.13/hr
runs $0.15-0.31 per document; Veryfi charges $0.16/invoice).

## The pitch framing that survived all six runs

**Do not say "600x cheaper than humans."** Say: **correctness became free to attempt and expensive to
guarantee, so sell the guarantee.** A failed inspection is expensive, same-day verifiable, and caused
by a knowable, repeating set of reasons. That is why the price holds here and not in per-document work.

## What is NOT verified

Three parallel streams died on the usage limit, so the rest of the re-work sweep is thin. Weakly
evidenced and not to be pitched without verification: manufacturing 8D/SCAR corrective action (passes
the "being wrong is expensive" test, cost anchors unverified, and it is unconfirmed that nobody sells
the finished document), failed restaurant health inspections, warranty callbacks (XOi and Aquant sit
close), subcontractor-side submittal prep, retail vendor compliance chargebacks. **Chargeback
representment is crowded and should not be pursued** (Chargeflow, Justt, Chargebacks911, Signifyd,
Riskified already sell it done-for-you, priced per win).

## Next physical action

Call a contractor who pulls 20+ permits a year and ask two questions: **what did you fail on last
time, and what did it cost you in days.** If the answer is "we rarely fail," it dies on the spot.
