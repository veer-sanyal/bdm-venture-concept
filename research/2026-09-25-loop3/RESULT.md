# Loop 3 under the active METHOD, 2026-09-25

Desk research only. This is not customer validation.

## Seed

The first run with the seed adopted after loop 2:

> Aim at work that tens of thousands of businesses already pay people to do by hand, their own staff or an outside firm, so that the spend AI would replace adds up to billions of dollars a year. Enter through the slice of that work where a mistake or a delay costs the buyer the most money, and often, and where no software company already holds the customer's data or buying channel.

## What happened

- **Generate.** Three generators ran alone this time, and none reported running out of searches.
  - Generators 2 and 3 independently chose long-term-care Medicaid applications for nursing homes.
  - Generator 1 chose change-order recovery for specialty subcontractors.
  - All three listed import-duty recovery as a runner-up, and all three called it crowded.
- **Merge.** `merged.md`. Archive evidence reached the shaper written as "an earlier round found…":
  - Loop 1's Medicaid judge had scored 10.0, with one judge.
  - The September 7 change-order notice screen survived, but found no staffed role at subcontractors that does this work.
- **Shape.** The shaper returned two companies (`agents/shaper.md`).
  - **Lead:** an AI caseworker for long-term-care Medicaid, starting with Indiana nursing homes.
  - **Fallback:** warranty chargeback defense for auto suppliers. Without knowing it, the shaper regenerated the archive's previously selected concept, Supplier Quality Chargeback Defense.
  - It dropped change orders because every piece now has a funded owner: Document Crunch (being bought by Trimble), Trunk Tools, Clearstory AI, Adaptive ($30M Series B) and Siteline.
- **Fact-check.** Every number in the two candidate paragraphs was checked against its source before judging (`paragraphs.md` lists each check).
  - Fixed: "Medicaid is the main payer for 63% of homes" became "over 60% of residents".
  - Dropped: a Claimlane claim that the cited page does not make.
