# H7 licensing check - primary-source verification

Verification pass, 2026-09-11. Every claim below was checked against a fetched primary
source. Where a source could not be reached, the verdict says NOT VERIFIED and nothing
is inferred from secondary coverage.

Subject under test: a pre-filing product that tells a US importer which line items on an
entry summary are most likely to draw a CF-28 or CF-29 on classification or valuation.
Blocking question: is selling that "customs business" under 19 CFR Part 111.

---

## Claim 1 - 19 CFR 111.1 definition of "customs business" and its exclusions

**VERDICT: VERIFIED.** Source: https://www.law.cornell.edu/cfr/text/19/111.1 (fetched
2026-09-11, raw HTML pulled and de-tagged, not a summary).

Verbatim, the whole definition:

> **Customs business.** "Customs business" means those activities involving transactions
> with CBP concerning the entry and admissibility of merchandise, its classification and
> valuation, the payment of duties, taxes, or other charges assessed or collected by CBP
> on merchandise by reason of its importation, and the refund, rebate, or drawback of
> those duties, taxes, or other charges. "Customs business" also includes the preparation,
> and activities relating to the preparation, of documents in any format and the electronic
> transmission of documents and parts of documents intended to be filed with CBP in
> furtherance of any other customs business activity, whether or not signed or filed by the
> preparer. However, "customs business" does not include the mere electronic transmission
> of data received for transmission to CBP and does not include a corporate compliance
> activity.

There are exactly two exclusions, both in the final sentence: (a) mere electronic
transmission of data received for transmission to CBP, and (b) corporate compliance
activity. Verbatim definition of the second:

> **Corporate compliance activity.** "Corporate compliance activity" means activity
> performed by a business entity to ensure that documents for a related business entity or
> entities are prepared and filed with CBP using "reasonable care", but such activity does
> not extend to the actual preparation or filing of the documents or their electronic
> equivalents. For purposes of this definition, a "business entity" is an entity that is
> registered or otherwise on record with an appropriate governmental authority for business
> licensing, taxation, or other legal purposes, and the term "related business entity or
> entities" encompasses a business entity that has more than a 50 percent ownership interest
> in another business entity, a business entity in which another business entity has more
> than a 50 percent ownership interest, and two or more business entities in which the same
> business entity has more than a 50 percent ownership interest.

Also on the same page, verbatim:

> **Customs broker.** "Customs broker" means a person who is licensed under this part to
> transact customs business on behalf of others.
>
> **Person.** [see claim 2 - 19 CFR 111.1 defines "person" to include individuals,
> partnerships, associations, and corporations; quoted through HQ H350722 below.]

**On the specific sub-question asked:** the corporate-compliance exclusion does NOT reach
an outside software vendor. The text is closed on its face. It covers activity a business
entity performs for a *related* business entity, and "related" is defined by a more-than-50-
percent ownership interest running in either direction or from a common parent. A vendor
selling to unaffiliated importers has no ownership relation to them and is outside the
exclusion. A second limit bites independently: even inside a corporate family, the exclusion
"does not extend to the actual preparation or filing of the documents or their electronic
equivalents."

---

## Claim 2 - CBP ruling HQ H350722 (January 2026)

**VERDICT: VERIFIED, and materially stronger and more specific than the paraphrase.**

Source: https://rulings.cbp.gov/api/getdoc/hq/2026/H350722.pdf (PDF fetched and text-
extracted 2026-09-11). Landing page: https://rulings.cbp.gov/ruling/H350722

The ruling is real. Header, verbatim: "HQ H350722 / January 16, 2026 / OT:RR:CTF:EPDR
H350722 SAB / CATEGORY: Entry / RE: Online platform; conducting customs business without a
license." Signed by Yuliya A. Gulis, Director, Commercial and Trade Facilitation Division.
It is internal advice requested by the Automotive and Aerospace Center of Excellence and
Expertise, dated July 23, 2025. The subject is an unnamed foreign "Unlicensed Company"
running an online platform with four services: broker matchmaking, an OCR tool that culls
entry data from shipping documents, an AI HTSUS classification tool, and submission of CBP
Form 5106.

