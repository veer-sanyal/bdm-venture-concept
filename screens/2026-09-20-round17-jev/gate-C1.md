# Final gate: Candidate 1, Real-Time HTS Entry Line Check (customs brokerages under 300 staff)

Fresh gate agent, round 17 (METHOD.md Part 4). No verdict, no suspected killer, and no gate question was
supplied to this agent. Vendor and platform names were taken only from screen-C1.md's rung 3 and rung 4
sections (per dispatch instructions); every claim below was independently fetched from the vendor's own
page or CBP's own site this session, the screen's paraphrases were not relied on for the quotes.

**One-sentence differentiated claim under test (from ideation-C.md, section 2):** An incumbent would
already have to be claiming that its classification tool scores the probability CBP accepts a specific
proposed code against *this broker's own history of CBP redeterminations*, not just matching product text
against the tariff schedule, for this to be dead.

---

## G1, CAPABILITY

Incumbents named in rung 4 of screen-C1.md: **United Parcel Service of America Inc** (patent
US11657467B2) and **TariffLens.ai**. I independently fetched both vendor pages plus one additional
classification vendor whose own product page carries the closest language to the claim
(**GingerControl**), and one enterprise incumbent's own case-study page (**Descartes CustomsInfo**), to
check whether any incumbent already makes the exact claim.

**United Parcel Service of America Inc, US11657467B2, "Predictive commodity classification" (granted
patent, fetched at Google Patents).**
- Confidence scoring exists: "the prediction classification system 100 may determine that the classified
  predictions are of an appropriate confidence level threshold to bypass further review from a subject
  matter expert (e.g., the broker 435) entirely."
- The confidence factors named in the patent's own text: "(a) part number, (b) country of origin, (c)
  country of importation, (d) part description, (e) ancillary information/data such as licenses, and (f)
  ancillary information/data such as certificates." **No mention anywhere in the fetched text of
  calibration to an individual broker's own history of CBP redeterminations**, the confidence factors are
  product/shipment attributes, not an audit-outcome ledger.
- The patent's own example use case has the system "automatically generating a customs entry... and may
  submit the entry to a customs authority", i.e., bypassing UPS's *own* broker, not a third party's. No
  language anywhere in the fetched text describes third-party licensing or sale to independent brokerages.
- **Verdict on this incumbent: does not make the exact claim.** Confidence is scored on shipment/product
  facts, not on the broker's own redetermination history, and the capability is not sold to the segment at
  all (see G2).

**TariffLens.ai (fetched directly, tariffslens.ai homepage).**
- Claims: "defensible HTS classifications in seconds"; "Classification time reduced from 30 minutes to 30
  seconds with cited sources."
- No probability-of-CBP-acceptance claim of any kind. No mention of calibration to broker history. No
  named customers or case studies anywhere on the page.
- **Verdict: does not make the exact claim, and makes no probability claim at all.**

**GingerControl (fetched directly, gingercontrol.com homepage, the closest language found this session).**
- "Our AI re-reasons every duty decision on your entries, 100% of them, not the 2% a team can sample."
- "Every research result includes a confidence score, full GRI reasoning, and the applicable duty rate."
  "When a product could fall under multiple headings, the AI flags it and presents the top candidates with
  reasoning."
- The confidence score here is tied to **GRI reasoning quality** (is this the legally correct heading under
  the classification rules), not to **CBP acceptance probability calibrated to this broker's own audit/
  redetermination history**. Nothing on the page ties the confidence number to a customer's own historical
  CBP outcomes; it is a classification-correctness score, not an outcome-calibrated one.
- **Verdict: closest of the four, but does not make the exact claim**, it scores GRI-correctness, not
  CBP-acceptance-probability-against-this-broker's-own-history.

**Descartes CustomsInfo (fetched directly, descartes.com solution and case-study pages).**
- "AI-assisted HTS classification software," "an up-to-date database of duties, tariffs, customs
  regulations... from 175+ countries."
- No probability/confidence-scoring claim found on either fetched page. No calibration-to-audit-history
  claim.
- **Verdict: does not make the exact claim, and makes no probability claim at all.**

