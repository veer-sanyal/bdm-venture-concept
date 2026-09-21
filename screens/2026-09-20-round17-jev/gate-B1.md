# Gate B1, Consumer Report Match-Confidence Grading (fresh gate, round 17)

**Candidate:** consumer reporting agencies (CRAs) doing employment/tenant background screening,
sub-300 employees. **Differentiated claim tested:** "our matching engine independently re-verifies
every borderline hit against full identifying detail before a human ever sees it, not just a
similarity score that still sends the ambiguous ones to a queue a person has to work through."
**Incumbents examined (named in dispatch):** Checkr; First Advantage (Sterling, now merged into
First Advantage). **Platforms named in dispatch to check for a free bundle:** none beyond the two
incumbents above, see G4.

All page fetches below are fresh (this session), not search-summary paraphrase, except where
marked NOT VERIFIED / no live page found.

---

## G1, CAPABILITY: does an incumbent already make the exact claim?

**Checkr.**

- Adjudication product page (`checkr.com/products/adjudication`): no claim of independent
  re-verification of borderline hits before human review; the page's own content covers record
  filtering and charge-classification only, and does not address how ambiguous matches are
  processed.
- Checkr AI page (`checkr.com/our-technology/ai-powered`): "Checkr AI identifies which name
  variants belong to the individual you're verifying and which belong to someone else, then
  searches records across every confirmed variant." The page states human review is still the
  final step: "Checkr AI handles the complexity. Your team makes the calls." That is the opposite
  of "before a human ever sees it", it hands off to the human, it does not remove the human from
  borderline hits.
- Assess product page (`checkr.com/products/assess`): "Assess Lite is included for free with every
  Checkr account." "Assess Standard reduces reports requiring manual review by up to 75%." Assess
  Premium: "reducing reports requiring manual review by up to 85%," with "up to 235 granular
  filters." Even at the top tier, Checkr's own number is a *reduction* in manual review, not
  elimination of it, 15% of reports still require the human queue, by Checkr's own published
  figure. That is not the claim being tested, which is exhaustive (every borderline hit) re-review
  before any human sees it.
- Checkr's own patent, US10878524B2 ("Identity Matching and Verification Process," fetched from
  Google Patents): describes exactly the mechanism the differentiated claim is written against.
  Abstract: "If the probability is below a threshold or manual review is desired, the system
  automatically triggers a manual review of the record to determine if it belongs to the
  candidate." Claims language: "computing a first final similarity score based on each individual
  similarity score component," and "determining, from the computed first final similarity score,
  that the probability... exceeds a threshold." Manual review trigger: "If the probability score is
  below the threshold or if a compliance review is needed, then... the system triggers a manual
  review." **This is the similarity-score-plus-human-queue pattern the claim is differentiated
  against, in Checkr's own patent text, not the claim itself.**

**First Advantage / Sterling.**

- Sterling's own homepage (`sterlingcheck.com`, fetched fresh): "Sterling Background Check
  Solutions is now First Advantage." "Sterling is now a First Advantage company." "We're bringing
  Sterling and First Advantage together." "Everything you rely on is moving to one place." Sterling
  is not a live, separate brand any more, tense matters here: any Sterling-branded product claim
  found elsewhere on the web is a claim about a predecessor product, not a currently marketed
  distinct one, and current marketing is under the First Advantage name.
- First Advantage's own criminal-background-checks page (`fadv.com/solutions/criminal-background-checks/`,
  fetched fresh) does **not** contain the word "SmartData" and does **not** describe a matching
  methodology or a human-review queue protocol. Its only automation claim on-page: "Our intelligent
  automation helps boost the consistency and efficiency of delivering results," and "Approximately
  90% of our U.S. criminal searches utilize intelligent automation to speed up the entire
  employment criminal background check process." No page reached this session states, in First
  Advantage's own current wording, that every borderline hit is independently re-verified against
  full identifying detail before a human sees it. (Search-summary text describing a "SmartData"
  product with that language exists, but the dedicated product URL did not resolve on fetch this
  session, consistent with the Sterling brand's absorption above, so that specific wording is
  **NOT VERIFIED** as First Advantage's current, live, on-page claim.)

**G1 finding:** No incumbent's own current page states the exact differentiated claim. Both
incumbents' own material instead confirms the status quo the claim is written against, a
similarity-score threshold with the below-threshold ("borderline") hits routed to a human queue
(explicit in Checkr's patent; implicit in Checkr's Assess review-reduction percentages, which are
all less than 100%). No capability overlap on the exact claim was found.

---

## G2, SEGMENT: who do they actually deploy to?

**Checkr customers page** (`checkr.com/customers`, fetched fresh): named, detailed customers are
Kimpton Hotels & Restaurants, Adventure Nannies, Pridestaff, eTech, Field Nation, HONK
Technologies, Purple Innovation, and Rock Point Church, every one an **end-employer or staffing
company buying background checks**, not a consumer reporting agency. Logo-only names (Dominos,
Coinbase, Instacart, Lyft, DoorDash, Uber, etc.) are the same: employers, not CRAs. **No named
customer on this page is a consumer reporting agency or background-check competitor**, at any
employee-count band.

**First Advantage's criminal-background-checks page** (fetched fresh): the only "customer-shaped"
detail is a statistic ("67% of Fortune 100 customers trust First Advantage") and a row of
**integration-partner logos**, Dayforce, Fountain, Greenhouse, HealthcareSource, Infinite,
TalentHub, Jobvite, Lever, OnShift, Oracle, PageUp, Paradox, SAP SuccessFactors, Tempworks, UKG,
Workday. These are HR/ATS platforms First Advantage plugs into, not consumer reporting agencies
using First Advantage's matching engine under license. No named CRA deployment appears here either.

**G2 finding:** Both incumbents' own customer-facing pages show deployment exclusively to
end-employers (direct hiring customers) and to ATS/HR software as integration partners. Neither
page names a consumer reporting agency, at the sub-300-employee band or any other band, as a
customer or licensee of the matching/adjudication technology. This holds for marketing material as
well as customer lists, there is no floor visible even in the "reach-down" marketing language on
these specific pages, let alone in a written policy. **No deployment in the segment was found.**

---

## G3, CAPABILITY OR DISTRIBUTION?

Two distinct gaps, and they point different ways:

1. **The exhaustive-review capability itself is a capability gap, not a price list.** Neither
   incumbent's own material, including Checkr's patent, its most literal statement of how the
   system works, describes a system that reviews every borderline hit without ever routing a
   share of them to a human. Checkr's best published figure (Assess Premium) still leaves 15% of
   reports in the manual queue; the patent's own logic makes a human-review branch structural, not
   incidental. If this were only undeployed capability sitting on a shelf, one would expect the
   in-house version used by Checkr's own biggest-volume customers to already be exhaustive. It is
   not, by Checkr's own numbers. That is evidence of a genuine technical/economic gap (cheap,
   fast, per-hit review), not a decision to withhold an existing capability.
