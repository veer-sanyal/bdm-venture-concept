# CONCEPT: Supplier Quality Chargeback Defense

**Written 2026-09-12 as the plain-language explainer of the chosen idea.** This file is a derived read.
Evidence, quotes and live status stay in `STATE.md` (sections "DECISION, VEER, 2026-09-11" and
"5. Supplier quality chargeback"), the call script in `CALL-GUIDE.md` Idea B, the contract reading in
`FORD-BUYER-DATA-SCOPE.md`. If this file and those disagree, they win and this one gets fixed.

Chosen by Veer 2026-09-11 after 16 rounds, 98 candidates, 42 screens. Team: Veer + Cole.

---

## 1. The problem, in one story

A 60-person shop in Kokomo stamps brackets for a Tier-1 seat maker. A bill shows up: *your parts were
bad, we stopped our line, hired a sort crew, and air-freighted replacements. You owe $6,200.* That is a
**supplier quality chargeback** (called an SCB, SMRR or QPN depending on the customer).

It is not a request. **The customer deducts it from what they already owe the supplier unless the
supplier disputes it, with documents, inside a window.** Adient: 30 days (working or calendar, by manual
revision). Piston Automotive and FICOSA: 10 days. Silence means the debit stands.

The bill bundles two kinds of money:
- **A fixed admin fee**, published by the issuer: Adient $250 to $275, RECARO not to exceed $250, Piston
  $200, plus $200 per shift for on-site sorts.
- **Pass-through charges on top**: third-party sort labour, line downtime, premium freight, rework. This
  is the real money, and its size is **not verified anywhere yet**. The calls exist to get it.

**The mistake that costs money:** the supplier's quality engineer, who also runs containment and has a
day job, either misses the window or answers with a narrative ("we take quality seriously") instead of
the three boring documents that actually reverse a line: shift records showing the claimed sort hours
are impossible, the carrier's dispatch time showing the freight was not really expedited, the inspection
log for that lot.

**The job to be done, in the customer's words (draft, to be replaced by a real quote):** *"Don't let a
debit I could have beaten come out of my receivables."*

## 2. Who the customer is

| | |
|---|---|
| **User and buyer** | Quality manager or plant manager (the Customer Quality Engineer does the work; job postings name "managing immediate containment and chargebacks", $80k to $105k) |
| **Company** | Tier-2 or Tier-3 supplier, 20 to 300 people, selling into automotive, appliance or heavy equipment |
| **Where** | Indiana has hundreds: Kokomo and Fort Wayne corridors, the Subaru (Lafayette) and Caterpillar supply bases |
| **Best first customers** | **Ford-supplying shops.** Ford's terms let a supplier share documents with consultants under a confidentiality flow-down (§16.03). GM's terms do not, and name subcontractors inside the bar (§30). Ask which OEM on every call |
| **How many exist** | **1,897 US firms / 2,173 plants at 20-499 employees** (auto parts, appliances, farm and construction machinery; Census SUSB 2022), 170 auto-parts plants in Indiana. Dollars per customer unpublished; mid case about $5M-$7M of US revenue. Full model: `MARKET-SIZE.md` |

## 3. The product

**What it decides, which is the whole thing:** given one chargeback's line items plus the supplier's own
records for that lot, **which lines to fight, on what ground, with which document, and which to concede.**
It is a triage and evidence-selection decision. Drafting the 8D is not the product; GM and Stellantis
portals already hand suppliers that for free.

The output looks like: *"This $6,200 debit has a sort-labour line your shift records disprove, a downtime
line you cannot defend, and a premium-freight line you win only if you produce the carrier's dispatch
time. Fight two, concede one, attach these, file by the 19th."*

**How it works, in order:**
1. **Intake.** The chargeback arrives (debit memo, QPN, the customer's supporting invoices, often a
   pre-filled 8D). The supplier adds its own production, inspection and shipping records for the lot.
2. **Read.** The model matches the sort firm's report (part numbers, shift times, quantities) against
   the supplier's production records, and reads **this** customer's supplier quality manual for what it
   actually obliges and what the dispute window is.
