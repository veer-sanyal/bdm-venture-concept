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

## The loop

The leaner loop was adopted 2026-09-24 (Veer). It changed three things. Each idea now gets its own shaper, because loop 1's single shaper stalled while managing its own research subagents. Controls now accumulate in a growing bank instead of being drawn fresh as three per loop. Every judge sees only one paragraph, so blindness doesn't need controls sitting in the same round, and every banked score stays in the bar. Judges are now added one at a time until the score is clearly on one side of the bar, because a fixed count spends judges where the answer was already clear. The estimate was about 2 to 2.5M tokens per loop, down from 4.1M; it has not been measured yet. Scoring anchors for the rubric were considered and declined (Veer, 2026-09-24): accurate anchors are hard to write, and more judges already reduce the noise. The same evening Veer asked that the bank keep growing: every loop adds three new AI-related 2026 YC companies, so the bar and the noise figures stay current and drift in the judges shows up.

1. **Generate.** Run three generators in parallel, each in a fresh context with the same prompt. They don't see the archive, past verdicts or each other.
2. **Merge.** The orchestrator folds duplicates together. Then it checks the archive for repeats. An old kill is evidence, not a ban.
3. **Shape, one shaper per idea.** Every idea that a generator put forward as its best or as a runner-up gets its own shaper, run in parallel. An idea that a generator itself dropped is not shaped. A shaper returns one company or says plainly that no strong company is there.
4. **Judge blind, one judge at a time.** The orchestrator writes each shaped company as a paragraph of about 130 words: problem, customer, product, how it makes money. No names, no team. Each judge is a fresh agent that sees one paragraph and does not know whether it is ours or a funded company. A paragraph starts with one judge. Add another while the paragraph's mean is closer to the bar than 2s/√n, where n is the judges so far and s is the pooled single-judge sd printed by `tools/scores.py` (0.67 on 9/24, so the band is 1.34, 0.95, 0.77, 0.67, 0.60 for n = 1 to 5). Stop at five. Paragraphs are judged in parallel with each other. `tools/scores.py` marks the paragraphs that need another judge.
5. **Record and read against the growing control bank.** Add one row per judge to `scores.csv` (the four rubric scores and the verdict; the total is computed), then run `python3 tools/scores.py`. A candidate advances if its mean total is at or above the bar. The bar is the mean of every YC control in the bank, each averaged over its judges. Ties count (Veer, 2026-09-24). Every loop adds three new controls to the bank (see Controls below). The bar, its standard error, the judge noise s and the step-4 band are all recomputed from the whole bank on every run. A control scored under a known flaw gets kind `excluded` and stays out of the bar; Tire Swing's validation score is excluded because its judge counted Tire Swing itself as a competitor. The script prints each round's standings and the per-parameter averages for controls and candidates across all rounds.
   - Do not decide on the BACK/PASS line; the judge passes nearly everything.
   - Read what each judge named as the killer and the fastest test. Those are the outputs worth acting on.
6. **One reshape pass for near misses.** A candidate that finishes below the bar by 1.0 or less (one rubric step on one parameter) gets one reshape. A fresh shaper gets the paragraph and every judge's strongest version, killer and fastest test. What it returns is judged as a new paragraph by fresh judges under step 4. It never gets a second reshape. The original keeps its scores; the reshape is recorded as a new paragraph with "(reshaped)" in its name.
7. **Team fit, separately.** For each candidate that advances, one agent answers the team-fit prompt below.
8. **Customers decide.** Desk research ranks the candidates. Customer calls settle which one wins. Every advancing candidate leaves with the one test the judge named.

## Controls (every loop)