2. **Access to whatever automation does exist is a distribution gap for this segment.** Checkr and
   First Advantage are themselves large CRAs competing for the same end-employer hiring dollars
   that a sub-300-employee CRA also competes for. Selling their internal matching engine as
   licensed software to a smaller competing CRA would arm a rival, not open a new market for them , 
   a channel/business-model choice, not a technical inability to package and sell the software.
   Nothing on either company's page suggests they lack the ability to productize this; they simply
   are not selling it that way.

**G3 answer:** both apply, at different layers. The specific claim under test (exhaustive,
before-human borderline-hit re-verification) is a capability the incumbents have not built even
for their own operations, a real capability gap. Separately, whatever automation they do have is
withheld from the sub-300-employee segment by channel choice (they'd be arming a competitor), which
is a distribution gap layered on top. Per Part 4, a distribution-only gap cannot be the whole
story here, and it isn't the whole story, because the capability gap is independently evidenced by Checkr's own patent and its own incomplete (not-100%) review-reduction numbers.

---

## G4, FREE BUNDLE: platforms the segment already runs

The dispatch named no platform distinct from the two incumbents above, and, per instruction , 
this gate read only the rung 3 and rung 4 sections of the prior screen for names, disregarding its
verdicts. Those two sections name exactly three vendors: Checkr, Sterling, and First Advantage (the
latter two now one company). No separate case-management system, applicant-tracking platform, or
other software that a sub-300-employee CRA is described as already running was named in that scope.

Given G2's finding, that Checkr and First Advantage sell to end-employers and integrate with
employer-side ATS/HR platforms, not to competing CRAs, there is no evidence within the given scope
that a platform the sub-300-employee CRA segment *itself* already runs bundles this capability at
zero marginal cost. The only candidate "platforms" in scope are the incumbents themselves, and by
G2 they are not deployed into this segment at all, bundled or otherwise.

**G4 answer:** NOT VERIFIED / not applicable within the named scope. No zero-marginal-cost bundle
was found because no platform other than the two competing incumbents was named for this segment,
and those two are not run by this segment's own operators (G2). This is a genuine gap in the
evidence, not a finding that a bundle exists, if a CRA-operations platform used by sub-300-employee
CRAs exists and bundles this, it was outside the names this gate was given to check, and identifying
it would need a wider list of segment-run platforms, not more searching on Checkr/First Advantage.

---

## Verdict

**ALIVE.** K3 requires all three, each quoted: the exact claim on an incumbent's own page (G1), a
named deployment in the segment (G2), and the outcome in words other than the vendor's. G1 fails on
its own, no incumbent's current page states the exact claim, and Checkr's own patent describes the
opposite pattern (threshold-and-queue). G2 fails independently, no named CRA deployment exists in
either company's customer material, in the sub-300-employee band or any other. With G1 and G2 both
unmet, K3 cannot fire regardless of G3/G4, so this is not DEAD.

**G3 and G4 are recorded as scored weaknesses on criterion 4**, per Part 4:

- G3: the core exhaustive-review capability is a real technical gap (evidenced by Checkr's own
  incomplete review-reduction numbers and its patent's structural human-review branch), but access
  to whatever partial automation the incumbents already have is withheld from this segment by
  channel choice, not technical inability, a distribution-shaped weakness layered on top of the
  capability one. Do not let the pitch collapse to "we serve smaller companies" alone; the harder
  and more defensible claim is the exhaustive per-hit review plus the match-confidence-to-outcome
  ledger, which no incumbent's own page describes doing at all.
- G4: no free bundle was found, but only because no segment-run platform beyond the two incumbents
  was in scope to check. This is an open evidence gap, not a cleared check, per Part 4's hard
  limit, this is now a practitioner question (does any CRA-operations platform the sub-300-employee
  segment runs day to day already bundle automated match adjudication?) for the customer call, not
  a further search question.

**Sources fetched this session:**
- https://checkr.com/products/adjudication
- https://checkr.com/our-technology/ai-powered
- https://checkr.com/products/assess
- https://checkr.com/customers
- https://patents.google.com/patent/US10878524 (US10878524B2)
- https://www.sterlingcheck.com/
- https://fadv.com/solutions/criminal-background-checks/
