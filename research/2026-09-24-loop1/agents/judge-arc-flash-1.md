I checked the pitch's claims against sources and found three problems. The "enforceable" claim is overstated. The per-study price caps revenue at tens of millions. Free field-collection tools from the two largest modeling vendors already sit in the workflow. Verdict at the end: pass.

## Claim check

- **Five-year review and update after changes: true.** NFPA 70E 130.5(G) says the arc flash risk assessment must be reviewed at intervals of no more than five years and updated after major changes ([Tyndale](https://tyndaleusa.com/nfpa-70e/130-5-a-d-arc-flash-risk-assessment/), [Zech](https://www.zechengineers.com/blog/when-to-update-arc-flash-study/)). NFPA 70B-2023 Chapter 6 adds current single-line diagrams and study intervals of no more than five years ([Eaton white paper](https://www.eaton.com/content/dam/eaton/services/eess/eess-documents/eaton-nfpa-70b-white-paper-wp027024Xen.pdf)).
- **"Made enforceable": overstated.** In 2023, 70B changed from a recommended practice ("should") to a standard ("shall"). It becomes law only where a jurisdiction, regulation, contract or insurer adopts it. Federal OSHA has not incorporated it. OSHA can use it as evidence in a General Duty Clause citation ([Reliamag](https://reliamag.com/guides/nfpa-70b-compliance/), [Gimba](https://gimba.io/is-nfpa-70b-required-by-osha/)).
- **Cost range: true.** Studies run from about $3,000 to $3,500 for small sites ([e-Hazard](https://e-hazard.com/how-much-does-an-arc-flash-study-cost/), [Zech](https://www.zechengineers.com/arc-flash-study-cost/)) up to $100,000 and more ([Leaf](https://leafelectricalsafety.com/blog/how-much-does-an-arc-flash-study-cost)).
- **"Much of the labor is copying and re-keying": true in direction.** e-Hazard's example is a $70,000 food plant: 15 days of data gathering, 5 weeks of modeling and 7 days of labeling. Leaf says a customer who helps with data collection cuts the base price by 15 to 20%. I found no source that gives an exact percentage.

## Who else serves this customer

- **Egalvanic (Milwaukee, founded 2019, $1.9M raised, about 10 staff).** It is the closest match. Its app is sold to service providers for medium- and high-voltage gear and covers arc flash data collection, single-line editing, photo tools and SKM, EasyPower and ETAP integration ([App Store](https://apps.apple.com/us/app/z-platform/id6751442873), [site](https://www.egalvanic.com/)). It is a broader maintenance platform, not an almost-exact match to this pitch, so I treat it as a competitor. Six years at that size suggests this buyer adopts software slowly.
- **ETAP (Schneider Electric has owned 80% since 2021).** Its etapAPP is a free field-collection app that syncs one-lines, equipment data and photos straight into ETAP ([ETAP](https://etap.com/product/etapapp)). It does not read photos automatically today.
- **EasyPower (bought by Bentley in 2023).** It offers data-collection templates and imports SKM files ([Business Wire](https://www.businesswire.com/news/home/20230223005979/en/Bentley-Systems-Announces-Acquisition-of-EasyPower-Leader-in-Power-Systems-Engineering-Software)).
- **FlashTrack (Facility Results).** A free data-collection tool that works with SKM, EasyPower and ETAP ([link](https://facilityresults.com/arc-flash-data-collection-software-download/)).
- **Gimba.** 70B compliance software for facility owners that imports SKM files.
- **CIMA+, an engineering firm.** It built an in-house neural network that classified 91% of components correctly in photos it had not seen before, and it may sell the tool ([CIMA+](https://www.cima.ca/en/blog/arc-flash-studies-through-artificial-intelligence/)).

**Does an incumbent own the data or the buying channel?** Partly. ETAP and EasyPower own the model files and are already in every engineer's workflow with free field apps. A lot of study volume goes through equipment makers' service arms (Schneider, Eaton, Siemens), which will use their own tools. The independent NETA-accredited testing firms are the open channel.

## 1. Strongest version

Sell to independent NETA testing firms (the accredited electrical testing and maintenance contractors), and bill per site per year instead of per study. Under 70B, these firms already visit the gear every one to three years for maintenance. On each visit the tech photographs the gear. The product compares the photos with the site's last model and flags what changed: a swapped breaker, a moved trip setting, a new feeder. It then outputs a change set for ETAP, SKM or EasyPower.

That turns a study done once every five years into a continuous update service the firm can sell to its clients. The pitch shifts from "save technician hours" to "sell more study updates." The first full study builds the baseline model.

The hard part is not reading the nameplate. It is matching the photographed trip unit to the correct device entry in each modeling program's library, and flagging data that photos cannot supply, such as cable lengths and settings hidden behind covers.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | In e-Hazard's $70,000 study, data gathering plus modeling took about 7 of 8 weeks of effort. |
| Value over what customers use today | 3 | The free etapAPP and FlashTrack already structure field capture. What's new is automatic reading from photos, and 91% accuracy (CIMA+) still leaves engineers checking every value before they stamp. |
| Market size | 2 | One analyst puts study services at $1.2B worldwide. At about $1,000 on a typical $10,000 to $15,000 study, the US ceiling is roughly $35–65M a year unless the per-site update product works. |
| Risk (5 = low) | 2 | Schneider's ETAP could add photo reading to a free app it already ships, and the stamping engineer's liability sets a very high accuracy bar. |

The market-size figure is my own estimate. It rests on a low-quality analyst number, so read it as a rough order of magnitude.

## 3. What kills it, and the fastest test

**What kills it:**
- Engineers re-verify every extracted value anyway, so the hours saved are worth less than the $500 to $1,500 price.
- The real bottleneck is outage windows and cable tracing, not typing.
- ETAP or Bentley ships photo reading for free.

**Fastest test (about 2 weeks):**
1. Get the photo archive and the final stamped model from 3 completed studies at one independent NETA firm. Firms keep hundreds of photos per study.
2. Produce the export using the models plus a human cleanup pass.
3. Have the firm's engineer time a review of that export against their normal re-keying.
4. Ask for a paid pilot on their next study.

**Kill rule:** kill it if review time is not at least 40% below normal entry, or if the firm will not pay $500 or more for the next one.

VERDICT: PASS