3. **Triage.** Line by line: fight or concede, the ground, the attachment, the deadline.
4. **File.** The rebuttal goes in through the customer's portal inside the window.
5. **Learn.** The customer returns a written disposition. Piston states the three outcomes verbatim:
   *amend, rescind, or let stand*. That label, tied to the evidence that was attached, trains the next
   triage.

**Why only now:** the inputs are scanned PDFs, emailed templates, photos and ERP exports in a different
format per customer, with no schema. A 2015 rules engine needs a schema. Reading and reasoning across
inconsistent documents is the class of work that became tractable recently.

**How it is built, in stages, and this order is deliberate:**
1. **By hand first.** Veer works a real case start to finish for a supplier who pays and keeps whatever
   comes back. This proves the judgment is learnable before any software exists.
2. **Back-test.** Three suppliers' redacted closed cases: would the triage have picked the lines that
   actually got reversed?
3. **Software** around the parts of the manual work that repeat.

**Price: not decided.** Outcome pricing (a cut of what is recovered) is the obvious pitch and the one
the evidence argues against: High Alpha's own data says only 5% of AI companies price purely on outcome,
and Foundation Capital says outcome pricing breaks when results vary by customer. The paid pilot sets the
first real number.

### 3a. Inputs: what comes from whom

**Labels:** RECORD = named in `STATE.md` with a source. TYPICAL = standard at an IATF 16949 automotive
supplier from general industry knowledge, not verified at any specific shop. The calls confirm which of
these a 20-to-300-person shop actually has and can export.

**From the issuing customer (Adient, Piston, a Ford or GM Tier-1).** We never have our own access. Every
one of these reaches us through the supplier, who logs into the customer's portal and hands them over.

| Document | How the supplier gets it | Status |
|---|---|---|
| The chargeback notice itself (SCB / QPN / debit memo), with line items and amounts | Customer portal: IRIS or SAP for Adient, SQP for Stellantis, SupplyPower for GM | RECORD |
| A pre-filled 8D (the defect report the supplier must answer) | Adient: *"automatically provided as part of IRIS or SAP electronic notification(s)"* | RECORD |
| **The evidence behind the charge**: third-party sort invoices, downtime records, freight invoices | Adient: chargebacks *"include supporting documentation such as third-party invoices, downtime records, freight invoices, etc."* FICOSA *"must present to the supplier all of the supporting data"* | RECORD |
| The supplier quality manual: fees, dispute window, dispute procedure | **Public**, free on the customer's website | RECORD |
| The purchase terms (confidentiality, data use) | Ford PPGTC public; GM behind login (2014 copy public) | RECORD |

**What we do NOT get:** the customer's own receiving-inspection records, the sort crew's raw timesheets
behind the invoice, the reasoning of the Purchasing rep who settles escalated disputes, and anything about
how other suppliers' disputes went with the same customer (barred, section 5). **And no portal access of
our own:** GM's SupplyPower terms bar using portal information for *"service bureau services, outsourcing
or consulting services,"* so at least for GM the supplier files, not us.

**From the supplier (our customer), about the batch in question:**

| Document | What it can prove | Status |
|---|---|---|
| Production and shift records for the batch | Sort hours or quantities claimed are impossible | RECORD |
| Inspection log for that lot | The parts were checked and passed when they left | RECORD |
| Shipping records and the carrier's dispatch time | Rush freight was not triggered by this defect, or not when claimed | RECORD |
| ERP export (orders, shipments, quantities) | Quantities charged exceed quantities shipped | RECORD |
| Photos of the rejected part | Whether the defect is what the notice says it is | RECORD |
| Lot traceability, packing slips / advance ship notices with lot numbers | Which lots were actually suspect, so a sort beyond them is out of scope | TYPICAL |
| Control plan, PFMEA, PPAP approval, drawing | The feature was in spec, or the customer approved the process | TYPICAL |
| Previous 8Ds and past dispositions with this customer | What this customer has reversed before | TYPICAL |

