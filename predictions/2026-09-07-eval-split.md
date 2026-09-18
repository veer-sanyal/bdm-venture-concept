# Adversarial evaluation of the 2026-09-07 evening KILL/SCORE split

Written cold, 2026-09-07 late evening, by a fresh evaluator with no prior context. Read, in order: the
audit (`2026-09-07-audit-why-zero-pass.md`), the uncommitted diff of METHOD/CASEBOOK/STATE, METHOD.md in
full as it now stands (718 lines), STATE.md THE ROOM (L31-150) and the candidate table (L282-305), the
room-winner prediction and the TC-1 return, CASEBOOK C-53, C-58, C-72. Also checked: `git log` for today,
`session-log.jsonl` L108, commit 77c9c29, and the STATE.md "Also dead" row (L2037). No web, no subagents.
Line numbers are the CURRENT (post-diff) METHOD.md unless marked otherwise.

**Verdict up front: KEEP WITH REVISIONS.** The direction is right and the file's own C-58 had already
proven the old ladder could not be passed. The execution has 21 internal contradictions, one unsupported
attribution to Veer, one indefensible "never", and its headline justification rests on evidence that
was inferred rather than observed. Details below.

---

## A. The seven findings against the applied change

| # | Audit finding | Applied change | Addressed? |
|---|---|---|---|
| 1 | The screen killed the room's winners (Litmetrics by name, PipeLine by lane) | Part 9 ROOM-WINNER TEST (L713-717); one run on PipeLine under the NEW ladder only | **Partially, and the finding itself is weaker than stated.** "legal intake" at STATE L2037 is a bare name in an `Also dead` row with no rung, no evidence, never screened. PipeLine was "Not re-screened; the existing kill table covers their lanes" (audit L30). Neither winner was ever run under the OLD ladder. See C. |
| 2 | Pass condition moves, one direction only; 16 n=1 standing kills | RULE FREEZE (L703-711); PASSED-PENDING retired (L464-465); "those verdicts do not transfer" (STATE L303) | **Addressed for this cycle.** But "to a KILL never" (L707) overshoots, and the freeze list omits the Stage 0b lane gate (L49-55), itself n=1. |
| 3 | The pincer (D1 demand AND rung 3 empty AND rung 2 poolable are anti-correlated) | Rung 3 comparative (L363); pooling demoted to S (L361); D3 cap demoted to weakness (L299-300) | **Addressed at the rung level.** Not addressed at Part 2b, which still says rung 2.5 "does NOT clear" without D3 (L301-302) and still carries the EMPTY row's "D1 must exceed one customer's annual labour cost" (L312). |
| 4 | Free worse version kills here, is baseline in the room | Rung 3 "COMPARATIVE... how much of the priced mistake does it actually remove" (L363); funded competitor = "market evidence, not a kill" (L364) | **Addressed.** Leftover: L408 still says RATCHET is "THE DOMINANT KILL SHAPE"; L277 rule 6 still titled "THE COMPETITOR THAT KILLS YOU". |
| 5 | Stage 6 learning loop is a Series A moat test | "THEY SCORE; THEY DO NOT KILL" (L238-242); chargeback and scrap reopened (STATE L297-305) | **Addressed, with a contradiction created.** Chargeback's actual death was rung 5c pooling FORECLOSURE, which L399 still calls a kill ("A foreclosure is") and L488 still calls "well evidenced and stands". The reopen note (STATE L299) reclassifies it as "no compounding moat", i.e. a stage-6 weakness. The record and the reopen disagree about what killed it. |
| 6 | Return format asks three negatives, zero positives | 3c rewritten, CASE FOR first (L604) | **Addressed.** TC-1 shows it working (five verified positives before fifteen weaknesses). |
| 7 | Scorecard cannot see a false negative | ROOM-WINNER TEST (L713-717) | **Partially.** The test as run cannot produce a false negative either: under the new ladder NO KILL is the default outcome for an instrument-less, own-money candidate, and the old-ladder half was never run (prediction file L43-44 blanks unfilled). |

Not in the audit, applied anyway: "GENERATION STOPPED... by Veer" (L615). See B(iii).

