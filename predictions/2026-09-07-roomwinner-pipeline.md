# Room-winner test 1: PipeLine (37th BDM, 1st place, $10k), screened blind under the KILL/SCORE ladder

Written BEFORE dispatch, 2026-09-07 evening. The screener is given the concept as "TC-1", is not told
this file exists, and is told not to read `predictions/`. It writes its return to
`predictions/2026-09-07-screen-TC1.md`.

## What is being tested

Not whether PipeLine is a good company. Whether the ladder as it stood this morning (every rung kills,
stop at the first) would have killed the concept at the idea stage, and whether the split ladder lets it
through with an honest weakness list. Per METHOD Part 9, any rung that kills a first-place winner is not
a kill rung for this room.

## The concept as handed to the screener

One-liner as pitched: "operating system for trade contractors using AI to reduce costly rework."
Tuple written by the main session from the industry, no competitor research:
customer = trade subcontractor (electrical, plumbing, mechanical), ~10-100 field staff, several
concurrent commercial jobs · mistake = installed work torn out and rebuilt (wrong drawing revision,
missed coordination change, failed QC or inspection) · asset = the contractor's own drawings, RFIs,
change orders, daily logs and punch lists linked to rework events · checker = the GC superintendent or
QC, the inspector, the engineer of record on punch and back-charge.

## Predictions

- **Old ladder (every adverse finding kills, stop at first): DEAD at rung 3, mechanism GIVES.** Procore
  gives subs a free seat; Buildertrend, ServiceTitan, Jobber and Fieldwire sell the ops layer at
  commodity prices with drawing-revision control and punch tracking built in. If rung 3 somehow holds,
  DEAD at rung 4 on ordinary competition (Trunk Tools, Document Crunch, the funded construction-AI set).
- **New ladder: NO KILL.** K1 holds (rework is priced by the contractor's own P&L; no fee floor). K2
  does not fire because there is no instrument at all, which scores as a weakness on criteria 2 and 3.
  K3 does not fire: no incumbent makes the exact pre-dispatch rework-prediction claim with a named
  deployment at the 10-100 band.
- **Scored weaknesses I expect, six:** rung 1 (no priced mistake, D1 empty) · rung 2 (no instrument, no
  checker with a published rule) · 2.5 (D3 empty: nobody is employed to "reduce rework") · rung 3 (large
  residue covered free or cheap by ops platforms) · stage 6 (learning loop unclear) · 1f (the answer may
  be a lookup against the current drawing revision, i.e. computed, not observed).
- **Stage 1:** the screener cannot name a private-by-operating asset in one sentence for the pitch as
  written. Under the old method that is "stop, do not research it."

## Scoring (fill after the return)

**Old ladder, OBSERVED (blind agent, METHOD at HEAD, `2026-09-07-screen-TC1-oldladder.md`): DEAD at rung
3, GIVES + CAPTURES, D3 FILLED AT THE CUSTOMER (large firm; 10-100 band not read), M0 NONE.** Verdict HIT,
rung HIT, mechanism HIT (GIVES; CAPTURES unpredicted). Discount, per the evaluator: the prediction
restated the audit by the same author, so it was not independent. The stage-1 sub-claim ("cannot name the
asset") MISSED: the new-ladder screener named it in one sentence.

**New ladder, OBSERVED (`2026-09-07-screen-TC1.md`): NO KILL, fifteen weaknesses, D3 FILLED AT THE
CUSTOMER at the 170-1000 band and UNRUN at 10-100, M0: a narrower formulation (failed-inspection slice).**
Verdict HIT. K2 mechanism WRONG: predicted "no instrument at all"; the screen's strongest rung-2 finding
was JCI §2.2 binding the sub as duty-holder. Weakness overlap about 3 of 6 (rung 3 residue and 1f hit;
rung 1 and stage 6 partial; rung 2 "no instrument" and 2.5 "D3 empty" missed). Ten unpredicted: 2a',
JCI §7.24 and Procore §3.7 pooling, the Autodesk patent, 5b, 5c, G4, RATCHET, ABSORBS, CAPTURES, buyer's
guides on the OS half. **Caveats on this run, from the evaluator: the tuple carried detail the one-liner
does not (10-100 band, municipal inspector), the prompt's instruction 4 hinted that a company exists, the
rung-3 fact was inherited from STATE.md, and the screener ran G1-G4 itself against Part 4, so its gate
findings are provisional.**

**What the pair shows.** The same concept, same tuple, same day: the old ladder returned DEAD and NONE;
the split returned ALIVE, a fifteen-line weakness sheet, and a mutation lead that points at the one
candidate on the board the old ladder had kept (inspection readiness). The old ladder's M0 could not see
that; the split's could.

**Second winner, Litmetrics (3rd), run under the old text for the evaluator's condition
(`2026-09-07-screen-PI1-oldladder.md`): DEAD at rung 4**, Filevine Lead Docket's LeadsAI documents
*"should be signed, referred out, or rejected"* on its own help center, paid, live, to PI firms; D3 FILLED
AT THE CUSTOMER with a partial inversion (paid to sign). **The outcome-feedback half is unclaimed.** So K3
is the one kill in the split that came within one unclaimed half-claim of a room winner. Open for Veer.
