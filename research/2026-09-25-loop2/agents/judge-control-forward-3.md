**Research note:** this is desk research only. It is not customer validation.

## What the evidence shows

**The pitch matches Forward (YC Fall 2026, useforward.co) almost exactly, so I treat Forward as this team.** YC describes it as "an AI platform that connects commercial debt advisors with mandate matching private credit funds." Its website shows the same product, the same "$20B AUM of funds" and "$100M+ in deals originated" figures, and "25+ hours saved per analyst weekly." It has offices in San Francisco and Sydney and is backed by YC, NextGen and Startmate. The founders come from Australian private credit (Kain Lawyers, Rixon Capital, Longreach).

**Checking the key claims:**
- **"$20B of funds use it": I could not verify it.** The logos on the site are small or mid-sized lenders, mostly in real estate and asset-backed credit:
  - Hudson Cove manages about $1.2B.
  - Namdar Capital is a New York bridge and rental-property lender.
  - iPartners is an Australian wholesale credit platform.
  - Arbitrium is an Australian special-situations fund making A$20–80M loans.
  
  The $20B is almost certainly the combined size of every fund that signed up, not software spend. Forward says it has "100+ funds onboarded" since May. That most likely means funds listed their lending criteria for free.
- **"$100M+ originated": no primary source.** Nothing says whether this means deals closed or deals sent to funds, and nothing shows fees earned.
- **Pricing is not disclosed.**

**Who else serves this customer:**
- **Termgrid** is software for running a debt financing process. It connects sponsors, lenders, advisors and law firms, and claims 1,500+ institutions, 25k users and more than $1T of financings. Clients include KKR, EQT, Apax and TA. It owns the workflow for private-equity-backed deals.
- **Axial** is a deal network for the lower middle market (smaller private companies, roughly under $250M of debt), with 10k+ deals a year. It lists 123 senior lenders and 40 junior-capital providers. Its own data says 70% of advisory firms in that market close 3 or fewer deals a year.
- **Finitive** runs a private credit marketplace with 900+ institutional investors.
- **CreditSME** in Australia has arranged A$500M+ through 125+ bank, non-bank and credit-fund lenders.
- **Fund-side AI tools** already parse documents and screen deals: Arc, Hebbia, BlueFlame, 73 Strings, and Ellis (a $10M seed round in July 2026).
- **Post-close loan monitoring** is crowded: 73 Strings, Chronograph, Cardo, Hypercore.
- **Lev is the cautionary case.** It raised about $170M for a commercial real estate debt marketplace, made two rounds of layoffs, then pivoted to selling CRM software to brokers.

**Does an incumbent own the data or the buying channel?**
- **Private-equity-backed deals: yes.** Most US middle-market direct lending comes from PE sponsors (Debtwire counts about 3,500 deals worth $369B in 2025). Termgrid owns that process, and DealCloud (Intapp) holds the funds' deal pipeline data.
- **US lower middle market: partly.** Axial owns advisor distribution there.
- **Non-sponsored deals: no.** These are companies without a PE owner, placed by independent commercial debt brokers with real estate, asset-backed and mid-market lenders. Nobody owns this channel; it runs on email and personal relationships. It is also where Forward's actual logos sit.

## 1. Strongest version

Build the standard deal-submission network for **non-sponsored credit placed through independent debt advisors**. Start in Australia, then move to US real estate bridge and asset-backed lenders.
- **The market is sizeable.** Australian private credit is about A$200B (ASIC Report 814, Sept 2025).
- **Timing helps.** ASIC is pressing that market on transparency and conflicts of interest, which favours standardized deal packs.

**How it works:**
- **Advisors get the tool free.** It turns a pile of borrower documents into a checked, standard credit paper with a proposed structure. With one click it goes to funds whose criteria match, and the advisor tracks every fund's response in one place.
- **Funds pay a subscription** for clean inbound deals that are already screened against their mandate.
- **A share of the fee on closed deals comes later.**

**The lasting asset** is outcome data: which fund bids on which deal, and at what price and terms. That becomes pricing benchmarks, and it gets harder to copy with every deal. Post-close monitoring should wait, because that space is crowded and it does not help win the network.

## 2. Ratings (total 12/20)

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Advisors are a long tail (70% of lower-middle-market advisory firms close 3 or fewer deals a year, per Axial) and shop deals by hand. Forward reports 100+ funds signing up in about 4 months. |
| Value over today | 3 | Fund-side parsing is already sold by Arc, Hebbia and BlueFlame. The new value is the matching network, and that only shows once funds respond. |
| Market size | 3 | There are about 3,000 private debt managers (Preqin coverage). Fund software alone is a few hundred million dollars. A cut of closed-deal fees on non-sponsored volume is larger, but it means sharing economics with advisors. |
| Risk | 2 | Debt marketplaces have a poor record (Lev pivoted after about $170M). There is adverse selection: widely shopped deals tend to be the ones insiders already turned down. The headline traction figures are not verified. |

## 3. What would kill it

Funds treat the routed deals as low-quality noise. They screen them but rarely issue terms, so advisors stop submitting and nobody pays.

**Fastest test (2–3 weeks):** send the next 20 live advisor deals through the platform and measure two things:
- How many produce an indicative term sheet from a matched fund within 14 days.
- Whether at least 3 of the named funds will sign a paid agreement, either a subscription or a fee on closed deals.

Weak signals would be fewer than 20% of deals getting terms, or no fund willing to pay. That would mean this is a free listing board, not a network.

VERDICT: BACK

Sources: [YC – Forward](https://www.ycombinator.com/companies/useforward), [useforward.co](https://www.useforward.co/), [Forward company page](https://www.useforward.co/company), [Termgrid](https://app.termgrid.com/platform-overview/), [Axial](https://www.axial.net/), [Finitive](https://www.finitive.com/), [CreditSME](https://www.creditsme.com.au/), [Arc](https://www.joinarc.com/ai/private-credit), [Ellis seed – TechCrunch](https://techcrunch.com/2026/07/31/repeat-founder-ryan-williams-raises-10m-seed-for-an-ai-startup-for-private-credit-managers/), [Lev pivot – Thesis Driven](https://www.thesisdriven.com/letters/deep-dive-lev/), [Lev layoffs – The Real Deal](https://therealdeal.com/new-york/2023/05/01/cre-finance-platform-lev-lays-off-more-staff/), [ASIC Report 814](https://download.asic.gov.au/media/z2tnnasb/rep814-published-22-september-2025.pdf), [Hudson Cove AUM – FINTRX](https://fintrx.com/firms/firm/hudson-cove-capital-management-llc-283128), [Arbitrium](https://www.acpartners.com.au/), [Namdar Capital](https://www.namdarcapital.com/), [Debtwire 2025 direct lending](https://ionanalytics.com/insights/debtwire/direct-lending-volumes-climb-as-refinancing-demand-drives-activity-2025-us-direct-lender-rankings/), [Preqin private credit data](https://www.preqin.com/data/private-credit)
