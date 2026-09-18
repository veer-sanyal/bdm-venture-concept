# I1. Pre-filing RFE prediction for 3-30 person flat-fee immigration firms. Blind screen return, 2026-09-08.

Budget used: 20 searches, 17 fetches, plus one primary xlsx download.

## THE CASE FOR

Strongest demand tier: **D2, published price of the worse substitute.** Powell Immigration Law (calivisa.com/attorneys-fees): H-1B flat fee "$3,500-$5,500"; "if USCIS issues a Request of Evidence (RFE), there are typically additional attorney's fees," "$2,000 to $4,500" nonimmigrant, "$3,000 to $5,000" immigrant, at "$350" hourly. **D3 filled:** Scott Law Firm careers page, Immigration Paralegal (Employment-based): "Prepare supporting letters, RFE responses and client correspondence"; "Assist attorney with coordination of RFE deadlines." **D4 primary, checker-published, fetched and parsed:** USCIS I-129 RFE dataset FY2026 Q2 (Oct 2025-Mar 2026): H-1B 173,227 completions, 15,337 "Completions with RFE" (8.9%); L-1A 25.2%; L-1B 28.7%; O 24.8%; Blanket L 22.7%; TN 12.8%. **Rung 2.5 clears on D2 + D3 + D4.**

Strongest rung-2 pass: the instrument is real, fetched, and the outcome is itemised by regulation. 8 CFR 103.2(b)(8)(iv): the RFE "will specify the type of evidence required, and whether initial evidence or additional evidence is required." Policy Manual Vol 1 Pt E Ch 6: RFEs must "Identify the eligibility requirement(s) that has not been established and why the evidence submitted is insufficient; Identify any missing or deficient evidence specifically required." A 5b attribution most candidates never had. No amnesty, no fee-shift.

## SCORED WEAKNESSES

