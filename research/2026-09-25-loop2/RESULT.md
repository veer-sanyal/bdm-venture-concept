# Loop 2 under the active METHOD, 2026-09-25

Desk research only. This is not customer validation.

## The seed and why

Across all rounds before this one, our candidates matched the YC controls on need (3.75 vs 3.77), value (2.35 vs 2.33) and risk (2.05 vs 1.98), and lost almost entirely on market (2.05 vs 2.70). Every judge's market line said the same thing: our ideas served a few hundred buyers at a modest price. Controls scored 3 or 4 on market when they drew on a large existing budget, usually labor (Hickory's compliance labor, Sona8's consulting, Grep's research work).

So the seed aimed generators at that gap without naming past verdicts:

> aim at work that tens of thousands of businesses already pay people to do by hand, their own staff or an outside firm, so that the spend AI would replace adds up to billions of dollars a year. Enter through the narrowest slice of that work where no software company already holds the customer's data or buying channel.

## What happened

- **Generate.** Three generators, seeded, web only. Two of the three independently chose the same best idea: environmental compliance for small manufacturers, starting with air permits. The third chose Medicaid long-term-care applications, a repeat of loop 1's candidate, which had stopped at 10.0.
- **Merge.** `merged.md`. Archive check: a September 7 kill of a related environmental idea (an EPA ECHO inspection predictor) is carried as evidence. Every state runs a free small-business environmental assistance program, and EPA waives penalties for small businesses that self-disclose.
- **Shape.** The shaper returned one company, an AI-run environmental department for small permitted plants. It dropped the rest: Medicaid (already scored), cost reports (costreporting.ai exists), and property tax, CAM and tax-credit audits (crowded). It ran EPA's ICIS-Air data and found Indiana an outlier: 30% of synthetic-minor plants had a formal enforcement action in five years.
- **Judge.** Three random new YC F26 controls (`agents/controls-draw.md`) and the one candidate, three blind judges each.

| Paragraph | Need | Value | Market | Risk | Mean total | n |
|---|---|---|---|---|---|---|
| Control: Perit.AI (practitioner-recorded training data) | 4.0 | 2.7 | 3.7 | 2.0 | 12.33 | 3 |
| Control: Vorelios (engineering physics foundation model) | 4.0 | 2.0 | 3.3 | 2.0 | 11.33 | 3 |
| Control: Forward (private credit origination) | 3.3 | 2.3 | 3.0 | 2.0 | 10.67 | 3 |
| **AI environmental department for small permitted plants** | 3.0 | 2.7 | 2.7 | 2.0 | **10.33** | 3 |

The bar is now 10.93, the mean of 13 banked controls. The candidate is 0.60 below it, outside the 0.5 band that calls for two more judges, so **it stops.** Nothing advances this round, so no team-fit agent ran.

## What the judges found

Judge totals were 11, 11 and 9. All three passed it.

- **Enforcement.** Two judges re-ran EPA's data and confirmed Indiana at 28 to 29%. The national rate is about 7%, and Ohio and Michigan are at 2 to 3%. Only New Jersey, California and a few others are close.
- **Penalties are small.** The median Indiana penalty is $1,400 to $5,000, many settle at $500, and the expected fine avoided is under $1,000 a year per plant. Fear of fines cannot carry a $6,000 to $12,000 price.
- **One claim in our paragraph was misquoted.** Judge 2 found that the $1,500 to $20,000 consultant figure is RMA Green's fee for a permit *application*, not annual compliance. The same source puts annual emission inventories at $0 to $5,000. Judge 3 found RMA's pricing page quoting $4,000 to $20,000 a year for permit-plus-reporting support. What small plants actually spend today is unknown. Correcting the claim would not help the idea; it makes the value case weaker.
- **Market, the parameter the seed aimed at.** Air alone is about $45M to $245M nationally, and Indiana is about $2M to $5.6M. It only reaches venture scale if the bundle works: air plus Tier II, stormwater, spill plans and hazardous waste at $15,000 to $20,000 a plant.
- **Competitors.**
  - Software: AirComply (launched 2 Sept 2026, reads permits, drafts 20+ report types, reseller pricing for consultants), RegPermit, Encamp Scout, and Mapistry at about $300 to $500 per location per year, which anchors prices far below ours.
  - Services: U.S. Compliance (2,200+ clients, "compliance as a service") and KPA (about 10,000 small clients).
  - Free: coating distributors hand out emissions tools, and IDEM's CTAP gives free help.
  - No one owns the plant's data. The local consultant owns the relationship, and all three judges named it as the channel: resell to consultants or buy their client books.
- **Strongest version (all three converged).** A fixed-fee, engineer-reviewed service that files everything, not just air, for independent single-site plants in the high-enforcement states. Sell from the public list of recently cited plants.
- **Fastest test (all three converged).** Pull the roughly 176 Indiana synthetic-minor plants with a recent formal action from ECHO, keep the independent single-site owners, and call 30 to 100 of them. Offer to take over their air filings for $500 to $750 a month, and ask what they pay today. Kill it if fewer than 3 in 30 (or 5 in 100) sign a paid pilot, or if typical current spend is under $3,000 to $4,000 a year.

## What the seed did

The seed moved market: 2.67 here, against a 2.05 average for every earlier candidate. It cost need, though: 3.0 here, against 3.75 before. That's because the seed's "narrowest slice nobody owns" landed on small plants whose penalties are too small to create urgency. The total ended close to the earlier candidates' average. A next seed should keep the large-labor-budget half and replace "narrowest slice nobody owns" with a slice where the buyer faces a large, frequent cost for getting it wrong.

## Process notes

- **Search budget.** Generators 1 and 3 said their web searches ran out after a few queries, probably from contention with the nine control judges running at the same time; the orchestrator's own search still worked afterwards. Their competitor lists are thin. The candidate judges were not starved (36 to 48 tool calls each). Next time, run control judges after the generators finish, not alongside them.
- **Repo reads by agents.** The repo's AGENTS.md tells every agent to read METHOD.md and STATE.md.
  - The shaper read repo state (it cites loop 1's 10.0 score, the 10.93 bar and the archive). METHOD's shaper prompt does not forbid local files, so this is within the rules. Still, the shaper knew the bar.
  - Two judges (Perit 3 and air-permit 1) opened METHOD.md. It names no candidates, so blindness held.
  - Proposed METHOD change, not applied: add the generator's "don't read local project files" clause to the shaper and judge prompts.
- **Control identity.** Perit judge 1 matched the pitch to Datoric (YC S26) rather than Perit, and treated Datoric as the team. No competitor penalty resulted.
- **Paragraph accuracy.** The candidate paragraph carried the shaper's misquoted consultant-fee range. The orchestrator checked the IDEM fee but not that one.

Files: `paragraphs.md` (all four paragraphs as judged), `merged.md`, and `agents/` (3 generators, the shaper and 12 judges, saved verbatim).
