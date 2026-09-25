**Best idea: an AI Medicaid-eligibility team for nursing homes**

The idea is software that does the long-term-care Medicaid paperwork a nursing home now gives to its business office or to an outside firm. It would:
- collect five years of the resident's financial records, pulling bank statements directly and chasing the family for the rest
- review the transfers the state will check in its five-year look-back
- fill in the state's application
- track every request for more information and its 10-to-30-day deadline
- prepare appeals and annual renewals

It starts with skilled nursing facilities and grows into eligibility work for assisted living, home care, and then hospitals.

**Why it fits the seed**
- **Buyers who already pay people to do it.** There are about 15,000 certified nursing homes, and Medicaid is the main payer for 63% of their 1.2 million residents. Every long-stay resident who runs out of money needs an application. Homes do this by hand or pay firms like Richter or Medicaid Plus. Adding assisted living and home care gets past "tens of thousands" of buyers.
- **Delay and mistakes cost a lot, often.** A typical home has 3–10 residents waiting on a Medicaid decision at any time. Each case usually takes six months or more, and many take over a year. That's about $8,250 a month per resident, or around $50k per case, in unpaid care. My rough estimate from those figures is several billion dollars of unpaid bills tied up across the industry at any moment. "Failure to provide verification" is one of the most common reasons applications are denied, which is the exact kind of deadline-tracking and document-chasing error the product would prevent.
- **A dated reason to buy.** From January 1, 2027, the law passed in 2025 (OBBBA) cuts how far back Medicaid will pay for elderly applicants from 90 days to 60. After that, a slow application loses the home money for good. States are also tightening checks before approval, and the typical state processing time runs 45 to 90 days.
- **Nobody holds the data.** The records are the resident's bank statements and asset papers, which no nursing-home software stores. The work is sold by service firms, not software companies. I found no AI product aimed at this; the closest are Medicaidsoft (a tool for elder-law attorneys) and ExaCare (admissions AI).
- **AI actually helps.** The job is reading five years of messy documents, applying 50 states' rules, and never missing a deadline. That is work AI is good at and a two-person team could ship.
- **Pricing that shows value.** Charge per approved case or a share of recovered revenue, measured against what the home loses while a case is pending.

**What's weakest**
- **Money spent on the work.** Spend on the nursing-home slice alone is probably about $1–2B a year, and that's my estimate, not a sourced figure. It only clearly passes "billions" once it expands to assisted living, home care and hospitals. Hospitals are where Fortuna Health (a16z, $18M) already works.
- **Buyers.** Nursing homes have thin margins and chain buying is slow. ExaCare ($30M, used by 1,500+ facilities) or PointClickCare, the dominant nursing-home software, could add this as a feature.
- **The real bottleneck may be families.** Delays often come from relatives who don't hand over records, and AI can only partly fix that.
- **Legal and state-by-state risk.** Advising on how to handle assets can count as practicing law, and each state's rules and portals differ.
- **No price data.** What homes pay outside firms isn't published and has to come from interviews.
- **None of this is customer validation.** First step: interview 15–20 nursing-home business office managers, starting in Indiana. Ask how many cases they have pending, how old they are, who does the work and what it costs.

**Runner-up 1: an AI auditor that checks every customs entry for mid-size importers**
- **Why it could work:** It's the biggest market I found. More than 400,000 US businesses import, filing about 35 million formal entries a year, and customs brokers earn $4–5B from that work. One startup says 1 in 8 entries overpays duty. There's a live refund window too: the Supreme Court struck down the IEEPA tariffs in February 2026 and about $85B is being refunded. The data is the importer's own, in the government's customs system, so no software company holds it.
- **Weakest:** It's already crowded, including two Y Combinator companies:
  - Tarifflo (YC Summer 2026)
  - Pax (YC Summer 2024, $4.5M raised)
  - Zollback
  - Gaia Dynamics
  - Forge, an AI-native customs broker

  Tariff policy also keeps shifting. IEEPA was struck down, the Section 122 replacement tariff was ruled invalid by the trade court, and the steel and aluminum (Section 232) rules were restructured in April 2026. Refunds are one-time money. Undergrads would struggle to stand out.

