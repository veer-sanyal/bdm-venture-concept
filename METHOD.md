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

1. **Generate.** Run three generators in parallel, each in a fresh context with the same prompt. They don't see the archive, past verdicts or each other.
2. **Merge.** The orchestrator folds duplicates together. Then it checks the archive for repeats. An old kill is evidence, not a ban.
3. **Shape.** The shaper builds the strongest companies it can from what the generators returned.
4. **Judge blind, with controls.** The orchestrator writes each candidate as a paragraph of about 130 words: problem, customer, product, how it makes money. No names, no team. It then adds three recent YC companies written the same way, drawn at random from the latest batch. A fresh judge scores each paragraph without knowing which ones are ours.
5. **Read against the controls.** A candidate advances if its rubric total matches or beats the mean of the YC controls in the same round.
   - Do not decide on the BACK/PASS line; the judge passes nearly everything.
   - Read what each judge named as the killer and the fastest test. Those are the outputs worth acting on.
6. **Team fit, separately.** For each candidate that advances, one agent answers the team-fit prompt below.
7. **Customers decide.** Desk research ranks the candidates. Customer calls settle which one wins. Every advancing candidate leaves with the one test the judge named.

## Prompts (what agents actually get)

**Generator**
> [Founder brief.] [Seed, if any.] Find the best startup you can for them. Use the web as much as you want, and don't read local project files. Come back with your best idea, any runners-up worth keeping, why each could work, and what's weakest about it.

(The local-files clause was added 2026-09-24. In the first run, one generator followed the repo's own instructions and read STATE.md and the old concept before generating.)

**Shaper**
> [Founder brief.] Independent generators produced these ideas: [merged file]. Build the strongest one to three companies you can from them. Keep, combine, reshape or replace. Research whatever you need.

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

## Rules for the orchestrator
- Add nothing to these prompts beyond the brief, the seed and the material being judged. A new constraint goes into this file first, with the reason for it.
- Desk research is never customer validation. State that on every write-up.
- Live decisions go in STATE.md.
