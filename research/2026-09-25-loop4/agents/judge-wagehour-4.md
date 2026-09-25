I found little support for backing this. The need is real and growing, but the market is limited to California, the 15% cap is worth less than the pitch implies, and the most distinctive feature carries legal risk for the customer. I didn't read the local project files, as you asked. This is desk research, not customer validation.

## How the key claims hold up

- **9,000–10,000 notices in 2025: true.** 10,098 were filed in calendar 2025, a record, and 8,846 in fiscal 2024–25. Healthcare & Medical Services files the most notices of any industry. Senior living and post-acute care rose 28.4% year over year, the fastest of any sector ([Ankura via Mondaq](https://www.mondaq.com/unitedstates/constitutional-administrative-law/1821956/the-2025-to-2026-paga-trend-update-%7C-2-years-out-from-the-2024-reform-where-are-paga-filings-headed); [CA Employment Law Report](https://www.californiaemploymentlawreport.com/2026/02/five-things-every-employer-needs-to-know-about-the-lwdas-proposed-paga-regulations/)).
- **$2.2B in settlements: overstated as a PAGA figure.** The employer group's tracker (CABIA) shows $2.16B across 2,352 cases in 2025 but doesn't say how it counts ([CABIA](https://cabia.org/research-data/paga-summary/)). It appears to be whole settlements, most of which also include class-action claims. In those combined settlements, the PAGA share is usually 2–4% of the total ([CA Employment Law Report](https://www.californiaemploymentlawreport.com/2026/09/five-settlements-five-lessons-what-augusts-california-wage-and-hour-resolutions-tell-employers/)). The 15% cap applies only to that share.
- **The 15% cap: accurate but not automatic.** The statute (Labor Code §2699(g)) lists "periodic payroll audits and took action in response" as a reasonable step. Courts judge it on the "totality of the circumstances" ([statute](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=2699)). The state's February 2026 proposed PAGA regulations don't define "reasonable steps." I found no published appeals ruling that has applied the cap yet.
- **The common violations: well supported.**
  - Donohue v. AMN (2021): time records showing missed or short meals create a presumption of a violation ([Cal. Supreme Court](https://supreme.courts.ca.gov/sites/default/files/supremecourt/default/2022-08/S253677.pdf)).
  - Ferra v. Loews (2021): break premiums must be paid at the regular rate, which includes non-discretionary pay such as bonuses.
- **Off-the-clock work shows up in health-record logins, but that cuts both ways.** A flag the employer doesn't act on becomes evidence it "knew or should have known." It's also unsettled whether relying on a lawyer-run audit to prove reasonable steps gives up attorney-client privilege ([Liebert Cassidy Whitmore](https://www.lcwlegal.com/news/taking-reasonable-steps-to-protect-against-paga-claims-and-penalties-in-the-new-year/)).

## Who else serves this customer

- **The almost-identical pitch is ePeople AI.** It targets California nursing homes, catches missed breaks during shifts, adds premiums before payroll, and keeps signed per-shift records "you can hand to counsel" ([epeople.ai](https://epeople.ai/labor-law/)). As you instructed, I treated it as this team, not a competitor. It confirms that people who run nursing homes see the same opening. It doesn't show that customers pay.
- **Scaled Comp** was founded by a California defense lawyer (Zaller Law Group). It audits 100% of shifts, not samples, for $5k–15k per baseline audit, then runs monthly. It also sells to defense firms ([scaledcomp.com](https://www.scaledcomp.com/for-businesses-hr-teams)).
- **PAGIQ** (from the HR firm Easeworks) is exposure-modeling software used by lawyers on both sides ([easeworks.com](https://easeworks.com/paga-iq)).
- **Timekeeping vendors already flag missed breaks and apply premiums.** UKG has break attestation ([UKG](https://www.ukg.com/resources/product-info/ukg-pro-attestation)), and SmartLinx, built for senior care, has meal and break rules ([SmartLinx](https://www.smartlinx.com/why-smartlinx/intelligent-compliance/)).
- **Who owns the data and the channel:**
  - PointClickCare holds about 60% of the nursing-home health-record market ([IntuitionLabs](https://intuitionlabs.ai/articles/pointclickcare-ehr-long-term-care)). It controls the login data this pitch depends on, through its partner marketplace.
  - UKG and SmartLinx own the punch data.
  - No incumbent owns the defense-firm channel, but some firms are building their own tools, as Zaller did with Scaled Comp.

## 1. The strongest version

Narrow it to **"from PAGA notice to reduced penalty"** for multi-site California nursing-home and home-health operators, sold through defense firms.

- **Entry point: the day a notice arrives.** That happens about 10,000 times a year, and healthcare files the most notices of any industry. The statute caps penalties at 30% if the employer fixes the practices within 60 days of a notice. The product deploys in two weeks to earn that cap. The employer then keeps it running before every payroll, which builds the record for the 15% cap if another notice comes.
- **Build only what timekeeping doesn't do well:**
  - A regular-rate engine that classifies pay codes (shift differentials, bonuses, the new healthcare minimum wage) so overtime and break premiums are calculated correctly.
  - A check of punches against PointClickCare logins, badge swipes and home-health visit logs, to find off-the-clock work.
- **Run it under counsel.** Findings stay privileged, and a separate program record is what gets disclosed.
- **Target employers with arbitration agreements.** They face PAGA-only suits, where the cap actually covers most of the exposure.
- **Drop clinics for now.** They're too fragmented and run different systems.

## 2. Ratings

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | Healthcare files the most PAGA notices of any industry, and senior living and post-acute care rose 28.4% year over year (Ankura). |
| Value over what customers use today | 3 | UKG, SmartLinx and ePeople already flag missed breaks and pay premiums, and Scaled Comp audits every shift for $5k–15k. The added value is regular-rate math and log matching, and the cap is untested in court. |
| Market size | 2 | About 146k nursing-home workers in California (BLS), plus home health (roughly 100k+, my estimate). At $4–8 per employee per month, the core market is about $15–30M a year, in one state only. |
| Risk (5 = low) | 2 | The cap is unproven. The 15% applies only to the small PAGA share of combined settlements. Login-data flags can become evidence against the client. Access to PointClickCare data isn't assured. PAGA law keeps changing. |

## 3. What would kill it, and the fastest test

**What would kill it:**
- Defense counsel and operators won't pay monthly on top of UKG or SmartLinx, because break premiums are already handled and the cap's value isn't proven.
- Or counsel won't let clients create login-versus-punch evidence they then have to pay on.

**Fastest test:** Offer 10 California defense partners who handle nursing-home and home-health PAGA cases a paid, fixed-fee 60-day response package for their live notices. It would use the client's punches, payroll records and PointClickCare login export.

- **Pass:** within 3 weeks, at least 2 firms sign paid engagements, and at least 1 client actually delivers the PointClickCare data.
- **Pass:** that run finds regular-rate or off-the-clock amounts the client's current system didn't flag.
- **Kill:** otherwise.

**Why I'd pass:** The demand is real. But the dollar value of the cap is small in combined class-and-PAGA cases, and the break-premium feature is already sold by incumbents and by an almost-identical nursing-home team. The one distinctive piece needs PointClickCare's cooperation and can create legal exposure for the customer. And the market is limited to California.

VERDICT: PASS
