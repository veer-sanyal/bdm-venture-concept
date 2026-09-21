# Ideation C, Lane: Latency in the Loop

Round 17, 2026-09-20. Technology: TypeSafe AI "Jev" (established facts not re-verified). Lane: decisions
made inside a live human/machine interaction, on text/JSON, that a business is later billed for getting
wrong. Ideation only, no competitor research here.

---

## Candidate 1: Real-Time HTS Entry Line Check

**1. Tuple**
- **Customer segment/band:** independent customs brokerages and in-house import-compliance desks at small
  importers, under 300 staff. Most of the ~13,000 licensed U.S. customs brokers are small firms or sole
  proprietors.
- **Asset:** a private ledger of {entry line-item text (commercial invoice description, proposed HTS
  code) → eventual CBP outcome (accepted at liquidation, CBP Form 29 rate advance, Request for
  Information, penalty)}, built only by operating across many entries for many clients.
- **Document/state input:** the entry line item as text/JSON, commercial invoice description, GRI-narrowed
  candidate HTS subheadings, entry summary fields, exactly at the moment the entry writer keys it, before
  transmission through ABI.
- **The mistake:** misclassifying a line item (wrong HTS heading/subheading), producing either an
  underpayment (penalty exposure) or an overpayment (margin lost, protest cost).
- **Checker and rule:** CBP Import Specialists and Regulatory Audit, acting on the "reasonable care"
  standard in 19 U.S.C. § 1484 and the civil penalty structure of 19 U.S.C. § 1592(c); post-entry review,
  CBP Form 28/29, Focused Assessments, and liquidation (normally ~314 days after entry under 19 U.S.C. §
  1504) are where the classification gets graded.

**2. Differentiated claim (one sentence):** An incumbent would already have to be claiming that its
classification tool scores the probability CBP accepts a specific proposed code against *this broker's own
history of CBP redeterminations*, not just matching product text against the tariff schedule, for this
to be dead.

**3. Question shape and why now:** Choice, the entry writer has already narrowed to a shortlist of
plausible HTS subheadings under GRI analysis, and Jev returns per-option probability of CBP acceptance
before submission. The honest driver is **cost, not raw latency**: a brokerage processes many line items a
day, and checking every single line (not a sample) only becomes economical at near-zero marginal cost;
sub-second return keeps it inside the entry writer's normal per-line workflow rather than becoming a
visible pause. This is not a load-tender-style hard deadline, say so plainly.

**4. Outcome observation:** CBP's own post-entry actions (Form 29, Form 28, liquidation with a duty
adjustment, or a 1592 penalty notice) arrive back to the broker/importer through ACE or physical notice.
The company gets it by tagging each entry's eventual liquidation/audit status inside its own entry-tracking
system and feeding the true outcome back into the ledger, a record the brokerage already receives for
itself but does not currently pool across clients or product lines.

**5. D1, VERIFIED.** 19 U.S.C. § 1592(c), quoted verbatim from the statute: negligence, penalty "not to
exceed" *"two times the lawful duties, taxes, and fees of which the United States is or may be deprived, or
… 20 percent of the dutiable value of the merchandise"*; gross negligence, *"four times the lawful duties,
taxes, and fees … or … 40 percent of the dutiable value"*; fraud, *"an amount not to exceed the domestic
value of the merchandise."* Source: [19 U.S.C. § 1592, FindLaw](https://codes.findlaw.com/us/title-19-customs-duties/19-usc-sect-1592/).
**Frequency: NOT VERIFIED** for a specific per-brokerage entries/year figure. CBP publicly reports more
than 36 million formal entries processed annually against roughly 13,000 licensed brokers, an aggregate
that implies frequent (likely far more than yearly) filing per active brokerage, but that per-customer
number is my own division, not a published statistic, so it is recorded as NOT VERIFIED rather than dressed
up as a measured frequency.

**6. Computed or observed / paperwork or physical act:** Mixed on 1f. The GRI classification logic itself
is largely COMPUTED (rules applied to product text) and does not alone support a private-by-operating
moat. What is genuinely OBSERVED, and what the asset is actually built from, is *whether CBP accepts*
that classification, which depends on CBP's own institutional pattern and cannot be deduced from the
tariff schedule text alone. **Paperwork**, cleanly: if the entry became instant and perfect tomorrow, the
duty/penalty exposure this candidate addresses would in fact disappear, nothing physical has to move for
the money to be real.

