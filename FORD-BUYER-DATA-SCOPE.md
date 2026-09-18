# Ford "Buyer Data" - scope verification

**Run 2026-09-11. Narrow question only: does Ford PPGTC §20.01 reach a supplier's OWN internally
generated records? No business judgment offered.**

---

## 1. The instrument, and what version is current

**VERIFIED. Document: "Production Purchasing Global Terms and Conditions", PPGTC Jul. 1, 2021.**
Cover page and footer of every page read: `PPGTC Jul. 1, 2021`, and on the release page:

> DOCUMENT RELEASE AND EFFECTIVE DATE: July 1, 2021

**Ford's own live page, fetched 2026-09-11**
(`https://corporate.ford.com/operations/governance-and-policies/production-purchasing-global-terms-and-conditions/`)
links an English interactive microsite plus four translated PDFs on Ford's own domain. **The English
PDF is not exposed at a guessable path (`ppgtc_english.pdf` → HTTP 404) and the microsite is a
JavaScript app that returns only its title to a fetcher, so the English text had to come from a
hosted copy.**

**Two independent copies were read and cross-checked, so the text below is not one firm's transcription:**

1. **English, full document, 2,468 lines of extracted text** - hosted by Butzel Long:
   `https://www.butzel.com/assets/htmldocuments/uploads/Automotive/2021.04.18%20New%20Ford%20terms%20effective%207_1_21.PDF`
2. **Spanish, full document, from FORD'S OWN DOMAIN**  - 
   `https://corporate.ford.com/acslibs/content/dam/na/ford/en_us/documents/corporate/governance-and-policies/production-purchasing-global-terms-and-conditions/ppgtc_spanish.pdf`
   Cover: `PPGTC 1 De Julio De 2021`; release line: `FECHA DE LIBERACION DE DOCUMENTO Y VIGENCIA
   EFFECTIVA: 1 DE JULIO DE 2021`. **Its §20.01 and its definition of "Datos del Comprador" are
   sentence-for-sentence the same instrument as the English copy** (both reproduced below), which
   authenticates the English copy.

**So: July 1, 2021 is still what Ford publishes as of 2026-09-11.** The record's "Ford July 2021
PPGTC as current contract text" is CORRECT on the date. **Caveat, stated not resolved:** the PPGTC
itself provides that revisions take effect the following July 1, and Supplemental Terms, Supplier
Guides and the referenced PII / Information Security Supplements live behind the Ford Supplier Portal
login, which was NOT reachable. A supplement could qualify §20 and would not show up here.

---

## 2. The definition of "Buyer Data", VERBATIM AND IN FULL

From DEFINITION OF TERMS, PPGTC Jul. 1, 2021:

> **Buyer Data** means all data and information which is collected, transmitted, stored, processed,
> derived from or used by, or on behalf of, or relating to, Buyer, including, but not limited to, (a)
> the Goods and Tech Products, and (b) Buyer operations, production, vehicle-related data.

Ford's Spanish text, same definition:

> **Datos del Comprador** significa todos los datos e información que se recopilan, transmiten,
> almacenan, procesan, derivan o utilizan por, o en nombre de, o relacionados con el Comprador,
> incluidos de manera enunciativa más no limitativa, entre otros, (a) los Bienes y Productos
> Tecnológicos y (b) datos relacionados a las operaciones del comprador, y producción de vehículos.

Two other definitions are load-bearing and must be read with it:

> **Buyer** Ford Motor Company or the Ford Motor Company Related Company identified on the face of
> the Purchase Order.

> **Supplied Data** means any data or metadata, including but not limited to digital data, that is
> related to Supplier's production, delivery, logistics, quality, volume or similar business
> information regarding the Goods and Tech Products.

> **Tech Products** means Software, Software as a Service, Buyer Data and Supplied Data.

### Which axis does the definition turn on?

**It turns on (b), RELATIONSHIP - not (a) who supplied the data, and not (c) marking.** The operative
words are *"derived from or used by, or on behalf of, or relating to, Buyer"* and *"including...
(a) the Goods and Tech Products."* Nothing in the definition mentions who furnished the data, and
nothing mentions a legend, marking, or secrecy. **On that narrow point the project's record - "Ford
defines Buyer Data by RELATIONSHIP to Ford, not by marking or secrecy" - is CORRECT, and the outside
analysis's characterisation ("Buyer Data, meaning data furnished BY Ford") is NOT what the definition
says.** The definition contains no "furnished by Buyer" limitation at all.

**Corroborating that marking is irrelevant, §16.01:**

> Information that does not meet these requirements is not Confidential Information, regardless of any
> legend or marking to the contrary.

---

