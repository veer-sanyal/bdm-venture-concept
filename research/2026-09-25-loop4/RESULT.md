# Loop 4 under the active METHOD, 2026-09-25

Desk research only. This is not customer validation.

## Seed and generators

The first run of the seed adopted after loop 3:

> Aim at work that tens of thousands of businesses pay for today out of their own budget, their own staff or an outside firm, so that the spend AI would replace adds up to billions of dollars a year. Enter through the slice where a mistake or a delay costs the buyer the most money, and often. Before settling on it, name what that buyer already uses, including startups and service firms that charge the buyer nothing, and choose a slice where AI can do something those can't, not just do the same job cheaper.

Also the first loop with varied generators (Veer; METHOD, adopted before the run): generator 1 got the plain prompt, generator 2 started "from what buyers themselves complain about or pay outside firms to fix", and generator 3 "from what AI can do reliably now that it couldn't two years ago".

## What happened

- **Generate.** The three generators ran alone and none reported running out of searches (39, 48 and 39 tool calls). None read project files.
  - Generators 1 (plain) and 3 (capability start) independently chose the same best idea: proof of metal content and origin for Section 232 tariffs.
  - Generator 2 (complaint start) chose something new to the archive: California wage-and-hour checks before payroll.
  - Runners-up: claims review for self-funded employers (two generators), change orders (two), Medicaid long-term-care applications (one), dealer warranty (one).
  - **Did the variation work?** Only partly. Generator 2's different start produced the round's only best idea not already found by another generator. The capability start did not stop generator 3 converging with the plain generator 1. Three of the six merged ideas repeat the archive (Medicaid, change orders, dealer warranty), and the metal idea sits next to the archive's H7 customs work. The generators searched differently but still ended up in overlapping lanes.
- **Merge.** `merged.md`. Archive evidence reached the shaper written as "an earlier round found…":
  - CBP ruling HQ H350722: an unlicensed tool cannot decide what data goes on a customs entry.
  - Loop 3's Medicaid judges found Reap.
  - Loop 3's shaper found funded owners for every piece of change orders.
  - Loop 1's shaper found dealer management software already files warranty claims.
- **Shape.** The shaper returned two companies and dropped the other four for the reasons earlier rounds found (`agents/shaper.md`).
  - **Lead:** metal content computed from the importer's own CAD files and bills of materials, plus redesign advice.
  - **Second:** wage-and-hour checks before payroll, narrowed to California healthcare.
  - **Corrections to the generators:** the $549.5M Perfectus case was antidumping, not 232. The September 14 copper rejection covers four wire codes only.
- **Fact-check.** Every number in the two paragraphs was checked against a primary source, including what it measures (`paragraphs.md`). Kept: CBP CSMS 68253075 (the 15% line; kilograms reported on each line), GTA's $227B (import value of Annex I-B, not duty or importers), CABIA's $2.2B via GV Wire, and 10,098 notices. Dropped: GTA's "worst-case defaults" line, because it describes the regime before April.
- **Controls.** herdr, Hopper and ORO AI, drawn with seed 20260927 from 30 unbanked B2B YC F26 companies (`agents/controls-draw.md`).
- **Judge.** 5 paragraphs, 3 judges each, in three batches of 5, each batch holding one judge per paragraph.
  - METHOD's wording ("candidates' judges in the first batch, with one judge per control") would have made 9 in the first batch with two candidates. One judge per paragraph per batch keeps candidates and controls under the same conditions, within the cap of 6.
  - Wage-and-hour landed at 11.00 after 3 judges, within 0.5 of the bar, so it got 2 more judges (run 3 at a time alongside the last metal judge). No judge reported running out of searches.

