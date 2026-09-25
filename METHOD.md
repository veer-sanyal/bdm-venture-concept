# METHOD

Adopted 2026-09-24. Replaces the archived method (`archive/2026-09-24/METHOD.md`).

## Why it changed

On 2026-09-24 we ran the old "try hard to break it" prompt blind on eight randomly drawn YC Fall 2026 companies. It passed two of eight. The kills had three things in common:
- The mere existence of funded competitors counted as fatal.
- The team was judged together with the idea.
- The verdict went on the pitch as written, even when the judge had already described a narrower version that works.

This method removes all three and anchors the bar to companies investors actually funded.

That same day the new judge was validated on those eight companies plus one of our own ideas. It backed one of the eight YC companies, fewer than the old prompt's two. A judge that researches with the web finds an incumbent almost every time, so its BACK/PASS line is close to always PASS. The useful signal is the rubric score relative to the YC controls. Totals ranged from 9 to 12 out of 20, and the YC mean was 10.75. Full results: `research/2026-09-24-judge-validation.md`.

## Founder brief (edit freely; every generator gets it)

> Veer and Cole are Purdue undergrads who want to build a real company and pitch it at Purdue's Burton D. Morgan Venture Concept Competition, which VCs judge on customer need, value over alternatives, market size and risk. They want scalable software, AI-native, that can start narrow and grow broad.

## Seed and angles (edit freely; every generator gets both after the brief)

From loop 5 (2026-09-25, Veer), every generator gets the same seed and a different angle.

Seed:

> Earlier rounds kept landing on paperwork for regulated back offices: claims, eligibility applications, audits, compliance filings and recoveries. Look elsewhere. Anchor the idea to something AI could not do reliably twelve months ago, and pick a market that can grow past a billion dollars a year.

Angles, one per generator:
- **Generator 1, the agent economy:** "Start from the companies and developers now building and running AI agents. Find a job they pay for, or soon will, that exists because agents now do real work: running them, testing them, supplying their data, securing them, handling what they spend, or proving who is human."
- **Generator 2, the physical world:** "Start from physical work: construction, maintenance, field service, manufacturing, logistics, energy and the data-center buildout. Find a job where AI that can now read drawings, video and sensor data can direct or check the people and machines doing the work, not just file their paperwork."
- **Generator 3, people:** "Start from people rather than businesses: students, workers who buy their own tools, families, older adults and their caregivers. Find something a person would pay for each month from their own card, that gets better with use in a way a general chatbot can't copy: their own data, a network of other users, a device, or a community."

Why (evidence: `research/2026-09-25-yc-direction.md`):
- **Every candidate in four loops was back-office paperwork.** All nine candidates in the ledger sit in that lane, and three of every six merged ideas in loops 2 to 4 repeated earlier rounds. Each labor-spend seed pointed generators there, and loop 4's varied starting clauses did not pull them out.
- **YC has moved on from that lane.** The Fall 2026 batch has no healthcare-provider, payer, legal-filing or tax companies. Twelve of YC's 13 Fall 2026 requests fall into the three angles above.
- **Consumer had never been tried.** The founder scope allows consumer AI with a moat, and no loop had produced one. Card-paid tools for individuals had the fastest revenue ramps among 2022 to 2026 breakouts.
- **The twelve-month anchor** follows the breakout study: most launched within about six months of a specific capability jump.
- **Risk.** YC's asks name crowded categories. The angles set where to search, not what to pick, and the merge step still checks for crowding and archive repeats.

The labor-spend seed used in loops 2 to 4 is kept in the history below.