**The HOLDING, verbatim and in full:**

> The Unlicensed Company is not conducting customs business by connecting importers to
> brokers if the company is merely acting as an intermediary in the transmission of
> electronic data. The Unlicensed Company is impermissibly conducting customs business by:
> developing an OCR tool that identifies what data will appear on an entry; deriving HTSUS
> subheading suggestions beyond the six-digit level via its AI classification tool if the
> merchandise being classified will be entered; and, submitting and certifying CBP Form 5106
> on behalf of others.

Each sub-claim in the outside analysis, checked against the ruling's own words:

**(a) Six-digit suggestions may be permissible - VERIFIED.**

> Accordingly, if the Unlicensed Company's AI classification tool only derives potential
> HTSUS subheadings to the six-digit level, then customs business is not being conducted.
> However, if the AI classification tool is deriving subheadings beyond the six-digit level,
> then a customs broker's license is generally required if that classification information
> will or may eventually be used for an entry.

The six-digit line is not new here; the ruling traces it to HQ H260075 (Apr. 3, 2017), which
held classification for an Importer Security Filing is not customs business "so long as the
HTS[US] number is not reported past the six-digit level," and conversely "[i]f the number is
reported to the ten-digit HTSUS level, then [it] concerns classification for purposes of
customs business and requires a license." The stated rationale: "filing an entry with CBP
requires classifying merchandise to the ten-digit level."

**(b) US-specific classification beyond six digits for actual or intended imports is
customs business - VERIFIED.**

> Consequently, if the Unlicensed Company's AI classification tool is deriving subheadings
> to the ten-digit level for merchandise that has been imported, or is intended to be
> imported, then customs business is being impermissibly conducted by an unlicensed entity
> classifying merchandise for which an entry is required to be filed with CBP.

And the nexus test, verbatim:

> The nexus to a prospective entry is established when the merchandise being classified is
> imported, or is intended to be imported, because all merchandise imported into the United
> States is required to be entered unless specifically exempt. 19 C.F.R. § 141.4(a).

**(c) General research disconnected from a real import can be permissible - VERIFIED, but
narrower than "disconnected from a real import."** The permission is conditional on three
things at once, and the ruling calls the boundary a "fine line" (quoting HQ H272798):

> Accordingly, to the extent that the tool is providing customers with general classification
> information that is disconnected from an actual or intended importation of merchandise
> requiring entry, then so long as the Unlicensed Company's disclaimer is meaningfully
> implemented, we find that this tool is akin to the narrowly permissible database in
> HQ H272798.
>
> In summary, so long as the Unlicensed Company's AI classification tool operates separately
> from the portal connecting importers to brokers for entry purposes, such that the tool does
> not direct either party on the proper classification which should appear on an entry and
> the disclaimer is meaningfully implemented, then it is permissible.

Note what the safe-harbour example actually was: in HQ H272798 (Jan. 26, 2017) the database
was available to clients "regardless of whether [a] particular product is ever actually
imported into the United States." The distinguishing fact the ruling identifies:

> A key distinction between the database at issue in HQ H272798 versus the classification
> information provided in HQ H290535 was that clients in the former situation could access
> the database for all products irrespective of whether they purchased or imported any
> specific merchandise – whereas in HQ H290535, the clients sought to classify the exact
> merchandise they purchased and imported.

**(d) A disclaimer does not save a product that in fact influences an entry - VERIFIED.**
Via HQ H290535 (Sept. 29, 2022), summarized in H350722:

> CBP determined the company was impermissibly conducting customs business despite the
> inclusion of a disclaimer because it was "providing specific subheadings on specific goods
> that its clients have ordered and for which they will be filing entry documentation with
> C[BP]." CBP explained that if a customer requests subheading information prior to importing
> merchandise then "there is a strong possibility that the customers will use subheadings
> provided on the entry filed with CBP," such that by providing the requested information a
> company in effect directs customs brokers on how to prepare the requisite entry documents.
> CBP thus held that including a disclaimer did not absolve the company from impermissibly
> conducting customs business.