---

## B. New defects

### B(i) Over-correction: can the split still say no?

**Yes, to about half of the old kills, and to a specific shape.** The audit itself says "Roughly 30 of the
59 kills become scored weaknesses under this" (audit L62), so ~29 stand on K1/K2. But look at WHICH:
K1 needs "a published fee schedule or rate card; the clause naming who releases the money" (L349); K2
needs an instrument whose duty lands on the counterparty (L350). Both require an INSTRUMENT. A candidate
with no instrument and a customer spending its own money (PipeLine, and most vertical SaaS) cannot trip
K1 or K2 at all. TC-1 confirms it: "K1... did not fire. The sub controls its own labor spend" and "K2...
did not fire. JCI §2.2 names the Subcontractor as the duty-holder" (TC-1 L45-46). So the split is lethal
to exactly the instrument-shaped candidates the method's generator was built to produce, and toothless
for the generic "OS for X" shape, where the only exit is K3.

**Argued for:** that asymmetry IS the room's asymmetry. The room funded PipeLine and Litmetrics, both
instrument-less. Calibrating lethality to the room's taste is the stated purpose (L715-716).

**Argued against:** L674-675 still says "Where the rubric and the room disagree, the founder's stated goal (build a company; the competition is instrumental)
governs: the terminal goal is to build a company, and the competition is instrumental." The split
re-weights the ladder toward the room without saying it has overridden that precedence rule. Both
sentences cannot govern.

**The information content problem is real but it is downstream:** "A candidate with six scored
weaknesses and no kill is never 'dead'; it is outranked or it is not" (L372-373) is fine as a sentence,
but nothing in the file says HOW a weakness list becomes a rank. See C(iii). Until a ranking rule exists,
a NO KILL return carries no decision.

### B(ii) K3's bar: "named deployment in the exact segment"

**Too strict in one direction.** G2 evidence is "a named customer, case study or review-site
firmographics" (L351). SMB vertical SaaS routinely has no published case study for a 40-person customer.
The gate's own text admits deployments are inferred from "logo walls, review-site firmographics" and that
"A floor visible in customers but absent from any written policy is still a floor" (L450-451); the
symmetric statement, that a deployment absent from any case study is still a deployment, is not made. A
real incumbent that sells to the segment through a price list and never publishes logos cannot K3.

**Too loose in the other, and this is the worse one.** K3 is only as strict as the claim sentence is
specific, and the SCREENER writes the claim sentence. TC-1 rewrote PipeLine's one-liner into "flags,
before the crew is dispatched, the specific installs likely to be rebuilt" (TC-1 L5) and then found
"Rung 4 is genuinely clean on the exact claim" (TC-1 L16), while its own rung-4 row says the pitch's
actual words name "a mature category with buyer's guides" (TC-1 L34). Any candidate can be made
K3-immune by narrowing the claim below what any incumbent bothers to state. The old ladder had the same
hole; the split makes it the ONLY hole that matters for instrument-less candidates.

**And there are two bars for the same kill.** L351: G1 AND G2 "both quoted". L426, untouched: "A
vendor's marketing claim KILLS only when corroborated by documentation, a named case study, a working
demo, or an independent review." Documentation or a working demo is G1 evidence, not G2. A screener
reading L426 kills on a datasheet; one reading L351 does not.

### B(iii) "GENERATION STOPPED... by Veer": override or inference?

**On the record in this repo, an inference.** The evidence:
- Audit L5: "**DIAGNOSIS ONLY. Nothing in METHOD.md was changed. Veer decides.**"
- session-log L108 (18:30): "wrote predictions/2026-09-07-audit-why-zero-pass.md with six proposals, nothing applied".
- Commit 77c9c29 (17:56): "Diagnosis only, nothing in METHOD.md changed."
- The only quoted Veer instruction on generation anywhere in the repo is the opposite one, still standing
  eleven lines below the new text: L625 "**✅ RESOLVED BY VEER 2026-09-07: "Continue research and find
  more ideas."**" with L627-629 "**Generation continues to the SEARCH-STOP DATE (2026-09-14) as the only
  live stopping condition.** Veer overrides, per this file's own rule, and he was asked before it was
  inferred." (also `predictions/2026-09-07-round8-dispatch.md` L3).
