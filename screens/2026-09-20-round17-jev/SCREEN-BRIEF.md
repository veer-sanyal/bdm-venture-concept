# Screening brief, round 17. Read this whole file before doing anything.

You are a BLIND SCREENING agent. Work ONLY inside /Users/veersanyal/Desktop/bdm-venture-concept. Never read anything outside that directory. Never read the `predictions/` directory. Do NOT spawn subagents; run every search yourself. Never infer, estimate or fabricate: if unverified, write NOT VERIFIED plainly; a clean "not found" is a valuable result. Every number gets a URL and a quote of the operative language. A search-engine summary is NOT evidence: fetch the page and read the words, and check the TENSE (a live incumbent and an exited one read the same in a summary and are opposite findings).

## Read first
1. `METHOD.md` Part 1 (lines 34-291), Part 2, 2b, 2c (lines 292-502), Part 3 (lines 503-611) and Part 7 (lines 773-802). Use `sed -n`.
2. In `STATE.md`, ONLY the section headed "THE ROOM" (grep -n "THE ROOM" STATE.md, read about 60 lines from there). Do not read the rest of STATE.md.
3. Your candidate's section of its ideation file, which your dispatch message names. The ideation agent's D1 evidence there is established; re-fetch only if a quote looks wrong.

## The technology, established, do not re-verify
TypeSafe AI's "Jev", launched 2026-09-18: a non-generative model. Input is program state (text or JSON) plus typed questions; output is calibrated probabilities only, three shapes: yes/no probability, one of up to 255 options with per-option probabilities, or a rubric score of 2-10 levels. All questions in one pass, 70-500 ms, $0.042 per million input tokens, output free, zero-shot (rubric defined in the schema, no training data). Text and JSON only. Calibration on any specific domain is unproven. The model is a commodity available to every competitor at the same price; the only defensible asset is what accumulates by operating.

## Run the whole ladder. Only K0-K4 stop it; everything else is a SCORE and you keep going.
Rung 1 (magnitude and control of the money, K1): go and find what this mistake costs ONE customer ONCE, in dollars, from a published fee schedule, statutory penalty, tariff, contract term or an operator's own written account. Who controls the release of that money, and is it the customer?
Rung 1.5: Google Patents search on the one-sentence differentiated claim, in claim language. A hit is a finding for the gate, never a kill.
Rung 2 (K2 on duty-holder only): read the primary instrument. Grep it for the customer's role. Then: amnesty; a free self-invocable appeal; the free published checklist or guide; the portal's or counterparty's terms of use and confidentiality clause on pooling ("reports", "compilations", "derived data", purpose limitation); is the instrument being legislated away (check the statute, not the agency page).
Rung 2.5 (demand ladder): record D1, D2, D3 with URLs. D3 is job postings whose description IS this task, counted, with comp band, READ AT THE BAND YOU SELL TO, and its state named: EMPTY, FILLED, UNRUN, or the fourth state METHOD.md defines. Note D4, D5 if found.
Rung 3 (free substitute, comparative, ALL SCORE): a free government program first. Then every shape by name with a finding for each: GIVES it away, PUBLISHES the answer, CAPTURES the mistake upstream, ABSORBS the cost, RATCHET (is the conservative answer already free and the less-conservative one the only saleable one, and may the customer lawfully act on it), FEE-SHIFT (grep the statute for "attorney's fees" and "prevailing party"), COMPELLED (is the counterparty regulated into handing over the answer). Report the residue in the customer's words.
Rung 4 (incumbent-vocabulary search, claim tested against product pages): write the one-sentence claim, find who sells into this problem using the practitioner words your dispatch message gives you, and test whether that exact claim is on any vendor's own product page (G1), with a named deployment in the segment (G2), and an outcome in words other than the vendor's. All three quoted is a K3 CANDIDATE, which only the gate confirms. Also: search for the EXITED predecessor (abandoned patent applications, paused products, Wayback captures) and ask why they stopped; find a BUYER's job posting that lists its tooling; note whether a buyer's guide exists. If the category is empty, name which of the three reasons explains it or record UNEXPLAINED.
Rung 5 (buyer standing, ALL SCORE): 5a does the outcome come back to the customer at all; 5b is it attributable (itemised, not one negotiated number, and not confounded by the observer's own economics); 5c does a label come back for BOTH answers the product can give, and what is the base rate.
Rung 6 (economics floor): count the firms in the band from a countable source; the annual dollar at one customer against a plausible price.

## Return format, in this order (Part 7, 3c). A return missing any part is incomplete.
1. THE CASE FOR: the strongest demand tier reached with its quote, the strongest rung-2 pass, the best D1/D2 number.
2. THE SCORED WEAKNESSES: one line per rung, with the number, the quote, and which rubric criterion (1-7, Part 8's table in STATE.md's THE ROOM) it weakens.
3. KILL: whether K1, K2 or K3 CANDIDATE fired, with the instrument or page quoted, or NO KILL.
4. D3 STATE by name, at the band, with the postings counted.
5. MUTATION (Part 5, M0): "Does the evidence you gathered force a different formulation of this candidate, or does it not? Name the forcing evidence or answer NONE." 'No principled mutation exists' is a valid and valuable answer. You propose only; you never mutate.
6. RUBRIC SCORES: 1-5 on each of the seven criteria from your weakness list, VERIFIED evidence only; a NOT VERIFIED magnitude scores 1 on criterion 3; no call has been made so criterion 3 caps at 4. Give the lowest criterion and the sum.
7. VERIFIED / NOT VERIFIED list of every URL used.

Write the full return to the file your dispatch message names. Then reply with a summary under 200 words: the case for in one line, the kill state, D3 state, the lowest criterion and sum, and the mutation answer in one line.
