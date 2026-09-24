I've built three companies from the research, ranked strongest first. None of them clearly beats the others. All three will score lowest on market size, so the judge-versus-controls round is still what decides this. This is all desk research, not customer validation.

**Dropped:**
- **Dealer warranty recovery.** The dealer management software vendors (IDS-Astra, Lightspeed) already hold the repair orders, connect to the manufacturers and file warranty claims. The unfiled backlog is found once and doesn't come back. The RV market is about $19M a year, and that estimate leans on one anecdote.
- **Accessible course materials, sales tax refunds, grant compliance, SNAP errors.** The generators already found established players in each.
- **Medicaid "medically frail" coding.** In September 2026, CMS gave states a three-tier model for finding these people from the claims data they already hold. States will do the work, so providers have little to buy. Fortuna Health ($18M from a16z) already sells Medicaid navigation to providers.

**Corrections to the merged file.** Don't carry these into any pitch:
- **Indiana's $462M.** The state held back two quarters of routine payments while it moved to managed care. It has nothing to do with Medicaid applications.
- **$9,450 a month.** That is the private-pay price. A facility actually loses closer to the Medicaid rate, about $6,000 a month.
- **Retroactive coverage.** The window is counted back from the filing month, so a slow caseworker costs the facility nothing. Only filing late costs money.
- **ETAP and EasyPower.** Schneider has owned a controlling stake in ETAP since 2021. Bentley bought EasyPower in 2023.

## 1. Photo-to-model software for arc flash studies (strongest)

- **Customer.** Small and mid-size electrical testing and engineering firms (NETA shops, 5 to 50 engineers) that run many $5k–$35k studies a year. Facility owners buy the finished study, not a tool, so they aren't the first buyer.
- **Product.** Technicians photograph and video the gear, including trip-unit menu screens. The model:
  - reads nameplates and settings
  - flags values that are missing or don't agree
  - draws the one-line diagram
  - exports a model ready to run in ETAP, SKM or EasyPower

  The PE reviews and stamps as before. In one large study e-Hazard broke down, modeling took longer than field collection (5 weeks against 15 days), so the pitch is about cutting both.
- **Why now.** NFPA 70E requires a review at least every 5 years. NFPA 70B-2023 made maintenance programs and current one-line diagrams enforceable. 70B-2026 reportedly requires updates after any system change, but only a compliance vendor says so.
- **Competitors.** eGalvanic (about $1.9M raised) does maintenance tracking with photos. arcflash.ai claims a "Photo To Report" feature, but I couldn't see how it works. CIMA+ keeps its model internal. ETAP's free field app stores photos but doesn't extract data from them, and its 2026 release suggests one-line connections. No venture-backed company is doing this specifically.
- **Price and market.** About $500–$1,500 per study, which is my estimate. The only market figure, about $1.2B in study services, comes from a weak source. That makes the starting market small, roughly $50–100M. It only gets venture-sized if the product grows into the facility's live electrical record: 70B maintenance, updates after changes, then multi-site owners and data centers.
- **Main risk.** The most important data may not be photographable: settings behind menus, cable lengths and sizes, hidden impedance values. If so, the savings shrink to typing. ETAP could also ship photo extraction as a feature.
- **Fastest test.** Have three study firms time one real project, split into site time, transcription and modeling.
- **Team fit.** Purdue EE faculty and local NETA firms are within reach.
- **Draft blind paragraph:** "US facilities with electrical switchgear must keep an arc flash study current: safety standards require review at least every five years and an update after system changes, and a 2023 revision made current one-line diagrams and maintenance programs enforceable. Studies cost $3,500 to over $100,000, and much of the labor is technicians copying nameplates and breaker settings by hand and engineers re-keying them into modeling software. We sell to the electrical testing and engineering firms that perform these studies. Technicians photograph and video the gear; our models read nameplates and trip-unit screens, flag missing or inconsistent values, draw the one-line diagram and export a ready-to-run model to ETAP, SKM or EasyPower. The licensed engineer still reviews and stamps. Firms pay about $500 to $1,500 per study."

## 2. Dispute-response software for debt collectors and subprime lenders

