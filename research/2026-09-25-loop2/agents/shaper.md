# Shaper, loop 2 (2026-09-25; founder brief plus merged.md; read only merged.md, web research)

Saved by the orchestrator from the agent's final reply. Desk research; not customer validation. The deciding number, how much these companies actually overpay, is unknown.

## Company 1 (recommended): "Overpaid" (working name)

**What it is:** finds sales and use tax that mid-size manufacturers overpay on purchases, files the refund claims, then stops the overpayment. Starts with Indiana manufacturers of 50–1,000 employees; grows into the leakage-recovery department for mid-market companies.

**Who buys and why:**
- Buyer: controller or CFO; cash back, no upfront fee.
- Source of overpayment: Indiana exempts production equipment, repair parts, consumables, packaging, safety gear and production utilities; vendors keep charging tax, mostly because no exemption certificate (ST-105) is on file.
- Today: Ryan, the Big 4 and regional CPA firms take 30–40% of the refund.
- Volume: a mid-market manufacturer can have 80,000–250,000 purchase invoices over three years; firms review the big ones and sample the rest.
- Ryan valued ~$7B in January 2026; serves large enterprises.

**Why Indiana first:**
- The buyer files directly with the state (online or GA-110L), 36 months.
- Ohio and Michigan also allow direct buyer claims with four-year lookbacks: next states. Illinois and Kentucky refund only through the vendor.
- Utilities: >50% production use exempts the meter; proving it needs an engineering study.
- 6,900 manufacturing firms with Indiana establishments; ~2,084 with 20–499 employees, ~359 with 500–2,499 (Census 2022).

