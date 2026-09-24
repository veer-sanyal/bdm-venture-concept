I've rebuilt the idea so it answers all three investors' objections. All of this is desk research, and none of it is customer validation. The chain data test in section 6 is the only thing that can confirm or kill it.

## 1. The company (working name: Lookback)

**One line:** a Medicaid desk for nursing home chains, run by AI, that gets paid when an application is approved. What it really sells is a checked, source-linked record of the applicant's last five years of finances, built in days rather than weeks.

**Why that record is the product:** the form was never the hard part. Every applicant has to account for 60 months of accounts and transfers, and the family, the facility, any lawyer and the state caseworker all redo that review by hand. Illinois's 2025 state audit shows it is where the state's time goes:
- 17 of the 50 sampled applications (34%) were sent for an asset investigation.
- Those cases spent an average of 58 days at the investigating office.
- Applications without an investigation were decided in about 22 days.

**What the engine does:**
- Retrieves all 60 months of records. It uses a bank-data connection where that works, sends automated records requests to banks under power of attorney for older statements, and reads paper statements and check images.
- Reconciles balances month by month and classifies every outflow.
- Flags transfers that trigger a penalty and computes the penalty under each state's rules.
- Produces a file ready for the caseworker, with every entry linked to its source document.

The same engine then drives:
- **At referral or admission:** a financial screen within 24 hours, before the bed is committed.
- **By about day 5:** filing timed to protect the new two-month retroactive window.
- **Until the state decides:** an agent answers every caseworker document request, and chases the family and banks by text and phone, before each deadline.
- **Every year:** the renewal for each Medicaid resident, which gives recurring revenue.

## 2. How it answers the investors

**"Most losses come from things software can't fix."** Change what gets counted. Hidden transfers and excess assets can't be fixed after admission, but they can usually be seen in bank data before it. The facility can then admit knowing the risk, set up a private-pay plan, or have the family return the transferred money, which can remove the penalty. So the test should measure the share of written-off dollars that were either fixable or foreseeable at admission, not fixable alone. I also found one hint that the fixable share can be large: in a vendor case study, CoreCare's tracking software alone cut a 25-building Texas chain's pending write-offs by 60% (over $1M).

**"The state is the bottleneck."** The analysis we would submit is exactly the step that is slow on the state's side. Whether a pre-checked file actually shortens the state's asset review is a hypothesis to test with caseworkers.

**"The product already exists."** I checked each incumbent:

| Incumbent | What it does | Why it's not this |
|---|---|---|
| Medicaidsoft | Do-it-yourself software; pulls about 24 months through a bank-data connection | Staff still do the work, and it doesn't cover 60 months |
| CoreCare (1,500+ facilities) and RevSuite | Track and monitor cases | They don't do the work |
| ExaCare ($30M Series A, Oct 2025) | Admissions and reimbursement AI agents | None of its listed agents handles eligibility |
| Medicaid Done Right (about 600 facilities, 16 states, 118,600 approvals since 2012) | Outsourced application service | Mainly people doing the work by hand |
| Medicaid Plus | Outsourced application service in PA, NJ, DE and MD | Free to the facility, so harder to compete with there |

**"The market is small."** For nursing homes alone, that's correct. The plan in section 4 grows from there.

## 3. Customer, pricing, first market

- **Buyer:** the revenue-cycle lead at chains of 10 to 50 buildings.
- **Pricing to test:**
  - about $1,250 per approved new application;
  - 10% of the balance recovered on cases handed over after more than 60 days pending;
  - about $150 per completed renewal;
  - no fee per building.
- **Rough value per chain:** Medicaid Done Right's own totals work out to about 14 approvals per facility per year, so a 25-building chain might file 350 to 500 applications and hold about 1,500 Medicaid residents. That is roughly $0.7M to $0.9M a year. This is an estimate, not validated.
- **States:**
  - Illinois first: it's two hours from Purdue, it had about 15,600 long-term care applications in 2023, and it has public audit data.
  - Pennsylvania second: the pain is sharpest there, with 30 facility closures between early 2024 and June 2025 and reports of applications taking over a year. But free outsourcers operate there.
  - California third: it brought back its $130,000 asset limit on January 1, 2026, and its lookback grows to 30 months by July 2028.
  - Indiana chains are easy to reach for discovery interviews.

## 4. Market and how it grows

**Nursing homes:**
- About 1.2M residents, 63% on Medicaid (about 756,000), according to KFF.
- About 200,000 to 300,000 new applications a year. This is my estimate, projected from the Illinois volume and Medicaid Done Right's per-facility rate.
- At these prices, that is about $400M to $550M a year including renewals. Not venture-scale alone.

**Expansion path:** sell to whoever loses money when an older or disabled person's Medicaid is late or lapses.
1. Assisted living waivers, home care agencies and PACE (204 programs, about 97,000 participants). About 5.1M people use Medicaid home and community-based care.
2. Dual-eligible Medicare Advantage plans (6M+ members in 2026). They lose members whose Medicaid lapses at the annual renewal, so they have a budget for renewal support.
3. Later, lending against pending receivables once we can predict approval odds and timing. Federal law bars factoring Medicaid receivables, so this would have to be structured as loans to the facility through a partner lender.

