# METHOD

Adopted 2026-09-24. Replaces the archived method (`archive/2026-09-24/METHOD.md`).

## Why it changed

On 2026-09-24 we ran the old "try hard to break it" prompt blind on eight randomly drawn YC Fall 2026 companies. It passed two of eight. The kills had three things in common:
- The mere existence of funded competitors counted as fatal.
- The team was judged together with the idea.
- The verdict went on the pitch as written, even when the judge had already described a narrower version that works.

This method removes all three and anchors the bar to companies investors actually funded.

That same day the new judge was validated on those eight companies plus one of our own ideas. It backed one of the eight YC companies, fewer than the old prompt's two. A judge that researches with the web finds an incumbent almost every time, so its BACK/PASS line is close to always PASS. The useful signal is the rubric score relative to the YC controls. Totals ranged from 9 to 12 out of 20, and the YC mean was 10.75. Full results: `research/2026-09-24-judge-validation.md`.

## Founder brief (edit freely)

**Full brief** (shapers; the team-fit prompt carries its own framing):
> Veer and Cole are Purdue undergrads who want to build a real company and pitch it at Purdue's Burton D. Morgan Venture Concept Competition, which VCs judge on customer need, value over alternatives, market size and risk. They want scalable software, AI-native, that can start narrow and grow broad.

**Generator brief** (generators only):
> Veer and Cole want to build a real company and pitch it at a venture competition that VCs judge on customer need, value over alternatives, market size and risk. They want scalable software, AI-native, that can start narrow and grow broad.

Why the generators get a copy without Purdue (Veer, 2026-09-25): in loop 2 all three generators went to Indiana manufacturers reached through Purdue's extension program. The judges then sized the Indiana wedge and scored both candidates 2 on market. Where the founders can reach customers is a team-fit question, and team fit is still judged separately (step 7).

## The loop

1. **Generate.** Run three generators in parallel, each in a fresh context with the same prompt. They don't see the archive, past verdicts or each other.
2. **Merge.** The orchestrator folds duplicates together. Then it checks the archive for repeats. An old kill is evidence, not a ban.
3. **Shape, one shaper per idea.** Each distinct idea in the merged file gets its own shaper, running in parallel in a fresh context. An idea counts if at least one generator put it forward as its best idea or a runner-up; ideas the generators themselves dropped get no shaper. Each shaper returns one company. After shaping, the orchestrator folds any two shaped companies that converged on the same customer and job. Why (Veer, 2026-09-25): a single shaper over the whole file ranks the ideas and gives the runners-up a thin look. In loop 2 it built one lead and one backup from six ideas.
4. **Check for funded clones.** Before anything goes to a judge, the orchestrator checks each shaped candidate against funded companies. It runs `python3 tools/yc_overlap.py <terms>` over the last four YC batches and one web search on the candidate's one-liner. A clone is a funded company selling the same job to the same customer. It is dropped and recorded with its neighbor. An adjacent company (a different customer or a different job) stays, and the neighbor is noted in the write-up, never in the paragraph. Why (Veer, 2026-09-25): the judge prompt treats a matching company as this team, so a clone would borrow that company's traction in its score. Also, the recent batches hold many near-duplicates (`research/2026-09-25-funded-patterns.md`).
5. **Judge blind, with controls.** The orchestrator writes each candidate as a paragraph of about 130 words: problem, customer, product, how it makes money. No names, no team. It then adds three recent YC companies written the same way, drawn at random from the latest batch. Three fresh judges score each paragraph, each without knowing which ones are ours. A paragraph's score is the mean of its judges. Any paragraph whose mean lands within 0.5 of the bar gets two more judges before the decision (why: see Judge noise below).
6. **Record and read against the controls.** Add one row per judged paragraph to `scores.csv` (the four rubric scores and the verdict; the total is computed), then run `python3 tools/scores.py`. A candidate advances if its mean total is at or above the mean of every YC control ever banked (all rounds, each averaged over its judges). Ties count (Veer, 2026-09-24). A control scored under a known flaw gets kind `excluded` and stays out of the bar; Tire Swing's validation score is excluded because its judge counted Tire Swing itself as a competitor. The script prints each round's standings and the per-parameter averages for controls and candidates across all rounds.
   - Do not decide on the BACK/PASS line; the judge passes nearly everything.
   - Read what each judge named as the killer and the fastest test. Those are the outputs worth acting on.
