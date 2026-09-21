# Screen B3a, Claims-file compliance severity grading for auto/GL TPAs

Candidate as dispatched (not from an ideation file): TypeSafe AI Jev-scored ledger grading every closed
auto/GL claim file at a small regional-insurer TPA (<300 employees) against state Unfair Claims Settlement
Practices standards, correlated to the TPA's own prior DOI market-conduct exam findings and complaint
dispositions. Checker named in the dispatch: the state DOI market-conduct examiner applying Cal. Ins. Code
§790.035 and 10 CCR §2695.1 et seq. (the Fair Claims Settlement Practices Regulations, "FCSPR"), plus other
states' equivalents.

---

## 1. THE CASE FOR

The strongest number reached is a **statutory ceiling, not a customer-attached demand tier**: Cal. Ins.
Code §790.035 caps the civil penalty at **"five thousand dollars ($5,000) for each act"** and, for a
willful violation, **"ten thousand dollars ($10,000) for each act"** (fetched, leginfo.legislature.ca.gov,
Article 6.5 full text). This is a real, quotable magnitude, but it is not a D1, because (see KILL below)
the penalty does not attach to the customer this candidate sells to. No D1/D2/D3 was reached that prices
the mistake at the TPA itself; the ladder stopped at rung 2 before the demand ladder (rung 2.5) ran.

The best rung-2-adjacent finding is negative for the candidate as specified, but it is precise: the
FCSPR's own definitions section, 10 CCR §2695.2(i), defines **"Insurer"** as *"a person licensed to issue
or that issues an insurance policy or surety bond in this state, or that otherwise transacts the business
of insurance in the state"* and explicitly carves out only agents/brokers, it does not name, and by
CA Ins. Code §1759's separate (and non-overlapping) definition cannot be stretched to include, a
third-party claims administrator for auto/GL lines (fetched, law.cornell.edu/regulations/california/10-CCR-2695.2).

