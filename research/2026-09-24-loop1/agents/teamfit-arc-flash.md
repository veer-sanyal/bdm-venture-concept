Two undergrads can get most of what this needs in one semester. The exception is anything tied to years of experience, like a PE license, and the business doesn't need those if it stays a software vendor. The hard input is one testing firm willing to hand over matched pairs: the photos from past studies and the finished engineering model the firm built from them. Every other requirement below can be learned, borrowed or bought.

## Skills

- **Power systems engineering, enough to run a small study on their own.** They need to understand short-circuit calculations (how much current a fault would draw), protective device coordination (which breaker trips first) and the IEEE 1584-2018 arc flash equations. They also need to be able to model a 20-bus system in ETAP by hand. This is how they earn credibility with a firm's engineering manager. If neither founder is an electrical engineer, they should recruit a senior or grad student from Purdue's Schweitzer power and energy systems group (ECE 43200 covers the basics). ETAP runs an academic program with no license fee to students, so they should check whether Purdue ECE already has it.
- **Reading photos, then mapping them to a device library.** Pulling text off a nameplate is mostly solved by current vision models. The hard part is turning "a photo of a trip unit's dials or LCD" into the exact library device and setting values in ETAP, SKM or EasyPower. A trip unit is the electronic module that decides when a breaker trips. The founders can build that mapping from manufacturers' public manuals for the few families that make up most of the installed gear: Square D Micrologic, Eaton Digitrip, GE MicroVersaTrip/EntelliGuard and Siemens ETU. The first customer's last 20 studies will show which models to do first.
- **Knowing what photos can't provide.** Some inputs never appear in a photo: the utility's available fault current (it comes in a letter from the utility), cable lengths and sizes run through conduit, relay settings stored in software, and CT ratios (the ratio of the current sensors feeding the relays). The product should output a list of these gaps for the technician, not guess them. That list is the "flag" feature.
- **Build one exporter first.** ETAP's DataX tool imports SKM and EasyPower files, EasyPower imports SKM format, and SKM accepts XML through its Data Exchange function. One SKM-format export could therefore reach all three programs. They must test early whether protective device settings survive those conversions, because settings are the data most likely to get lost.

## Access

- **Paired data (the constraint that decides everything).** Each pair is the photos from a completed study plus the stamped model built from them. Only testing firms have these, and client contracts may bar sharing. Workarounds: run the tool on the firm's own machine, have the firm strip identifying details, or ask one of the firm's clients for consent. Purdue Physical Facilities runs a lot of switchgear and may have its own studies, which could be a non-commercial test set. That is worth one email, but I did not verify it.
- **Software licenses.** They can use ETAP academic through Purdue, and should ask SKM and EasyPower for evaluation or partner licenses. The exporter is useless without the program's device library.
- **The prior model, for the change-set version.** Comparing new photos against "the site's last model" only works if the firm holds that model file. If another firm did the last study, there is nothing to compare against. So the first customers should be firms that already did the last study for their recurring maintenance clients.

## Credentials