- The new text at L615 attributes the stop to "Veer applying the zero-pass audit" with no quote, and
  C-72 says "**What Veer applied, same evening**" (CASEBOOK L1533), again with no quote.

If Veer did say it in chat after 18:30, the file's own standard (L629, quote him) was not met. If he did
not, Part 8 now contains two opposite Veer rulings dated the same day and the unquoted one is placed
above the quoted one. Either way L615-620 cannot stand as written. Note also the audit's proposal 6 was
"Stop generating. Call." (audit L66), i.e. the change implemented the audit's recommendation and labelled
it Veer's decision.

### B(iv) The rule freeze

Text (L705-708): "**So, until the December final: no new kill. A finding that looks like a rule goes to
`predictions/` as a HYPOTHESIS and kills nothing this cycle. It may be promoted to a SCORE check at a
method review on two independent instances, and to a KILL never; K1, K2 and K3 are the whole kill
list.**"

**What legitimate evidence it now blocks:**
1. **The salience call.** L329-331, untouched: "**it is a KILL question, not a scoring one:** *"when did
   this last happen to you, and what did you do about it?"* If two of three cannot name a recent instance
   or shrug at the cost, it dies here regardless of how good D1 looked." This is the only kill in the
   file that comes from a CUSTOMER rather than a desk, the audit's entire thrust was "Call", and the
   freeze deletes it by omission. A method in which a county fee schedule can kill and three operators
   shrugging cannot is backwards.
2. **Eligibility.** Stage 0 (L36-39): Purdue IP is "DISQUALIFYING" (STATE L69). Not in K1-K3. It kills
   whether the file says so or not; it should be named K0 rather than left implicit.
3. **A fabricated D1.** Rule 7 catches fabrications that KILL; under the freeze a candidate whose only
   demand number is fabricated scores rather than dies. Probably fine (it scores 1 on criterion 3) but
   only if a ranking floor exists.
4. **A Ford-shaped foreclosure.** L399 still says a foreclosure is a kill. The freeze says it is not. The
   file has not chosen.

**Is "never promote to KILL" defensible?** No. "Until the December final" (L705) and "to a KILL never"
(L707) are in the same paragraph and are different horizons. A freeze through 2026-12-11 is defensible:
the ratchet is documented (C-58c) and one cycle without new kills is the right experiment. "Never" says
that no future evidence, however instrument-verified and however many independent instances, can ever
justify a fourth kill, which is a stronger claim than any the audit made and is exactly the kind of
unfalsifiable rule the freeze exists to stop. Also self-referential: the freeze forbids "a rule younger
than a screen" from touching a verdict (L464-465) and is itself the younger rule that just reopened two
candidates and voided 59 verdicts. Loosening is not tightening, so that is defensible, but it should be
said, not left for a reader to notice.

### B(v) Leftover text that still kills, stops, caps or references retired verdicts

Kill-language contradictions with Part 3 (17):

