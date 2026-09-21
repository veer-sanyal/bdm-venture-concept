# Fast-policy urn, 2026-09-21: merge and shortlist (active METHOD, stage 1)

Two generators (one strong, one balanced), six ideas each, same brief and urn, no dead lists loaded. Files: `gen-1.md`, `gen-2.md`. The yard/warehouse dispatch concept was the main session's own bet, sent to verification in parallel (`verify-yard-dispatch.md`).

## Merged by customer, job and mechanism

| Idea | Generators | Archive overlap | Decision | Reason, in words |
|---|---|---|---|---|
| Peak-demand load policy for single commercial buildings (per-interval "will this set the month's peak", defer flexible loads) | 1 | none found | **Verify** | The demand charge is a large, itemised, monthly dollar set by one 15-minute interval; the label is observed every interval; small buildings have no energy engineer; actuation is slow and via existing controls |
| Load tender accept/reject and driver assignment for small carriers | 1 | none found (raised in chat 9/20, never researched) | **Verify** | Purest latency case (tenders expire in minutes), outcome priced per load within days, and the smallest carriers have no TMS at all |
| Kitchen-paced order admission for independent restaurants | 1 and 2 | none | Park | Both generators converged, which says more about the generator than the market. The POS vendor holds the live state and already ships rule-based quote-time throttling; the dollar per restaurant is small. Revisit only if a POS partner program makes the state reachable |
| Same-day chair recovery / no-show-aware overbooking for single-location clinics | 1 and 2 | none | Park | No-show prediction is widely sold inside practice-management software; the advantage would be the waitlist call-down policy, which needs the scheduler's state |
| Same-day admission and technician assignment for small field-service shops | 2 | none | Park | The two dominant field-service platforms own the dispatch board and the state |
| Ticket triage and escalation-before-breach for small MSPs | 2 | MSP tier-1 helpdesk dropped in archive (market pricing) | Drop this formulation | Helpdesk platforms already predict SLA breach; the archived finding on pricing stands unless new evidence arrives |
| Pick-wave release and order batching for a small 3PL | 2 | folds into the yard/warehouse dispatch verification | Folded | Same customer, same system, same label |
| Next-action anticipation for small B2B support desks | 1 | none | Park | A feature of the helpdesk product, not a company, until shown otherwise |
| Officer dispatch for small-city and campus parking enforcement | 1 | none | Park | Public-sector sales cycle; small dollar; interesting label |
| Dynamic admission and pricing for a single self-storage or event-parking facility | 2 | none | Park | Revenue management exists at the chains; single-site operators are a real gap but the decision is hourly, not sub-second, so the premise adds little |

Tradeoff stated plainly: the two verified are the two where the dollar per decision is largest and the label arrives fastest. The parked ones are not failed; several would be worth a look if access to the state (POS, scheduler, dispatch board) turned out to be easy.
