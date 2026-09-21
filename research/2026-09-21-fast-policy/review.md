# Independent review, fast-policy round, 2026-09-21

METHOD stage 3. One reviewer, no subagents. Files read: `METHOD.md`, `shortlist.md`, the three verify memos in this
folder, and the round-17 comparison candidate (C1 rows and paragraphs in `CANDIDATES-JEV.md`, plus
`screens/2026-09-20-round17-jev/gate-C1.md`).

Three web searches used, all spent on a single claim in `verify-yard-dispatch.md` I believed was wrong. Result in the
source-discipline section below. No other claim in the four documents looked wrong enough to spend a search on; the
decisive unknowns in all four are customer-behaviour questions that no amount of page-fetching answers.

---

## The question that governs all four

The founder brief says the technology premise is a non-generative calibrated-decision model that any competitor can
also buy, and that the founders start with no proprietary data and no customer access. That means the model is not the
asset. For every idea the real question is: after six months of operating, what do Veer and Cole hold that Extensiv,
McLeod, Johnson Controls or Descartes could not buy on the same terms the same afternoon?

There is exactly one honest answer available across all four ideas, and all four memos independently arrive at it: a
matched log of (state at decision time, decision taken, outcome that followed) for a specific customer's own work.
Nothing else in any of these four is a candidate asset. The load-tender memo states this plainly in its own closing
section. The peak-demand memo states it as the reason the durable edge "has to come from something other than we have
a better model". Round 17 states it in the premise paragraph of `CANDIDATES-JEV.md`.

That answer makes one property decisive and it is not market size, not the dollar per decision, and not competitor
absence. It is **whether the outcome label exists at all, arrives often enough, and is not systematically censored**.
An outcome log that never fills is not a moat, it is a subscription to someone else's API. I rank the four mostly on
that, and on a second property the round has not examined.

**The second property, and it cuts against three of the four.** The premise's stated edge over a general-purpose model
with the same JSON is speed (70 to 500 milliseconds) and near-zero cost at volume. Check the actual decision cadence
in each memo, using the memos' own evidence:

- Peak-demand: once per minute. The memo says so itself, and notes that the incumbent BAS already runs at that
  cadence, which "suggests latency may not be the binding constraint".
- Load tender: the response window is 15 minutes to 2 hours, and Best Buy's own implementation guide (fetched, quoted
  in the memo) allows 90 minutes.
- Yard and warehouse dispatch: task assignment happens on human and forklift timescales. No document in this round
  names a sub-second requirement.
- C1, the broker entry line check: a decision inside a keying workflow, on text already on the screen, while the entry
  writer is typing.

So on the round's own evidence, C1 is the only one of the four where the technology premise's headline property is
actually load-bearing. For the other three, a general-purpose model given the same JSON is a fair substitute on
latency, and at once-per-minute or once-per-tender volumes it is also cheap enough. The peak-demand memo reaches this
conclusion explicitly; the other two do not, and should have.

---

## 1. Yard and warehouse dispatch (small 3PL and yard operators)

**Strongest case.** The job is real, named and documented as a distinct problem across the industry, and one WMS built
for exactly this customer size ships alphanumeric-by-default pick-path ordering with manual override, which is a
hand-written rule of precisely the kind the concept targets. Task volume is high enough that per-decision inference
cost is genuinely negligible, so if a policy beats the rule at all, the economics of running it are not the obstacle.

**Strongest objection.** The memo's own evidence shows the integration is vendor-gatekept in both directions: SphereWMS
issues API keys only through its support team, and the fetch found no public endpoint for writing an assignment back
into the WMS, which is the entire product. Separately, the memo's claim that nothing competing exists is wrong: a
warehouse-orchestration category sells dynamic task assignment by skillset, proximity to work zone and current
workload to 3PLs today (AutoScheduler.ai, fetched 2026-09-21), and six searches did not surface it.

**Missing evidence or contradiction.** Both, and the contradiction is inside the memo rather than in the world. The
memo cites the same vendor (Extensiv) as evidence that the incumbent already ships dynamic task assignment and as
evidence that the incumbent's task ordering is static. Those are two different features: bin ordering within a pick
path is not assignment of work across workers. Only one of the two quotes reproduces on the cited page (see source
discipline below). The rest is missing evidence: no number anywhere, for or against, on policy versus rules at this
task and this scale.

