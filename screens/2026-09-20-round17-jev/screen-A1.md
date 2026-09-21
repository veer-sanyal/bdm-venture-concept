# Screen A1, Candidate 1: Export-Control Enforcement-Risk Score

Blind screen, round 17. Ladder run per METHOD.md Part 3 (kill/score split). No subagents used;
all searches run directly. Search-engine summaries are marked as such and never carried forward as
findings; only directly-fetched page text is treated as VERIFIED.

---

## 1. THE CASE FOR

**D1, VERIFIED, already established by ideation and reconfirmed here by direct fetch of
https://www.bis.gov/enforcement/penalties**: *"As of January 15, 2025, the maximum administrative
monetary penalty is $374,474 per violation or twice the value of the transaction, whichever is
greater."* Criminal exposure on the same page runs to 20 years imprisonment and $1,000,000 per
violation under the Export Control Reform Act. This is the strongest number on the board for this
candidate and it clears the Part 2b carve-out on its own: **D1 ($374,474+) is an order of magnitude
larger than one customer's annual compliance-labor cost** (Glassdoor: Export Compliance Specialist
average $92,301/yr, https://www.glassdoor.com/Salaries/export-compliance-specialist-salary-SRCH_KO0,28.htm),
so even if D3 turns out empty at the target band, rung 2.5's own rule says magnitude alone can still
clear it.

**Strongest rung-2 pass, duty-holder confirmed on the primary instrument, quoted directly (Cornell LII,
15 CFR 758.1(e)):** *"The person who transmits the EEI to the AES, whether exporter (U.S. principal
party in interest) or agent, is responsible for the truth, accuracy, and completeness of the EEI,"* and
758.1(g) requires that filer to report the ECCN and license authority. **The customer segment (the
exporter) is unambiguously the duty-holder, the instrument does not land on a counterparty.** K2 does
not fire.

**Best comparative finding on rung 4:** an incumbent-vocabulary search across the actual trade-compliance
software category (Descartes Visual Compliance, e2open, KYG Trade, Info-X, SAP GTS/Oracle GTM
integrations) found nobody making the candidate's exact claim. The closest adjacent claim, fetched
directly (not a summary), Descartes AI Assist, https://www.descartes.com/resources/knowledge-center/descartes-ai-assist-advantage-60-fewer-false-positives-denied-party
,  quotes *"Reduce screening false positives by 60%,"* which is a risk-score claim about **restricted-party
name-match confidence**, not about predicting whether a shipment will draw an AES hold or a BIS
enforcement inquiry. No vendor page names a segment deployment or an enforcement-outcome result. **No K3
candidate; the capability gap this candidate claims is real as far as the desk can see.**

---

## 2. THE SCORED WEAKNESSES

- **Rung 1 / criterion 3, magnitude verified, but the D3 seat check cuts against the segment as
  defined.** The candidate's own segment definition explicitly excludes companies with "a dedicated
  export-compliance officer." Job-board data (ZipRecruiter/Glassdoor, title-level only, every major
  board 403s on fetch per the known toolchain limit) shows the Export Compliance
  Specialist/Analyst/Trade-Compliance seat is real and well-paid ($70k–$155k/yr), but the visible
  postings skew toward large, already-staffed exporters (aerospace/defense primes), not the 50-500
  employee band this candidate targets. Per Casebook: "seat funding scales with headcount... a D3 result
  read at large firms does NOT transfer downward." **The candidate is, by its own definition, aiming at
  the population most likely to score D3 EMPTY**, weakens criterion 1 (is this really a distinct,
  nameable population) and criterion 3.
- **Rung 2.5 / criterion 3, D2 not independently verified.** A search-engine summary reported export
  compliance consulting at "$150-400/hour," but no single firm's page was fetched and quoted, so this is
  NOT VERIFIED, not a confirmed D2. Only D1 is solid.
