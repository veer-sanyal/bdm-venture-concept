# What funded companies have in common, and how that should steer the idea loop

Research note, 2026-09-25. **Desk research only; nothing here is customer validation.** Funded is not the same as working: these are investor bets, most less than a year old, and the breakout sample is survivorship-biased.

Inputs, all saved under [`2026-09-25-funded-patterns/`](2026-09-25-funded-patterns/):
- **YC, last four batches, every company:** W26 (199), X26 (193), S26 (230) and F26 (90 listed so far, batch in progress), 712 in total. Each was classified by an agent reading only its directory listing: customer, budget line, model, scope, regulated, physical, whether it sells to AI builders. Rows are in `data/class-*.csv`; summaries in `agents/classifiers.md`. The source is the yc-oss mirror of the YC directory, updated 2026-09-24.
- **Non-YC VC, seed to Series B, Jan–Sep 2026:** 34 companies with top-tier leads, plus 2026 funding data and the firms' stated theses (`agents/vc-rounds.md`).
- **AI breakouts, 2022–2026:** 25 companies and what each looked like at the start, plus the ones that got absorbed (`agents/breakouts.md`).
- **Our own ledger:** `scores.csv`, which holds 10 YC controls and 4 of our candidates.

## The answer

1. **Funded AI companies are bought out of a payroll budget, not a software budget.** Of the 385 YC companies that sell AI applications to customers (excluding infrastructure, hardware and AI-for-AI), 63% take over work people are paid to do. So do 24 of the 34 VC rounds. Sequoia's version: "for every dollar spent on software, six are spent on services."
2. **That is also the one place we lose to the YC controls.** On need, value and risk our candidates match the controls: 3.75 vs 3.77, 2.35 vs 2.33, 2.05 vs 1.98. On market they score **2.05 against 2.70**. Judges size ours as narrow fees per unit ($2 a dispute, about $1,000 a study) and land at $50–150M. They size the controls against a labor pool or a proven spend category. Closing that gap is the most useful change the loop can make.
3. **The typical shape is narrow at the start, with a platform ambition.** Half of YC companies do one workflow for one kind of customer. With enterprises the pattern is a narrow workflow (66 of 119); with small businesses it is "the operating system for one trade" (34 of 65). The breakouts started with a task that a well-paid professional does every day, then sold the second and third workflow to the same buyer.
4. **The crowd sits in AI serving AI, coding agents, and the AI-native service categories investors have named.** 18% of YC sells to AI builders. Insurance, legal, accounting firms, clinic admin and voice answering agents each hold several near-identical funded companies. Our scope's second category, AI-native services, sits inside that crowd.
5. **Some areas are thin in YC 2026, and each is thin for a reason.** Education, government back office, tax, payroll/HR/benefits, agriculture operations, payer-side healthcare and property operations are the thin ones. Thin can mean open, or it can mean a sales cycle nobody wants.
6. **Absorption kills products that the next model release or the customer's existing platform can ship as a feature.** Survivors own a workflow step, a system-of-record integration, a liability or accuracy guarantee, or a feedback-data loop.

## The patterns, with evidence

### P1. The budget is labor

| Source | Labor budget | Software budget | New spend |
|---|---|---|---|
| YC app layer, 385 companies | 243 (63%) | 55 (14%) | 68 (18%) |
| YC all 712 | 299 (42%) | 141 (20%) | 206 (29%) |
| VC rounds, 34 | 24 | — | — |
| Breakouts, 25 | ~12 (vertical and agent companies) | coding and prosumer tools | consumer |

The investor theses say the same thing in their own words:
- Bessemer: "Vertical AI isn't competing for IT budgets; it's competing for labor budgets."
- Sequoia: "A copilot sells the tool. An autopilot sells the work."
- Redpoint: "AI becomes the junior accountant."

**For the loop:** a candidate should name whose pay, or which outside firm's fee, it takes. That is also how its market gets sized.

### P2. They sell the work, mostly packaged as software

Only 76 of the 385 YC app-layer companies (20%) and 8 of 34 VC rounds sell finished work as an AI-native service, a forward-deployed team or a roll-up. The rest take over the labor but sell it as software. Outcome pricing is thesis language: pricing is unstated for about 98% of YC listings, and only 1 of the 34 VC rounds (Arrakis) verifiably ties fees to results.

**For the loop:** services are not required to fit the pattern. The labor budget is what matters, and a software product can take it.

### P3. Where the crowd is

- **AI serving AI:** 108 YC companies are AI infrastructure, and 125 (18%) sell mainly to AI builders, rising to about 22% in S26. Agent sandboxes, inference clouds, evals, training data, token compression and coding-agent tooling each have three or more funded near-duplicates in a single batch.
- **Categories investors call decided:** coding, legal, medical scribing and customer support (Elad Gil; new money there goes to the leaders at growth stage). Legal-tech funding in 2026 is running below 2025, and Harvey and Legora are buying startups.
- **Named AI-native service categories:**
  - insurance: 24 YC companies, including 7 in F26 alone, 4 of which replace a broker or TPA
  - accounting: three AI accounting firms in S26 alone, plus Basis ($1.15B) and Accrual
  - clinic admin and prior authorization: 7 in W26
  - voice agents that answer calls for small businesses: 27 YC companies mention calls, phones or voice in their vertical or job (a keyword count)
