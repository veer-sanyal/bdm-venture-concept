# Audit 2026-09-07 (evening): why zero of ~64 screened candidates pass, and whether the screen is the reason

Asked by Veer: "out of 50 if there's zero passes, maybe something is wrong with the screen itself."
Read for this: METHOD.md in full; CASEBOOK.md, STATE.md and all ten predictions/ files via two agents; the
kill table rebuilt from them. **DIAGNOSIS ONLY. Nothing in METHOD.md was changed. Veer decides.**

## The count

| | |
|---|---|
| Candidates tracked | 127 |
| Screened | ~64 |
| Dead | 59 |
| Survivors | 0 |
| CONDITIONAL / cleared-ungated | 3 + 1 (inspection readiness, PPAP, pharma APR; construction notice) |
| Never screened | ~63 (12 of round 2, 14 of round 3, 17 round-7 pre-filter rejects, 23 round-8 rejects whose file is missing) |
| Customer calls made | 0 |
| Casebook entries created or sharpened on 2026-09-07 alone | 37 |
| Standing kill rules resting on n=1 | 16 |
| Kills overturned by the "argue back" procedure | 0 of 2 (both found the reasoning wrong; both let the verdict stand) |

Yesterday's session log called nine new rules in a day "the screen is much sharper." That sentence is the symptom.

## Finding 1. The screen has already killed the winners of the room it exists to win

- **Litmetrics** (3rd, $5k, "AI-driven intake and case qualification for plaintiff law firms"): "legal intake" is on STATE.md's "Also dead" list by name.
- **PipeLine** (1st, $10k, "operating system for trade contractors using AI to reduce costly rework"): its lane is sub-side construction ops, killed at rung 3 (Procore gives the sub a free seat) and rung 4 (~$140M funded: Trunk Tools, Document Crunch, Parspec).
- **Oppit** (2nd): a hardware sensor. Outside the method's universe.

**Correction, same evening, after a fresh evaluator (`2026-09-07-eval-split.md`) caught that this was derived from the kill table and never observed, i.e. a kill on a claim not read, against rule 7.** "legal intake" was a name in an unscreened `Also dead` row. **Both winners were then run blind under the old text:** PipeLine DEAD at rung 3, GIVES + CAPTURES, M0 NONE (`2026-09-07-screen-TC1-oldladder.md`); Litmetrics DEAD at rung 4 on Filevine Lead Docket's documented intake predictor, outcome-feedback half unclaimed (`2026-09-07-screen-PI1-oldladder.md`). The finding stands as observed for both, with the evaluator's nuance: the old ladder killed PipeLine's wording and kept its substance alive as survivor 1. The casebook says so in its own words: C-49 "the judges are not the customer", C-52 "a candidate can pass every rung and still be the wrong company", C-58 "two standards, as written, no early-stage idea could meet."

## Finding 2. The pass condition moves, and only in one direction

- Every candidate that ever passed the gate generated the rule that killed it (C-58c). Supplier chargeback cleared six rungs and all four gate questions and died the same night to rung 5c, written that night.
- Rule 6's free-competitor list went from 2 shapes to 10 (GIVES, PUBLISHES, CAPTURES, ABSORBS, RATCHET, FEE-SHIFT, COMPELLED, UNDERCUT, RESERVE, FORBID). Each new shape applies to every later candidate. The number of ways to die grows with the number screened; no rule has ever been removed for being too harsh. Part 9 admits it: "a calibration loop that can only tighten is not a calibration loop, it is a direction."
- 16 rules rest on one instance and are applied as standing kills, against the method's own two-instance bar (C-53). The instances are not independent either: construction, freight, auto supply and compliance recur across most of the 64.
- The fixes for this (PASS STATEMENT, prune both ways, argue back) were bolted on the same day 37 rules were added. The fix was additive; the disease is additive.

## Finding 3. Three requirements are anti-correlated in the world (the pincer)

D1 demand (a counterparty prices the mistake in writing) AND rung 3 empty AND rung 2 poolable. A counterparty that prices the mistake in writing has usually also published the answer, reserved the determination, and written the data-ownership clause. So the strongest demand evidence predicts the kill. C-58a already names it: "the surviving band is pain priced by a counterparty, served by nobody and staffed by nobody... nearly empty by construction, and no single rule edit fixes it." That sentence was written, and then the search continued into the same band for another forty candidates.

## Finding 4. "A free worse version exists" is a kill here and the baseline in the room

Rung 3 (~15 kills) and rung 4 "ordinary competition" (~26 kills) are the two largest. Rung 3's own wording is "who does a WORSE version for nothing", and it kills on presence, never on comparison. The rubric's criterion 5 is "performance improvement over existing solutions", which requires existing solutions. Same fact, opposite verdict. Most rung-4 kills are "a funded competitor exists" (Dili $15M, Glimpse $10M, TrustLayer $15M). To a pre-seed panel a funded competitor is market validation. Every vertical SaaS that exists started against a free worse version.

## Finding 5. Stage 6's learning loop is a Series A moat test, and it killed the best-evidenced candidate

Supplier chargeback had the best D1 on the board (Tenneco: $1,000 per part number per resubmission). It died because Ford PPGTC §20.01 forbids pooling, and without pooling "our data gets better as we run" is unavailable, which stage 6 requires. A single-customer product on the customer's own records plus the free public CSRs is a real business, and the room does not score data moats. PipeLine had no pooled outcome ledger when it won.

## Finding 6. The return format asks for three negatives and zero positives

A screener must return: killing rung, D3 state, mutation answer. There is no field for the case FOR. Stop-at-first-kill means every dead candidate carries exactly one negative finding and no positive finding weighed against it. An agent asked "what killed it" finds something.

## Finding 7. The scorecard cannot see a false negative

Verdict hit rate runs 90%+ because the verdict is always DEAD; predicting the base rate is not calibration. Mechanism hit rate never exceeded 50% in any round. The two argue-backs both found the kill's reasoning wrong (uncorroborated vendor marketing on scrap grade calls; BLS data refuting the D6 reason) and both left the verdict standing.

## What to change (proposals, not applied)

1. **Run the ladder on PipeLine and Litmetrics as candidates.** Any rung that kills a first-place winner is demoted from KILL to SCORE. Three screens, one afternoon. This is the falsification test the method has never run.
2. **Split the ladder into KILL and SCORE.** Kill only on instrument-verified facts: the instrument does not bind the customer (2d); the money cannot be moved or the magnitude is under the fee floor (1); an incumbent makes the EXACT claim to the EXACT segment with a named deployment (G1 and G2 together, read on its own page). Everything else (free substitute, funded competitor, D3 empty, no pooling, no learning loop, a patent) becomes a scored weakness. Then rank, and the top of the ranking is the submission. Roughly 30 of the 59 kills become scored weaknesses under this.
3. **Freeze the rule set until the search stop.** A new finding is a hypothesis in predictions/ and kills nothing this cycle. Retire the 16 n=1 standing rules to hypotheses.
4. **Demote stage 6's learning loop from gate to weakness.** Reopen supplier chargeback and scrap grade calls under it (STATE.md already names scrap grade calls first to reopen).
5. **Add a CASE FOR field to the screener return, and make rung 3 comparative:** how much of the priced mistake does the free substitute actually remove? Presence is not a kill.
6. **Stop generating. Call.** Four candidates are alive. STATE.md already says the contractor call and the quality-manager call "are worth more to the December score than every competitor sweep in this file." This is the optimise-the-system-instead-of-acting shape: 630KB of method, 127 candidates, 37 rules in one day, zero customers spoken to.
