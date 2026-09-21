# Final gate: Candidate 2 - Prescription-Entry Look-Alike/Sound-Alike Check

**Segment given:** independent community pharmacies, under 300 staff.
**Differentiated claim given (one sentence):** An incumbent would already have to be claiming that its
verification software scores each technician entry's deviation-from-source using *this pharmacy's own
historical catch/miss pattern* - not a generic drug-interaction or national-formulary DUR check - for
this to be dead.
**Incumbents given:** PillPilot, MedAware, AESOP Technology (formerly named MedGuard/RxPrime).
**Platforms given as segment-owned:** PioneerRx, PrimeRx, EnterpriseRx, BestRx, Liberty (Liberty
Software), QS/1, ComputerRx.

All quotes below were fetched fresh this session from the vendor's own page or a vendor-issued press
release, with the URL. Where a page could not be reached, that is stated as NOT VERIFIED rather than
inferred.

---

## G1 - CAPABILITY

**PillPilot** (pillpilot.com, redirected from pillpilot.ai; segment- and PMS-matched, funded 2025).
Its own page: **"Reads the e-script, the fax, or the voice order, then fills the Data Entry screen"**;
**"Every field is checked a second time after it lands"**; **"Anything uncertain parks on a flag with
the reason attached"**; **"The agent only commits an action when it's sure."** ([pillpilot.com](https://www.pillpilot.com/))
This is a double-check-the-field claim: verify the entered field against the source a second time. It
does **not** use the words "score," "deviation," "historical," or "pattern," and it does not say the
check draws on *this pharmacy's own* past catch/miss record as opposed to the source document alone. It
does not make the exact claim.

**Liberty Software** (a PMS itself, but also the incumbent whose own page carries the closest wording).
Its own page: **"Look alike, sound alike alerts and check points, black box warnings, morphine
equivalent dosing alerts, 5-point checks and other innovative check points"** ([libertysoftware.com/pharmacy/](https://libertysoftware.com/pharmacy/)).
This names LASA alerting directly, but the page does not say whether the alert is built from a national
drug-name list or from this pharmacy's own historical entries, and it never uses "score" or "deviation."
It does not make the exact claim.

