I'd pitch an AI tool that turns photos of a facility's electrical equipment into the ready-to-run model an arc flash study needs. My runner-up has the better proof that customers are losing money: warranty-claim recovery for RV, boat, powersports and farm-equipment dealers. All of this is desk research. None of it is customer validation.

One process note first. Following the project's routing rules, I read `METHOD.md` and `STATE.md` before generating, so the previously selected concept and round 17 were in my context. The four research lanes I ran in parallel were given only the brief. The web-search budget (200 calls, shared with the lanes) ran out partway through, so several competitor checks are incomplete. I say which ones below.

## Best idea: electrical safety studies built from photos

**The problem.** Under NFPA 70E, the electrical safety standard OSHA relies on, any site where people work near live equipment needs an arc flash study. It is redone at least every five years. The study models the whole electrical system to work out how much energy an electrical explosion would release at each panel and what protective gear a worker needs. Since 2023, NFPA 70B has also required a written electrical maintenance program backed by condition assessments.
- An engineering firm prices a study at $3,500 to $22,000 or more depending on size ([Zech Engineering](https://www.zechengineers.com/arc-flash-study-cost/)). A medium plant runs $15,000 to $40,000 ([f7i](https://f7i.ai/blog/arc-flash-testing-requirements-the-complete-guide-to-analysis-compliance-and-safety-cycles)).
- Photographing equipment, reading nameplates and redrawing the wiring diagram (the "one-line") is 40 to 60 percent of the effort. That figure comes from an Electrical Contractor magazine piece I saw only as a search snippet (the page returned 403). An arc flash practitioner forum ([Brainfiller](https://brainfiller.com/arcflashforum/viewtopic.php?f=4&t=4188)) describes most firms still working on paper, with transcription errors and hours spent sorting photos.

**The product.**
- A qualified electrician photographs panels with a guided app.
- A vision model reads nameplates, breaker ratings, fuse types and labels, then builds the one-line. Anything it cannot see, like which conduit feeds which panel, gets flagged for a person to trace.
- It exports a model the existing study software already takes. EasyPower's 2026 release imports data and lays out one-lines automatically ([EasyPower](https://www.easypower.com/)).
- The licensed engineer (PE) runs the study and stamps it, as today.

**Who pays.**
- To start: small study firms and electrical testing companies, paying per study. The engineer keeps the liability.
- Later: facility owners, paying a per-site subscription that keeps the model current between five-year studies.

**Why it could work.**
- I found no AI-native competitor. That matters because every document-review vertical I checked already has several.
- ETAP's field app captures photos but has you type nameplate data in by hand ([ETAP](https://etap.com/product/etapapp)).
- REALTIMEais manages this data for $524 to $3,569 a year but doesn't read photos ([REALTIMEais](https://realtimeais.com/nfpa-70b-compliance-software/)).
- CIMA+, an engineering firm, built an internal model that classifies fuses in survey photos at 91 percent accuracy, which shows the task is doable ([CIMA+](https://www.cima.ca/en/blog/arc-flash-studies-through-artificial-intelligence/)).
- The study recurs every five years by rule, the photo library becomes a moat, and Purdue's power engineering faculty and Indiana plants give the team access.

**Narrow to broad.**
1. Arc flash data capture.
2. The NFPA 70B maintenance program for the same sites.
3. A live electrical model for multi-site owners, data center commissioning and insurers' risk data.

**Market (my estimate, not sourced).** About 100,000 to 150,000 US sites at roughly $12,000 per five-year study is about $250 to 350 million a year in study spend. A site subscription priced like REALTIMEais adds a similar amount.

**Weakest points.**
- The competitor check is the thinnest of any candidate. The search budget ran out before I could check YC's directory (it doesn't render without JavaScript) or whether Eaton and Schneider have AI apps. From memory, and unverified, Schneider owns ETAP; if so, a large incumbent sits on the study-software channel.
- Photos can't show wiring hidden in conduit, and a wrong model can get someone hurt, so liability and accuracy are the real risks.
- I have no direct quote from a buyer describing the pain.

**Fastest test.** Get one small study firm's archive of a finished study: the photos plus the final model. Check whether the AI rebuilds the model from the photos alone, and how many hours that saves.

## Runners-up

**1. Warranty recovery for RV, boat, powersports and farm-equipment dealers.**
- **The idea.** An AI-native service reads repair orders, technician notes and photos, then files and appeals claims with each maker and component supplier. It is paid a share of the money recovered.
- **Why it could work.**
  - Two lanes found this independently.
  - I confirmed that one top-50 RV dealer found $45,000 in unfiled claims over 60 days, and that "bad paperwork" is the number one reason claims are denied ([RV News](https://www.rvnews.com/opinion-making-money-with-rv-warranties-without-losing-your-mind/)).
  - Makers paid large 2025 warranty bills: Deere $1.33B, AGCO $415M, Thor $241M, Winnebago $98M ([Warranty Week](https://www.warrantyweek.com/archive/ww20260521.html)).
  - The model is proven for car dealers: WarrCloud has raised $40M ([Auto Remarketing](https://www.autoremarketing.com/ar/technology/warrcloud-continues-positive-moves-with-20m-in-series-b-funding-led-by-centana-growth-partners/)), but it serves only car dealers.
  - Elkhart is two hours from campus.
- **Weakest.**
  - About 3,000 RV dealers alone is only around $36M. It takes the other dealer types together to reach the lane's estimate of $135 to 300M.
  - Laws forcing makers to pay retail rates vary by state and by vertical. Without them this is plain claim processing, which dealers are used to buying at 2 to 4 percent of claims paid, not 30 percent.
  - The car-dealer companies could extend into these verticals.
- **Test.** Get three Elkhart dealers' denied and unfiled claims from last quarter and count what is recoverable.

**2. Credit-report dispute triage for lenders and collectors.**
- **The idea.** Any company that reports accounts to the credit bureaus must investigate each consumer dispute within about 30 days. AI tools now write those disputes in bulk. The product sorts them, pulls the account evidence and drafts a response that holds up in court.
- **Why it could work.** I confirmed that CFPB complaints doubled to 6.6 million in 2025, 88 percent of them about credit reporting, and the CFPB blames AI agents for the flood ([Orrick](https://infobytes.orrick.com/2026-04-10/cfpb-reports-complaint-volume-doubled-in-2025-citing-surge-in-credit-reporting-disputes/)). The lane found no dedicated startup.
- **Weakest.** The bureaus or the CFPB could choke off the flood; the CFPB already changed its complaint rules in June 2026. Selling to banks is slow, and the team has no access. The lane's market estimate is $125 to 230M.

**3. Medicaid "medically frail" exemption coding for community health centers.** Medicaid work requirements start January 1, 2027 under a CMS interim rule issued June 1, 2026, and states will find exempt patients mainly through diagnosis codes. The product would fix clinics' coding so eligible patients don't lose coverage. The weakest points: self-attestation through 2027 delays the pain to 2028, Fortuna Health (YC, a16z-backed) is next door, and the policy could be reversed. I did not verify this one myself.

## For the merge step

- The Indiana lane independently came up with supplier-side warranty chargeback defense, which is the previously selected concept. That is independent convergence, not new evidence. It named the same weakness, that suppliers won't fight a customer who controls future business.
- The dealer-side idea avoids that weakness, since filing a routine claim is expected rather than a fight.

**Killed, with reasons:**
- Aircraft logbook AI: Bluetail, LogAir, AeroLogBooks, WingFlow, ProvenAir.
- Phase I environmental site assessments: CaseMark, Build, V7.
- Parent IEP advocacy: at least six AI apps.
- Nursing-home Medicaid applications: CoreCare, ExaCare.
- CMMC: DoD paused Phase 2 on July 13, 2026.
- ADA Title II accessibility: deadlines moved to 2027 and 2028, and PDF fixing is down to $0.30 a page.
- Medical-device complaint handling: Smarteeva files about a third of FDA reports.
- Commercial property tax appeals: Ownwell raised $50M.
- AI oral exams: 19 platforms already.

**Left unchecked when the search cap hit:** pharma, aviation repair shops beyond logbooks, agriculture, hospice, school Medicaid, EU CBAM.

I wrote no files and committed nothing.