7. **Team fit, separately.** For each candidate that advances, one agent answers the team-fit prompt below.
8. **Customers decide.** Desk research ranks the candidates. Customer calls settle which one wins. Every advancing candidate leaves with the one test the judge named.

## Prompts (what agents actually get)

**Generator**
> [Generator brief.] [Seed, if any.] Find the best startup you can for them. Use the web as much as you want, and don't read local project files. Come back with your best idea, any runners-up worth keeping, why each could work, and what's weakest about it.

(The local-files clause was added 2026-09-24. In the first run, one generator followed the repo's own instructions and read STATE.md and the old concept before generating.)

**Shaper** (one per idea)
> [Full founder brief.] Independent generators produced this idea: [the idea's entry from the merged file, with its archive note]. Build the strongest company you can from it. Narrow, reshape or replace it if that makes a stronger company. Use the web as much as you want, and don't read local project files.

(Changed 2026-09-25 from one shaper over the whole merged file, which built "one to three companies" from it. The local-files clause matches the generator and judge prompts.)

**Judge** (one fresh agent per paragraph, blind)
> You're an experienced early-stage investor. Here is a startup concept: [paragraph]. Research it properly with the web, and don't read local project files: check its key claims against primary sources and find who else serves this customer. Then:
> 1. Describe the strongest version of this company. Narrow or reshape it if that helps.
> 2. Rate that version 1 to 5 on customer need, value over what customers use today, market size, and risk (5 means low risk). Give one line of evidence for each.
> 3. Say what would kill it and name the single fastest test that would tell us.
>
> Competition alone is not a reason to pass. Say whether an incumbent already owns this customer's data or buying channel. If you find a company whose pitch matches this one almost exactly, treat it as this team, not a competitor. Judge the idea, not the team. End with exactly "VERDICT: BACK" or "VERDICT: PASS".

(The local-files clause was added 2026-09-25. In loop 2, one of the quality-paperwork judges followed the repo's AGENTS.md and read METHOD.md and STATE.md before judging. STATE.md names our earlier PPAP work, so that judge was not blind, and its score is banked as `excluded`. Two control judges read METHOD.md only, and they are kept.)

(The matching-company sentence was added 2026-09-24. Without it, the judge found a YC control's own company and scored it as the leading competitor.)

**Team fit** (advancing candidates only)
> Two Purdue undergrads want to build this: [paragraph plus judge's strongest version]. What would they need to win it (skills, access, credentials, first customers), and how could they get it within a semester?

## Judge noise (measured 2026-09-24)

Four paragraphs were each scored by four independent judges using the identical prompt. One judge's total varies with a standard deviation of about 0.75 points (range up to 2 points on one paragraph). Need and market barely move across judges. Value and risk move because each judge finds different competitors (for example, only one of four arc flash judges found 70Ez and AmpSketch). With one judge, averaging flipped a decision: arc flash went from 11 (advances) to a mean of 10.5 (stops). Three judges bring the standard deviation of the mean to about 0.43, enough to separate a one-point gap in most cases. Near the bar that isn't enough, which is why a close paragraph gets five. `tools/scores.py` recomputes the noise figure every run. If it rises above 1.0, raise the default count.

## Rules for the orchestrator
- Add nothing to these prompts beyond the brief, the seed and the material being judged. A new constraint goes into this file first, with the reason for it.
- Save every agent's final report to `research/<date>-<round>/agents/<role>-<paragraph>-<n>.md` the day it runs. Scores go in `scores.csv`; the reasoning behind them lives in these files. The session's temporary task files are deleted when the session ends.
- Desk research is never customer validation. State that on every write-up.
- Live decisions go in STATE.md.
