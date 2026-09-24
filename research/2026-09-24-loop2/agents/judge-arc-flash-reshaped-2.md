I'd pass. The problem is real and I found no company pitching this exact product. But the version sold through testing firms has a small ceiling, and the two data sources it depends on are held by incumbents: the test reports (Megger PowerDB) and the study models (ETAP, owned by Schneider).

**Checking the key claims**
- **Schneider's 400-site audit: true.** Schneider's July 2025 blog says 89% of 400 audited sites had no single-line diagram or only a partial one. Schneider sells diagram and study services, so it has an interest in that number.
- **NFPA 70B: true, but I couldn't read the standard itself.** The full text needs an NFPA login, so this rests on industry write-ups. The 2023 edition turned 70B into a mandatory standard. Chapter 6 says one-line diagrams must be "kept current." It also says arc flash studies must be updated after major changes and reviewed at least every 5 years. A 2026 edition came out in September 2025. 70B is a voluntary standard, not law.
- **"Firms visit every one to three years": overstated.** 70B sets maintenance intervals from 12 to 60 months depending on equipment condition. Equipment in good condition can go 5 years between visits, the same as the study cycle.
- **Pricing context.** Arc flash studies run about $3.5k to $100k per site, so $500 to $1,200 a year is roughly 10–40% of what a site spends on studies per year.

**Who else serves this customer**
- **ETAP (bought by Schneider in 2021).** Its field app collects data straight into the model and links photos to devices. Its eProtect product already compares relay settings as designed against as found. ETAP 2026 adds an AI copilot. This is the closest incumbent, but it only works for ETAP users, and Schneider's own field service arm competes with the independent testing firms.
- **EasyPower (bought by Bentley in 2023)** has data-collection templates. SKM is still independent.
- **Test data:** Megger's PowerDB is the standard reporting tool at NETA testing firms, so it effectively holds the test data. Rapid Reports and FieldTestPRO are smaller.
- **Neighbouring startups:** Condoit ($4.25M seed in 2024; contractors, one-lines, arc flash data collection), eGalvanic, and REALTIMEais ($524 to $3,569 a year; ETAP integration; flags assets for arc flash reassessment).
- **No close match.** None of these reads test reports and relay setting files and compares them against SKM or EasyPower models.
- **Who owns the data and the buying channel:** Megger owns the test-data format. The study models belong to whichever engineering firm did the study, which is ETAP for Schneider sites. The testing firms are the channel themselves, and they're consolidating (Shermco has 41 locations, RESA 50+, Asplundh Electrical Testing formed from a 2023 merger).

**1. The strongest version**
A tool for large NETA testing firms that also do studies, so they already hold the model file. It sits between PowerDB exports and relay setting files (SEL, GE) on one side and SKM, EasyPower and ETAP device tables on the other. It flags only changes that move incident energy or a label's category, and turns each flag into a ready-to-sign update quote. Start with SKM and EasyPower sites, where Schneider isn't the incumbent, and with low-voltage breaker trip units and relays. Pitch it as a revenue engine for study updates rather than a compliance tool.

**2. Ratings**

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 3/5 | The drift is real (89% of sites lack a full diagram; mandatory 5-year review), but the compliance pain sits with the facility owner. Testing technicians already record as-found and as-left settings. |
| Value over today | 3/5 | It replaces manual checks against settings sheets and creates update leads, but eProtect already does settings comparison for ETAP users. |
| Market size | 2/5 | A few hundred NETA firms; I estimate (unverified) 50k–150k sites × ~$800 ≈ $40–120M a year at most. |
| Risk | 2/5 | Getting the model files, reverse-engineering proprietary formats, engineer sign-off liability, conservative buyers, and Schneider/ETAP can extend eProtect. |

**3. What kills it, and the fastest test**
It dies if testing firms don't hold the current model for most sites they maintain, or if drift that actually changes a label is rare. Either way there's nothing to match against and no update work to resell.

Fastest test (2–3 weeks, no software): get two or three NETA firms to hand over the last two maintenance cycles of PowerDB reports plus the study models for 20 sites each. Do the matching by hand. Measure three things:
- the share of sites where a current model is available;
- the share with drift that changes a label;
- whether the firm will quote those updates and pay for a pilot.

Under about 30% model availability or 20% material drift would kill it. This is desk research, not customer validation; that test is the validation.

Sources:
- [Schneider blog, 400-site audit](https://blog.se.com/services/2025/07/07/getting-to-know-your-power-infrastructure-a-guide-to-the-big-picture/)
- [IEEE ESW paper on NFPA 70B-2023](https://electricalsafetyworkshop.org/wp-content/uploads/sites/255/ESW-2023-18.pdf)
- [REALTIMEais on 70B Chapter 6](https://realtimeais.com/nfpa-70b/nfpa-70b-chapter-6-system-studies/)
- [REALTIMEais 70B software and pricing](https://realtimeais.com/nfpa-70b-compliance-software/)
- [CBM Connect on study requirements](https://www.cbmconnect.com/arc-flash-studies-why-and-when-are-they-required/)
- [C&H Electric on 70B condition levels](https://chelectric.com/nfpa-70b-equipment-condition-levels/)
- [e-Hazard on study costs](https://e-hazard.com/how-much-does-an-arc-flash-study-cost/)
- [Zech Engineering on study costs](https://www.zechengineers.com/arc-flash-study-cost/)
- [etapAPP](https://etap.com/product/etapapp)
- [ETAP eProtect](https://etap.com/solutions/eprotect)
- [ETAP 2026 what's new](https://etap.com/products/whats-new)
- [Schneider acquires ETAP](https://www.se.com/ww/en/about-us/newsroom/news/press-releases/schneider-electric-invests-in-operation-technology-inc-%E2%80%9Cetap%E2%80%9D-to-spearhead-smart-and-green-electrification-5fb224cc8c11a759eb3b4e16/)
- [Bentley acquires EasyPower](https://www.geoconnexion.com/news/bentley-systems-announces-acquisition-of-easypower-power-systems-engineering-software-provider)
- [PowerDB Pro](https://www.megger.com/en/products/powerdbtm-pro-asset-and-test-data-management-software)
- [Rapid Reports](https://www.rapidreportsapp.com/)
- [Condoit](https://www.condoit.io/)
- [Condoit seed round](https://www.finsmes.com/2024/04/condoit-raises-4-25m-in-seed-funding.html)
- [eGalvanic](https://www.egalvanic.com/arc-flash-software)
- [NETA firm landscape](https://www.irecruit.co/insights/neta-accredited-companies-2026-list-top-electrical-testing-firms)

VERDICT: PASS