**Product, in stages:**
1. Free scan: AP export and invoice PDFs; AI checks every line against Indiana's production rules and a short map of how the plant works (exemption depends on use; the plant map is hard to copy).
2. Claim package: evidence and citation per line; also lists under-paid use tax so it can be cleaned up before filing, reducing audit risk.
3. Recurring: quarterly recovery claims, pre-payment invoice checks, exemption-certificate management with vendors.
4. Growth: utility studies → business personal property returns (Indiana's 2025 SEA 1 as amended raised the BPP exemption threshold to $2M from 2026 and phased out the 30% floor for equipment placed in service after 2025) → Ohio and Michigan → duplicate payments and vendor overbilling.

**Pricing and economics (assumptions to test):**
- 20% of lookback refunds, then $1–2K/month or a share of tax prevented.
- Vendor examples: $172K (one plant), $1.1M (two plants). At ~1% overpayment of taxable-type spend, a $25–250M manufacturer has ~$60K–600K over three years.
- 27,531 US manufacturing firms with 50–999 employees (Census 2022); at ~$50K/yr overpayment each, ~$1.4B/yr of leakage in that segment.

**Competition:** Ryan, Big 4, regional CPAs (expensive, sampling); TaxMatrix, Revenew and utility-study firms (ICS Tax, SmartSave), people-heavy; Arthiva (now an AI-native ERP with recovery as a side module); Avalara AvaTax for AP (prevention only, no lookback); Thomson Reuters ONESOURCE SUT AI (returns for large companies, not refunds); Saveware (Penn State student team, restaurant refunds, sells to businesses and tax firms).

**Channels:** Purdue MEP (724 companies/yr), Indiana Manufacturers Association, regional CPA firms without state-tax staff (refer or white-label).

**Risks and mitigations:**

| Risk | Mitigation |
|---|---|
| Overpayment rate unknown (archive killed this on economics) | Measure it in pilot scans |
| Claim can trigger a state audit | Check both directions before filing; offer voluntary disclosure for under-payments |
| Trust in students with tax data | State-tax CPA advisor, read-only access, power of attorney per claim |
| Late, lumpy revenue | Quarterly recovery and subscription |
| Incumbents adopt AI | Their cost structure doesn't fit $50–300K refunds |

**Tests before BDM:** 20 Indiana controller interviews (past reverse audits, fees, certificate management); 3–5 free scans reviewed by the CPA advisor — kill or reshape if the median three-year refund is under ~$50K for plants with 100+ employees; ask three regional CPA firms about referral or white-label; walk in with signed engagement letters, one filed claim, and measured refund per dollar of spend.

**Team gap:** a state-tax CPA advisor, ideally ex-Ryan or Big 4 in Indiana.

## Company 2 (backup): outsourced AI quality department for small auto and aerospace shops

- Monthly subscription (~$2–4K) for shops with no quality engineer: PPAP and first-article packages, 8D responses, customer-specific requirements, audit prep. Finished documents, not a tool.
- Backup because the document layer is crowded: GroundControl (YC 2025, ~$3M, 70+ facilities, ~1,000 inspection reports/month, moving into PPAP); QualityEngineer.ai (full PPAP suite); Omnex (PPAPValidator.AI, FMEA agent); 8D Pack; fractional quality managers; offshore PPAP preparers. Room only for shops too small to hire a quality engineer.
- Test: will 30–150 person Indiana suppliers to Subaru, Honda or Toyota pay ~$3K/month, with a veteran quality engineer signing off every package?
- Margin risk: service-heavy.

## Considered and dropped
- Self-funded claims audits: crowded with AI seedlings (Avelis YC pre-seed, CodaHx, Klaims, BenOsphere); ASO contracts can block contingency auditors; Kraft Heinz spent over a year trying to get its own claims data.
- Standalone property tax appeals: step four of Company 1.
- Insurer premium audits: slow buyers, low price per audit.
- Environmental filings: Encamp (~$42M) launched AI May 2026.

## Sources
[Arthiva](https://arthiva.ai/) · [Ryan $7B](https://www.bloomberg.com/news/articles/2026-01-14/neuberger-berman-invests-in-ryan-at-7-billion-valuation) · [Indiana DOR refunds](https://www.in.gov/dor/i-am-a/business-corp/sales-use-tax-refunds/) · [Indiana utility exemption](https://www.in.gov/dor/i-am-a/business-corp/utility-sales-tax-exemption/) · [ICS Tax](https://ics-tax.com/utility-sales-tax-exemption/indiana-utility-sales-tax-exemption/) · [Agile Consulting](https://www.salesandusetax.com/indiana-sales-tax-exemptions) · [Invoice volumes](https://invoicedataextraction.com/blog/manufacturer-reverse-sales-tax-audit) · [SEA 1 / HEA 1427](https://dmainc.com/news-and-insights/indiana-sb1-amendment-hea-1427/) · [Census SUSB 2022](https://www.census.gov/data/tables/2022/econ/susb/2022-susb-annual.html) · [AvaTax for AP](https://www.avalara.com/us/en/products/avatax-for-accounts-payable.html) · [TR ONESOURCE](https://www.thomsonreuters.com/en/press-releases/2026/january/thomson-reuters-launches-ai-tax-compliance-solution-that-saves-time-and-reduces-risk) · [Saveware](https://www.psu.edu/news/invent-penn-state/story/penn-state-student-startup-saveware-innovates-tax-refunds-ai) · [Michigan refunds](https://www.salestaxinstitute.com/resources/michigan-issues-guidance-on-sales-and-use-tax-refund-procedures) · [Ohio ORC 5739.07](https://codes.ohio.gov/ohio-revised-code/section-5739.07) · [GroundControl](https://aeroxplorer.com/articles/how-groundcontrol-is-racing-to-untangle-aerospaces-paperwork-bottleneck) · [QualityEngineer.ai](https://app.qualityengineer.ai/) · [8D Pack](https://8dpack.com/) · [Fractional Quality Partners](https://www.fractionalquality.com/) · [PPAP pricing](https://elsmar.com/elsmarqualityforum/threads/cost-of-ppap-what-is-the-average-cost-is-there-a-yearly-cost.6411/) · [CAA 2026 PBM audit](https://www.morganlewis.com/pubs/2026/02/consolidated-appropriations-act-of-2026-the-new-landscape-of-pbm-fiduciary-oversight) · [Avelis](https://www.ycombinator.com/companies/avelis-health) · [CodaHx](https://codahx.com/) · [ASO restrictions](https://www.topcoindirect.com/strategic-sourcing-blog/aso-agreements) · [Kraft Heinz v. Aetna](https://www.beckerspayer.com/payer/kraft-heinz-drops-claims-data-lawsuit-against-aetna/)