### 3b. Outputs, per chargeback

1. **A line-by-line decision table:** each charge, its amount, FIGHT or CONCEDE, the ground, the exhibit,
   and how sure.
2. **A missing-evidence list:** "to fight line 3 you need the carrier dispatch timestamp; it is on the
   carrier's site; pull it by Tuesday." This is most of the value on a busy week.
3. **A dispute packet** in that customer's format: short rebuttal per contested line, exhibits labeled
   and referenced. No narrative.
4. **The clock:** the deadline under the manual revision in force, counted in the right kind of days.
5. **After the reply:** the customer's written disposition logged against each line and the evidence
   attached. That log is the per-supplier outcome ledger in section 5.

**What typically defeats each line type.** These are working hypotheses, not verified practice; the
domain advisor confirms or kills each one.

| Line | Fight it when | Usually concede |
|---|---|---|
| Admin fee ($200-$275) | Only if the whole notice is rescinded, since the fee rides on it | Yes |
| Sort labour | Hours invoiced do not fit parts sorted; sort ran past the suspect lots per traceability | |
| Downtime | Customer's own records do not tie the stoppage to this part number | Often, if the record ties it |
| Premium freight | Dispatch happened before the supplier was notified, or not for this part | |
| Scrap / rework | Quantity exceeds what was shipped in suspect lots; feature was in spec | |
| The defect itself | Transit or handling damage, or a drawing change the supplier was not given | |

### 3c. A worked example (numbers invented, for illustration only)

A $6,200 chargeback: admin $250, sort $2,400, downtime $2,100, premium freight $1,450.

| Line | Amount | Decision | Why | Attach |
|---|---|---|---|---|
| Sort labour | $2,400 | **FIGHT** | Crew invoiced 3,000 parts; traceability shows only lot 2231 (1,200 parts) was in the suspect date range | Traceability export, advance ship notice for lot 2231 |
| Premium freight | $1,450 | **FIGHT, if the timestamp exists** | Carrier dispatched 6:10am; the notice reached the supplier at 9:40am | Carrier dispatch record, notice timestamp |
| Downtime | $2,100 | CONCEDE | Customer's downtime record ties 2.5 hours to this part number and nothing contradicts it | |
| Admin fee | $250 | CONCEDE | Fixed by the manual; the notice itself is not being rescinded | |

**Contest $3,850, concede $2,350, file by the date on the clock.**

### 3d. Why not just paste everything into ChatGPT?

**Be honest first, because a judge will try it:** given the right documents already gathered, ChatGPT
reads PDFs, summarizes a quality manual and writes a polite rebuttal well. On a single easy case it gets a
long way. If the product is only "better reading," it loses.

**Where it breaks:**
1. **It only reasons over what you paste in, and gathering is the hard part.** The winning exhibit is the
   traceability export or the carrier's dispatch time, sitting in the ERP, the carrier's website and the
   shipping clerk's inbox. An engineer who already knew to pull those would not need help. The product
   tells you what to pull for each line type at each customer. **It does not fetch it** until integrations
   exist (3e step 4), so in the upload version the engineer still does the physical gathering. Against
   ChatGPT the edge is knowing what to ask for, the per-customer rules, the math checks and the outcome
   log; see 3g.
2. **It does not know what wins.** Asked which lines to fight, a general model writes a plausible
   argument, which is the exact failure mode: narrative instead of proof. It has never seen what this
   customer's plant reversed. The product gets a written disposition per line after every case.
   **Honest limit:** that learning is per supplier and starts empty, so on day one the edge is expert
   judgment written into the triage (the advisor and the manual work), not the model.
3. **The arithmetic is where general models slip.** Reconciling sort hours, part counts, shift times and
   lot ranges across a scanned invoice and an ERP export is where a chat model makes confident mistakes.
   The product does those as fixed checks and uses the model only to read.
4. **It does not run the case.** Ten calendar days at Piston, 30 days at Adient depending on revision,
   different formats, follow-up, recording the result. A chat window is not a case system.
