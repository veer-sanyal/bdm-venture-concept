I'd pass. The strongest version is a real product, but the claim it's sold on, the 15% cap, almost never gets applied in practice. The parts that stay useful are either already offered or capped by California's size.

## What checks out and what doesn't
- **Notice volume: confirmed.** 10,098 PAGA notices were filed in calendar 2025, a record. The state agency counted 8,846 in fiscal 2024–25, and five law firms filed about 24% of them ([Nat Law Review](https://natlawreview.com/article/lwda-theres-new-sheriff-town)).
- **$2.2B: confirmed, but it overstates the PAGA share.** The CABIA tracker (an employer group) counts 2,352 settlements in 2025 totalling $2.16B, averaging $918K, with $725M going to attorneys ([CABIA](https://cabia.org/research-data/paga-summary/)). Most of that money is class-action wage recovery settled alongside PAGA, not PAGA penalties. The 15% cap only reduces the PAGA penalty part. I could not find a published figure for how big that part usually is.
- **15% cap: accurate, but conditional and rarely used.** Labor Code §2699(g) requires "all reasonable steps" toward compliance with **all provisions named in the notice**. Courts judge that on the "totality of the circumstances," and a payroll audit is only one example of a reasonable step ([statute](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=2699)). One defense firm reviewed 652 settlements from June to August 2026. Only 20 mentioned the cap and 5 built it into the settlement math, which is not the same as a court applying it ([CELR](https://www.californiaemploymentlawreport.com/2026/09/five-settlements-five-lessons-what-augusts-california-wage-and-hour-resolutions-tell-employers/)). Courts can already cut penalties on their own: one appeals court upheld a 99% cut to a $56M demand ([WGA](https://www.wga.com/news/court-affirms-99-reduction-in-56-million-paga-penalty-demand/)).
- **The record-keeping promise has a built-in conflict.** An audit done without a lawyer directing it can be demanded by the other side in a lawsuit. It is also unsettled whether an employer must give up attorney-client privilege to use an audit as proof of reasonable steps ([Shaw Law](https://shawlawgroup.com/2025/04/employer-reasonable-steps-under-paga/), [LCW](https://www.lcwlegal.com/news/taking-reasonable-steps-to-protect-against-paga-claims-and-penalties-in-the-new-year/)). A system that compares every shift with health-record logins creates a dated record of unpaid work. Any flag left unpaid becomes the plaintiff's proof that the employer knew.

## Who else serves this customer
- **ePeople.ai:** software built for California nursing homes by former nursing-home operators. It watches meal breaks in real time, pays premiums automatically, and advertises "audit-ready proof." It works as either a full replacement or a layer on existing systems ([site](https://epeople.ai/)).
- **SmartLinx:** workforce software built for senior care, covering scheduling, timekeeping and payroll. It applies break and meal rules automatically and produces audit-ready reports ([SmartLinx](https://www.smartlinx.com/why-smartlinx/intelligent-compliance/)).
- **Scaled Comp:** checks 100% of shifts for meal, rest and wage-statement violations, offers monthly runs, and builds a "dated reasonable-steps record." It also sells settlement data to defense lawyers. Audits cost $5K–15K. It is not healthcare-specific and does not use health-record data ([site](https://www.scaledcomp.com/)).
- **UKG, ADP and similar:** their timekeeping systems already produce pre-payroll exception reports for missed or late meals.
- **Defense firms:** Ogletree and Fisher Phillips sell reasonable-steps audits themselves, so they are a channel that could also compete.
- None of these matches the pitch closely enough to count as the same team. Checking health-record logins against punches and classifying pay codes for overtime are not offered by any of them.

**Does an incumbent own the data or the channel?**
- **Data: yes.** Punches and pay codes sit in UKG, ADP or SmartLinx. In nursing homes, PointClickCare holds the health records and the login logs. Each of these can limit access.
- **Channel: nobody owns it outright.** Defense lawyers are where trust lives, and nursing homes already have a workforce-software budget, which SmartLinx and ePeople are going after.

## 1. The strongest version
Stop selling "15% cap insurance" and sell pay accuracy before payroll closes, delivered as a monitoring program run under a defense lawyer's direction to protect privilege.
- **Customer:** multi-site California post-acute operators running nursing homes and home-health agencies, starting with the ones that already use a defense firm. California has 1,224 nursing homes and about 145,000 nursing-home workers ([UC Berkeley Labor Center](https://laborcenter.berkeley.edu/demographic-and-job-characteristics-of-californias-skilled-nursing-facilities-workforce)).
- **Scope:** fix the underlying wages, which counts for more than the cap because it reduces both the class-action wages and the PAGA penalties. That means:
  - paying meal and rest premiums at the correct overtime rate, including shift differentials and bonuses;
  - California's separate healthcare minimum wage tiers under SB 525 ($23/hr for nursing homes from June 2026);
  - per-visit pay for home-health clinicians, where Labor Code §226.2 requires separate pay for rest breaks and non-visit time plus separate wage-statement lines ([§226.2](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=226.2)). This is a harder calculation that the general timekeeping vendors don't handle.
- **Off-the-clock flags:** send each flag to a supervisor who confirms it and either pays it or corrects it. Every flag must be resolved, never left sitting in a file.
- **Positioning:** a layer on top of the existing timekeeping system, not a replacement.

## 2. Ratings
| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | A record 10,098 notices in 2025, and $2.16B paid across 2,352 settlements. |
| Value over today | 2 | Premium calculation and full-shift audits already exist (UKG, SmartLinx, ePeople, Scaled Comp), and the cap was built into only 5 of 652 recent settlements. Checking against health-record logins is the one real gap. |
| Market size | 2 | PAGA exists only in California. About 145K nursing-home workers plus home health comes to roughly 300K employees; at about $5 per employee per month that is under $20M a year for the starting market. |
| Risk (5 = low) | 2 | Depends on PointClickCare and UKG for data, the privilege and discovery conflict, one state's law that keeps changing, and thin-margin Medi-Cal buyers. |

## 3. What kills it, and the fastest test
**What kills it:**
- The premiums and off-the-clock wages the product finds are an immediate payroll cost to the employer. Nursing homes that miss breaks because they are short-staffed may prefer not to know.
- The defense lawyers who are supposed to sell it may keep audits privileged and sampled rather than continuous.
- Timekeeping vendors may be "good enough" for everything except the health-record check.

**Fastest test (2–4 weeks):**
1. Through one defense firm, get 2–3 California nursing-home or home-health chains to share 6–12 months of punches, pay registers and PointClickCare or visit-verification logs, under the firm's direction.
2. Run the engine and report the unpaid premiums, overtime-rate errors and unmatched logins that the current timekeeping system missed.
3. Ask each operator to sign a paid letter of intent on the spot.

**Kill it if** the missed exposure is under about 5 times the annual subscription, or if the operators or their lawyers won't let the health-record-vs-punch results exist.

VERDICT: PASS
