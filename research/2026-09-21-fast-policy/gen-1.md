# gen-1: fast policy from state, and acting before asked

Six hypotheses, generated 2026-09-21. Nothing here is validated. No customer has been
spoken to, no number below is a measurement, and every "why it might be better" is a guess
that has to be knocked down before it is worth building.

Technology premise for all six: a model that takes program state as text or JSON plus typed
questions and returns only calibrated probabilities (yes/no, one of up to 255 labelled
options with per-option probabilities, or a score on a 2 to 10 level rubric), all questions
answered in one pass in 70 to 500 ms, zero-shot from a schema, at $0.042 per million input
tokens. It does not reason, generate or see. So every idea has to be a *decision* someone
makes over and over from state they already have in a database, where a rule or a person is
doing the deciding today, and where the result shows up fast enough to grade the decision.

The common shape: read state that already exists, answer a small fixed set of typed
questions every few seconds, act, then log the outcome and compare it back to the
probability that was emitted. That last part is the product. A rules engine cannot tell you
it was wrong.

---

## 1. Kitchen-paced order admission for independent restaurants (hospitality)

**Customer and outcome.** An owner-operator restaurant doing 60 to 200 delivery and pickup
orders a night on a POS like Toast, with DoorDash and Uber Eats firing into the same kitchen.
What they want is for the food to be ready when the driver arrives, and for the promised
quote time to be true. Today the choices are a manual quote time, a fixed throttle, or
"snooze the channel for 20 minutes" when the expo screen gets ugly. All three are blunt: the
pause is all-or-nothing and someone has to notice.

**Approach.** Sit next to the POS and the delivery integrations. Every few seconds, read the
open-ticket state and decide two things: what quote time to publish on the next order, and
whether to hold the next incoming order for a short window instead of firing it.

**Model role.** Two question shapes, one pass. A rubric score for "minutes until this ticket
mix clears" (bucketed, say 8 levels from under 6 minutes to over 40). A yes/no for "hold the
next third-party order for 3 minutes". State it reads: open tickets with items and
timestamps, items by station, which stations are staffed right now, current hour and day,
weather flag, and the last 30 minutes of ticket completion times. It never writes the menu
or talks to a guest, it only sets a number and a gate.

**Why it might be better.** The heuristic in the POS is a single global setting. The real
constraint is per-station and moves minute to minute: six pizzas and one salad is a very
different kitchen than seven salads. A probability per ticket, recomputed continuously, can
express "80 percent chance this clears in 12 minutes" where a rule can only express a
constant.

**Biggest uncertainty.** Whether the POS ticket JSON carries enough signal without knowing
who is actually on the line. Staffing is the dominant variable and it is often not in any
system. If the owner has to type in "Marco is on saute tonight", the whole thing dies.

**Graded by.** Actual ticket completion time, observed 5 to 40 minutes later, straight off
the POS. Quote error in minutes per order, and driver wait time where the delivery platform
exposes it. Thousands of graded decisions a week per restaurant.

---

## 2. Same-day chair recovery for single-location dental and specialty clinics (healthcare ops)

**Customer and outcome.** A two-to-four chair dental practice or a solo dermatology or
physical therapy clinic. An empty chair is pure lost revenue and they know it. They want
tomorrow's schedule to actually fill, and today's gap to be filled by someone from the
waitlist before it becomes an idle hour. The front desk does this by feel and by calling down
a list in order.

**Approach.** Read the practice management system nightly and continuously through the day.
Two decisions: which of tomorrow's appointments are likely enough to no-show that the slot
should be double-booked or pre-empted, and when a cancellation lands, which waitlist patient
to call first.

**Model role.** Yes/no with a probability for "this patient does not show". The labelled-
options shape for the call-down: given the open slot, rank the waitlist (up to 255 patients)
by probability of accepting and attending. State: appointment type and length, lead time
since booking, prior attendance history, insurance type, distance bucket, time of day, day of
week, whether a reminder was confirmed, weather. All of it already sits in the PMS.

**Why it might be better.** No-show models exist but are sold to hospital systems with data
teams. A single-location practice has no one to build one, and the alternative is a flat
overbooking rule that is either too timid or creates a waiting room. Zero-shot from a schema
matters here because a two-chair practice has a few thousand historical appointments, not
enough to train anything.