- **Judge.** All 15 judges ran together (METHOD's Ordering rule): 3 new random YC F26 controls and the 2 candidates, 3 judges each.

| Paragraph | Need | Value | Market | Risk | Mean | n |
|---|---|---|---|---|---|---|
| Control: ByteAsk (C/C++ coding agent) | 4.0 | 2.3 | 3.7 | 2.0 | 12.00 | 3 |
| **LTC Medicaid AI caseworker** | 4.0 | 2.7 | 3.0 | 2.0 | **11.67** | 3 |
| Control: Applied Kinetics (energy equipment follow-through agents) | 4.0 | 2.7 | 2.7 | 2.0 | 11.33 | 3 |
| Control: Agent Relay (coding-agent team infrastructure) | 3.0 | 2.0 | 3.3 | 1.7 | 10.00 | 3 |
| Supplier warranty chargeback defense | 3.0 | 2.7 | 2.0 | 2.0 | 9.67 | 3 |

The bar is 10.96, the mean of 16 banked controls.
- **The Medicaid caseworker advances**, 0.71 above the bar. That is outside the 0.5 band, so it needed no extra judges. Judge totals were 12, 12 and 11: two backed it, one passed.
- **Supplier warranty defense stops**, 1.29 below the bar. Judge totals were 10, 10 and 9.

## LTC Medicaid AI caseworker: what the judges found

- **Strongest version (all three converged).** An AI-run eligibility *service*, not software, paid only per approved case.
  - Buyer: regional chains of 10 to 100 homes with a central business office.
  - Entry: take each operator's oldest pending or denied cases, then file new ones before the retroactive window closes, and handle renewals.
  - AI does the family chasing, statement reading, transfer flagging and letter drafting. A small human team signs off and deals with caseworkers.
  - Cut VA benefits and long-term-care insurance (different buyers). Home-care Medicaid comes later.
- **Claims that held.** KFF (1.2M residents, over 60% Medicaid-primary), the retroactive cut from 3 months to 2 on 1 January 2027 (OBBBA §71112) and the Genworth $9,277 median all check out.
- **Claims that are weaker than the paragraph made them.** All three judges raised the same two points:
  - $9,300 is the private-pay price. What a home loses on an unpaid month is the Medicaid rate minus the resident's own contribution, which is less.
  - The retroactive cut only costs money on late *filing*. A case filed promptly is paid back to the filing date however slow the state is. The 2027 change adds pressure, not a forcing event.
- **Competitors.**
  - **Reap** (getreap.com): a near-identical AI agent, "Ruby". It has 12 buildings, a PointClickCare integration and a standalone bank-statement tool. Judge 2 treated it as this team.
  - **MedicaidSoft:** form filling, Plaid statement pulls and AI transfer flags, sold through the HPSI purchasing group.
  - **CoreCare:** pending-case tracking, Texas and Ohio.
  - Service firms: Senior Planning Services (22 states, including Indiana), Richter, and Medicaid Plus, which is free to the home because families pay.
  - Incumbents: PointClickCare owns the data and the marketplace, and ExaCare ($30M) is best placed to add this.
- **Market.** $0.5 to 0.9B nationally for new applications plus renewals (the judges' estimates, unsourced). Indiana is roughly $10 to 20M.
- **Main risks.** A near-zero price anchor from family-paid firms; incumbents that hold the data; cash arriving 45 to 90+ days after the work under per-approval pricing; state and county variation.
- **Fastest test (all three converged).** Offer about 10 Indiana operators to take their 10 oldest pending or denied cases, paid only on approval, and ask for their pending-aging report and 12 months of eligibility write-offs.
  - Kill it if fewer than 3 sign.
  - Kill it if most stuck dollars are waiting on the state or belong to residents who were never eligible, rather than waiting on family documents or late filing.
  - Kill it if operators won't pay more than about $750 per approved case.

## Team fit (`agents/teamfit-ltcmedicaid.md`)

- **The customer list is short and knowable.** CMS's August 2026 file shows 507 certified Indiana homes and about 36,800 residents. 339 of those homes, holding 68% of residents, belong to chains of 10 or more. There are about 12 such chains, among them American Senior Communities (90), Trilogy (62), Infinity (36), Brickyard (23), CarDon (19) and CommuniCare (18). The judges' "10 operators" is nearly the whole Indiana market for this buyer.
- **What gates it is legal standing and a credentialed person, not the AI.**
  - The company acts as authorized representative on Indiana State Form 55366, under 42 CFR 435.923.
  - Indiana's Navigator certification appears waived for nursing-home Medicaid help, per an IDOI FAQ from 2019. Confirm in writing.
  - It must stay on filing, never asset-planning advice; an elder-law attorney should review the letter templates.
  - It needs a HIPAA business associate agreement with each home and with the model vendor.
  - Calls with AI voices need prior consent under the TCPA (FCC, February 2024).
  - It needs one part-time eligibility veteran, such as a former DFR caseworker or business-office manager, paid per approval.
- **Semester plan.** Paperwork and recruiting in weeks 1 to 2, with calls to all 12 chains. Pilots and the cause-of-delay sort in weeks 3 to 6. Filings in weeks 6 to 11.
  - Realistic December state: 2 or 3 pilots, 20 to 30 cases, and a measured split of where the stuck dollars sit.
  - Few approvals before December, because DFR takes up to 90 days to decide an application.
  - Indiana law HEA 1277 moves long-stay residents back to fee-for-service on 1 July 2027, which adds business-office load and helps the "take it off your desk" offer.
- **Timing.** Check the date of the Burton D. Morgan final (Dec 10 last year).

## Supplier warranty chargeback defense: why it stops

This is the first blind score for the archive's previously selected concept. It scored 9.67, below every control but one.

- **Our paragraph misframed its headline number.** Warranty Week's $468M is total warranty cost reported by publicly listed US parts companies (Cummins, O'Reilly, Wabtec, Brunswick), mostly their *own* product warranties, not automaker chargebacks. The fact-check verified the number but not what it measures. That is exactly the failure METHOD step 4 names.
  - Judges' estimate of real automaker-to-supplier charges: about $1.2 to 3B a year in North America.
  - Contingency revenue on the reversible slice: tens of millions.
- **The contracts remove the per-charge dispute.** Stellantis's Global Warranty Terms bill by a "Technical Factor": a percentage times repair cost, starting at 50%, then reset from a sample of returned parts. Disputes "may in no case call into question" that percentage. The North America procedures give 5 business days to dispute a debit. GM moved to a 50/50 rule in 2010 and a new chargeback process in 2021.
- **The strongest version** defends the Technical Factor sample and audits monthly debits for arithmetic and attribution errors, for mid-size Tier 1 and 2 suppliers with Stellantis, GM or Ford exposure.
- **Fastest test.** Audit 12 months of debit files from 3 to 5 Midwest suppliers. Kill it if contract-valid errors come to under 3 to 5% of dollars charged, or if suppliers won't file against their customer.
- This bears on the STATE comparison concept (parked since 9/20 on the relationship objection). Two judges named the same fear of retaliation independently.

## What the seed did

Candidate averages across all rounds are now need 3.57, value 2.49, market 2.27 and risk 2.03. The controls are at 3.76, 2.33, 2.92 and 1.96.

The Medicaid caseworker kept need at 4 and reached market 3. The seed's "costly, frequent failure" wording fixed loop 2's urgency problem without giving back market. Market for the supplier idea fell to 2, because its slice turned out small once the headline number was read correctly.

## Process notes

- **Search starvation in judging.** 10 of the 15 judges said they ran out of web searches partway and finished by opening primary sources directly: 5 of the 6 candidate judges and 5 of the 9 control judges. In loop 2, the 3 candidate judges running alone made 36 to 48 tool calls each without running out. METHOD now caps concurrent agents (see Ordering). The scores are recorded as they are; the effect is unmeasured, and it probably hit the candidates harder.
- **Fact-check gap.** Checking a number is not the same as checking what it measures. The $468M figure passed the first check and failed the second. METHOD already says "say what it measures", and the orchestrator didn't do it here.
- **Local files.** Under the new clause, every judge and the shaper say they read no project files. The team-fit agent had no such clause and read METHOD.md (it cited the save path). That does no harm, because team fit is not blind.

Files: `paragraphs.md` (all five paragraphs as judged, with the fact-check notes), `merged.md`, and `agents/` (3 generators, the shaper, 15 judges, 1 team fit, and the controls draw).