- **Customer.** Debt collectors, debt buyers, and subprime auto and installment lenders handling 5k–50k disputes a month. They are sued most often, run lean teams, and don't make vendors sit through a year of bank review.
- **Product.** It pulls each dispute from e-OSCAR (the credit bureaus' system for sending disputes to lenders), from direct letters, from debt validation requests and from CFPB complaints. It matches the dispute to the account file and drafts a verify, correct or delete response that cites the evidence. It also keeps an investigation file that holds up in court. It never labels a dispute frivolous on its own.
- **Why now.**
  - CFPB complaints rose from 3.2M in 2024 to 6.6M in 2025. The CFPB names AI agents as one of four causes.
  - Complaints against creditors and collectors went from about 159k to about 302k.
  - FCRA lawsuits rose 37% in 2025 and are up another 44.6% through July 2026 (WebRecon).
  - In 2025 the CFPB withdrew its guidance and cut back enforcement, so private lawsuits now carry the risk. Defense counsel say detailed investigation records are what win those suits.
- **Competitors.** Bridgeforce is piloting an "AI Resolution Engine" for bureau disputes, aimed at large issuers. e-OSCAR now sells API access. AI collections startups (Domu, Gryphon, Sedric) work on outbound contact, not disputes. I found no startup focused on this.
- **Price and market.** $1–3 per dispute, or $50k–$250k a year per customer. Using 2012 data scaled up, I estimate 40–60M disputes a year and a $50–120M market for dispute handling alone. Wider collector compliance and litigation-defense packages would add to that.
- **Main risks.** Bridgeforce or e-OSCAR could ship this as a feature. If the tool gets a decision wrong, that record becomes evidence against the customer. The CFPB's June 2026 portal changes may slow the flood of template disputes.
- **Fastest test.** Get one mid-size collector to share its monthly dispute volume, its cost per dispute and its FCRA suits over the last 12 months.
- **Draft blind paragraph:** "Consumers now dispute credit reports and debts in bulk, often with AI-written letters from credit repair firms and apps. CFPB complaints doubled to 6.6 million in 2025, and Fair Credit Reporting Act lawsuits rose 37% in 2025 and another 45% in the first seven months of 2026. Lenders and collectors must investigate every dispute within 30 days, and a thin investigation record is what loses those suits. We sell to debt collectors, debt buyers and subprime lenders handling 5,000 to 50,000 disputes a month. Our software pulls each dispute from the bureaus' system and the lender's inbox, matches it to the account file, drafts the verify, correct or delete response with evidence cited, and keeps a litigation-ready investigation file. Customers pay $1 to $3 per dispute."

## 3. Long-term-care Medicaid applications for nursing home chains (keep, with a warning)

- **Customer.** Chains of 10–50 buildings in states that don't pay automatically after 45 days. Illinois does, which takes most of the pain away there, so avoid it.
- **Product.**
  - Pulls the applicant's bank statements and flags transfers that trigger penalties.
  - Fills the state's form.
  - Answers caseworker requests for documents and tracks every pending case.
  - Adds home-care waiver applications later, and the home-equity cap that starts in 2028.
- **Why now.** From January 1, 2027, H.R. 1 §71112 limits retroactive coverage for aged and disabled applicants to 2 months before the filing month, down from 3. Because the window runs from filing, the pitch has to be "file on time", not "get approved faster". Medicaid is the main payer for 63% of residents. By my extrapolation from Illinois (15,645 applications in 2023), there are about 300–400k applications a year nationally. Illinois audited 50 applications and found 22% past the deadline.
- **Competitors.** Medicaidsoft (Utah, about $1.5M raised) already sells nearly this exact product, and it has a referral channel to about 4,000 elder law attorneys. Telos LTC fills and e-files applications in Texas. ExaCare ($30M Series A) runs admissions in 1,500+ facilities and could add this.
- **Price and market.** About $500 per application, or a monthly fee per building. That comes to $150–200M in software, or $0.5–1B if it replaces the outside firms that charge families about $9,000 per application. That $9,000 figure comes from one elder law attorney, who has a stake in the comparison.
- **Main risk.** The product already exists, and a checklist with a deadline alert solves much of the January 2027 problem.
- **Fastest test.** Ask five Indiana chain business office directors for their Medicaid-pending days, their denial write-offs, and whether they've looked at Medicaidsoft.
- **Draft blind paragraph:** "Most nursing home residents end up relying on Medicaid, but coverage starts only after an application backed by up to five years of bank records, and states take 45 to 90 days or longer to decide. Until then the facility cares for the resident unpaid, and a denial can mean months of care never collected. From January 2027 federal law also limits retroactive coverage to two months before the filing month, so late filings lose money outright. We sell to nursing home chains with 10 to 50 buildings. Our software pulls the applicant's bank statements, flags transfers that trigger penalties, fills the state's form, answers caseworker requests for documents and tracks every pending case. Facilities pay about $500 per application or a monthly fee per building."

I didn't write any files or change the repo. If Veer puts any of these three in STATE.md, the "desk research, not customer validation" line has to go with it.