**(e) Software that extracts and decides which document data belongs on an entry can cross
the line - VERIFIED, and the ruling is blunter than "can."** On the OCR tool:

> We stress that the filing of an entry is not a prerequisite to such an activity constituting
> customs business because 19 U.S.C. § 1641(a)(2) explicitly encompasses preparation of
> documents or forms in any format, or parts thereof, which are ultimately intended to be
> filed with CBP. An OCR tool which identifies precise pieces of information for a shipment
> intended to be entered thus entails customs business because it prepares parts of the data
> appearing on an entry in an electronic format.
>
> In summary, whether data is extracted manually or automatically though an OCR tool, CBP has
> repeatedly held that an unlicensed entity cannot decide what data should appear on an entry.

**A finding the outside analysis omitted, and it is the most dangerous one for a software
product.** H350722 holds that a tool is not a person, so a licensed human must own the
decision the tool automates:

> A licensed individual broker is therefore a precondition to conducting customs business on
> behalf of others, whether conducted by that individual or by a legal person such as a
> partnership or corporation. This precondition necessarily extends to automated tools – if
> such tools are utilized to conduct customs business, then an individual broker or other
> licensed person must have a role in specifying what information, like value or
> classification, is automatically generated by the tool's decision matrix and ultimately
> appears on an entry filed with CBP. A tool does not constitute a "person" as defined by
> 19 C.F.R. § 111.1, such that the actual decision regarding the classification of imported
> merchandise, or any other information needed to make entry, must be made by a duly licensed
> customs broker.

Two further omitted findings, both structural:

> if the Unlicensed Company instead contracted to utilize an OCR tool developed by another
> unlicensed entity as part of the Unlicensed Company's online platform, we find that the
> company would still be impermissibly conducting customs business akin to the bureau in HQ
> H068278. In such a circumstance, the Unlicensed Company is conducting customs business
> through its unlicensed contractor by directing the contractor to create a decision matrix
> identifying what data will appear on an entry.

That is, buying the model from a third party does not cure it. And on where the work happens,
quoting 19 CFR 111.3(a): "[c]ustoms business must be conducted within the customs territory of
the United States as defined in § 101.1 of this chapter" - defined as "the States, the District
of Columbia, and Puerto Rico."

---

## Claim 3 - CBP has ruled that checking tariff numbers before entry is customs business when corrected classification information might end up on the entry

**VERDICT: VERIFIED.** The ruling is HQ 115248, dated August 28, 2001 (BRO-1-RR:IT:EC 115248
GG), issued to Casio Corporation of America. Source, fetched and converted 2026-09-11:
https://rulings.cbp.gov/api/getdoc/hq/2001/115248.pdf (served as a Word document; converted
locally). It is also the ruling H350722 cites for this proposition.

The operative paragraph, verbatim:

> The verification of tariff numbers prior to entry is a customs business activity when the
> possibility exists that corrected classification information derived from the verification
> process will end up on the entry. This is because such verification is "an activity relating
> to the preparation" of the entry documentation. CCA may not perform classification
> verifications on merchandise ordered by its sister companies under such circumstances.

The reasoning it rests on, verbatim:

> To give effect also to the second sentence of the statutory "customs business" definition,
> cited above, it is evident that the preparation of the entry documents, and the gathering of
> the information which will be placed on those documents, are customs business activities.
> This gathering of information is an activity "relating to the preparation" of the entry
> documents. In the classification context, this means that a person will require a broker's
> license not only to prepare entry documents for another person, but also to gather
> classification data which will be reflected on the entry.

From the HOLDING, verbatim:

> When the possibility exists that corrected classification and duty information derived from a
> verification process will be reflected on the entry, such verification is an activity related
> to the preparation of entry documents and, as such, is customs business.

