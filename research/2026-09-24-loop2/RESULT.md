# Loop 2 under the leaner METHOD, 2026-09-24/25 (Jev seed)

Desk research only. This is not customer validation.

**Setup.**
- Three generators ran with the founder brief plus a Jev seed (`seed.md`, written from `agents/jev-research.md`).
- The merge produced nine ideas (`merged.md`), and each got its own shaper.
- Paragraphs were judged one judge at a time against the growing control bank.
- Three new controls were drawn at random from 491 AI-related 2026 YC companies (`controls-pool.md`).
- Loop 1's two leftovers each got their one reshape.
- Every paragraph is saved word for word in `paragraphs.md`, and every agent report is in `agents/`.

## Result: nothing advances

The bar is 10.78 ± 0.30 SE, the mean of 13 controls. The new controls sit exactly on the old mean (drift +0.00), and judge noise is 0.68.

| Paragraph | Mean | Judges | Outcome |
|---|---|---|---|
| Kita (control) | 11.33 | 3 | control |
| ByteAsk (control) | 11.33 | 3 | control |
| Vela (control) | 9.67 | 3 | control |
| LTC Medicaid lookback desk (reshape of loop 1) | 10.20 | 5 | stops; no second reshape |
| Arc flash drift monitor (reshape of loop 1) | 10.00 | 3 | stops; no second reshape |
| Pre-release child-safety testing for chatbots (SB 1119) | 9.50 | 2 | stops; 1.28 below, too far for a reshape |
| Marketplace leakage recovery | 9.00 | 1 | stops |
| Compliance gate for AI voice agents | 9.00 | 1 | stops |
| Reshoring leads for job shops | 9.00 | 2 | stops |
| Plain-English scam rules, backtested | 9.00 | 1 | stops |
| Bounded characters for children's products (SB 867) | 9.00 | 1 | stops |
| Independent controls for refund-issuing AI agents | 8.00 | 1 | stops |
| Ad matching for AI apps; reliability layer for Jev users | n/a | 0 | the shaper found no strong company, or no specific customer |

**Two leftover `+judge` flags are moot.**
- Loop 1's Medicaid original was superseded by its reshape.
- The reshaped arc flash stands at 10, 10, 10. Noise rose from 0.64 to 0.68, which widened the band to 0.785 against a gap of 0.78. A fourth judge would need 13.1 or more to reach the bar.

**Standings across both loops.**
- Credit-dispute response (11.2, loop 1) is still the only candidate above the bar, and it is a close call.
- The 13-control mean (10.78) and the loop-1 bar are unchanged.

## What the loop found

1. **Convergence came from the law, not from Jev.**
   - All three generators independently picked a per-turn safety layer for consumer chatbots.
   - Its shaper then found NOPE already selling that product at the same price, $0.0001 per call, and OpenAI giving away a teen safety policy pack.
   - The surviving reshape was SB 1119 pre-release testing. Its judges found three problems:
     - companies can write the assessment in-house;
     - the outside audit waits until 2032 for companies under $500M revenue;
     - the free KORA benchmark and Common Sense's institute already cover most of it.
2. **Jev was not the edge in any surviving company.**
   - Six of the nine shapers made Jev optional or dropped it. Their reasons were three:
     - TypeSafe's telemetry and no-distillation terms, and the lack of an SLA;
     - open models priced within about 2x of Jev;
     - tasks that are numeric or run in batch.
   - Veer, 2026-09-24: open-source Jev replicas exist, so the TypeSafe contract is a supplier choice, not a design constraint. The model is a commodity, and the moat has to be data, evidence, workflow or distribution.
3. **The stop rules held.**
   - The loop spent 28 judge runs: 9 on controls, 10 on loop 1 carry-overs (2 more on the Medicaid original, 5 on its reshape, 3 on the arc flash reshape), and 9 on the new ideas.
   - Five ideas stopped after one judge.
   - The two loop 1 ideas hit both caps: at most 5 judges per paragraph and one reshape.

## Kept for later (from judges and founder discussion)

- **SB 1119's mandatory incident channel as a source of labels (Veer and orchestrator).** A product that hosts the required public incident intake and three-year record-keeping sees real failures across customers. That gives labels competitors lack and a regression library that grows over time. It was not judged.
- **Multi-check grading for crisis detection.** Split the judgment into small questions, shuffle and reword each question, use several different models, and escalate if any check fires. This reduces random error but not systematic role-play bias. Clinician-labelled hard cases are still required.
- **Fastest tests the judges named for the ideas closest to the bar.**
  - Child-safety: a $15,000 "Adam's Law pre-assessment" offered to about 20 school-AI and teen mental-health companies. Kill the idea if fewer than 3 sign.
  - Reshoring: a hand-run pilot with 10 metal shops. Kill it at under 5 quote requests per 200 pitches.
