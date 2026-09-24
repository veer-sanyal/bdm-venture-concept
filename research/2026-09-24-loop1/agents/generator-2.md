My pick is a service that prepares and files nursing home residents' long-term-care Medicaid applications. I ran this as a Generator under the team's METHOD.md: once I saw the task was the Generator prompt word for word, I stopped reading the repo. I skimmed the README, which names the earlier chargeback concept, but I did not read STATE, CASEBOOK or the candidate files. Everything below comes from the web, and none of it is customer validation.

## Best idea: AI that prepares long-term-care Medicaid applications for nursing homes

**The problem.** A nursing home isn't paid for a resident on Medicaid until the state approves that resident's application. Most residents end up there: 63% of the 1.24 million people in 14,742 certified facilities have Medicaid as primary payer (KFF, July 2025). A complete application needs 60 months of the resident's bank records. The state uses them to check for gifts or transfers made to qualify. Adult children are slow to gather those records, and the facility's business office staff are overloaded.

**Why now.**
- Starting January 1, 2027, the 2025 budget law cuts retroactive coverage for traditional Medicaid (which covers most nursing home residents) from three months to two. Coverage now reaches back only two months from the filing date, so a slow filing costs the facility about $9,450 per month at the median semi-private rate. The facility eats that bill.
- States are checking income and asset documents more strictly, and small discrepancies now cause delays and denials (Richter Healthcare, 2026).
- Indiana gives a local starting point. The state owed 496 nursing homes $462M in delayed payments this spring. It is also moving long-stay residents out of managed care and back to the state's direct payment system on July 1, 2027, after a $91M first-year overrun.

**Product.** The family gets a link and connects bank accounts or uploads statements. The AI reads five years of transactions, flags transfers the state will question, and drafts the explanations. It calculates income, assets and any penalty period, fills the state's form, and drafts replies when the caseworker asks for more information. Facility staff review and file. The price is per approved application, with renewals billed separately.

**Value over what facilities use today.** Today the work is done by in-house staff or by per-case services firms (Richter, Medicaid Plus). Telos LTC is software for whoever fills the forms, and it covers about 100 Texas facilities. CoreCare tracks pending applications for 1,500+ facilities but does not prepare them. As far as I could find, nobody does the actual preparation work with AI.

**Starting narrow, growing broad.** The path runs from Indiana nursing homes, to chains in several states, to home-care waiver and assisted-living applications, then renewals. After that come elder-law firms and families, then other aging benefits such as VA pension and long-term-care insurance claims. Each state's rules and each caseworker's patterns of requests become data a newcomer doesn't have. This lines up with YC's Fall 2026 request "AI for the Aging Population."

**Weakest points.**
- Market size. My rough estimate, which comes from no source, is 250,000 to 350,000 new nursing home applications a year at about $1,000 to $1,500 each. With renewals that is roughly $0.4B to $0.6B, before home-care waivers. A judge will likely score this a 3.
- CoreCare already sits in 1,500 facilities and could add preparation. PointClickCare, the dominant nursing home records system, controls the integration marketplace.
- Each state is effectively a separate rulebook. The product handles sensitive financial data, and a denial can be blamed on the product.
- The family is the real bottleneck. From memory (not checked this session), bank-connection services such as Plaid usually return about two years of history, so the other three years still arrive as PDFs.

**Fastest test.** Call ten Indiana nursing home business office managers and ask three things: how many residents are Medicaid-pending right now, the median number of days from when private funds run out to filing, and what they pay outside firms per application. If filing already happens within about 30 days, the 2027 cut barely matters and the urgency case weakens.

## Runners-up worth keeping

1. **AI sales-tax recovery for mid-sized manufacturers, paid from what it recovers.** Manufacturers often pay sales tax on equipment and supplies that their state's manufacturing exemption covers. The AI reads three to four years of vendor invoices and files the refund claims. The pitch is easy because the customer pays only out of recovered money, and Purdue's manufacturing extension program is a channel to Indiana plants. Weakest: Arthiva already does this with AI, CPA firms hold the relationships, and most of the money is a one-time look-back.
2. **Pre-award grant compliance review for universities.** An AI checks a proposal against sponsor rules before the university's grants office submits it. The founders can reach Purdue's grants office and faculty directly, and grants offices are cutting staff while funding stays uncertain. Weakest: the market is small, universities buy slowly, and FundRobin, GrantOps and the Cayuse/Kuali incumbents are already there.
3. **SNAP payment-error reduction for counties that run SNAP themselves.** This is the largest dollar pain I found. The FY2025 national error rate was 10.62%, and states could owe up to about $11B a year from FY2028. Weakest: Maximus shipped an "Accuracy Assistant," Code for America is piloting with Anthropic, incumbents own the eligibility systems, and government sales cycles are long.

