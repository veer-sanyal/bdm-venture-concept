I used only web sources, as you asked. I did not open the repo's METHOD.md or STATE.md, even though AGENTS.md says to read them. Everything below is desk research, not customer validation.

## Checking the claims

- **"Scheduling eats recruiter time": partly true.** Yello surveyed 200 recruiting and staffing staff in 2019. 67% said one interview takes 30 minutes to 2 hours to schedule, and 74% said reschedules are a challenge ([Yello](https://yello.co/blog/interview-scheduling-statistics/)). "A dozen emails per panel" is plausible, but I found no primary source for it. Bullhorn says automation removes "six or more" emails per candidate ([Bullhorn](https://www.bullhorn.com/blog/best-recruitment-ai-tools/)). Most of the "10–15 hours a week" figures come from vendor blogs.
- **"No dashboard, just copy it on the email" is not new.**
  - **Evie** matches this pitch almost exactly, so I treat it as this team. You copy evie@yourcompany.com and it contacts everyone, chases non-responders, handles panels and reschedules ([evie.ai](https://www.evie.ai/)). It launched in 2016 and moved into recruiting in 2018 because headhunters were using it to schedule interviews between their clients and candidates ([SMU](https://news.smu.edu.sg/news/2023/08/17/riches-through-niches-story-evie-ai-co-worker-everyone-thinks-human-0)).
  - **Evie's traction is flat.** It had "400+ companies in 40 countries" in 2020. Today it lists about 360 companies in 48 countries and about 11 employees ([Capterra](https://www.capterra.com.sg/software/181226/evie-ai), [Tracxn](https://tracxn.com/d/companies/evie/__De08BdLr3vWxnD2ODkhc9x4orBc87tR3lu0zSjv9_h8)). That is eight years in exactly this customer segment without breaking out.
  - **Others tried the same approach.** x.ai raised tens of millions for an email-copied assistant and was shut down in 2021 after Bizzabo acquired it ([GlobeNewswire](https://www.globenewswire.com/news-release/2021/06/03/2241277/0/en/Bizzabo-Acquires-x-ai-to-Launch-AI-powered-Scheduling-Accelerate-Personalized-Event-Experiences.html), [Tasbia](https://tasbia.com/x-ais-scheduling-tool-is-shutting-down/)). Clara still sells to recruiters at $80 a month for 30 meetings ([Clara](https://www.claralabs.com/pricing/)). Howie was rebuilt on modern language models, charges $25–95 a month and has 1,000+ paying customers, recruiters among them ([GeekWire](https://www.geekwire.com/2025/ai-scheduling-assistant-howie-raises-6m-launches-publicly-with-1000-paying-customers/)).
- **Email, SMS and WhatsApp are not a differentiator either.** GoodTime, Schela and X0PA already schedule over all three ([GoodTime](https://goodtime.io/products/hire/text-recruiting/), [Schela](https://schela.app/), [X0PA](https://x0pa.com/features/recruitment-communication/)).

## Who already owns this customer

- **In-house recruiting teams: yes, incumbents own them.**
  - Workday bought Paradox for about $1B in 2025 ([Workday](https://newsroom.workday.com/2025-08-21-Workday-Signs-Definitive-Agreement-to-Acquire-Paradox,-the-AI-Company-Redefining-the-Frontline-Candidate-Experience)).
  - GoodTime launched its Orchestra scheduling agents in 2025 ([GlobeNewswire](https://www.globenewswire.com/news-release/2025/05/21/3085776/0/en/GoodTime-Launches-Orchestra-A-Digital-Workforce-of-AI-Agents-Built-to-Transform-Hiring.html)).
  - ModernLoop, candidate.fyi and Guide all sell scheduling to these teams and connect to the applicant tracking systems (ATS) where their candidate data lives.
- **Staffing agencies: yes.** Bullhorn is their main system, and its Amplify AI schedules interviews inside it ([Bullhorn](https://www.bullhorn.com/news-and-press/press-releases/bullhorn-unveils-amplify-digital-workers-at-engage-2026/)).
- **Email and calendar: Google and Microsoft own the layer this product sits on.** Since March 2026, Gemini's "Help me schedule" in Gmail handles up to 20 guests ([Google](https://workspaceupdates.googleblog.com/2026/03/use-help-me-schedule-in-gmail-to-easily-set-up-a-meeting-time-with-multiple-guests.html)). Outlook added "Schedule with Copilot" ([Microsoft](https://support.microsoft.com/en-us/outlook/schedule-a-meeting-using-copilot)). Neither chases people or reschedules yet, but that gap is small.
- **Executive search firms: only partly.** Their client and candidate records sit in specialist systems (Invenias, Clockwork, Thrive, Ezekia). None of these shows a scheduling agent, so this is the one real gap.

## 1. The strongest version

An email- and WhatsApp-native coordinator only for retained executive search and boutique search firms. It schedules client-side panels, where the interviewers are client executives, board members and their assistants, and the search firm cannot see their calendars. That is where calendar-based and ATS-based tools fail and where a human-like email agent actually wins. The target is international firms (Middle East, India, Europe, Latin America), where candidates reply on WhatsApp at odd hours.

Charge per active search (say $300–600 per mandate) rather than per seat, because each consultant schedules too little for seat pricing to add up. Offer it as white-label, sending as "Sarah at [firm]", with a human reviewing anything touching a C-suite candidate.

Drop in-house recruiting teams and staffing agencies. Incumbents own both.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 3 | 67% of recruiters say one interview takes 30 min–2 hours to schedule (Yello). But Evie, which began with headhunters, stayed at roughly 400 accounts over eight years, which suggests the pain is tolerable. |
| Value over what customers use today | 2 | Evie, Clara and Howie already do "copy it on the email"; Howie does it for $25 a month. The only new pieces are WhatsApp and external client panels, which GoodTime and Schela partly cover. |
| Market size | 2 | Executive search is a ~$20B fee industry but AESC member firms employ only about 16,000 professionals ([AESC](https://www.aesc.org/insights/magazine/article/future-executive-search-and-leadership-consulting-evolving-profession)). Scheduling spend per firm is small, so realistic revenue is probably in the low hundreds of millions. |
| Risk (5 = low) | 2 | Gemini and Copilot added multi-person scheduling in 2026, the same capability powers generic assistants like Howie, and x.ai shut down. |

## 3. What would kill it, and the fastest test

**What would kill it:** search firms won't let an AI write to C-suite candidates and client boards, because that coordination doubles as relationship-building. Or each firm schedules too few panels to pay enough to matter. Either way the business stalls where Evie did.

**Fastest test (two weeks):** a paid concierge pilot run by hand, with a person plus an LLM behind the scenes.
1. Offer it to 20 boutique retained search firms at $400 per search.
2. Pass only if at least 5 firms actually copy it into live client-panel threads with real candidates.
3. Also require at least 3 of them to pay for a second search.

Fewer than 3 paying means the idea is dead.

VERDICT: PASS