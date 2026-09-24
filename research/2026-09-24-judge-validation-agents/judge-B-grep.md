I checked the concept's claims against primary sources where they exist: Anthropic, the Federal Reserve and OCC, OFAC, LexisNexis, and the LMSYS paper. Funding and revenue figures come from press releases and trade press, and a few secondary sources (Sacra, Latka) are marked as such.

## Checking the claims

- **"Teams add headcount to keep up."** This holds for compliance. LexisNexis/Forrester put US and Canada financial-crime compliance spend at $61B a year, and labor is the largest cost line ([LexisNexis](https://risk.lexisnexis.com/about-us/press-room/press-release/20240221-true-cost-of-compliance-us-ca)). The global figure is $206B ([LexisNexis](https://risk.lexisnexis.com/about-us/press-room/press-release/20230926-global-financial-crime-compliance-costs)).
- **"A mistake is expensive."** This is partly true. OFAC (Treasury's sanctions enforcement office) collected about $265M in penalties in 2025 across 14 actions, but 81% of that came from one case, GVA Capital ([Sidley](https://www.sidley.com/en/insights/newsupdates/2026/02/five-key-takeaways-from-2025-us-sanctions-enforcement), [OFAC](https://ofac.treasury.gov/civil-penalties-and-enforcement-information/2025-enforcement-information)). The steady cost for most banks is exam findings and consent orders (formal corrective orders from a regulator), not OFAC fines.
- **"Send routine steps to cheaper models."** This works, but it is not proprietary. RouteLLM is open source and cut cost by 85% on MT-Bench, a chat benchmark, while keeping 95% of GPT-4's quality. On math (GSM8K) the saving was only 35% ([paper](https://arxiv.org/pdf/2406.18665), [LMSYS](https://www.lmsys.org/blog/2024-07-01-routellm/)). How much you save depends on the task, and anyone can copy the method.
- **"Sources and a decision trail on every answer."** Model vendors now include this. Anthropic's Managed Agents ship "a full audit log in the Claude Console where compliance and engineering teams can inspect every tool call and decision" ([Anthropic, May 5 2026](https://www.anthropic.com/news/finance-agents)).
- **Regulation.** SR 26-2 (April 17, 2026) replaced SR 11-7, the banking regulators' model-risk guidance. It explicitly leaves generative and agentic AI out of scope, and the agencies say a request for information on AI is coming ([Fed](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm), [OCC](https://www.occ.gov/news-issuances/bulletins/2026/bulletin-2026-13.html)). For now banks have no approved way to validate agents, so each bank decides for itself.
- **"Individuals buy usage credits."** This does not fit the customer. Bank analysts cannot put client or KYC data (know-your-customer identity records) into a tool they paid for on a personal card. The credit channel reaches hobbyists, not the buyer.

## Who already serves this customer

- **Model vendors have shipped this product.** Anthropic released 10 finance agent templates, including a KYC screener, statement auditor, earnings reviewer and market researcher. It added data connectors (Moody's, D&B, Third Bridge, Intralinks) and named customers such as Citadel, BNY, Mizuho and Carlyle ([Anthropic](https://www.anthropic.com/news/finance-agents)). OpenAI's Frontier agent platform has a BBVA pilot, and Fiserv announced a partnership to bring it to banks ([CNBC](https://www.cnbc.com/2026/02/05/open-ai-frontier-enterprise-customers.html), [PYMNTS](https://www.pymnts.com/artificial-intelligence-2/2026/fiserv-and-openai-bring-frontier-ai-to-banks/)). Microsoft sells Copilot Studio, with Agent 365 as its governance layer at $15 per user per month ([Microsoft](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/6-core-capabilities-to-scale-agent-adoption-in-2026/)).
- **Vertical players are funded and deployed.**
  - Rogo: $160M Series D at a $2B valuation, used by 35,000 professionals at 250 institutions ([PR Newswire](https://www.prnewswire.com/news-releases/rogo-raises-160m-series-d-to-scale-the-agentic-platform-for-finance-302756546.html)).
  - Hebbia: "hundreds of finance- and legal-specific Agents" in its product ([Hebbia](https://www.hebbia.com/blog/whats-new-april-disclosure-2026)), and about $30M ARR in 2024 according to Sacra ([Sacra](https://sacra.com/c/hebbia/)).
  - V7 Go: lets non-technical users build document agents ([V7](https://www.v7labs.com/finance)).
  - Bretton AI (formerly Greenlite): $95M raised for agents that handle AML, sanctions and KYC work, running at banks regulated by the OCC, FDIC and Fed, including Lead Bank and Coastal Community ([BankInfoSecurity](https://www.bankinfosecurity.com/bretton-raises-75m-to-use-ai-for-financial-crime-compliance-a-30747)).
  - Parcha: sanctions and PEP (politically exposed person) screening agents ([Parcha](https://www.parcha.ai/agents/aml-screening)).
  - Harvey: over $400M ARR in contract and legal work, including 50 asset managers (secondary sources: [TechCrunch](https://techcrunch.com/2026/02/09/harvey-reportedly-raising-at-11b-valuation-just-months-after-it-hit-8b/), [Latka](https://getlatka.com/companies/harvey)).
- **Incumbents own the data and the buying channel.** Data vendors own the data: LSEG World-Check and LexisNexis for sanctions, PEP and adverse-media records, and Bloomberg, FactSet and LSEG for market data. All three market-data vendors now sell their own agent workflows: Bloomberg's ASKB Workflows, FactSet with Google Cloud, and LSEG with Claude and Databricks ([Bloomberg](https://www.bloomberg.com/professional/insights/press-announcement/bloomberg-unveils-askb-roadmap-for-clients-to-augment-their-investment-process-with-agentic-ai/), [LSEG](https://www.lseg.com/en/insights/from-interoperability-to-agents-powering-financial-workflows-with-ai)). At smaller banks the core banking processors (Fiserv, FIS, Jack Henry) control the buying channel, and Fiserv has already signed with OpenAI. A new entrant owns neither.

## 1. The strongest version

The horizontal "describe any task, get an agent" platform is the weakest form of this idea. Anthropic, OpenAI and Microsoft sell that shape, bundled into contracts banks already have. I would narrow it to one job for one buyer.

That job is clearing sanctions and adverse-media alerts and running periodic KYB/KYC refreshes (re-checking business and customer files) for banks with $1–30B in assets and the sponsor banks behind fintechs (banks that hold accounts for fintech apps). The procedure-upload feature does real work here: the agent compiles the bank's own written alert-handling procedure. Pricing is per closed alert rather than per credit. The output is a case file an examiner accepts, showing each list hit, the evidence pulled, the rule applied from the bank's own procedure, and whether a person or the model made the call. While SR 26-2 leaves agents out of scope, the pitch is that the bank's procedure governs the agent, so the bank can defend it at exam. Routing to cheaper models is only the cost structure, not the pitch.

## 2. Ratings for that version

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | $61B a year in US and Canada financial-crime compliance, with labor the largest cost line (LexisNexis/Forrester). |
| Value over what customers use today | 2 | What these buyers use today already includes Bretton, Parcha and Anthropic's free KYC screener template. Bretton reports 90% faster alert handling and 95% fewer false positives at one customer, Meso, though that is a vendor claim. A newcomer's gain over those tools is small. |
| Market size | 4 | Labor is the largest part of a $61B North American spend ($206B globally), so even a small share is a venture-scale market. |
| Risk (5 = low) | 2 | The regulators are still writing their AI position (an RFI is promised after SR 26-2), incumbents own the data (World-Check, LexisNexis), Fiserv and OpenAI are working on the buying channel, and Bretton has a two-year and $95M head start with regulated banks. |

## 3. What kills it and the fastest test

**What kills it.** The same compliance lead can get "good enough" alert clearing in something they already pay for: their screening vendor (World-Check or LexisNexis adding agents), their core processor (Fiserv with OpenAI), or Claude or Copilot under an existing enterprise contract. If that happens, a standalone vendor never clears bank vendor-risk review (the bank's security and vendor vetting) for a job that small. The second way it dies is one missed true sanctions match in a pilot. A single miss ends the account and follows the company through reference calls.

**The fastest test.** Get 10 compliance heads at $1–10B banks or sponsor banks to hand over last quarter's closed sanctions and adverse-media alerts, anonymized. Run the agent blind against their own procedures. Measure two things: whether it misses any true matches (it must miss none) and how often it agrees with the analysts' decisions. Then ask each bank for a paid pilot at a per-alert price. If fewer than 3 of 10 sign within 30 days, or the typical objection is "we're getting this from our screening vendor or core processor," the idea is dead. This takes about four weeks and needs no platform, only one working agent.

## Why pass

The reshaped version is a real need in a large market. But the thing that would set it apart (turning a written procedure into an agent, cheap model routing, and cited audit trails) became standard in Anthropic's, OpenAI's and Microsoft's platforms during 2026. The one specialized space where it still wins, compliance alert clearing, already has a funded leader running at regulated banks. Incumbents own both the data and the buying channel. Crowding alone would not be enough to pass, but here nothing the company would own is hard to copy.

VERDICT: PASS
