# METHOD - how this project finds, screens and kills venture concepts

**Durable protocol. `STATE.md` owns live decision state and points here; this file owns the process.**
**Read this before generating or evaluating any new idea.** It is only what you DO; every `[C-n]` anchor
is the evidence for that rule in **`CASEBOOK.md`** beside it. Why any of it exists: **[C-1]**

---

## PART 0 - THE ONE RULE THAT GOVERNS EVERYTHING BELOW

> **IDEATION AND EVALUATION MUST BE DIFFERENT AGENTS, AND THE EVALUATOR MUST BE BLIND.**
> The agent that proposes a candidate never screens it. The screening prompt names no suspected
> competitor and no suspected rung. The gate is a third agent. Mutation is a fourth. **[C-2]**

- **0.** Every ideation agent returns **the differentiated claim in ONE SENTENCE** alongside the asset - *"the thing an incumbent would already have to be claiming for this to be dead."* Ideation still does NOT research competitors.
- **1.** Ideation agents get the stage 1-2 criteria, the three surviving asset categories and the DEAD list (so they do not regenerate a corpse). They are **not** told what is expected to work.
- **2.** The screening prompt gives the asset, the mistake, the customer and the ladder, and **nothing about where it will die**: no suspected competitor, no suggested rung, no "check this hard." It reports in Part 7's 3c format (the case for, the scored weaknesses, whether K0-K4 fired), and the findings fall where they fall.
- **3.** The main session may generate candidates, but must then write the screening prompt with none of its own priors in it.
- **4.** **⚠ A BLIND PROMPT IS NOT A BLIND SCREEN. THE REPO CAN LEAK.** Screening agents have full repo access and are told `STATE.md` is authoritative, so **predictions live in `predictions/` and NOWHERE a screening agent is told to read.** `STATE.md` may name a candidate and its live status; it may never carry a predicted mechanism, a rung guess or a confidence column. **Mechanical check: `tools/venture-blind-check.sh` (in this package), run before dispatching any screen.** **[C-59]**

**The prediction corollary.** Where the main session generates or ranks, it records its predictions in
`predictions/` **before** results land and scores them afterwards - **verdict AND rung**, because
predicting death is easy and predicting cause is the part that tests the method. **[C-3]**

**Calibration: PREDICT THE MECHANISM, NOT THE RUNG.** Two rounds of default-rung guessing have now
failed in opposite directions: round 2 defaulted to rung 4 and scored 2 of 4; round 3 corrected to rung 3
and scored 0 of 3 clean, with two candidates dying at rung 5. **A default rung is a prior about the world,
not a claim about the candidate.** Name the specific mechanism you think kills it and let the rung number
follow. Where the mechanism was named precisely, it was right even when the number was wrong. **Being
right for the wrong reason is worse than being wrong.** **[C-3]**

---

## PART 1 - THE ORDER. Follow it forwards.

**Stage 0. Room gate (minutes). THIS IS K0 [C-72]: a candidate outside the eligibility caps is dead, and
it is the only kill that needs no search.** Check the candidate against **`STATE.md` -> THE ROOM**: the
published JTBD rubric, the eligibility caps (<$10k funding, <$5k revenue, **no Purdue IP**), and the panel
composition. A candidate that cannot name a specific customer and a specific job cannot score, however
good the market analysis is. **[C-4]**

**Stage 0b. THE LANE GATE - run ONCE PER CUSTOMER SEGMENT, by the main session, BEFORE any ideation agent
is dispatched. [C-54]**

> **IS THIS CUSTOMER CONTRACTUALLY ABLE TO CONTRIBUTE ANYTHING AT ALL?** A customer whose business runs
> through one dominant counterparty may be barred from contributing **every** record they touch, not just
> the one you asked about. The clauses that do this are drafted to catch derived data - *"whether in
> aggregated, anonymized, or de-identified format or not"*, *"or are based on"*, *"any other information
> relating to this Order"* - so scrubbing, aggregating and **even training a model on it** are all caught.
> **When that is true, no private-by-operating asset is available from that customer in ANY formulation,
> and there is no mutation to find.**
> **Under the split (Part 3) this is a lane-level K2 HYPOTHESIS on one instance: it closes a lane for
> ideation and scores as the heaviest rung-2 weakness on a candidate already in
> the lane. It does not kill one [C-72].**

> **⚠ THE FAST FORM OF THIS QUESTION, added 2026-09-11 from round 14. ASK IT FIRST, IT COSTS NOTHING:**
> **IS THERE A CONTRACT BETWEEN YOUR CUSTOMER AND THE COUNTERPARTY AT ALL? NO PRIVITY, NO FORECLOSURE.**
> I predicted the axis was PUBLIC vs PRIVATE counterparties and that was the wrong axis. Round 14's two
> cleanest candidates both face PRIVATE opponents and are clean anyway, because no data agreement exists
> between the parties: a royalty owner's lease *"is a conveyance, not a data-sharing contract, and the
> check stub is the operator's disclosure to the owner, not the owner's licensed access to operator
> data"*; a plaintiff firm has no contract with the insurer whose examiner it is grading. **Both
> candidates that DID foreclose had privity** (an MSP supplier agreement, an accreditor policy manual).
> **So: privity first, then read the clause. A customer with no contract cannot be gagged by one.**

**It is here, and not in stage 1, because its whole value is saving a LANE, and a rule that runs after
ideation has already generated the lane cannot do that.** One document read; it costs less than one
ideation agent. **A lane closed this way is written to `STATE.md` -> DEAD CUSTOMER LANES and handed to
every future ideation agent alongside the DEAD list, or the next round regenerates straight into it.**
**Evidence: one instance (automotive Tier-2 under Ford, GM and Magna terms). Treat as a hypothesis about
dominant-counterparty industries until a second lane confirms it.** **[C-54]**

**Stage 0c. ⚠ THE GENERATOR PRE-FILTER. Added 2026-09-07 from a read of the whole kill log at ~40 screened
candidates and ZERO survivors. Run it on every candidate BEFORE it is written down, by whoever generates
it. Two questions, about fifteen minutes, no search budget. [C-68]**