**Three facts about HQ 115248 that make it worse for this product than the paraphrase
suggests, not better:**

1. The test CBP applied is *possibility*, not intent and not use: "when the possibility exists
   that corrected classification information derived from the verification process will end up
   on the entry."
2. The same paragraph's logic was extended to **valuation-adjacent checking**. On duty
   verification: "this type of duty verification may only be performed by the importer or by a
   licensed broker when the possibility exists that corrected duty information derived from the
   duty verification process will ultimately appear on the entry."
3. CCA was a **wholly-owned sister subsidiary** of the importers it served, and it still lost.
   CBP: "Subsidiary sister corporations, although related through common ownership, are separate
   legal persons... Therefore, an unlicensed corporation may not conduct customs business on
   behalf of a related sister corporation." An arm's-length SaaS vendor is further from the line
   than CCA was, not closer.

A second supporting ruling, HQ 114654 (May 28, 1999), quoted in H350722, draws the
teach-versus-advise line verbatim:

> as a general rule, unlicensed persons may instruct others on customs laws, regulations,
> policies and procedures . . . they may explain the use of the Harmonized Tariff Schedules . . .
> or provide an overview of the different methods of valuation. They may not, however, advise a
> client on how to classify, appraise, or mark merchandise that is going to be the subject of an
> entry.

---

## Claim 4 - 19 U.S.C. 1641 and the "up to $10,000 per transaction" penalty

**VERDICT: VERIFIED as to the number, but the claim as stated omits a scienter element that
matters.** Source: https://www.law.cornell.edu/uscode/text/19/1641 (raw page fetched
2026-09-11).

19 U.S.C. § 1641(b)(1), verbatim:

> No person may conduct customs business (other than solely on behalf of that person) unless
> that person holds a valid customs broker's license issued to that person under paragraph (2)
> or (3) of this subsection.

19 U.S.C. § 1641(b)(6), verbatim - this is the unlicensed-practice penalty:

> Any person who intentionally transacts customs business, other than solely on the behalf of
> that person, without holding a valid customs broker's license granted to that person under
> this subsection shall be liable to the United States for a monetary penalty not to exceed
> $10,000 for each such transaction as well as for each violation of any other provision of this
> section. This penalty shall be assessed in the same manner and under the same procedures as
> the monetary penalties provided for in subsection (d)(2)(A).

Exactly what it attaches to and to whom:

- **Who:** any "person" - 19 CFR 111.1 defines person to include corporations - who
  **intentionally** transacts customs business other than solely on their own behalf without a
  licence. The word "intentionally" is in the statute. The prohibition in (b)(1) has no such
  qualifier; the *penalty* in (b)(6) does.
- **What unit:** "not to exceed $10,000 **for each such transaction** as well as **for each
  violation of any other provision of this section**." It is a per-transaction ceiling, not a
  fixed amount, and it stacks across transactions.
- **Separate track for licensed brokers:** § 1641(d)(2)(A) lets CBP serve notice on a *broker*
  "to show cause why the broker should not be subject to a monetary penalty not to exceed
  $30,000 in total for a violation or violations of this section," alongside revocation or
  suspension. That is the disciplinary track and applies to someone who holds a licence.

**Caveat flagged, not resolved:** these statutory figures are subject to annual civil-penalty
inflation adjustment across DHS. The $10,000 is the figure in the statute's own text; the
currently enforceable adjusted amount was not verified in this pass. NOT VERIFIED as to the
2026 adjusted figure.

---

## Claim 5 - 19 CFR 111.11, the organizational licence, national permit, responsible supervision

**VERDICT: VERIFIED.** Sources fetched 2026-09-11:
https://www.law.cornell.edu/cfr/text/19/111.11 , /111.19 , /111.28 , /111.1

**How many licensed individuals a corporation needs - 19 CFR 111.11(c), verbatim:**

