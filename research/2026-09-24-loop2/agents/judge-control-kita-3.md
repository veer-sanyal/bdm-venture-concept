I found a company already making this exact pitch: **Kita** (YC W26). It uses the same wording: "application completion, document verification, and underwriting," "localized risk signals," and "links document signals to repayment outcomes." Following your rule, I treat Kita as this team. Kita raised a $4.5M seed led by BoxGroup in August 2026, with YC, Golden Gate, BEENEXT and Kaya Founders, plus the founder of Tala (a large emerging-market lending app) as an angel. Named customers include Cashalo, Beloz by Amiloz, Trusting Social and TRBank. This is all desk research. None of it counts as customer validation.

## Checking the key claims

| Claim | What the sources show |
|---|---|
| Borrowers are thinly banked | **True (Philippines).** The central bank's 2025 survey found 50% of adults hold any formal account, down from 56% in 2021. Bank-account ownership is 23% and e-money 36%. |
| Lenders can't pull history through banking APIs | **Mostly true.** Philippines: the open-finance bill HB 9149 only left committee in May 2026, with rollout 2027 at the earliest. Mexico: rules for sharing transaction data are still unpublished after 8 years, and a lawsuit was filed in January 2026 over the delay. Indonesia: online lenders only became required to report to the official credit database (SLIK) in July 2025, and fintechs lean on private credit bureaus. **Exception:** in Mexico, tax data (SAT invoices) and social-security employment data (IMSS) can already be pulled by API through Belvo, so documents are not the only route there. |
| Manual review is slow and costly | Plausible, but labor in Manila, Jakarta and Mexico City is cheap. The value comes from speed and fraud caught more than headcount saved. The "70x faster" figure is unverified, and Kita's homepage still shows placeholder numbers ("0x faster", "0.0% accuracy"). |
| Risk signals improve underwriting | **Partly shown, by Kita itself.** One backtest on 8,000 files from a single microlender: +2.4 Gini points over the bureau score using all documents, +7.0 Gini (+0.036 AUC) on rich financial documents. That is real but modest lift, from one lender whose default rates ran from 22% to 49% by decile. |
| Traction | "$130M loan volume processed." The one public case study, TRBank (a rural bank), covers 5,100 loan folders worth ₱8.77B, about US$150M. My inference is that most of the headline volume is one bank's back-file digitization, not live underwriting flow. |

## Who else serves this customer

- **Perfios** is the main threat. It is India's category leader with ₹669.5 Cr (about $78M) FY25 revenue, is profitable and valued at $1B. It has local bank-statement analysers for the Philippines and Indonesia, a named Philippine bank customer (Security Bank), and built-in tamper checks on PDF statements.
- **Boost VerifyIQ** (Philippine SME documents: BDO, BPI, GCash statements, tax forms), **Floowed** (Singapore, Southeast Asia lending documents), **ADVANCE.AI** (OCR and anti-fraud in the Philippines, Indonesia and Mexico).
- **Inscribe, Ocrolus and Uptiq** do document fraud in the US.
- Adjacent data sources: **FinScore** (Philippine telco-based scores), **Belvo** (Mexico tax and employment data), **Brankas** and **Brick** (Southeast Asian bank-data APIs).

**Does an incumbent own the data or the buying channel?** No one owns the documents themselves, because borrowers hand them to lenders. But the data behind them is owned by others:
- GCash, the main Philippine e-wallet, scores its own users (GScore) and lends to them directly without documents.
- Mexico's tax authority is already reachable by API.
- Perfios and the credit bureaus (CRIF, CIBI, TransUnion) already hold the vendor slot at banks.

The channel is open with mid-tier lenders but contested at large banks.

## 1. The strongest version

Narrow it to a **cross-lender document-fraud and trust layer for mid-ticket lenders** in markets that still run on documents: small-business lenders, rural and thrift banks, Mexican non-bank lenders (SOFOMs; there are over 2,100), and salary lenders where a file is worth $2–10 to check.

- **Lead with fraud.** It is the one output where ROI is measurable and not undercut by cheap labor.
- **Build a fraud network across lenders** (for example, the same doctored GCash template appearing at several lenders). This beats "models improve with each lender's decisions," which stays siloed per lender under data-privacy law.
- **Pool repayment outcomes through a bureau partner.**
- **Don't care where the data comes from:** take API data when open finance arrives, and keep documents for informal income (payslips from informal employers, invoices, utility bills).
- **Sell through loan-origination systems and bureaus.** Drop the seven-product loan-platform sprawl.

## 2. Ratings

- **Customer need: 4.** 50% account ownership and stalled open finance in all three markets mean documents stay the main input for years.
- **Value over what customers use today: 3.** Today's alternatives are cheap manual review plus Perfios. Kita's own backtest adds only +2.4 Gini over the bureau score on typical documents.
- **Market size: 2.** Perfios, the leader in India (a much larger document-lending market), makes about $78M revenue after 15 years across 18 countries. Per-file pricing in low-wage markets caps what each customer pays.
- **Risk: 2 (high).** Perfios already sells the same thing to the same banks, vision-language models are making extraction a commodity, and open finance plus e-wallet lending will shrink the document-reliant segment from 2027 on.

