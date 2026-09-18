# EVIDENCE - agent-economy lane, demand tiers

**Gathered 2026-09-11 by blind evidence agents. Every load-bearing figure FETCHED, not snippet.**
Candidates: `CANDIDATES-AGENT-ECONOMY.md`. Predictions: `predictions/2026-09-11-agentic-web-lane.md`.

---

## ⚠ THE FINDING THAT GOVERNS THIS WHOLE LANE

**Every AI-specific law has a huge headline penalty and ZERO fines actually issued.**
Every large enforcement ledger that exists is the PRE-AI analogue.

| Law | Penalty | In force | Fines actually issued |
|---|---|---|---|
| EU AI Act Art. 99 | €35M / 7% turnover | Penalties since 2025-08-02 | **NONE FOUND** |
| Texas TRAIGA HB 149 | $80k-$200k uncurable; **$2k-$40k PER DAY** continuing | **2026-01-01, real** | **NONE FOUND** |
| California SB 53 / TFAIA | $1M per violation | 2026-01-01, frontier devs only | **NONE FOUND** |
| NYC Local Law 144 | $500 first, $1,500 subsequent | 2023-07-05 | **NONE DISCLOSED** |
| Colorado SB 24-205 | ~~$20,000~~ | **REPEALED.** Replaced by SB 26-189, eff. 2027-01-01 | N/A - see do-not-cite |

**And the one counted enforcement ledger counts almost nothing.** NY State Comptroller audit 2024-N-6
(published 2025-12-02, scope Jul 2023 - Jun 2025) on DCWP's enforcement of the first US AI-audit mandate:
> "Despite receiving only two AEDT complaints during the audit's scope..."
> "DCWP surveyed websites and bias audits of 32 companies and identified just a single issue of non-compliance."
> The audit team reviewing the same 32 found **"at least 17 instances of potential non-compliance."**
Two complaints, one finding, no disclosed fines, in 24 months. **The obligation exists; enforcement does not.**

**The biggest demand trigger moved 16 months out.** EU AI Act Annex III high-risk obligations deferred
from 2026-08-02 to **2027-12-02** (Annex I to 2028-08-02). Practitioner artifacts dated Feb-Mar 2026 still
cite the dead 8/2026 deadline.

**And for most high-risk AI there is no audit invoice at all.** EU AI Act Art. 43, fetched: Annex III
points 2-8 (critical infrastructure, education, employment, essential services, law enforcement,
migration, justice) use internal control "**which does not provide for the involvement of a notified
body**". Only Point 1 (biometrics) can require one. **7 of 8 high-risk categories self-assess.**

---

## D1 - PUBLISHED PRICE FOR THE MISTAKE

**The canonical agent-error award is tiny.** *Moffatt v. Air Canada*: **$812.02 total** ($650.88 + $36.14
interest + $125 fees). Liability holding, fetched: *"It should be obvious to Air Canada that it is
responsible for all the information on its website."* Primary decision unreachable (403 everywhere).

