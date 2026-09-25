I'm the team-fit agent for this candidate. Everything below is desk research. No customer has confirmed any of it.

## Team fit: an AI-run Medicaid eligibility service for Indiana nursing-home chains

### What gates this business

The AI parts aren't the hard part: reading statements, flagging transfers, drafting letters and chasing families are all buildable in a semester. Six other things decide whether two students can run it.

1. **Legal standing to work a case.** The company works each case as the resident's authorized representative. In Indiana that means signing State Form 55366 for each resident. Under federal rule 42 CFR 435.923, an organization acting as representative must promise to follow the Medicaid confidentiality rules and the ban on reassigning provider claims (§447.10). A representative can sign the application, attend the interview, send documents, get notices, handle renewals and appear at appeals.
   - **The Navigator licence probably isn't needed.** Indiana makes most people who help with Medicaid applications get certified as Navigators. But the Department of Insurance FAQ says two groups may skip it: people helping someone who may qualify for nursing-home Medicaid, and FSSA-designated authorized representatives. This company fits both. The FAQ is dated 2019, so confirm it in writing (the Navigator contact is LaCollins@idoi.in.gov). If certification turns out to be required, it costs $50, a background check, a course and an exam.
2. **Filing, not legal advice.** Non-lawyers may collect documents and fill in and submit the application. They may not advise on how to shift assets to qualify; that is elder-law work. The transfer-explanation letters should state facts, and an Indiana elder-law attorney should review the templates. Refer families who need planning to that attorney.
3. **Health-privacy law (HIPAA).** The company becomes a "business associate" of each home. That means a signed business associate agreement (BAA) with each operator before seeing any case, and a BAA with whoever supplies the AI model. A 10-case pilot doesn't need a SOC 2 security audit; a chain-wide contract later probably will.
4. **Automated calls and texts.** The FCC ruled in February 2024 that AI-generated voices count as "artificial" under the telephone consumer law (TCPA), so calling a family with one needs their prior consent. Put the consent in the same packet the family signs to appoint the representative. Every call and text must say who is calling and offer an opt-out.
5. **A credentialed human.** The Certified Medicaid Planner credential needs two or more years of Medicaid-planning experience, or a master's degree in a related field, so neither founder can earn it this semester. They need to recruit one person: a retired business-office manager, a former Indiana caseworker (DFR is the state office that decides eligibility) or a Certified Medicaid Planner. Pay that person partly out of each approval fee. They sign off on cases and talk to caseworkers. For a buyer, that person is the credential.
6. **The PointClickCare connection can wait.** PointClickCare's developer terms charge no API fee today. But each home needs an "integration package" to connect outside apps, and partners need PointClickCare's approval. Reap is already on its marketplace. Apply now, but run the pilot on the report the operator's business office exports from its own system.

### The customer list is short and knowable

I ran CMS's August 2026 nursing-home file (primary data):
- Indiana has 507 certified homes with about 36,800 residents on an average day.
- 339 of those homes, holding 68% of residents, belong to chains of 10 to 130 facilities.

Chains with 10 or more Indiana homes:

| Chain | Indiana homes | Homes elsewhere |
|---|---|---|
| American Senior Communities | 90 | none |
| Trilogy | 62 | OH, KY, MI, WI (123 total) |
| Infinity Healthcare Consulting | 36 | IL, TN |
| Brickyard | 23 | none |
| CarDon | 19 | none |
| CommuniCare | 18 | OH, WV, MD, VA |
| TLC Management | 15 | FL, OH |
| Life Care Centers | 15 | national, 194 total (probably too big) |
| Miller's Merry Manor | 14 | none |
| Aperion | 12 | IL |
| Envive | 12 | none |
| IDE Management | 10 | none |

Majestic Care has 8 Indiana homes plus Ohio and Michigan.

The judges' test of "10 Indiana operators" is close to the whole Indiana market for this buyer, so no contact can be wasted. Two more facts shape the pitch:
- **Who bears the loss.** County hospitals own many of these homes (114 are listed as government-owned, 25 of them inside American Senior Communities). Ask on every call who absorbs the write-off: the manager or the hospital.
- **A billing change is coming.** Trade press reports that Indiana law HEA 1277 moves long-stay residents out of managed care and back to fee-for-service on July 1, 2027. Business offices will be busy with that, which helps an offer to take cases off their desk.

### What they need, and how to get it by December

| Need | How |
|---|---|
| **Indiana rule fluency** | The Indiana Health Coverage Program Policy Manual is public. Read chapter 2600 (resources and transfers) and chapter 4200 (appeals), plus §71112 of the 2025 federal budget law (the retroactive-coverage cut). Indiana Court of Appeals decisions on transfer penalties are public and make good test cases. About 2 weeks. |
| **Paperwork** | An Indiana LLC; a BAA template; a family packet (Form 55366, HIPAA authorization, call/text consent); written confirmation from IDOI on the Navigator question. Get a startup lawyer referral through Purdue Innovates. |
| **People** | One part-time eligibility veteran, paid per approval, plus one elder-law advisor. Find them through the state elder-law bar section, LinkedIn searches for ex-DFR caseworkers and business-office managers, and Purdue alumni who run homes. |
| **Product** | Build it for internal use first, not as software for customers. It reads statements (OCR), flags transfers, fills Indiana forms, tracks deadlines, and drafts letters and caseworker replies. Families' banks can supply statements through Plaid, but Plaid returns at most 24 months, so the older look-back years still mean asking banks for paper statements. |
| **Channel** | The Indiana Health Care Association (IHCA/INCAL) convention was Aug 18–19, 2026, so it has passed; use its associate membership and webinars instead. The main route is direct calls to each chain's central business office or revenue-cycle director, plus LeadingAge Indiana. |
| **Money** | The Anvil and Purdue Innovates Ventures, which fund Purdue-connected founders. Elevate Ventures wants a market of at least $500M, so this pitch should be framed nationally when talking to it. |

