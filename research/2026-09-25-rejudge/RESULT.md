# Clean re-judge of the two advancing ideas, 2026-09-25

Desk research only. This is not customer validation.

**Why:** the loop 2 audit ([contamination-audit.md](../2026-09-25-loop2/contamination-audit.md)) found that 9 of 17 loop 2 judges had read METHOD.md or STATE.md before judging. Veer asked for both advancing ideas to be re-judged with clean judges, and for METHOD to be fixed so it can't recur.

**How:**
- Every judge got the judge prompt plus the new line "Use the web, and don't read local project files."
- Every transcript was checked with `tools/audit_reads.py` before its score was recorded. **All 15 were clean.**
- The nine flagged loop 2 rows have kind `excluded` in `scores.csv`. Their paragraphs were topped back up to at least 3 clean judges.
- All reports are in `agents/`.

## Results (bar = mean of 13 banked controls = 10.93)

| Paragraph | Clean judges | Need | Value | Market | Risk | Total | Before (contaminated or unaudited) |
|---|---|---|---|---|---|---|---|
| **Data center commissioning service** | 6 | 3.8 | 2.7 | 3.0 | 2.0 | **11.50, advances** | 11.60 (n=5, 4 of them read METHOD) |
| **Credit dispute response for collectors** | 5 | 4.0 | 2.8 | 2.2 | 2.0 | **11.00, advances** | 11.20 (n=5, loop 1, unaudited) |
| Truck dealer warranty claims | 3 | 3.0 | 2.0 | 2.0 | 2.0 | 9.00, stops | 10.00 |
| Control: Forward | 3 | 3.3 | 3.0 | 3.0 | 2.0 | 11.33 | 11.67 |
| Control: Vorelios | 3 | 4.0 | 2.3 | 3.3 | 1.7 | 11.33 | 11.00 |
| Control: Perit.AI (unchanged, all clean) | 3 | 4.0 | 2.3 | 3.3 | 2.0 | 11.67 | 11.67 |

Commissioning's 6 clean judges are 1 from the original round plus 5 new ones.

**Reading the numbers:**
- **Commissioning** clears the bar by 0.57. The sd of a 6-judge mean is about 0.33, so that is roughly 1.7 sd. It is the strongest candidate on clean scores. Verdicts: 2 BACK, 4 PASS.
- **Credit disputes** clears the bar by 0.07. That is well inside the noise (the sd of a 5-judge mean is about 0.36), so treat it as a tie with the bar, not a pass. Verdicts: 1 BACK, 4 PASS.
- **Truck warranty** drops to 9.0 and stays stopped.
- **Correction to the audit.** The audit estimated that reading METHOD added about a point. Against clean re-scores of the same paragraphs, the effect was smaller: about +0.25 on commissioning, +0.67 on Forward, +0.67 on Vorelios and +1.5 on truck. The direction held and the size varied. Commissioning's lead survived.

## Commissioning: what the clean judges said

**Strongest version.** Five of the six clean judges reached the same version the contaminated judges did:
- an independent agent hired by the owner;
- only the last two test levels (functional and integrated) on liquid-cooled halls;
- for neoclouds and second-tier developers, not hyperscalers;
- live grading merging building, power, cooling-unit and load-bank data, with a signed report the same day or within 48 hours;
- a fee per MW plus a schedule bonus or fee at risk.

One clean judge (A) disagreed: sell to the general contractor's side, which carries late-delivery penalties and doesn't need independence. The customer question is open.

**Consistent findings:**
- Script writing is already sold with AI: Facility Grid (under 2 minutes versus 4 to 8 hours), CxPlanner, Bluerithm. CxAlloy/OTTO and AutoCXI automate functional tests from BMS trends. Nobody sells live grading of the integrated test with sign-off.
- A senior agent still has to witness on site, so leverage is about 1.5 to 2 times, not "several."
- CBRE names power and equipment, not commissioning, as the delivery risk.
- Commissioning services firms sell cheaply (CYMCOR about $30M). Vertiv bought PurgeRite for about $1B, which moves an equipment maker into liquid-cooling services.

**Fastest test (the judges agree):**
- Get 3 to 5 recent liquid-cooled integrated-test logs.
- Split the lost days into agent-bound time (analysis, write-up, waiting on the agent) and physical fixes.
- Kill it if agent-bound time is under about 15% of test days, or under about a week.
- Alongside that, send priced proposals to 10 to 15 neocloud and developer leads. Kill it if fewer than 2 or 3 sign a pilot or a letter of intent.

## Credit disputes: what the clean judges said

**Strongest version:**
- Narrow to debt buyers and large collectors first. They lack the original paperwork, which is Hinkle v. Midland exposure.
- Make it the investigation file of record: an e-OSCAR API middleware vendor with a verify, correct or delete recommendation tied to cited documents.
- Screen credit-repair direct disputes under Reg V 1022.43, which lets them be dismissed as frivolous.
- Handle validation requests under the debt collection rules.
- Sell through FCRA defense firms or as an add-on to collection software.

**Consistent findings:**
- About 5.1M of the 5.8M credit-reporting complaints target the three bureaus, not this buyer. Complaints against creditors and collectors were about 302K to 387K.
- The CFPB added portal friction in February and June 2026.
- Deleting the entry is the near-free default.
- Incumbents sit on both sides: Provana/Sonnet (intake plus a 7-year investigation record), Bridgeforce (AI Resolution Engine in pilot), e-OSCAR's own API, and collection software (C&R, Finvi, Latitude).
- The market ceiling is about $100M to low hundreds of millions.

**Fastest test:**
- Ask 10 compliance heads for their all-in cost per dispute, delete rate, FCRA suits and suit cost.
- Offer a paid pilot at $1.50 to $2 per dispute.
- Kill it if the median cost is under $1 to $2, most firms delete more than half of disputes, or fewer than 2 or 3 sign.

## Status

Commissioning is the stronger candidate on clean scores. Disputes ties the bar. Neither has any customer evidence. The deciding facts for both are in the first 10 calls.