## 3. What would kill it, and the fastest test

**What would kill it:** lenders won't pay per-file prices that add up to venture scale. That happens if fraud caught and risk lift are worth less than what cheap manual review plus Perfios already give them, which leaves only commodity extraction to sell.

**Fastest test (2–4 weeks):** run a **back-book fraud audit**.
1. Take 1,000–2,000 already-disbursed files from 3 target mid-ticket lenders.
2. Score them for tampering and join the scores to actual repayment.
3. Agree up front that a positive result converts to a paid contract.

Kill the idea if:
- flagged files don't default at least 2x more than unflagged files, or
- losses the tool would have prevented per 1,000 files come in under the proposed annual price, or
- fewer than 2 of the 3 lenders sign a paid contract of at least roughly $50k a year.

The problem is real, and Perfios proves the category can produce a $1B company. But this version sits in thinner, lower-priced markets, faces a well-funded incumbent already at the same banks, sells a commoditizing core, and has shown only modest risk lift. Until the paid back-book test shows fraud ROI, I would not back it.

Sources:
- [Kita site](https://www.kita.ai/), [About](https://www.kita.ai/about), [Document Risk Score](https://www.kita.ai/document-risk-score), [Case studies](https://www.kita.ai/case-studies), [Seed post](https://www.kita.ai/blog/kita-seed-round)
- [Launch HN: Kita](https://news.ycombinator.com/item?id=47417335), [Launch YC](https://www.ycombinator.com/launches/PEj-kita-turn-financial-documents-into-risk-signals-for-lenders), [startup.ph on seed](https://www.startup.ph/a-filipino-founded-startup-just-convinced-talas-founder-to-bet-on-it-kita-raised-4-5-million-to-fix-the-credit-scoring-problem-tala-spent-a-decade-trying-to-solve/)
- [BusinessWorld: BSP 2025 inclusion survey](https://www.bworldonline.com/banking-finance/2026/04/17/743500/financial-account-ownership-among-filipinos-at-50-bsp/), [Inquirer](https://business.inquirer.net/585729/filipino-financial-account-ownership-slips)
- [BSP Open Finance](https://www.bsp.gov.ph/Pages/InclusiveFinance/Open%20Finance/Open%20Finance.aspx), [Open Banking Tracker PH](https://www.openbankingtracker.com/regulation/philippines-open-finance)
- [Open Banking Tracker: Mexico still waiting](https://www.openbankingtracker.com/blog/open-banking-in-mexico-eight-years-of-promise-still-waiting-on-the-regulations), [FinTech Futures: CNBV legal action](https://www.fintechfutures.com/regulatory-actions/mexico-s-cnbv-reportedly-facing-legal-action-over-delays-publishing-open-finance-rules), [LatAm Fintech: CNBV first rules](https://www.latamfintech.co/articles/cnbv-emite-las-primeras-reglas-y-estandares-de-open-finance-en-mexico)
- [Belvo Fiscal Mexico](https://developers.belvo.com/products/fiscal_mexico/fiscal-mexico-introduction), [Clip/Belvo](https://www.fintechfutures.com/commercial-sme-lending/mexican-fintech-clip-integrates-belvo-employment-data-tools)
- [Indonesia credit data primer](https://nategunawan.substack.com/p/do-you-know-your-credit-score-a-primer), [Yahoo: Indonesia P2P growth](https://finance.yahoo.com/markets/crypto/articles/indonesias-p2p-lending-grows-25-101800209.html)
- [Perfios PH BSA](https://perfios.ai/ph/products/bank-statement-analyser/), [Perfios ID BSA](https://perfios.ai/id/products/bank-statement-analyser/), [Inc42: Perfios FY25](https://inc42.com/buzz/perfios-fy25-profit-soars-46-to-%E2%82%B9104-cr-revenue-crosses-%E2%82%B9700-cr/)
- [Boost VerifyIQ](https://www.boostkh.com/2026/09/18/how-boost-uses-ai-to-unlock-credit-for-philippine-small-businesses/), [Floowed](https://www.floowed.com/insights/southeast-asia-fintech-document-automation), [ADVANCE.AI OCR](https://www.advance.ai/en/advance-ocr?country_num=1&indust_num=22), [Inscribe](https://www.inscribe.ai/industries/lenders), [FinScore](https://www.finscore.ph/), [Brankas Statement](https://blog.brankas.com/brankas-statement-on-demand-financial-transaction-data)
- [GCash GLoan](https://gcash.com/services/gloan), [GScore](https://www.factfin.com/blog/gcash-and-the-power-of-gscore-data-science-in-loan-governance), [GCash AI fake receipts warning](https://mynt.com.ph/newsroom/gcash-warns-public-on-emerging-ai-generated-fake-receipts-scams-urges-users-to-always-check-transactions-tab)
- [SOFOM count](https://sofomes.com/lista-sofomes-mexico)

VERDICT: PASS