- **Recurring YC one-liners:** "company brain" (four in X26), "AI OS for [trade]", "Cursor/Legora for X".

### P4. Where YC 2026 is thin

The counts are over 712 companies, matched on vertical and job.

| Area | YC count | What is there | Why it may be thin |
|---|---|---|---|
| Education | 4 | A K-12 curriculum tool and three consumer learning apps | Long school sales cycles and budget politics; consumer edtech retention is weak |
| Government back office | ~7 | FOIA, permitting | The same sales-cycle problem; YC's Spring ask says a founder should have done the job |
| Tax | 4 | Two AI accounting firms that also file taxes, a tax API, a consumer agent | Preparer liability (PTIN, credentials); incumbents Intuit and H&R Block |
| Payroll, HR, benefits operations | ~8 | Mostly recruiting | Incumbents (ADP, Rippling, Gusto) own the data and the channel |
| Agriculture | 6 | Five are hardware or bio | Fragmented buyers, seasonal cash |
| Payer-side healthcare and claims | ~13 claims-related, mostly provider-side | Workers' comp, P&C claims | Payers buy slowly and build in-house |
| Property operations | ~9 | Mostly construction robots | Legacy platforms (Yardi, AppFolio, Buildium) own the data |

Thin plus a known reason is not an opening. Thin plus a reason that no longer holds is one: a model capability that just arrived, or a buyer the incumbents underserve. Elad Gil's list of still-open application categories (accounting, compliance, financial tools, sales, security) partly contradicts the YC counts. Accounting is thin as software sold to firms but crowded as AI-native firms.

### P5. Customer size sets the shape

| Customer | Narrow workflow | Vertical suite | Horizontal | Platform |
|---|---|---|---|---|
| Enterprise (119) | 66 | 15 | 31 | 7 |
| SMB (65) | 26 | 34 | 3 | 2 |

Enterprises buy one workflow. Small businesses buy "run my shop" (VC examples: Probook for HVAC and plumbing, Avoca for home services, Agave for construction accounting, Pie for salons). For two founders without an industry network, the SMB-suite shape has a reachable buyer but a wide product. The enterprise-narrow shape has a small product but a buyer who is hard to reach.

### P6. The physical economy is rising, and its software is in scope

The physical share of YC rose from 17% in W26 and X26 to 31–32% in S26 and F26. Physical-AI venture reached $47.4B in H1 2026, and 8 of the 34 VC rounds serve "Main Street" trades, construction, industrial firms and property. The hardware is outside the founder scope. The operations software around physical work is inside it: dispatch, quoting, back office, compliance paperwork. Accel's line: "teaching AI to operate the software the world already runs on."

### P7. How the breakouts started

- **The wedge:** one document type, one well-paid professional, a task done daily (about 12 of 25: Harvey, EvenUp, Abridge, Hebbia, Rilla).
- **The first market looked small, unglamorous or already won:** about 17 of 25 (plaintiff personal-injury firms, HVAC sales, faxed referrals).
- **Timing:** each launched within about 6 months of a model capability it depended on (long context, tool calling, real-time voice, agentic coding).
- **Founder edge:** "the founder is the user" or "the founder can reach the buyer", about 16 of 25. Credentials were not the common factor. Founders without it used one design-partner customer or switched markets fast.
- **Expansion:** the second and third workflow went to the same buyer. Almost every B2B breakout did this.
- **Market story:** "the labor is huge" for vertical and agent companies; user count for coding and consumer.
- **Consumer path:** a viral demo or open-source release, then a $10–25 monthly card subscription, then a move up-market.

### P8. What got absorbed

- AI writing (Jasper).
- Chat-with-PDF apps and generic note-takers.
- General chatbots (Character.AI, Inflection, Adept).
- Standalone image generators, now 3 on a16z's top-100 list.
- Per-seat SaaS in general: the early-2026 sell-off erased about $2T of market value.
- Scribes, under pressure since Epic shipped its own AI charting in Feb 2026.

VCs said in March 2026 that they no longer want wrappers, generic horizontal tools without proprietary data, or CRM and project-management clones.

### P9. Our ledger against the controls

| | Need | Value | Market | Risk | Total |
|---|---|---|---|---|---|
| YC controls (10) | 3.77 | 2.33 | **2.70** | 1.98 | 10.78 |
| Our candidates (4) | 3.75 | 2.35 | **2.05** | 2.05 | 10.20 |

How the judges argued market size (from the saved judge reports):
- **Ours:**
  - Disputes: "about 15k a month at $2 each... about $55M in total."
  - Arc flash: "$500 to $1,500 each caps revenue near $40M to $100M."
  - LTC Medicaid: "15,000 facilities × 30 applications × $500."
- **The controls that scored higher:**
  - Grep (market 4): "Labor is the largest part of a $61B North American spend."
  - Sona8 (market 3): Celonis at $771M ARR and the consulting budget.
  - Papaya (market 3): Braintrust at $800M.