**Runner-up 2: warranty-claim recovery for RV, marine, powersports and equipment dealers**
- **Why it could work:** Claims are filed by hand into many manufacturer and parts-supplier portals, rejections and short payments happen constantly, and missed claims are the biggest recoverable cost for these dealers. Elkhart, Indiana is the RV capital, which gives Veer and Cole local access.
- **Weakest:** Each vertical has only a few thousand dealers, and dealer software vendors hold the repair-order data. Forge AI already does this for car dealers. I researched this one least.

**Ideas I rejected**
- **Retailer deductions for consumer-goods brands:** Glimpse already has a16z backing and $52M.
- **Surprise-billing arbitration for doctors:** 2.56M disputes in 2025, but only a few thousand buyers and heavy political risk.
- **Commercial property-tax appeals:** Ownwell is there, and appeals come once a year.

As instructed, I used only the web and didn't open any project files, including the METHOD.md that the repo's AGENTS.md points to.

Sources:
- [GMA CPA: Medicaid pendings](https://www.gma-cpa.com/blog/how-long-term-care-facilities-can-better-manage-receivables-and-collections)
- [KFF: nursing facility characteristics](https://www.kff.org/medicaid/a-look-at-nursing-facility-characteristics/)
- [Hall Booth Smith: OBBBA and long-term care](https://hallboothsmith.com/medicaid-reforms-big-beautiful-bill/)
- [Richter: eligibility enforcement](https://blog.richterhc.com/medicaid-eligibility-enforcement-reshapes-long-term-care)
- [Texas HHS: denials](https://www.hhs.texas.gov/handbooks/medicaid-elderly-people-disabilities-handbook/b-6500-denials)
- [ExaCare Series A](https://www.prnewswire.com/news-releases/exacare-ai-raises-30m-series-a-to-reimagine-admissions-and-launch-a-powerful-suite-of-ai-agents-for-skilled-nursing--home-care-302586587.html)
- [Fortuna Health](https://www.businesswire.com/news/home/20250721481890/en/Fortuna-Health-Raises-$18M-Led-by-Andreessen-Horowitz-to-Modernize-Medicaid-Access-and-Infrastructure-Amid-Federal-Reforms)
- [Medicaidsoft](https://www.medicaidsoft.com/)
- [Medicaid Plus](https://www.mymedicaidplus.com/nursing-facilities.html)
- [Holland & Knight: IEEPA refunds](https://www.hklaw.com/en/insights/publications/2026/06/ieepa-tariff-refund-update-government-appeals)
- [Skadden: Section 122 ruling](https://www.skadden.com/insights/publications/2026/05/us-trade-court-strikes-down-section-122-tariffs)
- [Customs brokerage market](https://www.expertmarketresearch.com/reports/united-states-customs-brokerage-market)
- [Tarifflo (YC)](https://www.ycombinator.com/companies/tarifflo-inc)
- [Pax](https://www.paxai.com/blog/pax-ai-raises-4-5m-seed-funding-duty-drawback-ai-tariff-refunds)
- [Zollback](https://www.zollback.com/blog/tariff-refunds-for-smbs)
- [Glimpse Series A](https://www.tryglimpse.com/post/seriesa)
- [HFMA: surprise-billing arbitration data](https://www.hfma.org/payment-reimbursement-and-managed-care/no-surprises-act-idr-data-provider-wins/)
- [Ownwell](https://www.housingwire.com/articles/ownwell-property-tax-appeal-funding/)
- [Forge AI (dealer warranty)](https://www.forgedrive.ai/blog)
- [RV Reports](https://rvreports.ai/rv-warranty-coverage-explained-whats-covered-whats-not-and-how-to-win-claims/)
