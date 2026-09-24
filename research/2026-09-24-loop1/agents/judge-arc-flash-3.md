Short answer: the pain is real and the standards back it, but this is a small market, and the incumbents own both the file format and the field app. It could be a good bootstrapped business. It is not a venture bet at this price.

**Claim check against sources**
- **Five-year review: correct.** NFPA 70E 130.5(G) requires the arc flash risk assessment to be reviewed at least every 5 years and updated after a major modification. NFPA 70B-2023 6.7.2 also requires the arc flash analysis to be reviewed at least every 5 years. It sets the same interval for the short-circuit study (6.3.3) and the coordination study (6.4.3).
- **The 2023 revision: partly correct, and overstated.** NFPA 70B-2023 did change "should" to "shall", effective January 16, 2023. Single-line diagrams "shall be kept accurate" and must show their last revision date (6.2.2 and 6.2.3), and owners must document an electrical maintenance program. But OSHA has not adopted 70B. It becomes enforceable only where a jurisdiction, a regulation, a contract or an insurer requires it. OSHA can also cite it as evidence under its General Duty Clause (the catch-all rule for hazards no specific OSHA standard covers).
- **$3,500 to over $100,000: correct.** Published estimates run from $3,000 to $7,500 for small sites and $75,000 to $500,000 for very large ones.
- **Data collection is the heavy part: supported.** Industry write-ups put data collection at 40 to 50% of study cost. One e-Hazard example, a $70,000 food plant, took 15 days on site to gather data, 5 weeks to model and 7 days to label.

**Who already serves these firms**
- **ETAP (owned by Schneider Electric; ownership is from memory, not re-checked).** Its free etapAPP already captures photos, nameplate data and one-line diagrams in the field and syncs them into ETAP. Its AI assistant, Electric Copilot, builds and edits one-lines from chat commands. No vision or OCR on nameplate photos yet.
- **EasyPower.** EasyPower OnSite is a tablet app with photos and templates. EasyPower 2026 added CSV import of app-collected data and automatic one-line layout. That takes away most of the "we draw the one-line" pitch.
- **FlashTrack (Facility Results).** Data-collection software that works with SKM, EasyPower and ETAP. It claims contractors see profit increases as high as 60%. No AI.
- **Owner-side tools.** Gimba sells 70B maintenance-program software to facility owners and imports SKM study files. CMMS vendors (maintenance-tracking software) such as f7i want the arc flash data stored inside their systems.
- **No company pitching this idea.** I found nobody offering AI that reads nameplates and trip units from photos and exports an ETAP, SKM or EasyPower model. The one lead, a Mike Holt forum thread about a data-collection tool, returned 403 and I could not read it.
- **Incomplete sweep.** I hit the session's web-search limit, so a stealth startup could be missing from this list.

**Does an incumbent own the data or the buying channel? Yes, partly.** Every target firm already pays ETAP, SKM or EasyPower for a license. ETAP and EasyPower already put a free app in the technician's hands, and they control the import formats this product would depend on. Adding vision to etapAPP is a feature release for them, not a new company.

**1. The strongest version**
Sell to NETA-style testing firms, not to study engineers. These firms already open the gear every year or so for maintenance testing, often during outages when covers are off and trip-unit screens can be reached. The product captures and checks the data during that routine work and keeps a current per-facility model in ETAP, SKM or EasyPower format. The firm can then sell the five-year update and the 70B "keep the single-line accurate" duty cheaply as a recurring service.

Charge per facility per year rather than per study. The defensible asset is a living electrical model of each facility, which the testing firm carries from site to site. Photo OCR on its own is not defensible.

**2. Ratings for that version**
- **Customer need: 4.** Data collection is 40 to 50% of study cost, and both 70E 130.5(G) and 70B 6.7.2 force a review at least every 5 years.
- **Value over today: 2.** Free etapAPP and EasyPower OnSite already handle photo-linked structured capture and one-line export, and EasyPower 2026 lays out one-lines automatically. The real gap left is reading and checking the values. Photos also cannot supply cable lengths, conductor sizes or settings behind closed covers.
- **Market size: 2.** My rough estimate is 50,000 to 100,000 US studies a year at $500 to $1,500 each, about $50M to $150M a year. That rests on roughly 250,000 manufacturing sites plus commercial critical facilities, most of them on a 5-year cycle and not all compliant. It is my own estimate, not a sourced figure. The buyers are many small firms.
- **Risk: 2.** ETAP (Schneider) and EasyPower control both the file formats and the field app. The stamping engineer's liability may also force them to re-check every extracted value, which would erase the time saved.

**3. What kills it, and the fastest test**
It dies if either of two things turns out true:
- The fields photos can actually capture are a small share of the study's hours. Walking the site, measuring cables and opening gear remain.
- Engineers will not trust extracted values without re-checking every one.

Either way the saving drops below about 15% of study hours, and ETAP can match whatever is left with a free-app update.

The fastest test needs no product and takes about a week. Get two or three completed, stamped studies from one partner firm, along with the photos its technicians already took. Run a current vision model over those photos. Then measure two things against the final stamped model:
- the share of model input fields that appear in the photos at all
- the field-level accuracy on those that do

Have the firm's engineer time how long a review takes. Continue only if photos cover at least 60% of fields at 95% or better accuracy and the review is clearly faster than re-keying. Those thresholds are my own proposal.

Sources:
- [NFPA 70B Chapter 6 (Gimba)](https://gimba.io/nfpa-70b-chapter-6-single-line-diagram-system-studies/)
- [70B enforceability (Gimba)](https://gimba.io/is-nfpa-70b-required-by-osha/)
- [ELECTRI NFPA 70/70E/70B overview](https://www.electri.org/wp-content/uploads/2025/12/ELECTRIGuideNFPA70_Chapter-1.pdf)
- [Zech Engineering 5-year rule](https://www.zechengineers.com/blog/when-to-update-arc-flash-study/)
- [e-Hazard cost examples](https://e-hazard.com/how-much-does-an-arc-flash-study-cost/)
- [Leaf Electrical Safety costs](https://leafelectricalsafety.com/blog/how-much-does-an-arc-flash-study-cost)
- [etapAPP](https://etap.com/product/etapapp)
- [ETAP what's new](https://etap.com/products/whats-new)
- [EasyPower OnSite](https://www.easypower.com/resources/article/data-collection-part-3-mobile-data-collection-with-easypower-onsite)
- [FlashTrack](https://facilityresults.com/arc-flash-training-2/)
- [Gimba](https://gimba.io/)
- [f7i](https://f7i.ai/blog/arc-flash-testing-requirements-the-complete-guide-to-analysis-compliance-and-safety-cycles)
- [PowerSafe on AI](https://www.powersafe-engr.com/post/ai-in-arc-flash-analysis-what-the-future-looks-like)

VERDICT: PASS