Our candidates were priced as small fees on a narrow task. The controls were read against a labor pool or a proven category spend. Caveats: 10 controls and 4 candidates, and one judge's total varies by about 0.67. This is a pattern, not a proof.

**The fix is P1 and P7, not going horizontal.** Size and price against the labor line the product takes over, and name the second and third job for the same buyer. A judge checks claims against sources, so an inflated labor claim will be caught. The claim has to be real.

## How this should steer the loop

Two of these need no METHOD change. Two do, and wait on Veer and Cole. Per AGENTS.md, nothing here is added to any agent's prompt until METHOD says so.

**1. Use a seed (allowed now; METHOD's generator prompt has a `[Seed, if any.]` slot).** One seed per round, identical for all three generators. A seed must stay abstract and must never name funded companies, because that invites clones (see item 3). Options, in order of recommendation:

- **Seed A, labor line (recommended next):**
  > Look for work that businesses now pay people or an outside firm to do, where AI can now do most of it and the pay behind that work is large. Say whose pay or which firm's fee it replaces.

  Why: it addresses P1 and P9 directly, and it is the one lever that moved control scores.
- **Seed B, thin but reachable:**
  > Look in industries that few AI startups are serving yet, and say why they have been left alone and what has changed.

  Why: it points at P4 without handing generators the list. A named list would converge three generators on the same few areas.
- **Seed C, founder as user:**
  > Look for work that the founders or people they can reach at Purdue do every week.

  Why: P7 (the founder was the user or could reach the buyer in about 16 of 25 breakouts). Tension: METHOD judges team fit separately, and a Purdue-shaped seed may shrink the market. Use it once, as a comparison round.

**2. Read judge output with the breakout tests (no METHOD change; this is how the orchestrator reads step 5).** When reading what each judge named as the killer, also note:
- **Next model:** would a generic chat app with the next model make it unnecessary?
- **Labor line:** is the replaced pay at least 10 times our price?
- **Frequency:** is it a daily or weekly task?
- **Capability timing:** what capability made it possible within the last 12 months?
- **Second workflow:** what second job can the product do for the same buyer?

These tests go into the write-up. They are not a gate.

**3. Proposed METHOD change: check candidates for clones of funded companies at the merge step.**
> After the archive check, run `python3 tools/yc_overlap.py <terms>` over the last four YC batches and do one web search for the candidate's one-liner. A candidate that nearly copies a funded company is reshaped or dropped before judging.

Reason: the judge prompt tells the judge to treat an almost-identical company as the team. A clone would borrow that company's traction and inflate its score, and the controls come from the same batches. The P3 crowd makes clones likely. Running `yc_overlap.py` on the current board already finds two neighbors (see below).

**4. Proposed METHOD change: the shaper names the budget line and the next workflows.** Append to the shaper prompt:
> For each company, name the budget it takes (whose pay or which outside firm's fee), how large that budget is, and the second and third jobs it can do for the same buyer.

Reason: P9. The paragraph then carries the real market argument into judging on the same terms the controls get from their own descriptions. Risk: it pushes the shaper toward labor-replacement ideas and away from new-spend and consumer ideas (29% of YC is new spend). Veer should decide whether that trade is wanted.

**Refresh.** F26 has 90 companies listed so far. Rerun the classification when the batch completes, and before any control draw that uses it.

## The current board against these patterns

- **Credit-dispute response for collectors (11.2, advances):**
  - Fits P1 (dispute-ops analyst labor) and the regulated, narrow enterprise shape.
  - Its market score of 2.2 is exactly the P9 gap: it is priced per dispute.
  - Neighbors: Zomma (YC S26), "the AI BPO for financial services", whose computer-use agents handle "KYC reviews, transaction alerts, and disputes." Audun (S26) is an AI-native debt collector, and Hickory, a banking-compliance control, is also in F26.
  - Next: size it against the analysts who work disputes today and name the next jobs for the same buyer (for example validation notices and other collection-compliance files). The customer calls STATE already lists still decide it.
- **Customs-broker entry line check (C1):**
  - Tarifflo (YC S26) sells AI customs filing to importers under their own filer codes, charges nothing to file, and earns from duty refunds. That is the importer-side neighbor of C1's broker-side position.
  - It confirms the category is funded. It does not show that a broker product is crowded.
- **Technician knowledge capture:** Pairio (YC X26) is a photo-to-manual lookup app for factory technicians. It is adjacent, not the same job. The two-hour scan in STATE still applies.
- **Chargeback defense:** fits P1 and P2 (a contingency, outcome-priced service). Still parked on the relationship objection until a supplier conversation happens.

## Source quality

- **Directory text:** the YC classifications read one listing paragraph each. Customer and budget are the least certain fields. Several listings are empty.
- **VC table:** 25 of 34 rows were opened directly; the rest come from snippets or aggregators. Press coverage over-represents a16z and exclusive stories.
- **Breakout figures:** many ARR figures are Sacra estimates, marked [S] in the agent report.
- **Our ledger:** 14 paragraphs in total. Treat P9 as a direction to test, not a measured effect.
