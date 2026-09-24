# Loop 2 judged paragraphs, 2026-09-24

Each judge received exactly one paragraph below, inside the METHOD judge prompt. Desk research only; not customer validation.

## Control: ByteAsk (Fall 2026)

Engineers who write C and C++ for trading systems, cars, chips and operating systems get little from today's AI coding assistants, which propose diffs that look right but break at compile time, leak memory or introduce race conditions. This company sells an AI coding agent built only for C and C++. It does not stop at a suggested change: it builds, debugs and tests every change with the customer's real compiler, debugger and test suite, iterating until the change holds. It runs from the terminal or inside VS Code, Neovim and Emacs, and can be deployed fully on-premises for teams whose code cannot leave their network. Individual developers start free and can bring their own model keys; revenue comes from paid plans for managed model usage and from enterprise on-premises licences.

## Control: Kita (Winter 2026)

Lenders in emerging markets such as the Philippines, Indonesia and Mexico cannot pull a borrower's history through banking APIs, because most borrowers are thinly banked and their financial record lives in documents: e-wallet statements, bank statements, utility bills and payslips. Credit teams review these by hand, which slows decisions, raises cost per loan and caps lending volume. This company sells lenders an AI platform that completes applications, verifies documents for fraud, extracts the data and produces localized risk signals for underwriting within minutes. It links document-level signals to later repayment outcomes, so fraud and risk models improve with each lender's decisions. Customers are banks, digital lenders, SMB lenders and fintechs. It is sold as enterprise software, priced by deployment and volume of borrower files processed.

## Control: Vela (Winter 2026)

Recruiters and executive-search firms spend hours coordinating interview panels: a single panel takes a dozen emails, and every reschedule starts the chain again, often across time zones and with candidates who reply at odd hours. This company sells an AI scheduling coordinator that works like a human assistant. The recruiter copies it on the email thread; it contacts every participant, finds times that work, chases people who don't reply, reschedules when plans change and confirms, over email, SMS and WhatsApp, at any hour. There is no dashboard or new workflow to adopt. It sells to recruiting teams, search firms and other professional-services teams with heavy meeting loads, priced per seat as a subscription, and positions the value as coordinator hours saved each month.

## Loop 1 carry-over: LTC Medicaid applications (additional judges)

Loop 1 did not save the text its one judge saw. This is the shaper's draft blind paragraph (`research/2026-09-24-loop1/agents/shaper.md`), which the orchestrator most likely used verbatim.

Most nursing home residents end up relying on Medicaid, but coverage starts only after an application backed by up to five years of bank records, and states take 45 to 90 days or longer to decide. Until then the facility cares for the resident unpaid, and a denial can mean months of care never collected. From January 2027 federal law also limits retroactive coverage to two months before the filing month, so late filings lose money outright. We sell to nursing home chains with 10 to 50 buildings. Our software pulls the applicant's bank statements, flags transfers that trigger penalties, fills the state's form, answers caseworker requests for documents and tracks every pending case. Facilities pay about $500 per application or a monthly fee per building.

## Loop 1 carry-over: arc flash (input to the reshaper)

The reshaper receives this paragraph (the shaper's draft, same caveat) and the five loop 1 judges' strongest-version and kill/test sections.

US facilities with electrical switchgear must keep an arc flash study current: safety standards require review at least every five years and an update after system changes, and a 2023 revision made current one-line diagrams and maintenance programs enforceable. Studies cost $3,500 to over $100,000, and much of the labor is technicians copying nameplates and breaker settings by hand and engineers re-keying them into modeling software. We sell to the electrical testing and engineering firms that perform these studies. Technicians photograph and video the gear; our models read nameplates and trip-unit screens, flag missing or inconsistent values, draw the one-line diagram and export a ready-to-run model to ETAP, SKM or EasyPower. The licensed engineer still reviews and stamps. Firms pay about $500 to $1,500 per study.

## Arc flash drift monitor (reshaped)

Written by the orchestrator from `agents/reshaper-arc-flash.md`. Judged fresh under METHOD step 4.

US facilities must keep an arc flash study current: NFPA 70B requires one-line diagrams kept accurate and studies reviewed at least every five years and after changes, yet a Schneider audit of 400 sites found 89% had no complete one-line diagram. Between studies, breakers get swapped and trip settings changed, so arc flash labels silently go wrong. We sell to the independent electrical testing firms that already visit each site every one to three years for 70B maintenance. Our software reads their test reports, relay setting files and gear photos, matches each device to the site's existing ETAP, SKM or EasyPower model, and flags where the site no longer matches its study, with every value linked to its source for the engineer to approve. Firms pay $500 to $1,200 per site per year and resell the flagged updates as billable study work.
