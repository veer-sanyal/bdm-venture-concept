**VERDICT ON THE PITCH AS WRITTEN:** it is a credible tech-enabled services business in a real bottleneck. But the easiest parts are already being built by the commissioning software vendors, and the established commissioning firms own the buying channel. I score it 12/20 and lean PASS.

**Claim check**
- **Construction spend:** verified. The Census Bureau put US data center construction at a $50.7B annual rate in April 2026, up from $39.8B a year earlier. That is +27%; one trade article prints +28%. I confirmed this through reports of the Census release ([Bloomberg](https://www.bloomberg.com/news/articles/2026-06-01/us-construction-spending-on-data-centers-eclipses-50-billion), [Electrical Marketing](https://www.electricalmarketing.com/economic-data/construction-industry/article/55383786/data-centers-still-sizzling-with-a-287-april-yoy-spending-increase-to-507-billion)); the Census index page itself doesn't show the figure.
- **$200k per MW per month:** roughly right, but at the high end. CBRE's H2 2025 wholesale average was $196.25 per kW per month, for 250–500 kW deals only ([CBRE](https://www.cbre.com/insights/books/north-america-data-center-trends-h2-2025)). Hyperscale-size leases are lower, about $145–170. Either way, a month of delay on a large hall costs millions.
- **Agent scarcity:** confirmed. Uptime Institute lists commissioning engineers among the hardest roles to fill ([Uptime](https://intelligence.uptimeinstitute.com/resource/survey-highlights-industry-staffing-crisis)). One caveat: most 2026 delays are blamed on power and equipment, not commissioning ([Network World](https://www.networkworld.com/article/4201941/up-to-50-of-data-center-capacity-slated-for-2026-could-be-delayed.html)).
- **Selling to general contractors is a problem.** The final-stage commissioning agent is normally independent and hired by the owner, precisely so it isn't grading the builder's work ([Salas O'Brien](https://salasobrien.com/news/data-center-commissioning-hyperscale/)).

**Who else serves this customer**
- **Commissioning software, which already has AI:**
  - Facility Grid says it drafts a test script in under two minutes instead of four to eight hours ([Facility Grid](https://facilitygrid.com/our-approach-to-ai/)).
  - CxPlanner's AI drafts test scripts ([CxPlanner](https://cxplanner.com/blog/how-cxai-redefines-data-center-commissioning-across-levels)).
  - CxAlloy (owned by Trinity) bought OTTO, which runs automated tests and trend analysis on HVAC units only ([CxAlloy](https://www.cxalloy.com/cxalloy-acquires-otto/)).
  - BlueRithm is a configurable commissioning platform.
- **Closest to the full pitch:** PingCx sells an "autonomous commissioning" platform to data center operators ([PingCx](https://www.pingcx.com/blog/data-center-commissioning-when-failure-is-not-an-option)). It is software, not a service with a signing agent, so I didn't treat it as an exact match. I found no company pitching exactly this.
- **Incumbent commissioning firms:** Jacobs, Burns & McDonnell, Salute Mission Critical and Salas O'Brien.
- **Who owns what:** No single incumbent owns the test data. The building-management and power-monitoring vendors (Schneider, Siemens, Vertiv) own the live system data; the commissioning software vendors own the workflow records. The **buying channel is owned by the established commissioning firms**, through owners' approved-vendor lists. The big hyperscalers bring their own commissioning playbooks.

**1. Strongest version**
An independent commissioning firm hired by the owner, not the contractor. It sells only the last two stages (system functional tests and the integrated full-load test) on liquid-cooled halls. The customers are AI cloud providers and colocation developers, which are more open to new vendors than the hyperscalers.

The core product is not script writing, which is now a commodity. It is live grading during the test: pull building-management, power-monitoring, cooling-unit and load-bank data as the test runs, grade every step against the acceptance criteria, and deliver a report ready for sign-off the same day.

Pricing: a fee per MW, plus a bonus for handing over on schedule. That ties the fee to the $150–200k per MW per month the owner loses while the hall sits idle.

**2. Scores (total 12/20)**
- **Customer need: 4.** Commissioning engineers are among Uptime's hardest-to-fill roles, and every month of delay costs about $150–200k per MW in lease income.
- **Value over what customers use today: 3.** Facility Grid and CxPlanner already draft scripts with AI. What's left is live grading and letting one agent cover more MW. One industry blog estimates the full-load test takes 10–14 weeks on liquid-cooled halls ([Archdesk](https://archdesk.com/blog/global-ai-data-center-construction-2026)), and much of that is physical work that software can't shorten.
- **Market size: 3.** Commissioning is about 1–3% of project cost. On $50.7B a year of US spend that is roughly $0.5–1.5B in service fees, tied to the data center building cycle.
- **Risk: 2.** The firm carries sign-off liability on mission-critical systems. Owners choose commissioning firms on track record. Incumbent firms can buy the same AI tools. Getting live data feeds during a test needs the owner's and the vendors' cooperation.

**3. What would kill it, and the fastest test**
- **Killer:** faster grading and reporting doesn't shorten the handover date. If the physical work and retests set the schedule, the product only improves the firm's own margin. The owner would get no time saved and would still prefer a firm with a track record.
- **Fastest test:** get one completed liquid-cooled full-load test package: the scripts, the building-management and power-monitoring trend data, and the final report. Replay it through a prototype grader. Measure how often it agrees with the human pass/fail calls. Then measure how many days of that test were spent waiting on grading, paperwork and retests rather than on physical testing. Under about a week of avoidable delay means no real value to the owner.

This is desk research only, not customer validation.

VERDICT: PASS