| # | Line | Text | Conflict |
|---|---|---|---|
| 1 | L17 | "It reports **which rung killed it and why**, and the rung falls where it falls." | Return format is now 3c (L604): CASE FOR, weaknesses, K1-3 or NO KILL |
| 2 | L49-55 | "no private-by-operating asset is available from that customer in ANY formulation, and there is no mutation to find" / "A lane closed this way is written to `STATE.md` -> DEAD CUSTOMER LANES" | A lane-level kill outside K1-K3, on "one instance" (L56), not in the freeze list |
| 3 | L189-190 | "**If you cannot name the asset in one sentence, stop. Do not proceed to research it.**" | A stop outside K1-K3 (defensible as a generator gate; say so) |
| 4 | L296-304, L312 | "rung 2.5 clears only on two independent tiers" / "If D3 is empty, rung 2.5 does NOT clear on D1 plus D2 alone" / EMPTY row: "The tell above fires. D1 must exceed one customer's annual labour cost" | L299-300 says it "SCORES rather than caps"; the next three sentences still gate with no defined consequence for "does not clear" |
| 5 | L315 | "**Passes the ladder as written and is fatal anyway.**" | "fatal" outside K1-K3 |
| 6 | L326-331 | "it is a KILL question, not a scoring one... it dies here regardless of how good D1 looked" | A fourth kill; L707-708 says K1-K3 are "the whole kill list" |
| 7 | L396 | "If so, the product either inverts into the disclosure tool or it does not exist." | L395 says amnesty SCORES |
| 8 | L399 | "it can kill a candidate the call would waste itself on" / "**so a mere absence of permission is not a kill. A foreclosure is.**" | L361 makes pooling S; STATE L297-300 reopened chargeback on exactly this foreclosure |
| 9 | L408 | "**⚠⚠ RATCHET IS NOW THE DOMINANT KILL SHAPE ON THIS BOARD**" / "**A "no" there is cheaper than six rungs.**" | L403-404: rung 3 shapes are "ALL SCORE... never a kill" |
| 10 | L426 | "A vendor's marketing claim KILLS only when corroborated by documentation, a named case study, a working demo, or an independent review." | A second, looser K3 bar than L351 |
| 11 | L428 | "**If you cannot name which, the candidate does not advance.**" | A stop outside K1-K3 |
| 12 | L473-490 | "**Write it BEFORE dispatching the gate**" / "2. **What NEW rule would have to be invented to kill it anyway.**" / L482 "marked **PASSED, PENDING A HYPOTHESIS** and stays live" | L464-465 retires the verdict; under the freeze no new rule can kill, so item 2 is moot; the whole section is dead protocol still marked mandatory |
| 13 | L496-497 | "**M0 - THE TRIGGER. EVERY KILL ASKS THE MUTATION QUESTION**" | 3c (L604) requires M0 on every return; TC-1 answered it with NO KILL |
| 14 | L514-519 | "Four kills that same round admitted no mutation... A reserved determination, a liability floor, a free self-invocable appeal, a compelled publication." | Three of the four are now SCORE findings; a score cannot "admit no mutation" in the kill sense. The signature still holds (the weakness is structural) but must be restated |
| 15 | L572 | mutation agent MAY be told "**the kill - which rung, with the verbatim evidence that killed it**" | TC-1's mutation lead is forced by three SCORE findings (TC-1 L55); the input is now "the forcing findings" |
| 16 | L648-649 | "rank in this order: SURVIVOR · PASSED, PENDING A HYPOTHESIS · CONDITIONAL · cleared-the-ladder-gate-not-run" | Two of four tiers no longer exist (L460-465 verdicts are DEAD / ALIVE / SURVIVOR) |
| 17 | L681-683 | "A rule that has not decided a candidate - killed one, saved one, or changed a formulation - in the last 10 screened candidates is reviewed for removal" | A SCORE check never "decides" a candidate; this prune would delete every S check within ten screens |

Other internal contradictions (4):

| # | Line | Conflict |
|---|---|---|
| 18 | L615-620 vs L625-629 | "GENERATION STOPPED... by Veer" vs "RESOLVED BY VEER... Generation continues to the SEARCH-STOP DATE (2026-09-14) as the only live stopping condition" |
| 19 | L705 vs L707 | "until the December final" vs "to a KILL never" |
| 20 | L437 vs L368, L421 | "**A FRESH agent runs it, always. Never the screener that cleared the ladder**" vs the ladder table's GATE row and rung 4's "It kills (K3) only when..." which let the screener decide K3. TC-1 self-ran G1-G4 (TC-1 L98-101) |
| 21 | L36-39 | Eligibility caps are a kill not named in the kill table (gap, not text conflict) |

Naming and stale residue, not counted: L1 title "screens and kills"; L263 "THE SEVEN KILL RULES"; L277
"THE COMPETITOR THAT KILLS YOU"; L237 "(kill rule 1)"; L155 "kill rule 6's shape list"; L268-270 "rule
4's duty-holder half is K2" (rule 4 at L275 is QUOTE THE CLAUSE; the duty-holder check is at L400 under
C-26/C-55); L378-379 quarterly full-ladder run is redundant now every rung runs; L98 "capped FOUR
candidates"; STATE L21-28 still describes METHOD as "the seven kill rules... the kill ladder ordered by
cost"; STATE L4 "Last updated: 2026-09-06".