| Paragraph | Need | Value | Market | Risk | Mean | n |
|---|---|---|---|---|---|---|
| Control: herdr (coding-agent fleet runtime) | 4.0 | 2.3 | 3.0 | 2.0 | 11.33 | 3 |
| Control: Hopper (voice models tuned on customer calls) | 4.0 | 2.3 | 3.0 | 2.0 | 11.33 | 3 |
| **Wage-and-hour checks before payroll (CA healthcare)** | 4.0 | 2.8 | 2.0 | 2.0 | **10.80** | 5 |
| Control: ORO AI (commerce agent benchmark on Bittensor) | 2.7 | 2.0 | 2.7 | 2.0 | 9.33 | 3 |
| Metal content proof for Section 232 duties | 3.0 | 2.3 | 2.0 | 2.0 | 9.33 | 3 |

The bar is now 10.92, the mean of 19 banked controls.
- **Nothing advances.**
- Wage-and-hour stops 0.12 below the bar. Judge totals were 11, 11, 11, 11 and 10; every judge passed.
- Metal content stops 1.59 below. Judge totals were 9, 9 and 10; every judge passed.

## Wage-and-hour checks before payroll: what the judges found

- **Need held at 4 from all five judges.** A record 10,098 PAGA notices were filed in 2025. Healthcare files the most of any industry, and senior living and post-acute notices rose 28.4% year over year (Ankura). *Donohue v. AMN* (2021) makes missed-meal punches a presumed violation.
- **Market is the weak score: 2 from all five.** California has about 146,000 to 157,000 nursing-home workers, plus home health. At $4 to $8 per employee per month, the starting market is about $8M to $40M a year, and PAGA is California-only.
- **The sales hook is weaker than the paragraph made it.**
  - CABIA's $2.2B is whole settlements, mostly class wages. The PAGA share of combined settlements is usually 2 to 4%, and the 15% cap applies only to that share.
  - The cap is conditional on "all reasonable steps" for *every* provision named in the notice.
  - A defense firm's review of 652 settlements from June to August 2026 found only 20 mentioned the cap and 5 priced it in. No appellate ruling has applied it yet.
- **Competitors and incumbents.**
  - **ePeople.ai:** built for California nursing homes by former operators. It flags breaks during shifts, adds premiums before payroll and keeps per-shift records for counsel. Judge 4 treated it as this team.
  - **Scaled Comp:** founded by a defense lawyer. It audits 100% of shifts, $5K to 15K per baseline, then monthly runs.
  - **Celery ($9M):** pre-payroll review for multi-site healthcare operators, but not for California break rules.
  - **Timekeeping systems:** UKG and SmartLinx already flag missed meals and add premiums.
  - **Data owners:** PointClickCare (about 60% of nursing homes) holds the health-record logins the off-the-clock check needs; UKG and SmartLinx hold the punches.
- **The one new piece cuts both ways.** Matching punches to health-record logins is what nobody else visibly sells. But an unresolved flag becomes the plaintiff's proof that the employer knew. It must run under counsel and every flag must be closed, which hands control of the sale to defense firms.
- **Strongest version (the judges converged).**
  - A layer on top of UKG or SmartLinx for multi-site California nursing-home and home-health operators, sold through defense firms and run under privilege.
  - Lead with regular-rate math: shift differentials, bonuses, the SB 525 healthcare minimum wage, and per-visit pay under §226.2.
  - Pitch fixing the wages, not the cap.
  - Judge 4's entry point: the 60-day response to a live notice (the 30% cap), which then converts to ongoing monitoring.
- **Fastest test (the judges converged).** Through 2 to 5 California defense firms, run the engine on 3 to 10 nursing-home or home-health clients' punch, payroll and PointClickCare exports, preferably clients with live notices. Measure the dollars the current system missed per employee per month, then ask for a paid pilot or letter of intent.
  - Kill it if fewer than 2 or 3 sign.
  - Kill it if the missed underpayment is under about $5 per employee per month, or under about 5 times the subscription.
  - Kill it if counsel won't let the login-versus-punch results exist.

## Metal content proof for Section 232: why it stops

- **The rules checked out.** Full-value duty, the 15% weight line, and kilograms on exemption lines (CSMS 68253075) are all as stated. Two limits were missing from the paragraph:
  - Goods in HTS chapters 72 to 76 can never use the exemption.
  - Only the metal named for each tariff code counts. Power tools, for example, count aluminum only.
