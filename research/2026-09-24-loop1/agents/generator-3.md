My best idea is AI-native arc flash studies. Arc flash is the burst of heat and pressure released when electricity jumps between conductors, and a study calculates how dangerous each piece of electrical equipment is to work near. The product reads photos of a building's electrical equipment and builds the study automatically. My runner-up is AI tools that make math-heavy university course materials accessible to disabled students, which the law now requires. All of this is desk research, not customer validation. I didn't read STATE.md, the archive or the old candidate files, but I did read METHOD.md and the README. The README names the earlier concept (supplier quality chargeback defense), so I steered away from it.

## Best idea: arc flash studies from phone photos

**Problem.** Workplaces with electrical equipment have to assess arc flash risk and put a warning label on every panel. NFPA 70B, the national standard for maintaining electrical equipment, became mandatory in 2023. It requires these studies to be redone at least every five years and after any change to the system. A study costs about $5,000 to $50,000 per facility and takes weeks of a scarce power engineer's time. A patent filing on arc flash assessment says collecting the equipment data is about half the total effort. Collecting it means opening panels, photographing nameplates and breaker settings, typing each value in by hand, and redrawing the wiring map (called a one-line diagram) that is usually out of date. Without a current one-line diagram, the study costs another 25 to 35%.

**Product.** A technician photographs each panel, nameplate and breaker setting. The AI reads the photos, builds the one-line diagram and the electrical model, and hands that model to the existing calculation software (ETAP, SKM or EasyPower). It also flags missing or suspicious values. A licensed engineer reviews and stamps the result. Customers get the study and labels in days instead of weeks, at roughly half today's price.

**Start narrow, grow broad.**
- **Start:** mid-size Indiana manufacturers. Purdue runs the Indiana Manufacturing Extension Partnership, which advises thousands of small manufacturers, so there is a local channel to reach them.
- **Grow:** once a building's electrical system is on file, sell everything else that needs that data:
  - the NFPA 70B maintenance program
  - load calculations for EV chargers, heat pumps and solar
  - risk data for insurers
  - data centers
- **Durable edge:** a labeled dataset of real electrical equipment photos that competitors don't have.

**Why it could work.**
- The need never goes away. The standard forces a new study at least every five years, whatever the political climate.
- The work splits into a perception step (reading photos) and a physics step (the calculation). AI replaces the costly perception step without touching the physics.
- I found no funded AI-native startup doing photo-to-model studies:
  - CIMA+, a Canadian engineering firm, trained a model on 4,300 photos that identified equipment with 91% accuracy on new images. It is an internal research project that the firm says it may sell.
  - REALTIMEais tracks maintenance compliance but does not capture data or build the model.
  - ETAP, SKM and EasyPower do the calculations but need the data typed in.
- The customers are fragmented (thousands of plants, hundreds of small testing firms), so no incumbent owns the buying channel.

**Weakest points.**
- **It is part services.** You need a licensed engineer to stamp studies, and qualified people to open live panels. That lowers margins and brings liability: a wrong label can injure a worker.
- **Customers buy rarely.** Once every five years is not recurring revenue unless the maintenance product sells.
- **Big players could copy it.** Schneider, Eaton and ABB all have field service arms that could add photo capture.
- **The team lacks credentials.** Neither founder has an electrical engineering license, and one would be needed early.
- **My market size is unverified.** I estimate about $0.5–1.5B a year for studies alone: roughly 300k–500k facilities that need one, times $8k–15k every five years. I found no published figure.
- **Fastest test:** show 10 facility managers or small testing firms a quote at half their last study's price, and see whether they will hand over panel photos.

## Runner-up: accessible STEM course materials for public universities

**Problem.** Public colleges must make course materials meet WCAG 2.1 AA, the federal web accessibility standard, by April 26, 2027. The deadline was originally April 2026. Purdue's own guidance says course materials inside the learning management system (Brightspace at Purdue) must comply.

**Why it could work.**
- **The government named the gap.** When the Justice Department delayed the deadline, it said automated tools aren't reliable enough for "complex educational and STEM content."
- **Current fixes are very expensive.** A vendor quoted Ohio State $5 a page, about $20M, just for its library's PDFs. Services charge $5–25 a page, and $25–75 or more for tables, charts and forms. About 75% of scholarly PDFs fail accessibility checks (ACM, 2024).
- **There is a Purdue angle.** Two Purdue math professors and Purdue's Innovative Learning team built ink2html on Claude. It turns handwritten math notes into accessible web pages, and it is licensed to Purdue's West Lafayette and Indianapolis campuses only. Licensing it through Purdue Innovates and selling it to other public universities is a credible story for the judges.
- **It can grow.** Hospitals and clinics that take federal health funding face a similar deadline in May 2027. Later markets are local governments and EU companies under the European Accessibility Act.

