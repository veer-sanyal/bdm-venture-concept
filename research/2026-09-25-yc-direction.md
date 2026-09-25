# Where YC is heading, and why our loops keep missing it (2026-09-25)

Desk research only. This is not customer validation. It uses three sources:
- The batch classification of all four 2026 YC batches, from a separate session (branch `claude/vc-backed-company-patterns-sqlq8o`, `research/2026-09-25-funded-patterns/`, which also holds the breakouts and non-YC round reports).
- YC's live Requests for Startups page, fetched today.
- This repo's own score ledger.

## What our loops produced

All nine candidates judged since 9/24 sit in one lane: paperwork for a regulated back office.
- Credit-dispute responses
- Arc-flash studies
- Medicaid applications (twice)
- Environmental permits
- Supplier warranty chargebacks
- Wage-and-hour audits
- Tariff metal-content proof
- AI review certification

Every seed since loop 2 has pointed generators at "work businesses already pay people to do by hand", and generators read that as clerical recovery and compliance work. Across loops 2 to 4, three of every six merged ideas repeated earlier rounds (Medicaid, change orders, dealer warranty, customs).

## What YC funded in 2026 (counts from the classification CSVs)

| Batch | Size | Physical | Sells to AI builders | AI-native service | Densest shapes |
|---|---|---|---|---|---|
| Winter 2026 | 199 | 34 | 33 | 20 | AI infra; picks and shovels; licensed professional work (four law firms); small-clinic admin |
| Spring 2026 | 193 | 32 | 24 | 20 | Agent picks and shovels (~22); a third of the batch sells to, secures or hosts agents; robotics data |
| Summer 2026 | 230 | 74 | 50 | 28 | AI firms selling finished work (28); lab data and RL environments (18); single-job robots (10); defense (9) |
| Fall 2026 | 90 so far | 28 | 18 | 13 | Always-on computers for agents (6); inference clouds (6); data-center buildout (6); autonomous factories (5); personal AI and consumer devices (6) |

**Fall 2026 has no healthcare providers or payers, no legal filings, no tax, and no government software.** The back-office lane we keep generating in was the Winter/Summer crowd. It is thinning in the newest batch.

## What YC is asking for now (Requests for Startups, Fall 2026, fetched 2026-09-25)

The Primer (adaptive tutoring) · The Future of American Defense · A Cloud for Small Software · Multiplayer AI · Compute at Sea · AI-Powered Consumer Products for 1 Billion People · AI for the Aging Population · New Operating Systems for the Physical World · The Best Time to Build in Crypto · Data for the Real World · Proving You're Human · AI-Native Compliance Infrastructure · Self-Maintaining APIs.

Only one of the 13 (compliance infrastructure) is in our lane. The rest fall in three groups:
- **The agent economy:** Cloud for Small Software, Multiplayer AI, Self-Maintaining APIs, Proving You're Human, plus the Fall batch's agent computers, inference clouds and lab data.
- **The physical world:** Operating Systems for the Physical World, Data for the Real World, Defense, Compute at Sea, plus the batch's data-center buildout and autonomous factories.
- **People:** The Primer, Consumer Products for 1 Billion People, AI for the Aging Population, plus the batch's personal AI devices.

## Two patterns from the breakout study (same branch, `agents/breakouts.md`)

- **Timing.** Most breakouts launched within about six months of a specific capability jump:
  - long context → EvenUp, Hebbia
  - tool calling → Sierra, Decagon
  - agentic coding → Lovable, Replit Agent
  - real-time voice → ElevenLabs, Vapi
- **Consumer and prosumer grow fastest.** The fastest revenue ramps were card-paid tools for individuals: Lovable, Perplexity, Suno, Wispr, Granola, Manus. The founder scope allows consumer AI with a moat, and no loop has produced one.

## Consequence for loop 5

- **Replace the shared seed with three angles, one per generator: agent economy, physical world, people.** The shared seed is what keeps steering generators into back-office paperwork.
- **Tell every generator plainly that earlier rounds covered regulated back-office paperwork.** Otherwise the web's densest material (W26/S26 coverage) pulls them back into it.
- **Anchor each idea to a capability that became reliable in the last twelve months.**

These changes are in METHOD.md from loop 5, with the reasons.

**Caveats.**
- YC asks name categories, and category names are where the crowd is (see `research/2026-09-21-rfs-channel.md`). The angles are directions to search in, not a list to pick from, and the merge step still runs the crowding check.
- The Fall 2026 batch was 90 companies and still being listed on 9/24.
