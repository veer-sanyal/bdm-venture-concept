I'd have Veer and Cole build an AI trade-compliance analyst for mid-market importers. It works out what each imported product is made of and where it came from, and keeps the proof. The first slice is Section 232 steel, aluminum and copper duties. Customs is crowded with AI startups, but the part nobody serves well yet is proving each product's facts from engineering documents and suppliers. That, not tariff-code lookup, is the pitch.

Everything below is desk research from the web; I didn't read any local project files. None of it is customer validation.

## Best idea: a proof file for every imported product

**Why now.** Since June 8, 2026 (running to Dec 31, 2027), the duty on a steel, aluminum or copper product depends on facts about the product itself:
- If metals are more than 15% of its weight, it pays 25% on its full value. Under 15% by weight, this duty doesn't apply.
- If the metal was melted in the US, the rate drops to 10%. Some machinery, farm equipment and HVAC pays 15%. Raw metal pays 50%.
- The metal weight has to be entered on the customs filing, and the importer needs a bill of materials, supplier statements and a written method behind it.
- When the importer can't give the customs broker the data, the broker often just declares the full duty. So importers overpay, or they claim the lower rate without proof.

**The cost of mistakes is large and frequent.**
- The Justice Department's trade-fraud task force recovered over $1B in about 10 months. The biggest case, Perfectus Aluminum, settled for $549.5M.
- Whistleblowers filed a record 1,297 fraud suits in fiscal 2025, and the 232 metal duties are a named enforcement priority.
- In a 2026 survey of trade teams, 76% had no traceable record of their products' materials and origins, and 76% couldn't produce product information within 24 hours when customs or a broker asked.

**Who the buyers are.** There were 239,231 US importers in 2024, including 41,531 manufacturers and 87,429 wholesalers. Small and mid-size firms bring in about a third of the $2.9T in imports.

**The spend to replace.**
- The customs brokerage market is about $5.5B.
- 64% of trade teams say they're understaffed, 41% are hiring, and new-hire pay is up 15% or more.
- On top of that come trade lawyers and consultants.
- My own unsourced estimate: 20,000–30,000 mid-size importers spending $150k–$300k a year on staff and advisors comes to several billion dollars.

**What buyers use today:**
- **Customs broker.** Paid per filing, and it files whatever the importer says. The importer carries the liability.
- **In-house staff.** Usually supplier emails and spreadsheets.
- **Lawyers and consultants.** Too expensive to cover 3,000 products one by one.
- **Free options.** Tarifflo audits past filings free and only takes a cut of refunds it wins. Brokers help with tariff codes at no extra charge, and Flexport has free tools.
- **Enterprise software.** Assent collects supplier data on where metal was melted. Altana has raised $343M at a $1B valuation and was chosen by customs for its "product passports." Thomson Reuters and E2open sell large trade-management suites.
- **AI startups.** Gaia Dynamics, GingerControl, Tarifflo, Amari (for brokers), Caspian (duty refunds on re-exports), Tandom (anti-dumping duties), Border Logic and Bruges.

**What AI can do that those can't.** Almost all of the above work from product descriptions and supplier questionnaires. This product would check the claims against the physical product:
1. **Compute metal content from engineering documents.** It reads drawings, bills of materials, spec sheets, mill certificates and photos, then works out metal weight with a worksheet that cites its sources. It flags supplier claims that don't add up, such as "12% steel" on a part with a 3mm steel housing.
2. **Chase suppliers in their own language.** It follows up by email or WeChat until the documents arrive, then reads what comes back.
3. **Check every past filing line.** It compares each line in the importer's customs records against the product file. Overpayments get corrected while the refund window is still open (up to roughly 300 days after entry, then a 180-day protest window). Underpayments get disclosed early, which reduces penalties.

**Why this wasn't possible two years ago.** Models now read technical documents and drawings reliably. Agents are above human level on short computer tasks (over 85% on the OSWorld-Verified benchmark, where humans score 72%). They are still weak on long ones (about 21% on OSWorld 2.0). So the product should be built as many short, checkable tasks, with a person signing off.

**Model.** Charge a yearly fee per active product. Get in the door with a free audit of past filings, to match Tarifflo's free offer.

**How it grows from narrow to broad:**
1. Steel, aluminum and copper duties.
2. Anti-dumping duties, where tariff codes alone don't decide coverage and the duties can exceed 100%.
3. Proving trade-agreement origin (USMCA, CAFTA-DR), which exempts goods from the new 10–12.5% forced-labor tariffs.
4. Forced-labor due diligence.
5. EU carbon border fees and digital product passports.

Long term, it becomes a shared supplier network. A supplier answers once and many importers reuse the answer, which is a network-effect moat.

**Local way in.** Indiana manufacturers through Purdue's manufacturing extension program. The Elkhart RV cluster imports a lot of aluminum and steel; that's my guess and they'd need to check it.

**What's weakest:**
- **Competition.** Altana and Assent already own the "supplier data" story at large companies, and Tarifflo gives audits away. The claim that checking engineering documents beats questionnaires is untested and is the whole case.
- **Policy risk.** The metal-duty rules changed in April and June 2026 and currently expire at the end of 2027. The answer to judges is that every tariff program depends on the same product facts, but the first slice could shrink.
- **Liability.** If the product says 14% and customs finds 16%, the customer pays. They'll need a licensed customs broker reviewing the work and insurance for errors.
- **Suppliers can refuse or lie.** The physics check helps but doesn't fully solve this.
- **No domain expertise yet.** Two undergrads need a trade-compliance advisor early.

