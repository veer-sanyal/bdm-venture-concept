**VERDICT: PASS.** The pain is real, but the product at $500 to $1,500 per study is a feature the software vendors can add to apps they already give away. That caps it at a small market.

## Claims checked against sources

- **Five-year review: true.** NFPA 70E 130.5(G) says the incident energy analysis must be reviewed at least every 5 years and updated after system changes ([e-Hazard](https://e-hazard.com/how-often-do-i-need-an-arc-flash-study-performed/), [Zech](https://www.zechengineers.com/blog/when-to-update-arc-flash-study/)).
- **"Enforceable" since 2023: overstated.** NFPA 70B changed from "should" to "shall" on Jan 1, 2023, and requires current one-line diagrams and a maintenance program ([Eaton](https://www.eaton.com/content/dam/eaton/services/eess/eess-documents/eaton-nfpa-70b-white-paper-wp027024Xen.pdf), [ESFI](https://www.esfi.org/nfpa-70b/)). Federal OSHA has not adopted it. It only binds where a jurisdiction, contract or insurer adopts it, or when OSHA cites it under the General Duty Clause (a catch-all duty to protect workers from recognized hazards) ([ReliaMag](https://reliamag.com/guides/nfpa-70b-compliance/), [OSHA](https://www.osha.gov/laws-regs/standardinterpretations/2003-07-25)). It creates pressure to comply, not a legal requirement.
- **Cost of $3,500 to over $100,000: true.** Published examples run from about $3,000 for one 208V panel to about $70,000 for a plant with a 115kV substation ([e-Hazard](https://www.e-hazard.com/how-much-does-an-arc-flash-study-cost/)). A practitioner on Brainfiller cites more than $100,000 for a large power park ([forum](https://brainfiller.com/arcflashforum/viewtopic.php?f=4&t=2270)).
- **Data collection is most of the labor: true.** Leaf calls data gathering and one-line development "typically the most costly part" ([Leaf](https://leafelectricalsafety.com/blog/how-much-does-an-arc-flash-study-cost)). A practitioner says his firm dropped per-point pricing because it "is no good for estimating the data collection," which needs two people on site.

## Who already serves this customer

The three software vendors own the engineer's desktop, and each already ships a field data app that syncs straight into its own model:

- **ETAP** is owned by Schneider Electric. Its etapAPP is free ([ETAP](https://etap.com/product/etapapp)), and ETAP 2026 already includes an AI copilot and AI autocomplete that suggests one-line elements ([ETAP 2026](https://etap.com/product-releases/etap-2026-release)).
- **SKM Mobile** captures photos, video and QR codes and imports into SKM's desktop program, PTW ([SKM](https://www.skm.com/myskm_cloud_mobile_app.html)).
- **EasyPower OnSite** links photos to one-line equipment ([EasyPower](https://www.easypower.com/data-collection)).
- **FlashTrack** from Facility Results has sold vendor-neutral nameplate capture since 2012 and exports to SKM, EasyPower, ETAP and ARCAD ([Facility Results](https://facilityresults.com/arc-flash-training-2/)).

None of these pages mentions AI that reads nameplates or trip-unit screens from photos, so that gap is still open. Nearby tools are shallow. SmartSLD turns a photo of a hand-drawn one-line into a diagram ([SmartSLD](https://smartsld.com/)), and Kopperfield has premium panel-photo AI aimed at contractor permit drawings. I found no company whose pitch matches this one. My web search budget ran out before I could check more names, so an exact match could still exist.

**Does an incumbent own the data and the buying channel? Yes.** The engineer's model files are in ETAP, SKM or EasyPower's proprietary formats, and each vendor has an app already sitting in the technician's hand.

## 1. The strongest version

Keep the photo-to-model engine, but change who buys it and what it holds.

- **Buyer.** Sell to the large testing firms and roll-ups, priced per technician seat or per bus, not per study. Examples are Shermco (700+ certified technicians, 41 locations) and RESA Power (50+ sites) ([iRecruit](https://www.irecruit.co/insights/neta-accredited-companies-2026-list-top-electrical-testing-firms)).
- **When capture happens.** Capture during NFPA 70B maintenance outages, when the gear is already shut off and open. That removes the hardest part of data collection, which is getting safe access to live equipment.
- **What it becomes.** Keep one living model per facility that every maintenance visit updates. The five-year restudy then shrinks to a list of changes, and the testing firm can sell the owner a yearly compliance subscription.
- **Hardest work to automate.** The biggest value is matching each device to the right entry in the modeling software's protective-device library, not the OCR itself.

A bigger alternative is to become an AI-enabled study provider that keeps the $15k study fee rather than $1k. That puts you in competition with your own customers and means running field crews.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Data gathering and one-line development is "typically the most costly part," and practitioners stopped per-point pricing because data collection was unpredictable. |
| Value over today | 3 | The current apps are free and sync natively but need manual keying. Photos remove the keying, but not cable lengths, conductor sizes or the cost of getting two people to the gear. |
| Market size | 2 | Global study services are about $1.2B (MarketIntelo, a low-quality source). Assuming roughly 30,000 to 100,000 US studies a year at about $1k each, the software market is about $30M to $100M. |
| Risk (5 = low) | 2 | ETAP is already shipping AI into the one-line, and any of the three vendors can add photo reading to a free app. A misread trip setting leads to an under-rated PPE label, so engineers may re-check every value and erase the time saved. |

## 3. What kills it, and the fastest test

**What kills it:** either of these.
- Accuracy on trip settings and device-library matches is below what engineers will trust without re-checking, so hours saved are near zero.
- ETAP or EasyPower adds photo extraction to its free app.

**Fastest test (about two weeks, no product needed):**
1. Get archived field photos and the final stamped model files for 3 recently completed studies from one testing firm.
2. Run a vision-model script over the photos.
3. Score it on two numbers:
   - The share of the final model's fields that can be derived from photos at all.
   - Field-level accuracy on trip settings and library matches.
4. In the same meeting, ask the firm's project manager how many hours were spent keying data on those three jobs.

**Kill thresholds:** below 50% field coverage, or below about 97% accuracy on trip settings.

VERDICT: PASS