**7. Competition fit:** A classification-copilot embedded in the broker's existing ABI-filing software,
monetized as a subscription; the moat is the cross-client, cross-product ledger of {line-item text → CBP
outcome} pairs, which a new entrant cannot buy or replicate without operating entries over time, not a
brokerage's per-entry consulting fee.

**Open flag (Stage 0b):** No contract was found or read between a broker and CBP (regulatory, not
contractual) that would foreclose pooling. The unexamined risk is the broker-importer engagement letter,
which occasionally restricts data reuse, NOT VERIFIED either way; flag for the mutation/screening stage
before further investment.

---

## Candidate 2: Prescription-Entry Look-Alike/Sound-Alike Check

**1. Tuple**
- **Customer segment/band:** independent community pharmacies, under 300 staff (nearly all are single- or
  few-location operations, far under the cap).
- **Asset:** a private ledger of {technician's as-typed entry (drug, strength, sig, quantity, days
  supply) → the source e-prescription text it was transcribed from → downstream outcome (caught and
  corrected at pharmacist verification, reached dispensing, PBM reversal/DUR override, board complaint)}.
  This exists only inside a pharmacy's own verification workflow and is never published.
- **Document/state input:** the incoming e-prescription (NCPDP SCRIPT structured message, text) plus the
  technician's just-typed data-entry fields, compared live before the record reaches the pharmacist's
  verification queue.
- **The mistake:** a transcription error, wrong strength, wrong sig, wrong quantity, or a
  look-alike/sound-alike drug substitution, that reaches dispensing.
- **Checker and rule:** the state Board of Pharmacy, acting on complaint or inspection under the state
  pharmacy practice act (e.g., California Business & Professions Code § 4314 citation authority; 16 CCR §§
  1775–1775.4 govern the citation program), and PBMs on claims audit/recoupment.

**2. Differentiated claim:** An incumbent would already have to be claiming that its verification software
scores each technician entry's deviation-from-source using *this pharmacy's own historical catch/miss
pattern*, not a generic drug-interaction or national-formulary DUR check, for this to be dead.

**3. Question shape and why now:** Score (a 2–10 rubric on how closely the entry matches the source order)
rather than a strict yes/no, because textual mismatches come in degrees (e.g., a strength transposition
reads very differently from a wrong-drug substitution). Sub-second, near-zero-cost matters because a
technician enters dozens to 100+ scripts per shift and the check must resolve before the pharmacist's
verification screen loads, an LLM-priced check run on every field of every entry, all day, every pharmacy,
would not pencil; a fraction-of-a-cent probability check does.

**4. Outcome observation:** the pharmacist's own verification step, does the pharmacist catch and correct
the tech's entry before dispensing, inside the pharmacy's existing dispensing software (e.g., PioneerRx,
QS/1, BestRx). The company gets it by instrumenting that screen to log any correction made between tech
entry and pharmacist sign-off: a record the pharmacy already generates for itself but does not pool.

