I rated the strongest version of this idea and would **pass**. People really do want this, but a "cc an AI to schedule" product is now cheap and widely available. The one place it clearly wins, recruiters working between a client and a candidate, is too small a market at the price this pricing model can hold.

As you asked, I used only the web and didn't open METHOD.md or STATE.md, even though AGENTS.md says to read them first.

**Near-exact match, treated as this team.** Vela (Y Combinator's Winter 2026 batch) describes itself on its YC page as an "AI Recruiting Coordinator for Executive Search". You cc it on a thread, and it handles email, SMS and WhatsApp at any hour, with no dashboard. The "a dozen emails per panel" line is Vela's own wording. Vela says it has paying enterprise customers and schedules "thousands of interviews each week". Its homepage has since widened to lawyers, associates and business development staff.

**Checking the key claims**
- **"A dozen emails per panel" is not independently supported.** It comes only from Vela's founders. The best primary data is a 2019 Yello survey of 200 recruiting and staffing staff. It found 67% take 30 minutes to 2 hours to schedule one interview, 17% take 2 to 5 hours, and 74% struggle with last-minute reschedules. It is old and run by a vendor, but the direction supports the pitch.
- **The widely quoted "38% of recruiter time goes to scheduling" is weak.** It comes from GoodTime, a scheduling vendor, and the report gives no sample size or method.
- **"No dashboard, just cc it" is not new.** Evie has sold exactly that to Siemens, Deloitte and Philips, prices per recruiter, and says it has arranged 50,000+ interviews. Several newer products do the same on email, SMS and WhatsApp:
  - Howie: $25 or $95 a month, $6M seed round, 1,000+ paying customers, used by recruiters among others.
  - Carly: from $35 a month.
  - Schela: aimed at agencies and search firms, pricing not yet public.

**Who already owns this customer**
- **In-house recruiting teams:** yes, the incumbents own both the data and the buying channel.
  - Workday bought Paradox, whose assistant schedules over SMS and WhatsApp, for $1.0B in October 2025.
  - Ashby announced autonomous scheduling agents in May 2026, in preview.
  - GoodTime and ModernLoop (Taylor AI) already sell autonomous panel scheduling.
- **Agencies and executive search:** Bullhorn and its Invenias product hold the records and the add-on marketplace. As far as I could find, they have no scheduling agent that works across companies. Sense does SMS scheduling for staffing firms through Bullhorn, but only with candidates.
- **Email and calendar:** Google and Microsoft own these, but their features are shallow for now. Gemini's "Help me schedule" in Gmail handled only two people at launch. A competitor's blog says Copilot won't negotiate times back and forth over email; I didn't confirm that with Microsoft.

**1. Strongest version.** An AI scheduling coordinator for recruiters who sit between two organisations: executive search, retained search and specialist agencies. The recruiter has to line up a client's hiring panel whose calendars and applicant-tracking system they can't access, plus a candidate who replies at odd hours, sometimes on WhatsApp. That is where tools built into an applicant-tracking system break, because they need calendar access. An agent that negotiates over email and chat is the natural fit. Build it with:
- the search firm's own domain and branding, so the candidate thinks a person at the firm is writing,
- handling for confidential searches,
- automatic logging into Bullhorn, Invenias, Loxo and Thrive.

Drop the general "professional services" push, where it competes head-on with the $25 assistants.

**2. Ratings for that version**

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Yello survey (n=200): 67% need 30 min to 2 hr per interview and 74% struggle with reschedules. Vela says its first staffing customer had looked for a fix for about eight years. |
| Value over what they use today | 2 | Evie, Howie and Carly already take a cc and chase replies, the last two at $25–35 a month. The extra value is limited to cross-company edge cases and logging into the recruiting system. |
| Market size | 2 | Executive search is a $20B+ industry, but its trade body (AESC) counts only about 16,000 member professionals. Even adding agency recruiters, seats priced near $25–35 a month cap revenue at a few hundred million dollars at most. |
| Risk (5 = low) | 2 | Workday/Paradox, Ashby, GoodTime and Gmail are all shipping scheduling features, and cheap cc assistants set the price. x.ai (sunset after its 2021 sale to Bizzabo) and Clara Labs (shut down) show that booking mistakes and handling edge cases can sink these companies. |

**3. What would kill it, and the fastest test**
- **Killers:**
  - Search firms judge a $25–35 general assistant "good enough" and won't pay a premium for the recruiting-specific version.
  - One wrong booking with an executive candidate ends the firm's trust.
  - Too few interviews per consultant each month to justify a paid seat.
- **Fastest test:** a two-week head-to-head at 5–8 search or agency firms that have already tried Howie or Carly.
  - Run both on live client-and-candidate panel threads.
  - Measure the share of threads finished with no human touch, and count errors.
  - Then ask for an annual contract at about $150 per seat per month, four times or more the general tools' price.
  - If fewer than 3 firms sign, it's a feature, not a company.

Sources:
- [Vela YC page](https://www.ycombinator.com/companies/vela)
- [Launch HN: Vela](https://news.ycombinator.com/item?id=47264741)
- [tryvela.ai](https://tryvela.ai/)
- [Yello survey](https://yello.co/blog/interview-scheduling-statistics/)
- [GoodTime stats](https://goodtime.io/blog/talent-operations/hiring-statistics/)
- [Evie](https://www.evie.ai/)
- [Evie pricing](https://www.evie.ai/pricing)
- [Howie on GeekWire](https://www.geekwire.com/2025/ai-scheduling-assistant-howie-raises-6m-launches-publicly-with-1000-paying-customers/)
- [Carly comparison](https://www.usecarly.com/blog/best-ai-assistant-for-recruiters/)
- [Carly on Copilot scheduling](https://www.usecarly.com/blog/can-copilot-schedule-meetings/)
- [Schela](https://schela.app/)
- [Workday completes Paradox acquisition](https://newsroom.workday.com/2025-10-01-Workday-Completes-Acquisition-of-Paradox)
- [Ashby agents release](https://www.prnewswire.com/news-releases/ashby-expands-its-ai-native-ats-with-agents-assistant-and-mcp-support-302765986.html)
- [ModernLoop](https://www.modernloop.com/)
- [Gemini "Help me schedule"](https://workspaceupdates.googleblog.com/2025/10/help-me-schedule-meeting-gmail-calendar.html)
- [Sense and Bullhorn](https://www.sensehq.com/partners/bullhorn)
- [AESC](https://www.aesc.org/)
- [Clara Labs shutdown](https://prio.sh/compare/clara-labs)

VERDICT: PASS