**G1 finding: none of the four incumbents checked claims what the differentiated claim requires.** The
nearest approach (GingerControl's per-line "confidence score") is scored against classification correctness
under GRI logic, not against a specific broker's own history of CBP redeterminations. No G1 quote clears
the bar.

---

## G2, SEGMENT (deployed to, not marketed to)

- **UPS/US11657467B2:** not sold to third parties at all on the evidence fetched, it is the assignee's own
  internal tooling, described in its own patent as bypassing *its own* broker's review. Zero deployment,
  named or otherwise, in the independent-brokerage segment. This is not marketing reach-down; there is no
  marketing to reach down from.
- **TariffLens.ai:** zero named customers of any kind on the fetched page, no segment evidence either way.
- **GingerControl:** two named testimonials, both individuals, not firms: "Michael Weick, Retired Customs
  Compliance Manager at Subaru of America" (a large manufacturer's former in-house employee, not a
  brokerage) and "Dorée Conley, Licensed Customs Broker" (an individual's professional title, with no firm
  name, staff count, or case-study numbers attached). Partner/logo mentions are trade associations (ICPA,
  HCBFFA, AAEI), not customers. **No named brokerage-firm deployment at the under-300-staff band**, at
  most a single unnamed-firm individual testimonial, which is weaker than a case study.