5. **Confidentiality.** Ford §16.03 allows sharing with consultants only under a written confidentiality
   agreement; GM §30 bars any third party without consent. An engineer pasting a customer's notice into a
   personal chatbot account has signed nothing. **This does not fix GM for us either**, but for Ford a
   vendor that signs the flow-down is clean and a personal account is not.

**The test that settles it, and it is also the Dec 11 number:** in the back-test on redacted closed cases,
run plain ChatGPT as the baseline. Same cases, one straightforward prompt, versus our triage, both scored
against the disposition that actually came back. The gap is "performance improvement over existing
solutions," scored word for word by the rubric. **If ChatGPT matches us, criterion 5 is a 1 and we need to
know that in October, not in December.**

### 3e. Where the documents live, and getting the numbers right

**Yes, every supplier's software is different.** The record names Plex as the dominant Tier-2 automotive
ERP, and every customer portal is different too; none offers third-party API access (rung 5). Small shops
also run other ERPs, spreadsheets, and paper binders (TYPICAL, confirm on the calls).

**So the product does not start by connecting to anything.** Build in this order, and only move to the
next step when paying customers force it:
1. **Pilot: the supplier uploads or emails files.** A PDF, a CSV export, a phone photo of a binder page.
   Nothing to integrate; it works on any system, including paper.
2. **Per-supplier evidence map, set up once at onboarding.** The checklist of WHAT to pull is the same
   everywhere (for a sort charge: batch tracking, advance ship notice, inspection log). WHERE it lives is
   one short table per supplier: "ship notices are Plex report X, carrier is the freight portal, inspection
   log is the blue binder." The missing-evidence list then says exactly where to go.
3. **Saved export templates** for the two or three ERPs most customers actually run.
4. **Direct integrations last**, for one ERP, once enough customers share it. Customer portals stay manual
   at least for GM, whose SupplyPower terms bar service-bureau use.

**Storage is walled off per supplier.** Each supplier gets its own case folders: notice, exhibits,
decision table, the customer's reply. **No record and no model training crosses suppliers**, because the
record's reading of Ford §20.01 is that a model trained on Buyer Data is Buyer Data in aggregated form.

**Getting the math right. The model never does arithmetic.**
1. **The model only extracts.** Every number (part count, batch, hours, rate, timestamp) goes into a
   table with its source: document, page, line or cell. A value it cannot locate is left blank and
   flagged, never guessed.
2. **Code does every calculation**, the same way every time.
3. **Documents check themselves.** If the extracted invoice lines do not add up to the invoice's printed
   total, the extraction is wrong and the case stops for a human.
4. **Units and clocks are converted explicitly:** shifts vs hours, parts vs boxes (pack quantity),
   plant time vs carrier time zone, calendar vs working days under the manual revision in force.
5. **Fight only on a material gap.** Billed 3,000 vs shipped 1,200 is a fight. Billed 3,000 vs 2,950 is
   a concede or a question. A disputed charge with wrong math costs credibility with the plant that
   decides the next dispute, so uncertainty resolves to concede.
6. **A person signs every packet.** In the pilot, Veer and the advisor review everything, and the
   supplier's quality engineer approves and files. Each number in the packet links to its source so the
   check takes minutes.
7. **Closed cases become the test set.** The redacted closed cases, with correct numbers and the real
   disposition, are rerun after every change. A change that breaks one old case does not ship.

**None of steps 2-4 of the build order is needed before Dec 11.** The pilot and the back-test run on
uploaded files, a spreadsheet, and a human check.

### 3f. Software or agency? (added 2026-09-12)

**Uploading files does not make it an agency.** Expense software and tax software run on uploads too. What
decides it is **who the human in the loop is on each case.** If our people read every case, it is an
agency. If the supplier's own quality engineer uploads, reviews the recommendation and files, it is
software.