No incumbent was found making this exact claim. A quick rung-4 pass on the practitioner vocabulary found
Verisk's "Claim Scoring" product, but its own page title is **"Claims Scoring detects fraud quickly and
accurately"** (fetched, verisk.com/products/claim-scoring), a fraud-scoring claim, not a compliance/exam-
finding-risk claim. No G1 (exact claim on a vendor's own page) was found; rung 4 is clean but the sweep was
not exhaustive (ladder stopped at K2 before the full incumbent-vocabulary search ran).

---

## 2. THE SCORED WEAKNESSES

- **Rung 1 (magnitude).** The only quoted dollar figure, the §790.035 $5,000/$10,000-per-act penalty
  ceiling, is a magnitude that exists but was never shown to land on the paying customer (see KILL). Not
  attributable to the TPA. **Weakens criterion 3** (NOT VERIFIED at the customer, so criterion 3 is forced
  to the floor per Part 8's rule).
- **Rung 1.5 (patent).** Google Patents searches on the claim language ("claims handling compliance
  severity score," "prior examination / complaint disposition," "calibrated probability") returned no
  patent reading on this specific claim, closest adjacent hits were generic claims-processing and
  compliance-monitoring patents (US20100145734A1 automated claims pre-scoring; US20200372397A1 ML
  compliance-risk minimization) with no auto/GL-UCSP specificity. **No weakness recorded; clean search,
  not a finding either way.**
- **Rung 2 (duty-holder / primary instrument).** **This is the kill.** See below. **Weakens criterion 7
  heaviest, and criterion 2** (the JTBD as stated, "avoid a DOI finding", is not actually the TPA's own
  legal exposure under the named instrument).
- **Rung 4 (incumbent vocabulary, partial).** Verisk Claim Scoring is fraud-shaped, not compliance-shaped;
  no G1 quote matches the differentiated claim. This is favorable (no K3), but the sweep covered one
  vendor, not the full practitioner-vocabulary list in the dispatch (claims compliance software, DOI exam
  prep vendors, NAIC MCAS tooling, Ventiv/Origami/RegEd-class GRC platforms were not individually tested
  against the exact claim). **Weakens criterion 4** (incomplete evidence, recorded as NOT VERIFIED rather
  than a clean pass).
- **Rung 6 (economics floor).** No countable source was found or searched for the number of small regional
  (<300-employee) auto/GL TPAs, because the ladder stopped before this rung ran. **Weakens criterion 6**
  (NOT VERIFIED, forced low per Part 8).
- **D3 (demand ladder).** Not reached before the kill; see D3 STATE below. **Weakens criterion 3
  independently of the magnitude problem.**

---

## 3. KILL

**K2 fired.** The instrument named by the dispatch as the checker, Cal. Ins. Code §790.035 / 10 CCR
§2695.1 et seq., does not bind the customer (the TPA). It binds the licensed insurer. Evidence, all
fetched and quoted from the primary source:

1. **10 CCR §2695.2(i)** defines *"Insurer"* as *"a person licensed to issue or that issues an insurance
   policy or surety bond in this state, or that otherwise transacts the business of insurance in the
   state"* and states *"The term 'insurer' shall not include insurance agents and brokers, surplus line
   brokers and special lines surplus line brokers."* A TPA is named nowhere in this definition.
   (law.cornell.edu/regulations/california/10-CCR-2695.2, fetched)
2. **Cal. Ins. Code §790.01** (Article 6.5's own scope section) lists the parties the article binds , 
   *"reciprocal and interinsurance exchanges, Lloyds insurers, fraternal benefit societies, fraternal fire
   insurers, grants and annuities societies, insurers holding certificates of exemptions, motor clubs,
   nonprofit hospital associations, life agents, broker-agents, surplus line brokers and special lines
   surplus line brokers as well as all other persons engaged in the business of insurance"*, an
   enumerated list with a broad catch-all, but third-party claims administrators are not named anywhere in
   it. (leginfo.legislature.ca.gov, Article 6.5 full text, fetched)
3. **Cal. Ins. Code §730**, the examination-authority statute that actually produces the market-conduct
   exam findings this candidate scores against, examines **"the business and affairs of the insurer,"**
   requires the Commissioner to **"conduct an examination of every insurer admitted in this state,"** and
   only reaches any other person **"insofar as the examination or investigation is... necessary or
   material to the examination of the company"**, i.e., a TPA's files are pulled in derivatively, as
   evidence about the insurer, not as an examination of the TPA. (leginfo.legislature.ca.gov §730, fetched)
4. **NAIC Model Guideline 1090** (Registration and Regulation of Third-Party Administrators, Oct. 2011),
   the model TPA statute states have adopted in modified form, states plainly: **"An insurer utilizing the
   services of a TPA is responsible for the acts of the TPA and is responsible for providing the TPA's
   books and records relevant to the insurer to the commissioner upon request"** (Section C), and **"In
   the event of a dispute between the payor and the TPA regarding which of them is to fulfill a lawful
   obligation with respect to a policy, certificate or claim subject to the written agreement, the payor
   shall fulfill such obligation"** (Section E). The insurer, not the TPA, is the party the regulator holds
   and the party the model law makes fulfill the obligation. (content.naic.org/sites/default/files/GL1090.pdf,
   fetched and converted to text)
5. **Cal. Ins. Code §1759**, California's own statutory "administrator" (TPA) licensing definition , 
   covers only **"life or health insurance coverage or annuities or coverage described in Section 740"**
   (fetched, leginfo.legislature.ca.gov §1759). Auto and GL claims administration is outside this regime
   entirely; the only CA license potentially reaching an auto/GL claims-handling firm is the independent
   adjuster license (Ins. Code §14020 et seq.), which licenses individuals, not the firm's book of files,
   and is a different instrument than the one the dispatch names as the checker.

Taken together: the checker the candidate names (DOI market-conduct examiner applying §790.035/2695) sits
on the insurer's Certificate of Authority, not the TPA's contract. The TPA's downside from a bad file is
indirect, reputational and contractual (losing the insurer's business, or an indemnification clause in
the servicing agreement), never the quoted DOI penalty itself. That is a real business, but it is not the
one this candidate describes, and "who controls the release of the money, and is it the customer" (K1's
own question) has the same answer: no, the insurer does.

**Not every state matches California on this**, which is why K2 rather than a broader "no market"
conclusion, see MUTATION.

---

## 4. D3 STATE: **UNRUN**

The demand ladder never got a clean run because the kill fired at rung 2, before rung 2.5. A cheap check
was still done: generic "Claims Compliance Analyst" and "Claims Quality Analyst" postings exist (e.g. a
QBE "Claims Compliance Analyst (Workers Compensation)" role, $69,500–$104,500; ZipRecruiter/Glassdoor
aggregate a "Claims Quality Analyst" average salary of $77,032/year), but per the toolchain limit already
on record in this project (major job boards 403 on direct fetch), these are **title-level and NOT VERIFIED
AT PAGE**, and none of the postings found were at a TPA under 300 employees specifically, nor did any
posting's duties match this candidate's specific task (grading closed files against UCSP/FCSPR for exam-
finding risk). Record as **UNRUN**, not EMPTY, a search that could not reach a live, on-point posting is
not a finding.

---

## 5. MUTATION

**Forced.** The forcing evidence is state-specific, and it points at a concrete reformulation rather than
a dead end. California's FCSPR/§790.035 regime makes the insurer the sole duty-holder (see KILL). But
**Texas does not run the same way**: Texas Insurance Code Chapter 4151 ("Third-Party Administrators")
requires a TPA itself to hold a **"Certificate of Authority"** (§4151.051), imposes claims-handling duties
directly on the TPA (§4151.111, "Adjudication of Claims"), and provides for **direct administrative
sanctions and license revocation against the TPA** (§4151.301 "Grounds for Denial, Suspension, or
Revocation of Certificate of Authority"; §4151.308 "General Administrative Sanctions"; §4151.309
"Criminal Penalty") (texas.public.law, section titles fetched; full statutory text of each section NOT
independently fetched, so treat the operative penalty language as NOT VERIFIED and confirm before
building). Search-level, not-fetched evidence also surfaced two real Texas TDI consent orders against TPAs
directly (Free Market Administrators, LLC, $12,500; MaxCare, LLC, $4,000) for failing to maintain TPA
Certificate-of-Authority requirements, NOT VERIFIED at page, but if confirmed this is exactly the D1 the
California version of this candidate cannot produce, because it is a dollar penalty against the TPA by
name.

So the forcing evidence is: **a TPA-direct duty-holder state exists (Texas, and likely others with a
Chapter-4151-style TPA Act) where California does not have one.** The candidate as dispatched should be
reformulated from "auto/GL TPAs nationally, checked by DOI market-conduct examiners applying FCSPR-style
regs" to "auto/GL TPAs in states whose TPA Act makes the TPA itself the licensee and duty-holder", a
segment narrowing, not a new claim. This has not been confirmed against the actual claims-handling
standard inside Chapter 4151 (does it independently impose UCSP-style file standards, or only
license-maintenance and reporting duties?), so the mutation is a lead to chase, not a cleared candidate.

---

## 6. RUBRIC SCORES

| # | Criterion | Score | Why |
|---|---|---|---|
| 1 | Clarity of target customer | 3 | Named type, business relationship and size band (auto/GL TPA, <300 employees, serving small regional insurers) are specific; count of firms in the band NOT VERIFIED (rung 6 never ran) |
| 2 | Clarity of JTBD | 3 | One clear sentence, but it assumes the TPA carries the exam-finding exposure it names, which the kill shows is the insurer's, not necessarily language a TPA QA supervisor would use for their own risk |
| 3 | Significance and magnitude of unmet need | **1** | Magnitude figure found ($5,000–$10,000/act) is NOT VERIFIED as attaching to this customer; D3 UNRUN; no call made. Forced to floor per Part 8 |
| 4 | Differentiation and uniqueness | 3 | One vendor checked (Verisk) does not make this claim; sweep incomplete, so a clean pass is NOT VERIFIED as exhaustive |
| 5 | Performance improvement over existing solutions | **1** | No measured number against manual QA sampling; nothing beyond the candidate's own assertion of "near-zero marginal cost" |
| 6 | Size of market opportunity | **1** | No countable source for the number of small regional auto/GL TPAs; rung 6 never ran |
| 7 | Market / technical / execution risk | **1** | The core mechanism, DOI examiner penalizes the TPA, is contradicted by the primary instrument's own text (K2); the real business model would have to run through the insurer's contractual risk, not the TPA's regulatory risk, which is a different, unverified product |

**Lowest criterion: 1 (criteria 3, 5, 6, and 7 all score 1). Sum: 3+3+1+3+1+1+1 = 13.**

---

## 7. VERIFIED / NOT VERIFIED

**VERIFIED (fetched from the primary source, quoted above):**
- 10 CCR §2695.2(i), "Insurer" definition, https://www.law.cornell.edu/regulations/california/10-CCR-2695.2
- Cal. Ins. Code Article 6.5 full text (§790.01 person list; §790.035 penalty amounts), https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?lawCode=INS&division=1.&part=2.&chapter=1.&article=6.5.
- Cal. Ins. Code §730, examination authority, https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=INS&sectionNum=730.
- Cal. Ins. Code §1759, "administrator" definition (life/health/annuity/§740 only), https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=INS&sectionNum=1759.
- NAIC Model Guideline 1090 (Registration and Regulation of TPAs, Oct. 2011), Sections C and E, https://content.naic.org/sites/default/files/GL1090.pdf
- Verisk "Claim Scoring" product page title ("Claims Scoring detects fraud quickly and accurately"), https://www.verisk.com/products/claim-scoring/
- Texas Insurance Code Chapter 4151 section titles (§4151.051, §4151.111, §4151.301, §4151.308, §4151.309), https://texas.public.law/statutes/tex._ins._code_title_13_subtitle_d_chapter_4151

**NOT VERIFIED (search-engine summary only, or fetch failed, never quoted forward as fact above):**
- California DOI market conduct exam settlement dollar figures (Mercury Insurance ~$1M, 2015), https://www.insurance.ca.gov/0400-news/0100-press-releases/archives/release025-15.cfm (503 on fetch)
- CDI accusation against State Farm, "398 violations... 34 additional", https://www.insurance.ca.gov/0400-news/0100-press-releases/2026/release019-2026.cfm (not independently fetched)
- California Insurance Guarantee Association 2024 exam report TPA claims-handling detail, https://www.insurance.ca.gov/0250-insurers/0300-insurers/0400-reports-examination/upload/California-Insurance-Guarantee-Association-2024-Exam-Report-Final.pdf (503 on fetch)
- Texas TDI consent orders against TPAs directly (Free Market Administrators LLC $12,500; MaxCare LLC $4,000), search-summary only, underlying tdi.texas.gov PDFs not fetched
- Job postings: QBE "Claims Compliance Analyst (Workers Compensation)" $69,500–$104,500; ZipRecruiter/Glassdoor "Claims Quality Analyst" $77,032 average, title-level only, job-board pages not fetchable (known toolchain 403 limit)
- Independent-adjuster licensing as the alternative CA channel for auto/GL TPA discipline (Ins. Code §14020 et seq.), search-summary only, statute text not independently fetched
- Google Patents search on the differentiated claim, no reading patent found; searched but not exhaustive (rung 1.5, a clean search result, not a citation)

Rungs 2.5 (demand ladder beyond D3's title check), 3 (free substitute sweep, GIVES/PUBLISHES/CAPTURES/
ABSORBS/RATCHET/FEE-SHIFT/COMPELLED), most of rung 4 (the full incumbent-vocabulary sweep), rung 5 (buyer
standing), and rung 6 (economics floor) were **not run**, because the ladder stops at the first
instrument-verified kill (K2), per Part 3.
