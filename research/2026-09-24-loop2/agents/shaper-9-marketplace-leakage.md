I'd keep the problem but not the product. A tool that only detects when a deal is moving off-platform isn't a strong company. Better detection doesn't win the sale, and building on Jev is a liability rather than an edge. A reshaped version is worth pitching: a product that measures how much revenue a marketplace loses to off-platform deals, wins some of it back, and gets paid on the revenue it can prove it saved. It's a moderate opportunity, not a slam dunk. Everything below is desk research, so none of it counts as customer validation.

**Two of the generator's numbers are wrong**
- **The 18% Airbnb figure.** It comes from blogs. The peer-reviewed Airbnb study matched bookings to phone location data and found **5.4%** of bookings in Austin went off-platform in 2019. Instant Book cut that by about 9% and Airbnb Plus by about 6%. The "18%" matches a different paper: when China blocked Skype, off-platform deals on a freelance marketplace fell about **18%**.
- **The $84M Upwork figure.** It's a blogger's estimate, not an Upwork disclosure. Upwork's FY2025 10-K lists circumvention as a risk and says the losses are **"difficult or impossible to measure."** That line is the real opening.

**Why detection alone fails**
- **Anyone can build it.** Reading a message thread for "let's take this off-platform" is a cheap classification job for any language model, and messages don't need instant answers. Jev's price advantage (about $42 per billion input tokens) saves little, because model cost is small next to what a customer would pay.
- **Competitors already cover it.** SafetyKit ($27M Series A; Upwork, Etsy, Depop, Lyft) sells an "Offsite Transactions" policy check. Chat providers like Stream and CometChat already mask contact details and flag scams.
- **Blocking isn't what works.** The research shows marketplaces keep deals by adding value (Instant Book, Airbnb Plus) and by lowering fees for repeat pairs. More trust between buyer and seller can even increase off-platform deals (Gu & Zhu). Upwork and Preply already cut fees as a relationship grows: Upwork's fee drops from 15% toward 0% with billing history, and Preply's commission drops from 33% to 18%.

**The Jev terms rule it out as the core.** I checked TypeSafe's agreement (last updated 2026-09-23):
- **No model of our own.** §2.3(b) bans training a model to imitate Jev's outputs, so there's no path to a cheaper in-house model or a data advantage.
- **Privacy blocker.** §4.1(c) lets TypeSafe use customer data "in perpetuity" to derive telemetry. That covers private buyer-seller messages full of phone numbers and emails, which a marketplace's legal team is unlikely to accept.
- **No uptime promise.** There's no SLA and TypeSafe can suspend immediately, so the product must keep working if Jev goes down.
- **Signups are closed.** They paused on 2026-09-22. Jev can still be reached through OpenRouter and Vercel AI Gateway, but I didn't check which terms apply there.
- **Resale risk.** A thin detection API that passes Jev's answers through is close to the §2.3(a) ban on offering it "as a standalone service."
- **Unverified.** I couldn't confirm "zero data retention is enterprise-only." The agreement has no BAA.

The product should work with any model and not depend on Jev.

**The reshaped company: a revenue-recovery tool for mid-sized commission marketplaces** (roughly $20M–$1B in yearly sales, such as services, tutoring, freelance or B2B wholesale).
1. **Measure first.** Start with a paid audit of past messages: how often contact details get exchanged, which conversations stop right after, and which repeat pairs stop transacting while both stay active on the platform. It answers the question Upwork calls unmeasurable, and it's the entry sale.
2. **Intervene instead of blocking.** When a conversation or pair looks at risk, show a timely reason to stay: payment protection, a lower fee for loyal pairs, or a legitimate "conversion fee" exit like Upwork's.
3. **Prove it with a control group inside the flagged conversations.** Across all conversations the effect is too diluted to measure: about 270k per group, using an illustrative 30% booking rate as the base. Within flagged ones, about 650 per group can show a 25%→32% lift.
4. **Charge on recovered take.** Recovered take is the marketplace's commission on deals the product kept on-platform. Priced this way it's a growth-budget purchase, not a trust-and-safety cost like SafetyKit.
5. **Grow broad later** into fee and pricing tools for marketplaces, meaning personalized fees for pairs at risk of leaving. The research (Enache & Rhodes, 2025) and the Upwork and Preply fee structures show the demand.

**Rough economics (all assumptions):** a $100M marketplace taking 15% might lose $0.75–2.25M a year in commission to off-platform deals. Winning back 20–30% and charging 20% of that gives $30k–135k a year per customer. With about 1,000 target marketplaces, the main addressable market is around $75M. The closest comparison, Churnkey (a tool that stops subscribers from cancelling), is only about $1.7M in revenue with 300 customers. Judges will push on market size, so the move into pricing matters.

**Main risks**
- Large marketplaces build this in-house.
- Mid-sized ones may not share message data.
- The win-back rate is unknown.
- SafetyKit could add the same feature.

**Next step:** interview 15–20 heads of marketplace or trust and safety. Kill the idea or narrow it if fewer than 3 would share past messages for an audit, or if off-platform deals aren't a top-5 problem for them.

Sources:
- [Airbnb disintermediation, ICIS 2022](https://aisel.aisnet.org/icis2022/sharing_econ/sharing_econ/12/)
- [Gu, Technology and Disintermediation (Mgmt Sci)](https://pubsonline.informs.org/doi/10.1287/mnsc.2021.02736)
- [Gu & Zhu, Trust and Disintermediation](https://pubsonline.informs.org/doi/10.1287/mnsc.2020.3583)
- [Enache & Rhodes 2025](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.02150)
- [No Fixed Path blog (18%/$84M origin)](https://www.nofixedpath.com/p/fighting-disintermediation-can-ai)
- [Upwork FY2025 10-K](https://www.sec.gov/Archives/edgar/data/1627475/000162747526000012/upwk-20251231.htm)
- [SafetyKit marketplace moderation](https://www.safetykit.com/marketplace-moderation)
- [SafetyKit $27M](https://www.safetykit.com/news/safetykit-raises-27m-to-make-ai-do-techs-dirty-work)
- [Stream moderation](https://getstream.io/moderation/)
- [CometChat platform leakage](https://www.cometchat.com/blog/platform-leakage)
- [TypeSafe MCA](https://typesafe.ai/legal/mca)
- [TypeSafe signup pause](https://x.com/typesafeai/status/2102281508950307159)
- [Upwork fee](https://support.upwork.com/hc/en-us/articles/211062538-Learn-about-the-Freelancer-Service-Fee)
- [Preply commission](https://help.preply.com/en/articles/4171383-preply-commission-model)
- [Churnkey (Latka)](https://getlatka.com/companies/churnkey)