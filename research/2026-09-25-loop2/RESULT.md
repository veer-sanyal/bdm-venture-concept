# Loop 2, 2026-09-25 (labor-line seed)

Desk research only. This is not customer validation.

**Nothing advances.** Bar: 11.01, the mean of the 13 banked YC controls, including this round's three.

| Paragraph | Need | Value | Market | Risk | Total | n |
|---|---|---|---|---|---|---|
| Control: Kailash Labs (small video models) | 3.0 | 3.0 | 4.0 | 2.0 | 12.00 | 3 |
| Control: Definite (finance data layer for agents) | 4.0 | 2.0 | 4.0 | 2.0 | 12.00 | 3 |
| Control: Maritime (managed cloud for agents) | 3.7 | 2.0 | 3.7 | 2.0 | 11.33 | 3 |
| **Outsourced quality paperwork for small auto suppliers** | 3.3 | 2.7 | 2.0 | 2.0 | **10.00** | 3 |
| **Sales and use tax recovery for manufacturers** | 3.0 | 2.3 | 2.0 | 2.0 | **9.33** | 3 |

Neither candidate came within 0.5 of the bar, so neither got extra judges. All 16 verdicts were PASS.

## How the round ran
1. **Generate.** Three generators ran with the founder brief plus the labor-line seed: *"Look for work that businesses now pay people or an outside firm to do, where AI can now do most of it and the pay behind that work is large. Say whose pay or which firm's fee it replaces."* Generators 1 and 3 each picked sales and use tax recovery for Indiana manufacturers independently. Generator 2 picked an AI quality engineer for auto and aerospace suppliers, with tax recovery as its runner-up.
2. **Merge.** Result in `merged.md`. The archive holds evidence against both leads: the reverse audit was killed on economics, and supplier quality documentation was "survives-narrowed". Both were passed to the shaper as evidence.
3. **Shape.** One shaper (`agents/shaper.md`) returned tax recovery as the lead and a monthly "outsourced quality department" as the backup. It dropped claims audits, standalone property tax appeals, premium audits and environmental filings.
4. **Funded-clone check.** This was the first run of the new METHOD step 4 (`paragraphs.md`).
   - Tax recovery is adjacent to Arthiva, an AI-native ERP with a recovery module.
   - Quality paperwork is adjacent to GroundControl (YC Spring 2025), which sells software for first-article and PPAP paperwork, aimed at aerospace. The paragraph was limited to the shaper's own test market, small auto shops, so it would not match GroundControl's pitch.
   - Neither was a clone.
5. **Judge.** Five blind paragraphs, three judges each. Controls were drawn at random from YC F26 B2B (`agents/controls-draw.md`).
   - One quality judge read METHOD.md and STATE.md before judging, which broke blindness because STATE.md names our PPAP work. Its 11 is banked as `excluded`, and a replacement judge scored 10.
   - The judge prompt now carries the local-files clause (METHOD, 2026-09-25).
   - Fixing this exposed a bug in `tools/scores.py`: excluded judges were averaged into their paragraph's mean before being dropped. It is now fixed and has a regression check. No earlier round was affected.

## What the judges said
- **Tax recovery.** All three judges contradicted the core premise that mid-size plants get skipped.
  - TaxMatrix publishes Indiana wins for small plants ($118K for a machine shop, $172K, $1.1M) on success-only fees and pays for the utility studies itself.
  - Avalara AvaTax for AP already sells the recurring invoice check and certificate management.
  - The state requires a "description of how items are used", and a 2024 ruling needed photos and videos. So the plant-use map needs plant knowledge, not only invoices.
  - Market: 1,270 Indiana manufacturing firms have 50–999 employees (Census 2022 SUSB, per one judge). The fee pool is about $40M, mostly one-time.
  - Strongest version: an AI-run recovery firm, white-labelled through regional CPA firms and PE operating partners, across the states where buyers claim directly.
  - Fastest test: a free 36-month AP scan for 10–40 Indiana controllers. Kill if fewer than 3–5 hand over data, or if the median refund excluding utilities is under $40–75K.
- **Quality paperwork.**
  - The need is real and mandated: Ford and Flex-N-Gate flow PPAP down to sub-tier suppliers, and containment is due in 24 hours.
  - But AI drafting is already cheap: QualityEngineer.ai at $49–249 per seat, IATF Solutions at €39 a report, and 1factory, whose case is 168 PPAPs in seven months with one person.
  - What $3,000 a month buys is a quality engineer's time, which makes it a services business.
  - Market: about 3,700–3,900 US IATF sites, falling. Shops that submit many packages hire a quality engineer (Indiana listings pay $70–105K), and shops without one submit few.
  - Strongest version (all three judges): lead with 8D complaint responses, price per job plus a small retainer, and widen to aerospace first-article reports and medical.
  - Fastest test: ask 10–30 Indiana Tier-2/3 shops for their 12-month package and complaint counts, and offer the next one for a $1,500 deposit. Kill if the median is under 8–10 a year, or if fewer than 3 pay.

## What this round says about the method
- **The seed did not fix the market score.** Both candidates scored market 2.0, the same as loop 1's candidates. The controls averaged 3.7–4.0. The generators did name a labor line, as asked. But the brief's "Purdue undergrads" plus a Purdue MEP channel pulled all three generators to Indiana manufacturers, and the judges then sized the Indiana wedge ("Indiana is a few hundred shops"). The shaper kept the Indiana start.
- **The controls that scored market 4 are horizontal or platform plays** (a finance data layer, agent infrastructure, video models) with a proven adjacent budget (BlackLine $700M, Modal $4.65B). Our candidates were narrow services with a local start.
- **Both leads had an incumbent service firm already in the "underserved" segment** (TaxMatrix; consultants and cheap AI tools). This is the archive's process lesson again: search in the incumbent's own vocabulary before claiming a gap. The generators and the shaper did not do that search.