**The software version, which is the product being pitched:**
- **Customer does:** uploads the notice and records, answers the missing-evidence list, approves, files.
- **Software does:** pulls every number with its source, runs the checks, applies the rules for that
  customer's manual (window, fees, format), recommends fight or concede per charge, lists missing
  evidence, builds the packet, tracks the deadline, logs the reply.
- **We do:** nothing per case. The onboarding map is a setup screen the customer fills in.
- **Priced** per plant per month or per case, decided by frequency (below).

**Why the hand-worked phase still comes first:** the rules inside the software (which charge types lose
to which evidence at which customer) do not exist yet in any written form. Working cases by hand with
the advisor is how they get written. That is validation, not the business model. The rules come from
public manuals and expert knowledge, so they can be shared across suppliers; the outcome log cannot.

**Two constraints from the record that shape this:**
- **Workflow alone does not sell.** Rung 3: the customer's portal already gives away the dispute button and
  the 8D. **The software has to contain the judgment** (the recommendation), or it is a free feature. A
  bare deadline tracker was already killed on this ground.
- **Frequency decides the pricing, and nobody knows it yet.** A supplier with chargebacks every month pays
  a subscription. One with three a year will not pay monthly for a tool; it pays per case, which starts
  to look like a service again. The record's gate agent inferred that a 20-to-300-person stamper
  generates low claim volume (inference from iNymbus' pricing, not a measured chargeback count). **Call
  question 1, "how many did you get last year", decides software vs service.**

**An untested alternative channel, if per-supplier volume is too low:** sell the software to the firms
already on the supplier's side, such as containment firms (Vayan, Quality Liaison) or automotive quality
consultants, who work many suppliers' cases. That is the room's winning shape, software sold into a
services industry, and Ford §16.03 permits sharing with consultants under a confidentiality agreement.
Not screened; a channel question, not a new candidate.

**The room:** last edition's 1st and 3rd place sold software into service industries; none of the 13
confirmed winners delivers the service itself. Pitch the software. The December evidence can be
hand-worked cases, because the rubric has no traction criterion and a proof of value is what High Alpha
says replaces the demo.

### 3g. Gathering is two jobs, and upload software solves only one (added 2026-09-12)

| Job | Upload software solves it? |
|---|---|
| **Knowing what to pull** (which record beats which charge) | **Yes**, the missing-evidence list |
| **Physically fetching it** (run the report, log into the carrier site, find the binder) | **No**, the engineer still does it |

**Call question 4b decides which one hurts.** "Twenty minutes, it is all in Plex" means upload software is
enough. "Half a day, the binder is at the other plant" means one of: an early Plex integration (if the
calls confirm most customers run it), cheap automation (a forwarding address for notices and carrier
emails; carrier tracking for pickup times, NOT VERIFIED), or accepting a service. Paper binders are never
automated. **Question 1 (frequency) and 4b (gathering time) together decide software vs service.**

### 3h. A full tracking system, or stay niche? (added 2026-09-12)

**Build the tracker into the product; do not build a general system.**
- **The tracker comes free.** Every case already stores the notice, deadline, decision, evidence and the
  customer's reply. A list view of that (open chargebacks, days left, dollars contested, won and lost by
  customer) is the "keeps track of everything" screen. It is also the per-supplier outcome ledger from
  section 5, so it is part of the moat, not a side project.
- **A general supplier-quality system is a different company.** That category is occupied by Plex QMS,
  Ideagen and High QA, and the record already found that moving upstream "walks into every QMS vendor."
  It also gives up the one clean position this idea has: nobody sells defense on the supplier's side. A
  student with no domain credibility does not beat Plex on breadth.

**Niche is fine, and the room says so.** High Alpha's own 2026 prediction is that early-stage SaaS will
leapfrog with outcome-based pricing *"for Niche Problems,"* and a16z's screen asks whether you can *"start
with one assignment and grow into the whole job."* The niche is the wedge.

**What niche does hurt is criterion 6, market size, currently a 2.** Two fixes, and neither is building
more product:
1. **Count the market.** Rung 6 is open: US Tier-2/Tier-3 supplier count times chargebacks per year times
   average all-in amount. The calls supply the last two numbers.