## 3. Article 20, VERBATIM AND IN FULL (all five subsections)

> **SECTION 20. DATA**
>
> **20.01 Buyer Data** Buyer retains all right, title, and interest in and to all Buyer Data. Supplier
> has no rights in or to any Buyer Data not expressly indicated under the PPGTCs. During the term of
> the applicable Purchase Order, Buyer hereby grants to Supplier a limited, non-exclusive,
> non-transferable, revocable license to strictly collect, transmit, store, or otherwise process Buyer
> Data for the sole purpose of providing the Goods and Tech Products to Buyer. Supplier shall not use
> Buyer Data, whether in aggregated, anonymized, or de-identified format or not, for any business or
> other commercial purpose of Supplier or any other person. Without limiting the foregoing, Supplier
> shall not use Buyer Data which is aggregated, anonymized, or de-identified and attempt to use it in
> manner which, either alone or in combination with other information, would make such Buyer Data
> identifiable.
>
> **20.02 Data Incident** Without limiting the other provision of the Global Terms, Supplier shall be
> responsible for all reasonable and necessary data incident notifications, forensics, credit
> protection services, and other data mitigation services resulting from Supplier's failure to protect
> Buyer Data under the PPGTCs.
>
> **20.03 Supplied Data** Shall be provided to Buyer at no additional charge at the request of Buyer.
> Supplied Data shall not include any Buyer Data provided by Buyer to Supplier. Supplier shall deliver
> all requested Supplied Data to Buyer with right for Buyer to use Supplied Data in analytics, in
> operations, related to providing products and services, in manufacturing, with third parties, or
> merged with other data assets. The formatting and specifications of all Supplied Data provided to
> Buyer by Supplier shall be as specified in the Supplier Production Data Supplier Guide or as
> otherwise agreed upon by the Parties in the SOW.
>
> **20.04 Privacy** See PII Supplement available on the Ford Supplier Portal (FSP) for details.
>
> **20.05 Cyber Security** See Information Security Supplement available on the Ford Supplier Portal
> (FSP) for details.

**The §20.01 sentence the project quoted is accurate, word for word.** Verified against the Spanish:
*"El Proveedor no utilizará los Datos del Comprador, ya sea en formato agregado, anónimo o que no
permita datos de identificación, para ningún negocio u otro propósito comercial del Proveedor ni de
cualquier otra persona."*

**The neighbouring subsection the project's record never registered is §20.03, and it is the whole
fight.** See item 4.

---

## 4. DOES §20.01 REACH THE SUPPLIER'S OWN INTERNALLY GENERATED RECORDS?

**VERDICT: GENUINELY AMBIGUOUS ON THE FOUR CORNERS. Not resolved, and I am not guessing.** Both
readings are textually supported, each by words in Section 20 itself. The project's record stated the
broad reading as settled; it is not settled. The outside analysis stated the narrow reading as
settled; that is not settled either, and its stated ground ("meaning data furnished BY Ford") is the
one ground the definition affirmatively does NOT use.

### Reading A - it DOES reach the supplier's own records. Words that decide it:

- *"or relating to, Buyer"* - an inspection result for a lot shipped to Ford is data **relating to**
  Ford. Nothing narrows "relating to."
- *"including, but not limited to, (a) **the Goods and Tech Products**"* - the Goods are the parts sold
  to Ford. Data about those parts is inside the illustrative list by its own terms.
- *"derived from"* - reaches records the supplier generated out of the relationship rather than
  received.
- **The license verb is the strongest single word for Reading A: Ford grants the supplier a license
  "to strictly COLLECT, transmit, store, or otherwise process Buyer Data."** A license to *collect*
  presupposes Buyer Data the supplier itself brings into existence. Data Ford already handed over does
  not need a license to be collected.
- **§20.03's own carve-out sentence cuts this way too:** *"Supplied Data shall not include any Buyer
  Data **provided by Buyer to Supplier**."* The qualifier "provided by Buyer to Supplier" is only
  necessary if some Buyer Data is NOT provided by Buyer. Read against the outside analysis, this is
  the sentence that most directly contradicts it.

### Reading B - it does NOT reach the supplier's own operational records. Words that decide it:

- **The PPGTC creates a SEPARATE defined category for exactly the records at issue.** *"Supplied Data
  means any data or metadata... that is related to **Supplier's production, delivery, logistics,
  quality, volume or similar business information** regarding the Goods and Tech Products."* That is
  the supplier's inspection results, production records, lot traceability and defect rates, named.
