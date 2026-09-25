I'd put Veer and Cole on an **AI caseworker that gets nursing-home residents approved for Medicaid**. Two cautions first. I ran out of web searches early: the whole session has a 200-search cap and I got only about a dozen of them. Everything below is also desk research, not customer validation. I didn't read any local project files, including METHOD.md, because the brief said not to.

## Best idea: an AI Medicaid application caseworker for nursing homes

**The work being replaced.** About 62% of nursing-home residents rely on Medicaid, which spent $56.7B on nursing-home care in 2016 (MACPAC). When a resident runs out of money, someone has to file a state Medicaid application. That means collecting up to five years of financial records, flagging gifts or asset transfers in that period, working out how much the resident must spend first, answering the state's requests for more documents, and redoing it at each renewal. Nursing-home billing staff do this, or the home pays small outside firms like Medicaid Plus. Those firms sell application processing, renewals, stalled-case rescue and appeals of denials.

**The product.** Families upload statements or connect their bank. The AI flags transfers in the five-year window, works out the spend-down, fills in that state's application, tracks the state's deadlines and drafts replies. A person reviews the file before it goes out. It could be priced per approved application or as a share of unpaid bills it recovers, so the home pays only when money comes in.

**Why it could work:**
- **The need is real and measurable.** Unpaid bills written off are about 1.41% of nursing-home revenue. The main cause is slow follow-up on residents whose Medicaid is still pending, plus private-pay balances. Billing offices are short-staffed; one example had a single person doing 2.5 people's work.
- **It's getting more urgent.** From January 1, 2027, a 2025 federal law (the "One Big Beautiful Bill") cuts how far back Medicaid pays for these residents, from 90 days to 60. Each late application can now cost a home about $9,450 in care it never gets paid for.
- **There's a home-state way in.** Indiana moved long-term care into managed care in 2024. As of April 2026, 496 Indiana nursing homes were owed $462M in back payments, and a 2026 state law moves long-stay residents back to the old system in 2027. Local homes are going through exactly this kind of paperwork upheaval.
- **No software company sits on this work.** PointClickCare holds the nursing home's clinical and billing records, but the application work runs on families' bank statements, state portals and paper. Approved Admissions only checks whether someone already has coverage. Qatalyst fills in reimbursement forms. HeyMedicaid and Fortuna sell to families, not nursing homes. My search was cut short, so this list isn't complete.
- **It can grow broad.** Next would be assisted-living and home-care Medicaid programs, then hospitals paying outside firms to get uninsured patients enrolled, then veterans' and disability benefits. That wider market is plausibly billions of dollars a year, but that's my estimate, not a sourced figure.

**What's weakest:**
- The narrow slice alone probably isn't billions. My rough estimate is about 15,000 homes with roughly one staff member each on this work, around $1B, plus outside-firm fees I couldn't find prices for. The billions depend on expanding.
- The slowest step may not be paperwork. Families not finding statements and states processing slowly are things AI can't fix. Indiana's backlog was mainly a state payment-method problem, not application quality.
- Nursing homes are low-margin, slow buyers, and PointClickCare could build this into its own product.
- Some states restrict Medicaid planning advice from non-lawyers, so the product must stay on application prep. It also handles health and financial data, so it needs HIPAA compliance and a SOC 2 audit from day one.
- The founders have no healthcare operations background.

**What to check first:** talk to 15–20 Indiana nursing-home billing managers and outside Medicaid firms. Ask how many applications they file a year, how many hours each takes, what outside firms charge, and how many of their days of unpaid bills sit in pending Medicaid.

## Runners-up

1. **Pre-audit of tenant income files for affordable housing (low-income tax credit and HUD properties).** The AI checks each tenant's income-certification file against the program rules before it's filed. It would sell to property managers and outside file-review firms. It could work because mistakes can cost owners their tax credits and trigger penalties. Haven AI cites a 2026 survey saying 91% of affordable-housing operators use AI, but almost all of it for leasing, not compliance. The weak spot is that Yardi and RealPage hold the data and the buying channel, which breaks your seed rule. The market also looks like about $1B, which is my rough estimate.
2. **Unchecked leads I ran out of searches for:** unclaimed-property reporting for mid-size companies, recovering overpaid sales and use tax, freight damage claims for mid-size shippers, and environmental compliance paperwork for small industrial sites. All fit the seed; none are researched.

## Looked at and rejected (already crowded)
- **Duty drawback and tariff refunds:** Pax AI ($4.5M seed), Zollback (YC S24) and Freehand ($75M). The Supreme Court tariff refunds are also a one-time event with the government's own portal.
- **Commercial property tax appeals:** Ownwell ($50M Series B, covers commercial too) and Reserve Tax AI. Business personal property tax filing is already covered by Avalara, CSC and Personal Property Pro.
- **Workers' comp premium audits:** Roots, V7, Insurity and EXL.
- **Cost segregation studies:** made more valuable by the permanent 100% bonus depreciation, but already a crowded market of cheap online providers.

Sources:
- [MACPAC nursing facilities](https://www.macpac.gov/subtopic/nursing-facilities/)
- [Maynard Nexsen on the OBBBA](https://www.maynardnexsen.com/publication-nursing-homes-feeling-mixed-effects-after-one-big-beautiful-bill-enacted)
- [AARP on the OBBBA and nursing homes](https://www.aarp.org/advocacy/one-big-beautiful-bill-nursing-homes/)
- [Skilled Nursing News, Indiana $462M](https://skillednursingnews.com/2026/04/nursing-homes-in-state-owed-almost-500m-in-medicaid-back-payments-due-to-managed-care-transition-delays/)
- [GMA-CPA bad debt benchmark](https://www.gma-cpa.com/blog/how-does-your-skilled-nursing-facilitys-bad-debt-expense-as-a-percentage-of-revenue-measure-up)
- [GMA-CPA receivables guide](https://www.gma-cpa.com/blog/how-long-term-care-facilities-can-better-manage-receivables-and-collections)
- [Medicaid Plus](https://www.mymedicaidplus.com/nursing-facilities.html)
- [Approved Admissions](https://approvedadmissions.com/nursing-homes/)
- [Qatalyst Health](https://app.dealroom.co/companies/qatalyst_health)
- [HeyMedicaid](https://heymedicaid.med/)
- [Medicaid pending explainer](https://www.medicaidplanningassistance.org/medicaid-pending/)
- [Haven AI survey](https://www.usehaven.ai/post/ai-for-affordable-housing-leasing-glossary)
- [M&L file reviews](https://mlcm.net/services/move-in-file-reviews-lihtc/)
- [Pax AI seed](https://www.paxai.com/blog/pax-ai-raises-4-5m-seed-funding-duty-drawback-ai-tariff-refunds)
- [Freehand drawback comparison](https://www.freehand.ai/articles/best-duty-drawback-software)
- [Penn Wharton on IEEPA refunds](https://budgetmodel.wharton.upenn.edu/p/2026-02-20-supreme-court-tariff-ruling/)
- [Ownwell $50M](https://www.housingwire.com/articles/ownwell-property-tax-appeal-funding/)
- [Reserve Tax AI](https://reservetax.ai/)
- [Personal Property Pro](https://personalpropertypro.com/)
- [Roots premium audit](https://www.roots.ai/platform/insurance-ai-agent/premium-audit)
- [Pease Bell on cost segregation](https://www.peasebell.com/insights/cost-segregation-study-2026/)