### Semester sequence (about 11 weeks left)

- **Weeks 1–2.** Do the paperwork above, recruit the specialist and the advisor, and email IDOI. Call all 12 chains with the judges' offer: "We take your 10 oldest pending or denied cases and are paid only on approval. Send your pending-aging report and 12 months of eligibility write-offs."
- **Weeks 3–6.** Sign BAAs and pilot letters with 3 or more operators. Sort every case by cause:
  - waiting on family documents,
  - waiting on the state,
  - never eligible,
  - lost on a missed deadline.

  That breakdown is the judges' kill test. Also ask what the home actually loses per month: the Medicaid rate minus the resident's own contribution, not the $9,300 private-pay figure.
- **Weeks 6–11.** File, re-apply or appeal. Indiana appeals must be filed within 33 days of the denial notice, and the judge decides within 90 days of the request. DFR takes up to 90 days to decide an application.

A realistic end state: two or three signed pilots, 20 to 30 live cases, a measured split of where the stuck dollars sit, several filings, and maybe a few approvals. Approvals will come only if some inherited cases were already nearly complete, because per-approval pay mostly lands after the semester ends. There will be no PointClickCare integration and no SOC 2 by December.

### Signals that should stop them
- Fewer than 3 of the roughly 12 chains hand over cases, or their lawyers won't sign a BAA with a student company.
- Most stuck dollars are waiting on the state or belong to residents who were never eligible.
- Operators say Reap, MedicaidSoft or a firm that is free to the home already covers it. Reap's own site says staff "approve every send," so "we take the case off your desk" is the difference to test.
- No experienced specialist will join on shared approval fees.

Two dates to check: the Burton D. Morgan final. Last year's was Dec 10, 2025, and this year's last workshop is Dec 3. And the Navigator exemption, whose FAQ is from 2019.

Sources:
- [IDOI Navigator FAQs](https://secure.in.gov/idoi/files/Navigator-FAQs.pdf)
- [IDOI Indiana Navigators](https://www.in.gov/idoi/indiana-navigators/)
- [DFR: Becoming an Authorized Representative](https://www.in.gov/fssa/dfr/becoming-an-authorized-representative)
- [Indiana Medicaid authorized representative form](https://www.in.gov/medicaid/members/member-resources/authorized-representative-form/)
- [42 CFR 435.923](https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-C/part-435/subpart-J/subject-group-ECFR0717d3fdf4a090c/section-435.923)
- [Krause Financial: state variations in unauthorized practice of law for Medicaid planning](https://www.krausefinancial.com/blog/state-variations-in-defining-the-unauthorized-practice-of-law-in-medicaid-planning/)
- [FCC: TCPA applies to AI-generated voices](https://www.fcc.gov/document/fcc-confirms-tcpa-applies-ai-technologies-generate-human-voices)
- [CMP Board: becoming a CMP](https://cmpboard.org/become-a-cmp/)
- [SmartAsset on the Certified Medicaid Planner](https://smartasset.com/financial-advisor/certified-medicaid-planner)
- [PointClickCare developer terms](https://developer.pointclickcare.com/spa/terms)
- [PointClickCare: become a partner](https://marketplace.pointclickcare.com/s/become-a-partner)
- [Enzo Health on PointClickCare pricing](https://www.enzo.health/resource/pointclickcare-pricing)
- [Reap](https://getreap.com/)
- [Plaid Statements](https://plaid.com/docs/statements/)
- [CMS Provider Information, Aug 2026](https://data.cms.gov/provider-data/sites/default/files/resources/328596835e6db31b2564cd733c3795f4_1786724150/NH_ProviderInfo_Aug2026.csv)
- [Approved Admissions on HEA 1277](https://approvedadmissions.com/indiana-pulls-long-stay-residents-out-of-managed-medicaid-a-warning-shot-for-every-pathways-style-state/)
- [Purdue Exponent on HEA 1277](https://www.purdueexponent.org/city_state/politics/house-bill-1277-affects-medicaid/article_41580a09-4212-4762-add0-6d814f985d6e.html)
- [IHCA sponsorship](https://www.ihca.org/sponsorship/)
- [IHCA/INCAL convention 2026](https://withorbital.com/conferences/indiana-health-care-association-convention-and-expo-2026)
- [OALP resources for FSSA appeals](https://www.in.gov/oalp/resources-for-fssa-appeals/)
- [Indiana policy manual, chapter 4200](https://www.in.gov/fssa/ompp/files/Medicaid_PM_4200.pdf)
- [Indiana policy manual, chapter 2600](https://www.in.gov/fssa/ompp/files/Medicaid_PM_2600.pdf)
- [Indiana Lawyer on a transfer-penalty appeal](https://www.theindianalawyer.com/articles/appeals-court-rules-for-fssa-in-health-care-transfer-penalty-dispute)
- [Purdue Innovates Ventures funds](https://ventures.prf.org/funds/)
- [The Anvil](https://www.anvilstartups.com/)
- [Elevate Ventures](https://elevateventures.com/purdue-hits-startup-milestone-with-200-startups-350-million-funding-in-five-years-nine-acquired-for-2-3-billion/)
- [Purdue Business: Burton D. Morgan competition](https://business.purdue.edu/news/features/2026/burton-d-morgan-venture-concept-competition.php)

I haven't written any files. The chain counts came from a CMS download in my scratchpad. Per METHOD, this report should be saved verbatim to `/home/user/bdm-venture-concept/research/2026-09-25-loop3/agents/teamfit-ltcmedicaid.md`.
