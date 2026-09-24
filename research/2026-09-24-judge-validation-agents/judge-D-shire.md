I ran 25 web searches and fetches. Three facts shape the answer:

- **A YC-backed company is already selling this exact pitch.** [Shire](https://shireintelligence.com/) describes itself in nearly the same words, and it also sells a full POS. Its camera-only product costs $150 a month and up per location. It claims "7 min faster table turns" and "14% more guests served per month". Those are the company's own claims, and I found nothing independent that confirms them.
- **Someone tried this before and it did not take.** [Presto Vision](https://thespoon.tech/presto-launches-computer-vision-system-for-front-of-house-restaurant-operations/) piloted cameras in Outback lobbies in 2019 and planned a dining-room version. Nothing more came of it. Nasdaq [delisted Presto in September 2024](https://www.restaurantdive.com/news/presto-automation-delisted-from-nasdaq-during-voice-ai-pivot/723684/), after 2019 camera AI cost far more to run than it does now.
- **The core claim has support in primary research.** Sheryl Kimes's Cornell study of [Chevys Arrowhead](https://www.researchgate.net/publication/238302631_Restaurant_Revenue_ManagementImplementation_at_Chevys_Arrowhead) found most of the wasted table time fell before and after the meal, especially while guests waited to pay. Cameras can see those moments. The POS cannot.

## 1. The strongest version

The strongest version is narrower than the pitch. Sell to multi-unit casual-dining groups, from 20 to 500 locations, whose peak shifts have a wait at the door. Many of the big chains run older POS systems like NCR Aloha or Oracle Simphony, where Toast is weak. The buyer is the VP of operations, and the pitch is more covers during the peak hours they already have, with no new hardware.

Start with the two table states that are easiest to detect and easiest to check: a table waiting on its check, and a table that is empty but not yet cleared. Push those alerts into the host stand the restaurant already uses (Toast Tables, OpenTable or SevenRooms) instead of replacing it. Measure the gap between the last guest leaving and the next party sitting down, and charge per location, roughly $300 to $600 a month.

Leave "ready to order" detection and pricing features until later. Don't build a POS; Shire did, and that means taking on Toast directly. The long-term asset is a record of what actually happens on dining-room floors, which later feeds staffing and pricing tools.

## 2. Ratings for that version

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Kimes found the slack in table time comes mostly after the meal, at the check. [Black Box](https://www.fsrmagazine.com/feature/restaurant-staffing-stabilizes-but-operators-face-a-new-workforce-reality/) (mid-2025) reports 40% of full-service brands are always short-staffed at the front of house. Toast's 2025 survey, as summarized in search results, says 93% of restaurants have peak waits; I could not open the page (it returned 403). |
| Value over what they use today | 3 | [Toast Tables](https://support.toasttab.com/en/article/Using-Toast-Tables-Waitlist) ($50 to $199 a month) already does server rotation, cover counts and quotes based on turn time. It relies on the host tapping in each table's status, so cameras add automatic status on top of an existing workflow rather than a new one. |
| Market size | 3 | The [2022 Economic Census](https://data.census.gov/table/ECNCOMP2022.EC2200COMP?q=ec2200&codeset=naics%7E722511) counts about 102,550 full-service establishments (from a search summary; I could not open the table directly). At $3,600 to $7,200 a year each, that is $370M to $740M in the US, and only locations with real waits will buy. Industry-wide [pre-tax margin is 2.8% of sales](https://restauranttechnologynews.com/2026/08/how-ai-powered-cctv-analytics-is-turning-restaurant-cameras-into-operational-intelligence/). |
| Risk (5 means low) | 2 | Three risks stack. Presto's attempt failed. Security cameras are placed for theft and liability, not for a clear view of every table. [California AB 1331](https://leginfo.legislature.ca.gov/faces/billStatusClient.xhtml?bill_id=202520260AB1331), a workplace-surveillance bill, went to the Governor on September 14, 2026 and is unsigned. And traffic fell in 15 of 16 months ([NRA](https://restaurant.org/research-and-media/research/restaurant-economic-insights/economic-indicators/same-store-sales-and-customer-traffic/)), which shrinks the set of restaurants with a wait. |

**Do incumbents own the data or the buying channel?** Partly, and in pieces:

- **Toast owns POS data and the SMB channel.** It has [about 180,000 locations and $2.4B ARR](https://www.morningstar.com/news/business-wire/20260804267340/toast-announces-second-quarter-2026-financial-results) (Q2 2026) and sells its own host stand.
- **DoorDash owns SevenRooms.** It [paid $1.2B](https://www.restaurantdive.com/news/DoorDash-acquires-sevenrooms-1-billion/747226/) and reaches 13,000 venues. OpenTable and Resy hold the rest of the host stand.
- **Camera software vendors already hold the camera feed.** [Solink](https://solink.com/resources/industry-insights/toast-pos-integrations/) already ties Toast transactions to video and tags tables. [Wobot](https://wobot.ai/industry/dine-in) sells dine-in heatmaps and customer counts.
- **Newer entrants are close by.** [Emilia AI](https://www.theinvestorsociety.com/prosus-backs-emilia-ai-to-turn-restaurant-cameras-into-sales-coaches/) (Prosus pre-seed, September 2026) coaches servers from existing cameras in Latin America.

What none of them owns is live, per-table status taken from video. That is the opening. The threat is that Toast gets it by partnering with Solink.

## 3. What would kill it, and the fastest test

**What kills it** is any one of these:

- Existing cameras can't see enough of each table to be accurate, and false alerts teach staff to ignore the system.
- Servers can't receive alerts during a rush, since many floors ban phones.
- The gain in covers is too small, or appears only on the few shifts that have a wait, so the ROI doesn't clear even $300 a month.
- Toast and Solink ship "good enough" table status as a bundled add-on.

**The single fastest test** is an alternating-shift pilot. Take 5 locations that run a waitlist on Friday and Saturday. Give them 3 weeks with alerts on some peak shifts and off on others, using their existing cameras and no new hardware.

Measure two numbers:
- the minutes from a party leaving to the next party sitting, from the camera logs plus host-stand timestamps
- covers per peak hour, from POS data

Before starting, agree the pass mark and a price. It passes if the reset gap drops by 5 minutes or more, peak-hour covers rise by about 5% or more, and at least 3 of the 5 sign a paid contract at $300 a month or more. It dies if the rise stays under about 2% or nobody signs.

## Why I'd back it

The need is real and the mechanism has research behind it. The product installs on cameras restaurants already own, and the pilot above can kill or confirm it within a month. Nobody owns per-table status from video yet. What would change my mind is Toast bundling this, or the pilot showing that a floor manager with a Toast Go handheld closes most of the gap without cameras.

VERDICT: BACK