- **Pool.** YC companies from any 2026 batch whose directory tags or one-liner make AI central to the product and that are not already in the bank. The orchestrator saves the pool list to `research/<date>-<round>/controls-pool.md`.
- **Draw.** Three at random: `random.sample(pool, 3)` with the seed recorded next to the pool. No hand-picking.
- **Write.** The orchestrator writes each one from its public YC description as a paragraph in the same form as ours: about 130 words, no name, no team.
- **Judge.** Three judges each, with the same prompt as the candidates, run in parallel with the candidates' judges. Controls don't use the sequential rule because nothing is decided about them. Their three judges also feed the noise estimate s.
- **Read.** `tools/scores.py` prints the bar with its standard error (the spread of control means over √k), and each round's new controls against the rest of the bank. If a round's controls differ from the rest by more than twice the combined standard error, the judges may have drifted: Veer decides whether to switch to a recent-window bar. A candidate whose distance from the bar is smaller than the combined uncertainty (2·√(s²/n + SE²)) is marked a close call. The advance rule does not change.
- The first ten controls (validation and loop 1) stay in the bank as they are. Seven of them have one judge; new controls are a better use of judge runs than topping those up.

## Prompts (what agents actually get)

**Generator**
> [Founder brief.] [Seed, if any.] Find the best startup you can for them. Use the web as much as you want, and don't read local project files. Come back with your best idea, any runners-up worth keeping, why each could work, and what's weakest about it.

(The local-files clause was added 2026-09-24. In the first run, one generator followed the repo's own instructions and read STATE.md and the old concept before generating.)

**Shaper** (one per idea)
> [Founder brief.] An independent generator proposed this idea: [the idea's entry from the merged file]. Build the strongest company you can from it. Keep it, reshape it, or say plainly that no strong company is here. Research whatever you need, and don't read local project files.

(The local-files clause matches the generator's, for the same reason. Loop 1's single shaper got the whole merged file and was asked for one to three companies.)

**Reshaper** (near misses only, once)
> [Founder brief.] Independent investors scored this company just below the bar: [paragraph]. Their notes: [each judge's strongest version, what would kill it, and fastest test]. Build the strongest company you can from it. Research whatever you need, and don't read local project files.

**Judge** (one fresh agent per paragraph, blind)
> You're an experienced early-stage investor. Here is a startup concept: [paragraph]. Research it properly: check its key claims against primary sources and find who else serves this customer. Then:
> 1. Describe the strongest version of this company. Narrow or reshape it if that helps.
> 2. Rate that version 1 to 5 on customer need, value over what customers use today, market size, and risk (5 means low risk). Give one line of evidence for each.
> 3. Say what would kill it and name the single fastest test that would tell us.
>
> Competition alone is not a reason to pass. Say whether an incumbent already owns this customer's data or buying channel. If you find a company whose pitch matches this one almost exactly, treat it as this team, not a competitor. Judge the idea, not the team. End with exactly "VERDICT: BACK" or "VERDICT: PASS".

(The matching-company sentence was added 2026-09-24. Without it, the judge found a YC control's own company and scored it as the leading competitor.)

**Team fit** (advancing candidates only)
> Two Purdue undergrads want to build this: [paragraph plus judge's strongest version]. What would they need to win it (skills, access, credentials, first customers), and how could they get it within a semester?

## Judge noise (measured 2026-09-24)

Four paragraphs were each scored by four independent judges using the identical prompt. One judge's total varies with a standard deviation of about 0.75 points (range up to 2 points on one paragraph). Need and market barely move across judges. Value and risk move because each judge finds different competitors (for example, only one of four arc flash judges found 70Ez and AmpSketch). With one judge, averaging flipped a decision: arc flash went from 11 (advances) to a mean of 10.5 (stops). Three judges bring the standard deviation of the mean to about 0.43, enough to separate a one-point gap in most cases. Near the bar that isn't enough, which is why the sequential rule in step 4 keeps adding judges up to five. `tools/scores.py` recomputes the noise figure every run, and the band in step 4 follows it.

## Rules for the orchestrator
- Add nothing to these prompts beyond the brief, the seed and the material being judged. A new constraint goes into this file first, with the reason for it.
- Save every agent's final report to `research/<date>-<round>/agents/<role>-<paragraph>-<n>.md` the day it runs. Scores go in `scores.csv`; the reasoning behind them lives in these files. The session's temporary task files are deleted when the session ends.
- Desk research is never customer validation. State that on every write-up.
- Live decisions go in STATE.md.