- **Rung 3, RATCHET shape / criterion 5, the heaviest weakness found.** BIS's own free classification
  channel (SNAP-R commodity classification request, and the free Interactive Commerce Control List,
  https://www.bis.gov/regulations/ear/interactive-commerce-control-list) already lets any exporter get
  the conservative answer (classify high, seek a license) for zero cost. The product's only
  differentiated, sellable output is the *less*-conservative one, "this shipment is low-risk, ship
  without escalation", and given the instrument's own stated stakes (up to $374,474 or 2x transaction
  value, up to 20 years imprisonment, per https://www.bis.gov/enforcement/penalties), **no compliance
  officer can act on a probability score instead of a license determination.** This is the same pattern
  METHOD.md calls out under Sabre/Textura: *"Agreeing with the free guidance is free; disagreeing with it
  is unusable. The saleable half is the half you cannot sell."* Weakens criterion 5 directly.
- **Rung 5c / criterion 5, censored label on the branch that matters.** If the model flags a shipment
  high-risk and the customer responds conservatively (delays, gets a license, or declines the sale), the
  customer never observes what would have happened had it shipped, so the model only ever gets a graded
  outcome on the branch it called safe. Combined with the base-rate problem (the overwhelming majority of
  shipments clear without incident, BIS enforcement actions are comparatively rare events against
  hundreds of thousands of small exporters, per Census's 270,014 small/medium exporter count, "A profile
  of U.S. importing and exporting companies," https://www.census.gov/foreign-trade/Press-Release/edb/edbrel2022.pdf
  and successor releases), most signal is "nothing happened," which is exactly the base-rate trap METHOD.md
  flags on cargo-theft prediction. Weakens criterion 5.
- **Frequency/severity tension / criterion 7.** The frequent, cheap-to-observe outcome (an AES fatal/hold
  code, returned near-instantly) carries little money. The outcome that carries the real dollar figure (a
  BIS Office of Export Enforcement inquiry or penalty) is rare and lagged, often years after the
  shipment, which is the same "the more consequential the checker, the less often it acts" tension
  METHOD.md names in Part 1. A cold-start ledger at one company will see very few of the labels that
  actually matter for years. Weakens criterion 5 and criterion 7 (buildability/cold start).
- **Rung 4 / criterion 4, adjacent vocabulary is already crowded.** "AI risk scoring," "predictive
  compliance alerts," and "red-flag detection" are already standard marketing language in this category
  (Descartes AI Assist, Info-X, https://infox.com/blog/aes-filing-explained, quoted: *"AI identifies
  potential red flags before they trigger audits"*). None of these name the exact enforcement-outcome
  claim, but a judging room will need the distinction between "risk-aware screening" (existing) and
  "learns from this company's own downstream BIS outcomes" (claimed) explained carefully. Weakens
  criterion 4 modestly.
- **Rung 6 / criterion 6, no segment-specific count.** The only countable figure found is Census's
  270,014 small/medium (<500 employee) U.S. exporters overall, which is not narrowed to
  dual-use-goods self-classifiers without a compliance officer. No published count exists for that exact
  intersection. Weakens criterion 6.
- **Contamination note, not a weakness on the candidate but a caution for future screens on this lane:**
  several "trade compliance software pricing" results (gingercontrol.com, tradecompliancesoftware.org)
  read like the dev.to decoys STATE.md already flags, oddly specific, SEO-shaped posts with confident
  numbers and no visible authorship or methodology. None of their figures are cited above as VERIFIED;
  flagging for the main session in case another lane's screen is tempted to use them.

---

## 3. KILL

**NO KILL.** K1 does not fit this candidate's shape cleanly (the "mistake" is a penalty owed *by* the
customer, not money a counterparty is withholding *from* the customer, so "who controls release of the
money" does not map the way it does on a recovery-shaped candidate) and the magnitude clears any plausible
floor regardless. K2 does not fire, 15 CFR 758.1(e)/(g), quoted above, puts the exporter/USPPI squarely
as the duty-holder. K3 does not fire, no vendor's own page states the exact claim (G1), names a
deployment in this segment (G2), and shows the mistake solved there (outcome) together; Descartes AI
Assist is the closest and is confirmed by direct fetch to be about screening-alert false positives, not
enforcement-outcome prediction.

---

## 4. D3 STATE

**UNRUN AT BAND**, not EMPTY and not FILLED. The seat (Export Compliance Specialist/Analyst) clearly
exists and is funded in the exporter population generally, at $70k–$155k/yr (ZipRecruiter, Glassdoor , 
title-level aggregates only; every major job board 403s on direct fetch, a known toolchain limit, not a
finding about the world). But the visible postings skew toward larger, already-staffed exporters, and the
candidate's own segment definition (50-500 employees, "without a dedicated export-compliance officer")
targets exactly the band those postings do not cover. Per Casebook's headcount corollary, this makes a
true EMPTY at the target band *more* likely, not less, but it was not verified either way at that band.

---

## 5. MUTATION

**NONE, no principled mutation exists from the evidence gathered.** The two heaviest weaknesses found
(RATCHET at rung 3, the censored-label problem at rung 5c) are properties of the instrument and of what a
rational compliance officer can act on given $374,474-and-20-years stakes, not properties of how the
five-tuple (customer, asset, document set, mistake, checker) is worded, no rewording of the candidate
changes what BIS penalizes or what a compliance officer is willing to act on without a real license
determination. One lead is worth naming but NOT proposing as a tested mutation: narrowing the customer
to companies already under a BIS Consent Agreement or with an open compliance-monitoring obligation
would raise the frequency of graded outcomes (they get audited on a schedule) and could resolve the
frequency/severity tension, but that changes who pays in a way METHOD.md's M5b treats as a different
company, not a reformulation of this one, and it has not been searched or tested.

---

## 6. RUBRIC SCORES

Scored 1-5 per STATE.md → THE ROOM / METHOD.md Part 8, VERIFIED evidence only. No customer call was run
(none was in scope for a blind desk screen), so criterion 3 is capped at 4 per Part 8's own rule.

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Clarity of target customer | 3 | Segment is specifically described (band, product category, monthly export cadence, no compliance officer) but not backed by a countable figure for that exact intersection |
| 2 | Clarity of JTBD | 3 | One clear sentence, but not sourced to a practitioner's own words, no call, no forum quote |
| 3 | Significance and magnitude of unmet need | 3 | D1 verified and large; D2 unconfirmed at page; D3 unresolved at the actual target band; no salience call (caps below 4 regardless) |
| 4 | Differentiation and uniqueness | 3 | No K3, real apparent capability gap, but adjacent "AI risk scoring" vocabulary is already commonplace in the category |
| 5 | Performance improvement over existing solutions | 2 | No measured number; the RATCHET and 5c findings suggest the sellable half of the output may not be actionable at all, which caps any performance claim before a demo exists |
| 6 | Size of market opportunity | 2 | Only a broad, unnarrowed exporter count (270,014) is available; no segment-specific figure |
| 7 | Market/technical/execution risk | 2 | RATCHET, censored labels, and a rare/lagged severe-outcome ceiling on cold start together make this a hard build to de-risk before revenue |

**Lowest criterion: 2 (tied on 5, 6, 7). Sum: 18.**

---

## 7. VERIFIED / NOT VERIFIED

**VERIFIED (fetched and read directly):**
- https://www.bis.gov/enforcement/penalties, max penalty $374,474 / 2x transaction value; criminal exposure
- https://www.law.cornell.edu/cfr/text/15/764.5, voluntary self-disclosure is a mitigating factor at OEE's discretion, no fixed percentage cap; senior-management-authorization requirement
- https://www.law.cornell.edu/cfr/text/15/758.1, EEI filer (USPPI/exporter or agent) responsible for accuracy; must report ECCN and license authority
- https://www.bis.gov/regulations/ear/interactive-commerce-control-list, free CCL/ECCN lookup tool, no predictive/enforcement-risk claim
- https://www.visualcompliance.com/compliance-solutions/export-classification/eccn-classification/, Descartes ECCN classification page, no enforcement-risk prediction claim
- https://www.e2open.com/global-trade/export-management/, no enforcement-risk prediction claim
- https://www.kygtrade.com/solutions/by-role/export-compliance, no enforcement-risk prediction claim, one unnamed customer quote only
- https://infox.com/blog/aes-filing-explained, "AI identifies potential red flags before they trigger audits," vague, no outcome or segment named
- https://www.descartes.com/resources/knowledge-center/descartes-ai-assist-advantage-60-fewer-false-positives-denied-party, "Reduce screening false positives by 60%," about restricted-party name-match confidence, not enforcement-outcome prediction; no named segment/customer
- https://www.bis.gov/freight-forward-guidance, best-practices/red-flag narrative guidance, no standalone free checklist template
- https://www.census.gov/foreign-trade/Press-Release/edb/edbrel2022.pdf and https://www.census.gov/foreign-trade/Press-Release/edb/2023prelimprofile.pdf, 270,014 small/medium (<500 employee) U.S. exporters, 2023, 97.2% of identified exporters
- https://www.glassdoor.com/Salaries/export-compliance-specialist-salary-SRCH_KO0,28.htm, Export Compliance Specialist average $92,301/yr

**NOT VERIFIED (search-engine summary only, page not independently fetched/quoted, or no primary source found):**
- Export compliance consulting rate "$150-400/hour", summary only, no firm's page fetched
- Trade-compliance software SMB pricing "$5K-$50K/year", traced to gingercontrol.com / tradecompliancesoftware.org, treated as suspect contamination (dev.to-decoy-shaped), not cited as a finding
- Exited/paused predecessor product specifically attempting enforcement-risk prediction for exporters, none found
- Buyer's own job posting naming specific trade-compliance tooling in this exact segment, not found in the time budget
- Google Patents claim search, no granted claim found reading directly on this candidate's claim language in the time budget; treat as NOT VERIFIED rather than a clean absence
- D3 comp band read at the specific 50-500-employee, no-dedicated-officer band, job boards 403 on direct fetch (known toolchain limit); title-level aggregates only