- **And §20.03 imposes no use restriction on the Supplier for that category at all.** Its only
  obligations run the other way: the supplier must hand Supplied Data over at Ford's request, and Ford
  gets sweeping rights to it (*"in analytics, in operations... with third parties, or merged with other
  data assets"*). **If the supplier's own quality records were already Buyer Data under §20.01, both
  the separate definition and §20.03's delivery obligation would be surplus, and §20.01's prohibition
  would already govern them.** A drafter who meant §20.01 to swallow the supplier's production data
  would not have needed §20.03.
- Grammar: in *"collected, transmitted, stored, processed, derived from or used **by, or on behalf
  of**, or relating to, Buyer,"* the prepositions attach to those verbs, so the acts contemplated are
  Ford's or Ford's agent's. On that parse, a supplier unilaterally recording its own scrap rate has not
  had data "collected by or on behalf of" Ford.

### What is NOT ambiguous

- **The definition does not turn on who furnished the data.** So the outside analysis cannot rest on
  that; if the narrow reading wins, it wins on §20.03 and the Supplied Data definition, which the
  outside analysis did not cite.
- **Aggregation and anonymisation are no defence to anything §20.01 does reach.** *"whether in
  aggregated, anonymized, or de-identified format or not."* That part of the record survives intact.
- **The narrative side of a chargeback is not helped by either reading.** The quality-problem notice,
  the QPN text, the sort invoice and the third-party evidence are Ford's documents, and §16.01(b)(2)
  reaches *"(E) any other information that would reasonably be regarded as being of a confidential
  nature."*
- **A limit on §16, which the record did not have:** Buyer Confidential Information requires, at
  §16.01(b)(1), that the information be *"non-public information that is proprietary to: (A) the Buyer;
  (B) any of its Related Companies; or (C) any third party..."* A supplier's own inspection record,
  proprietary to the supplier, fails that gate - **so Section 16 does not independently cover it.**
  §20.01 carries no such "proprietary to Buyer" gate, which is why the whole question lands on §20.

---

## 5. Ford: service-provider / consultant carve-out - **FOUND**

**§16.03, in full:**

> **16.03 Sharing with Related Companies and Consultants** The Buyer and the Supplier may share
> Confidential Information of the Other Party with their: (a) Related Companies; and (b) consultants,
> contractors, experts, and agents; provided that the person or entity with whom or which the
> information is being shared has agreed in writing to be bound by confidentiality provisions
> comparable to those specified in this Section 16. The Supplier will first obtain the written consent
> of the Buyer if the Supplier or any of its Related Companies wants to share Buyer Confidential
> Information with any party (including any of its Related Companies) that is a motor vehicle
> manufacturer or distributor.

Ford's Spanish text confirms: *"(b) consultores, contratistas, expertos y agentes, siempre que la
persona o entidad con quien o cuya información se comparta haya acordado por escrito estar sujeta a
disposiciones de confidencialidad comparables."*

**§16.04, the outer bound:**

> **16.04 Sharing with Other Third Parties** Neither the Buyer nor the Supplier will share any
> Confidential Information of the Other Party with any third party, including any competitor of the
> other party, without the prior written agreement of the other party, except as may otherwise be
> permitted under the Purchase Order, a Technology Agreement, or other written agreement between the
> parties.

**This directly answers a question the project had recorded as NOT VERIFIED** ("whether OEM purchase
terms permit a supplier to disclose Buyer Data to its own service providers or processors at all. No
document in the record addresses it"). **For Ford: yes, with a written confidentiality flow-down, no
Ford consent needed unless the recipient is a motor vehicle manufacturer or distributor.** Note the
limit precisely: §16.03 permits **sharing** Confidential Information with a vendor; it does not touch
§20.01's separate ban on **use** of Buyer Data *"for any business or other commercial purpose of
Supplier **or any other person**."* Those last five words reach the vendor's own use.

*Aside, since the record relies on it: Aptiv §18.6's "employees only" was not re-read in this run and
is unverified here.*

---

## 6. GM General Terms and Conditions §30

**Version: February 2014** (printed in the document footer: `February 2014`). Copy read:
`https://www.butzel.com/assets/htmldocuments/GM%20General%20Terms%20and%20Conditions%20February%202014.PDF`,
13 pages, full text extracted.

**⚠ GM CURRENCY IS NOT VERIFIED.** GM publishes its GTCs behind the GM SupplyPower login
(`www.gmsupplypower.com` does not resolve publicly; DNS failure). No GM-hosted public copy was
reachable, and trade press indicates GM was adding new supplier-contract clauses as recently as
October 2025. **Treat February 2014 as the newest publicly reachable text, not as confirmed current.**
The project's own record already flagged this ("The GM February 2014 T&Cs... as CURRENT contract
text") and the flag is right.

**§30, in full:**

> **30. Confidentiality; No Advertising**
> Seller will maintain the confidentiality of any information provided by Buyer or its
> representatives, and any materials or information that contain, or are based on, any such
> information. Seller may only use such information in connection with its performance under this
> Contract and will not provide such information to any third party (including, without limitation,
> Seller's subcontractors) without Buyer's advance written consent.
>
> Seller will not, without first obtaining the written consent of Buyer, in any manner (a) advertise or
> publish the fact that Seller has contracted to furnish Buyer the goods or services covered by this
> Contract; (b) use Buyer's trademarks, trade names or confidential information in Seller's advertising
> or promotional materials; or (c) use Buyer's trademarks, trade names or confidential information in
> any form of electronic communication such as web sites (internal or external), blogs or other types
> of postings.

**Definition of the protected information: there is none.** GM §30 uses no defined term. The scope is
built in the clause itself, and **unlike Ford, GM's scope IS keyed to provenance: *"any information
provided by Buyer or its representatives."*** The reach beyond that is the extension *"any materials
or information that contain, or are based on, any such information."*

**So on the disputed question, GM reads the way the outside analysis described Ford.** A supplier's
own inspection record is not "information provided by Buyer"; it is caught only if it is *"based on"*
information Ford - GM - provided, which is arguable for a measurement taken against GM's drawing or
specification and weak for the supplier's own defect rate or its own record of which argument won.
**The project's recorded gloss on GM - "No marking requirement, no materiality threshold" - is correct
as far as it goes** (there is no marking requirement and no materiality threshold) **but it is not a
relationship-based definition.** GM is narrower than Ford's definition on its face. Calling GM "a
second independent foreclosure" of the same breadth overstates it.

**GM service-provider carve-out: NOT FOUND, and worse than absent.** §30 bars providing the
information *"to any third party (including, without limitation, Seller's subcontractors) without
Buyer's advance written consent."* **GM names subcontractors expressly as inside the bar.** No
consultant, agent, auditor, accountant, advisor or processor exception appears anywhere in the 13-page
document; a full-text grep for those terms returns nothing in a confidentiality context. So **Ford
permits a vendor under flow-down and GM does not permit one at all** - the opposite of how the record
treated the two.

One adjacent GM provision worth noting, §29, because it is the mirror image and shows the drafter
knew how to key a clause to provenance:

> Any technical or other information provided by Seller to Buyer or its affiliates will not be subject
> to confidentiality or nondisclosure obligations unless the parties have entered into a separate
> written confidentiality and nondisclosure agreement signed by their respective authorized
> representatives prior to the effective date of this Contract.

---

## 7. What in the project record changes, and what does not

**Stands:**
- Ford PPGTC Jul. 1, 2021 is the current published version, and the §20.01 quote is verbatim correct.
- "Ford defines Buyer Data by RELATIONSHIP to Ford, not by marking or secrecy" - correct as a
  description of the definition's axis. Confirmed twice (definition text; §16.01's
  "regardless of any legend or marking").
- Aggregation and anonymisation are foreclosed for whatever §20.01 reaches.

**Changes:**
- **The breadth was recorded as settled and it is not.** §20.03 and the "Supplied Data" definition put
  the supplier's own production, quality and logistics records in a separate box that §20.01 never
  mentions and that carries no use restriction on the supplier. That subsection does not appear
  anywhere in the project record. **The correct status is AMBIGUOUS, with the ambiguity sitting inside
  Article 20 itself.**
- **"Whether OEM purchase terms permit disclosure to a supplier's own service providers" is no longer
  NOT VERIFIED.** Ford §16.03: permitted with written flow-down. GM §30: expressly not permitted,
  subcontractors named.
- **GM is not a second instance of Ford's definitional breadth.** GM §30 is provenance-keyed
  ("provided by Buyer"), extended only by "contain, or are based on." The "two independent
  foreclosures" framing should be one broad-but-ambiguous instrument plus one narrower,
  provenance-keyed instrument that is nevertheless absolute on third-party disclosure.

**Untouched by this run:** the antitrust exposure (MEMA guidelines), Magna §19, Aptiv §18.6, Toyota,
Nissan, the portal terms of use, and everything about whether the business is worth doing. Not
examined, no view offered.

**Not verified / blocked, stated plainly:**
- Ford's English PPGTC PDF on Ford's own domain (404 at the guessable path; microsite is JS-rendered).
  English text came from a hosted copy, authenticated against Ford's own Spanish PDF.
- Ford's PII Supplement and Information Security Supplement (§20.04, §20.05) and all Supplier Guides  - 
  behind the FSP login, never read. Either could qualify §20.
- Whether GM's February 2014 GTCs are still current - GM SupplyPower not publicly reachable.