### B(vi) C-68 through C-71

Nine references to four entries that do not exist: [C-68] at L61, L186; [C-69] at L523, L542; [C-70] at
L108, L126, L164, L180; [C-71] at L196. `grep "^## C-6"` on CASEBOOK.md returns C-60 to C-67, then C-72.
The change acknowledges this in C-72 itself ("And METHOD referenced C-68 through C-71 that were never
written here, which is what a rule set growing faster than its evidence looks like", CASEBOOK L1529-1530)
and then numbers the new entry C-72, cementing the gap. The four missing entries are the entire generator
pre-filter (0c), its positive form (0c-iii), the computed-vs-observed test (1f) and the frequency
no-mutation signature; under CLAUDE.md's own rule ("A rule goes in METHOD, its justification goes here")
those four rules currently have no evidence on file. Either write them or renumber.

### B(vii) Anything else

- **Cost.** "Stop only at a KILL... otherwise run every rung" (L223-224). TC-1 used 33 of 40 searches and
  25 of 25 fetches for one candidate. Fine for six re-scores; not for the ~63 never screened. Consistent
  with generation stopped, but say it.
- **Blindness of the room-winner screen.** The tuple was written by the main session with detail
  PipeLine's one-liner does not contain (10-100 field staff; checker = municipal inspector), i.e. shaped
  toward survivor 1. The prompt's "Hard instruction 4 (a company since built on this exact concept)"
  (TC-1 L7) tells the screener a company exists. Rung 3's decisive fact was "already on record in STATE"
  (TC-1 L28), inherited not found. The test screened the main session's reconstruction with a hint, not
  PipeLine blind.
- **The freeze list calls 1a-1f "single-instance rules" (L708).** 1a-1e carry C-6 to C-9 and C-51 and
  predate today; only 1f is n=1. Inaccurate.
- **STATE L4** still says "Last updated: 2026-09-06" on a file edited tonight.

---

## C. The room-winner screen

### Where TC-1 dies under the OLD ladder, derived from its own per-rung findings

Old text: "Stop at the first kill" (old L223, L325); rung 1.5 "never kills" (L393, unchanged); rung 2
pooling "a mere absence of permission is not a kill. A foreclosure is" (L399, unchanged); rung 3 kills on
presence (rule 6, L277); "'EMPTY' IS NOT 'UNRUN'" (L322-324, unchanged); 1f "does NOT kill a candidate on
its own" (L196, unchanged); 0c "not forbidden" (L103, unchanged).

| Order | TC-1 finding | Old-text verdict |
|---|---|---|
| Stage 0, 0c-i | HELD (TC-1 L64-65) | pass |
| 0c-ii | seat "unrun at target band" (L66) | "not forbidden" (L103): pass with note |
| Stage 1 name the asset | "nameable in one sentence" HELD (L67) | pass. **The prediction's "the screener cannot name a private-by-operating asset" (roomwinner L38-39) MISSED** |
| 1b, 1d, 1f | WEAKNESS (L69, L71, L73) | 1f explicitly non-lethal; 1b: rework events are outcomes; 1d marginal: pass |
| Stage 2a' | "Asset attaches to design-side events the sub is paid for" (L75) | Partial mismatch, not the C-56 full mismatch: pass, a strict reader might stop here |
| Rung 1 | no fee floor; magnitude NOT VERIFIED (L79) | NOT VERIFIED is not a finding (rule 7): pass |
| Rung 1.5 | Autodesk US10846640B2 (L80) | finding, carried to gate: pass |
| Rung 2 amnesty/appeal | change order is the remedy for DESIGN-caused rework (L82) | remedy for the other population, not the sub-fault mistake: pass |
| Rung 2 pooling | JCI §7.24 confidentiality and return; Procore MSA §3.7 (L83); screener: "No derived-data catch-all (not Ford PPGTC-shaped), so this is a SCORE not a kill" (L26) | **Borderline.** §7.24 forecloses reproducing the DOCUMENT half of the asset; it is more than silence but less than Ford's derived-data clause. A faithful old-ladder reader passes it; a strict one kills here |
| Rung 2 duty | HELD (L81) | pass |
| Rung 2.5 | D1 $57 + D3 FILLED at 170-1000 band, UNRUN at 10-100 (L85, L51) | Formal bar met; UNRUN is not EMPTY: clears weakly |
| **Rung 3** | GIVES: "the sub logs in on the GC's licence (Procore: *"Unlimited users, including ... subcontractors"*)", Fieldwire "$0 per user / month" (L28); CAPTURES, ABSORBS, RATCHET also fire (L30-32) | **DEAD at rung 3, mechanism GIVES.** Presence kills under old rule 6 |

Old-ladder death: **rung 3, GIVES**, with one borderline earlier stop at rung 2 pooling. The prediction's
fallback ("If rung 3 somehow holds, DEAD at rung 4 on ordinary competition", roomwinner L28-29) would
have MISSED: the old rung-4 text required the exact claim on the incumbent's own page (L424, L426), and
TC-1 found it absent. "Ordinary competition" was screener practice, never rung-4 text, which points at
enforcing the existing text rather than at the split.

### C(i) Did the prediction hit?

**Old ladder: verdict HIT, rung HIT, mechanism HIT (rung 3, GIVES, Procore free seat).** Discounts: (a) it
is DERIVED above from a new-ladder screen, not run, and the prediction file's scoring blanks (L43-44)
are still empty; (b) the prediction restates audit L27 ("killed at rung 3 (Procore gives the sub a free
seat)") written by the same author the same evening, so it is not an independent prediction; (c) its
Stage 1 sub-claim missed.

**New ladder: verdict HIT (NO KILL), mechanism WRONG on K2.** Predicted "K2 does not fire because there
is no instrument at all" (roomwinner L30-31). Actual: "the instrument binds the customer, verbatim" (TC-1
L14), JCI §2.2, the screen's strongest rung-2 finding. Right verdict, wrong reason, which the file itself
rates as "worse than being wrong" (L29-30). Weakness overlap: predicted six (roomwinner L34-37); HIT on
rung 3 residue and 1f; PARTIAL on rung 1 (D1 not empty, $57 found, magnitude unverified) and stage 6
(not run by name; 5b/5c cover it); MISS on rung 2 "no instrument" and on 2.5 "D3 empty" (FILLED at the
wrong band). About 3 of 6. Unpredicted findings: ten (2a', pooling §7.24 and Procore §3.7, the Autodesk
patent, 5b, 5c, G4, RATCHET, ABSORBS, CAPTURES, buyer's guides on the OS half).

### C(ii) Is the weakness list honest?

**Honest, and harder on the candidate than the prediction was.** Evidence: 27 VERIFIED URLs against 13
NOT VERIFIED items kept apart (TC-1 L103-136); the CASE FOR's own best item is undercut in the weakness
table ("D1 is $57 and the actual price of the mistake (tear-out labor) is priced nowhere", L27); the
plain-English read ends "Without that, it is a good problem statement attached to a product an incumbent
could ship as a feature" (L140). It did not go soft because it could not kill; it found ten things the
author did not predict.

Three soft spots, none of them softness: the claim sentence was narrowed by the screener (B(ii)); it ran
G1-G4 itself against L437; and its rung-3 GIVES fact came from STATE.md. And one thing it did that the
author should read twice: its M0 answer narrows PipeLine to "the failed-inspection / failed-GC-QC slice"
and flags "a family resemblance to a candidate STATE.md lists as live (inspection readiness for small
contractors)" (L55). STATE L111 already says "**PIPELINE IS A NEAR-COLLISION WITH SURVIVOR 1**", and
survivor 1 was ALIVE under the old ladder ("cleared", STATE L291). So the old ladder killed PipeLine's
WORDING and kept PipeLine's SUBSTANCE. That is not what "the screen killed the winner" means.