**The best D1 found, and it cuts both ways.** Google AI VRP: **up to $30,000 for a "rogue action"**;
qualifying categories "rogue actions, sensitive data exfiltration, phishing enablement and model theft."
And explicitly: *"While prompt injections, jailbreaks and alignment issues remain issues for AI products,
these faults will be out of scope of the AI VRP."* **Deployers will price the agent doing the wrong
thing, and refuse to price the input that causes it.** (Google's own rules page 404s; trade press fetch.)

Others: HackerOne AI bug bounty minimums Critical $5,000 / High $2,000 / Medium $750 / Low $200 (page
2026-02-25). Anthropic model safety bounty "up to $35,000 per novel, universal jailbreak" (jailbreaks
only, technical vulns excluded). FTC v. DoNotPay **$193,000** - but priced as deceptive claims, not as a
wrong agent action.

**The pre-AI analogue dwarfs all of it.** SEC off-channel communications recordkeeping: *"more than 100
firms and over $2 billion in penalties."* FINRA Notice 24-09 extends existing rules to Gen AI but, fetched,
**does not mention Rule 4511 or AI-generated records.** The books-and-records hook for AI output is
inferred by practitioners, not stated by the regulator.

---

## D2 - PUBLISHED PRICE FOR THE WORSE SUBSTITUTE. This is the strongest tier in the lane.

**AI red-teaming, vendor list price (page 2026-04-07), and the SHAPE is the finding:**
simple chatbot $8K-$15K · RAG pipeline $15K-$35K · **tool-using agent $25K-$60K** · **multi-agent
$50K-$150K+** · **MCP-connected ecosystem $60K-$150K+**. Continuous subscription $5K-$20K/mo.
Price roughly doubles at each step toward agency.

**ISO/IEC 42001 certification, year one $91K-$217K** (two sources disagree 2-4x; second gives
$85K-$150K small, $180K-$320K mid, $350K-$650K large). Surveillance years 2-3 $8K-$22K/yr.
Claimed procurement pull: *"72% of enterprise buyers screen for ISO 42001 before the first RFP round"*
(single vendor source, NOT VERIFIED).

**e-Discovery, the priced substitute for reconstructing agent behavior** (Winter 2026 survey, n=53):
39.6% pay $25-$75/GB processing; 52.8% pay $100-$200/hr project management.

**EMPTY, and this matters: nobody publishes a bias-audit price.** Checked nycbiasaudit.com, warden-ai.com,
babl.ai (and babl.ai/pricing 404). All gate pricing behind contact-sales. **No public price exists for
the most-cited AI audit obligation in the US.** No CB publishes an ISO 42001 rate card either.

---

## D4 - COUNTABLE LEDGERS

**MCP has a real, dated, CVE-numbered defect ledger - the hardest technical evidence in the lane.**
vulnerablemcp.info (fetched 2026-09-11): **50 vulnerabilities, 13 Critical**, 32 contributing researchers.
Other tallies 14 / 30+ / 40+ depending on window. "200,000 servers" RCE-exposed; "492 MCP servers exposed
to the public internet with zero auth/encryption" (Trend Micro, Jul 2025); "53% rely on static API
keys/PATs; only 8.5% use OAuth" across 5,200+ servers (Astrix, Oct 2025). 14 dated incidents Apr 2025 -
Apr 2026 with CVEs.

**⚠ OWASP's own incident corpus demotes prompt injection.** 7,714 incidents analyzed, 6,639 classified.
Ranked on the public incident record alone **prompt injection falls to #12**; OWASP holds it at #1 on
expert judgment. Expert-vs-record agreement: **Cohen's kappa 0.20.** What the record actually supports is
**Excessive Agency / agentic execution.** Lots of talk, comparatively few counted losses.

IBM Cost of a Data Breach 2026 (IBM's own page): global average **$4.99M**; AI model inversion attack
**$6M**; 56% increase in AI-driven attacks.

Vendor surveys (LOW confidence, commercially interested, disagree by 23 points): 88% vs 65% of orgs
reporting an agent-caused incident. Directional only: "41% unintended actions in business processes,"
"35% financial losses," "60% can't terminate a misbehaving AI agent."

---

## D5 - COUNTED COMPLAINT

- HN `"prompt injection"` stories: **515 since Jan 2025, 332 in 2026 alone.** `MCP security`: 498.
  Top: "Google Antigravity exfiltrates data via indirect prompt injection" 768pts/215 comments (2025-11-25).
- HN `AI agent deleted database`: **43 stories**; lead thread 860pts/**1,032 comments** (2026-04-26,
  PocketOS: production database and backups deleted in nine seconds, three months of data lost).
  **Dollar cost: not disclosed.**
- GitHub, agent + audit trail + compliance issues since 2025-09-01: 899 (upper bound, bot-polluted).
  Two verified genuine: microsoft/semantic-kernel #13957 (71 comments), crewAIInc/crewAI #5541.

**⚠ THE CROWDING TELL, and it is the single most important D5 finding.** HN query `"AI agent" audit log
compliance`: only **10 stories**, and **7 of the 10 are Show-HN product launches** (traceprompt, CoSig,
OnGarde, Conduit, air-blackbox, tansive, halo-record). **On this topic HN is founders shipping tools, not
practitioners complaining.** That is a weak demand signal and a strong crowding signal.

---

## THE OTHER VERIFIED NEGATIVE: agent payments have no priced rule

Fetched Visa Trusted Agent Protocol developer page, Stripe ACP docs, agenticcommerce.dev.
**None contains liability, chargeback or refund allocation language.** Per a fetched dispute-industry
analysis, no rule assigns fault among consumer, AI provider and merchant; the AI provider "currently faces
no direct chargeback liability" and the merchant bears "full chargeback cost, fees, and penalties."
**As of today there is no published binding agentic chargeback rule with a price on it.** Merchants absorb
it silently under existing card-absent-fraud codes. That is the ABSORB kill shape, pre-emptively.

---

## NOT VERIFIED / UNRUN - do not treat as absent

Reddit entirely (fetches blocked in the agent environment). EUR-Lex authoritative Art. 99/113 text
(returned truncated recitals; Art. 99 figures rest on one secondary rendering). Digital Omnibus adoption
dates. NYC Admin Code § 20-872 primary text (403/404). OpenAI and 0DIN bounty tables (403 / no table).
Google's own AI VRP rules page (404). HackerOne's "540% surge" source (404). Illinois HB 3773.
Armilla/Lloyd's and AIUC agent-insurance pricing. Digital forensics day rates. **D3 (salaries) was never
run in this pass** - the agent that owned it stalled. A re-dispatched seat-count agent is running.

---

# ADDENDUM - agent readiness (a) vs bot-traffic economics (c). Added 2026-09-11.

**These two areas look adjacent and their evidence is opposite. This is the most useful contrast in the file.**

## (a) "My site is wrong for agents" - NO D1 AT ALL

- **D1 EMPTY, established by looking.** No counterparty anywhere publishes a penalty, deduction or fee
  charged to a merchant *because* its site failed an agent. What exists is liability ALLOCATION language,
  never a price.
- **D2 is historical, not live.** ChatGPT Instant Checkout charged merchants "a 4% fee on sales made
  through ChatGPT checkout, on top of the fees charged by Shopify" (~$7.20 of platform+processing on a
  $100 order). **Instant Checkout was retired March 2026.** OpenAI's own commerce docs carry no fee
  information; the announcement page 403s.
- **D4 measures FOREGONE UPSIDE, not a bill.** Adobe Analytics: AI-referred retail traffic "grew 138%
  year over year in May 2026", "1,324% since October 2024", converts "54% better", and "30 to 40% of
  content is still overlooked or uncaptured by AI." Nobody is charged; somebody just fails to win.
- **D5 exists and is real but thin.** 7 distinct dated HN posts in a ~6-month 2026 window on site
  unreadability, e.g. "Only 8.9% of sites block AI crawlers, but 94.8% are never cited in AI answers"
  (2026-08-02, 61 comments) and "A quarter of YC Fall 2025 startups are blank pages to AI crawlers."

**Read plainly: the pain is real, nobody is billed for it, and Cloudflare gives the diagnosis away free
(isitagentready.com). That is no-D1 plus rule 6. This is the weakest area in the lane.**

## (c) Bot-traffic economics - the ONLY area with D1, D2, a real dollar ledger AND dense complaint

- **D1, published, live: Cloudflare Pay Per Crawl. "The minimum price is $0.001 USD per crawl."**
  Mechanism: `HTTP 402 Payment Required` with pricing; "Cloudflare acts as the Merchant of Record."
  **Paid BY the agent operator TO the site owner.** Cloudflare publishes no take rate anywhere (EMPTY,
  checked three doc pages plus the changelog). Still private beta.
- **D1 second instance: TollBit**, rate hierarchy "bot -> page -> keyword -> time -> subdirectories",
  examples "$0.001 per page" and "$0.005" for specialized directories, and "TollBit doesn't take a
  percentage of your rates or revenue share." Its own fee to AI customers is unpublished.
- **D2, and the shape is the finding: AWS WAF Bot Control.** "$10.00 per month per web ACL"; common bot
  detection "$1.00/million"; **targeted bot detection "$10.00/million" - ten times the price.** AI agents
  are by construction the targeted tier. Fraud Control tiers run "$1,000/million down to $50/million."
- **D4, the only clean DOLLAR ledger found in the entire lane - Read the Docs, operator's own bill:**
  > "One crawler downloaded 73 TB of zipped HTML files in May 2024, with almost 10 TB in a single day."
  > **"This cost us over $5,000 in bandwidth charges, and we had to block the crawler."**
  > "By blocking these crawlers, bandwidth for our downloaded files has decreased by 75%."
  ⚠ Dated 2024-07-25, the oldest evidence in the set.
- **D4, and this is the number that makes the economics bite (Cloudflare, own network):** *"Training
  traffic, responsible for nearly 80% of the crawling from AI bots"*; user-action purposes "less than 5%".
  **~80% of the load produces no referral and no transaction.** Crawl-to-refer: Anthropic **70,900:1**,
  Mistral 0.1:1 (window 2025-06-19 to 06-26).
- **D4 corroboration:** Wikimedia, "bandwidth used for downloading multimedia content grow by 50%" since
  Jan 2024 and "at least 65% of this resource-consuming traffic... is coming from bots" against 35% of
  pageviews. **No dollar figure - the Foundation never prices it.** Imperva: automated traffic "more than
  53% of all web traffic in 2025."
- **D5 is the strongest in the lane, and it is OUTAGES, not annoyance.** 11 distinct operators across 11
  sites, Jan 2025 - Sep 2026: "We can't have nice things because of AI scrapers" (465pts/266 comments),
  "Gentoo bugzilla closed due AI bot scraper overload", "Due to relentless AI scrapers notabug.org is
  currently down", "LWN sluggish due to DDoS onslaughts from AI-scraper bots", GNOME, weirdgloop wikis.

**⚠ AND THE FREE COMPETITOR IS ALREADY THERE, AT SCALE.** `TecharoHQ/anubis`, a proof-of-work wall built
for exactly this: **22,364 stars, 716 forks**, created 2025-03-17, still pushed 2026-09-10. Eighteen
months, built by an individual, given away. That is rule 6 shape one, from the community rather than a
vendor. Plus Cloudflare and TollBit hold the paid rail.

## What the contrast says

**The money in the agent economy is currently flowing on the CRAWL side (a metered toll, a real bill, real
outages) and not on the READINESS side (no bill, free diagnosis, foregone upside only).** Veer's original
scanner idea is on the wrong side of that line. **But the crawl side is already occupied by Cloudflare
(merchant of record), TollBit (marketplace) and Anubis (free), which is why neither blind ideation lane
proposed anything in it.**

⚠ **Methodological note, reported as an observation and not as evidence.** Three of the four load-bearing
primary sources for area (a) were unreachable by an automated fetcher, two with HTTP 403 bot-blocks
(openai.com, geekwire.com) and three with 60s timeouts (Adobe). n=2 403s is an anecdote, not a count.

---

# D3 - THE SEAT COUNT. Added 2026-09-11. This is the finding that closes the lane.

## The market pays ~2,000 people to inventory AI SYSTEMS. It pays nobody to be answerable for what an agent DID.

**FILLED, richly:** AI governance. **1,997 US postings Jan-Aug 2026, ~71 new/week, median $169,000**
(axialsearch tracker); 658 live openings, median ~$146,000 (GRC Careers board). Verified example, Mercury
Senior Manager Data & AI Governance, **$225,800-$282,300** (NYC/SF), duties verbatim: *"Maintain an
enterprise inventory of material data assets, AI use cases, and related governance decisions."*

**⚠ But read the duty nouns across all six title families: "use cases," "model inventory," "risk
assessments," "EU AI Act," "NIST AI RMF," "ISO 42001." Not AGENTS. Not ACTIONS.** It is a
compliance-artifact job about systems. **"AI compliance officer" as a title: ZERO postings. Nobody is
appointing a named, accountable officer for AI.** Exactly one title anywhere pairs *Agent* with
*Governance* (KPMG, SAP practice). The one fetched posting naming *"agents acting in production"* has it
as a **preferred qualification on a SOX role** (Anthropic, $410k-$510k).

## ⚠⚠ THE KILL ON THE CONVERGENT CANDIDATE (Seal Trail / Stamp Queue), AND IT IS THE INVERSION

**D3 for "review AI-drafted work before a licensed professional seals it" is EMPTY across engineering,
accountancy and customs - and where any reviewing seat IS funded, it is FILLED BUT INCENTIVE-INVERTED.**
METHOD Part 2b calls this the case the ladder cannot see. Read the stated PURPOSE, not the duties:

- Medical scribe vendor sells *"up to a 60% reduction in documentation time"* and *"a clean, ready-to-sign
  note instead of a rough draft."* Purpose: fewer physician seconds.
- CPA tooling sells *"300-500 hours saved annually per user"* = *"$10,000 to $15,000 in recovered billable
  hours per CPA."* Purpose: realization.
- Customs pitch: 30-60 min/entry of data entry *"limits how much volume any broker can handle."*
  Purpose: entries per broker.

**The seat that reviews AI-drafted work in the licensed trades, where it is paid at all, is paid for
THROUGHPUT. It is paid for the opposite answer to the one this candidate sells.**

**And the boards added ZERO headcount by design.** NCBELS (2025-07-16): *"the licensee shall maintain
responsible charge over all aspects of the work... exercise direct control, maintain complete oversight of
all data inputs, and be capable of reproducing the output independently from any AI program."* TBPELS PAO
71 (2024-11-14) went further: *"No new Policy Advisory Opinion will be developed for this request as the
Act and Board rules adequately address the use of artificial intelligence software at this time."*

**NSPE Board of Ethical Review case 24-2, and it is the sentence of the session** (snippet, NSPE 403'd,
NOT VERIFIED verbatim): *"the engineer's mentor and quality-assurance reviewer had retired and had not
been replaced. The tool did not remove the review layer. The organization did."*

## ⚠ AND THE DUTY HAS NEVER BEEN ENFORCED. SIX RULES, ZERO CASES.

Grepped as primary sources: **California BPELSG Board Bulletin Winter 2026 - ZERO occurrences of "AI" or
"artificial intelligence" anywhere, enforcement section included.** TSBPA Board Report Aug 2026 - 44
occurrences of "AI", **every one inside the feature article; the Enforcement Actions section (two board
meetings, ~8 respondents, sanctions $500-$12,000) contains ZERO AI cases.** No AI discipline found at
Texas PELS; Florida FBPE has published no AI guidance at all. NCEES's own June 2026 enforcement column
tells boards they need to **start** preparing investigators, in the future tense, citing no complaint file.

**The one profession where it costs money is LAW, and not via a licensing board:** ~1,490 decisions
worldwide, 1,000+ US, **1,148 attributed to lawyers**, sanctions escalating to **$15,000 per attorney**
and the first bar suspensions (trackers, NOT VERIFIED at the database).

**⚠ THE MECHANISM, and it generalises beyond this lane.** In law, **an adversary and a judge read the
output before it takes effect**, and a fabricated citation is checkable in seconds. That produced 1,000+
enforced sanctions in under three years. In engineering, accountancy, medicine and customs brokerage,
**the only reader of the AI-drafted work before it takes legal effect is the licensee who seals it.**
That produced six rules and no cases. **A board cannot discipline what nobody detects.**

**So the candidate's premise inverts: the licensed professional's exposure is real, but it is not yet
SALIENT, because nothing has ever come back at anybody. That is K4, and only a call can move it.**

## The other seat finding: (a) splits, and the split is the whole story

**FILLED on the visibility half.** 50+ dedicated GEO/AEO roles across 50+ companies in one two-week
window: Stripe, Amazon, Pfizer, LinkedIn, eBay, Victoria's Secret, Vanguard, HubSpot, Anthropic. Senior
and budgeted: Director of Product (AEO & SEO) at eBay; Experian AEO & SEO Manager $100K-$174K.

**EMPTY on the transactional half, searched.** Zero postings whose duty is making the company's own API,
checkout, auth flow or forms work when an agent is driving. **The marketing department owns "can an AI
SEE us." Nobody owns "can an AI TRANSACT with us."**

**(c) Reconstructing why an agent did what it did: EMPTY inside companies.** What exists instead is a 2026
academic literature growing in the hole ("Incident Analysis for AI Agents", "Decision Evidence Maturity
Model for Agentic AI", "Property-Level Reconstructability of Agent Decisions"). **Papers are being written
about how to reconstruct agent decisions. Nobody has been hired to do it.**

**(d) Deciding what authority an agent may exercise: FILLED, but always bundled into the ENGINEER who
built the agent.** RYZ Labs Principal AI Engineer: *"establishing robust AI agent governance policies
covering permissions, code execution controls, system access, and human-in-the-loop enforcement."*
**There is no separation of duties. SR 11-7 made independent validation the entire regulatory point for
models; agent deployment has not reproduced it.**
