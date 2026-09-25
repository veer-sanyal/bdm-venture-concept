# Generator 3, loop 2 (2026-09-25; founder brief plus labor-line seed; web only)

Saved by the orchestrator from the agent's final reply. Desk research; not customer validation.

**Best idea:** an AI service that finds overpaid sales and use tax on manufacturers' purchases, files the refund claims, then prevents the overpayment. Start with Indiana manufacturers.

## Best idea: sales and use tax refunds for mid-size manufacturers

**The work being replaced.** Tax consultants review past purchase invoices for sales or use tax paid on exempt items: production machinery, repair parts, consumables, packaging, and electricity or gas used in production. They file refund claims going back 3 years for a share of the refund.
- **Whose fee:** the 30–40% contingency fee a first-time client pays for a ["reverse audit"](https://rkmillerassociates.com/sales-and-use-tax-compliance-consultants/salt-sales-and-use-tax-reverse-refunds-tax-recovery-services/). Firms: Ryan LLC (about [$715M revenue in 2021](https://en.wikipedia.org/wiki/Ryan_LLC)), the Big 4, regional firms (Cherry Bekaert, CLA), specialists (TaxMatrix).
- **Also replaced:** engineering firms' "utility studies" proving at least half a meter's power goes to production ([Whitinger](https://whitinger.com/services/predominant-use-studies/), [GA Group](https://gagroup.com/capabilities/advisory-services/appraisal-valuation-services/tax/utility-sales-tax-exemption/indiana-utility-sales-tax-exemption)). Later, in-house tax and AP time on purchase tax.

**Why AI can do most of it now.** Reading huge numbers of messy invoice lines and checking each against state exemption rules (Indiana requires direct use in direct production, [45 IAC 2.2-5-8](https://www.law.cornell.edu/regulations/indiana/45-IAC-2.2-5-8)). Firms review samples by hand; AI can review every line cheaply, making smaller companies worth serving.

**Why Indiana.**
- Manufacturing is ~27% of Indiana's economy ([USAFacts](https://usafacts.org/answers/what-is-the-gross-domestic-product-gdp/state/indiana/)); ~7,500–9,500 manufacturers ([MNI](https://www.mni.net/info/indiana-manufacturers-directory), [D&B](https://www.dnb.com/business-directory/company-information.manufacturing.us.indiana.html)).
- A specialist calls Indiana "the most amenable state"; example refunds $172K (25,000 sq ft plant) and $1.1M (two plants) ([TaxMatrix](https://www.taxmatrix.com/indiana-sales-tax-refunds-why-stop-at-energy/)).
- Indiana DOR allows 36-month lookback ([DOR](https://www.in.gov/dor/i-am-a/business-corp/sales-use-tax-refunds/)).
- Purdue MEP served 724 companies in a year ([NIST](https://www.nist.gov/mep/centers/purdue-manufacturing-extension-partnership)): a channel.

**Growth.** (1) Free scan, paid from refunds at ~20% instead of 30–40%. (2) Monthly subscription checking tax on every purchase invoice before payment. (3) Neighboring states. (4) Other leakage: business property tax, duplicate supplier payments (PRGX, apexanalytix), tariff refunds. End state: an AI tax department for mid-size companies.

**Market size.** Businesses paid >$220B a year in sales tax on purchases in FY2024 ([EY/COST](https://www.ey.com/en_us/insights/tax/total-state-and-local-business-taxes-fy24)). If 1% is overpaid (assumption), ~$2.2B a year, ~$6.6B across a 3-year lookback. Indiana: 2,000 manufacturers × $150K × 20% ≈ $60M one-time fees (assumptions).

**Weakest.**
1. Revenue repeats poorly; valued like services unless the subscription proves itself.
2. Cash arrives late (states take months).
3. Not unique: [Saveware](https://www.psu.edu/news/invent-penn-state/story/penn-state-student-startup-saveware-innovates-tax-refunds-ai) (Penn State student startup, restaurants, 2024); [CereTax](https://www.ceretax.com/blog/manufacturing-sales-tax-refunds); Thomson Reuters [AI sales and use tax product](https://www.thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk) (Jan 2026); Ryan adding AI.
4. Trust and risk: three years of purchase data to students; denied claims; audit fear; need a SALT CPA advisor and insurance.

**Before the competition:** interview 20+ Indiana manufacturing controllers on past reviews, who did them and the fee; run 3 free scans.

## Runners-up

**1. Medical claims audits for self-funded employers.** Replaces outside claims auditors and benefits consultants. Administrators check 250–400 of ~80,000 claims a year; full review recovers 1–3% of claims spend ([Benosphere](https://benosphere.com/blog/self-funded-claims-audit-5-percent-problem)). 67% of covered workers are in self-funded plans ([KFF 2025](https://www.kff.org/health-costs/2025-employer-health-benefits-survey/)). A 2026 federal law gives plans the right to audit PBMs with an auditor of their choosing from plan years starting 2029 ([DWT](https://www.dwt.com/blogs/employment-labor-and-benefits/2026/02/reform-raises-stakes-for-pbms-erisa-fiduciaries)). Weakest: getting claims data out of administrators; broker-led sales; HIPAA; [CodaHx](https://codahx.com/) and others.

**2. Commercial property tax appeals.** Replaces consultants' 25–35% of savings. Public assessment records allow pre-computed over-assessment and cold outreach. Weakest: crowding ([Reserve Tax AI](https://reservetax.ai/) at 15%, [Avalara](https://techedgeai.com/avalara-unveils-ai-powered-property-tax-platform-to-speed-enterprise-compliance/), Ownwell $50M); annual cycle with hearings; certification in some states.

## Checked and not recommended
- **Duty drawback:** crowded (Pax and Tarifflo, both YC; Zollback, LightSource, Tariff Refund HQ) ([Zollback](https://www.zollback.com/blog/tariff-refunds-for-smbs), [Pax](https://www.ycombinator.com/companies/pax)); the IEEPA refund wave runs through a new CBP system ([Skadden](https://www.skadden.com/insights/publications/2026/03/tariff-refund-mechanism-takes-shape)).
- **Environmental compliance reporting:** [Encamp](https://www.prnewswire.com/news-releases/encamp-launches-compliance-platform-with-embedded-ai-accelerating-the-shift-to-proactive-ehs-management-302770998.html) >$40M, AI product May 2026.
- **Auto-supplier quality paperwork:** Omnex, QualityEngineer.ai; value hard to quantify.