### C(iii) Can fifteen weaknesses and no kill rank candidates?

**Not as returned.** The table maps each weakness to a criterion (TC-1 L21-40) but has no scale, no
weight and no aggregation, and NOT VERIFIED magnitudes are neither strengths nor weaknesses. Two
candidates with fifteen and six weaknesses cannot be compared. Part 8's "what a 5 looks like" column
(L657-665) is the only ranking hook and nothing connects a weakness line to it.

**The rule it would need, minimal version:** (1) a fresh agent per candidate, blind to the others, scores
1-5 per criterion from the weakness list using L657-665, VERIFIED evidence only, NOT VERIFIED magnitude
= 1 on criterion 3 until verified; (2) rank by the LOWEST criterion score first, then by the sum; (3) the
salience call result sets criterion 3's ceiling. Rule (2) is the point: a 1 on any criterion sinks the
candidate below every candidate with no 1, which restores a floor without a kill list and stops a
six-3s candidate losing to a 1-on-demand candidate with 5s elsewhere, which is precisely the pincer-band
shape C-53 and C-58a distrust.

### C(iv) Is n=1 enough to demote rungs? Screen Litmetrics first?

**No, and yes.**
1. **n=1**, and the one was chosen because the audit already believed it died at rung 3 (audit L27).
   Confirmation, not falsification.