**MedAware.** Its own site (medaware.com and the /technology/ subpage) returned **HTTP 401 Unauthorized**
to this session both times it was fetched - NOT VERIFIED from the primary source this session. Falling
back to MedAware's own press release (a vendor-issued document, not a third party's): **"Ballad Health's
acute care pharmacy team is the first to natively utilize MedAware within an Epic pharmacy workflow"**
([PR Newswire](https://www.prnewswire.com/news-releases/medaware-partners-with-ballad-healths-pharmacy-team-to-bring-personalized-medication-risk-monitoring-to-rural-healthcare-302292638.html)).
No claim of technician-entry-vs-source deviation scoring appears in this release; the claim is about
patient-level medication-risk monitoring inside a hospital EHR pharmacy workflow, a different mechanism
than checking a technician's typed entry against an incoming e-prescription. Does not make the exact
claim, and the mechanism itself is different from the candidate's.

**AESOP Technology.** Its official site is **aesoptek.com** (aesoptech.com, the URL supplied in the
screen return, 301-redirects to an unrelated company, Frontline Education - a dead/wrong URL, flagged
here so the error isn't repeated). Aesoptek.com's own homepage, fetched fresh, makes **no LASA-specific
claim at all**; it names a product called "Medigator" with "Care" and "Insights" sections and no
detection-methodology language. The only LASA claim traceable to AESOP is in a 2022 vendor press
release: **"RxPrime (formerly MedGuard) not only detects errors that were not previously identified"**,
alongside a study finding that **"only about 15% of intercepted wrong drug errors... could be clearly
categorized as LASA errors"** ([PR Newswire](https://www.prnewswire.com/news-releases/a-safer-tomorrow-aesop-technologys-battle-against-look-alike-sound-alike-medication-errors-301964307.html)).
No scoring methodology, no historical-data mechanism, and no segment is named. Does not make the exact
claim, and the product name/positioning on the current site has moved away from this claim entirely.

**G1 finding: no incumbent's own page or press release makes the exact claim** (deviation-from-source
scoring built on a pharmacy's own historical catch/miss pattern). PillPilot's "checked a second time"
and Liberty's "LASA alerts and check points" are the closest, and both are a field-level double-check or
a generic-list alert, not a historical, pharmacy-specific deviation score.

---

## G2 - SEGMENT (who they actually deploy to, not who they market to)

**PillPilot.** The only customer evidence on its own page is two testimonials, both **anonymous by
role, not by name**: "Owner - multi-store pharmacy" and "Pharmacist in charge - single-store"
([pillpilot.com](https://www.pillpilot.com/)). No named pharmacy, no logo wall, no case study with a
verifiable identity was found this session. PillPilot does maintain PMS-specific landing pages (for
example a QS/1-specific page, [pillpilot.ai/qs1/](https://www.pillpilot.ai/qs1/), which states PillPilot
"fills its data-entry screens" for pharmacies "QS/1 has served... for decades") - this shows deliberate
go-to-market into the independent/retail-pharmacy PMS surface, which is evidence of intent to deploy in
this exact band, but it is still not a named deployment. **G2 for PillPilot: NOT VERIFIED - no named
customer in the segment, only anonymous testimonials and a PMS-targeted landing-page strategy.**

**MedAware.** Has a named deployment - **Ballad Health** - but Ballad Health is a hospital/health-system
acute-care pharmacy team running inside **Epic**, a hospital EHR, not an independent-pharmacy PMS
([PR Newswire](https://www.prnewswire.com/news-releases/medaware-partners-with-ballad-healths-pharmacy-team-to-bring-personalized-medication-risk-monitoring-to-rural-healthcare-302292638.html)).
This is a named deployment outside the candidate's segment (independent pharmacies under 300 staff), not
inside it. **G2 for MedAware: fails - wrong segment.**

**AESOP Technology.** No named customer, hospital, or pharmacy of any kind was found in either the
current site or the vendor press release; the only outcome evidence cited is an unattributed internal
"clinical research" study with no institution named. **G2 for AESOP: fails - no deployment found at
all, any segment.**

**G2 finding: no incumbent has a named deployment inside the independent-pharmacy segment.** MedAware's
one named deployment is a hospital, the wrong segment; PillPilot's is real go-to-market into the right
PMS surface but with no named customer, only anonymous testimonials; AESOP has no named deployment
anywhere.

---

## G3 - CAPABILITY OR DISTRIBUTION

**Versus PillPilot** (the only incumbent with full distribution already inside this exact segment and
PMS roster - it is live on PioneerRx, PrimeRx, EnterpriseRx, BestRx, Liberty, QS/1, and ComputerRx per
its own page: **"PioneerRx, PrimeRx, EnterpriseRx, BestRx, Liberty, QS/1, ComputerRx"** listed as
integrations on [pillpilot.com](https://www.pillpilot.com/)): the gap is **capability, not
distribution**. PillPilot already sells to this exact customer, on this exact PMS surface, at this
exact price point. What it does not do, per its own words, is score deviation using the pharmacy's own
historical catch/miss pattern rather than a single second-pass field check. Closing that gap requires
PillPilot to build a different scoring model on a pharmacy-specific data asset, not change a price list
- there is no distribution-only escape hatch here.

**Versus Liberty Software:** also a **capability** gap, for the same reason in reverse - Liberty already
owns 100% of its own distribution (it is the PMS itself), and what it lacks per its own page is
specificity: its LASA alerting is described as generic "check points," not scoring built from this
pharmacy's own historical pattern.

**Versus MedAware and AESOP:** here the gap reads as **distribution-shaped**. Both already claim
AI-driven error-detection technology; what is absent is deployment in the independent-pharmacy band and
integration with the independent-pharmacy PMS roster (PioneerRx, PrimeRx, BestRx, QS/1, etc.) rather than
Epic or a hospital EHR. Moving down-market and re-integrating against a different PMS surface is more
than literally "a price list" - it is real integration engineering - but it is a go-to-market and
segment decision, not evidence that the underlying detection technique cannot work outside a hospital.

**G3 answer: mixed by incumbent.** The nearest, most segment-matched competitor (PillPilot) and the
free-bundle incumbent (Liberty) both present a **capability** gap - they would have to build
pharmacy-specific historical deviation scoring, which neither claims today. The two AI-detection vendors
outside the segment (MedAware, AESOP) present a **distribution**-shaped gap - the technology exists, the
segment and PMS integration do not.

---

## G4 - FREE BUNDLE (platforms the segment already runs, checked individually)

- **Liberty Software** - own page confirms, quoted above: **"Look alike, sound alike alerts and check
  points... 5-point checks and other innovative check points"** ([libertysoftware.com/pharmacy/](https://libertysoftware.com/pharmacy/)).
  **Confirmed: a free, bundled LASA/check-point module exists inside this platform at zero marginal
  cost to the pharmacy.** Residue: the page never states whether the alert draws on a national generic
  drug-pair list or on this pharmacy's own history: on its face it reads as a generic list (it is offered
  alongside standardized items like "black box warnings" and "morphine equivalent dosing alerts," which
  are necessarily generic, not pharmacy-specific), so the pharmacy-specific historical-deviation-scoring
  claim is not what's bundled, only a generic LASA check.
- **PioneerRx** - fetched its own pharmacy-software page directly this session: it contains **no**
  claim about LASA alerts, clinical screening, or deviation checks of any kind. NOT VERIFIED as a
  zero-cost module from the page checked; this does not rule out the feature living on a different
  PioneerRx subpage not fetched this session.
- **ComputerRx, BestRx, PrimeRx, EnterpriseRx, QS/1** - no vendor-own-page LASA or deviation-scoring
  claim was located for any of these five this session. Third-party review sites (SelectHub, Capterra)
  describe generic "drug interaction," "allergy," and "dose" checks for some of them, but those are not
  the vendor's own page and are not quoted here per the evidence standard. **NOT VERIFIED for all five.**

**G4 answer: confirmed for one of the seven named platforms (Liberty), and only as a generic national-list
LASA check, not pharmacy-specific historical deviation scoring. NOT VERIFIED for the other six** - the
pages fetched or searched this session did not surface a vendor-page claim either way, so this is an open
question, not a clean bill.

---

## Verdict

**ALIVE.** K3 requires all three, quoted: the exact claim on an incumbent's own page (G1), a named
deployment in the segment (G2), and the outcome in words other than the vendor's. G1 fails outright - no
incumbent's own page or press release claims deviation-scoring built on a pharmacy's own historical
catch/miss pattern; the closest are PillPilot's "checked a second time" and Liberty's generic LASA
"check points," both a field-level or generic-list check, not the claim as written. G2 also fails - no
incumbent has a named deployment inside the independent-pharmacy segment (PillPilot: anonymous
testimonials only; MedAware: named but hospital/Epic, wrong segment; AESOP: no named deployment
anywhere). Because G1 and G2 both fail, there is no vendor claim plus in-segment deployment to test an
outcome against, so G3 (outcome in independent words) is moot - it cannot even be reached.

G3 and G4 are recorded as scored weaknesses on criterion 4, not kills: PillPilot and Liberty present a
capability gap (they would have to build historical-pattern scoring, not just change price), while
MedAware and AESOP present a distribution-shaped gap (technology exists, segment and PMS integration do
not). G4 is confirmed bundled-and-free for one of seven named platforms (Liberty) as a generic LASA list,
NOT VERIFIED for the other six.

**The gate's hard limit applies here too.** PillPilot in particular is a real, funded, segment- and
PMS-matched product doing an adjacent version of the same check ("checked a second time" vs. "scored
using this pharmacy's own history"). Whether that technical distinction - score-the-deviation versus
double-check-the-field - is one a pharmacist would actually experience as different, or would pay
differently for, is a **practitioner question for the customer call**, not a search question. Further
searching this session would not resolve it; PillPilot's and MedAware's own product pages and press
material are the ceiling of what a desk search can produce here.
