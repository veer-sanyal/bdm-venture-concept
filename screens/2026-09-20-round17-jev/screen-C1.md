# Screen: Candidate 1, Real-Time HTS Entry Line Check (customs-brokerage customer only)

Screened 2026-09-20, round 17 (Jev). Source: `ideation-C.md` lines 9-76 (primary), `ideation-B.md` lines
65-126 "2. Customs Entry Classification Second-Look" (sibling, read as additional established evidence,
broker-side only, the importer-side variant of this mistake is `H7` in `STATE.md`, already **DEAD AS
SCOPED**). This screen covers **only** the customs-brokerage-firm customer, per dispatch instructions; the
"in-house import-compliance desks at small importers" half of ideation-C's tuple is out of scope here (that
is the H7 shape).

---

## 1. THE CASE FOR

The strongest thing this candidate has that its importer-side sibling (H7) did not: **the primary
instrument binds the actual customer directly, in the customer's own name, on a statute untouched by the
tariff-regime volatility that already sank H7's headline number.** 19 U.S.C. § 1641(b)(4), fetched at
Cornell LII: *"A customs broker shall exercise responsible supervision and control over the customs
business that it conducts."* That is a broker duty, not an importer duty, unlike H7, where the $34.41B
CBP aggregate that anchored magnitude turned out to be an unattributed, 51.5x-swinging tariff-regime
artifact (`STATE.md` H7 post-check), nothing in 1641 depends on the tariff rate at all; it is a supervision
penalty, flat and structural.

