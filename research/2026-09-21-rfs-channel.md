# Investor "request for startups" lists as a sourcing channel

Research note, September 21, 2026. Three bounded research lanes plus spot checks of the primary pages. Desk research only; nothing here is customer evidence.

## The question

Veer's proposal: investors and accelerators (YC, a16z, others) publish lists of problems they want solved. Picking from those lists could be an easier route to a good idea because a third party has already verified demand. The open worries were (1) whether a listed problem is already being solved and (2) how to differentiate if it is.

## Answer

**Use the lists as a filter and a vocabulary, not as the generator.** Generate ideas the way METHOD already says (fresh generators, founder brief, no dead lists), then check the merged batch against the current lists. A match is one supporting signal that a category is fundable. It is also an automatic trigger for the crowding check below, because the same match tells every other founder the same thing.

Three findings drive that:

1. **The premise "demand is verified by a third party" is half right.** What a list verifies is that capital is available for the category. It does not verify that a customer pays. YC's own page: "These represent just a fraction of what we fund; if one excites you, take it as extra validation to dive in, but you don't need to work on these ideas to apply to YC" ([ycombinator.com/rfs](https://www.ycombinator.com/rfs), fetched 2026-09-21). YC partner Jared Friedman said the Spring 2025 asks were selected from 100+ submissions by YC's own alumni founders ([x.com/snowmaker](https://x.com/snowmaker/status/2018502910733377642), 2026). In other words, part of each list describes what funded founders are already building, written up after the fact.

