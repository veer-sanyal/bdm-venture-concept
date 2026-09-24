Kita (YC W26) is pitching almost exactly this, so I treated it as this team. Its seed round and the $130M of loans it says it has processed show that lenders buy it. My concern is that each customer pays little, and a well-funded incumbent already sells the same product in these countries. I'm passing, with the scores below.

## Checking the claims against sources

- **"Thinly banked, the record lives in documents":** Mostly true in the Philippines, weaker elsewhere.
  - **Philippines:** 43% of adults have an e-money account and only 21% have a bank account (BSP/SWS survey, first quarter 2026). GCash shows only 90 days of history in the app and itself warns about AI-faked receipts, so lenders are handed screenshots and PDFs.
  - **Mexico:** 63% of adults have a formal account (ENIF 2024).
  - **Indonesia:** the financial inclusion index is 80.5% (SNLIK 2025).
- **"No banking APIs":** True for now, but it won't last forever.
  - **Mexico:** the rules for sharing bank transaction data are still unpublished eight years after the 2018 Fintech Law.
  - **Philippines:** BSP's open finance pilot is voluntary, and a bill that would require it (HB 9149) is pending.
  - **Indonesia:** the regulator limits P2P lending apps to the phone's camera, microphone and location. That pushes lenders toward documents.
- **The data gap is narrowing.** The Philippine credit bureau (CIC) held 79.1M borrower records by July 2026, and lenders pulled 28.2M reports in 2025, about half of them by online lenders. Bureau data shows repayment history, not income or cash flow, so documents still matter for sizing a loan.
- **The team's traction** (company and press claims): $4.5M seed led by BoxGroup in August 2026, with Tala's founder as an angel. It reports $130M of loan volume processed across the Philippines, Indonesia, Mexico and the US, and "70x faster" decisions. No customers are named and revenue is not disclosed.

## Who else serves this customer
- **Perfios** already sells a bank-statement analyzer in the Philippines and Indonesia, with tamper checks on PDF statements. Security Bank is a named Philippine customer. It is the closest incumbent for selling to banks.
- **Floowed** (Singapore) targets Southeast Asian lenders with messy documents. It claims it caught 3x more statement fraud at Alon Capital.
- **Other data sources compete for the same decision:** ADVANCE.AI with FinScore (telco scoring), Credolab, GCash's own GScore, and in Mexico Syntage (tax-authority e-invoice data from more than 150 institutions) and Palenca (income verification).
- **Does an incumbent own the data or the buying channel?** Not fully.
  - GCash owns e-wallet data but mainly uses it for its own lending partners.
  - CIC owns repayment history, but not income.
  - Perfios has a head start in banks. No one owns the channel to rural banks, financing companies and microfinance lenders.
  - In Mexico, Syntage's tax data largely replaces documents for formal small businesses, which weakens Mexico as a first market.

## 1. The strongest version
Start in the Philippines, then Indonesia, and focus on the document-heavy middle of the market. That means small-business and salary loans, auto loans, and rural, thrift and microfinance lenders, where loans are big enough to justify reviewing documents. Instant micro-loan apps don't ask for documents, so leave them out.

Lead with fraud detection on GCash/Maya and local bank statements and payslips, including fakes made with AI tools. Build a shared fraud network across lenders: fingerprints of tampering and templates, not credit data, which is easier to justify under the Data Privacy Act. Add underwriting decisions once that is in place.

Drop Mexican small-business lending and keep the US as a separate bet. The pitched moat, where models improve on each lender's own repayment outcomes, stays inside each lender and does not compound across customers. The shared fraud network would.

## 2. Ratings
| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | E-money accounts outnumber bank accounts 2:1 in the Philippines, GCash in-app history covers 90 days, and GCash itself warns about AI-faked receipts. |
| Value over today | 3 | Perfios already sells Philippine banks automated statement analysis with tamper flags. The gains that are left are e-wallet documents, phone photos and the outcome loop, and none of these has been shown in public. |
| Market size | 2 | Kita's $130M processed implies well under $1M in revenue at typical per-file fees. Indonesia's entire P2P loan book is only about $6B (IDR 98.5T). Annual contracts with small emerging-market lenders are small. |
| Risk (5 = low) | 2 | Open finance in the Philippines and Indonesia, bureau growth and extraction becoming a commodity (lenders can parse statements with general AI models) all shrink the product. The pooled fraud data may face legal limits. |