**Weakest points.**
- **It is crowded.** Competitors include Mathpix, YuJa Panorama (which Purdue already uses), Anthology Ally's auto-tagging, UDOIT (which Canvas is adopting), Continual Engine, CampusMind, and a free AWS tool built at Arizona State.
- **Demand is a one-time spike.** Much of the backlog is a one-time job, and content that is archived and unused is exempt.
- **Deadlines can slip again.**
- **Purdue already solved it for itself,** so the team would depend on a licensing deal.

## Checked and dropped

In each case a well-funded player already owns the space or the timing collapsed:
- **Tariff refunds (duty drawback):** Pax (YC), Zollback and Tariff Refund HQ.
- **Medicaid work-requirement verification:** Fortuna Health raised $18M led by a16z and already serves health plans covering 25M+ people.
- **Dealer warranty claims:** Forge AI, ClaimLane, WickedFile.
- **Transfer credit evaluation:** CourseWise is piloting at about 120 campuses; EdVisorly and EDMO also compete.
- **Phase I environmental site assessments:** LightBox owns the records data; V7 and CaseMark already automate reports.
- **Defense contractor cybersecurity certification (CMMC):** the Defense Department suspended mandatory third-party certification on July 13, 2026.
- **FAA safety management systems for charter operators:** the market is small and PreflightSMS, TrustFlight and Ideagen already serve it.

I couldn't verify arc flash injury statistics because the session ran out of web searches. I wrote no files and made no commits.

Sources:
- [NFPA 70B Chapter 6 (REALTIMEais)](https://realtimeais.com/nfpa-70b/nfpa-70b-chapter-6-system-studies/), [REALTIMEais product](https://realtimeais.com/nfpa-70b-compliance-software/), [NFPA 70B becomes a standard (Facilitiesnet)](https://www.facilitiesnet.com/maintenanceoperations/article/Electrical-Safety-Compliance-Under-NFPA-70B--20949)
- [Zech Engineering arc flash cost](https://www.zechengineers.com/arc-flash-study-cost/), [e-Hazard cost](https://e-hazard.com/how-much-does-an-arc-flash-study-cost/), [CIMA+ AI arc flash](https://www.cima.ca/en/blog/arc-flash-studies-through-artificial-intelligence/), [ETAP](https://etap.com/product/arc-flash-software)
- [DOJ extension (Duane Morris)](https://www.duanemorris.com/alerts/doj_extends_ada_title_ii_digital_accessibility_deadlines_one_year_0426.html), [adatitleiii.com](https://www.adatitleiii.com/2026/04/doj-extends-ada-title-ii-website-accessibility-deadlines-for-governmental-entities-but-litigation-and-compliance-risks-remain/), [HHS 504 extension](https://www.hhs.gov/press-room/hhs-extends-mobile-and-web-accessibility-deadline.html)
- [Ohio State $20M (Inside Higher Ed)](https://www.insidehighered.com/news/government/colleges-localities/2026/01/21/higher-ed-prepares-new-era-ada), [UC Tech News](https://uctechnews.ucop.edu/pdf-accessibility-trends-in-higher-education/), [CampusMind comparison](https://campusmind.ai/blog/best-pdf-remediation-tools-higher-education), [PDF cost guide (Venngage)](https://venngage.com/blog/pdf-accessibility-cost/)
- [Purdue ink2html](https://www.purdue.edu/online/purdue-launches-new-accessibility-app-that-converts-handwritten-text-to-compliant-html/), [Purdue Title II FAQ](https://www.purdue.edu/innovativelearning/tools-resources/accessibility/ada-title-ii-compliance-faqs), [Mathpix accessibility](https://mathpix.com/use-cases/accessibility), [Title II exceptions (UW System)](https://www.wisconsin.edu/digital-accessibility/exceptions-to-title-ii/)
- [Pax (YC)](https://www.ycombinator.com/companies/pax), [Zollback](https://www.zollback.com/), [Fortuna Health raise](https://www.businesswire.com/news/home/20250721481890/en/Fortuna-Health-Raises-$18M-Led-by-Andreessen-Horowitz-to-Modernize-Medicaid-Access-and-Infrastructure-Amid-Federal-Reforms), [CMS community engagement rule](https://www.aha.org/news/headline/2026-06-01-cms-issues-interim-final-rule-medicaid-community-engagement-requirements), [CourseWise (GovTech)](https://www.govtech.com/education/higher-ed/university-developed-ai-tool-helps-simplify-transfer-process), [CMMC Phase 2 suspension](https://cabrilloclub.com/insights/cmmc-timeline-2026-key-dates), [Part 135 SMS deadline](https://www.preflightsms.com/faa-2027-sms-deadline/), [YC RFS Fall 2026](https://www.ycombinator.com/rfs)
