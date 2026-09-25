I'm returning one company, not three. The other ideas either scored below the bar before (Medicaid LTC applications, 10.0) or sit in small markets that already have AI entrants. This is desk research only; nobody has talked to a customer.

## Company: an AI-run environmental department for plants too small to have one

It starts with air permits in Indiana.

**Customer.** Single-site manufacturers with a state air permit and no environmental staff: paint and coating lines, printers, plastics, metal finishing, woodworking, foundries. In Indiana the first target is the 623 plants holding a federally enforceable synthetic-minor permit (FESOP), then smaller minor-source permits, then single-site Title V plants.

**Product.**
- Reads the plant's public permit and turns it into a calendar of obligations.
- Each month it takes purchase invoices, safety data sheets and production logs, and computes emissions and 12-month rolling totals against the permit limits.
- Drafts the quarterly, deviation, annual-certification and renewal filings. The plant official signs.
- An environmental engineer on staff reviews every filing.
- Charges extra for permit revisions when a plant adds a line or a paint booth.

This is sold as a finished service, not a tool for an EHS manager. Permit reading alone is now common: Encamp Scout (May 2026), [AirComply](https://aircomply.com/) (2 Sept), [EHS Insight](https://www.ehsinsight.com/blog/26.11-release-notes) (16 Sept) and [RegPermit](https://regpermit.com/) all do it. What sets this apart is taking over the monthly record-keeping and every filing, for plants with nobody to run software.

**Evidence I found:**
- **Indiana enforces the paperwork.** From EPA's ICIS-Air bulk data (refreshed 2026-09-20), 186 of Indiana's 623 operating synthetic-minor plants (30%) got a formal enforcement action in the last five years. That is the highest rate of any state with 200 or more such plants; the national rate is about 8%.
  - Of those 250 actions, 109 settled at $500. That is the amount IDEM charged in a case I found for a late quarterly report. Another 38 actions exceeded $10,000.
  - So fines are small. The pitch is replacing consultant fees and staff time, not avoiding fines.
- **Money already spent.**
  - An Indiana FESOP plant pays IDEM [$6,100 a year](https://www.in.gov/idem/airpermit/resources/timeframes-and-fees) in permit fees alone.
  - Ongoing consulting for a minor source runs [$1,500 to $20,000 a year](https://www.rmagreen.com/rma-blog/how-much-does-an-air-permit-cost), plus about $5,000 per renewal.
  - Other filings: Tier II $1,500 to $5,000 a year, and SPCC plans $3,000 to $6,000.
  - EPA's own paperwork estimate for Title V alone is [4.76M hours and $345M a year](https://www.govinfo.gov/content/pkg/FR-2022-03-25/html/2022-06348.htm), across 14,201 sources and 117 permitting agencies.
- **Market.**
  - Plants that could buy: 183,977 operating air facilities in EPA's database, of which 26,980 are synthetic minor, 13,544 major and 135,940 reported minor (minors are under-reported).
  - Expansion programs: about 463,000 Tier II filers and about 571,000 SPCC facilities.
  - Spend it draws from: US environmental consulting is [$27.4B](https://www.ibisworld.com/united-states/market-size/environmental-consulting/1427/) (IBISWorld 2025).
  - My own estimate, not sourced: 50,000 plants at about $8,000 a year is $400M for air alone. The whole environmental function at $15,000 to $20,000 per plant gets to about $1B.
- **Competitors.** Encamp (300+ enterprise customers, 32,000 facilities) and Mapistry (60+ customers, multi-site) sell to companies with EHS teams. AirComply sells annual per-facility contracts to EHS teams. No one I found does the work end to end for a plant with no EHS person.
- **Sales route.** Every Indiana permit is posted publicly, and EPA's ECHO database shows each plant's violation history. The company can build a plant's obligation calendar before the first call. Purdue MEP (500+ companies a year, already partnered with IDEM) and paint-booth installers, whose installs trigger permit revisions, are referral channels.

**Weaknesses:**
- Small plants pay modestly and buy slowly.
- Indiana's free, confidential assistance program (CTAP) advises plants. It doesn't file reports for them, but a judge will raise it.
- An AI error in a certified report creates liability, so the engineer review can't be skipped, which caps margins.
- AirComply or Encamp could move down-market.
- Federal deregulation, though state permits still bind.
- The generators' claim that paint suppliers give away VOC reports is unconfirmed.

**What would kill it:** plants won't pay about $500 a month to hand off reporting they now do late but cheaply.

**Fastest test:** build free obligation calendars for 30 Indiana FESOP plants from their public permits. Count how many take a call, and how many pay $500 to have the next quarterly report done.

**Expected scores (my guess):** need 3 to 4, value 3, market 3, risk 2. That puts it around the 10.93 bar; market is the parameter the judges could still mark at 2.

**Draft blind paragraph (about 150 words; trim before judging):**
> "Small US manufacturers with state air permits (coating lines, printers, plastics, metal finishing) must turn a long permit into deadlines, keep monthly emission records calculated from material purchases and safety data sheets, and file quarterly, annual and renewal reports. Plants without environmental staff pay consultants $1,500 to $20,000 a year or leave it to a plant manager. In Indiana, 30% of plants holding federally enforceable synthetic-minor permits received a formal enforcement action in five years, 44% of those actions settling at $500, the amount charged in a late-report case. This company acts as the environmental department for those plants. It reads the permit, takes in monthly purchase and production records, calculates emissions and drafts every report for the plant official to sign, with an environmental engineer reviewing each filing. It starts with air permits in Indiana, then adds stormwater, spill plans, chemical inventories and hazardous waste. Plants pay about $6,000 to $12,000 a year per facility."

## Dropped
- **Medicaid LTC applications:** scored 10.0 last round, and nothing new changes its roughly $100–250M market or its competitors (CoreCare, Medicaid Done Right, Medicaidsoft).
- **Medicare cost reports:** [costreporting.ai](https://costreporting.ai/) already prepares home health and hospice reports with AI, and the fee pool is under $1B.
- **Property tax, CAM audits, tax-credit file audits:** the generators' own crowding findings stand.
- **Freight claims:** CorePiper (YC W19) is already there, per the archive. **Sales and use tax recovery:** a one-time refund that every regional CPA firm sells. **Unclaimed property:** the money goes to the state.
- **Replacements I looked at and rejected:**
  - Medicaid work-requirement enrollment for providers: Fortuna already raised $18M from a16z for it.
  - Phase I site assessments: Atlas AI and FlipType are in it, and LightBox/EDR holds the data.
  - Stormwater as the first product: CloudCompli, ComplianceGo, SW² and Mapistry already sell it.
  - PFAS reporting under TSCA: delayed to 2027 and shrinking in scope.

## Corrections to the merged file
- AirComply also sells to facilities, not just consultants.
- Enforcement is thin nationally (about 8% of synthetic minors) but not in Indiana (30%).
- The Title V count of about 15,000 holds: EPA puts it at 14,201 sources.

I used the ECHO API and the ICIS-Air bulk download dated 2026-09-20. My working files are in the session scratchpad, which is deleted when the session ends, so the counts would need to be re-run to reproduce them. I didn't write or change any repo files.