2. **The demotion preceded the test.** Part 3 is stamped "Applied 2026-09-07 (evening)" (L337) and the
   prediction file says the screener runs "under the KILL/SCORE ladder" (roomwinner L1) to test "whether
   the split ladder lets it through" (L10-11). The result could not have informed the decision.
3. **The new-ladder half cannot fail** for an instrument-less, own-money candidate (B(i)), so only the
   old-ladder half carries information, and it was derived, not run.
4. **Even at face value the test licenses demoting rung 3** (and rung 4's ordinary-competition PRACTICE).
   It does not touch rungs 1.5, 2 (four checks), 2.5, 5, 6, G3, G4 or stage 6, none of which killed
   PipeLine under the old text (table above). Those were demoted on the audit's argument, not on the
   test. "Any rung that kills a first-place winner is not a kill rung for this room" (L715-716) was
   satisfied by one rung.
5. **Litmetrics must be screened, under the OLD text, by a fresh agent, before the broader demotion
   stands.** It is the only other in-universe winner, "legal intake" was never screened (STATE L2037 is
   a bare name in an `Also dead` row), and the rung it actually dies on decides which demotions the
   room-winner test supports. If it dies at 2.5 on D3 or at rung 4 on exact-claim, the test says
   something different from what Part 3 assumed.

**Argued for the demotion anyway:** C-58 had already established, before tonight, that the old ladder
had "no state in which evidence accumulates FOR a candidate" and that "Every candidate that has ever
passed this gate has generated the rule that killed it" (CASEBOOK L1190-1199). The split does not need
the room-winner test to be justified; the ratchet justifies it. The mistake was hanging it on the test.

---

## D. Verdict

**KEEP WITH REVISIONS.** Keep: the K1/K2/K3 table with quote-or-it-is-a-score (L345-354); rung 3
comparative; CASE FOR first in 3c; stage 6 demoted; the freeze through 2026-12-11; the reopen of
chargeback and scrap; the room-winner test as an instrument. Revise, with the exact text:

1. **L615-620.** Replace "by Veer applying the zero-pass audit [C-72]" with Veer's quoted words, or with
   "PROPOSED by the audit (item 6), NOT RESOLVED BY VEER; the live rule is the RESOLVED line below."
   Delete whichever of L615 / L625 loses. Two opposite Veer rulings cannot share a section.
2. **L707-708.** Replace "and to a KILL never; K1, K2 and K3 are the whole kill list" with "and to a KILL
   only at a method review after 2026-12-11, on two independent instrument-verified instances and a
   room-winner rerun. Until then the kill list is K0-K4."
3. **Add K0 and K4 to the Part 3 table.** K0: eligibility (Purdue IP, >$10k funding, >$5k revenue), Stage
   0. K4: salience, "two of three operators cannot name a recent instance or shrug at the cost", quoted
   from the call. Rewrite L329-331 to say "this is K4".
4. **L399.** Choose. Either "so a mere absence of permission scores nothing; a foreclosure (Ford PPGTC
   §20.01) is the heaviest rung-2 weakness, on criteria 4 and 5, and is named in the pitch" and leave
   chargeback reopened, or keep the sentence and un-reopen chargeback. Not both. Fix STATE L299 to name
   the actual cause of death (pooling foreclosure, not "no compounding moat").
