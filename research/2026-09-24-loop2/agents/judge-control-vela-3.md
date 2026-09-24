The idea is sound and the pain is real, but I'd pass. The stated pain holds up; the problem is that "copy an AI on the thread" is already crowded, cheap and moving into Outlook and Gmail.

**Same pitch, already running.** Vela (YC Winter 2026, founded 2026, San Francisco, 2 founders) matches this pitch almost word for word: copy it on the thread, it chases, reschedules and confirms over email, SMS and WhatsApp, with no dashboard. I treated it as this team. Its site claims SOC 2. It says it schedules "thousands of meetings each week" for "teams that work with" Netflix, LinkedIn, AWS and others. That wording suggests those logos are companies its users deal with, not paying customers. The only named customers are Paragon Legal and FirstLook Partners, plus pilots at unnamed "larger executive search firms". Pricing isn't published.

**How the key claims check out**
- **Hours lost: supported.** Yello's survey of 200 recruiters found 67% take 30 minutes to 2 hours to schedule one interview. Its 2019 survey (published 2020) found 74% call last-minute changes a problem. Candidate.fyi's own customer data puts manual scheduling at 243 minutes per interview and reschedules at 14%.
- **"A dozen emails per panel": no primary source.** The survey doesn't count emails. The "10 emails per interview" figure only appears in unsourced blogs. Vela's benchmark of 70,000 emails is behind a form, so I couldn't check it.
- **Hours-saved pitch: somewhat inflated.** Vela's example (30 interviews a week, 15 minutes each) gives 43.5 hours a month but assumes a 35% reschedule rate. The best available data says 14%, which works out to about 37 hours a month.
- **Search firms do this work by hand: supported.** Coordinator job ads (e.g. WittKieffer) list scheduling across time zones with senior people as a core duty. A US recruiting coordinator averages about $62k a year (Glassdoor).

**Who else serves this customer**
- **Same product, same buyer:**
  - Evie has done copy-on-thread scheduling for recruiters for years. Customers include Siemens, Deloitte and Prudential; it has arranged 50,000+ interviews and charges per recruiter, about $25 a month by third-party reports.
  - Howie, a general assistant you copy on threads, raised $6M in September 2025 with 1,000+ paying customers. It costs $25 or $95 a month and lists recruiters as users.
  - Lindy and Guide's Aria also do this.
- **Corporate recruiting teams:** the hiring-software vendors own the data and the buying channel. Workday bought Paradox for $1.0B, and Paradox schedules about 1 in 10 US interviews. Other players include Greenhouse, GoodTime, ModernLoop and candidate.fyi.
- **Search firms:** their systems (Bullhorn Invenias, Thrive, Clockwork, Ezekia) hold the data, but I found no AI scheduling in any of them. The workflow runs in Outlook and Gmail. Microsoft's Copilot now schedules straight from a thread. Google's "Help me schedule" launched October 2025 for two people only.
- **History:** x.ai shut down in 2021 and Clara Labs also closed. Clara's human backup for hard cases was expensive, and scheduling alone was too narrow a product.

## 1. Strongest version
Skip corporate recruiting teams; the hiring-software vendors have them locked up. Focus on retained executive search, private-equity and VC talent teams, and law-firm lateral hiring. In these settings:
- Panels are senior people at the *client*, whose calendars the firm can't see, so availability has to be negotiated.
- Candidates are executives who expect white-glove handling, across time zones and often on WhatsApp.
- Discretion matters, and a single placement fee is often $100k or more.

Price it per consultant at a coordinator-replacement level, around $300–800 a month, not $25 a seat. Write every interaction back into the firm's search system. Later, expand into other firms with heavy outside-party scheduling, such as expert networks and deal teams.

## 2. Ratings
| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | 67% of recruiters take 30 min–2 h per interview (Yello), and search-firm coordinator roles exist mainly for multi-time-zone senior scheduling. |
| Value over what they use today | 2 | Evie and Howie already do copy-on-thread scheduling for about $25 a month, and Copilot schedules from threads. The gap is reliability with outside panels, plus SMS and WhatsApp. |
| Market size | 2 | Executive search is a $20B+ industry, but its trade body (AESC) counts only about 16,000 member consultants. The larger corporate market is controlled by the hiring-software vendors. |
| Risk (5 = low) | 2 | Microsoft and Google are building this into email, prices are anchored at $25 a month, one botched CEO interview loses the account, and x.ai and Clara both died. |

## 3. What kills it, and the fastest test
**What kills it:**
- Search firms won't pay much more than Evie or Howie charge, so the business can't support enterprise sales.
- Or the agent can't reliably finish panels with outside participants without a person stepping in (Clara's cost trap).
- Or Copilot and Gemini get good enough at group scheduling.

**Fastest test:** a paid pilot, not a free one. Take 3–5 mid-size retained search firms, at least one of which should be Vela's current pilots. Run their next 2 weeks of live client-panel threads through the agent at $400 per consultant a month. It passes if at least 90% of panels are confirmed with no human stepping in and at least 3 firms sign on at that price. If they only convert at about $25–50, or it needs a person on a meaningful share of threads, it fails. Desk research can't settle this; only live customer threads can.

## Sources
- https://www.ycombinator.com/companies/vela
- https://www.ycombinator.com/launches/PNn-vela-ai-scheduling-that-adapts-to-how-you-work
- https://tryvela.ai/
- https://tryvela.ai/ps
- https://www.vsnewsnetwork.com/newsroom/y-combinator-backed-vela-launches-ai-scheduling-coordinator-focused-on-email-based-meeting-management
- https://www.evie.ai/
- https://www.evie.ai/pricing
- https://www.geekwire.com/2025/ai-scheduling-assistant-howie-raises-6m-launches-publicly-with-1000-paying-customers/
- https://newsroom.workday.com/2025-10-01-Workday-Completes-Acquisition-of-Paradox
- https://www.greenhouse.com/newsroom/greenhouse-launches-new-ai-capabilities-built-to-strengthen-structured-hiring-not-shortcut-it
- https://techcommunity.microsoft.com/blog/microsoft-copilot-blog/effortless-scheduling-with-copilot-%E2%80%93-transform-email-threads-into-productive-mee/4358034
- https://workspaceupdates.googleblog.com/2025/10/help-me-schedule-meeting-gmail-calendar.html
- https://yello.co/blog/interview-scheduling-statistics/
- https://candidate.fyi/post/2026-recruiting-coordination-statistics
- https://builtin.com/job/executive-search-coordinator/10089822
- https://www.glassdoor.com/Salaries/recruitment-coordinator-salary-SRCH_KO0,23.htm
- https://www.aesc.org/insights/blog/what-association-executive-search-and-leadership-consultants
- https://prio.sh/compare/clara-labs
- https://www.cbinsights.com/compare/clara-labs-vs-xai-bizzabo

VERDICT: PASS