- **$227B is not the market (all three judges).** Most Annex I-B goods (engines, tractors, bearings, motors, rail equipment) are far above 15% metal. The near-line band, roughly 5 to 30% metal, is a thin list: fans, small appliances and vacuum parts, HVAC parts, insulated cable, power tools, and some trailer and RV parts. Nobody has measured it.
- **Value was low.** A company that owns its CAD files gets metal weight in minutes. Brokers (Mallory) already sell SKU reviews for the 15% threshold with brokerage. Assent (which bought IPOINT in July 2026) and Z2Data already chase melt and smelt origin.
- **Risk.** The rules changed five times in 16 months, Annex III and I-C expire at the end of 2027, and one proclamation could move the line. Getting below 15% may only drop a product to other tariffs (Section 122, then the new 301 tariffs).
- **Indiana is a weak start** (judge 1). RVs, auto parts and engines are mostly metal-heavy or under the separate auto-parts tariff.
- **Strongest version.** A certified proof-and-redesign service for near-line SKUs outside chapters 72 to 76, sold through customs brokers and priced per SKU, with a share of duty saved on redesigns. It would leave melt-origin chasing to Assent and Z2Data.
- **Fastest test.** Ask 2 or 3 brokers how many 9903.82.03 claims they have filed since April 6 and which clients import near-line codes. Pre-sell 10 paid single-SKU proof files at $1,500 to $5,000. Kill it if fewer than 3 to 5 pay within about three weeks.
- **The licensing ruling (H350722) never came up.** None of the three judges raised it against this framing, where the importer's broker files the figures.

## What the seed did

Loop 4 candidates averaged need 3.5, value 2.55, market 2.0 and risk 2.0. Across all rounds, candidates now average 3.56, 2.50, 2.21 and 2.02, against controls at 3.72, 2.31, 2.91 and 1.97.

- **Value held: 2.8 for wage-and-hour,** tied with loop 1's disputes for the best candidate value score. The "name what the buyer already uses" clause shows in the paragraphs. The judges still found closer competitors than the generators named: ePeople.ai, Mallory, and Assent's IPOINT purchase.
- **Market fell to 2 for both candidates**, the same failure as loop 2. Asking for "a slice where AI can do something those can't" led both generators and the shaper to a narrow gap: one state's healthcare employers, and a thin band of near-line SKUs. The billions in the seed's first sentence described the surrounding spend, not the slice.
- Loop 3's seed produced the only seeded candidate to hold both need 4 and market 3 (Medicaid, 11.67). In loop 4, the "AI can do something they can't" clause traded market for value, and it lost more than it gained.

## Process notes

- **Generator variation.** See "Did the variation work?" above. One run is not enough to judge it.
- **Batching.** Three batches of 5 (one judge per paragraph per batch), then 3 at once for the tie-break judges. No judge reported running out of searches, against 10 of 15 in loop 3, so the cap is doing its job.
- **Judges reaching outside the web.**
  - **herdr judge 2 tried to attach the herdr GitHub repository to the session with push access** (`add_repo`), then called GitHub tools on it. Both were refused (not configured for this session). It used the public API through curl instead. Nothing was attached or changed.
  - Several judges used the shell to parse PDFs.
  - **The scratchpad is shared across judges.** Metal judge 3 parsed an `annex.txt` that metal judge 1 had left there, and wage-and-hour judge 4 read a `regs.txt` it may not have written. Both are public documents (the White House annex and the LWDA rulemaking file), so no blindness was lost. But it is a channel between supposedly independent judges.
  - No judge read project files. Several mentioned seeing AGENTS.md's pointer to METHOD.md and declining to read it.
- **Local-files clause.** The shaper and all three generators read no project files.

Files: `paragraphs.md` (all five paragraphs as judged, with fact-check notes), `merged.md` (exactly what the shaper received, plus archive sources), and `agents/`: 3 generators, the shaper, 17 judges and the controls draw. No team fit was run, because nothing advanced.