Fortuna Health ($18M Series A led by a16z) is building the same kind of company for the working-age expansion population, which is a different lane. Ours is the asset-tested lane for older and disabled people. Taken together, this is plausibly a market above $1B. That is an estimate.

## 5. Why now

- From January 1, 2027, retroactive coverage is limited to two months before the filing month (down from three), so filing late now loses money outright.
- California brought back its asset test in 2026.
- From the end of 2026, states must renew expansion adults every six months and start work requirements. My inference is that this will pull caseworkers away and slow long-term care decisions further.
- The federal streamlining rule is on hold until 2034, so states' slow processes will stay.

## 6. What could kill it, and the 30-day test

**Risks:**
- Free outsourcers paid by families.
- States starting to pay providers during the pending period (a Pennsylvania bill proposed this in October 2025).
- PointClickCare or CoreCare adding this work to what they already sell.
- Unauthorized practice of law: stay on application preparation and refer planning advice to elder-law attorneys.
- Misuse to turn away Medicaid residents: position the screen as a planning tool, and follow state anti-discrimination rules.

**The test:**
1. Get 3 to 5 chains in Illinois, Indiana or Pennsylvania to share 12 months of pending cases and write-offs.
2. Sort every day of delay by cause (family, facility or state). Tag every written-off dollar as fixable, foreseeable at admission, or neither.
3. Record which vendor each chain uses today and what it pays, including family-paid "free" services.
4. Run 20 stuck cases by hand for pilot chains using AI tools, and compare against similar cases the chain handles itself.
5. Ask 3 to 5 caseworkers whether a source-linked transfer ledger would cut their document requests.

**The idea is dead if** fixable plus foreseeable causes are under about 40% of written-off dollars, chains already get this done cheaply, or fewer than 2 chains sign a paid pilot within 30 days.

## 7. Weaknesses

- Nobody on the team has worked in this industry. Recruit a former business office manager or state caseworker as an advisor early.
- We have no pricing data for any competitor. Get it in the chain interviews.

I haven't published this anywhere. It can be turned into a shareable page or pitch document if you want one.

Sources:
- [AARP: the 2025 federal law and nursing home residents](https://www.aarp.org/advocacy/one-big-beautiful-bill-nursing-homes/)
- [ASTHO law summary](https://www.astho.org/advocacy/federal-government-affairs/leg-alerts/2025/one-big-beautiful-bill-law-summary/)
- [Illinois Auditor General, Medicaid long-term care eligibility audit (2025)](http://www.auditor.illinois.gov/Audit-Reports/Performance-Special-Multi/Performance-Audits/2025_Releases/25-Medicaid-LTC-Eligibility-Perf-Digest.pdf)
- [McKnight's on pending Medicaid models](https://www.mcknights.com/news/new-models-emerge-for-handling-pending-medicaid-applications-provider-pay/)
- [Medicaidsoft for care facilities](https://www.medicaidsoft.com/care-facilities)
- [CoreCare](https://corecare.ai/)
- [CoreCare case study: Focused Post Acute Care Partners](https://corecare.ai/resources/how-focused-post-acute-care-partners-reduced-medicaid-write-offs-by-2m/)
- [ExaCare Series A](https://www.insightpartners.com/ideas/exacare-ai-raises-30m-series-a-to-reimagine-admissions-and-launch-a-powerful-suite-of-ai-agents-for-skilled-nursing-home-care/)
- [Medicaid Done Right](https://www.medicaiddoneright.com/Company.html)
- [Medicaid Plus](https://www.mymedicaidplus.com/nursing-facilities.html)
- [RevSuite](https://www.revsuitesolutions.com/)
- [Fortuna Health Series A](https://www.businesswire.com/news/home/20250721481890/en/Fortuna-Health-Raises-$18M-Led-by-Andreessen-Horowitz-to-Modernize-Medicaid-Access-and-Infrastructure-Amid-Federal-Reforms)
- [KFF: 5 key facts about nursing facilities and Medicaid](https://www.kff.org/medicaid/5-key-facts-about-nursing-facilities-and-medicaid/)
- [KFF: Medicaid home care in 2025](https://www.kff.org/medicaid/medicaid-home-care-hcbs-in-2025/)
- [Justice in Aging: California asset limit reinstatement](https://justiceinaging.org/reinstatement-of-medi-cal-asset-limit-faq/)
- [National PACE Association: 200 programs](https://www.npaonline.org/about-npa/news/news/2026/02/26/pace-reaches-major-milestone-with-200-programs-nationwide)
- [Disability Exchange: dual-eligible plans in 2026](https://disabilityexchange.org/blog/d-snp-dual-eligible-special-needs-plans-2026/)
- [Abrams Law: restriction on factoring Medicaid receivables](https://www.abramslaw.com/media/announcements/legal-restriction-on-factoring-medicaid-and-medicare-receivables-limits-financing-options-for-healthcare-providers/)
- [BDO: six-month renewals and work requirements](https://www.bdo.com/insights/blogs/bdo-knows-healthcare/understanding-the-new-medicaid-redetermination-and-work-requirements)
- [Pennsylvania Senate co-sponsorship memo (Sen. Judy Ward)](https://www.palegis.us/senate/co-sponsorship/memo?memoID=46098)