> (c) Association or corporation. In order to qualify for a broker's license, an association or
> corporation must:
> (1) Be empowered under its articles of association or articles of incorporation to transact
> customs business as a broker; and
> (2) Have at least one officer who is a broker.

So: **one licensed individual, and that individual must be an officer.** Not merely an employee.
(By contrast 111.11(b): "a partnership must have at least one member of the partnership who is
a broker.") The individual's own prerequisites, 111.11(a), verbatim in substance: US citizen and
not a federal officer or employee, at least 21, "of good moral character," and a passing grade
(75 percent or higher) on the broker exam taken within the 3-year period before application.

**National permit - 19 CFR 111.19(a), verbatim:**

> A national permit is required for the purpose of transacting customs business throughout the
> customs territory of the United States as defined in § 101.1 of this chapter.

The application under 111.19(b) requires, among eleven listed items, "(7) A list of all employees
together with the specific employee information prescribed in § 111.28 for each employee" and
"(8) A supervision plan describing how responsible supervision and control will be exercised over
the customs business conducted under the national permit, including compliance with § 111.28".
The qualifying individual must be "a licensed broker employed by the partnership, association, or
corporation."

**What responsible supervision and control demands - the definition in 19 CFR 111.1, verbatim:**

> "Responsible supervision and control" means that degree of supervision and control necessary to
> ensure the proper transaction of the customs business of a broker, including actions necessary
> to ensure that an employee of a broker provides substantially the same quality of service in
> handling customs transactions that the broker is required to provide.

**19 CFR 111.28(a), verbatim opening:**

> Every individual broker operating as a sole proprietor, every licensed member of a partnership
> that is a broker, and every licensed officer of an association or corporation that is a broker
> must exercise responsible supervision and control (see § 111.1) over the transaction of the
> customs business of the sole proprietorship, partnership, association, or corporation. A sole
> proprietorship, partnership, association, or corporation must employ a sufficient number of
> licensed brokers relative to the job complexity, similarity of subordinate tasks, physical
> proximity of subordinates, abilities and skills of employees, and abilities and skills of the
> managers.

Note the second sentence: the floor is one licensed officer to *qualify*, but the ongoing
obligation is "a sufficient number of licensed brokers relative to the job complexity," which
scales with volume. 111.28(a) then lists thirteen non-exclusive factors CBP may weigh, including
"(3) The volume and type of business conducted by the broker", "(4) The reject rate for the
various customs transactions relative to overall volume", "(6) The availability of a sufficient
number of individually licensed brokers for necessary consultation with employees of the broker",
and "(8) The frequency of audits and reviews by an individually licensed broker of the customs
transactions handled by employees of the broker."

111.28(b) additionally requires the national permit holder to file, before transacting any customs
business, a list of every employee with "name, social security number, date and place of birth,
date of hire, and current home address," updated within 30 days of any change, new hire, or
termination.

**Read together with the H350722 automation holding (claim 2), the practical requirement for an
automated product is not "have a licensed officer on the cap table." H350722: "an individual
broker or other licensed person must have a role in specifying what information, like value or
classification, is automatically generated by the tool's decision matrix and ultimately appears
on an entry."**

---

## Claim 6 - CBP's "$34.41 billion net revenue recovered due to Entry Summary Reviews, FY2025"

**VERDICT: VERIFIED as to both figures. REFUTED as to any classification / clawback / penalty
characterization. NOT VERIFIED as to any explanation for the 50x jump - no explanation exists on
the page or in any source reached.**

Source: https://www.cbp.gov/newsroom/stats/trade - raw HTML fetched and de-tagged 2026-09-11
(not the WebFetch summary; the numbers below were read out of the page source). Page footer:
"Last Modified: Aug 24, 2026."

**The exact label, verbatim:** "Net Revenue Recovered due to Entry Summary Reviews (ESF)".
It sits inside the table "Trade Enforcement Activities".

**The full row, verbatim, all six fiscal years:**

| FY 2026 | FY 2025 | FY 2024 | FY 2023 | FY 2022 | FY 2021 |
|---|---|---|---|---|---|
| $7,898,144,437 | $34,410,000,000 | $667,550,000 | $256,360,000 | $267,370,000 | $473,620,000 |

Both claimed numbers check out: FY2025 = $34.41 billion, FY2024 = $667.55 million. That is a
51.5x year-over-year increase.

**Does CBP say it is caused by classification errors, or that it is clawbacks or penalties?
No. The claim that CBP does not say this is correct, and the page's own structure argues
against the penalty reading.**

- The label says only "Net Revenue Recovered due to Entry Summary Reviews (ESF)." There is no
  breakdown by error type, no mention of classification, no mention of valuation, no mention of
  penalty.
- No footnote defines "ESF" or the line's scope. The only notes attached anywhere near it are
  "1, 2 FY 2026 and FY 2025 are updated as of July 27, 2026" and the blanket disclaimer:
  "Figures are not official statistics of United States. Source: US Customs and Border
  Protection: Use for monitoring purposes only."
- **Penalties are a separate row in the same table.** "Total Collected from Trade Penalties and
  Liquidated Damages" is $46,040,000 for FY2025 - three orders of magnitude below the ESF line.
  So the ESF figure is definitionally not penalty revenue; CBP counts penalty revenue elsewhere.
- **Audits are also a separate row.** "Total Collected as a result of Importer Audits" is
  $235,460,000 for FY2025.

Anyone using the $34.41B as a proxy for money recovered from classification mistakes is
attributing a cause CBP never states, on a line CBP labels only by the process that produced it.

**On the 50x jump - no explanation was found, and the same table shows the denominators also
moved hard.** All from the same page, verbatim:

- "Total Duty, Taxes, and Fees Collected": FY2024 $88,078,654,581 → FY2025 $216,711,007,541.
  That is 2.46x, not 51.5x.
- "Total Entry Summaries": FY2024 38,362,713 → FY2025 50,084,153. That is 1.31x.
- Trade-remedy duties assessed appear for the first time or expand sharply in FY2025 and FY2026
  across new programs (Automobiles $17.68B FY2025 from nothing in FY2024; Derivatives of Steel
  and Aluminum $52.77M FY2024 → $13.12B FY2025; Section 122 All Products $31.06B first appearing
  FY2026, "Effective February 24, 2026").

So the ESF line grew about 21x faster than total duty collections and about 39x faster than entry
volume. Neither CBP nor any source reached explains the residual.

**Searched for an explanation and did not find one.** The only contemporaneous trade-press item
located is International Trade Today, Aug. 13, 2025, "CBP: Net Revenue Raised From Entry Summary
Reviews Catapults to $25B", which reports the number rising ($25.6 billion as of June 30, FY2025)
but is paywalled beyond a preview and offers no cause, no CBP statement, and no composition
breakdown in the accessible portion. **NOT VERIFIED: any explanation of the jump.**
**NOT VERIFIED: whether the definition of the ESF line changed between FY2024 and FY2025.** CBP
publishes no definition of the line on this page, so a definitional change could not be ruled in
or out from the primary source.

**One more fact the project should not skip: the line is already falling.** FY2026, updated
through July 27, 2026 (roughly ten months into the fiscal year), stands at $7,898,144,437  - 
about 23 percent of the FY2025 figure. A line that went from $0.67B to $34.41B to $7.9B in three
years is not a market size. It is a number whose generating process is unexplained and unstable.

---

## Claim 7 - 19 U.S.C. 1592(c) penalty tiers, caps, and 1592(d)

**VERDICT: VERIFIED on both points.** Source: https://www.law.cornell.edu/uscode/text/19/1592
(raw page fetched 2026-09-11).

**The subsection is titled, verbatim, "(c) Maximum penalties."** That word is the statute's own,
not a gloss. The three culpability tiers, verbatim:

> **(1) Fraud.** A fraudulent violation of subsection (a) is punishable by a civil penalty in an
> amount not to exceed the domestic value of the merchandise.
>
> **(2) Gross negligence.** A grossly negligent violation of subsection (a) is punishable by a
> civil penalty in an amount not to exceed - 
> (A) the lesser of -  (i) the domestic value of the merchandise, or (ii) four times the lawful
> duties, taxes, and fees of which the United States is or may be deprived, or
> (B) if the violation did not affect the assessment of duties, 40 percent of the dutiable value
> of the merchandise.
>
> **(3) Negligence.** A negligent violation of subsection (a) is punishable by a civil penalty in
> an amount not to exceed - 
> (A) the lesser of -  (i) the domestic value of the merchandise, or (ii) two times the lawful
> duties, taxes, and fees of which the United States is or may be deprived, or
> (B) if the violation did not affect the assessment of duties, 20 percent of the dutiable value
> of the merchandise.

**Point one - maximums subject to caps, not automatic multipliers: VERIFIED.** Every tier reads
"not to exceed." The 4x and 2x multipliers are not standalone figures; each is the second half of
a "lesser of" test capped by the domestic value of the merchandise. A "2x duties" penalty can
therefore never exceed the goods' domestic value, and where duties were unaffected the cap drops
to a flat 20 or 40 percent of dutiable value. Quoting a headline "four times duties" without the
lesser-of cap and the "not to exceed" overstates exposure.

Also within (c): **19 U.S.C. § 1592(c)(4) prior disclosure** sharply reduces the ceiling for a
self-reporting importer - for negligence or gross negligence, to "the interest (computed from the
date of liquidation at the prevailing rate of interest applied under section 6621 of title 26) on
the amount of lawful duties, taxes, and fees of which the United States is or may be deprived so
long as such person tenders the unpaid amount." For fraud, to 100 percent of the duties deprived.
That is a material fact about the shape of the problem a pre-filing product claims to address.