**Biggest uncertainty.** Calibration on a small, idiosyncratic patient population is exactly
what is unproven, and the cost of a miss is asymmetric and visible: an overbooked patient
waiting 40 minutes is a bad review. Also PMS integration is a real moat and a real wall,
Dentrix and Eaglesoft are not friendly.

**Graded by.** Showed or did not show, observed the same day. Chair idle minutes per day.
Waitlist call accept rate, observed within minutes of the call. Roughly 20 to 60 graded
decisions a day per clinic, which is slow but every one is labelled cleanly.

---

## 3. Load tender accept/reject for small trucking carriers (freight)

**Customer and outcome.** A carrier running 5 to 40 trucks, receiving load tenders from
brokers by email, EDI and load board all day. The dispatcher decides in seconds whether to
take a load at the offered rate and which driver to put on it. The outcome they want is more
loaded miles at a good rate, fewer empty repositioning miles, and drivers who hit their hours
without sitting in detention.

**Approach.** Sit on the tender feed and the TMS. For every incoming tender, answer a small
set of typed questions in under half a second, before the load is gone, and surface a ranked
accept/decline with a reason code the dispatcher can override.

**Model role.** Yes/no for "accept this tender". A rubric score for "on-time delivery
likelihood" and another for "detention risk at this shipper". Labelled options for "which
driver". State: origin and destination, pickup window, rate per mile, commodity, current
positions and remaining hours of every driver, the next known load in each lane, historical
detention at that facility, lane balance for the week. All structured, all in the TMS or the
tender itself.

**Why it might be better.** Small carriers use a rate-per-mile floor and a dispatcher's
memory of which shippers are terrible. That floor cannot price the option value of ending the
day in a good market, and memory does not scale past the dispatcher. Latency is a genuine
edge here: tenders on a board are first-come.

**Biggest uncertainty.** Whether two students can get access to a carrier's TMS and tender
feed at all, and whether the model beats an experienced dispatcher, who is genuinely good at
this. Also: the ranked-driver decision touches how much a driver earns, which is political.

**Graded by.** Whether the load was won, observed in minutes. Detention hours and on-time
delivery, observed in hours. Revenue per truck per week and deadhead percentage, observed
weekly. Dozens to hundreds of graded decisions a day.

---

## 4. Next-action anticipation for small B2B support desks (software operations)

**Customer and outcome.** A 3 to 15 person support team at a B2B software company, on
Zendesk, Intercom or Front. The outcome is lower time-to-first-meaningful-response and fewer
tickets that bounce between people. This is the anticipation half of the urn: predict what
the agent will need and have it there before they ask.

**Approach.** As a ticket arrives and as the conversation updates, decide what to pre-fetch
and pre-stage: which internal account records to pull, which of the team's runbooks or macros
is the right one, which agent it should route to, and whether it needs escalation now rather
than after the first reply. The point is that pre-fetching is cheap and wrong guesses cost
almost nothing, so a calibrated probability is enough to justify doing the work speculatively.

**Model role.** Labelled options for "which runbook or macro" (a team has tens to low
hundreds, well within 255) and for "which agent or queue". Yes/no for "this will escalate"
and "this needs the billing record pulled". State: the ticket text, customer plan and tenure,
recent error rates or incident flags for that account, open tickets from the same customer,
time since last deploy, and which agents are online. Note the ticket text is input only, the
model does not write the reply.

**Why it might be better.** Trigger-based routing in these tools is literally keyword rules
that someone wrote once and never maintained. And a generative assistant here costs orders of
magnitude more per call and cannot be run on every state change. At this price, running the
questions on every keystroke-level update is affordable, which is what makes anticipation
rather than classification possible.

**Biggest uncertainty.** Whether pre-staging actually saves an agent enough time to pay for
the product, or whether it is a nice-to-have on top of a workflow that is already fast. Also
the risk that the real buyer wants the generative thing that drafts the reply, and this looks
like a worse version of a product they already evaluated.

**Graded by.** Did the agent use the staged runbook, observed within minutes. Was the ticket
reassigned after routing, observed within minutes. Time to first meaningful response and
resolution time, observed in hours. Hundreds of graded decisions a day even on a small desk.

---

## 5. Officer dispatch for small-city and campus parking enforcement (public sector)