- **Descartes CustomsInfo:** the only named, firm-level case studies found this session are **Meggitt PLC**
  ("a leading international company specializing in high-performance components and sub-systems for the
  aerospace, defense, and selected energy markets") and **Sony Electronics**. Both are large importers/
  manufacturers running their own compliance function, not independent customs brokerages, and neither
  case study gives a staff count consistent with the under-300 band. This is exactly the marketing-reach-
  down pattern the gate brief warns about, except here it runs the other way: the vendor doesn't even
  market a brokerage angle on these pages, its actual named floor sits at large-enterprise importers.

**G2 finding: no incumbent checked has a named deployment inside the segment (independent customs
brokerages / in-house compliance desks under 300 staff).** The one candidate deployment-shaped fact
(GingerControl's individual "Licensed Customs Broker" testimonial) names a person, not a firm, and carries
no outcome data, it does not amount to a segment case study.

---

## G3, CAPABILITY OR DISTRIBUTION

The gap is **capability**, not distribution. Every confidence/scoring mechanism found this session (UPS's
patent, GingerControl's GRI confidence score) is built from product/shipment attributes or classification-
rule logic that is available at the moment of classification, none of them ingest a customer's own stream
of post-entry CBP outcomes (CF-28s, CF-29s, liquidation, penalty notices) to calibrate a probability. That
is not a pricing-tier or packaging decision an incumbent could flip on; it requires a new data pipeline (per-
customer outcome ledger, fed back over time) and a new calibration step that does not exist in any fetched
claim, at any price point, from any of the four vendors checked. No vendor page offers this capability
behind a paywall or an enterprise tier that a smaller brokerage merely doesn't get sold, the capability
itself is simply not shown to exist anywhere in the market evidence gathered this session.

---

## G4, FREE BUNDLE (platforms the segment already runs)

Checked, separately from the paid-competitor check, against the platforms named in rung 3 of screen-C1.md
plus the mandatory filing system the candidate would embed in (ideation-C.md, section 7: "embedded in the
broker's existing ABI-filing software"):

- **ABI/ACE (the Automated Broker Interface into CBP's Automated Commercial Environment).** Per CBP's own
  site (cbp.gov/trade/automated) and help.cbp.gov, ACE is the mandatory single-window data-interchange
  system through which brokers submit entry data and CBP determines admissibility, a filing and reporting
  system, not a classification-scoring engine. No search result or vendor page found this session describes
  a predictive/confidence-scoring module inside ABI/ACE itself. **Not a free bundle for this claim**, it
  is the pipe the candidate would run alongside, not a competing module inside it.
- **CROSS (rulings.cbp.gov), CBP's free rulings database.** CBP's own description (via help.cbp.gov
  Article 1199 and the cbp.gov CROSS tag page, surfaced by search after direct fetch was blocked by the
  site's client-side rendering, noted as a limitation, not a vendor quote) is a **keyword/Boolean search
  of past published rulings** ("simple or complex search characteristics using keywords and Boolean
  operators," "free access to a comprehensive database of CBP customs rulings"). It looks up precedent; it
  does not compute a probability for a new proposed code, and it is not calibrated to any individual
  broker's own history. **Free, but does not reach the differentiated claim.**
- **CBP's free Informed Compliance Publication "Reasonable Care."** Confirmed as a free, publicly posted
  PDF checklist (direct fetch of the PDF returned a 404 this session; the page hosting the link at
  cbp.gov/document/publications/reasonable-care was reachable and confirmed the free download with no
  access restriction). A checklist is not a scoring tool.

**G4 finding: no platform the segment already runs, the mandatory ABI/ACE filing interface or CBP's own
free rulings/guidance tools, bundles the differentiated claim as a zero-marginal-cost module.** The free
substitutes remove the cold, precedent-free case (CROSS) and set a due-diligence floor (the Reasonable Care
publication), but neither computes or approximates a broker-specific CBP-acceptance probability.

---

## VERDICT

**ALIVE.** K3 requires all three, quoted: the exact claim on an incumbent's own page (G1), a named
deployment in the segment (G2), and the outcome in words other than the vendor's. G1 fails outright, no
incumbent checked (UPS, TariffLens.ai, GingerControl, Descartes) claims probability-of-CBP-acceptance
calibrated to a specific broker's own redetermination history; the nearest approach (GingerControl's
GRI-correctness confidence score) is a different claim. Because G1 does not clear, G2 and the outcome
question are moot for K3 purposes, but for the record, G2 also fails (no named brokerage-firm deployment
in the under-300-staff segment was found for any of the four), so K3 would not have been reachable even if
G1 had cleared.

G3 and G4 are recorded as scored weaknesses/strengths on criterion 4, not kills: the gap is a capability
gap (G3) that no vendor shows built at any price tier, and no platform the segment is already forced to run
gives this away for free (G4), CROSS and the Reasonable Care publication cover the precedent-based and
due-diligence floor, not the predictive one.

**Remaining open question, flagged as practitioner-only per the gate's hard limit:** across every vendor
page and the granted UPS patent fetched this session, no one claims to calibrate confidence to a specific
customer's own historical audit/redetermination outcomes, not just this candidate's incumbents, but
apparently no classification vendor surfaced in this search does. Whether that is because the underlying
CBP outcome data most entries generate is too sparse/right-censored to calibrate against (most entries
liquidate without a CF-28/CF-29 ever being issued) is a question about CBP's own audit-selection behavior,
not about any vendor's roadmap, it cannot be resolved by further vendor-page searching and belongs in the
customer call, not this gate.

---

## Sources fetched or searched this session

- TariffLens.ai homepage (fetched)
- Google Patents, US11657467B2 (fetched)
- gingercontrol.com homepage (fetched)
- gingercontrol.com/blog/trade-compliance-software-buyers-guide-2026 (fetched)
- gingercontrol.com/blog/trade-compliance-software-customs-brokers-2026 (fetched)
- descartes.com/resources/knowledge-center/automating-customs-classification-descartes-customsinfo-solution (fetched)
- descartes.com/solutions/global-trade-intelligence/product-classification-and-duty-determination (fetched)
- rulings.cbp.gov and rulings.cbp.gov/help (fetch attempted; site is client-rendered, no body content returned)
- cbp.gov/document/publications/reasonable-care (fetch attempted; landing page reachable, linked PDF 404'd this session)
- WebSearch: "Descartes CustomsInfo classification HTS customers case study customs broker" (used only to
  locate the Meggitt/Sony case-study URLs, which were then fetched directly and quoted above)
- WebSearch: "CROSS" "Customs Rulings Online Search System" site:cbp.gov description free (used only because
  direct fetch of rulings.cbp.gov and help.cbp.gov returned no body content; flagged above as a search-index
  description, not a fetched vendor quote)
- WebSearch: ACE/ABI free classification prediction module (used to confirm ACE is a filing/data-interchange
  system, not a classification-scoring product)
