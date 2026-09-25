# STATE: current venture exploration

Updated September 25, 2026. This file owns current decisions; [METHOD.md](METHOD.md) owns the active process.

## As of 2026-09-25 (read first)

- **The method was replaced on 9/24.** Short prompts, blind judges scoring on the BDM rubric, a bar set by the mean of every banked YC control, and 3 to 5 judges per paragraph. Scores go in `scores.csv`; run `python3 tools/scores.py` to see them. Every agent report is archived under `research/2026-09-2*`.
- **Loop 3 (9/25), new seed: the LTC Medicaid AI caseworker advances at 11.67** (need 4, value 2.7, market 3, risk 2, n=3; bar 10.96). Full write-up: [research/2026-09-25-loop3/RESULT.md](research/2026-09-25-loop3/RESULT.md).
  - **What it is (the judges' strongest version):** an AI-run eligibility service, paid per approved case, for regional nursing-home chains. It takes their oldest pending and denied cases first, then files new cases before the retroactive window closes and handles renewals.
  - **Watch out for:**
    - Reap (getreap.com) sells a near-identical AI agent.
    - MedicaidSoft already sells form filling and transfer flagging.
    - Some eligibility firms are free to the home.
    - $9,300 is the private-pay rate, not what a home actually loses.
    - The 2027 retroactive cut only hurts late filings.
  - **Fastest test:** offer about 10 Indiana chains to take their 10 oldest pending or denied cases, paid on approval, and get their pending-aging reports.
    - Kill it if fewer than 3 sign.
    - Kill it if the stuck dollars are mostly waiting on the state or belong to residents who were never eligible.
    - Kill it if chains won't pay more than about $750 a case.
  - **Team fit:**
    - About 12 Indiana chains of 10 or more homes hold 68% of residents: American Senior Communities (90 homes), Trilogy (62), Infinity (36) and others.
    - What gates it is authorized-representative standing (State Form 55366), a HIPAA business associate agreement with each home, TCPA consent for AI calls, and one hired eligibility veteran.
    - Only 2 or 3 pilots and a cause-of-delay breakdown are realistic by December.
  - **Supplier warranty chargeback defense: 9.67, stops.** This is the first blind score for the archive's comparison concept, which the shaper regenerated without knowing it. Automaker contracts bill suppliers by a sampled "Technical Factor" that can't be disputed on the invoice, and the reversible pool is tens of millions of dollars. Our paragraph also misread Warranty Week's $468M: it is suppliers' own product warranties, not automaker chargebacks.
  - **Search starvation:** 10 of 15 judges ran out of web searches with all 15 running at once. METHOD now runs judges in batches of at most 6.
  - **New controls:** ByteAsk 12.00, Applied Kinetics 11.33, Agent Relay 10.00.
- **Loop 2 (9/25): nothing advanced.**
  - The air-permit environmental department scored 10.33.
  - The seed lifted market but cost need; the next seed fixed that.
  - Write-up: [research/2026-09-25-loop2/RESULT.md](research/2026-09-25-loop2/RESULT.md).
- **Standings (desk research only, not customer validation):**
  - Bar: 10.96, the mean of 16 YC controls.
  - **LTC Medicaid AI caseworker: 11.67, advances (loop 3).** It is the highest candidate so far. Loop 1's single-judge nursing-home version scored 10.0.
  - **Credit-dispute response for collectors: 11.2, advances (loop 1).** Team fit found Sonnet (Provana), which handles over 1M disputes a month. The opening is a litigation-ready file for purchased debt (*Hinkle v. Midland*). Test: 10 dispute-ops calls asking cost per dispute, share of documents held electronically, and a $2 per-dispute pilot on 1,000 closed disputes.
  - Arc flash from photos: 10.6, stops. 70Ez and AmpSketch already sell it.
  - Environmental department for small permitted plants: 10.33, stops (loop 2).
  - Supplier warranty chargeback defense: 9.67, stops (loop 3).
  - AI review certification (Assay): 9.0, stops.
- **Decisions waiting on Veer:**
  1. Adopt the proposed leaner loop: one shaper per idea, a stored control bank, judges added one at a time, and one reshape pass for near misses. Estimated cost falls from about 4.1M to 2 to 2.5M tokens per loop.
  2. Refresh the control bank with scoring anchors for 1, 3 and 5 on each parameter. Risk currently varies by only 0.09 across ideas and does no ranking work. This means re-judging the 10 controls to 3 judges each.
  3. Install Agent-Reach (Panniantong/Agent-Reach), starting with the check-only mode. Reddit and X need Veer's own cookies from a throwaway account; Claude never handles them.
  4. Choose the concept to name for the prelim due **Sun 9/27, 11:59pm**. It is unscored; a name and a paragraph are enough. Two candidates are above the bar: the LTC Medicaid caseworker (11.67, Indiana-local buyers, and a test that fits the semester) and credit disputes (11.2).
- **METHOD updated 9/25 from loop 2 (Veer's request):**
  - The shaper and judge prompts now carry the "don't read local project files" clause.
  - A seed section holds the current seed and a one-line history per round. The new seed keeps the labor-spend half and asks for the slice where a mistake or delay costs the buyer the most, and often.
  - The stages run in order (generators, then the shaper, then the judges). After loop 3, judges run in batches of at most 6.
  - Every number in a candidate paragraph is checked against its source before judging, and paragraphs are saved as judged.
  - Controls are drawn from unbanked B2B companies with a recorded random seed.
  - Archive evidence reaches the shaper written as "an earlier round found…".
  - Agent reports are saved verbatim from transcripts.
- **Known issue:** the shaper stalled after spawning its research subagents and had to be resumed by message (loop 1; not repeated in loop 2).

## Founder scope

Veer explicitly wants **AI B2B SaaS**, **AI-native services**, or **consumer AI with a defensible moat**. AI must materially affect value or delivery. Human involvement is compatible with an AI-native service. Ordinary services or marketplaces with incidental AI do not fit.

Team context: Veer + Cole, Purdue. Actual skills, budget, customer access and current time commitment remain unconfirmed. Company-building comes first; competition constraints should be checked against current official rules when submitting.

## Current decision

Exploration is reopened at Veer's request. The old search-stop date and "no further ideation" instructions are superseded. **Supplier Quality Chargeback Defense remains the previously selected concept and comparison point; no replacement has been chosen.**

Its historical evidence is in [CONCEPT.md](CONCEPT.md), [CALL-GUIDE.md](CALL-GUIDE.md) and the specialist research files. Those records have not been fully re-verified in this method update. Their legal, market and performance conclusions are historical claims, not newly validated facts.

The previous validation plan was supplier conversations, redacted closed cases, an experienced advisor and a paid pilot. Completion of those actions has not been established in this session. Compare the concept against an ordinary general-purpose AI workflow on the same inputs before assuming a product advantage.

## Scope correction to the first exploratory run

The initial short-prompt run generated 12 broad hypotheses and desk-checked three before Veer clarified the allowed business types. It is a process pilot, not a completed in-scope search or a controlled quality/cost comparison.

| Idea | Current status | Next useful step |
|---|---|---|
| Supplier Quality Chargeback Defense | Existing selected concept; validation status unconfirmed | Establish which customer evidence exists and test its proposed advantage against current alternatives. |
| Technician diagnostic knowledge capture | In-scope AI B2B SaaS hypothesis; desk-checked, not validated. 2026-09-21: Pear's August 2026 RFS asks for an agent that interviews a company for tacit knowledge, a second-source demand signal ([note](research/2026-09-21-rfs-channel.md)) | Two-hour crowding scan on Pear's ask first. Then, with real technician access, examine whether an interview adds useful diagnostic knowledge beyond existing records and whether it transfers to another case. |
| Buyer-readable manufacturing proof packets | Adjacent to prior PPAP research; AI role and advantage need clarification | Retrieve relevant history if shortlisted; do not call it new or verified. |
| Connected-building compatibility record | Unresearched; in scope only if AI is material | Clarify the AI-dependent job and obtain an actual installer case before investing in research. |
| Conditional mobile-service stops | **Out of scope as formulated** | Remove from the active shortlist; do not add incidental AI to preserve it. |
| Unavailable replacement-part recovery | **Out of scope as formulated** | Remove from the active shortlist; a materially different AI-native formulation would be a new hypothesis. |

Other ideas from the broad batch are not promoted. No consumer AI moat was verified. No in-scope idea has been demonstrated superior to the existing concept. No customer outreach or product trial occurred in the desk-research run.

## Next research round

Use the clarified brief and short generation prompt in METHOD. Generate within all three allowed categories without imposing an industry allocation. Check archive overlap afterward. Then check the merged batch against the current investor ask lists (catalog and reasoning in [research/2026-09-21-rfs-channel.md](research/2026-09-21-rfs-channel.md)): a match is one fundability signal and triggers the two-hour crowding scan; never generate from the lists. Proposed as a METHOD addition, not yet adopted. Shortlist a few hypotheses, verify decisive claims and prepare small tests. Maintain a concise current board rather than repeatedly importing the archive.

## 2026-09-20 desk run on the chargeback concept (recorded 2026-09-21, ran on the archived method)

Four blind desk lanes on the salience question. Result: the "relationship objection" (suppliers do not fight chargebacks to protect the OEM relationship) is the best-supported explanation for the demand gap, and the concept's stated mistake is contradicted by the only first-hand account found. The desk is exhausted on three questions that need a human. Full text: `archive/2026-09-20/STATE-pre-reset.md` (section "THE FOUR-LANE DESK RUN"), predictions `predictions/2026-09-20-k4-relationship-desk.md`. Status under the active method: **park until a supplier conversation happens**; no desk work changes it.

## Round 17, the Jev lane (2026-09-20 to 09-21). Ran on the archived ladder, integrated here under the active method.

Premise: TypeSafe AI's Jev (launched 2026-09-18), a non-generative model returning calibrated probabilities on typed questions in under half a second at near-zero cost. AI is central to every candidate's delivery, so all are in scope as AI B2B SaaS. Twelve generated in three fresh contexts, ten desk-checked, five independently reviewed for an incumbent making the same claim (none did). Digest and ranked board: `CANDIDATES-JEV.md`. Full returns: `screens/2026-09-20-round17-jev/`. Predictions and scoring: `predictions/2026-09-20-round17-jev.md`.

| Idea | Status under the active method | Next useful step |
|---|---|---|
| Real-time HTS entry line check for customs brokerages under 300 staff (C1) | **Test next.** Strongest case built: statute binds the broker, the seat is funded, no vendor or free bundle calibrates against a broker's own post-entry outcomes, and the January 2026 CBP ruling that stopped the importer-side version requires exactly this customer | One entry writer, one question: how many filed lines come back challenged in a month and how they find out. Decides whether a probability is learnable |
| Documentary-credit discrepancy predictor for small exporters (A2) | **Park.** Only candidate with no scored 2, and every presentation is graded on both branches, but the fee per event is $50 to $130 and the US segment is uncounted | Count US exporters under 500 staff presenting under letters of credit monthly; if small, drop |
| Grant cost-allowability grading for small recipients and their auditors (B4) | **Park.** Capability gap and free public outcome data, but one audit label a year and a two-headed buyer | Pick the recipient as the buyer; ask one CHC finance lead what a questioned cost costs them |
| Consumer-report match-confidence grading for small screeners (B1) | **Park.** Large screener holds a patent on the mechanism and sells to employers, not to small screeners; pooling rights unknown | Read one small screener's platform contract for data-use terms before any further desk work |
| Prescription-entry LASA check for independent pharmacies (C2) | **Park.** Fines small; a funded competitor already integrates with the same systems | None until a pharmacist names a recent miss that cost money |
| Claims-file compliance grading for auto/GL TPAs (B3a) | **Drop this formulation.** Re-screen found the DOI instrument binds the insurer, not the TPA (10 CCR 2695.2(i), NAIC Guideline 1090) | A Texas-only version (Ins. Code ch. 4151 licenses the TPA directly) is a new hypothesis for Veer to accept or decline; not run |
| H-1B RFE-risk score (A4) | **Drop this formulation.** The buyer is outside counsel, and a vendor already sells law firms a private model on their own RFE responses | A law-firm version is a new hypothesis, not a rescue |
| Import classification audit-risk for importers (A3) | **Drop this formulation.** Duplicate of the archived H7; CBP HQ H350722 reserves the decision to a licensed broker | None; the broker-side C1 is the in-scope form |
| Export-control enforcement-risk (A1), pesticide label rate check (C3) | **Drop this formulation.** Only saleable output is the less-conservative call nobody will act on (A1); penalties near zero and D3 empty (C3) | None |
| Refrigerant closeout (C4) | Unresearched | Only if an HVAC contractor names an EPA audit they paid for |

Generator note for the next round: three fresh contexts converged on tariff classification and one reproduced the archived H7 exactly, because the brief given to generators listed killed candidates but not "does not survive as scoped" ones. The active method says not to load dead lists at all; overlap is checked after generation instead, which would have caught this in the merge step.

## Fast-policy round (2026-09-21, early morning), the first round run on the active method

Urn: decisions made continuously from live state that run on hand-written rules today, where a calibrated decision every hundred milliseconds could replace the rule and the outcome is observed within minutes. Two fresh generators (one strong, one balanced), twelve ideas, merged and shortlisted in `research/2026-09-21-fast-policy/shortlist.md`; three verified with a bounded search budget; one independent review over the three plus round 17's C1 as comparison (`research/2026-09-21-fast-policy/review.md`).

| Idea | Verdict | Reason | Next useful step |
|---|---|---|---|
| Real-time HTS entry line check for customs brokerages (C1, from round 17) | **TEST NEXT, first conversation** | The only idea where the workflow actually needs a sub-second answer; the buyer is a licensed individual with personal statutory exposure; the one open question is binary and short | One entry writer: of the lines you file in a month, how many come back challenged, and how do you find out. A "hardly any" answer undermines the outcome-log premise for the whole lane |
| Load tender accept/reject and driver assignment for carriers with 1 to 20 trucks | **TEST NEXT** | Tenders verifiably expire in minutes (load-board expiry webhooks, EDI 990 windows); no small-carrier product scores accept/reject, only drafts replies; the substitute is a dispatch service at 4 to 10 percent of gross forever | Shadow one small carrier's real tenders for a week; compare the dispatcher's reasoning with what a calibrated call returns. The reviewer flagged the memo's per-load dollar swing as the memo's own arithmetic, not a published number |
| Task-assignment policy for small warehouse and yard operators | **PARK** | The gap (default alphanumeric task order) is plausible but the memo's keystone vendor quote could not be found on the cited page, and one search found a vendor selling dynamic task assignment to 3PLs; no operator or vendor number for policy beating rules exists | Only if an operator hands over one logged day of assignments and outcomes for a replay comparison |
| Peak-demand load policy for single commercial buildings | **DROP THIS FORMULATION** | A fetched Johnson Controls Metasys bulletin shows the incumbent already runs demand limiting once a minute with a forecast and prioritized shedding; the surviving re-scope is a commissioning service, outside scope | None |
| Kitchen pacing, clinic no-shows, field-service admission, support-desk anticipation, parking enforcement, self-storage pricing | PARK (unresearched) | Reasons in the shortlist file; most hinge on whether the system holding the live state is reachable | Revisit if access appears |
| MSP ticket triage | Drop this formulation | Archived pricing finding stands; helpdesk platforms already predict SLA breach | None |

Method notes from this round: the verifiers' memos each carried at least one claim presented as verified that the reviewer could not reproduce (a quote absent from the cited page, a memo's own arithmetic labelled published, a resolution number against the wrong URL); the single-review step caught all three, which is what it is for. Decision status: desk research only; no customer contact has happened; nothing here is validated.

## Evidence and history

- [Method reset and findings](research/2026-09-18-method-reset.md)
- [Investor ask lists as a sourcing channel, 2026-09-21](research/2026-09-21-rfs-channel.md): use as filter and vocabulary, not generator; current in-scope asks from YC, a16z, Bessemer, Pear; the two-hour "already being solved" scan; differentiation moves for a team with no capital. Second pass: twenty more firms hold no list, Primary VC's March 2026 RFS added, and a customer-side sweep (HN, Capterra) found narrow named workflows; accounting-shaped AI-native services now carry three independent sources, with expat tax filing for Americans holding US investments the one buyer quote with a price. Reddit unreached. No candidate promoted; nothing here is customer validation.
- [Archived method, state and README](archive/2026-09-18/README-ARCHIVE.md); [ladder-era STATE.md as of 2026-09-21, with the 9/20 desk run and round 17](archive/2026-09-20/README-ARCHIVE.md)
- CASEBOOK, CANDIDATES-*.md, screens/ and predictions/ remain evidence/history. Their old rankings, stop rules, kills and imperative prompts are not current instructions.

Record future decisions here with a date, reason, evidence status and next action. Update only when evidence or founder preferences change; more model agreement is not new market evidence.