**Point two - unpaid duties remain due regardless: VERIFIED.** 19 U.S.C. § 1592(d), verbatim and
in full:

> **(d) Deprivation of lawful duties, taxes, or fees.** Notwithstanding section 1514 of this
> title, if the United States has been deprived of lawful duties, taxes, or fees as a result of a
> violation of subsection (a), the Customs Service shall require that such lawful duties, taxes,
> and fees be restored, whether or not a monetary penalty is assessed.

"Shall require" and "whether or not a monetary penalty is assessed" are both in the text. Duty
restoration is mandatory and independent of the penalty track.

---

## Sources fetched

- 19 CFR 111.1 - https://www.law.cornell.edu/cfr/text/19/111.1
- 19 CFR 111.11 - https://www.law.cornell.edu/cfr/text/19/111.11
- 19 CFR 111.19 - https://www.law.cornell.edu/cfr/text/19/111.19
- 19 CFR 111.28 - https://www.law.cornell.edu/cfr/text/19/111.28
- 19 U.S.C. 1641 - https://www.law.cornell.edu/uscode/text/19/1641
- 19 U.S.C. 1592 - https://www.law.cornell.edu/uscode/text/19/1592
- HQ H350722 (Jan. 16, 2026) - https://rulings.cbp.gov/api/getdoc/hq/2026/H350722.pdf
- HQ 115248 (Aug. 28, 2001) - https://rulings.cbp.gov/api/getdoc/hq/2001/115248.pdf
- HQ 114654 (May 28, 1999) - https://rulings.cbp.gov/api/getdoc/hq/1999/114654.pdf
- CBP Trade Statistics - https://www.cbp.gov/newsroom/stats/trade (last modified Aug 24, 2026)

Rulings cited inside H350722 and relied on above but not independently fetched in this pass:
HQ H260075 (Apr. 3, 2017), HQ H272798 (Jan. 26, 2017), HQ H290535 (Sept. 29, 2022),
HQ H326926 (Dec. 19, 2023), HQ H068278 (Sept. 28, 2009), HQ H258556 (Sept. 6, 2017).
Their language above is quoted as H350722 quotes them, which is stated at each point.