2. **Name the expansion, with evidence, not assertion.** The AHERA candidate died partly because its
   expansion story was asserted and turned out false. Verified adjacent: Piston also issues a **Delivery
   Problem Notice ($200 minimum)**, the same debit-and-dispute mechanic through the same channel, fought
   with shipping records the product already asks for. Unverified and worth one question on the calls:
   whether warranty chargebacks and controlled-shipping costs run the same way. Beyond automotive, the
   same supplier quality manuals exist in appliance and heavy equipment, already inside the target
   customer definition.

## 4. Why nobody does this today

**Every vendor is on the other side of the transaction.** That is the strongest finding in the record.
- **Plex, Supplios, SupplyOn** sell chargeback tools to the company **issuing** the charge. Supplios
  literally advertises tracking bad quality "to issue supplier charge-backs."
- **Deduction-management platforms (HighRadius, iNymbus)** handle retail shortage and pricing
  deductions for Walmart and Amazon vendors. None handles sort labour, downtime or an 8D.
- **Recovery consultancies (Detering, Claimlane, WarrantyHub)** also sell to the issuer.
- **Containment firms** sell getting out of controlled shipping, not beating the debit.
- **The customer's own portal** gives the supplier the notice, the deadline, the dispute button and the
  evidence behind the charge. **What it never tells them is which argument wins, and structurally it
  never will, because the portal is the adversary's instrument.**
- No buyer's guide exists for supplier-side quality chargeback defense.

## 5. The moat, stated honestly

**The moat everyone would pitch is a pooled database: "we see what Adient reverses across 200
suppliers." That moat is not available, and the pitch must say so before a judge does.**
- Ford PPGTC §20.01 bars suppliers from using Buyer Data *"whether in aggregated, anonymized, or
  de-identified format or not."* Scrubbing does not help; the customer's plant is the axis of the output.
- GM §30 reaches anything *"based on"* information GM provided, and bars sharing with subcontractors.
- **Antitrust:** a dataset telling competing suppliers which arguments win against their shared customer
  is an information exchange about contract terms. MEMA's own guidelines warn against exactly this.
  Counsel before the first pooled record, not after.
- The one open door: Ford separately defines **Supplied Data** (the supplier's own production, quality
  and logistics records) and puts no use restriction on it (§20.03). Whether that carves the supplier's
  own records out of §20.01 is **genuinely ambiguous and a lawyer's question**, not settled either way.

**So what the moat actually is, in order of strength:**
1. **Position.** Every capable incumbent sells to the issuer. Plex or SupplyOn cannot start helping
   suppliers beat the charges their paying customers issue. That is a structural reason the category is
   empty, and it holds as long as the product stays on the supplier's side.
2. **The outcome ledger, per supplier.** Every filed dispute returns a written disposition. That record
   of *this evidence reversed that line at this customer* only exists because the product ran; it is
   data the product causes to exist, not data it imports. It lives inside one supplier's own history,
   which makes it legally defensible and a real switching cost, and a good tool rather than a
   network-effect asset.
3. **Judgment.** Knowing which line of a quality chargeback is defensible needs someone who has read a
   control plan and argued a PPAP. It is hard to acquire, which is also Veer's biggest gap (section 7).

**What is commodity, said out loud:** the document-matching and portal-automation engine. iNymbus
already does credentialed portal automation for retailers. That half is a head start on a timer.

**The honest one-liner for the room:** at idea stage, application companies win with lagging moats. The
moat is being the only one on the supplier's side of the table, and a per-supplier record of what wins
that compounds with every dispute.

## 6. What the competition wants

**Burton D. Morgan Venture Concept Competition, 38th.** Lead: Prof. Kostas Grigoriou (ex-High Alpha).
$100k pool, two tracks, about 25 awards. Top 10 get Venture X2 admission. Eligibility caps (under $10k
funding, under $5k revenue, no Purdue IP) make every team pre-revenue, so traction is not a lever. Dates and form links are on the competition page.