## Checked and dropped
- **Duty drawback:** Zollback plus eight or more platforms already compete.
- **IEEPA tariff refunds:** a one-time event.
- **PFAS declarations:** Assent and Certivo already sell AI tools, and EPA is narrowing the rule.
- **ADA Title II accessibility:** the deadline moved to April 2027, and Adobe, PDFix and several AI newcomers are there.
- **Transfer credit:** DegreeSight, EDMO and DiscArc.
- **Export classification (ECCN):** GingerControl and TariffWolf.
- **Medicaid work requirements:** Fortuna Health ($22M, a16z).
- **CMMC:** DoD suspended Phase 2 on July 13, 2026.
- **Insurance premium audits:** Roots.ai and V7.
- **Crop insurance:** Insure.ag and Leaf.
- **Lease audits:** Tango and LeaseMind.
- **Aircraft logbooks:** Bluetail, LogAir and others.

Every lane already had AI entrants, so what separated them was a hard deadline worth real dollars to the buyer and whether an incumbent already owns the data.

The session's web-search budget (200 calls) ran out near the end. The market-size estimate and the claim that no one else does the preparation step are unverified beyond what's cited here. I wrote no files and made no commits.

Sources:
- [KFF nursing facility characteristics](https://www.kff.org/medicaid/a-look-at-nursing-facility-characteristics/)
- [AARP on the budget law and nursing homes](https://www.aarp.org/advocacy/one-big-beautiful-bill-nursing-homes/)
- [Kiplinger on nursing home effects](https://www.kiplinger.com/retirement/long-term-care/striking-ways-the-big-beautiful-bill-affects-nursing-homes)
- [Richter on Medicaid pending in 2026](https://blog.richterhc.com/medicaid-pending-in-2026-new-risks-greater-scrutiny-higher-stakes)
- [CoreCare](https://corecare.ai/)
- [Telos LTC](https://www.telosltc.com/)
- [Approved Admissions on Indiana's 2027 change](https://approvedadmissions.com/indiana-pulls-long-stay-residents-out-of-managed-medicaid-a-warning-shot-for-every-pathways-style-state/)
- [Skilled Nursing News, Indiana back payments](https://skillednursingnews.com/2026/04/nursing-homes-in-state-owed-almost-500m-in-medicaid-back-payments-due-to-managed-care-transition-delays/)
- [ExaCare Series A](https://www.prnewswire.com/news-releases/exacare-ai-raises-30m-series-a-to-reimagine-admissions-and-launch-a-powerful-suite-of-ai-agents-for-skilled-nursing--home-care-302586587.html)
- [YC Fall 2026 requests](https://modelence.com/yc-rfs-fall-2026)
- [Arthiva](https://arthiva.ai/)
- [FundRobin](https://www.fundrobin.com/articles/thought-leadership/ai-grant-writing-tools-university-research-administrators/)
- [Polimetrics on SNAP cost share](https://polimetrics.substack.com/p/snaps-new-error-rate-penalty-a-12)
- [Maximus Accuracy Assistant](https://maximus.com/news-and-events/maximus-launches-snap-accuracy-assistant)
- [GovExec on Code for America and Anthropic](https://www.govexec.com/technology/2026/05/anthropic-code-america-pilot-ai-tools-snap/413464/)
- [Zollback](https://www.zollback.com/blog/duty-drawback-services)
- [Fortuna Health](https://www.businesswire.com/news/home/20250721481890/en/Fortuna-Health-Raises-$18M-Led-by-Andreessen-Horowitz-to-Modernize-Medicaid-Access-and-Infrastructure-Amid-Federal-Reforms)
- [CMMC Phase 2 pause](https://elevateconsult.com/insights/cmmc-level-2-phase-2-suspension-what-it-means/)
- [DOJ Title II extension](https://upcea.edu/doj-extends-accessibility-deadline-to-april-2027-policy-matters-april-2026/)
- [TSCA PFAS status](https://greensofttech.com/blog-2026-current-status-of-the-tsca-8a7-pfas-reporting-rule/)