- **A PE license.** They can't get one; it takes years of supervised experience. They don't need one if they sell software to firms whose PE reviews and stamps. In most states, selling a study directly to a facility is the practice of engineering, so they should never do it. They do need a practicing arc flash PE as an advisor. Sources: Purdue ECE's industry contacts, the Central Indiana IEEE IAS/PES chapters, or a retired PE.
- **Field safety.** Online NFPA 70E awareness training takes a few hours. On ride-alongs they observe from outside the arc flash boundary; technicians take the photos. The FE exam and NETA technician certification don't matter for this.
- **Paperwork a firm will ask for.** A mutual NDA, a data-handling one-pager (where photos are stored, who can see them, when they're deleted) and a basic LLC.

## First customers

- **Who.** Independent NETA-accredited firms in Indiana, Illinois, Ohio, Michigan and Kentucky with roughly 10 to 75 technicians. They find these through NETA's "Find a NETA Accredited Company" directory. The buyer is the owner or engineering manager who pays engineers to re-key data. First they should confirm each firm does studies in-house; some subcontract the engineering.
- **How to reach them.** Warm introductions through Purdue ECE's industrial advisory contacts, Purdue alumni at those firms (a LinkedIn search) and local IEEE chapter meetings. In spring, NETA PowerTest (March 8–12, 2027, Orlando) and the IEEE Electrical Safety Workshop (March 22–26, 2027, Reno) put most of the buyers in one place.
- **Competitors to check in week 1.** arcflash.ai advertises "Photo To Report" and an "Engineering Partners" program, which may already be this company. ETAP 2026 added an AI copilot, and its free field app already captures photos. eGalvanic is a record-keeping system and does not read photos. CIMA+ built an in-house model that classifies fuses from photos at 91% accuracy. That shows the approach works, and also that large firms build it themselves.

## A 15-week semester plan

| Weeks | Work | Done when |
|---|---|---|
| 1–2 | Demo arc flash.ai and etapAPP. The EE founder models a textbook system in ETAP. Pull the NETA directory for five states. | A 40-firm list, and a written answer on whether arcflash.ai already does this |
| 2–5 | 20 calls with firm owners and engineering managers. Ask how many hours re-keying takes per study, which program they use, and whether they hold the prior models. | 2 firms agree to share 3 completed studies under NDA |
| 3–6 | Sign up the PE advisor. Get the SKM or EasyPower evaluation license. | Advisor on record |
| 5–10 | Build extraction and library mapping for the trip-unit families in those studies. Export in the first firm's program. Output the missing-data list. | The export opens in the firm's software with no manual fixes |
| 8 | PowerTest, if this is spring semester | 10 more conversations |
| 10–12 | Timed test: the firm's engineer reviews our export against their normal re-keying on the same 3 studies. | Measured time saved |
| 12–15 | Ask for a paid next study at $500 or more. | A signed paid pilot, or a kill |

The kill rule comes from the judges' fastest test. Stop if review isn't at least 40% faster or the firm won't pay $500. A realistic good outcome for one semester is one paid pilot and one measured timing number. It is not a won market.

The weakest spot for two undergrads is the paired data. That depends on one firm owner trusting two students with client data. Weeks 2 to 5 are where this lives or dies.

A process note: this is the team-fit step in METHOD. No founder brief came with the prompt, so this answer judges two generic Purdue undergrads. I read the loop 1 files (`/Users/veersanyal/Desktop/bdm-venture-concept/research/2026-09-24-loop1/RESULT.md` and `merged.md`) to get the judges' kill criteria. I did not change or write any files.

Sources:
- [NETA accreditation overview and directory](https://www.netaworld.org/accreditation/overview)
- [PowerTest 2027 (NETA)](https://www.powertest.org/event/d9d61ab7-27af-40f8-b245-c667956c20b8/summary)
- [IEEE Electrical Safety Workshop](https://electricalsafetyworkshop.org/)
- [arcflash.ai](https://arcflash.ai/Home)
- [eGalvanic arc flash software](https://www.egalvanic.com/arc-flash-software)
- [etapAPP](https://etap.com/product/etapapp)
- [ETAP 2026 release](https://etap.com/product-releases/etap-2026-release)
- [ETAP DataX import/export](https://etap.com/product/Built-in-DataX-and-Conversion-Tools)
- [ETAP academia program](https://etap.com/industries/academia)
- [SKM data import via XML](https://industrialmonitordirect.com/blogs/knowledgebase/skm-powertools-data-file-format-and-xml-import-automation-guide)
- [EasyPower SKM import](https://help.easypower.com/ezp/24.0/Content/12_Using_EasyPower_w_Other_Programs/SKM/Importing_an_SKM_Format_File.htm)
- [CIMA+ AI arc flash studies](https://www.cima.ca/en/blog/arc-flash-studies-through-artificial-intelligence/)
- [Licensed engineers and NFPA 70E](https://www.electricalsafetypub.com/nfpa-70e/the-crucial-role-of-licensed-engineers-in-performing-arc-flash-studies-state-regulations-vs-nfpa-70e/)
- [Purdue power and energy systems courses](https://engineering.purdue.edu/ECE/Research/Areas/PES/Course-Structure)
