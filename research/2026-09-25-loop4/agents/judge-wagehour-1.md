## Assessment: continuous pre-payroll wage-and-hour checks for California healthcare employers

As you asked, I did not read the local project files. That includes METHOD.md, which the repo's AGENTS.md says to read. Everything below comes from web sources.

### What checked out
- **Notice volume is correct.** The LWDA logged a record 10,098 PAGA notices in 2025, and 8,846 in fiscal 2024-25. Five law firms filed about 24% of them. ([CA Employment Law Report](https://www.californiaemploymentlawreport.com/2026/01/paga-is-not-slowing-down-what-reasonable-steps-must-look-like-for-california-employers-heading-into-2026/), [GV Wire](https://gvwire.com/2026/04/15/california-goes-after-vexatious-paga-law-firms-how-much-have-they-cost-employers/))
- **$2.2B is roughly right, with a caveat.** CABIA's tracker shows $2.16B across 2,352 settlements in 2025, averaging about $918K each, of which $725M went to attorney fees. 2026 had reached $1.63B by August. The caveat is that these are total settlement amounts. Most cases settle class wage claims together with PAGA claims, and the PAGA-penalty share is usually a small part of the total. ([CABIA](https://cabia.org/research-data/paga-summary/), [LASC model settlement](https://lascpubstorage.blob.core.windows.net/forms/Forms%20Comprehensive%20List/LASC%20CIV%20296.pdf))
- **The 15% cap exists, but it is narrower than the pitch implies.** Labor Code §2699(g) caps penalties at 15% if the employer took "all reasonable steps to be in compliance with **all provisions identified in the notice**" before receiving the notice. The cap is 30% if those steps come within 60 days after it. The statute's examples include "periodic payroll audits and took action in response." ([Labor Code §2699](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=LAB&sectionNum=2699)) Three limits follow:
  - The cap applies only to PAGA penalties, not to class wages or premiums.
  - Notices usually allege a long boilerplate list of violations. A tool that only checks meal breaks and overtime cannot, alone, show reasonable steps for everything listed.
  - As of April 2026, no significant published court decision had interpreted "reasonable steps." ([Loeb](https://www.loeb.com/en/insights/passle/2026/04/keeping-up-with-paga))
- **Size of the first market.** California nursing homes employed about 156,800 people in December 2025 ([FRED](https://fred.stlouisfed.org/series/SMU06000006562310001)).

### Who else serves this customer
- **Incumbents own the data and the buying channel.** The time and payroll data sits with UKG/Kronos, SmartLinx and Viventium, which sell specifically to senior care and skilled nursing. Home health also has its own visit-verification and scheduling platforms. These systems already flag missed meals before payroll closes ([Viventium](https://viventium.com/industries-skilled-nursing/), [SmartLinx](https://www.smartlinx.com/solutions/time-and-attendance/)). CloudApper, a UKG partner, automatically adds meal-break premiums inside UKG and Workday ([CloudApper](https://ukg.cloudapper.ai/time-capture/california-meal-rest-break-compliance-ukg/)).
- **Scaled Comp is the closest match, so I treat it as this team.** It checks 100% of shifts at every location and runs monthly checks that build "a dated reasonable-steps record." It takes data exports from any system, has a tier for defense firms, and charges $5K–$15K for an initial audit ([Scaled Comp](https://www.scaledcomp.com/for-businesses-hr-teams)). What it does not show is checking before payroll runs, using health-record or badge data, or a healthcare focus. Those three things are what would set this company apart.
- **Law firms and point tools.** Littler (its Audit QB tool), Seyfarth and Ogletree sell audits backed by in-house data teams ([Littler](https://www.littler.com/practices-industries/audit-services), [Ogletree](https://ogletree.com/insights-resources/blog-posts/beyond-the-data-part-i-using-ai-tools-to-turn-workforce-data-into-preventive-compliance/)). Regular Rate Audit handles overtime-rate math ([site](https://regularrateaudit.com/learn/regular-rate-of-pay-employer-guide/)). Employer's Guardian sells meal and rest break management ([site](https://www.employersguardian.com/meal-and-rest-period-management)).
- **No one visible checks punches against health-record logins.** Plaintiff firms already use those timestamps as evidence against employers ([RM Legal](https://www.rmlegalgroup.com/your-bosss-data-can-prove-your-overtime-using-badge-swipes-pos-logs-and-ehr-timestamps-to-win-wage-claims/)).

### 1. The strongest version
A pre-payroll check for multi-site California nursing-home operators. It sits on top of UKG, SmartLinx or Viventium rather than replacing them. It does three things:
- Corrects underpayments in the same pay period: missing meal and rest premiums, and overtime that leaves out bonuses and shift differentials. Paying them promptly limits wage exposure too, not just PAGA penalties.
- Checks punches against login records from the nursing-home health-record system, and badge swipes, to find off-the-clock work. Nobody else visibly does this.
- Produces a reasonable-steps record covering the full list of violations that typical notices allege. That list includes wage statements, final pay timing, sick pay and expense reimbursement, not just meals and overtime.

It would be sold through defense firms, so the findings can be protected by attorney-client privilege, and through the state nursing-home trade association. Where an insurance policy covers wage-and-hour claims, that coverage is usually capped at $250K–$500K and often pays defense costs only ([SHRM](https://www.shrm.org/topics-tools/employment-law-compliance/epli-often-excludes-wage-hour-claims), [Woodruff Sawyer](https://woodruffsawyer.com/insights/ruling-insurance-wage-hour-claim)), so the uninsured exposure is the pitch. Home health would come second. I would drop clinics.

### 2. Ratings
| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | A record 10,098 notices in 2025 and average settlements near $918K. For a 300-person operator, that dwarfs about $15K a year of software. |
| Value over what customers use today | 3 | The time systems and CloudApper already add meal premiums, and Scaled Comp already checks every shift monthly and keeps a reasonable-steps record. Only the pre-payroll timing and the health-record/badge check are new. |
| Market size | 2 | About 157K nursing-home workers × about $4 per employee per month is under $8M a year. Adding home health gives low tens of millions. PAGA exists only in California. |
| Risk (5 = low) | 2 | The 15% cap has no court interpretation yet and requires compliance with every provision in the notice. Customers run on thin margins, and the product's flags raise their wage bill. |

### 3. What kills it, and the fastest test
**What kills it:** Operators decline to pay what the tool flags, because paying raises labor costs and creates a written admission. Or courts, or defense firms, don't treat a meal-and-overtime check as "all reasonable steps." Either way the product becomes a monthly audit report that Scaled Comp or a UKG add-on already sells, sitting on a small California-only market.

**Fastest test:** Get three multi-site California nursing-home operators to hand over six months of time, payroll and health-record login exports under a defense firm's privilege. Run the checks and show each operator its own dollar findings. Then ask for a paid per-employee contract that commits them to paying the flagged amounts going forward. Two of three signing means the need is real. Zero signing kills it within weeks.

Competition is not why I'm passing. The concept is sound, but the verified market is small, the legal benefit is untested, and the close matches already exist. The genuinely new part, checking punches against health-record logins, is too narrow on its own to support a venture-scale company.

VERDICT: PASS
