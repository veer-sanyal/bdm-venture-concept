# Loop 2 under the active METHOD, 2026-09-25

Desk research only. This is not customer validation.

> **Caveat added after the round (see [contamination-audit.md](contamination-audit.md)).** 9 of 17 judges read METHOD.md before judging, including 4 of commissioning's 5. Judges who read it scored about a point higher. With clean judges only, commissioning is about 11.0 against a bar of about 10.9-11.2, so it sits **at** the bar, not clearly above it. Its advance is provisional until it is re-judged under the fixed prompts.
>
> **Update, same day:** the clean re-judge gave commissioning 11.50 from 6 clean judges, so it advances ([../2026-09-25-rejudge/RESULT.md](../2026-09-25-rejudge/RESULT.md)). Truck warranty is 9.00 clean.

Seed given to the generators: "AI B2B SaaS or AI-native services" (Veer, 9/25). Three generators ran in parallel with the founder brief and the seed. The shaper returned two companies. Each was judged blind by three judges, with five for any paragraph within 0.5 of the bar. The three YC controls were drawn at random from Fall 2026 B2B companies not already banked; the draw method is in `agents/controls-draw.md`. Paragraphs as judged: `controls.md`, `candidates.md`. All 23 agent reports are in `agents/`.

## Scores (mean of judges; bar = mean of all 13 banked controls = 10.93)

| Paragraph | n | Need | Value | Market | Risk | Total | |
|---|---|---|---|---|---|---|---|
| Control: private credit origination (Forward) | 3 | 3.7 | 3.0 | 3.0 | 2.0 | 11.67 | control |
| Control: speech and robot training data (Perit.AI) | 3 | 4.0 | 2.3 | 3.3 | 2.0 | 11.67 | control |
| **Data center commissioning service** | 5 | 3.8 | 2.8 | 3.0 | 2.0 | **11.60** | **advances** |
| Control: engineering physics foundation model (Vorelios) | 3 | 4.0 | 2.0 | 3.3 | 1.7 | 11.00 | control |
| **Truck dealer warranty claims** | 3 | 3.3 | 2.7 | 2.0 | 2.0 | **10.00** | stops |

Adding the three new controls moved the bar from 10.78 to 10.93. Commissioning's 11.6 is the highest score any of our candidates has reached so far; the credit-dispute idea from loop 1 was 11.2. Commissioning verdicts: 1 BACK, 4 PASS. Truck warranty: 3 PASS. Judge noise across all rounds is now a pooled sd of 0.79 for one judge, below the 1.0 threshold that would require more judges.

## What the generators converged on

- Two of three generators independently picked **warranty-claim recovery for equipment dealers** as their best idea; the third listed it as a runner-up.
- Two named an **AI quality engineer for small parts suppliers** (PPAP, 8D) as runner-up. The third dropped it as crowded.
- The third generator's best idea was **AI commissioning for data centers**.
- Loop 1's shaper had dropped dealer warranty for RV and marine dealers. This loop's shaper reshaped it toward heavy-truck dealers using NADA's ATD 2025 data ($5.41B of warranty, $13,816 per warranty repair order). It still stops on market size.

## Data center commissioning: what the judges said

**Strongest version (all five judges converged on it):**
- An **independent commissioning agent hired by the owner**, not a vendor to general contractors. ASHRAE Guideline 0 and ACG certification require independence from the builder, so the paragraph's "and their general contractors" is a conflict of interest.
- Covers only the last two test levels (system functional tests and the full-load integrated test) on liquid-cooled AI halls.
- First customers are owners without in-house programs: neoclouds, second-tier developers, and bitcoin miners converting sites for AI tenants. Hyperscalers run their own commissioning.
- The product is **live grading**: building-management, power-monitoring, cooling-unit and load-bank data merged on one timeline and graded step by step during the test, with a signed report within 24 hours. Script writing is already sold with AI by Facility Grid, CxPlanner and ArchiLabs, and CxAlloy's OTTO does automated functional testing from trend data.
- Price is a fixed fee per MW plus a bonus for on-schedule handover.

**Market:** Census revised April 2026 data center construction to $61.9B and put July at $75.2B, up 57% year on year (judge 1, from Census `privsa.xlsx`). Commissioning costs 0.5 to 2% of construction, roughly $0.4 to 1.5B a year in the US. Service firms have sold at 7.5x EBITDA (Limbach/CYMCOR, about $30M) and about 15x operating profit (Bureau Veritas/Lotusworks, €375M).

**What would kill it (every judge named one of these two):**
1. Paperwork and grading are not what delays handover. Delays come from physical fixes, retests, load banks and equipment lead times, and a senior agent must still witness tests in person, so "several times the megawatts" shrinks to about 1.5 to 2 times.
2. Owners, tenants or lenders won't accept a new firm's sign-off on a hall worth hundreds of millions.

**Fastest tests:**
- Ask 5 to 8 owner-side commissioning leads for the day-by-day log of their last liquid-cooled integrated test. Split the days into paperwork and grading versus physical work. Kill it if paperwork and grading are under about a week, or under 10% of the test window, or if the tenant chooses the agent.
- Replay one completed test package through a prototype grader. Kill it if it misses more than 20% of logged issues or saves under 40% of senior hours.
- Offer 10 neocloud and miner builders a fixed per-MW price with a schedule bonus. Kill it if fewer than 2 agree to a paid pilot or a shadow run.

## Team fit (commissioning)

- **Not viable for two undergrads alone.** The signature is the product, and the Certified Commissioning Authority needs a PE or architect license plus 3 years and 3 projects. The team needs a PE and certified agent who has run data center integrated tests, as a co-founder with equity, plus professional liability insurance.
- **What they can do this semester:**
  - Recruit that partner through 7x24 Exchange chapters, the Fall conference (Oct 25-28) and Purdue alumni.
  - Take OSHA 30 and NFPA 70E training.
  - Build the grader on 2 to 3 redacted test datasets.
  - Run 15 to 20 owner calls.
  - Do one free shadow run aimed at a letter of intent.
- **Named early targets:** TeraWulf Lake Mariner (CB4 in commissioning), Galaxy Helios, IREN, Applied Digital. On these sites the tenant (Microsoft, CoreWeave) accepts the hall, so the gating question is tenant acceptance.
- **Kill point:** if no qualified agent commits by the end of October, sell the grader as software to existing commissioning firms instead. That removes the sign-off risk but meets Facility Grid and CxPlanner head on.

## Truck dealer warranty claims: why it stops

- Market is the problem: 1% of $5.41B is about $54M a year for US trucks, and 94.5% of dealer owners run 1 to 5 stores.
- Dealer management systems (Procede Excede, Karmak Fusion) already own the repair-order data and the submission rail.
- Daimler Truck's Tavant system already offers dealers AI repair-code suggestions for free.
- The EPA proposed in July 2026 to roll back the longer emissions warranty.
- No judge found published data on how much truck dealers lose to documentation-driven cuts. Every judge's fastest test was the same: pull 90 days of claim statements from 3 to 5 dealers and kill it if documentation losses are under about 2% of warranty dollars.

## Process notes

- The shaper, most judges and the team-fit agent read local files. METHOD now forbids it for every role (adopted 2026-09-25, at Veer's request for the shaper and extended to judges and team fit after the audit).
- Control judges handled the matching-company rule unevenly. One Vorelios judge treated BeyondMath as the team instead of Vorelios, one Perit judge couldn't find Perit at all, and one Vorelios judge treated PhysicsX as the team. Their scores were within the other judges' range.
- The shaper finished without needing to be resumed (about 13 minutes).