**Customer and outcome.** A parking authority or campus operation with 3 to 12 enforcement
officers and no analytics staff, running payment through an app like Passport or ParkMobile
plus meters. The outcome is compliance and revenue per officer hour, and, in the version that
sells politically, fewer wasted patrol loops. Today officers walk a fixed beat rotation.

**Approach.** Read payment state continuously, which is entirely structured: which spaces
have a paid session, when each expires, historical violation density by block and hour. Every
few minutes, tell each officer which block to walk next.

**Model role.** Labelled options for "which zone or block segment next" from a list of up to
255. A rubric score for "expected violations per officer-minute on this block in the next 20
minutes". Yes/no for "this block is not worth a pass right now". State: expired and expiring
sessions by space, time of day, day of week, event calendar for nearby venues, weather,
officer position and last visit time per block. No cameras, no plate reading, which keeps it
inside the scope and out of the worst of the privacy fight.

**Why it might be better.** A rotation is a rule that ignores today. Expiry state is already
known to the minute and is currently used for nothing except the officer's handheld when they
happen to be standing there. The decision also has a natural cooldown, you do not re-walk a
block you just cleared, which a probability handles and a static route does not.

**Biggest uncertainty.** Whether a public agency will buy anything from two students on a
timeline shorter than a year, and whether "make enforcement more efficient" is a sale anyone
wants to be seen making. A campus or a private lot operator is probably the wedge, not a city.
There is also a real question of whether the venture wants this politically.

**Graded by.** Citations or warnings written per officer hour, observed within the hour.
Whether the predicted violation was actually there when the officer arrived, observed in
minutes, which is a clean label. Compliance rate by block over weeks.

---

## 6. Peak-demand load policy for single commercial buildings (energy)

**Customer and outcome.** An owner or operator of one or a few commercial buildings: a small
manufacturer, a grocery, a gym, a multi-tenant office. A large share of their electricity bill
is the demand charge, set by the single highest 15-minute interval in the month. They want
that peak lower without anyone noticing a temperature change. Today this is a schedule
someone wrote, plus a manual scramble when a monitoring dashboard turns red.

**Approach.** Read the interval meter and the building automation system every minute or two.
Decide which flexible loads to defer or soften for the rest of the current 15-minute window:
HVAC setpoint drift, which rooftop units to stagger, water heating, EV chargers, non-critical
process equipment.

**Model role.** Yes/no per controllable load, several loads in one pass, for "defer this load
for the remainder of this interval". A rubric score for "probability this interval sets a new
monthly peak". State: the running kW for the current interval, minutes elapsed in it, zone
temperatures and setpoints, outside temperature and forecast, occupancy from the booking or
badge system, the month's peak so far, and the tariff. All JSON, all slow, all text. Setpoints
change every few minutes, nowhere near actuator speed, which keeps it inside the scope.

**Why it might be better.** The rule is a fixed kW threshold that trips too late or too often,
because the right threshold depends on how much of the interval is left and how much thermal
slack the building has. A calibrated "this interval will set the peak" every 60 seconds is a
strictly richer signal than a threshold, and the price makes per-building, per-minute
inference cost nothing.

**Biggest uncertainty.** Writing to a BAS is a commissioning and liability problem well beyond
two students on day one, so the first version is probably advisory: tell the operator what to
do and measure whether it helps. That may be too weak to sell. And a miss here is a
comfort complaint from a tenant, which is loud.

**Graded by.** The kW peak of each 15-minute interval, observed at the end of that interval,
so roughly 96 cleanly graded decisions per building per day. Zone temperature deviation from
setpoint, observed continuously. Monthly demand charge, observed on the bill.

---

## Cross-cutting notes

Every one of these assumes a customer will connect a system of record to two students. That
is the same risk six times and it is probably the binding constraint, not the technology.

The thing worth checking early, across all six: whether calibration holds on small, weird,
single-site data. The whole pitch is that a business with 2,000 historical events gets a
useful probability with no training. If that is false, only the highest-volume ideas here
(1, 4, 6) survive, because they are the ones that could accumulate their own feedback fast
enough to correct a badly calibrated prior.

Two of these (1 and 6) were sanity-checked only to the extent of confirming the workflow
exists and is rule-driven today. Nothing about competitors, market size or willingness to pay
has been looked at.