**First test.** Interview about 20 trade-compliance managers and 5 brokers. Ask what they declare when they have no metal data, and ask for three months of their customs records to run a back-audit. A clear result is either money found or proof they already have the data.

## Runners-up worth keeping

**1. Warranty claims for auto, RV, powersports and equipment dealers.**
- There are tens of thousands of dealers. Warranty is 30–40% of service revenue, up to 15% of warranty gross profit leaks, and manufacturers claw back paid claims after audits.
- Dealers use in-house warranty clerks, outsourced processing firms, their dealer software's warranty module, and firms that win higher repair rates for a cut of the gain.
- AI checks the technician's notes, photos and fault codes against each manufacturer's policy and service bulletins before submitting, so the claim survives an audit.
- **Weakest:** Forge AI already does exactly this, dealer software vendors could bundle it, the rules differ per manufacturer, and deals are small. The Elkhart RV angle is a guess I haven't checked.

**2. Claims and pharmacy-benefit oversight for self-insured employers.**
- A 2026 federal law (the Consolidated Appropriations Act, 2026) puts new duties on employers to monitor their benefit vendors.
- Audits review about 5% of claims; checking all of them usually recovers 1–3% of claims spend.
- Employers use claims administrators (who check their own work), benefits brokers (paid by commission, so "free" to the employer) and audit firms.
- **Weakest:** getting the data depends on the claims administrator cooperating, ClaimInformatics and CodaHx are already there, and sales go through conflicted brokers.

**Rejected for crowding or policy risk:**
- **Construction change orders:** Trunk Tools, Provision and Document Crunch are already there.
- **Defense-contractor cybersecurity certification (CMMC):** the Pentagon suspended the next phase in July 2026, and many tools exist.
- **Commercial property tax appeals:** Ownwell, Reserve Tax AI and contingency firms.
- **Nursing-home billing assessments:** MedaSync and PointClickCare.

Sources:
- [Skadden – IEEPA refunds](https://www.skadden.com/insights/publications/2026/03/tariff-refund-mechanism-takes-shape)
- [C.H. Robinson – June 2026 Section 232 update](https://www.chrobinson.com/en-us/resources/insights-and-advisories/client-advisories/2026q2/06-02-2026-client-advisory-updates-to-section-232-tariffs-on-steel-aluminum-copper/)
- [Mallory – 15% threshold](https://www.mallorygroup.com/blog-posts/section-232-tariff-update-new-15-de-minimis-threshold-details-for-u-s-importers)
- [Honigman – Section 301 forced-labor tariffs](https://www.honigman.com/alert-3462)
- [ArentFox – False Claims Act mid-2026](https://www.afslaw.com/perspectives/investigations-blog/baseline-not-finish-line-fca-customs-enforcement-mid-year-2026)
- [Morgan Lewis – Perfectus settlement](https://www.morganlewis.com/pubs/2026/05/doj-announces-major-fca-settlement-relating-to-evaded-customs-duties)
- [AAEI/Altana survey](https://www.financialcontent.com/article/bizwire-2026-9-23-more-than-half-of-enterprise-trade-teams-arent-ready-for-modern-trade-demands-aaei-and-altana-survey-finds)
- [Gateway salary survey](https://gatewayrecruiting.com/2026-trade-compliance-salary-survey/)
- [Thomson Reuters 2026 trade report](https://www.thomsonreuters.com/en-us/posts/corporates/2026-global-trade-report/)
- [Census importer profile](https://www.census.gov/foreign-trade/Press-Release/edb/edbrel2024.pdf)
- [Mordor – customs brokerage market](https://www.mordorintelligence.com/industry-reports/united-states-customs-brokerage-market)
- [Altana/CBP product passports](https://www.businesswire.com/news/home/20251001718752/en/U.S.-Customs-and-Border-Protection-Selects-Altanas-AI-Powered-Product-Passports-to-Drive-Next-Generation-Supply-Chain-Traceability-Trusted-Trade)
- [Altana funding (Tracxn)](https://tracxn.com/d/companies/altana-technologies/__daylA5vt7W5ta18Wp3y318Q_KOAt9RwvMplp4oiOB5Y)
- [Assent – Section 232](https://www.assent.com/blog/prepare-for-section-232-tariffs/)
- [Tarifflo](https://www.tarifflo.com/)
- [Gaia Dynamics](https://www.gaiadynamics.ai/)
- [TechCrunch – Amari AI](https://techcrunch.com/2026/02/19/this-former-big-tech-engineers-are-using-ai-to-navigate-trumps-trade-chaos/)
- [Caspian seed round](https://pulse2.com/caspian-5-4-million-seed-funding-raised-for-ai-based-customs-compliance/)
- [Tandom](https://compliance.tandom.ai/)
- [OSWorld benchmark](https://benchmarkingagents.com/osworld/)
- [OSWorld 2.0](https://arxiv.org/abs/2606.29537)
- [Forge AI](https://www.forgedrive.ai/)
- [Claimlane – dealership warranty](https://www.claimlane.com/resources/blog/dealership-warranty-management)
- [Benosphere – claims audits](https://benosphere.com/blog/self-funded-claims-audit-5-percent-problem)
- [ClaimInformatics](https://www.claiminformatics.com/post/2026-compliance-outlook-self-funded-fiduciaries)
- [Cabrillo Club – CMMC suspension](https://cabrilloclub.com/insights/cmmc-timeline-2026-key-dates)
