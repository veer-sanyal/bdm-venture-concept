I'd pass. The problem is real and getting worse, but a specialist incumbent already owns this customer's buying channel, and the buyer's cheapest answer to a flood of disputes is to delete the entry rather than defend it.

## Claims checked against sources

- **"CFPB complaints doubled to 6.6M in 2025": true, but misleading as used.** 6.6M in 2025 against 3.2M in 2024, and 88% (about 5.8M) were about credit reporting. Most of these complaints are against the credit bureaus, not lenders or collectors. Complaints against creditors and debt collectors went from about 159k to about 302k. The CFPB blames credit repair firms and AI tools for flooding it with "duplicative and spurious submissions." It now sends consumers to the bureaus first and has added identity checks, which could shrink the flood. ([Orrick](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/), [ABA](https://bankingjournal.aba.com/2026/04/cfpb-received-6-6m-consumer-complaints-in-2025/), [WebRecon Dec 2025](https://webrecon.com/litigation-statistics/webrecon-dec-2025-stats-year-in-review))
- **FCRA lawsuits up 37% in 2025, then 45% more: true.** 2025 was up 37.4% (6,092 to 8,369 suits). 2026 is up 44.6% through July, with 1,134 suits in July alone. I could not find how many of these suits target lenders and collectors rather than the bureaus. ([Shipkevich/WebRecon July 2026](https://www.shipkevich.com/july-2026-litigation-update-fcra-filings-continue-to-climb-as-other-consumer-litigation-pulls-back-ytd-figures-still-high/))
- **"A thin investigation record loses suits": plausible, not verified.** It fits case law I know from memory: Johnson v. MBNA (4th Cir. 2004) held that a lender's investigation must be reasonable, not cursory, and Hinkle v. Midland (11th Cir. 2016) applied this to debt buyers checking only their own records. I did not check these cases against primary sources in this session.
- **The bureaus' system (e-OSCAR):** the bureaus own it. It charges $0.34 per transaction and now offers an API for automated intake and responses. ([e-OSCAR](https://www.e-oscar.org/services-by-e-oscar))

## Who else serves this customer

- **Provana, which bought Palinode's Sonnet in Feb 2025.** Sonnet automates bureau disputes and disputes sent straight to the lender. It keeps a 7-year investigation record as proof of "reasonable investigation." It is built into collection and lending software (DAKCS, Nortridge). Provana sells it with outsourced dispute staff to collection agencies, and one case study claims response time fell from 28 to 7 days. **This incumbent owns the buying channel.** It is the closest match, but it is an established incumbent, not this startup's pitch. Its gap is AI that matches evidence and drafts the response. ([Provana](https://provana.com/provana-acquires-palinode-further-strengthening-dispute-solutions-for-financial-institutions/), [Nortridge](https://nortridge.com/press-releases/nortridge-software-launches-integration-of-sonnet-by-palinode-to-provide-lenders-with-tool-to-remain-compliant-amidst-credit-report-disputes/))
- **Bridgeforce Data Solutions** has dispute oversight products and an AI Resolution Engine in pilot. ([Bridgeforce](https://bridgeforcedatasolutions.com/what-is-e-oscar/))
- **The account data sits in the collection software:** C&R Debt Manager already has dispute management and verification letters, and Collect! and DAKCS are in this market too. Offshore dispute outsourcing competes on price. ([C&R](https://www.crsoftware.com/industries/debt-buyers))
- **Size of the customer base:** a Feb 2025 furnisher survey (search snippet only) says 53% handle 250 or fewer disputes a month and 34% handle more than 1,000. The 5k–50k-a-month band is probably a few hundred firms; that count is my inference.

## 1. The strongest version

Narrow it to debt buyers and large third-party collectors. Collection accounts are the most disputed, and debt buyers usually lack the original paperwork and proof of ownership chain.

Sell a defensible investigation file, not labor savings:
- AI matches each dispute to the paperwork the buyer actually holds, or flags that it's missing.
- It recommends verify, correct or delete, including the cost of defending against the cost of deleting.
- For disputes sent straight to the lender, it identifies the ones that don't need investigating: those from credit repair firms and frivolous ones. From memory, Reg V 1022.43 allows both; not checked in this session.
- It builds a litigation-ready file on every dispute.

Sell it through FCRA defense firms and as an add-on to Sonnet, Debt Manager, DAKCS and similar systems, not against them. Price per dispute, with a premium for the litigation file.

## 2. Ratings

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | FCRA suits up 44.6% so far in 2026, and complaints against creditors and collectors roughly doubled to about 302k. |
| Value over current tools | 2 | Sonnet/Provana already automate intake and keep investigation records, e-OSCAR has an API, and deleting costs almost nothing. |
| Market size | 2 | A few hundred firms at 5k–50k disputes a month × $1–3 is roughly $100–250M of total spend, and the bureaus' own fee of $0.34 per transaction keeps prices low. |
| Risk (5 = low) | 2 | Four risks: the bureaus and CFPB are filtering spurious volume; incumbents own the channel; customers can simply delete; and an AI-backed "verify" that turns out wrong becomes the evidence a plaintiff sues on. |

## 3. What would kill it, and the fastest test

**Kill:** customers answer the flood by deleting the entry or stopping credit reporting altogether, not by verifying. Then no one pays $1–3 to defend an account, and whatever is left gets bought as a Provana add-on.

**Fastest test:** in one week, reach 10 compliance heads at debt buyers or collectors in the 5k–50k band. Ask three things:
1. What share of disputes do you delete without investigating?
2. What does each dispute cost you all-in today?
3. Will you sign a paid pilot at $2 per dispute for litigation-ready files?

Kill it if most of them delete more than half their disputes, or none will sign. These interviews are real customer validation; everything above is desk research.

I ran out of web searches partway through. That left the FCRA split between lenders and bureaus, Provana's pricing, and the CFPB's full bureau complaint report unchecked (that PDF wouldn't parse).

VERDICT: PASS