- **Rung 1 (crit 2, heavy):** who is principal for the hours depends on the engagement letter, and the one fee page read bills RFE response separately at $350/hr. Where RFE is excluded from the flat fee, the RFE is firm REVENUE of $2,000-4,500, and the product sells its removal. "Most firms include one RFE response" is a blog claim, NOT VERIFIED. Filing fee and I-290B are the client's money.
- **Rung 1.5 (crit 4):** US8244659B2, "Immigration application management apparatus, systems, and methods," per search summary "to increase the likelihood of acceptance." Patent page NOT FETCHED.
- **Rung 2 duty-holder (crit 1):** 8 CFR 103.2(b)(8) names only "the applicant or petitioner"; the representative appears nowhere. Not K2 (the petitioner is the firm's principal, not its counterparty), but the instrument does not bind the buyer.
- **Rung 2 pooling (crit 4, 5):** ABA Formal Opinion 512, per summaries: "Informed client consent is required before entering information related to client representation into a self-learning genAI tool" and "boilerplate consent included in engagement letters will not be adequate." NOT FETCHED. If accurate, the cross-firm ledger cannot be carved in by boilerplate, and a 3-30 person firm's own RFE history is thin (a 200-H-1B firm at 8.9% sees ~18 RFEs a year).
- **Rung 2 legislated (crit 7):** Policy Manual, fetched: "the issuance of an RFE or NOID is not required by regulation and USCIS has discretion to deny the request without first issuing an RFE or a NOID." Blogs date the change to 5 Aug 2026; NOT VERIFIED from USCIS. The mistake is migrating from RFE to outright denial.
- **Rung 3 GIVES/UNDERCUT (crit 4):** Prolexis (Capterra): "AI Case Strength Assessment," "RFE Response Generator," "Document Readiness Score," from $79/month, 0 reviews. AutoPetition (fetched): "RFE risk predictions with explanations," "AI-powered gap analysis shows what's missing," free "Check Case Strength," for "self-petitioners, firms, employers, and agents." Docketwise/8am: extraction and writing assistant; no pre-filing RFE claim on the page read.
- **Rung 3 PUBLISHES/COMPELLED (crit 3, 5):** the regulation compels the checker to hand the customer the itemised answer free with a cure window of up to "twelve weeks"; the RFE IS the free appeal. ~82% of RFE'd H-1Bs are then approved (12,597 of 15,337), so the H-1B RFE is mostly a delay-and-hours event, not a loss event.
- **Rung 3 CAPTURES (NOT VERIFIED):** USCIS ELIS "Evidence Classifier" (DHS AI inventory, per summary). **ABSORBS:** premium processing does not absorb. **RATCHET (crit 5, moderate):** over-document everything is free and current practice. **FEE-SHIFT:** none at agency level.
- **Rung 4 (crit 4, 2):** claim already made on vendor pages: SpaceLizit, fetched, "AI pre-filing audit checks every H-1B, L-1, and O-1 petition against 10,000+ USCIS denial patterns before submission," "RFE rates dropping from 25% to under 3%," no named firm, "Last updated April 2026." Visalaw.ai, fetched: "predict the most likely USCIS RFE issues for this case, and recommend evidence to add now to reduce RFE risk." Prolexis product page 403 twice. No incumbent claims the "at this service center" clause; that clause is a narrowing below the incumbents' stated claims (crit 2). Installed base from postings (summaries): "INSZoom, Docketwise, LawLogix." Exited predecessor: UNRUN.
- **Rung 5 (crit 5):** 5a passes. 5b passes by regulation. 5c fails: the "add this evidence" branch is graded only as an aggregate no-RFE rate; base rate 91% "nothing happened" for H-1B.
- **Rung 6 (crit 6):** AILA "18,000+ current AILA members" (fetched). IBISWorld 18,417 immigration law businesses, average 2.5 employees (summary, NOT VERIFIED): most of the population is below the 3-person floor. Expected value per petition: 8.9% x $2,000-4,500 = roughly $180-400 per H-1B, $500-1,300 per L-1 (derived).

## KILL: NO KILL. No K1; no K2 (petitioner is the firm's principal); no K3 (SpaceLizit, Prolexis, AutoPetition, Visalaw.ai supply G1 only; no named deployment in the 3-30 band, no outcome in words other than the vendor's).

## D3 STATE: FILLED AT THE CUSTOMER, with an incentive caveat: postings pay people to RESPOND to RFEs; where RFE is billed separately the firm's revenue is inverted relative to prevention. Band read: one firm's careers page, size NOT VERIFIED.

## MUTATION (M0): Forced. (1) The Policy Manual's discretion to deny without RFE converts the mistake from "an RFE" (free cure, 82% still approved) to "adverse action for insufficient initial evidence," more expensive and more attributable; (2) the firm is principal for the hours only when its flat fee includes RFE response. Mutation: same customer, mistake redefined as denial-or-RFE on initial-evidence sufficiency, outcome label from the decision notice, "service center" clause dropped as unsupported, pooling conditional on per-client consent per ABA 512. Adjacency: "legal intake" shares none of the five-tuple; "provider denial appeals" shares the mistake SHAPE (itemised deficiency notice with cure window, response labour already outsourced: immisupport.com sells "outsource H1B RFE response to virtual paralegals").

## PRACTITIONER QUESTIONS
1. Does your flat fee include the RFE response, or is it billed on top? What did the last one cost you in hours?
2. When did an RFE last arrive, and what did you change afterwards?
3. Since August 2026, have you had a denial with no RFE first?
4. Do RFEs arrive itemised, or as boilerplate templates?
5. Which case-management system, and does it flag missing evidence pre-filing?
6. Would you consent, per client, to pooling filed petitions and RFEs across firms?
7. Does the service center change what you file?

## VERIFIED: 8 CFR 103.2(b)(8), (b)(11), (b)(13)(i) (law.cornell.edu); Policy Manual Vol 1 Pt E Ch 6 (uscis.gov); USCIS I-129 RFE xlsx FY2026 Q2 (uscis.gov); Powell fees (calivisa.com); Scott Law Firm postings (pwscottlaw.com/careers); AILA 18,000+ (aila.org/about); SpaceLizit, AutoPetition, Visalaw.ai blog, Docketwise blog, Capterra Prolexis pages; Envoy Nov 2023 H-1B RFE history (secondary: FY2019 40.2%, FY2022 9.6%, FY2023 10.5%).

## NOT VERIFIED: Prolexis probability claim (403); ABA Op. 512 quotes; 5 Aug 2026 policy date; I-290B $800; premium-processing clock; US8244659B2 text; IBISWorld counts; Parikh/Barre/Glassdoor postings; ELIS Evidence Classifier; "most firms include one RFE response"; the prompt's "10-20 hours" and "two- to three-month delay". D5 UNRUN. Exited-predecessor UNRUN beyond one query.