**THE FINDING THAT FORCES IT: the kill log has a signature, and it is a property of the GENERATOR rather
than of the world.** Of the roughly 30 kills carrying a recorded mechanism, **about 22 chose a customer who
is the WEAK party in an asymmetric relationship with one dominant counterparty** - a subcontractor under a
GC, a Tier-2 under Ford, a travel agency under ARC, a provider under a broker, a repair station under the
FAA, a small facility under EPA. **And the recurring kill mechanisms are not a random assortment. They are
an exhaustive list of what a dominant counterparty does:** it RESERVES the determination (E2, chargeback),
PUBLISHES the answer free (CMS, BRCGS, FDA, RRC, cities, ARC/IATA), FORBIDS the pooling (Ford PPGTC §20.01,
Fannie A3-4-01, FCA eSupplierConnect), ABSORBS the cost (Sabre's fare guarantee), CAPTURES the mistake
upstream (ModivCare buying WellRyde), or is COMPELLED to provide the remedy (FERC, state DOT referee
tests). **The candidates that died to ordinary competition instead - freight brokerage, skilled nursing,
SDS authoring, WPS - are precisely the ones whose customer was NOT structurally weak.** The generator has
been drawing from one urn and the urn is empty for a reason.

> **0c-i. DOES THE EVIDENCE OF THE MISTAKE PHYSICALLY COME BACK TO YOUR CUSTOMER'S BUILDING?** Not "can
> they request it," not "is it about them," and - **sharpened 2026-09-07 by the first run under this
> rule** - not merely "do they possess a record." **Does the graded outcome physically arrive?** A
> rejected pallet on the dock. A cylinder break report in the mail. A lien served on the job. A tenant's
> audit letter. A driver reporting the bridge was lower than the map said. If the record lives with the
> counterparty, the counterparty decides whether you exist, and across ~22 kills it has decided no every
> time. **The one candidate whose customer owns its own record outright - the subcontractor's own
> subcontract read against the prime it was handed - is the ONLY candidate that ever cleared rungs 3 and 4
> cleanly against a full sweep.** n=1 positive against ~22 negative, so treat it as a strong prior, not a
> law.
>
> **⚠ AND 0c-i HAS A SIDE EFFECT THAT MUST BE CHECKED IN THE SAME BREATH, found by the ideation run
> itself.** Pushing the grading record into the customer's hands pushes you toward customers **whose only
> checker is themselves**, and those die at stage 2b. **Four of seventeen rejects in the first run died
> exactly that way** (bid-loss prediction, manufacturer-side warranty adjudication, distributor margin
> leakage, several rental variants) - graded only by the customer's own P&L. **The genuinely hard box is
> RECORD IN HAND *AND* AN EXTERNAL CHECKER, and the reason the kill log is full of weak parties is that
> those two conditions co-occur most naturally when the counterparty is both the checker and the
> record-holder.** So run 0c-i and 2b together, never 0c-i alone. **The physical-arrival test is what
> reconciles them: a rejected pallet arrives BECAUSE an external checker rejected it.**
>
> **⚠⚠ AND PHYSICAL ARRIVAL DOES NOT GIVE YOU A DOLLAR. Added 2026-09-11 from round 16, where a blind
> screen inverted the ideation file's own best structural claim.** That file argued that when an object
> comes back on a truck "the dollar is automatically real." **The four object-return candidates were exactly
> the four with NO verified price, because the loss lands inside the customer's own P&L as freight, rework
> and carry, and nobody publishes their own P&L. The two verified prices in that lane belonged to the two
> candidates where nothing physical returns.** **ONLY A THIRD PARTY WHO BILLS FOR THE MISTAKE PRODUCES A D1,
> AND IT ONLY BILLS WHEN A STATUTE, TARIFF OR ORDINANCE TELLS IT TO.** So 0c-i buys you ATTRIBUTION (rung 5b)
> and a CHECKER (2b); it does not buy you MAGNITUDE (rung 1). Run them as separate questions.
>
> **AND READ THE PRICING INSTRUMENT'S LIMITER IN THE SAME BREATH. A headline multiplier is not the number.**
> Both verified prices of round 16 carried a cap or a floor in the same instrument: a county waives strength
> surcharges under $200 quarterly, and N.C. G.S. 106-284.42 (*"in no case shall the penalty exceed the retail
> value of the product"*) caps a statutory "three times the deficiency" back down to 1x one lot.
>
> **0c-ii. IS THERE A FUNDED SEAT AT YOUR CUSTOMER WHOSE JOB ALREADY INCLUDES THIS?** This is Part 2b's D3,
> pulled forward from rung 2.5 to before generation, because it costs one search and it has now capped
> FOUR candidates across four industries after they had each consumed a full screen. **Ask it as: whose
> job description would this task be a line in, and does that person exist at a company this size?**

**Both are answerable before a candidate is written down, and between them they would have killed roughly
24 of ~40 before any of them cost a screening agent.** A candidate failing either is not forbidden - it is
recorded as failing it, so nobody re-derives the same finding at rung 3 a week later.

> **⚠ 0c-iii. THE POSITIVE VERSION, AND IT IS THE MOST USEFUL THING IN THIS FILE'S GENERATOR SECTION.
> Found 2026-09-07 by the second ideation run, which was asked to work inside 0c-i AND 2b and reported
> back an unasked-for structural finding. [C-70]**
>
> **DOES YOUR CUSTOMER *HIRE* THE GRADER?**
>
> An accredited calibration laboratory. A proficiency-testing provider. A certification body. A federal-state
> produce inspector the receiver ordered. **A grader-for-hire is an external checker - so 2b passes - and it
> is structurally incapable of running any of the kill mechanisms in the log:**
> - **it cannot RESERVE the determination away from you**, because you commissioned it;
> - **it cannot PUBLISH the answer**, because the answer is specific to the customer paying for it;
> - **it cannot FORBID the pooling**, because the resulting record is the customer's property;
> - **it has no incentive to CAPTURE the mistake upstream or ABSORB it**, because grading is what it sells.
>
> **And it fixes the cold start for free: certification and accreditation schemes REQUIRE the customer to
> retain exactly the documents the asset is built from**, so a new entrant can back-test on a customer's own
> history from day one - which is the answer to the room's criterion 7 that a private-by-operating ledger
> otherwise cannot give.

**⚠⚠ 0c-iii IS PARTLY WRONG AND THE COUNTEREXAMPLE ARRIVED THE SAME DAY IT WAS WRITTEN. THE "CANNOT
PUBLISH" BULLET IS FALSE. Corrected 2026-09-07 by the S1 screen. [C-70]**

> **A DOMINANT COUNTERPARTY PUBLISHES TO CONTROL YOU. A HIRED GRADER PUBLISHES TO WIN YOU.**

A grader-for-hire competes for your **recurring** spend, and the way a competitive service vendor sells is
**content marketing** - white papers, worked cases, webinar series, free templates. **So it gives the
adjacent expertise away at commercial scale, which is a cheaper and more reliable kill than anything a
dominant counterparty does.** Worked case: the largest independent accredited calibration lab in North
America publishes a free white paper containing the entire OOT impact method with four worked numeric
cases, including the arithmetic that reaches *"we can conclude with reasonable confidence that no product
was affected"* - the differentiated claim, given away, by the hired grader.

**⚠ SECOND INSTANCE 2026-09-07, hours later, on an unrelated candidate (proficiency testing), so this is a
RULE and not a hypothesis. And it sharpens into the precise statement:**

> **0c-iii IS A RUNG-2 AND RUNG-5 IMMUNITY. IT INVERTS AT RUNG 3.**
> Because the customer commissioned the grading, **rung 2's pooling check and rung 5's buyer-standing check
> both pass cleanly - which almost nothing in the kill log does.** But the grader competes for the same
> dollar, and grading is what it sells. **A paid grader cannot FORBID you; it UNDERCUTS you, because
> attached service is how it defends its grading revenue.**
>
> **A GRADER-FOR-HIRE IS THE ONLY COMPETITOR THAT CAN PRICE THE DIAGNOSTIC AT ZERO AND STILL PROFIT.**

Second worked case: the PT provider **gives the root-cause half away by name** - *"contact our technical
support group. We will guide you through the most effective corrective action process and, if necessary,
we will provide a FREE QC Standard to help get you back on track!"* - and **sells the definitive empirical
pre-check for $42-$66**, a past PT sample explicitly marketed for *"practicing/checking tests that have
been problematic."* **A prediction from a proxy cannot beat a measurement that costs fifty dollars.**

**So add UNDERCUT to kill rule 6's shape list and run it by name whenever the customer hires the grader.**

**What survives of 0c-iii, and only this:** hiring the grader genuinely removes **RESERVE** (nobody can
withhold the determination from you) and **FORBID** (nobody bars you pooling your own certificates), and it
buys clean passes at rungs 2 and 5. **It does NOT remove GIVES or PUBLISHES - it makes them more likely.** And the immunity does not extend to
the certification-body grader at all: **PRI Registrar's client terms §1.01 make all reports and records
*"the sole and exclusive property of PRI."***

**Net: 0c-iii remains a useful generator prompt and is NOT a survival predictor. Two of its four immunity
bullets are refuted.** Recorded here rather than quietly softened, per Part 9. **[C-70]**

**⚠ AND THE TENSION THE SAME RUN FOUND, WHICH IS NOT RESOLVED AND MUST NOT BE PAPERED OVER.**

**PHYSICAL ARRIVAL AND FREQUENCY PULL AGAINST EACH OTHER: the more consequential the checker, the less
often it acts.** Demanding that a real external party mail a graded verdict kills most candidates on
**stage 2c** rather than on competition or economics - an ICE Notice of Inspection, an IFTA audit (Articles
mandate an average of **3% of licensees per year**), an IRS Letter 226-J, an FDA inspection. **A checker who
grades you once a decade cannot support a learning loop however expensive the verdict.** Five of the second
run's rejects died exactly there.

**And the honest counterweight to 0c itself, from the same run: the two candidates it could construct with
the STRONGEST 2a and frequency were the two where the checker IS the dominant counterparty.** So **the
weak-party signature in the kill log may not be purely a generator artifact.** The most defensible reading
of all the evidence so far: **the weak party is where the pain is dense enough to fund a product; the
paid-grader lane is where standing is clean but the pain is thinner and more diffuse. 0c relocates that
tension rather than dissolving it, and a candidate should be asked which side of it it is on.** **[C-70]**

**⚠ AND THE HONEST LIMIT ON THIS RULE: the weak party is where the PAIN is, and the room's rubric scores
pain.** This pre-filter is not an instruction to go sell to enterprises. It is an instruction to notice
that pain and standing come apart, and that ~40 candidates were generated as if they did not. **Where a
candidate insists on the weak party, it must answer 0c-i and 0c-ii affirmatively or it is starting two
rungs down.** **[C-68]**

**Stage 1. Find the ASSET, not the task.** Ask what will exist because this product runs that does not
exist today and that a competitor cannot buy. **If you cannot name the asset in one sentence, stop. Do
not proceed to research it. [C-5]** (A generator-side stop, not a screen kill; a screened candidate that
cannot name one scores 1 on criterion 4 [C-72].) Then four tests, all before spending any search budget:

- **1a. A great public asset is an already-mined asset.** Quality is not a moat; quality attracts miners. What survives is **a nuisance to assemble**, **private and only becomes yours by operating**, or **inside the customer's own documents**. Treat "there is a great public dataset for this" as a YELLOW flag raising priority on **rungs 3 AND 4** - never skip rung 3. **[C-6]**
- **1b. Does the data record OUTCOMES, or ADMINISTRATION?** A dataset of administrative events cannot support a product predicting technical failure, however big it is. Check resolution too: one bit is not a model. **Read the actual column list before valuing any dataset. [C-7]**
- **1c. Does the asset cover the segment you will sell to?** A dataset can be famous and bulk-downloadable and still be defective for exactly your customers. **Look for the publisher's own coverage caveat first. [C-8]**
- **1d. "Scattered across parties" does not mean "unpublished."** **Extract 2-3 ACTUAL documents before valuing scattered institutional knowledge.** Fragmentation creates an asset only when the pieces are **OUTCOMES**, not **REQUIREMENTS**. **[C-9]**
- **1f. ⚠ IS THE ANSWER COMPUTED, OR IS IT OBSERVED? Added 2026-09-07, and it is the cheapest test in this file. [C-71]** Ask: *to produce my answer, do I look something up in the world, or do I do arithmetic on numbers the customer already holds?* **If the answer is DEDUCED from the customer's own two documents, there is no outcome to observe, therefore nothing to pool, therefore NO PRIVATE-BY-OPERATING ASSET IS AVAILABLE IN ANY FORMULATION.** Worked case: "did this out-of-tolerance gage invalidate that measurement" is settled by shifting the acceptance limit by the as-found bias plus the lab's uncertainty and comparing it against the recorded reading. **A cross-customer ledger of what "actually" invalidated measurements cannot beat an inequality over two numbers the customer already has.** **This does NOT kill a candidate on its own** - "inside the customer's own documents" is still one of the three surviving asset categories - **but it forecloses the private-by-operating moat, so the candidate must name a different one, and "our data gets better as we run" is not available to it.** The distinguishing question is then how HARD the computation is: bespoke document reasoning across two private contracts is defensible; an inequality is not.
- **1e. DOES THE OUTCOME COME BACK TO YOUR CUSTOMER, IN A FORM THEY CAN HAND YOU?** A private-by-operating asset assumes the graded result lands in the customer's lap. Often it does not. Three questions, all answerable in minutes and all before any search: **who OBSERVES the outcome** · **is the cause ATTRIBUTABLE, or confounded by the observer's own economics** · **may it be POOLED, or does a contract the customer already signed forbid it.** This is the cheap version; rung 5 is where you verify it. **[C-51]**

**Stage 2. Find the expensive, GRADEABLE, REPEATING mistake the asset predicts or prevents.** Not "an
expensive task." A **mistake**, because that is what makes correctness worth paying to guarantee. It must
be **expensive to the buyer** in a same-cycle, verifiable way (money back, a penalty avoided, a trip not
wasted) and never hypothetical future savings; **gradeable fast**, so an expert can tell within minutes
whether the answer was right; and **frequent**, so the loop learns.

**⚠ RULING 2026-09-07, because a candidate was nearly killed on a misreading: "GRADEABLE FAST" MEANS
VERIFY-FAST, NOT ARRIVE-FAST.** The clause is about the expert's verification, not the ground truth's
latency, and stage 3's a16z screen says the same thing (*"can an expert quickly tell what the AI got right
or wrong"*). **The only arrival-shaped requirement in this file is 2c FREQUENCY**, plus C-70's note that a
checker who grades once a decade cannot support a loop. **A 28-day concrete cylinder break is a LAG, not a
RARITY** - a producer is graded thousands of times a year - **so it is a cold-start and iteration-speed
problem for the builder, not a method violation. Do not re-litigate this.**

- **2a. Where does the money sit - the document, or the physical act it records?** Ask: *if this paperwork became instant and free tomorrow, how much of the customer's bill actually disappears?* If the answer is "a little, the rest is testing, travel, materials, or a licensed person's signature," stop. **[C-10]**
- **2a'. DOES YOUR ASSET ATTACH TO THE MISTAKE YOU NAMED?** A claim with two halves can address two different populations without anyone noticing. Verified case: the mistake was an incomplete trip log, the asset was reconsideration outcomes by reason code, **and under the instrument incomplete logs route to RESUBMISSION rather than reconsideration - so the asset described a different set of denials entirely.** Write the mistake and the asset next to each other and check they are about the same events. **[C-56]**
- **2b. No checker, no business.** **Name the checker - auditor, customer, regulator, payer - and quote the rule that makes them check.** If you cannot, the fragmentation is decoration. **[C-11]**
- **2c. How often does the obligation recur for the same customer?** **Count purchases per customer per year, and name the mechanism.** A renewal clause is the cleanest; new units, new SKUs, new sites, new projects and new parts all count equally. Below roughly one purchase per customer per year, it is a project business. **[C-12]**

**Stage 3. Run the external screens (one hour, no budget). Use these as the generator instead of
"expensive human task." [C-13]**
- **a16z's four-part vertical-AI test** - can an expert quickly tell what the AI got right or wrong · is the work hard enough that judgment matters · does it happen often enough to learn · can you start with one assignment and grow into the whole job.
- **Bessemer's three tests** - market structure · delivery economics · defensibility.

**Stage 4. Run the ladder (Part 3). Stop only at a KILL (K1, K2, K3); otherwise run every rung and record
the scores.** Then run **THE FINAL GATE (Part 4)** on every candidate still alive. "Survivor" means alive
after the gate and ranked first on Part 8's rubric. **[C-72]**

**Stage 5. Get the REST of the customer evidence** (the demand ladder already ran at rung 2.5).
**Any demand evidence outranks every verified competitor absence in this repo. [C-15]** But rank the
evidence: a published price beats a remembered one. See **Part 2b** for the ladder and the bar. Where a
call is the right instrument, bring back their words, not a paraphrase.

**Stage 6. Only now, decide the implementation. AI goes LAST - but it must be THERE. [C-14], [C-52]**

The ordering is unchanged and is not negotiable: if "we use AI" is the answer to *why now*, there is no
answer, and a candidate reverse-engineered from *"what could AI do here"* is obvious to a judging room.
**But the terminal goal is an AI-NATIVE company, not a services business with a model bolted on**, and
the room punishes services delivery models (kill rule 1). So when you reach this stage, the candidate
answers three questions. **⚠ THEY SCORE; THEY DO NOT KILL. Demoted from gate to weakness 2026-09-07 by
the zero-pass audit [C-72]: the learning-loop requirement killed the best-evidenced candidate on the board
(supplier chargeback: six rungs and all four gate questions cleared, D1 of $1,000 per part number) on a
moat the room does not score. A candidate without a cross-customer loop records "no compounding moat" as
a weakness on criterion 5 and stays alive.**

1. **WHAT DOES THE MODEL DECIDE?** One sentence, in the form *"given X, it decides Y."*
   **A decision, not a draft.** Drafting is typing. A decision is a judgment somebody is currently paid
   for, where being wrong is expensive and an expert can tell within minutes that it was wrong. If the
   honest answer is "it fills in the form faster," the candidate is NOT AI-native and must be recorded
   that way rather than dressed up.
2. **WHY IS THAT DECISION ONLY AUTOMATABLE NOW?** What about it needs a model rather than rules? **If a
   decision tree from 2015 does it, it is software, not AI-native.** That is an acceptable answer, but it
   must be said out loud, because it changes the pitch and the moat.
3. **WHAT DOES THE MODEL LEARN FROM?** Name the graded feedback that returns and improves it. This is
   the a16z loop from stage 3, and it is the same loop stage 1e and rung 5 verify: the outcome must come
   back, be attributable, and be poolable.

**The one-line test: an AI-native business gets BETTER as it runs, because the outcomes come back. A
service does the same quality of work on day 400 as on day 1.** A candidate that cannot say how it
improves is a service, however much of it is automated, **and that is a scored weakness on criterion 5,
not a kill [C-72]. [C-52]**

---

## PART 2 - THE SEVEN KILL RULES. What the ladder is applying.

Each one is here because it killed or saved something real. The ladder in Part 3 is the ORDER to apply
them in; this is what each one means.

**Under the KILL/SCORE split (Part 3) [C-72]: rule 5 is K1; the duty-holder check inside rung 2 [C-26],
[C-55] is K2; rules 3, 4 and 7 set the evidence standard; rule 6's shapes SCORE, each as a weakness with
its residue named; rule 1 scores on criterion 7.**

1. **The room punishes services DELIVERY MODELS, not services MARKETS. The operative test: does revenue scale with CUSTOMERS or with HOURS? Ask what the tenth customer costs to serve.** If the honest answer names a person doing work, it is a services delivery model however unglamorous the market. An unglamorous services industry is a GOOD market to sell into; selling your own hours into it is what loses. **[C-16]**
2. **⚠ PARKED 2026-09-07 under Part 9, kept in place only so the numbering of rules 3-7 does not move.** *Sell attested output, not cheap output; pick a category where being WRONG is expensive to the buyer.* **The word "attestation" appears ZERO times in `STATE.md` across ~40 screened candidates. This rule has never killed or saved anything; it is the project's founding thesis, not a screen.** Its live half already survives inside stage 2, which requires an expensive gradeable mistake. **Cut at the next method review unless it decides something first.** **[C-17]**
3. **Search every "nobody does this" claim in the INCUMBENT INDUSTRY'S vocabulary, not startup vocabulary.** A claim that dies to one search is worse than no claim. **[C-18]**
4. **QUOTE THE CLAUSE FROM THE INSTRUMENT ITSELF.** A deadline candidate is not alive until you have read the contract, tariff, statute or policy that creates it. **[C-19]**
5. **MAGNITUDE TEST.** A perfect deadline does not survive a fee floor above the disputed amount. **[C-20]**
6. **THE COMPETITOR THAT KILLS YOU IS USUALLY FREE, NOT FUNDED.** **And it takes four KNOWN shapes: it GIVES the service away to sell something adjacent; it PUBLISHES the answer as a standard-setter or regulator; it CAPTURES the mistake away upstream (a checker's own data-capture tool); or it ABSORBS the cost outright (an indemnity). The list has already grown once, on 2026-09-07, when it was found to be missing half the field. A shape you cannot name is not a shape that is absent.** **[C-56]** The sweep is not finished until you have asked: who already does a worse version of this for nothing, and why? Look at government agencies, trade associations, and anyone giving the service away to sell something adjacent. **[C-21]**
7. **PROVENANCE - fetch the page the number is attributed to, PROPORTIONALLY.** **⚠ AND A KILL-SHAPED CLAIM GETS FETCHED BEFORE A SUPPORT-SHAPED ONE, ALWAYS.** A fabrication that SUPPORTS a candidate gets caught later, because the candidate stays alive and someone re-reads it. **A fabrication that KILLS one is never caught, because the kill ends the inquiry and nobody goes back.** Two instances now: a summarizer invented a ReSpark product claim (the page was fetched and does not contain it), and a search engine asserted that Autodesk Construction Cloud does *"automatic notice deadline tracking"* when Autodesk's own documentation says otherwise. **Never kill a candidate on a capability you have not read on the vendor's own page.** **[C-57]** Fetch the source for any number a kill-or-survive decision rests on; numbers that do not change the verdict are marked NOT VERIFIED and never quoted forward. Also: **check the DATE, not just the page**; **a vendor's own marketing is not evidence for market size or error rate**; **a competitor's blog is not evidence about a competitor**; **"X company does Y" requires X's own page**; **absence of a negative is not a positive** - a refuted prior failure updates you to *no signal*, not to encouragement. **⚠ AND THE UNATTRIBUTED AGGREGATE, added 2026-09-11 after a headline figure survived a full screen and died to one verification.** A large official number is not a market size until the publisher says what CAUSED it. Three checks, all cheap, run them on any agency or industry aggregate before it anchors a pitch: **(1) does the publisher state a cause, or only a label?** **(2) does the publisher book the cause you are claiming on a SEPARATE row, and how big is that row?** **(3) what did the same line read LAST year and what does it read THIS year?** Worked case: CBP's *"Net Revenue Recovered due to Entry Summary Reviews (ESF)"* reads **$667.55M FY2024, $34.41B FY2025, $7.90B FY2026 through July** - a 51.5x jump and a fall back to 23%, with no stated cause anywhere, while penalties sit on their own row at $46.04M, three orders of magnitude below. **A number that moves 50x in a year is an artifact of a policy regime, not a market.** Check the neighbouring rows and the adjacent years before quoting, and name the regime the number depends on. **And when you catch a fabrication, ADD IT to `STATE.md` -> "Do not cite in front of judges" in the same session.** **[C-22]**

---

## PART 2c - ⚠ THE COMPLEMENT TEST. Why the free competitor gives it away, and the four positions it cannot reach.

**Added 2026-09-11 from round 12 (agent-economy lane), where 17 of 24 candidates died and the dominant
kill shape was, for the twelfth round running, a free answer published by an incumbent or a regulator.**

Rule 6 says the competitor that kills you is usually free. It never said WHY, so the generator kept
walking into it. This is the why, and it is predictive rather than diagnostic.

> **HYPERSCALERS AND DOMINANT PARTIES COMMODITIZE THEIR COMPLEMENTS. "Free" is not generosity and it is
> not a land grab. It is a weapon aimed at whatever makes their core good more valuable.**

Worked instance: Cloudflare gives away `isitagentready.com` (free, no login, ~20 standards, **plus a
copy-paste remediation prompt for every failing check**, plus the same scores in URL Scanner and its API,
plus a free Radar dataset over the top 200,000 domains) because a web that agents can transact with sends
more traffic through Cloudflare. Google co-authors the IETF bot-auth draft for the same reason. Every
protocol in the lane is free and foundation-governed: MCP and A2A at the Linux Foundation, AP2 at FIDO,
x402 at zero protocol fees, Content Signals CC0.

### RUN THIS BEFORE WRITING A CANDIDATE DOWN. One sentence.

> **WHOSE CORE REVENUE DOES THIS MAKE MORE VALUABLE?**

**If the answer is a large incumbent, they will give it away and the candidate is dead on arrival.**
If the answer is nobody, or is a party whose interests run AGAINST that incumbent, the candidate is
structurally safe from rule 6. It can still die on demand, price or salience; it will not die on free.

### The four positions free cannot reach, strongest first

1. **WHERE THE PLATFORM CANNOT BE NEUTRAL.** No platform can sell the thing whose job is to establish
   fault against it, its product or its customers. Neutrality IS the product; the moment the platform
   offers it, it is worth zero. *Round 12 instance: Agent Discovery Bank went WEAK, not dead. Microsoft
   publishes the agent-retention half free because it sells Purview; nobody publishes the how-do-I-pry-it-
   out-of-an-adversary half, because no platform has a reason to.*
2. **WHERE THE PLATFORM IS LEGALLY BARRED.** Sealing a drawing, signing an audit opinion, filing as a
   licensed customs broker, practising law or medicine. **AWS cannot take that liability at any price.**
   The most durable escape that exists, and both blind lanes found it unprompted. ⚠ It failed in round 12
   on PRICE and SALIENCE, not on structure: six licensing-board rules exist with **zero** enforcement
   actions, and the review seat is paid for THROUGHPUT. **If any board ever disciplines someone over
   AI-drafted work with a dollar figure attached, this position reopens immediately. Watch for it.**

   > **⚠⚠ AND THE OTHER EDGE OF ESCAPE 2, FOUND 2026-09-11 AND IT HAS TO BE READ EVERY TIME ESCAPE 2 IS
   > USED. THE SAME BAR THAT KEEPS AWS OUT KEEPS YOU OUT.** Escape 2 says a platform cannot take licensed
   > liability at any price. True. **But neither can you, and the licence is not a filing you obtain once
   > and forget.** Worked case, fetched: **CBP HQ H350722 (2026-01-16)** holds that *"A tool does not
   > constitute a 'person' as defined by 19 C.F.R. § 111.1, such that the actual decision regarding the
   > classification of imported merchandise... must be made by a duly licensed customs broker,"* and that
   > **buying the model from a third party does not cure it.** **Where a regulator has ruled that a licensed
   > human must make the actual decision, automation cannot remove the human, so REVENUE SCALES WITH HOURS
   > BY LAW.** That is kill rule 1 arriving through the front door, and no product design escapes it.
   >
   > **So escape 2 protects you from a platform and hands you a services delivery model in the same move.**
   > Before using it, ask the two questions in this order: **(a) is the DECISION I sell reserved to the
   > licence-holder, or only the FILING?** and **(b) how low is the nexus threshold?** Threshold worked
   > case: **HQ 115248 (2001)** sets it at mere *possibility* - customs business arises *"when the
   > possibility exists that corrected classification information derived from the verification process
   > will end up on the entry."* **A possibility threshold means a disclaimer does not save you and
   > "we only advise" is not a position.** Where the answer to (a) is the decision, escape 2 is not an
   > escape for this candidate; it is a reason the category is empty, which is what C-53 demands be named.
3. **WHERE THE PARTY IS OPPOSED TO THE INCUMBENT.** Publishers against crawlers, municipalities against
   datacenter power and water draw, ratepayers against AI-driven rate cases, assessors and school
   districts against tax abatements. **An incumbent will never fund the other side's tooling.** ⚠ **The
   least picked-over of the four, and NEITHER round-12 lane generated a single candidate in it.**
4. **THE NEW SCARCITY ABOVE THE RAISED FLOOR. ⚠⚠ DEMOTED 2026-09-11 BY ROUND 13. THIS IS NOT A REAL
   ESCAPE - treat it as a generation prompt only, never as a defence.** Lane E ran it honestly and **6 of
   its 8 candidates named a large incumbent sitting directly above, usually the party that gave away the
   floor.** **THE REASON: the layer above a free floor is STILL A COMPLEMENT TO THE FLOOR.** Whoever gave
   the floor away wants the layer above it to work, because that is what makes the floor valuable, so they
   extend upward. **Escape 4 relocates inside the complement test rather than exiting it. Escapes 1, 2 and
   3 genuinely exit, because an adversary, a licence and an opposed interest are complements to nothing.**
   The original text follows, kept because it still generates well:** Free commoditizes the layer it measures and pushes the
   rent one layer up, to whatever the free tool CANNOT measure. Ask of any free incumbent tool: what does
   it not check? *Round 12 instance, from the D3 seat count: 50+ funded AI-visibility roles at Stripe,
   Amazon, Pfizer, eBay; **ZERO** postings whose duty is making the company's own API, checkout, auth
   flow or forms work when an agent is driving. **The marketing department owns "can an AI SEE us."
   Nobody owns "can an AI TRANSACT with us."** Cloudflare's scanner checks whether standards are
   PRESENT; it cannot check whether an agent trying to buy from you completes.*

### ⚠ THE FAKE ESCAPE, and it must be named every time it is used

**"They have not gotten to it yet."** Fragmentation, unglamorous segments and per-system integration cost
buy TIME, never SAFETY. A candidate resting on this is betting on execution speed against a company that
has more of it. **Round 12's sole survivor, The Undo Path, rests exactly here, and the file says so.**

### ⚠⚠ THE PERMISSION TEST. Added 2026-09-11 from round 16, where the ideation agent contradicted its own brief.

The round was generated on THE ADVERSARIAL READER: a mistake is priced where a paid opponent reads the
submission before it binds. **The agent could not build it. Every candidate from a genuine two-party
adversary (subrogation, surety, bid protest, App Store review, chargeback arbitration) collapsed at
generation on two-sided buyer, competing members, GIVES or the complement test. All eight it could defend
had a government GATEKEEPER reading an application.** The corrected filter:

> **A MISTAKE IS PRICED WHERE A GATEKEEPER MUST SAY YES IN WRITING BEFORE THE CUSTOMER MAY ACT, AND MUST
> STATE A GROUND WHEN IT SAYS NO.**

**Physical arrival (0c-i), no privity (Stage 0b), non-competing members and a funded seat (0c-ii) all fall
out of that sentence automatically. None of them falls out of "an adversary reads it."** The written ground
is what makes the outcome attributable; the permission is what makes it repeat.

**⚠ AND THE EVIDENCE FOR THE ADVERSARIAL READING IS UNDER-DETERMINED, NOT CONFIRMED.** The 1,490 legal
sanctions may measure DETECTION COST rather than readership: a fabricated citation is checkable in seconds,
an over-stressed beam is not checkable in seconds by anyone. **Across round 16, candidate strength tracked
how cheap detection is, not how strong the adversary is - and it cuts both ways. Cheap detection ATTRACTS
the competitors (three of eight already had a funded vendor making the exact claim); late detection BREAKS
THE LOOP (one candidate's graded verdict can arrive 7,594 days after the defect).** Do not assert the
law-versus-engineering contrast in a pitch as though it were settled.

### ⚠ THE REVENUE-AGENCY RULE. It costs ZERO searches and it predicts D1 availability before you spend any.

> **A PERMISSION GATEKEEPER PUBLISHES ITS RULES ALWAYS, AND ITS DOLLARS ONLY WHEN IT COLLECTS OR PAYS MONEY
> ITSELF.**

Round 16 worked case, eight candidates, one session: **CBP is a revenue agency and publishes $34.41B
recovered via entry summary reviews in FY2025 plus a statutory penalty at "two times the lawful duties";
SBA writes cheques and its OIG publishes $11.5M across 16 loans.** The other six gatekeepers - FDA CDRH,
state insurance departments, BIS, NIH study sections, state franchise examiners - collect nothing but a
filing fee, **so there is no dollar for them to publish and there never will be.** Ask which kind of
gatekeeper you are facing before generating into it.

### ⚠ RATCHET FIRES WHEN THE CUSTOMER IS THE DUTY-HOLDER, NOT WHEN THE CUSTOMER IS THE CHALLENGER.

**A gatekeeper publishes its standard to reduce its own workload**, which is rule 6's PUBLISHES shape wearing
a new costume, and it is the reason the conservative answer is always free and only the less-conservative
answer is saleable. Round 16: it fired on seven of eight, and **did not fire on the single candidate sitting
in escape 3** (a party structurally opposed to the incumbent). **So this rule points the generator straight
at escape 3, which is still the least picked-over of the four.**

---

## PART 2b - THE DEMAND LADDER. What counts as evidence of an unmet need, ranked. [C-50]

**Demand evidence is ranked by how hard it is to FAKE, and the top three tiers are reachable from a
desk.** Run this at rung 2.5, before the expensive desk rungs.

| Tier | Evidence | Why it ranks here |
|---|---|---|
| **D1** | **A published price for the MISTAKE ITSELF** - the checker's own fee schedule, penalty table, deduction rate or chargeback line | The counterparty pricing the error in writing. Nothing is stronger and nobody is guessing |
| **D2** | **A published price for the WORSE SUBSTITUTE** - rate cards, published minimums, contingency percentages, marketplace rates | A transacted price is revealed willingness to pay |
| **D3** | **A SALARY** - job postings whose description IS this task, counted, with the comp band | A firm employing someone to do it is the market's standing bid on the problem |
| **D4** | **A COUNTABLE OUTCOME LEDGER** - regulator, standard-setter or association data giving frequency and severity | Establishes the problem exists at scale. Says nothing about willingness to pay |
| **D5** | **UNPROMPTED PRACTITIONER COMPLAINT, COUNTED** - forums, trade press, with dates and venue | Weak singly, strong in aggregate. Unprompted beats prompted: nobody asked them to complain |
| **D6** | **A PROMPTED OPERATOR STATEMENT ON A CALL** | n=1, recall-biased, and the easiest of all to obtain, which is exactly why it is last |

**THE BAR: rung 2.5 clears only on two independent tiers, at least one of which is D1, D2 or D3.** **Under
the split, "does not clear" means a criterion-3 score of 1 or 2 on the rubric, nothing more [C-72].**
D4 and D5 alone are interest, not demand. **D6 alone is colour, not evidence.**

**⚠ THE UNPAID-MARKET TELL. An EMPTY D3 is the heaviest single weakness on criterion 3 and is recorded on
every screen; under the split (Part 3) it SCORES rather than caps [C-72].** D3 is the only tier that asks whether anyone has a budget line for this job.
**If D3 is empty, rung 2.5 does NOT clear on D1 plus D2 alone. It clears only if D1 is larger than the
annual cost of the labour it would replace at one customer.** Below that, the pain is real and spread too
thin to fund anything, and a verified competitor absence is compatible with there being no money here at
all. **Record the D3 result explicitly on every screen, including "empty."**
**CONFIRMED 2026-09-07 and no longer a hypothesis: four instances across four industries** (inspection
readiness · subcontractor claim notice · vaccine excursion · pay-application withholding). **[C-50]**

**⚠ AND D3 HAS FOUR STATES, NOT TWO. Record which one, by name, on every screen. [C-60]**

| State | What it means | What to do |
|---|---|---|
| **EMPTY** | Nobody is paid to do this | The tell above fires: criterion 3 scores 1 unless D1 exceeds one customer's annual labour cost |
| **FILLED AT THE CUSTOMER** | Your buyer employs someone for this task | The only state that is straightforwardly good news, and it is still not sufficient |
| **FILLED AT THE COUNTERPARTY** | The budget line exists on the OTHER side of the transaction | **Looks like demand, is evidence against it.** The duty usually sits over there too. Go back to rung 2(d) and check the duty-holder |
| **FILLED BUT INCENTIVE-INVERTED** | Someone is paid, and paid for the OPPOSITE answer to the one you sell | **Passes the ladder as written; scores EMPTY on criterion 3 and a weakness on criterion 2.** Read the posting's stated PURPOSE, not just its duties |
| **FILLED, TASK ABSENT** (added 2026-09-11, round 16) | The seat and the budget exist, and the specific answer you sell is not in the duties | **A fifth state, so the table's name is now wrong and that is deliberate.** Better than EMPTY (a budget line exists to sell into), worse than FILLED AT THE CUSTOMER (nobody is currently paid for your answer). Three Lane I candidates landed here with nowhere to record it |

**So the question is not "does someone get paid to do this." It is "is someone paid for THE ANSWER I am
selling."** The inverted case is the one the ladder cannot see: a skilled-nursing admissions director at
$24-27/hr whose posting says the *"primary purpose of your job is to support facility operations by
increasing the facility census"* scores as a clean D3 hit, and would be sold a DECLINE recommendation.

**⚠⚠ TOOLCHAIN, VERIFIED 2026-09-11 ACROSS TWO INDEPENDENT SCREENS: EVERY MAJOR JOB BOARD 403s ON FETCH.**
Indeed, ZipRecruiter, Glassdoor, Ladders and Lensa all refuse the fetcher, and neither round-16 screen could
read a single live customer-side posting end to end. **So a D3 comp band is title-level and NOT VERIFIED AT
PAGE unless it is read from a state or university portal or an employer's own ATS, and the unpaid-market
tell cannot fire in EITHER direction under the current toolchain.** Record that as a tooling limit, never as
a finding about the world. Same session: eCFR, federalregister.gov and congress.gov are unreadable; read
federal regulatory text at Cornell LII.

**⚠ AND "EMPTY" IS NOT "UNRUN." A search that could not reach a posting is a NOT-VERIFIED, not a finding.**
The unpaid-market tell fires only on a real empty, established by looking and not finding. **Any screen
reporting D3 must say which of: EMPTY · FILLED (which of the three) · UNRUN.** **[C-60]**

**What the call still uniquely owns, and it is one thing: SALIENCE.** Every desk tier can establish that
the mistake is expensive and frequent. None of them can tell you whether the operator experiences it as
a problem worth paying to fix, or as weather they priced in years ago and stopped noticing. **That is
the only question worth a phone call, and it is K4, the one kill that comes from a customer and not a
desk [C-72]:** *"when did this
last happen to you, and what did you do about it?"* If two of three cannot name a recent instance or
shrug at the cost, it dies here regardless of how good D1 looked. **[C-50]**

---

## PART 3 - THE LADDER. Every rung runs. Only three findings kill; everything else is a SCORE.

**⚠ THE KILL/SCORE SPLIT. Applied 2026-09-07 (evening) by Veer from the zero-pass audit,
`predictions/2026-09-07-audit-why-zero-pass.md`. [C-72]** Sixty-four candidates were screened under a
ladder where every rung killed and the rule count only ever grew; zero survived, and the ladder had
already killed the lanes of last edition's first and third place. **So a rung may now KILL only on one of
three instrument-verified facts. Every other adverse finding is recorded as a scored weakness with a
number and a quote, and the candidate keeps going.** The ladder no longer stops at the first adverse
finding; it stops at the first KILL, and otherwise runs to the end.

**The three kills. Each must be quoted from the source, never inferred:**

| | Kill | Evidence that counts |
|---|---|---|
| **K1** | **The money cannot be moved.** The recoverable amount at one customer is below the incumbent's published fee floor, or the customer does not control the release of the money | A published fee schedule or rate card; the clause naming who releases the money **[C-20], [C-24]** |
| **K2** | **The instrument does not bind your customer.** The duty, penalty or deadline lands on the counterparty, not on the person paying you | The instrument's own text, grepped for the customer's role **[C-26], [C-55]** |
| **K3** | **The mistake is ALREADY SOLVED for your segment.** Not "an incumbent makes the claim": a product the segment already runs removes the mistake you named, in the segment you sell to. Three parts, all quoted: the claim on its own product page (G1), a named deployment in the segment (G2), AND evidence the job is done there (a stated outcome, a customer saying so, or the free bundle in the customer's existing platform doing it). **Veer, 2026-09-07 (late): *"comp should score not kill unless its actually already solved."*** A claim without the outcome is a weakness on criterion 4. Tested against BOTH the one-liner as the room would hear it and the differentiated claim; a claim narrowed below what any incumbent states is a weakness on criterion 2. Confirmed only by the fresh gate agent (Part 4) | The vendor's own page, a named customer in the segment, and the outcome in words other than the vendor's. Marketing reach-down is not a deployment; a feature list is not a solved mistake **[C-31], [C-33], [C-72]** |
| **K0** | **Ineligible.** Purdue IP, more than $10k funding, more than $5k revenue (Stage 0) | The competition's published caps |
| **K4** | **No salience.** Two of three operators on the call cannot name a recent instance of the mistake, or shrug at its cost (Part 2b) | The operators' own words, quoted, from the call. The only kill that comes from a customer |

**A finding shaped like a kill but resting on a search-engine summary, a vendor's marketing claim or a
competitor's blog is a SCORE, not a kill, until the page is fetched (rule 7).**

| # | Rung | K or S | Cost |
|---|---|---|---|
| 0 | **Provenance (rule 7), always on, proportional** | evidence gate | as needed |
| 1 | **Magnitude and control of the money** | **K1** | 1-2 searches |
| **1.5** | **Patent search on the differentiated claim.** Google Patents, in claim language | S | 10 min, free |
| 2 | **Read the primary instrument**, including the portal terms of use and confidentiality clause. The duty-holder check is **K2**; amnesty, free appeal, pooling and legislated-away are **S** | **K2** / S | 1 fetch each |
| **2.5** | **The demand ladder (Part 2b).** D3 state recorded by name. An empty D3 is a weakness on criterion 3, not a cap | S | searches, then one call |
| 3 | **Free substitute, COMPARATIVE.** Not "does a free worse version exist" (one always does) but **how much of the priced mistake does it actually remove, and what residue is left?** Report the residue in the customer's words | S | 2-3 searches |
| 4 | **Incumbent-vocabulary search, claim tested against their own product page.** Competition SCORES on criterion 4; a funded competitor is market evidence. Returns **K3 CANDIDATE** only when G1, G2 and an outcome in the segment are all quoted; the gate agent confirms | S / K3 candidate | 5-10 searches |
| 5 | **Buyer standing** (5a observation, 5b attribution, 5c a label for both answers) | S | a few fetches |
| 6 | **Economics floor** at the target customer size | S | varies |
| 7 | **Full competitor sweep**, only to settle a contested K3 | evidence for K3 | very expensive |
| **GATE** | **Part 4.** G1, G2 and a solved outcome together are K3; G3 and G4 are S | see Part 4 | most expensive |

**What a SCORE returns.** One line per rung: the finding, the number, the quote, and which rubric
criterion it weakens (Part 8's table). **The candidate then ranks on the room's rubric with its weakness
list attached, and the top of the ranking is the submission.** A candidate with six scored weaknesses and
no kill is never "dead"; it is outranked or it is not.

**THE RANKING RULE, without which a weakness list is not a decision [C-72].** (1) A fresh agent per
candidate, blind to the others, scores 1-5 on each of the seven criteria from the weakness list, using
Part 8's "what a 5 looks like" column, VERIFIED evidence only; a NOT VERIFIED magnitude scores 1 on
criterion 3 until verified. (2) Rank by the LOWEST criterion score first, then by the sum. (3) The
salience call sets criterion 3's ceiling. Rule (2) is the point: a 1 on any criterion sinks a candidate
below every candidate with no 1, which restores a floor without a kill list.

**Kill roster and the survivorship caveat on the OLD numbers: [C-23].** Those rates were produced under the
every-rung-kills ladder and do not transfer.

**Once or twice a quarter, run the FULL ladder on one candidate regardless of when it dies, and record
which rungs would also have killed it.** Until then the kill rates are survivorship-contaminated. **[C-23]**

**Inside rung 1 - can the product MOVE the money it is denominated in?** Ask: *who controls the release
of this money, and is it my customer?* **[C-24]**

**⚠ RUNG 1.5 - SEARCH THE PATENT LITERATURE FOR YOUR DIFFERENTIATED CLAIM. Google Patents, ten minutes,
free, and it sees what no product page will. [C-55]** It needs only the one-sentence claim that Part 0
rule 0 already requires ideation to return, so it is runnable immediately and **it belongs above every
rung that costs a search or a call.** A granted claim reading on yours is a capability an incumbent has
already secured and simply has not shipped, which converts a capability gap into a **distribution** gap.

**But the VERDICT is a finding, not a kill, and this is a correction made 2026-09-07 by blind audit.**
Granted claims exist over most plausible software ideas, are frequently narrow or invalid, and are
routinely designed around; **claim construction is not something a ten-minute desk search settles.**
**A hit is carried to the Final Gate as evidence on G1 and G3. It never kills at rung 1.5.**

**Inside rung 2 - five checks. Only the duty-holder check kills (K2); the other four SCORE [C-72].**
- **Is there an AMNESTY that makes prediction worthless?** Before building anything that predicts an enforcement action, check whether the regulator lets the customer erase the penalty by confessing. If so, the product either inverts into the disclosure tool or records the amnesty as a weakness on criterion 4. **[C-25]**
- **⚠ DOES THE INSTRUMENT SHIP ITS OWN FREE APPEAL? Amnesty is not only erasure-by-confession.** An instrument that provides a **free, self-invocable remedy** makes advice about whether to invoke it worthless. Check the price of the remedy and who initiates it. State DOT specs are the worked case: **Texas makes the first three referee tests per project free regardless of outcome; Michigan defines eligibility as an arithmetic inequality over data the contractor already holds, and at the severe end fires the re-test automatically, agency-initiated and agency-paid.** *The instrument does not just create the penalty, it also ships the appeal, prices it at zero for the first three tries, and in the worst case files it for you.* **[C-61]**
- **Does the instrument that would make your asset worthless already exist?** Reading the primary instrument includes reading the free published checklist, guide or template that removes the need for your product. **[C-9]**
- **⚠ MAY THE OUTCOME BE POOLED? READ THE TERMS OF USE AND THE CONFIDENTIALITY CLAUSE. A portal's terms of use IS a contract clause, so this is rung 2's own job, and `CASEBOOK.md` says plainly that it "outranks a phone call, because it can kill a candidate the call would waste itself on."** Any cross-customer ledger needs many customers to CONTRIBUTE, and contributing is a separate legal act from possessing. **Grep the portal's terms and the counterparty's manual for "reports", "compilations", "derived data", and for a purpose limitation.** **Ask it in the form a founder can actually act on: can MY OWN agreement with MY customer carve this in, and does the COUNTERPARTY'S instrument foreclose that carve-out?** Almost no data network could show pre-existing permission in somebody else's contract, and incumbents got their pooling rights by writing them into their own customer agreements - **so a mere absence of permission scores nothing. A foreclosure is the heaviest rung-2 weakness, on criteria 4 and 5, and must be named in the pitch; under the split it does not kill [C-72].** Ford PPGTC §20.01 forecloses it (*"whether in aggregated, anonymized, or de-identified format or not"*); most silence does not. **[C-51], [C-54]**
- **Does the instrument bind YOUR CUSTOMER, or their counterparty?** **Grep the instrument for your customer's role. If they are not named as the duty-holder, you have the wrong instrument. [C-26]** **And "who actually FEELS the pain" is this question, not a market-size question - it belongs here at rung 2, not at rung 6.** A penalty that lands on your customer's customer is the wrong instrument however large it is. **[C-55]**
- **CHECK WHETHER THE INSTRUMENT IS BEING LEGISLATED AWAY, and check the STATUTE rather than the agency's own web page.** A live municipal page said it fined alarm companies four years after the state banned exactly that. **A government web page is not evidence of current law.** Where a penalty falls on a party with a trade association, expect that association to be lobbying to move it, and check whether they have already won. **[C-55]**

**Inside rung 3 - seven checks, ALL SCORE. A shape found is a weakness with its residue named, never a
kill [C-72].**
- **Check for a FREE GOVERNMENT PROGRAM before checking vendors**, whenever the candidate is compliance-shaped. **[C-28]**
- **⚠ RUN ALL FOUR SHAPES OF THE FREE COMPETITOR FROM KILL RULE 6, BY NAME, AND RECORD A FINDING FOR EACH: GIVES it away · PUBLISHES the answer · CAPTURES the mistake away upstream · ABSORBS the cost.** A blank against any shape is a NOT-YET-SEARCHED, never a clean. The two newest shapes each rest on **one instance** and are hypotheses rather than laws: **CAPTURE** - a checker will never build you a tool to fight it with, but will happily build one that captures the data correctly at source, which removes the mistake instead of predicting it (ModivCare bought WellRyde for $12.0M and gives it away); **ABSORB** - before selling a product that predicts a penalty, **check whether somebody already absorbs it, and MEASURE WHAT THE INDEMNITY EXCLUDES**, because Sabre's fare guarantee is bounded to auto-priced tickets and what it leaves behind is the judgment-heavy residue where a model has least signal. **[C-56]**
- **⚠ THREE MORE SHAPES, added 2026-09-07, each on ONE instance and therefore hypotheses. Run them by name too.**
  - **⚠⚠ RATCHET IS THE MOST FREQUENT SCORE SHAPE ON THIS BOARD (it killed under the old ladder). It entered 2026-09-07 as a ONE-INSTANCE hypothesis and fired as primary or contributory in FOUR candidates the same day** - GC lien exposure (the incumbent auto-holds payment), collision repair (every free surface and a new state law push toward billing MORE, never less), ready-mix (`f'cr = f'c + 1.34Ss` is a mandatory arithmetic floor), oversize routing (the permit requires a physical survey that must *"guarantee"* three inches). **The generalisation, and it is worth checking on every candidate before anything expensive is run: MOST OF THESE PRODUCTS HAVE A CONSERVATIVE ANSWER AND A LESS-CONSERVATIVE ANSWER, THE CONSERVATIVE ONE IS ALREADY FREE, AND THE LESS-CONSERVATIVE ONE IS THE ONLY ONE ANYONE WOULD PAY FOR. Ask it at stage 2: which of my two outputs makes money, and may my customer lawfully act on it?** A "no" there is the heaviest rung-3 weakness, on criterion 5.
  - **RATCHET - the published answer is a LIABILITY FLOOR, not merely a substitute. ⚠ SECOND INSTANCE FOUND 2026-09-07, so this is no longer a one-case hypothesis: on the GC lien-exposure candidate, Oracle Textura AUTOMATICALLY PLACES A PAYMENT HOLD on a missing sub-tier waiver and the title company simply will not fund the draw - so a residual-exposure SCORE only earns money when it says something LESS conservative than "hold", which no contract administrator may act on and no title company would honour. Two industries, same shape. [C-62]** When a regulator publishes a recommended action, the product only earns money by saying something **less conservative**, and a duty-holder cannot act on that. **Agreeing with the free guidance is free; disagreeing with it is unusable. The saleable half is the half you cannot sell.** Ask: *what does my product say that the published guidance does not, and may my customer lawfully act on it?* (FDA's Listeria Table 6 against 21 CFR 117.150(a)(2)(iv)'s duty to *"ensure that the affected food is not adulterated."*)
  - **FEE-SHIFT - a statute can manufacture a free lawyer. [C-63]** A prevailing-party fee-shifting provision puts competent counsel in the room at no cost to your customer for any dispute large enough to matter. **Grep the governing statute for "attorney's fees" and "prevailing party" before valuing any dispute-advice product.** (CA Bus. & Prof. §7108.5(c).) **This check has NOT been run on the subcontractor notice candidate and must be.**
  - **COMPELLED - the counterparty may be REGULATED into publishing the answer and providing the remedy. ⚠ SECOND INSTANCE 2026-09-07, also no longer a one-case hypothesis: CA Civ. Code §8200 requires a lower-tier claimant to serve preliminary notice on the direct contractor, and "Compliance with this section is a necessary prerequisite to the validity of a lien claim" - so the STATUTE COMPELS YOUR CUSTOMER'S ADVERSARY TO HAND THEM THE ROSTER FREE, as a condition of having any claim at all. [C-64]** Not a standard-setter choosing to publish, but a regulator forcing your customer's adversary to hand them the answer free. (18 CFR 284.12(b)(2)(iv)-(v) and (b)(3)(vi): a pipeline *"must provide timely information that will enable shippers to minimize the adverse impacts"* and must post and notify.)
- **Fragmentation is only a moat when someone will pay to have it removed.** Before valuing an ugly assembly, ask who has already done it for free - a regulator, a nonprofit, an advocacy group, or a vendor monetising an upsell. **[C-29]**
- **Recurring labour is not a moat** - a barrier that stops a competitor ONCE differs from a cost you pay EVERY MONTH. **⚠ PARKED 2026-09-07: never applied to any of ~40 screened candidates.** **[C-29]**
- **The STANDARD-SETTER usually publishes the failure ledger.** Check the body that writes the standard before believing "which things actually fail is not public anywhere." **[C-30]**

**Inside rung 5 - two questions plus 5c, ALL SCORE [C-72]. [C-51]**
- **5a. Does the outcome come back to your customer AT ALL?** Not "can you technically reach the data" - does the graded result reach the person paying you? **It fails when a third party settles on the customer's behalf**, which is what killed underground utility damage claims: the claim resolves between the utility and the contractor's insurer.
- **5b. Is the outcome ATTRIBUTABLE?** A result that comes back without a cause is a row you cannot learn from. **Ask whether the observer's own economics confound it** (an adjuster who settles rather than fights) and **whether it arrives itemised or as one negotiated number** (a lump-sum reversal cannot be traced to the document that won it).
- **⚠ 5c. DOES A LABEL COME BACK FOR *BOTH* ANSWERS THE PRODUCT CAN GIVE? Added 2026-09-07. [C-66]** A recommender that says accept-or-decline learns only from the branch the customer acted on. **A skilled nursing facility never learns what happened to a referral it DECLINED**, so the model can only ever train on accepts - **and that is precisely why the EHR incumbent wins, because it sees the accepted-stay outcome anyway.** The sibling failure is **base rate**: with 2,646 confirmed cargo thefts against tens of millions of brokered loads, nearly all signal is *"nothing bad happened"*, which is why incumbents anchor on deterministic identity checks rather than prediction. **Ask: for each answer my product can output, what observation later grades it?**

**Inside rung 4 - enumerating vendors is not screening. A patent pointer, then two halves, and the second half is the one that matters. It returns K3 CANDIDATE only when the exact claim is on the incumbent's own page, a deployment in the segment is named, AND the mistake is shown solved there; only the fresh gate agent (Part 4) confirms K3. A vendor list, a funding round, or a claim without a deployment and an outcome is a SCORE on criterion 4 [C-72].**
0. **Run the rung-1.5 patent result first** - if a granted claim reads on your claim, bring it to the gate as a finding. **[C-55]**
1. **Find who sells into this problem** - the incumbent-vocabulary search.
2. **Write your differentiated claim in ONE SENTENCE before searching, then check whether any incumbent already makes that exact claim on its own product page.** Not "are there competitors" but "has my specific claim already been made." Read the product page, the datasheet and the feature list - not the homepage tagline, not a directory listing. **A vendor list is not a screen. A vendor list plus your claim tested against each one is a screen. [C-31]**

- **The evidence standard must be SYMMETRIC.** A vendor's claim contributes to K3 only when it is on the vendor's own page (G1), a deployment in the segment is named (G2), and the mistake is shown solved there; otherwise it is a SCORE on criterion 4 and a **practitioner question** for the customer call. **[C-32], [C-72]**
- **Distinguish a CAPABILITY gap from a DISTRIBUTION gap.** A capability gap requires the incumbent to BUILD something; a distribution gap requires them to change a price list. A distribution-only gap is a gap on a timer - it can still be a real opening, but "we serve smaller companies" is not a moat and must never be the whole answer. **[C-33]**
- **⚠ AN EMPTY CATEGORY WITH OBVIOUS DEMAND IS USUALLY EMPTY FOR A REASON, AND THE REASON IS UPSTREAM OF THE PRODUCT.** When rung 4 comes back clean, **do not record an opening. Record WHICH of three reasons explains the emptiness, and go test that one before proceeding: (i) the asset may not legally be assembled - go read the terms at rung 2 now; (ii) a free actor covers the profitable half - go back to rung 3 and search for the NON-VENDOR actor; (iii) nobody has a budget line - go back to 2.5 and check D3. If you cannot name which, record UNEXPLAINED as a weakness on criterion 4.** Two instances: bid tabulations (ii), supplier chargeback pooling (i). **[C-53]**
- **⚠ SEARCH FOR THE EXITED PREDECESSOR, NOT ONLY THE LIVE COMPETITOR. Added 2026-09-07, three instances in one round. [C-65]** **"Somebody built this and stopped" is stronger evidence than "somebody sells this":** a live competitor proves the market is contested, a dead one proves the experiment already ran. Three places to look, all cheap: **ABANDONED PATENT APPLICATIONS** whose specs disclose your claim (Sample6's US20140046722A1, food environmental monitoring, discontinued); **PAUSED PRODUCTS** saying so on their own site (VeriSight AdmitScore: *"paused... not taking new pilots"*); and **WAYBACK CAPTURES OF DISCONTINUED SERVICE PAGES** (MQMR sold repurchase-demand rebuttal in 2013-2015 and the word "repurchase" is gone from its live site). **Then ask why they stopped.**
- **⚠ THE BUYER'S OWN JOB POSTING IS A RUNG-4 SOURCE, and a better one than any vendor page. [C-65]** A target customer's posting that lists its tooling names the installed incumbent from the buyer's side: a freight brokerage's Carrier Compliance Specialist req listed *"Samsara • Highway • FMCSA Clearinghouse • SAFER / SMS..."* **This costs one search and it is the same search rung 2.5 already runs for D3.**
- **A cheap maturity signal, DEMOTED 2026-09-07 from a check to a line on the rung-4 report: has the category produced a BUYER'S GUIDE?** Directories and "best X software" roundups are the artifact a category produces AFTER the land grab is over. **Recorded on many candidates; never decisive on its own.** **[C-34]**

---

## PART 4 - THE FINAL GATE. Expensive, last, and mandatory before calling anything a survivor. [C-35]

**A FRESH agent runs it, always. Never the screener that cleared the ladder, never the ideation agent
that proposed the candidate, never the main session.** One candidate per gate run - never bundle two.
The gate cannot be blind the way a screener is; it is given the incumbents, but never the verdict:
- **MAY be told:** the candidate, the one-sentence differentiated claim, the named incumbents, and which platforms the segment already owns.
- **MUST NOT be told:** what verdict anyone expects, which vendor is suspected of being the killer, which gate question is expected to fail, or the screener's reasoning. **"Treat X as seriously as Y" is steering and must not appear in a gate prompt.**

**G1 - CAPABILITY. Does the leading incumbent already make your exact differentiated claim?** Read the
product page, datasheet, documentation, demo and any implementation case study of the top two or three
incumbents, and quote what they claim feature by feature against your one-sentence claim. If they
already claim it, you do not have a capability gap. **A claim without a deployment and an outcome in the
segment scores on criterion 4; it does not kill (K3, Part 3).**

**G2 - SEGMENT. Who do they actually DEPLOY to, as distinct from who they market to?** Named customers,
case studies, logo walls, review-site firmographics. **Marketing language always reaches down ("from
startup to Fortune 500"); deployments do not.** A floor visible in customers but absent from any written
policy is still a floor.

**G3 - IS THE GAP CAPABILITY OR DISTRIBUTION?** See rung 4; a distribution-only gap cannot be the whole
answer. **[C-33]**

**G4 - THE FREE-BUNDLE CHECK, run separately from the paid-competitor check.** Does the platform your
customer ALREADY OWNS include this as a module at zero marginal cost? Name the platforms the segment
actually runs and check each. **[C-36]**

**Verdicts under the split [C-72].** **DEAD** only on K3 as Veer set it: the mistake is already solved for
the segment (G1 claim, G2 deployment, and the outcome, all quoted). **ALIVE** otherwise, with G3 and G4
recorded as scored weaknesses; a distribution-only gap must still never be pitched as "we serve smaller
companies" alone. **SURVIVOR** is the alive candidate ranked first on Part 8's rubric; the word is
conferred by the ranking, not by a clean sheet. **PASSED, PENDING A HYPOTHESIS** is retired: under the
rule freeze (Part 9) no rule younger than a screen can touch that screen's verdict.

**The gate's hard limit: when it returns only vendor claims, the remaining question is a PRACTITIONER
question, not a search question.** Stop, and put it in the customer call. Searching further buys
nothing. **[C-37]**

---

### ⚠ THE PREDICTED WEAKNESS LIST. Write it BEFORE dispatching any screen or gate. [C-58], [C-72]

**Before dispatch, the main session writes to `predictions/`: the verdict it expects (K0-K4 or NO KILL),
the mechanism, and the weakness list it expects; it scores itself afterwards.** The old PASS STATEMENT's
second question, "what new rule would have to be invented to kill it anyway", is moot under the rule
freeze (Part 9): no rule younger than a screen touches that screen's verdict, and PASSED, PENDING A
HYPOTHESIS is retired.

**Why this exists, and it is uncomfortable. Every candidate that has ever passed this gate has generated
the rule that killed it.** The supplier chargeback candidate cleared six rungs and passed all four gate
questions on 2026-09-07 - the method's own defined pass condition, met - and was killed the same night by
rung 5c, a rule created that night, which was then generalised into 1e', which closed the whole customer
lane. **The individual finding was well evidenced; under the split it is the heaviest rung-2 weakness and
the candidate is reopened (STATE.md). The SHAPE is the problem: a screen whose pass
condition moves whenever something reaches it cannot be passed, and its output is indistinguishable from
a broken screen's.**

---

## PART 5 - MUTATION. When a candidate may be reformulated, and when that is cheating. [C-38]

**⚠ M0 - THE TRIGGER. EVERY SCREEN, KILL OR NOT, ASKS THE MUTATION QUESTION IN WRITING, AND THE ANSWER GOES IN THE
SCREEN'S OWN RETURN. Added 2026-09-07 because Part 5 was never once invoked across nine kills in a single
round - not declined, simply never asked. [C-67]**

**The protocol was sound and inert.** A rule with a carefully designed brake (M5) had never been touched
because the pedal had never been pressed, and the M5c counter still reads ZERO. **So the question moves
out of the main session's discretion and into the screening agent's mandatory return format**, next to the
D3 result, which is now the model for anything that must not be forgotten:

> **"Does the evidence you gathered force a different formulation of this candidate, or does it not?
> Name the forcing evidence (M1) or answer NONE. 'No principled mutation exists' is a valid and valuable
> answer."**

**The screener proposes; it never mutates.** A named lead goes to a FRESH mutation agent per the rules
below. **A lead recorded and not dispatched is not a tested mutation, and must never be reported as one**  - 
on 2026-09-07 a screener handed over an explicit lead (*"a lead for a mutation agent, not a rescue for this
formulation"*) and it was written down and left. **Untested is not failed.**

**Four findings that same round (kills under the old ladder, scores under the split) admitted no mutation, and they shared one structure worth recognising on
sight: THE BARRIER WAS THE COUNTERPARTY OR THE INSTRUMENT, NOT THE FORMULATION.** A reserved
determination, a liability floor, a free self-invocable appeal, a compelled publication. **When the thing
that weakens you is what the other side is required or permitted to do, M1 cannot be satisfied by any
rewording; the weakness is structural and stays on the sheet - the same conclusion the chargeback candidate reached as "structurally unavailable to this
customer in any formulation."**

**⚠ A SECOND NO-MUTATION SIGNATURE, found 2026-09-07 by the mutation agent on the notice candidate, and it
is the more useful of the two because it is visible from a DEMAND finding rather than from a contract.
[C-69]**

> **THE BARRIER IS FREQUENCY. THE FUNDED SEAT EXISTS WHERE THE TASK FIRES ON EVERY PROJECT, AND DOES NOT
> EXIST WHERE IT FIRES ONLY WHEN SOMETHING GOES WRONG.**

**How to recognise it: several independent surfaces stop at the SAME boundary.** On the worked case three
did - the free tooling (Levelset's calculator), the paid outside vendor, and the funded internal seat all
serve the every-project statutory notice and all stop before the episodic contractual one. **When free,
paid and in-house all draw the same line, the line is a property of the world and no rewording moves it,
so M1 cannot be satisfied.** Contrast this with a single competitor stopping there, which is an opening.

**Two corollaries, both cheap:**
- **Seat funding scales with headcount.** A dedicated specialist appears once a firm carries enough concurrent jobs to fill one. **So a D3 result read at large firms does NOT transfer downward** - it makes a genuine EMPTY at the smaller target band *more* likely, not less. **Read D3 at the band you actually sell to, and say which band you read.**
- **A published clerical wage is a finding about the TASK, not just the seat.** Apogee's notice specialist at **$19-$22/hour** prices that work as throughput rather than judgment. **A judgment product priced against a clerical wage is in the wrong lane, and the wage says so before any competitor sweep does.**

**AND THE PROCEDURAL RULE THIS RUN CONFIRMS: a proposal that changes NONE of the five tuple elements  - 
customer, asset, document set, mistake, checker - IS NOT A MUTATION.** It is positioning, packaging or
pricing, and it belongs at stage 6. Dispatching one as a mutation consumes a blind re-screen at rung 1 to
re-derive findings the file already holds. **Four leads were tested this way and all four failed on it or
on 2b.** **[C-69]**

- **M1 - THE MUTATION MUST BE FORCED BY EVIDENCE, NOT BY THE VERDICT.** State which piece of evidence forced the change. If you cannot name one, it is not a mutation, it is a retreat. **[C-39]**
- **M2 - A MUTATED CANDIDATE RE-ENTERS AT RUNG 1. It inherits nothing.** Treat it as a new candidate with a family resemblance. **[C-39]**
- **M3 - WRITE THE MUTATION DOWN BEFORE RE-SCREENING**, in `predictions/`, stating what changed, what evidence forced it, and which specific kill it is meant to escape. Same discipline as recording predictions before results; without it, nobody can tell later whether the reformulation was principled.
- **M4 - NAME THE ORIGINAL KILL AND SHOW THE MUTATION ESCAPES IT.** Write the escape explicitly. **[C-39]**
**M5 - THE BRAKE: two substantive tests (M5a, M5b), plus an arbitrary counter that escalates rather than
kills (M5c).**

- **M5a - EACH MUTATION MUST BE FORCED BY EVIDENCE THAT DID NOT EXIST AT THE PREVIOUS FORMULATION.** Name the new fact and when it arrived. **[C-39]**
- **M5b - THE CUSTOMER MUST NOT CHANGE.** Changing the document is evolution; changing who pays is a different company, and it enters at stage 1 with none of the family's history. **[C-39]**
- **M5c - AT TWO MUTATIONS, ESCALATE TO VEER. Do not auto-kill, and do not auto-continue.** Present four
  things: the original formulation · each kill with its evidence · each mutation with its forcing
  evidence · what is left of the market. **He decides whether there is a third.** **The number 2 is
  arbitrary and has never bound - revisit it once any candidate actually reaches it, and record what
  happened.** **[C-40]**
- **M6 - CHECK THE MARKET AT EVERY MUTATION.** After each one, re-answer stage 0: can this still name a customer segment rather than a customer? **[C-39]**

**Who mutates: A FRESH AGENT. Always. No exceptions.** Never the screener that killed it, never the
ideation agent that proposed it, never the gate agent, never the main session. **[C-41]**

**The framing of the mutation prompt is the whole safeguard, and it is one word wide.** Never ask *"how
would you reformulate this so it survives?"* Ask instead:

> **"Does the evidence force a different formulation, or does it not? 'No principled mutation exists' is
> a valid and valuable answer."**

Say in the prompt that **a mutation agent returning NONE has done its job correctly.** Steering toward NO
is still steering, so no expected verdict goes in either. **[C-41]**

- **MAY be told:** the original candidate (asset, customer, document set, checker, mistake); **the forcing findings, kill or score, with the verbatim evidence**; the stage 1-2 tests so its output is well-formed; the DEAD list; and the room gate, because M6 requires re-checking market size.
- **MUST NOT be told:** that anyone wants this to survive; which mutation is hoped for; any speculation about salvage; **or how many mutations remain** - an agent that knows it is on its last attempt will stretch to make it count. **The main session keeps the M5 counter privately.**
- **It must return:** what changed, the evidence that forced the change (M1), how the new formulation escapes the original kill (M4), and its M6 answer on market size. A proposal missing any of those is rejected without re-screening.
- **Then the main session records it in `predictions/` (M3) and dispatches a BLIND re-screen at rung 1** - by an agent that has seen neither the mutation's rationale nor the original candidate's history.

---

## PART 6 - TWO DECISION HEURISTICS (not search rules)

**⚠ PARKED 2026-09-07 under Part 9.** *A licensing gate you can cheaply clear is an ASSET, not an
obstacle; the ungated states are the saturated states.* **No candidate in ~40 ever turned on a licensing
gate as an asset, and the one licensing kill on record (duty drawback, 19 U.S.C. 1641) worked as an
OBSTACLE, which is the opposite of what this says.** Kept as a generator prompt, not a test. **[C-42]**

**⚠ PARKED 2026-09-07 under Part 9, same evidence as rule 2: zero hits for "attestation" in `STATE.md`
across ~40 screened candidates.** *Before pitching any attested-output business, name the party who pays
for the attestation and cannot get it any other way.* **Cut at the next method review unless it decides
something first.** **[C-43]**

**And a distinction:** a deadline that triggers a **penalty owed to the government** is not the same as a
deadline after which **the buyer's own money is unrecoverable**. Only the second one is this
pattern. **[C-44]**

---

## PART 7 - HOW TO DISPATCH RESEARCH

**Every agent prompt must carry these four instructions. [C-45]**
1. **"Do NOT spawn subagents. Run the searches yourself."** An agent that delegates loses its findings.
2. **"Never infer, never estimate, never fabricate. If unverified, say NOT VERIFIED plainly - a clean 'not found' is a valuable result."**
3. **"Every number gets a URL, and quote the operative language."** Separate **VERIFIED / NOT VERIFIED** in the return.
3b. **"A SEARCH-ENGINE SUMMARY IS NOT EVIDENCE. Fetch the page and read the words."** Seven bad artifacts were caught in one session on 2026-09-07, in three distinct modes: **FABRICATED** (a sentence attributed to Ironclad that would have killed a candidate outright and is not on the page), **UNSOURCED BUT WIDELY REPEATED** (a "CDC estimates $20M" figure traced to a vendor blog), and **STALE PRESENTED AS CURRENT** (an MQMR service quote, verbatim accurate and a decade dead). **So also check the TENSE:** identical words describing a live incumbent and an exited one are opposite findings. **[C-59]**
3c. **The return MUST explicitly state, in this order: THE CASE FOR (the strongest demand tier reached with its quote, the strongest rung-2 pass, the best D1/D2 number) · the SCORED WEAKNESSES, one line per rung with number, quote and the rubric criterion it weakens · whether a KILL fired (K1/K2/K3) with the instrument or page quoted, or NO KILL · the D3 state by name (or UNRUN) · the mutation answer from Part 5's M0.** A return missing any of the five is incomplete and gets resumed, not accepted. **The case FOR comes first because a return format that asks only what killed it will always find something [C-72].**
4. **Restate the incumbent-vocabulary rule (rule 3) inside the prompt**, with the actual practitioner words for that industry.

**⚠⚠ 5. AIM A SCREEN AT THE RUNG YOU WANT ANSWERED, OR IT WILL NOT GET ANSWERED. Added 2026-09-11, round 16,
and it corrects a standing read that survived fifteen rounds. [C-73]**
`STATE.md` said from 2026-09-07 that **"THE DESK CANNOT MANUFACTURE CRITERION 3"**, on the evidence that
fifteen rounds of screens returned NOT VERIFIED magnitude almost everywhere. **Round 16 pointed both
screening prompts explicitly at rung 1 - "go and find what this mistake costs ONE customer ONCE, in dollars,
from a published fee schedule, statutory penalty, tariff or an operator's own written account" - and three
verified D1s came back in a single session.** The difference was not the lane, the generator or the model.
**Fifteen rounds of screens had been aimed at COMPETITION, so competition is what they reported.**

**The corrected statement: THE DESK CANNOT MANUFACTURE SALIENCE (K4, which comes only from a call). IT CAN
MANUFACTURE MAGNITUDE, IF A SCREEN IS AIMED AT IT.** And the general form, which is the part worth keeping:
**a standing finding of the shape "the desk cannot do X" must be checked against whether any prompt ever
ASKED for X, before it is believed.** A return format determines a return.

**Give each agent ONE lane** - the budget is ~200 web searches per session and it goes fast. **Give
agents the already-established facts explicitly** and tell them not to re-verify. **When an agent stops
without reporting**, resume it and tell it to synthesize with what it has and name the gaps. **[C-45]**

---

## PART 8 - THE SELECTOR. How the search ENDS and a concept gets CHOSEN. [C-46]

**The stopping rule. Generation STOPS at the earlier of: a candidate passing the Final Gate, or the
SEARCH-STOP DATE.** After that date no new candidates are generated, whatever the board looks like.
Screening already-live candidates and closing their open checks continues; ideation does not.

**⚠ A stop was applied for three hours on 2026-09-07 (evening) as item 6 of the zero-pass audit and
REVERSED BY VEER the same night: *"dont stop generation."* [C-72]** Generation continues to the SEARCH-STOP
DATE. What the audit still binds: a new candidate runs the split ladder (Part 3), returns in the 3c format
and ranks by the ranking rule; and the two calls STATE.md names are owed regardless of what is generated.

**The dates:** SEARCH STOP **2026-09-14** · COMMIT **2026-09-21** · prelim due 2026-09-27 · final
2026-12-11 (in person, mandatory). Veer overrides. **[C-47]**

**✅ RESOLVED BY VEER 2026-09-07 (morning), REAFFIRMED THE SAME NIGHT (*"dont stop generation"*):
"Continue research and find more ideas." A REVERSED GATE PASS DOES NOT STOP GENERATION.** The gate-pass condition fired on the supplier chargeback candidate and then that
candidate died the same night, so the condition that fired no longer exists. **Generation continues to the
SEARCH-STOP DATE (2026-09-14) as the only live stopping condition.** Veer overrides, per this file's own
rule, and he was asked before it was inferred. The original question is kept below for the record.

**⚠ OPEN DECISION, FOR VEER, RAISED 2026-09-07 AND NOT RESOLVED HERE. DOES A REVERSED GATE PASS STILL STOP
GENERATION?** The stopping rule fires at the earlier of a gate pass or the date. **A candidate DID pass the
Final Gate on 2026-09-07** - supplier quality chargeback, all four questions, the only one ever to do so  - 
**and was killed the same night at rung 5c.** So the first condition fired eleven days before the date, and
then the thing that fired it died. **This file does not say whether the kill un-fires the stop, and the
main session should not infer it.** The live stake is one named lead (the roadside candidate's load-swap
gap, `predictions/2026-09-07-round6-backlog-screens.md`), which under M2 enters as a NEW candidate at rung
1 rather than as a mutation, and therefore counts as generation.

**⚠ WHAT HAPPENS IF THE BOARD IS EMPTY AT THE SEARCH STOP. Added 2026-09-07 by blind audit, because
nothing covered it and there are seven days left. A CONDITIONAL IS SUBMITTED. "Nothing survived" IS NOT
AN OPTION.**

The preliminary submission on 2026-09-27 is **explicitly unassessed** - a name and a paragraph. The
binding date is **2026-12-11**. **So the cost of submitting the best CONDITIONAL is approximately zero,
and the cost of submitting nothing is the entire competition.**

**At the search stop, and now for every candidate already alive, score each on the rubric below by the
ranking rule in Part 3; there are no verdict tiers.
Submit the top of that list.** Say plainly in `STATE.md` what is unresolved about it and what would have
to be true by December. **A concept whose weaknesses are named is a stronger December pitch than a
concept whose weaknesses were never looked for.**

**Then score every live candidate 1-5 on the room's own published rubric** (`STATE.md` -> THE ROOM), used
verbatim, because that is what is actually scored. The seven criteria, and what a 5 looks like:

| # | Criterion | A 5 |
|---|---|---|
| 1 | Clarity of target customer | You can name the person, their title, their company size, and how many exist |
| 2 | Clarity of JTBD | One sentence, in the customer's words, that a practitioner would recognise |
| 3 | **Significance and magnitude of unmet need** | **Two independent demand tiers, at least one of them D1, D2 or D3 (Part 2b), plus a salience answer from an operator** |
| 4 | Differentiation and uniqueness | Passed the gate on CAPABILITY, not on distribution |
| 5 | Performance improvement over existing solutions | A number you measured, not one you assumed. **And the improvement must COMPOUND - see stage 6: a service that is no better on day 400 scores flat here** |
| 6 | Size of market opportunity | A segment, sized from a countable source, not a customer |
| 7 | Market / technical / execution risk | See buildability below |

**Criterion 3 is scored on the demand ladder (Part 2b). The call is required only for the salience
half.** **[C-48]**, **[C-50]**

**Buildability, the founder-fit half of criterion 7:** can a demo exist by 2026-12-11 · what does the
COLD START look like, i.e. how are the first ten customers won while the asset is still empty · would you
want to work on this for six years. **[C-49]**

**Where the rubric and the room disagree, the founder's stated goal governs: the terminal goal is to build a
company, and the competition is instrumental.** **[C-49]** **The split (Part 3) calibrates what KILLS to
the room; what is worth six years is decided by the ranking's founder-fit half (criterion 7) and by Veer,
never by the kill list [C-72].**

---

## PART 9 - KEEPING THIS FILE HONEST

**Prune. A rule that has not decided a candidate - killed one, saved one, changed a formulation, or moved
its rank on the rubric - in
the last 10 screened candidates is reviewed for removal at the next method review.** Cut it or record
why it stays; its casebook entry survives either way as history.

**EXCEPTION: LANE-LEVEL RULES ARE REVIEWED ON LANES CLOSED, NOT ON CANDIDATES DECIDED.** Stage 0's test
1e' works by preventing candidates from being generated at all, so it will never appear in a per-candidate
kill roster. **Without this exception the pruning rule would delete the cheapest rule in the file for
doing its job perfectly.**

**⚠ AND THE COUNTERWEIGHT, ADDED 2026-09-07 AFTER A BLIND AUDIT. PRUNE BOTH WAYS.**

The rule above prunes rules that are INACTIVE. Nothing in this file has ever pruned a rule for being
**TOO HARSH**, and nothing can, because **a false negative is never observable**: a candidate killed
wrongly simply disappears and no one writes it down. `predictions/` scores whether a kill was PREDICTED.
It has never once scored whether a kill was CORRECT. **A calibration loop that can only tighten is not a
calibration loop, it is a direction.**

So, once per round: **take the candidate killed with the LEAST evidence and argue it back.** Write the
strongest available case that the kill was wrong, in `predictions/`, and record whether it changed the
verdict. **A screen that has never overturned one of its own kills has no false-negative rate, and
therefore no calibration.**

**⚠ THE RULE FREEZE. Applied 2026-09-07 (evening) [C-72].** Thirty-seven casebook entries were created or
sharpened in one day, sixteen standing kills rested on a single instance, and every candidate that ever
passed the gate generated the rule that killed it. **So, until the December final: no new kill. A finding
that looks like a rule goes to `predictions/` as a HYPOTHESIS and kills nothing this cycle. It may be
promoted to a SCORE check at a method review on two independent instances, and to a KILL only at a method review after 2026-12-11, on two independent instrument-verified instances and a room-winner rerun. Until
then the kill list is K0-K4.** Loosening is not tightening: this freeze is itself the younger rule that
reopened two candidates and voided fifty-nine old-ladder verdicts, and that is the intended direction. The
rules that rest on one instance or never decided a candidate (1f, the lane gate, the amnesty and free-appeal checks,
the standard-setter ledger, the buyer's guide, the licensing gate, the fee-shift, the liability floor, the
compelled publication, the once-per-customer pooling question) stay in this file as generator prompts and
SCORE questions. None of them kills.

**⚠ THE ROOM-WINNER TEST, and it is the calibration this file never had [C-72].** A prediction scorecard
that scores "did we predict DEAD" against a board that is always dead measures nothing. **The test that
measures something: run the ladder, blind, on last edition's winners as if they were candidates. Any rung
that kills a first-place winner is not a kill rung for this room.** Rerun whenever a rung is proposed for
promotion to K.

**Two runs on 2026-09-07 (evening), both OBSERVED by blind agents under the OLD text, after a fresh
evaluator (`predictions/2026-09-07-eval-split.md`) caught that the audit had only DERIVED them:**
- **PipeLine (1st):** DEAD at rung 3, GIVES + CAPTURES (Procore's free sub seat captures the drawing
  revision at source), **M0: NONE.** Under the split: NO KILL, fifteen scored weaknesses, and M0 found the
  narrowing to the failed-inspection slice that the old ladder's M0 could not. **Rung 3's demotion is
  observed.** `predictions/2026-09-07-roomwinner-pipeline.md`, `-screen-TC1.md`, `-screen-TC1-oldladder.md`.
- **Litmetrics (3rd):** DEAD at rung 4: Filevine's Lead Docket documents *"predicts... should be signed,
  referred out, or rejected"* on its own help center, paid and live, to PI firms. **The outcome-feedback
  half of the claim is unclaimed.** `predictions/2026-09-07-screen-PI1-oldladder.md`.

**What the two runs license, honestly.** Rung 3 and rung 4's "a competitor exists" practice are demoted on
observation. K3 came within one unclaimed half-claim of a room winner. **Resolved by Veer the same night: *"comp
should score not kill unless its actually already solved."* K3 now requires the outcome, not the claim;
Lead Docket's documented feature scores Litmetrics on criterion 4 and does not kill it, which matches
what the room did.** Rungs 1.5, 2, 2.5, 5, 6, G3, G4 and stage 6 were demoted on C-58's ratchet argument, not on the
test; the test never reached them because both winners died earlier.
