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

## Seed (edit freely; every generator gets it after the brief)

Current seed, adopted 2026-09-25 after loop 2:

> Aim at work that tens of thousands of businesses already pay people to do by hand, their own staff or an outside firm, so that the spend AI would replace adds up to billions of dollars a year. Enter through the slice of that work where a mistake or a delay costs the buyer the most money, and often, and where no software company already holds the customer's data or buying channel.

Seed history (one line per round: seed, what it moved):
- Loop 1 (2026-09-24): no seed. Candidates tied the controls on need, value and risk and trailed on market (2.05 vs 2.70).
- Loop 2 (2026-09-25): "…billions of dollars a year. Enter through the narrowest slice of that work where no software company already holds the customer's data or buying channel." Market rose to 2.67. Need fell to 3.0, because the unowned slice was small plants whose typical fine was about $1,400, so the buyer had no urgency. The current seed keeps the labor-spend half and asks for a costly, frequent failure instead of the narrowest slice.

## The loop

1. **Generate.** Run three generators in parallel, each in a fresh context with the same prompt. They don't see the archive, past verdicts or each other. Nothing else runs while they work (why: see Ordering below).
2. **Merge.** The orchestrator folds duplicates together. Then it checks the archive for repeats. An old kill is evidence, not a ban. The merged file may carry that evidence, written as "an earlier round found…" with no file paths or scores, so the shaper weighs the finding without going to read the archive.
3. **Shape.** The shaper builds the strongest companies it can from what the generators returned.
4. **Judge blind, with controls.** The orchestrator writes each candidate as a paragraph of about 130 words: problem, customer, product, how it makes money. No names, no team. Before judging, check every number in a candidate paragraph against the primary source it came from, and say what it measures (loop 2 sent a permit-application fee to the judges as an annual compliance cost; a judge caught it). It then adds three recent YC companies written the same way, drawn at random from the latest batch: B2B companies not already in the control bank, drawn with a recorded random seed, noted in `agents/controls-draw.md`. Save all paragraphs exactly as judged to `research/<date>-<round>/paragraphs.md`. Three fresh judges score each paragraph, each without knowing which ones are ours. Candidate and control judges run together in this step, never during generation or shaping. A paragraph's score is the mean of its judges. Any paragraph whose mean lands within 0.5 of the bar gets two more judges before the decision (why: see Judge noise below).
5. **Record and read against the controls.** Add one row per judged paragraph to `scores.csv` (the four rubric scores and the verdict; the total is computed), then run `python3 tools/scores.py`. A candidate advances if its mean total is at or above the mean of every YC control ever banked (all rounds, each averaged over its judges). Ties count (Veer, 2026-09-24). A control scored under a known flaw gets kind `excluded` and stays out of the bar; Tire Swing's validation score is excluded because its judge counted Tire Swing itself as a competitor. The script prints each round's standings and the per-parameter averages for controls and candidates across all rounds.
   - Do not decide on the BACK/PASS line; the judge passes nearly everything.
   - Read what each judge named as the killer and the fastest test. Those are the outputs worth acting on.
6. **Team fit, separately.** For each candidate that advances, one agent answers the team-fit prompt below.
7. **Customers decide.** Desk research ranks the candidates. Customer calls settle which one wins. Every advancing candidate leaves with the one test the judge named.

## Prompts (what agents actually get)

**Generator**
> [Founder brief.] [Seed, if any.] Find the best startup you can for them. Use the web as much as you want, and don't read local project files. Come back with your best idea, any runners-up worth keeping, why each could work, and what's weakest about it.

(The local-files clause was added 2026-09-24. In the first run, one generator followed the repo's own instructions and read STATE.md and the old concept before generating.)

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

Four paragraphs were each scored by four independent judges using the identical prompt. One judge's total varies with a standard deviation of about 0.75 points (range up to 2 points on one paragraph). Need and market barely move across judges. Value and risk move because each judge finds different competitors (for example, only one of four arc flash judges found 70Ez and AmpSketch). With one judge, averaging flipped a decision: arc flash went from 11 (advances) to a mean of 10.5 (stops). Three judges bring the standard deviation of the mean to about 0.43, enough to separate a one-point gap in most cases. Near the bar that isn't enough, which is why a close paragraph gets five. `tools/scores.py` recomputes the noise figure every run. If it rises above 1.0, raise the default count. After loop 2 (9 paragraphs with repeat judges) it was 0.86, so a 3-judge mean has a standard deviation of about 0.49.

## Ordering (measured 2026-09-25)

In loop 2, nine control judges ran alongside the three generators. Two generators reported that their web searches ran out after a few queries, so their competitor lists were thin. The candidate judges, which ran alone later, made 36 to 48 tool calls each. Web search is shared across the session's parallel agents. Run the stages in order: generators, then the shaper, then all judges (candidates and controls together). Never overlap generating or shaping with judging.

## Rules for the orchestrator
- Add nothing to these prompts beyond the brief, the seed and the material being judged. A new constraint goes into this file first, with the reason for it.
- Save every agent's final report to `research/<date>-<round>/agents/<role>-<paragraph>-<n>.md` the day it runs, verbatim (copy it from the agent's transcript, don't retype it). Scores go in `scores.csv`; the reasoning behind them lives in these files. The session's temporary task files are deleted when the session ends.
- Desk research is never customer validation. State that on every write-up.
- Live decisions go in STATE.md.