| When | Deliverable | Scored? |
|---|---|---|
| **Sun Sep 27, 11:59pm** | **Preliminary concept** via the Airtable form. A name and a paragraph. | **No.** "An expression of commitment." Must not eat a call slot |
| Thursdays Sep 24, Oct 8, Oct 22, Nov 5, Nov 19, Dec 3 | Six workshops | Attendance |
| At milestones | **Four short assignments** via Brightspace, plus 1 to 2 virtual office hours | Unknown |
| **Fri Dec 11, 10am to 2pm, HIVE** | **Final, in person, mandatory.** Judged by a VC panel | **Yes** |

**⚠ NOT VERIFIED: the format of the Dec 11 final** (pitch length, deck, booth, Q&A) and the content of
the four assignments. Nothing in the repo records either, and there are no notes from the Sep 10 info
session. Ask at Workshop 1 on Sep 24 or email Grigoriou.

**The published rubric, verbatim categories:** Priority JTBD (clarity of target customer, clarity of
JTBD, significance and magnitude of unmet need) · Clarity of value proposition (differentiation,
performance improvement over existing solutions) · Size of market opportunity · Market, technical and
execution risk. **Three of four categories are about the customer and the need.** No team, traction or
tech-novelty criterion.

**Last panel:** two High Alpha-lineage judges, Elevate Ventures, and **two industrial operators** (HG
Ventures, Roll Tack / New Eagle). An automotive supplier problem lands with the industrial half, which
pure SaaS ideas do not.

**What Dec 11 has to show, derived from the rubric and the record:**
1. **Operators' own words.** Quotes from three supplier calls: when the last chargeback hit, what it came
   to all-in, what they did. This carries the three JTBD lines.
2. **A proof of value, not a demo.** High Alpha's 2026 prediction is that proof of value becomes the new
   demo. For this idea that is the back-test on redacted closed cases, and ideally one manually worked
   case with a disposition returned.
3. **The differentiation answer** (section 4) and the **named weakness** (section 5: no pooled data,
   per-supplier ledger instead). Named weaknesses beat undiscovered ones in front of this panel.
4. **A market size** from a countable source. Count done 2026-09-12 (`MARKET-SIZE.md`); the dollars
   per customer come from the calls.
5. **The domain advisor on the slide.** Someone who has argued a chargeback, answering the "you are a
   student with no domain experience" objection with a person, not a claim.

## 7. Where it stands, and what can still kill it

**Rubric score on desk evidence only (2026-09-07):** 18 of 35, lowest criterion 2. Customer 3, JTBD 4,
unmet need 2, differentiation 3, performance 2, market size 2, risk 2. Every 2 is a missing number or a
missing voice, which is what the calls fix.

**The bar to clear before December (from `STATE.md`):** 3 supplier calls, 3 redacted closed cases in
hand, 1 domain advisor who has argued a chargeback, 1 supplier who says yes to a paid manual pilot.

**The kill risks, ranked:**
1. **Does a partial reversal come back line by line or as one negotiated number?** A lump means the
   system can never learn which document won. **This kills the asset. It is question one on every call.**
2. **Who decides the dispute?** Adient escalates disputes to the Purchasing rep who awards the next
   program. If disputes are settled on relationship, evidence is second-order and the premise is wrong.
   Corollary: does disputing more make a customer's charges go up?
3. **Is the money there?** If the answer is "a couple a year at $250, we just pay them," it is dead.
   Frequency and all-in size are unpublished.
4. **Can the supplier legally hand over the documents?** Clean for Ford suppliers under flow-down, blocked
   for GM suppliers on the face of the 2014 terms (current GM text not verified).
5. **Domain credibility.** Veer has not read a control plan or sat through a sort. Closed by recruiting
   an advisor, not by reading.

**Next physical actions:** reach Cindy Farrer at Purdue MEP (Quality and Supply Chain), then book the three calls through MEP, Kokomo/Fort Wayne, Subaru/Caterpillar.