**AI advantage given a commodity model.** Weak as formulated. The founders would hold a per-operator log of which
worker or vehicle was assigned what and what the wait and dwell times turned out to be. That log is real and it does
accumulate. But the WMS vendor already holds the same log by construction, at every customer, and controls the write
path the founders need. Building the asset requires the party who already owns a better version of it to let you in.

**Verdict: PARK.**

Not a drop, because I cannot trust the negative finding either. The memo's competitive sweep missed a live category in
one search, so its "nothing found competing" is not evidence the space is open, and its keystone support quote does not
reproduce. There is nothing solid enough under this idea to test against yet. Unpark it only after a corrected
verification pass, and only for a formulation that changes who the customer is: the plausible shape is selling the
policy layer to the WMS or YMS vendor as a component, not to the operator across a gatekept API. That is a different
company with a different sales motion, and it should be generated and verified as such rather than smuggled in as a
narrowing.

**Concrete first test if it is unparked.** One small 3PL or yard operator already running Extensiv, Logiwa, SphereWMS,
YardView or GoRamp. Real recent case: one already-logged shift of task assignments and the wait, dwell and throughput
figures their system already recorded, so nothing new has to be instrumented. Existing alternative: the rule or
supervisor call that produced those assignments. Proposed improvement: a calibrated per-task assignment from the same
state. What changes the decision: if the counterfactual assignment would have measurably cut wait or dwell on that
real logged data, and the operator can name who inside the building would be allowed to authorise a write back into
the WMS, pursue it. If the counterfactual matches the rule, or the operator says only the WMS vendor can authorise a
write, stop.

**What would change my mind.** A named WMS or YMS vendor with a public, self-serve write path for task assignment, or
one operator who can point at the person in their building who would sign off on an outside system moving work.

---

## 2. Load tender accept and reject, plus driver assignment (carriers with 1 to 20 trucks)

**Strongest case.** The decision is forced, timed and priced: a tender auto-revokes to the next carrier in the routing
guide if unanswered inside the shipper's window (Best Buy's own guide requires 90 minutes), and the outcome of each
accepted load, margin, detention, on-time, resolves within days. That combination, a decision the customer must make
on a clock and an outcome that lands soon after on the same record, is the cleanest cold start for an outcome log in
this round.

**Strongest objection.** The memo's own closing section concedes the point: no durable technical edge was found, and
McLeod, Truckstop, Samsara and Motive already sit inside the tender flow of every carrier who runs any software at all
and can buy the same model. Worse, the failure mode is asymmetric and silent: an accepted load that blows an
hours-of-service limit or misses an appointment is a bigger loss than the status quo of a dispatcher saying no when
unsure, which is exactly the behaviour a probability number has to displace.

**Missing evidence or contradiction.** Missing evidence, cleanly. Nothing checked contradicts the premise. What is
absent is the one fact that decides it: whether the dispatcher's actual reasoning reduces to a small number of legible
factors that fit in JSON (rate per mile against a personal floor, deadhead, hours remaining, known-bad broker or lane)
or whether it is dominated by relationship knowledge that never becomes structured state.

**AI advantage given a commodity model.** Thin now, but with the clearest path of the four. Day one the founders hold
nothing an incumbent could not buy. What they could hold after a few months is a per-carrier calibration on that
carrier's own realised margins, detention history and broker behaviour, which is genuinely not in any incumbent's
generic prior. The honest counterweight is that an incumbent sitting inside the tender pipe can start building the
same log the day it decides to, from more carriers at once. The founders' advantage is time and focus, not exclusivity.

**Verdict: TEST NEXT.**

Not because the case is strong, it is not. Because the test is one week of shadowing, requires no build, no access
grant and no spend, and its answer transfers to the rest of the lane: it is the first real measurement of whether a
practitioner's decision reduces to typed state at all, which is the assumption under every idea in this round.