2. **Whatever a widely read list names is the most crowded place to enter.** Spring 2025: 67 of 144 YC companies were AI-agent companies, up from 58 of 163 in Winter 2025 ([PitchBook](https://pitchbook.com/news/articles/y-combinator-is-going-all-in-on-ai-agents-making-up-nearly-50-of-latest-batch), summarized via search; the article itself is paywalled). Winter 2026: 56 of 199 companies were "AI-native service" businesses, the largest category in the batch, with healthcare the densest cluster and six legal companies ([Extruct, W26 breakdown, 2026-03-25](https://www.extruct.ai/research/ycw26/)). AI-native services is exactly the founder scope's second category, so the scope is already inside the crowd. The lists did not necessarily cause this (agents got cheap for everyone at once), but the effect on two unfunded founders is the same either way.

3. **The lists name categories, not problems.** "AI-Native Compliance Infrastructure" or "Company Brain" is a category. The thing that is crowded is the category name. A problem-level formulation one level narrower, in a segment the funded entrants ignore because it is too small or too painful, is where a two-person team can stand. That is the same wedge logic METHOD already applies, so the lists do not change the method; they change where the overlap check looks.

Paul Graham's essay is the standing counterweight: ideas that "sound plausible enough to fool you into working on them" are what YC calls "made-up" or "sitcom" ideas, and "the most successful startups almost all begin" as organic ideas grown from the founders' own experience ([paulgraham.com/startupideas.html](https://www.paulgraham.com/startupideas.html)). He does not name RFS lists; the transfer is inference.

**What is not known.** No public dataset compares outcomes of list-inspired companies against organically found ones. No YC partner has given a percentage of any batch that came from an RFS. First-person founder accounts of using or ignoring the lists did not surface in a general web search.

## Current lists, filtered to the founder scope

Scope: AI B2B SaaS (cat 1), AI-native services (cat 2), consumer AI with a defensibility hypothesis (cat 3). Hardware, bio, crypto, defense, space, energy and license-gated asks are dropped without comment.

| Source, edition, date | In-scope asks |
|---|---|
| **YC Fall 2026** ([ycombinator.com/rfs](https://www.ycombinator.com/rfs), live 2026-09-21, 13 asks) | The Primer (adaptive tutoring at private-tutor quality, cat 3) · A Cloud for Small Software (deploy infra for AI-generated single-user apps, cat 1) · Multiplayer AI (teams sharing agent tasks, cat 1) · AI-Powered Consumer Products for 1B People (cat 3) · New Operating Systems for the Physical World (managing mixed agent and field-worker teams, cat 1) · AI-Native Compliance Infrastructure (**financial** compliance: "still stitched together with spreadsheets, siloed tools, and expensive headcount", cat 1) · Self-Maintaining APIs (agents that update customer code on breaking changes, cat 1) |
| **YC Summer 2026** (15 asks; the page bundles editions client-side, so this came via [modelence.com](https://modelence.com/yc-rfs-summer-2026) and matches the verbatim pull in `archive/2026-09-18/STATE.md`) | AI-Native Service Companies (explicit list: insurance brokerage, accounting/tax/audit, compliance, healthcare administration, cat 2) · Company Brain (cat 1) · Dynamic Software Interfaces (cat 1) · SaaS Challengers (cat 1) · Software for Agents (cat 1) · The AI Operating System for Companies (cat 1) |
| **YC Spring 2026** (8 asks, [modelence.com](https://modelence.com/yc-rfs-spring-2026)) | Cursor for Product Managers (cat 1) · AI-Native Agencies (cat 2) · AI Guidance for Physical Work (cat 2) · Infra for Government Fraud Hunters (cat 1; government sales cycle is the practical barrier, and the ask says at least one founder should have done the work) |
| **a16z Big Ideas 2026**, parts [1](https://a16z.com/newsletter/big-ideas-2026-part-1/) and [2](https://a16z.com/newsletter/big-ideas-2026-part-2/), Dec 9–11 2025 | Multimodal data cleanup and governance (cat 1) · AI-native data stack, agents with business context (cat 1) · Systems of record lose ground to agent layers (cat 1) · Vertical AI goes multiplayer, counterparty network effects (cat 1) · AI reinforces business models, outcome-based pricing (cat 2; names Eve, contingency legal) · Voice agents for full workflows (cat 1/3) · Prompt-free proactive apps (cat 3) · Legacy banking and insurance data normalization (cat 1) · Forward-deployed motions into non-tech industries (cat 2) · Fortune 500 multi-agent orchestration (cat 1) · Consumer AI "see me" (cat 3) · AI startups selling to AI startups (cat 1) · Healthy MAUs, preventive health subscriptions (cat 3) · Personalized education and media (cat 3) |
| **a16z Speedrun, 14 Big Ideas**, [2025-12-18](https://speedrun.substack.com/p/14-big-ideas-for-2026) (same firm as above) | Multiplayer beats single-player AI · Personal curation agents · Buyer-side AI marketplaces · Fat AI startups owning the slowest markets (cat 2) · Tools that help people stay human · Consumer AI making travel, therapy and tutoring affordable |
| **Bessemer Atlas, AI Systems of Action**, [2025-05-29](https://www.bvp.com/atlas/roadmap-ai-systems-of-action) (oldest here) | Agentic integration inside vendor ecosystems (names CurieTech, Mando) · AI-enabled services platforms for migrations (cat 2; names Mechanical Orchard, Isoform) · AI-native ERP (names Doss, Everest) · Passive CRM data capture (names Day.ai, Attio) · Voice AI for non-emergency 911 · IP disclosure harvesting (names Tradespace) |
| **Bessemer, AI Infrastructure Five Frontiers**, [2026-03-30](https://www.bvp.com/atlas/ai-infrastructure-roadmap-five-frontiers-for-2026) | Harness infrastructure: memory, context, evals and observability for deployed AI (names Bigspin, Braintrust, Judgment Labs) |
| **Pear VC RFS**, [2026-08-05](https://pear.vc/request-for-startups-august-2026/), 6 asks each from an outside operator | An agent that interviews your company for tacit knowledge (cat 1) · AI operating system for work (cat 1) · A true personal coach (cat 3) · Governance sandboxes for enterprise AI (cat 1) · Lovable for kids (cat 3) · Enterprise AI evaluation infrastructure (cat 1) |
| **Antler India, B2B AI list**, [2025-07-31](https://www.antler.co/blog/the-next-big-thing-in-b2b-ai) | A vertical checklist, India-focused, over a year old. Weak as a signal. |

Checked and found no current published ask list: Sequoia (Arc is a cohort program), NFX, First Round (a founder survey), General Catalyst, Khosla, Redpoint, Lightspeed, Menlo, Emergence, Craft, Founders Fund, South Park Commons, Neo. McKinsey and Gartner publish trend sizing, not problem statements. ARPA-H and NSF SBIR current topics are clinical or hardware.

**Asks that appear in two or more independent firms** (the strongest version of the third-party signal):

1. An AI operating or orchestration layer for company workflows: YC Summer 2026, Pear, a16z.
2. AI-native services with outcome-based economics: YC Summer and Spring 2026, Bessemer, a16z.
3. Evaluation, observability and governance infrastructure for deployed enterprise AI: Bessemer, Pear.
4. Multiplayer or vertical agents replacing enterprise workflow software: YC, a16z.
5. Consumer AI personalization ("optimize for me", a personal coach): a16z, Pear.

Item 2 is the founder scope's own second category. The lists confirm the scope rather than move it.

## Where the current board sits

- Supplier quality chargeback defense (the comparison concept) is a contingency, outcome-priced service. It maps to a16z's "AI reinforces business models" (Eve is the named example, in legal) and YC's AI-native service ask. Category confirmed fundable; category also crowded (56 of 199 in W26). The desk verdict from 2026-09-20 stands: parked until a supplier conversation happens.
- The customs-broker entry line check (round 17, C1, test next) sits near "AI-Native Compliance Infrastructure", but that Fall 2026 ask is explicitly financial compliance, so C1 is adjacent, not inside the crowd. Confirms the narrower-than-the-ask position.
- Technician diagnostic knowledge capture (first exploratory run, desk-checked, not validated) now has a second-source signal: Pear's August 2026 ask for "an agent that interviews your company" to capture tacit how-work-gets-done knowledge, with YC Spring 2026's "AI Guidance for Physical Work" adjacent. The existing formulation is one level narrower than the ask (field technicians, not the whole company), which is the position this note recommends. Next: the two-hour scan on Pear's ask, then the technician access STATE already calls for.
- Self-Maintaining APIs (YC Fall 2026) is the one ask whose customer, developers, is reachable by two students without an industry network. Run the scan before anything else; likely crowded.
- Nothing on the lists is a formulation the board has not already circled. The lists add no new candidate this round; they add one supporting signal to an existing unresearched hypothesis.

## The two-hour "is someone already solving this" scan

Run this on each shortlisted idea before spending a verify budget. Everything costs zero dollars.

| Step, time | Tool | What it shows | What it misses |
|---|---|---|---|
| 1, 15 min | [YC company directory](https://www.ycombinator.com/companies), filter by industry tag and batch, plus a plain web search "[problem] startup" | The named-competitor list among YC companies | Everyone not YC-funded: bootstrapped, other-VC, stealth |
| 2, 20 min | [G2 categories](https://www.g2.com/categories) and Capterra (same parent, Gartner Digital Markets) | Review count and how recently reviews arrive; reviews require actual use | Small vendors under-ranked until reviews pile up; some vendors run review campaigns |
| 3, 20 min | Crunchbase free profiles | Round size, date, investors, founding date | Free tier blocks filters and export; only self-created profiles |
| 4, 20 min | LinkedIn job postings on the top three names | Whether they hire sales and customer success (a repeatable motion) or only engineers (still building) | No revenue; hiring freezes confound it |
| 5, 10 min | Google Trends on the top two brand names | Relative interest over time | Curiosity, not paying demand |
| Dev tools only | GitHub stars, forks, commit velocity | Real usage proxy | Irrelevant outside open source |

**Solved versus trying.** Practitioner signals, not validated research; no single metric proves product-market fit ([PostHog](https://posthog.com/founders/measure-product-market-fit)). A competitor has likely solved it when several hold at once: named customer logos with numbers in case studies; a public pricing page with an enterprise tier and annual billing; open sales, SDR and customer-success roles alongside engineering; a steady monthly trickle of verified reviews rather than a launch-week burst; a Series B or later within 18 months from a recognized fund; headcount growing over the trailing year; trade-press coverage continuing past the funding cycle. A field is only "trying" when the entrants are waitlist-only, demo-request-only with no price, engineering-only hiring, seed or accelerator money only, and a review burst then silence.

## Differentiating inside a named category

Moves with a source, ranked for two founders with no capital and no industry network:

1. **Beachhead first.** Pick the narrowest segment you can dominate and sequence outward (Moore, *Crossing the Chasm*; Sarah Tavel's wedge framing). Harvey entered legal AI after Westlaw, LexisNexis and funded startups, wedged into the largest firms first, and reached an $11B valuation by March 2026 ([CNBC, 2026-03-25](https://www.cnbc.com/2026/03/25/legal-ai-startup-harvey-raises-200-million-at-11-billion-valuation.html)). Costs focus, not money.
2. **Vertical depth over horizontal breadth.** Go deep on one workflow's specific data points, compliance quirks and integrations. A research and design problem, not a capital problem. Elad Gil's version: target the segment or channel the incumbent structurally cannot serve ([blog.eladgil.com](https://blog.eladgil.com/p/ai-startup-vs-incumbent-value)).
3. **Distribution the incumbent cannot copy.** Rampell's argument that innovation rarely beats an incumbent's distribution ([a16z, Distribution vs. Innovation](https://a16z.com/distribution-vs-innovation/)). For this team that means a channel reachable from Purdue, not a sales team.
4. **A different product, not a thinner one.** Cursor entered coding assistants after GitHub Copilot and won share with a forked, repo-aware editor rather than a layer on the same experience (product-comparison journalism, directional only). The negative case is the wrapper cohort: OpenAI's own product cadence is reported to have absorbed roughly 200 funded wrapper startups in 2024, and Relay, a Zapier-style AI workflow tool, shut down as the platforms absorbed the feature ([TechCrunch AI graveyard, 2026-09-15](https://techcrunch.com/2026/09/15/the-ai-graveyard-a-running-list-of-projects-and-startups-that-didnt-make-it/); the percentages come from aggregator sites and are directional).
5. **Not recommended here: services-led or forward-deployed motions** ([a16z, services-led growth](https://a16z.com/services-led-growth/)). Trading margin for moat needs capital to run the service layer at a loss or a network to land the first logos.

On the AI moat question itself, the sources disagree. a16z, Sequoia's application-layer thesis and Benedict Evans argue models commoditize and workflow, data and distribution win; a16z's own September 2026 writing argues compute scale still builds moats at the model layer. Helmer's 7 Powers, applied to AI startups, points at counter-positioning, cornered resource and process power as the three a small team can build early ([YC Library](https://www.ycombinator.com/library/Mx-the-7-most-powerful-moats-for-ai-startup)). Consistent with METHOD: name the mechanism, dependency and test; do not assert a flywheel.

## Proposed METHOD addition (not applied; Veer and Cole decide)

Under "1. Generate, then shortlist", after the archive overlap check:

> Check the merged batch against the current investor ask lists (the catalog in `research/2026-09-21-rfs-channel.md`; refresh each YC batch). A match is one supporting signal that the category is fundable, and it triggers the two-hour scan before the idea enters verification. Never generate from the lists; they name categories, and category names are where the crowd is.

## Second pass, same day: the firms not yet checked, idea newsletters, and customer-side signals

**Twenty more firms, one search each, none with a current list:** Village Global, Contrary, Hustle Fund, Floodgate, Homebrew, Precursor, SignalFire, Point Nine (a stated thesis against thin wrappers, not a list), Boost VC (frontier hardware, out of scope), HF0, Techstars, 500 Global, Entrepreneur First, Antler global, Greylock, Index, Accel, Founders Inc, Speedinvest, Seedcamp. Conclusion: YC, a16z, Bessemer, Pear and Primary are the published-list universe as of today.

**Primary VC, "Our 2026 Request for Startups", [2026-03-31](https://www.primary.vc/articles/our-2026-request-for-startups).** In-scope asks: planning software for usage-based pricing ("seat based pricing most definitely is" dead, cat 1) · a communication layer for human-agent and agent-agent work (cat 1) · a system of record for customer-specific agent deployments after rollout (cat 1) · voice agents replacing phone trees with "white-glove service" (cat 1/2) · **verticalized AI accounting for sectors with complex billing and cost structures** (cat 1/2) · catastrophic-risk simulation for insurers (cat 1, actuarial depth). Out: tokenized equities, T+0 back office, stablecoin treasury, insurance-core replacement.

This adds a sixth cross-source ask. **Accounting-shaped AI-native services** now have three independent sources: YC Summer 2026 names accounting, tax and audit outright; Primary asks for vertical AI accounting; and Financial Cents' 2025 workflow report (cited second-hand, not opened) has 55.5% of accounting firm owners naming workflow inefficiency, mostly client onboarding and document chasing, as their biggest problem.

**Idea newsletters and databases.** Ideabrowser (Greg Isenberg) scrapes subreddits, Facebook groups and Google Trends for demand signals and sells the result at $499 to $2,999 a year; that is the same signal the customer-side sweep below collects for free. Trends.vc is editorial market writeups. Exploding Topics is keyword-volume curves with a business-idea layer on top; the example found (AI personal shoppers against a "$1.3T by 2030" projection) is market sizing, not demand. Starter Story is retrospective case studies, useful to check a chosen idea against a comparable business, useless for surfacing unmet demand. Indie Hackers' ideas pages are generated one-line stubs with no evidence attached. None beats doing the sweep.

**Customer-side signals.** Reddit was blocked at the tool level for both the agent and the main session, so this leans on one Hacker News thread and Capterra review pages, both opened directly. Named buyer, named workflow, and whether a vendor already exists:

| Problem, in the buyer's words | Who, where, when | Vendor state |
|---|---|---|
| "Tax filing service for American expats with American investments who live abroad", files correctly in both countries; would pay $1–2k a year | Self-described expat investor, [Ask HN: What could I build to make your life a little easier?](https://news.ycombinator.com/item?id=44618822), 2025 | Bright!Tax and Greenback exist; the framing says the investments-plus-abroad combination is what they handle badly |
| Email alerts for Upwork postings matching client criteria, since RSS was removed | Freelancer, same thread | Built-in alerts inadequate per the poster; narrow |
| Engineering performance reviews that weigh "fair evaluation, growth, and impact" without admin overhead | Engineering manager, same thread | Crowded HR category |
| Field-service software for IT repair shops: 16 months of broken notifications, a 150-day support fix, inventory that "has a mind of its own", broken QuickBooks sync | Shop owners and managers, [Capterra reviews of RepairShopr](https://www.capterra.com/p/133945/RepairShopr/reviews), 2022–2025 | Incumbent exists and is disliked; switching signal |
| Estimating database "missing tons of everyday items contractors utilize"; no view across all projects at once; large estimates slow the tool | Construction PMs and ops managers, [Capterra reviews of Contractor Foreman](https://www.capterra.com/p/166113/Contractor-Foreman/reviews) | Incumbent exists with named recurring gaps |
| "Payments collected but not deposited. Late fees applied incorrectly", no audit trail; onboarding "doubled everyone's workload for about 4 months"; fees 30–50% above advertised on a 100-door portfolio | Property and condo managers, a CEO, [Capterra reviews of Buildium](https://www.capterra.com/p/47428/Buildium-Property-Management-Software/reviews), Apr–Aug 2026 | Large funded incumbent; the pain is reconciliation and onboarding, not the category |
| Helpdesk that "glitched frequently", one form template only, crashes under load; reviewer names the competitor they moved to | IT leads and sysadmins, [Capterra reviews of Spiceworks](https://www.capterra.com/p/102709/Spiceworks-IT-Help-Desk/reviews), 2023–2026 | Crowded category; the signal is that switching happens over reliability |
| Rate confirmations and bills of lading auto-generated badly; entries fail to save | Small freight brokers, Capterra reviews across AscendTMS, Toro and LoadPilot | Directional only, synthesized across products, no single attributable reviewer |

Reading across the table: the big-category complaints (helpdesk, property management, HR) are switching signals inside markets that already hold many funded competitors, which is the crowding case from the first pass. The narrow, named workflows are where a two-person team could stand: expat tax with US investments, contractor estimating item data, freight paperwork generation. The expat tax case is the only one with a stated price, and it lands inside the accounting-shaped cluster that three investor sources also name. Its dependency is that paid tax preparation carries preparer obligations (a PTIN at minimum, credentials for representation), so the formulation would need a credentialed reviewer in the loop, which METHOD's AI-native services lens allows and prices.

**Open gap.** Reddit operator communities (r/msp, r/accounting, r/Contractor, r/PropertyManagement and similar) were the brief's main target and are unreached. A tool with Reddit access is the next step, not more web search.

## Source quality

Primary and verified this session: YC RFS page, Paul Graham's essay, Extruct's W26 count, a16z, Bessemer and Pear pages. Second-hand: PitchBook batch numbers (paywalled, taken from search summaries and a LinkedIn repost), YC Summer and Spring 2026 asks (modelence summary, cross-checked against the verbatim archive pull). Weak: aggregator sites for the wrapper-failure statistics and several moat essays; the HBR "competitor job postings" piece (August 2026) was cited by a lane but not opened. Antler's list is a year old and India-focused.