Seed history (one line per round: seed, what it moved):
- Loop 1 (2026-09-24): no seed. Candidates tied the controls on need, value and risk and trailed on market (2.05 vs 2.70).
- Loop 2 (2026-09-25): "…billions of dollars a year. Enter through the narrowest slice of that work where no software company already holds the customer's data or buying channel." Market rose to 2.67. Need fell to 3.0, because the unowned slice was small plants whose typical fine was about $1,400, so the buyer had no urgency. The loop 3 seed kept the labor-spend half and asked for a costly, frequent failure instead of the narrowest slice.
- Loop 3 (2026-09-25): "…billions of dollars a year. Enter through the slice of that work where a mistake or a delay costs the buyer the most money, and often, and where no software company already holds the customer's data or buying channel." Two of three generators converged on long-term-care Medicaid applications. The caseworker version scored 11.67 (need 4, market 3) and advanced, the first seeded candidate to hold both need and market. The same seed also surfaced supplier warranty chargebacks (9.67, market 2). Value was now the weak score: every judge who marked it down named a cheap or free alternative the buyer already had (family-paid eligibility firms, MedicaidSoft, Reap). The seed also pulled all three generators toward claims, recovery and paperwork lanes, and two of five picks were archive repeats. The current seed adds "out of their own budget", requires naming what the buyer already uses (service firms and startups included), and asks for something AI can do that those can't. It drops the software-company clause, which the new sentence covers more strictly.
- Loop 4 (2026-09-25): the current seed, with generators varied by starting point (below). Value held (wage-and-hour checks before payroll scored 2.8), but market fell to 2 for both candidates, as in loop 2. "A slice where AI can do something those can't" led to narrow gaps: California healthcare employers, and a thin band of products near the 15% metal line. Nothing advanced (wage-and-hour 10.80 against a 10.92 bar; metal content 9.33). Loop 4's seed text: "Aim at work that tens of thousands of businesses pay for today out of their own budget, their own staff or an outside firm, so that the spend AI would replace adds up to billions of dollars a year. Enter through the slice where a mistake or a delay costs the buyer the most money, and often. Before settling on it, name what that buyer already uses, including startups and service firms that charge the buyer nothing, and choose a slice where AI can do something those can't, not just do the same job cheaper." Replaced for loop 5 by the seed and angles above.

## The loop