**Concrete first test.** One owner-operator or small-fleet dispatcher who currently self-dispatches or pays a
percentage-based dispatch service (published rates run 4 to 7 percent of gross on one dispatcher's own pricing page,
which is a real recurring alternative cost, not a hypothetical). Real recent case: the next 10 to 15 tenders that
actually arrive in one week. Record for each how it arrived, minutes available to answer, the dispatcher's own
reasoning in their own words at the time, and the realised outcome. Existing alternative: that dispatcher's judgment,
or the percentage dispatch service. Proposed improvement: a calibrated accept-or-reject and driver match from the same
tender text and self-reported state. What changes the decision: if the reasoning is dominated by a handful of legible
factors and the dispatcher says they would have wanted a fast second opinion on some of those calls, continue. If it
turns on relationship knowledge, or the dispatcher says they will not act on a number whose reasoning they cannot see,
drop or re-scope before building.

**What would change my mind.** A carrier who has a documented recent loss they can attribute to one bad accept or
reject decision, and who will hand over their tender history to see whether the pattern was predictable. Against:
evidence that the ELD integration cannot be authorised by the owner-operator alone.

---

## 3. Peak-demand load policy for single commercial buildings

**Strongest case.** The dollar is real, itemised and structurally shaped exactly like the product: one published tariff
(fetched) sets the monthly demand charge from the single highest 15-minute interval, and a ratchet clause can hold an
elevated floor for up to eleven further months, so one bad interval is taxed long after it happens. Buildings in the
target class have no energy manager to watch for it.

**Strongest objection.** The premise is contradicted by a fetched primary vendor document. The concept's stated status
quo, that these buildings use a fixed kW threshold, is not what the incumbent BAS does: Johnson Controls Metasys
demand limiting runs once per minute, projects consumption forward for the demand interval using an
exponential-smoothing error model with a 95 percent confidence bound, computes the required correction and sheds
prioritised loads pre-emptively. That is the proposed mechanism, shipping, on hardware the building already owns, from
a vendor who can buy the same model at the same price.

**Missing evidence or contradiction.** Contradiction, and it is the strongest checked fact in the entire round. This is
not competitor presence, which METHOD correctly refuses to treat as a kill. It is the concept's own description of the
alternative being false.

**AI advantage given a commodity model.** None identified. The only asset would be a per-building history of which
shed decisions avoided a peak, and the BAS vendor already holds the telemetry that produces it. The memo's second
objection is also correct and underrated: replacing a deterministic, safety-bounded shed algorithm with a probabilistic
trigger creates a new tuning decision (what probability fires a shed) for an owner who by definition has nobody to tune
it. That is a new failure surface sold as a removed one.

**Verdict: DROP THIS FORMULATION.**

The obvious re-scope, and the memo names it, is to sell activation and commissioning of demand-limiting features that
buildings already own but never turned on. That may well be a real business. It is a controls-commissioning services
business in which AI is incidental, so under the founder brief it is out of scope as that reformulation, and the brief
is explicit that an AI layer should not be invented to rescue it. Say that plainly rather than carrying the idea
forward in a shape the brief excludes.

**Concrete first test, only if someone wants to contest the drop.** One facilities manager or owner at a standalone
grocery, school, church or small manufacturer on a demand-metered tariff with no energy manager. Real recent case:
their last twelve demand-charge lines and whichever intervals set them. Existing alternative: whatever controls they
have, and whether a contractor ever configured or mentioned demand limiting. Proposed improvement: a calibrated
per-minute decision replacing or activating that. What changes the decision: if most buildings in this class turn out
to have no digital control surface capable of running demand limiting at all, the opening is real but it is a hardware
and commissioning opening, which is a different company. If they have it and it is off, that is a services business.
Neither outcome revives the idea as formulated.

**What would change my mind.** A measured comparison, from anyone, showing a calibrated multi-signal forecast beating
the linear projection already embedded in commissioned BAS demand limiting, in dollars, on this building class. The
memo looked and found nothing on either side.

---

## 4. C1, broker-side HTS entry line check (customs brokerages under 300 staff)

**Strongest case.** It is the only one of the four where the technology premise is actually load-bearing: a decision
made inside a keying workflow, in under a second, on text already on the entry writer's screen, in a seat that is
funded and named, for a buyer the statute binds personally. And unlike the other three, the founders do not need a
write path into anyone else's system to be useful; the output goes to the human who is already typing.