**5. D1, VERIFIED (with an instrument-dependent limiter, flagged honestly).** California Business &
Professions Code § 125.9, quoted from statute: *"In no event shall the administrative fine assessed by the
board, bureau, or commission exceed five thousand dollars ($5,000) for each inspection or each
investigation made with respect to the violation…"*, this is the cap 16 CCR § 1775.1 applies to Board of
Pharmacy citations. Source: [Cal. Bus. & Prof. Code § 125.9, FindLaw](https://codes.findlaw.com/ca/business-and-professions-code/bpc-sect-125-9/);
cross-reference [16 CCR § 1775.1, Cornell LII](https://www.law.cornell.edu/regulations/california/16-CCR-1775.1).
A second published instrument gives a much smaller number for the same underlying event class: Pennsylvania
49 Pa. Code § 43b.7 fines specific documentation/dispensing-adjacent violations (e.g. "lack of required
information on prescriptions") at **$100** each. Source:
[49 Pa. Code § 43b.7](https://www.pacodeandbulletin.gov/Display/pacode?file=%2Fsecure%2Fpacode%2Fdata%2F049%2Fchapter43b%2Fs43b.7.html&d=reduce).
Read both before pricing this: the "$5,000 per event" headline is a California ceiling, not a national
floor, and Pennsylvania's actual schedule for the closest analogous violations is two orders of magnitude
smaller. **Frequency: VERIFIED.** NCPA's 2024 Digest: *"the average prescription volume was 59,644 per
store"* annually. Source: [NCPA 2024 Digest release](https://ncpa.org/newsroom/news-releases/2024/10/27/ncpa-releases-2024-digest-report).

**6. Computed or observed / paperwork or physical act:** OBSERVED, whether an entry error is caught
depends on a human pharmacist's downstream behavior, not on arithmetic over two documents, so 1f's
foreclosure does not apply here. **Mostly paperwork, with an honest tail exception**: board-citation
exposure (the D1 evidence above) is paperwork-driven and would shrink if entry became perfect tomorrow; the
rare high-severity case (an actual adverse drug event from a missed error) is physical-act-driven and is
not what the dollar figures above capture, don't conflate the two.

**7. Competition fit:** a verification-layer module inside existing pharmacy dispensing software, sold as a
subscription; the asset is the cross-pharmacy corpus of entry-error patterns and catch rates, which only
grows by running inside real verification queues, not a pharmacist consulting engagement.

**Open flag (Stage 0b):** the data used here is pre-claim, internal workflow data generated between a tech
and a pharmacist inside one company, it never crosses into PBM-adjudicated claims data, which is where
PBM network-agreement data restrictions typically bite. This assumption has not been checked against an
actual PBM contract; NOT VERIFIED, flag before further investment.

---

## Candidate 3: Point-of-Load Label Rate Compliance Check

**1. Tuple**
- **Customer segment/band:** independent agricultural retailers and custom pesticide-application
  businesses (co-ops, independent ag retail branches, custom applicator crews), under 300 staff.
- **Asset:** a private ledger of {tank-mix load order (product, rate, crop, acreage, application date,
  weather at load time) → the applicable EPA label's rate/crop/interval conditions → eventual outcome
  (state lead-agency misuse finding, drift/crop-injury claim, or none)}, built only by operating across many
  loads and any enforcement or claim events.
- **Document/state input:** the load ticket / mix order, structured text naming product, rate, crop,
  restricted-entry interval, pre-harvest interval, buffer zone, entered by the loader or applicator
  immediately before mixing, checked against the specific product's EPA-approved label for that crop and
  site.
- **The mistake:** an off-label application, wrong rate, wrong crop, a missed pre-harvest interval, or a
  missed buffer/restricted-entry interval.
- **Checker and rule:** the state lead pesticide-control agency, cooperating with EPA enforcement under
  FIFRA § 26, investigating a residue finding, drift complaint, or crop-damage claim, and able to cite use
  "inconsistent with its labeling" under FIFRA § 12(a)(2)(G) with civil penalties under FIFRA § 14(a).

**2. Differentiated claim:** An incumbent would already have to be claiming that its load-ticket software
checks the *specific* rate/crop/PHI/REI/buffer conditions for the exact product-crop-site combination
against *this retailer's own history* of near-boundary mixes and their outcomes, not merely displaying the
label PDF or a generic tank-mix compatibility chart, for this to be dead.

**3. Question shape and why now:** Choice, among {compliant / minor deviation / likely off-label}, with
per-option probability, decided the moment the loader keys the mix order while the truck waits in the yard.
Cost matters more than raw millisecond latency: a retailer runs many loads a day in season and cannot
absorb per-call LLM pricing on thin per-load margins; near-zero cost is what lets every load get checked,
not just a sample.

**4. Outcome observation:** a state lead-agency Notice of Warning or civil-penalty complaint, or a
grower/neighbor damage claim, arriving at the retailer as a formal letter, logged in the retailer's
existing agronomy software (e.g. Agvance, SSI), which already stores every mix ticket. The company gets the
outcome by tagging tickets that later produced a complaint, claim, or citation.

**5. D1, VERIFIED.** 40 CFR § 19.4, current table for 7 U.S.C. § 136l(a)(1) (commercial applicators,
wholesalers, dealers, retailers, and other distributors): **"$24,885"** per violation, for penalties
assessed on or after January 8, 2025. Source: [40 CFR § 19.4, Cornell LII](https://www.law.cornell.edu/cfr/text/40/19.4).
**Frequency: NOT VERIFIED.** Could not source a specific applications-per-season figure for a custom
applicator or ag retail branch within this search budget.

**6. Computed or observed / paperwork or physical act, honest split, flagged per rung 1f.** The narrow
rate/PHI/REI check (does the entered rate exceed the label maximum, is today inside the PHI window) is
COMPUTED, an inequality over two documents (the label and the ticket), and by itself supports **no**
private-by-operating moat; per 1f, that slice cannot claim "our data gets better as we run." What is
OBSERVED, and is the only defensible asset here, is the near-boundary judgment layer: which
technically-compliant mixes still produced a drift injury or residue finding under real weather and field
conditions. **Physical act dominates the money**, and this is the candidate's weakest point against 2a: if
the mix ticket became instant, free, and perfect tomorrow, a real drift event driven by wind at
application time would still happen or not, most of the risk survives the paperwork fix. The one thing
that keeps this from collapsing entirely, per STATE.md's C-70 correction, is that the FIFRA penalty above
attaches to the *recorded use decision itself* (label-inconsistent use is citable whether or not physical
drift actually occurred), so the paperwork layer is independently billable even though it is not most of
the money.

**7. Competition fit:** a point-of-load compliance layer built into the retailer's existing load-ticket
software; the asset is the cross-retailer corpus of near-boundary mixes and their eventual outcomes, not
an agronomist's advisory service.

**Open flag (Stage 0b):** many crop-input manufacturers (large chemical/seed companies) run dealer
agreements with independent ag retailers that include usage-reporting and data-ownership clauses, the
same structural shape as the automotive Tier-2 pattern already dead-listed in this project. Whether such a
clause reaches a retailer's own load-ticket records (as opposed to manufacturer-owned sales data) has not
been read. NOT VERIFIED; this is a privity check that must run before this candidate proceeds.

---

## Candidate 4: Refrigerant Closeout Compliance Check

**1. Tuple**
- **Customer segment/band:** independent HVAC/mechanical service contractors, under 300 staff (the large
  majority of U.S. HVAC contracting firms are single-digit to low-double-digit truck operations).
- **Asset:** a private ledger of {technician's closeout entry (refrigerant recovered vs. charged, leak-repair
  narrative, equipment size, certification number) → outcome (EPA/state inspection finding, or none)},
  built only by operating across many work orders and any enforcement contact.
- **Document/state input:** the digital work-order closeout form, structured text/JSON for refrigerant
  recovered (lbs), refrigerant added (lbs), full system charge, leak-repair completion status and date,
  technician certification number, filled on a mobile app the moment the technician finishes the job.
- **The mistake:** a closeout record that fails Section 608 recordkeeping/leak-repair requirements, a
  missing certification number on a 50+ lb system, unreconciled recovered-vs-purchased refrigerant, or a
  leak repair not completed or documented inside the 30-day window.
- **Checker and rule:** EPA (and in some states, a state air agency) under Clean Air Act § 113 (42 U.S.C. §
  7413), acting on the contractor's own closeout records, the record lives with the customer, satisfying
  the "physical arrival" test (0c-i): EPA inspects the contractor's records, it does not generate them.

**2. Differentiated claim:** An incumbent would already have to be claiming that its field-service app
scores each closeout record's probability of surviving an EPA/state recordkeeping audit against *this
contractor's own audit history*, not merely providing a required-field checklist, which every major field
service management platform (e.g. ServiceTitan) already does, for this to be dead.

**3. Question shape and why now:** Score (a 2–10 audit-survivability rubric) evaluated the instant the
technician taps "complete" on the work order. Sub-second matters because the check must return before the
technician physically leaves the site and moves to the next call; near-zero cost matters because a
contractor's fleet closes hundreds of tickets a week and a per-call LLM fee would be a real added cost per
truck-roll with no offsetting revenue per ticket.

**4. Outcome observation, and the candidate's honest weak point:** the outcome is an EPA/state Notice or
Finding of Violation, or, far more commonly, no visit at all for years. This is a genuinely rare external
check event, which is the same latency-vs-consequentiality tension STATE.md's C-70 note names explicitly:
a checker this consequential acts this infrequently. The nearer-term signal the company would actually
train on is a supervisor's own periodic internal record review flagging the same ticket, a weaker,
self-graded proxy, not the external checker itself. Recorded honestly as a stage-2b/1e weakness, not
papered over.

**5. D1, VERIFIED.** 40 CFR § 19.4, current table: Clean Air Act 42 U.S.C. § 7413(b) civil judicial penalty
**"$124,426"** per violation; 42 U.S.C. § 7413(d)(1) administrative penalty **"$59,114"** per day of
violation (up to a statutory cap). Source: [40 CFR § 19.4, Cornell LII](https://www.law.cornell.edu/cfr/text/40/19.4).
**Frequency: NOT VERIFIED.** A blog aggregator (ainora.lt) estimates 3–6 HVAC service calls per technician
per day, implying roughly 1,000–1,200 calls/year, this is not an authoritative source and is recorded as
NOT VERIFIED, and in any case it counts all service calls, not the refrigerant-relevant subset this
candidate needs.

**6. Computed or observed / paperwork or physical act:** OBSERVED, whether a given closeout record would
survive an audit depends on EPA/state enforcement discretion and real inspection trigger patterns, not on
arithmetic over the rule text and the ticket alone; genuinely private-by-operating, contingent on the
frequency weakness in (4) being solved. **Paperwork**, cleanly: recordkeeping penalties attach to the
record, not the physical refrigerant handling itself, so a perfect record tomorrow would remove this
specific exposure even if the underlying mechanical work were unchanged.

**7. Competition fit:** an audit-risk scoring module sold inside or alongside existing field-service
management software; the asset is the cross-contractor corpus of closeout records and their (rare) audit
outcomes, not a compliance retainer delivered by consultants.

**Open flag (Stage 0b):** no counterparty contract was identified that would foreclose a contractor from
pooling its own closeout records (refrigerant distributor agreements were not reviewed and are NOT
VERIFIED to be silent on this). Independent contractors are the dominant structure in this trade, so risk
here looks lower than candidates 1 and 3, but it has not been read.

---

## VERIFIED / NOT VERIFIED source list

**VERIFIED (fetched and read directly, quoted above):**
- [19 U.S.C. § 1592, FindLaw](https://codes.findlaw.com/us/title-19-customs-duties/19-usc-sect-1592/), Candidate 1, D1.
- [Cal. Bus. & Prof. Code § 125.9, FindLaw](https://codes.findlaw.com/ca/business-and-professions-code/bpc-sect-125-9/), Candidate 2, D1.
- [16 CCR § 1775.1, Cornell LII](https://www.law.cornell.edu/regulations/california/16-CCR-1775.1), Candidate 2, D1 cross-reference.
- [49 Pa. Code § 43b.7, Pennsylvania Code and Bulletin](https://www.pacodeandbulletin.gov/Display/pacode?file=%2Fsecure%2Fpacode%2Fdata%2F049%2Fchapter43b%2Fs43b.7.html&d=reduce), Candidate 2, D1 limiter.
- [NCPA 2024 Digest release](https://ncpa.org/newsroom/news-releases/2024/10/27/ncpa-releases-2024-digest-report), Candidate 2, frequency.
- [40 CFR § 19.4, Cornell LII](https://www.law.cornell.edu/cfr/text/40/19.4), Candidate 3 D1 ($24,885, FIFRA); Candidate 4 D1 ($124,426 / $59,114-per-day, CAA § 113).

**NOT VERIFIED (searched, not found to a standard worth citing, or explicitly flagged as weak/derived):**
- Per-brokerage import-entries-per-year frequency (Candidate 1), only aggregate CBP totals (36M
  entries/year, ~13,000 brokers) were found; the per-customer figure is my own division, not a published
  statistic.
- Custom applicator / ag retailer applications-per-season frequency (Candidate 3).
- HVAC technician refrigerant-relevant service-call frequency (Candidate 4), only a blog aggregator
  (ainora.lt) estimate was found, not an authoritative source.
- PBM network-agreement data-use restrictions on pre-claim pharmacy workflow data (Candidate 2, Stage 0b
  flag), not read.
- Crop-input manufacturer dealer-agreement data clauses reaching ag retailer load-ticket records
  (Candidate 3, Stage 0b flag), not read.
- Refrigerant/equipment distributor agreement data clauses (Candidate 4, Stage 0b flag), not read.
- Broker-importer engagement-letter data-reuse restrictions (Candidate 1, Stage 0b flag), not read.