1. **Generate.** Run three generators in parallel, each in a fresh context with the generator prompt below. From loop 5 each gets the shared seed and its own angle (see Seed and angles). They don't see the archive, past verdicts or each other. Nothing else runs while they work (why: see Ordering below).
2. **Merge.** The orchestrator folds duplicates together. Then it checks the archive for repeats. An old kill is evidence, not a ban. The merged file may carry that evidence, written as "an earlier round found…" with no file paths or scores, so the shaper weighs the finding without going to read the archive.
3. **Shape.** The shaper builds the strongest companies it can from what the generators returned.
4. **Judge blind, with controls.** The orchestrator writes each candidate as a paragraph of about 130 words: problem, customer, product, how it makes money. No names, no team. Before judging, check every number in a candidate paragraph against the primary source it came from, and say what it measures (loop 2 sent a permit-application fee to the judges as an annual compliance cost; a judge caught it). Save all paragraphs exactly as judged to `research/<date>-<round>/paragraphs.md`. Three fresh judges score each paragraph. Judges run only in this step, never during generation or shaping.
   - **The control bank is frozen from loop 5** (2026-09-25, Veer): 19 YC controls, bar 10.92. No new controls are drawn each loop.
   - **Why:** over loops 2 to 4 the bar moved 10.93, 10.96, 10.92. The standard error of a bar built from 19 controls is 0.24, and three more controls cut it only to about 0.22. They cost 9 judge runs a loop, more than the candidates' own 6.
   - **Re-open the bank** (draw 3 new controls the old way: unbanked B2B companies from the latest YC batch, a recorded random seed, `agents/controls-draw.md`, 3 judges each, run alongside the candidates' judges) when any of these happens:
     - the judge prompt changes;
     - the model serving judges changes;
     - four loops pass without a re-anchor;
     - a candidate lands within 0.5 of the bar and the judges' conditions differ visibly from the bank's, for example searches running out.
   - Judges still don't know which paragraphs are ours when controls run alongside. With no controls in a loop, they still see one paragraph each and no bar. A paragraph's score is the mean of its judges. Any paragraph whose mean lands within 0.5 of the bar gets two more judges before the decision (why: see Judge noise below).
5. **Record and read against the controls.** Add one row per judged paragraph to `scores.csv` (the four rubric scores and the verdict; the total is computed), then run `python3 tools/scores.py`. A candidate advances if its mean total is at or above the mean of every YC control ever banked (all rounds, each averaged over its judges). Ties count (Veer, 2026-09-24). A control scored under a known flaw gets kind `excluded` and stays out of the bar; Tire Swing's validation score is excluded because its judge counted Tire Swing itself as a competitor. The script prints each round's standings and the per-parameter averages for controls and candidates across all rounds.
   - Do not decide on the BACK/PASS line; the judge passes nearly everything.
   - Read what each judge named as the killer and the fastest test. Those are the outputs worth acting on.
6. **Team fit, separately.** For each candidate that advances, one agent answers the team-fit prompt below.
7. **Customers decide.** Desk research ranks the candidates. Customer calls settle which one wins. Every advancing candidate leaves with the one test the judge named.

## Prompts (what agents actually get)

**Generator**
> [Founder brief.] [Seed.] [This generator's angle.] Find the best startup you can for them. Use the web as much as you want, and don't read local project files. Come back with your best idea, any runners-up worth keeping, why each could work, and what's weakest about it.

(The local-files clause was added 2026-09-24. In the first run, one generator followed the repo's own instructions and read STATE.md and the old concept before generating.)

Loop 4 alone used a different variation. Every generator got the same seed, and the sentence "Find the best startup you can for them" gained a starting point:
- generator 1: none (the plain prompt);
- generator 2: ", starting from what buyers themselves complain about or pay outside firms to fix";
- generator 3: ", starting from what AI can do reliably now that it couldn't two years ago".

Generators 1 and 3 still converged on the same idea. The angles replaced these clauses from loop 5.

**Shaper**
> [Founder brief.] Independent generators produced these ideas: [merged file]. Build the strongest one to three companies you can from them. Keep, combine, reshape or replace. Research whatever you need on the web, and don't read local project files.

**Judge** (one fresh agent per paragraph, blind)
> You're an experienced early-stage investor. Here is a startup concept: [paragraph]. Research it properly on the web, and don't read local project files: check its key claims against primary sources and find who else serves this customer. Then:
> 1. Describe the strongest version of this company. Narrow or reshape it if that helps.
> 2. Rate that version 1 to 5 on customer need, value over what customers use today, market size, and risk (5 means low risk). Give one line of evidence for each.
> 3. Say what would kill it and name the single fastest test that would tell us.
>
> Competition alone is not a reason to pass. Say whether an incumbent already owns this customer's data or buying channel. If you find a company whose pitch matches this one almost exactly, treat it as this team, not a competitor. Judge the idea, not the team. End with exactly "VERDICT: BACK" or "VERDICT: PASS".

(The matching-company sentence was added 2026-09-24. Without it, the judge found a YC control's own company and scored it as the leading competitor.)

(The local-files clauses in the shaper and judge prompts were added 2026-09-25. The repo's AGENTS.md routes every agent to METHOD.md and STATE.md. In loop 2 the shaper read the bar and loop 1's scores, dropped an idea because it had "scored 10.0 last round", and predicted its own score against the bar. Two judges opened METHOD.md; it names no candidates, but STATE.md does, and a judge that reads it is no longer blind.)

**Team fit** (advancing candidates only)
> Two Purdue undergrads want to build this: [paragraph plus judge's strongest version]. What would they need to win it (skills, access, credentials, first customers), and how could they get it within a semester?

## Judge noise (measured 2026-09-24)

Four paragraphs were each scored by four independent judges using the identical prompt. One judge's total varies with a standard deviation of about 0.75 points (range up to 2 points on one paragraph). Need and market barely move across judges. Value and risk move because each judge finds different competitors (for example, only one of four arc flash judges found 70Ez and AmpSketch). With one judge, averaging flipped a decision: arc flash went from 11 (advances) to a mean of 10.5 (stops). Three judges bring the standard deviation of the mean to about 0.43, enough to separate a one-point gap in most cases. Near the bar that isn't enough, which is why a close paragraph gets five. `tools/scores.py` recomputes the noise figure every run. If it rises above 1.0, raise the default count. After loop 3 (14 paragraphs with repeat judges) it was 0.87, so a 3-judge mean has a standard deviation of about 0.50.

## Ordering (measured 2026-09-25)

In loop 2, nine control judges ran alongside the three generators. Two generators reported that their web searches ran out after a few queries, so their competitor lists were thin. The candidate judges, which ran alone later, made 36 to 48 tool calls each. Web search is shared across the session's parallel agents. Run the stages in order: generators, then the shaper, then all judges (candidates and controls together). Never overlap generating or shaping with judging.

In loop 3 all 15 judges ran at once, and 10 of them reported running out of web searches partway, including 5 of the 6 candidate judges. So run judges in batches of at most 6 at a time, with one judge per paragraph in each batch (candidates and any re-anchor controls alike), so every paragraph is judged under the same conditions. Loop 4 ran three batches of 5 this way, and no judge ran out. When a judge says its searches ran out, note it in the round's RESULT.md.

Judges share the session's scratchpad. In loop 4, two judges read PDF extracts another judge had left there. Both were public documents, so no blindness was lost. Still, clear the scratchpad of judge files between batches, and note any reuse in RESULT.md.

## Rules for the orchestrator
- Add nothing to these prompts beyond the brief, the seed and the material being judged. A new constraint goes into this file first, with the reason for it.
- Save every agent's final report to `research/<date>-<round>/agents/<role>-<paragraph>-<n>.md` the day it runs, verbatim (copy it from the agent's transcript, don't retype it). Scores go in `scores.csv`; the reasoning behind them lives in these files. The session's temporary task files are deleted when the session ends.
- Desk research is never customer validation. State that on every write-up.
- Live decisions go in STATE.md.