**Strongest objection.** The moat theory and the open question are the same question, and the gate could not answer it.
The only defensible asset in this entire premise is an outcome log, here a log of CBP redeterminations calibrated to
one broker's own history. The gate's own closing paragraph flags that most entries liquidate without a CF-28 or CF-29
ever issuing, which would make the label sparse and right-censored on the branch that matters. If that is true, the
asset does not accumulate and the product is a classification tool competing with vendors who already ship one.

**Missing evidence or contradiction.** Missing evidence today, with a live contradiction risk. If the label base rate
turns out to be near zero, that is not a weak spot, it defeats the moat mechanism the round chose C1 for. It should be
treated as a potential kill, not as a scored weakness on a criterion.

**AI advantage given a commodity model.** The most substantial of the four, conditional on the label existing. What the
founders would hold is a per-broker ledger of proposed codes, filed codes and subsequent CBP outcomes. The gate checked
four vendors and found none ingesting a customer's own post-entry outcome stream, and correctly identified this as a
capability gap requiring a new pipeline rather than a pricing tier someone could flip on. Note the limit, which the
gate observes and `CANDIDATES-JEV.md` then partly loses: nobody claiming to do it is not evidence that it is worth
doing, and the gate itself raises the alternative explanation, that the data may be too sparse to calibrate against.
METHOD is explicit that no competitor found is not proof of an opening, and that is the weight this finding is
currently carrying.

**Verdict: TEST NEXT.**

**Concrete first test.** One licensed customs broker or entry writer at an independent brokerage, findable on LinkedIn
in Indiana or Chicago. Real recent case: the lines they filed last month, and any CF-28, CF-29 or import-specialist
flag that came back. Existing alternative: their own experience plus the free CROSS rulings database, which searches
precedent by keyword and returns no probability for a proposed code. Proposed improvement: a per-line acceptance
probability calibrated against that brokerage's own history of redeterminations. What changes the decision: if the
broker can name a rate of challenged lines that is more than negligible, and can say how and when they learn of it,
the label exists and the idea earns a build conversation. If they say challenges are rare, arrive a year later, or
arrive in a form nobody records, the outcome ledger cannot fill and the idea should be dropped rather than parked,
because the same defect will apply to every variant of it.

**What would change my mind.** Either direction, from the same conversation. Also: a vendor page showing calibration
against a customer's own audit outcomes would remove the capability gap the round's case rests on.

---

## Ranking for the founders' first conversation

**C1, the broker entry line check, goes first.** It is the only idea in the round where the premise's speed property is
actually required by the workflow, the buyer is a named licensed individual with personal statutory exposure rather
than a diffuse budget, and the founders need no integration to be useful on day one. Decisive for the ordering: its
single open question is answerable in one short conversation with one findable person, and the answer is binary and
consequential either way. If the label is sparse, that finding does not only kill C1, it undermines the outcome-log
moat theory under every candidate in this lane, which makes it the highest information per minute available anywhere on
this board.

**Load tender second.** The test is nearly as cheap, needs no access grant, and measures the other assumption under
the whole lane: whether a practitioner's real reasoning reduces to typed state. It ranks below C1 only because it takes
a week of shadowing rather than a phone call, and because the incumbents sitting inside the tender flow start with the
distribution the founders would spend years acquiring.

**Yard and warehouse dispatch third.** The idea may be fine; the evidence under it currently is not, and the write path
the product depends on is not confirmed to exist on any named product. Talking to an operator before the verification
is corrected risks spending a first conversation on a formulation that a single vendor-page fetch could have retired.

**Peak-demand last, and not as a conversation.** The incumbent already ships the proposed mechanism at the proposed
cadence on hardware the customer owns, documented in the vendor's own technical bulletin. The version that survives
that fact is a commissioning services business the founder brief excludes. Its value to this round is that it is the
one idea where the desk research actually decided something, which is worth more than three inconclusive maybes.

Two of four earn a next test. That is a normal result, and it is acceptable that none is ready to build.

---

## Source discipline: vendor claims and search summaries presented as fact

All four documents label their sources, and three of them do it carefully. These are the places where the labelling
slipped or where a label did not hold up.