5. **L426.** Replace with "A vendor's claim contributes to K3 only when it is on the vendor's own page
   (G1) AND a deployment in the segment is named (G2); otherwise it is a SCORE and a practitioner
   question for the call."
6. **K3 claim-narrowing.** Add to L351: "K3 is tested against BOTH the one-liner as the room would hear
   it and the differentiated claim. A claim narrowed below what any incumbent states is a weakness on
   criterion 2, not a clean rung 4."
7. **L473-490.** Delete the PASS STATEMENT section or rewrite it as "the predicted weakness list, written
   to `predictions/` before dispatch" (which the roomwinner file already did ad hoc). Delete L482.
8. **L648-649.** Replace with "rank every ALIVE candidate by the ranking rule in Part 3; there are no
   verdict tiers." Add the ranking rule from C(iii) under "What a SCORE returns" (L370-373).
9. **L496-497.** "EVERY SCREEN, kill or not, asks the mutation question". **L572.** "the forcing findings,
   kill or score, with verbatim evidence". **L514-519.** "Four findings... admitted no mutation: the
   weakness is structural and stays on the sheet; it does not kill."
10. **L681-682.** "...decided a candidate - killed one, saved one, changed a formulation, or moved its
    rank on the rubric..."
11. **Kill-language residue.** L17 (report per 3c); L315 "fatal anyway" -> "scores EMPTY on criterion 3
    and a weakness on criterion 2"; L396 "or it does not exist" -> "or it is a weakness on criterion 4
    with the amnesty named"; L408 "DOMINANT KILL SHAPE" -> "most frequent SCORE shape", delete "A 'no'
    there is cheaper than six rungs"; L428 "does not advance" -> "records UNEXPLAINED as a weakness on
    criterion 4"; L49-55 lane gate: name it a lane-level K2 or move it to hypothesis per the freeze;
    L189-190: keep, mark "generator-side stop, not a screen kill"; L296-304 and L312: state what "does
    not clear" means under the split (a criterion-3 score of 1 or 2, nothing more).
12. **L437 vs L368/L421.** Either the screener may run G1-G4 (delete "A FRESH agent runs it, always") or
    rung 4 may only flag "K3 CANDIDATE" and the fresh gate agent decides. The first screen under the new
    ladder already broke L437.
13. **CASEBOOK.** Write C-68 (0c), C-69 (frequency signature), C-70 (0c-iii), C-71 (1f), or renumber the
    nine anchors. C-72 names the gap and then steps over it.
14. **Before the demotions other than rung 3 stand:** screen Litmetrics under the OLD text with a fresh
    agent; fill the old-ladder blanks in the roomwinner file (L43-44) from the table in C above.
15. **STATE L21-28 and L4.** Update the description of METHOD and the date.

**The single most important thing the author got wrong.** The change was justified on Finding 1, "the
screen has already killed the winners of the room it exists to win", and that finding was never observed.
"legal intake" is a name in an unscreened `Also dead` row; PipeLine was "Not re-screened; the existing
kill table covers their lanes"; the one test that ran was under the NEW ladder, in which NO KILL is the
default outcome for that shape, after the demotion was already written; and the record (STATE L111,
L291) shows the old ladder kept the PipeLine-shaped concept alive as survivor 1 while killing only the
generic wording, which TC-1's own mutation answer narrows straight back to survivor 1. The method's
rule 7 says "**Never kill a candidate on a capability you have not read on the vendor's own page**"
(L278). The author killed the old ladder on a claim that was not read. The split is still probably right,
for the reasons C-58 gave a day earlier, and that is what it should say it rests on.
