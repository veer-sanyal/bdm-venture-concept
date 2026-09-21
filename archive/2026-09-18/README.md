# Burton D. Morgan Venture Concept Competition 2026

Working repo for the team (Veer + Cole). Chosen concept: **Supplier Quality Chargeback Defense**
(`CONCEPT.md`). Everything here is the method that produced it, the evidence behind it, every
candidate that was tried and why it died, and the raw research returns.

## The competition

| Date | What |
|---|---|
| Thu Sep 24, 7-8pm | Workshop 1 of six (Thursdays: Sep 24, Oct 8, Oct 22, Nov 5, Nov 19, Dec 3) |
| **Sun Sep 27, 11:59pm** | **Preliminary concept submission.** Explicitly unassessed: a name and a paragraph suffice |
| Between | 1-2 required virtual office hours, four short assignments via Brightspace at milestones |
| **Fri Dec 11, 10am-2pm** | **Final event at the HIVE, in person, mandatory** |

- Purdue Daniels / HIVE, 38th annual. Lead: Prof. Kostas Grigoriou, kgrigori@purdue.edu.
- Open to all Purdue students, solo or team. Ineligible if the concept has taken more than $10,000
  in funding, generated more than $5,000 in revenue, or rests on Purdue-owned IP.
- $100,000 pool across two tracks (assigned after submissions close), equal per track: $10,000 /
  $7,000 / $5,000 for the top three, plus seven $3,000 "You need to build this!" awards. About 25
  teams receive awards. Winners get a paid San Francisco trip; the top ten get Venture X2 admission.
- Concept submission form: https://airtable.com/appbOLgMKkZ9qAMxR/pagddradTeIElFEUK/form
- Workshop and info-session signup: https://airtable.com/appbOLgMKkZ9qAMxR/pagVc2UdZlTJ3Orgw/form

## What matters now

The calls. The bar before Dec 11 is 3 supplier calls, 3 redacted closed cases, 1 advisor and 1 paid
pilot yes; `CALL-GUIDE.md` has the questions. Desk research is done.

## Read in this order

1. `METHOD.md`. The process: the order to think in, the kill ladder, the demand ladder,
   how to dispatch a blind screen, how the search ends. Read it before generating or judging
   any idea, including a brand-new one.
2. `STATE.md`. What is alive, what is dead and why, what the judging room rewards, and the
   do-not-cite list. The ranked board is the section to start from.
3. `CASEBOOK.md`. The evidence behind every rule in METHOD. Each rule carries a `[C-n]`
   anchor; the matching entry here holds the origin story and the quotes. Open on demand.
4. `CALL-GUIDE.md`. Who to call for each live candidate and the numbered questions. The
   calls are worth more to the December score than any further desk research.

Detail files (`INSPECTION-PASS.md`, `CANDIDATES-AI-NATIVE.md`, `LTL-DISPUTE.md`, etc.) hold
the evidence for individual candidates. `screens/` holds verbatim blind-screen returns.
`predictions/` holds the main session's pre-dispatch predictions and their scoring; screening
agents must never be pointed at it.

## Using it with Claude

Claude Code: open this folder and start with "Read METHOD.md in full, then STATE.md. Then
[generate five candidates in lane X / screen candidate Y blind / re-score the board]."

Claude.ai: create a Project, upload the top-level files and `screens/` as knowledge, and
start every conversation with the same instruction.

Three rules that matter more than the rest, all in METHOD Part 0 and Part 7:

- The agent that generates an idea never screens it. Screening prompts carry the asset, the
  mistake, the customer and the ladder, and nothing about where you think it will die.
- Write your prediction (where it dies, at what rung, how confident) BEFORE dispatching the
  screen, and keep it in `predictions/`, never in `STATE.md`. Run
  `sh tools/venture-blind-check.sh STATE.md` before any screen.
- Quote the instrument, not the summary: the statute, the contract clause, the price list,
  the vendor's own page. A claim without a quoted source is not evidence.

## Working in this repo

This repo is the working copy from 2026-09-17 on. Edit here, commit with a real message, and say
in the commit which file's facts changed. `STATE.md` is the one place for live decisions; every
other file points at it.