**`verify-yard-dispatch.md`, most serious.** The memo's opening support quote, "This dynamic task assignment helps
reduce unproductive idle time and can help lower overtime hours", is attributed to the Extensiv blog page and listed
under VERIFIED, primary source fetched, operative words quoted directly. I fetched that page on 2026-09-21 and the
phrase "dynamic task assignment" does not appear anywhere on it; the page covers directed picking, mobile scanning,
verification checkpoints and picking methods. A search for the sentence returns the concept from other vendors, not
from Extensiv. Either the page changed within the day or the quote is misattributed. Either way the memo's stated
interpretation, that Extensiv describes its own task assignment as a live gap, does not currently stand, and it is the
first fact the memo offers.

**`verify-yard-dispatch.md`, second.** "Nothing found (in six searches) constitutes a competing product doing this
today" is presented as a searched finding with the correct caveat that absence is not an opening. The finding itself is
wrong. Warehouse orchestration vendors sell dynamic task assignment by skillset, proximity to work zone and current
workload to 3PLs, including forecasting labour needs from history (AutoScheduler.ai, fetched 2026-09-21). One search
found it. A negative competitive finding that a single search overturns should not be carried as support.

**`verify-yard-dispatch.md`, third.** The budget-owner argument, which is one of the memo's three objections, rests
entirely on cost ranges (5,000 to 50,000 dollars implementation, 1,000 to 15,000 pounds or up to 50,000 dollars per API
connection, 5 to 10 hours per week of champion time) that the memo itself lists as NOT VERIFIED search summaries from
inventory and blockchain-consultancy blogs. The memo flags them honestly and then reasons from them anyway. An argument
is not more verified than its inputs.

**`verify-load-tender.md`.** The section header says "The money per decision is real and published" and the paragraph
ends with "roughly a 1,000 to 1,200 dollar gross-revenue swing". The published part is the per-mile linehaul average
from DAT, correctly fetched and quoted. The swing is the memo's own arithmetic, and it measures the wrong quantity: a
rejected tender does not forfeit a load's gross revenue, it forfeits the difference between that load and the next-best
load the truck takes instead, which is a much smaller and unstated number. The stake is real; this is not the size of
it. Also, the "3 to 329 seconds versus 70 to 500 milliseconds" comparison is a vendor-run benchmark reported by a
trade outlet. The memo flags the general-model side as inference, which is right, and then still uses the range as a
comparison figure.

**`verify-peak-demand.md`, best of the set, with one citation defect.** It repeatedly refuses to generalise (do not
apply this tariff's dollar figure elsewhere; do not rely on the 30 to 50 percent of the bill figure), correctly marks
the Schneider page as unverified after a 403 and the Green Button description as an aggregator summary rather than the
utility's own page, and it damages its own idea with a primary source, which is the behaviour METHOD asks for. The
defect: the text cites Rate Schedule 231 as effective 1 January 2026 under Resolution No. 6743, while the supporting
URL is a May 2026 service-regulations update under Resolution 6767. The one verified dollar in the memo rests on a
citation that does not identify its own document consistently. Re-pull the exact rate sheet before anyone quotes the
figure outside this repository.

**`gate-C1.md`.** Disciplined on vendor quotes: it fetched each vendor page itself and says explicitly that it did not
rely on the screen's paraphrases. Two lesser flags. The CROSS description is a search-index summary, used because the
site is client-rendered and returned no body, and the gate says so. The Reasonable Care publication is characterised
as a checklist although the linked PDF returned 404 on the attempt, so its content is inferred from the landing page.
The larger flag is structural rather than a mislabelled source: the gate's ALIVE verdict is an absence finding across
four vendor pages, and the gate itself states that G1 failing makes the rest moot. By the time it reaches
`CANDIDATES-JEV.md` this has become "the gate found a genuine capability gap", which is a stronger claim than four
fetched pages support, and the gate's own alternative explanation, that the data may be too sparse to calibrate
against, is the one that should travel with it.

**One pattern worth naming across the round.** Three of the four documents treat "no vendor claims this" as support.
METHOD already rules on that: no competitor found is not proof of an opening. In this round the rule earned itself,
because the one negative competitive finding I spent searches on did not survive the first search.