**D1, VERIFIED at the primary source (re-fetched, not just carried from ideation):** 19 U.S.C. § 1592(c),
law.cornell.edu, negligence, *"the lesser of... the domestic value of the merchandise, or two times the
lawful duties, taxes, and fees"*; gross negligence, *"four times"*; fraud, *"the domestic value of the
merchandise."* Ideation-B's court-priced instance (*United States v. UPS Customhouse Brokerage*, Ct. Int'l
Trade, $75,000 / 45 misclassified entries ≈ $1,667/entry, under § 1641's supervision duty) is carried as
established per the dispatch brief and is the best D1/D2-shaped number on the sheet, a judgment against a
brokerage, for its own misclassification pattern, is exactly the customer this screen is scoped to. (Caveat
below: I did not re-fetch the CIT opinion myself this round, and the $75,000 figure sits oddly against
1641(d)(2)(A)'s $30,000 total disciplinary cap, flagged, not resolved.)

**D3, FILLED AT THE CUSTOMER.** "Customs (Brokerage) Entry Writer" is a real, populated job title at
brokerage firms specifically (not the importer-side compliance-manager title H7 used), $44k-$105k
(ZipRecruiter), $49k-$75k IQR (Glassdoor), duties stated as *"Classifying imported goods using the
Harmonized Tariff Schedule (HTS)... preparing and submitting customs entries... via ACE."* This is the
person who would use the product, employed by the exact customer, doing the exact task, today.

**Rung 6, corrected and VERIFIED from CBP's own published list, not an aggregate.** I downloaded CBP's own
national broker-permit contact list (`TA-015 Broker Permit_Contact List Final 05.2026.csv`,
cbp.gov/sites/default/files/2026-05/) and counted it programmatically: **2,516 unique nationally-permitted
broker firm names.** This is a genuinely countable source of *firms*, which the ideation tuple did not have
,  it cited "~13,000 licensed U.S. customs brokers," which is the count of individual license holders, not
firms (see weaknesses, criterion 6).

---

## 2. THE SCORED WEAKNESSES

- **Rung 1 (criterion 3).** The $75,000 UPS figure is carried from ideation-B, not independently re-fetched
  by me this round, and it exceeds 19 U.S.C. § 1641(d)(2)(A)'s own quoted cap, *"a monetary penalty not to
  exceed $30,000 in total for a violation or violations of this section"*, an internal tension I could not
  resolve without the actual CIT opinion (not fetched). Either the $75,000 rested on a different statute
  (e.g., § 1592 against UPS as the filing "person," not § 1641) or the characterization needs correction.
  Weakens criterion 3 until the opinion itself is read.
- **Rung 2 (criterion 5).** 19 U.S.C. § 1592(c)(4), fetched: prior disclosure caps negligence exposure to
  *"an amount equal to 100 percent of the lawful duties"* (interest-equivalent), a free, self-invocable,
  statutory discount that undercuts the "avoid the penalty" half of the pitch once a broker suspects an
  error, it does not touch the "avoid overpaying duty" half of the tuple's own mistake definition.
- **Rung 2 (criterion 2 unresolved).** No foreclosure clause was found in one sample broker POA form
  (packair.com, fetched) restricting data reuse, but this is one non-representative form, not an industry
  survey, so ideation-C's own "Open flag" on the broker-importer engagement letter remains **NOT VERIFIED
  either way**, exactly as ideation-C recorded it. Not resolved by this screen.
- **Rung 3, PUBLISHES (criterion 5).** CBP's own free Informed Compliance Publication "Reasonable Care" is
  confirmed live and free (cbp.gov/document/publications/reasonable-care, fetched), a free checklist
  covering classification due diligence exists already. And CBP's free CROSS ruling database is the
  standing free substitute for "what has CBP said about a similar product before", it does not reach the
  differentiated claim (a probability calibrated to one broker's own audit history), but it removes the
  cold, precedent-free case.
- **Rung 3, RATCHET (criterion 5), partial.** GRI classification genuinely admits lawful ambiguity among
  2-4 headings (unlike FDA's binary adulterated/not-adulterated), so the "may the customer lawfully act on
  the less-conservative answer" question likely clears here where it didn't for FDA Table 6, but CBP's own
  published rulings still constitute a free, precedent-based conservative default for the well-trodden
  cases, so the product's paid edge narrows to the precedent-free residue.
- **Rung 3, ABSORBS / CAPTURES / FEE-SHIFT / COMPELLED, NOT-YET-SEARCHED.** Session's web-search budget
  was exhausted before these four shapes could be run individually (customs-broker E&O insurance as an
  ABSORB candidate, ABI/ACE vendor-side error-capture-at-source tooling, a fee-shifting clause elsewhere in
  Title 19, and any COMPELLED counterparty disclosure). Recorded as a tooling gap, not a clean pass, per
  Part 3's own rule that a blank is never a clean.
- **Rung 4 (criterion 4, criterion 7).** A **granted** patent, US11657467B2 ("Predictive commodity
  classification," assignee **United Parcel Service of America Inc**, fetched at Google Patents) already
  covers a confidence-scored, entry-linked classification system that can *"bypass further review from a
  subject matter expert (e.g., the broker)"* and auto-generate the entry. It does **not** claim calibration
  to a specific broker's own history of CBP redeterminations, so it does not read on the exact
  differentiated claim, and it appears to be UPS's own internal capability (its own patent's example use
  case is bypassing *its own* broker review), not a product sold to third-party independent brokerages, so
  there is no G2 (named deployment in the independent-brokerage segment). This is not K3, but it is the
  single most concrete rung-4 finding on the sheet: one of the largest national-permit-holding brokerages
  already owns adjacent IP and, structurally, already owns more historical CBP-interaction data at higher
  volume than any startup's cold start. Also found: a live **buyer's-guide artifact for this exact
  category** ("Trade Compliance Software 2026: A Buyer's Guide to 10 Vendors," gingercontrol.com), a
  maturity signal per Part 3's demoted rung-4 check.
- **Rung 4, TariffLens.ai (criterion 4, clean).** Fetched the vendor's own comparison page directly: it does
  **not** claim probability-of-CBP-acceptance scoring calibrated to a specific broker's audit history, and
  lists no named customers or deployments. No K3 here.
- **Rung 4, exited predecessors / buyer's-tooling job posting, NOT-YET-SEARCHED** (budget exhausted).
- **Rung 5c (criterion 5, criterion 3), the sharpest unresolved risk on the sheet.** This is structurally
  the same failure mode the room's own casebook already names for cargo theft and skilled-nursing referrals:
  the overwhelming majority of entries liquidate at ~314 days (19 U.S.C. § 1504) with **no** CF-28/CF-29
  ever issued, and I could not verify this session (search budget exhausted before I could find CBP's own
  exam/audit-selection rate) whether "liquidated without challenge" is a true accept-label or simply "CBP
  never looked." If it is mostly the latter, the model trains almost entirely on a right-censored,
  low-information label, exactly the base-rate problem that already favored deterministic checks over
  prediction in the room's cargo-theft precedent. **NOT VERIFIED, and it is the single biggest open
  question for December**, not a desk-closeable one.
- **Rung 6 (criterion 6).** The ideation tuple's implied market ("~13,000 licensed U.S. customs brokers")
  conflates individual license holders with firms. CBP's own permit list gives **2,516** firms, a real
  number, but roughly one-fifth the size the tuple implied, and I have no verified per-seat or per-line
  price point to turn that into a TAM this round.
- **Rung 1.5, patent search, S only, not a kill, but see rung 4 above** for the UPS patent; a second
  differently-numbered continuation, US11145020B2, appears to be the same family (not independently opened
  this round).

---

## 3. KILL

**NO KILL.**
- **K1** does not fire, 1641 prices a real dollar against the broker directly (the UPS judgment), and the
  broker does not control whether CBP assesses it, but the money is genuinely at stake at one customer.
- **K2** does not fire, 1641(b)(4), read directly, names the customs broker as the duty-holder. This is
  the one rung where the broker-as-customer framing is cleanly better than H7's importer-as-customer
  framing, which had to reach for 1484/1592 (largely importer-facing) to make its case.
- **K3 CANDIDATE** does not fire, no vendor page quotes the exact differentiated claim (TariffLens
  checked directly and does not); the one adjacent granted patent (UPS) has no G2 (named deployment sold
  into the independent-brokerage segment) and is not shown solved there.

---

## 4. D3 STATE

**FILLED AT THE CUSTOMER.** "Customs (Brokerage) Entry Writer" / "Customs Entry Writer," band $44k-$105k
(ZipRecruiter) / $49k-$75k IQR (Glassdoor) / $41.6k-$58.6k (Salary.com), duties stated as HTS classification
plus entry preparation and submission via ACE/ABI, this is the exact task, at the exact customer. **NOT
VERIFIED AT PAGE**: direct fetch of the ZipRecruiter listing page returned HTTP 403, consistent with the
standing toolchain limit already recorded in `METHOD.md` Part 2b (every major job board 403s on fetch);
figures above are aggregator-reported, title-level, not read from a state portal or an employer's own ATS.

---

## 5. MUTATION

**NONE.** No principled mutation exists beyond the formulation ideation-C already chose. The two obvious
alternate formulations are each independently worse, and the forcing evidence for saying so came out of
this screen, not before it:
1. **Selling to the importer instead of the broker** is simply H7, already screened **DEAD AS SCOPED** in
   `STATE.md` on the same statute cluster (19 CFR 111.1 / H350722), the same magnitude fragility, and the
   same RATCHET/GIVES pattern.
2. **Retreating to a "general classification database, disconnected from a specific entry"**, the shape
   H350722 is reported (via secondary commentary, not the primary ruling text, see below) to bless, would
   discard exactly the differentiated claim (real-time, at-the-entry-line, broker-history-calibrated), which
   is the same conclusion `STATE.md` already reached for H7's own commoditized-product alternative.

So the current scoping (customer = the licensed brokerage itself; product = decision support surfaced to
the entry writer, broker retains sign-off; real-time, inside the ABI workflow) is the formulation to keep,
not a formulation to fix.

---

## 6. RUBRIC SCORES

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Clarity of target customer | **4** | Named precisely (licensed customs brokerage firm, sub-300 staff, entry writer as the user) and counted from CBP's own permit list (2,516), short of 5 only because that list is *national*-permit firms and may undercount local-permit-only brokers |
| 2 | Clarity of JTBD | **4** | "Tell me before I submit whether CBP will accept this code, so I don't eat a penalty or leave duty on the table", practitioner-recognizable, GRI/entry-writer vocabulary matches |
| 3 | Significance and magnitude of unmet need | **3** | Two tiers clear (D1 statutory + D3 filled), but capped, no call was made this round (standing rule), the $75,000 figure carries an unresolved statutory tension, and the rung-5c base-rate question directly threatens whether the "unmet need" is dense or rare |
| 4 | Differentiation and uniqueness | **2** | No K3, but a granted, on-point-adjacent patent already sits with one of the largest national-permit brokers, and a buyer's guide for the category already exists |
| 5 | Performance improvement over existing solutions | **2** | The 1f asset (observed, not computed) is real, but RATCHET, GIVES, and § 1592(c)(4)'s free statutory discount all narrow the paid edge, and rung 5c threatens whether the loop compounds at all |
| 6 | Size of market opportunity | **3** | Sized from a genuinely countable government source (2,516 firms) for the first time on this candidate, but materially smaller than assumed and with no verified price point yet |
| 7 | Market/technical/execution risk | **2** | The same licensing-ambiguity family that forced H7 to "DEAD AS SCOPED" is unresolved here too, better-positioned (customer is already the licensed party; product is decision-support, not autonomous filing) but not settled, and I could not get the primary ruling text to confirm the favorable reading myself this round |

**Lowest criterion: 2** (tied on 4, 5, 7). **Sum: 20.**

---

## 7. VERIFIED / NOT VERIFIED

**VERIFIED (fetched primary or countable source myself this session):**
- https://www.law.cornell.edu/uscode/text/19/1592, 19 U.S.C. § 1592(c) penalty tiers, (c)(4) prior disclosure, (d) restoration of duties
- https://www.law.cornell.edu/uscode/text/19/1641, 19 U.S.C. § 1641(b)(4) supervision duty, (b)(6) unlicensed-person penalty, (d)(2)(A) disciplinary cap
- https://www.cbp.gov/document/publications/reasonable-care, free CBP Informed Compliance Publication exists
- https://www.cbp.gov/sites/default/files/2026-05/TA-015%20Broker%20Permit_Contact%20List%20Final%2005.2026.csv, downloaded and counted directly: 2,516 unique permitted broker firm names
- https://patents.google.com/patent/US11657467B2/en, granted patent, assignee UPS, confidence-based classification with broker-bypass mechanism
- https://www.tarifflens.ai/compare, vendor page checked directly; does not claim the differentiated claim, no named customers
- https://www.packair.com/Forms/POA.pdf, sample POA form; no confidentiality/data-reuse clause present (one non-representative sample only)

**NOT VERIFIED (secondary summaries, fetch failures, or unrun this session, none used to support a kill):**
- CBP HQ H350722 itself, every attempt to fetch the ruling's own text (rulings.cbp.gov/ruling/H350722, the CROSS getdoc PDF, Mondaq's writeup) either returned a 500 error, navigation-only content, or an unrelated document. Everything about it here (including the favorable "does not address broker-internal tool use" reading and the six-digit/beyond-six-digit line) comes from secondary law-firm and vendor-blog commentary (customsandinternationaltradelaw.com, gingercontrol.com/blog/ai-hts-classification-tools-legal-requirements, gingercontrol.com/blog/ai-in-trade-compliance), not the primary ruling. `STATE.md`'s own prior H7 analysis claims this ruling was independently fetched and verified in an earlier round; I could not reproduce that this round and am not carrying its exact quotes forward as re-verified by me.
- *United States v. UPS Customhouse Brokerage* $75,000/45-entries figure, carried from ideation-B, not re-fetched against the CIT opinion this round; the $30,000 statutory-cap tension is unresolved
- ZipRecruiter, Glassdoor, Salary.com entry-writer compensation figures, search-summary level only; direct fetch of the ZipRecruiter listings page returned HTTP 403
- CBP's entry examination/audit-selection rate (needed for rung 5c's base-rate question), session's web-search budget was exhausted before this could be run
- Customs-broker E&O insurance as an ABSORB substitute, ABI/ACE vendor CAPTURE tooling, a Title 19 fee-shift clause, and any COMPELLED counterparty disclosure, none searched this session (budget exhausted); recorded as gaps, not clean passes
- Exited predecessors and a buyer-side job posting naming installed tooling (rung 4), not searched this session