## 3. What would kill it, and the fastest test
**What kills it:** each lender pays too little for the business to reach venture scale. That happens if Perfios or an in-house parser built on general AI models is "good enough", and if open finance removes the need for documents in two to three years.

**Fastest test (about 3 weeks):** Take 10 document-heavy Philippine lenders, some using Perfios and some reviewing manually. Run a blind scoring of about 2,000 of each lender's past files where fraud and default outcomes are already known. Then ask each lender to sign an annual minimum of at least $50k.
- If fewer than 3 sign, pass.
- If 5 or more sign, and the extra fraud caught beyond what they catch today pays for the fee, the market-size score goes up and the call flips.

A caveat on method: the user asked for web-only research, so I didn't read the repo's METHOD.md or STATE.md. The search budget also ran out before I could confirm figures on document-fraud prevalence in these markets.

Sources:
- [YC: Kita](https://www.ycombinator.com/companies/industry/Lending)
- [Launch YC: Kita](https://www.ycombinator.com/launches/PEj-kita-turn-financial-documents-into-risk-signals-for-lenders)
- [startup.ph on Kita's seed round](https://www.startup.ph/a-filipino-founded-startup-just-convinced-talas-founder-to-bet-on-it-kita-raised-4-5-million-to-fix-the-credit-scoring-problem-tala-spent-a-decade-trying-to-solve/)
- [American Bazaar on Kita's seed round](https://americanbazaaronline.com/2026/08/24/open-for-hiring-kita-raises-4-5m-to-expand-ai-credit-assessment-486922/)
- [Kita about page](https://www.kita.ai/about)
- [PNA on BSP account ownership](https://www.pna.gov.ph/articles/1275692)
- [GCash: request transaction history](https://help.gcash.com/hc/en-us/articles/360034155433-How-to-request-transaction-history)
- [GCash warning on AI-generated fake receipts](https://mynt.com.ph/newsroom/gcash-warns-public-on-emerging-ai-generated-fake-receipts-scams-urges-users-to-always-check-transactions-tab)
- [Spot.ph on CIC borrower records](https://www.spot.ph/newsfeatures/money/cic-credit-report-a8218-20260826-bsc)
- [Open Banking Tracker on Mexico](https://www.openbankingtracker.com/blog/open-banking-in-mexico-eight-years-of-promise-still-waiting-on-the-regulations)
- [Open Banking Tracker on the Philippines](https://www.openbankingtracker.com/country/philippines)
- [INEGI ENIF 2024](https://www.inegi.org.mx/contenidos/saladeprensa/boletines/2025/enif/ENIF2024_RR.pdf)
- [OJK SNLIK 2025](https://ojk.go.id/id/berita-dan-kegiatan/siaran-pers/Pages/OJK-dan-BPS-Umumkan-Hasil-Survei-Nasional-Literasi-Dan-Inklusi-Keuangan-SNLIK-Tahun-2025.aspx)
- [KrASIA on OJK phone-data rules](https://kr-asia.com/indonesia-tightens-rules-for-online-lending-platforms)
- [Indonesia P2P outstanding loans](https://finance.yahoo.com/markets/crypto/articles/indonesias-p2p-lending-grows-25-101800209.html)
- [Perfios Philippines bank statement analyzer](https://perfios.ai/ph/products/bank-statement-analyser/)
- [Floowed on Southeast Asian document automation](https://www.floowed.com/insights/southeast-asia-fintech-document-automation)
- [ADVANCE.AI and FinScore partnership](https://www.finextra.com/pressarticle/91917/advance-ai-and-finscore-to-boost-alternative-credit-scoring-and-fraud-prevention-in-the-philippines)
- [Syntage](https://www.legalparadox.com/fintech/syntage)
- [Palenca funding](https://inforcapital.com/news/mexican-startup-palenca-raises-4-million/)

VERDICT: PASS