# Predictions: second pass on chargeback frequency and size

Written 2026-09-12 BEFORE dispatch. Pass 1 (`screens/2026-09-12-market-size/B-frequency-and-dollars.md`)
searched manuals, surveys, forums and vendor blogs and found no count and no all-in figure. Pass 2 aims at
sources where numbers leak rather than get published.

## Lane 1: courts, bankruptcy, small-cap SEC filings
- At least one court opinion or docket with a dollar figure for a quality chargeback or setoff between a
  supplier and an automotive customer (70%). Amounts will skew large ($100k+), because small ones never
  reach court.
- A bankrupt Tier-2 (claims register or first-day declaration) shows customer setoffs or quality claims
  in dollars (50%).
- A small public supplier 10-K quantifies customer quality claims or chargebacks in dollars (40%).
- None of these gives a COUNT per year (75%).

## Lane 2: people describing their own work
- Resumes or LinkedIn profiles state chargeback dollars recovered or issued per year (80%), mostly from
  the ISSUER side ("recovered $1M+ from suppliers"), at $250k to $3M per plant per year.
- At least one states a count (chargebacks or claims per month or year) (55%).
- A job posting quantifies volume (35%).
- A thesis or case study with plant-level supplier claim data (40%).

## What this does to the model
- Issuer-side totals divided by supplier count will land between the low and mid columns of
  `MARKET-SIZE.md` per supplier (60%). The market stays small.

---

## SCORED 2026-09-12

| Prediction | Result | Score |
|---|---|---|
| Court record with a dollar figure (70%), skewing $100k+ | ATD v. DaimlerChrysler: $94,000 and $709,971.86; Mando: "several million" | HIT |
| Bankrupt Tier-2 shows setoffs in dollars (50%) | Registers exist, JavaScript-rendered, unread | MISS (access, not absence) |
| Small-cap 10-K quantifies chargebacks (40%) | Core Molding, $179k-$2.34M, mixed categories | HIT |
| No count per year (75%) | None | HIT |
| Resumes state dollars (80%), mostly issuer side | Only template samples | **MISS** |
| A resume states a count (55%) | None | MISS |
| Job posting quantifies volume (35%) | None | correct direction |
| Thesis with plant data (40%) | None | correct direction |
| Issuer totals / suppliers lands low-to-mid (60%) | No issuer total found to divide | UNSCORABLE |

**The confident miss was résumés at 80%.** Real people do not publish these numbers where a fetch can
read them; the dollar-bearing résumés online are generated samples.
