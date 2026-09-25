The company in this pitch is **Herdr** (herdr.dev, github.com/ogulcancelik/herdr). The product, the "over a million installs" figure, the socket API and the plugins all match, so I treated Herdr as this team. As you asked, I didn't read the local project files, which include METHOD.md. Everything below is desk research, not customer validation.

## Checking the claims against primary sources
- **Installs:** herdr.dev says "1,046,795 installs to date." Homebrew's own figures show about 8,500 installs in the last 30 days and 55,000 over 365 days. In August a news article reported 340,000 downloads, so the claimed total roughly tripled in about six weeks. The count most likely includes install-script runs and updates. Treat it as a claim: I couldn't verify it and it's probably inflated.
- **Other adoption numbers:** the GitHub repo shows about 40,600 stars (25,000 in August), and the site lists 1,324 community plugins. The license is Apache 2.0.
- **Features:** the background server, sessions that survive disconnects, SSH to other machines, the socket API and plugins are all confirmed in the README. The site lists the states as working, blocked and idle, and supports 22 agent command-line tools. For some agents, and according to one third-party guide this includes Claude Code, Herdr works out an agent's state by reading its screen. That breaks if the agent's own interface changes. I found no native phone app; phone check-in presumably means SSH.
- **Money and team:** a $6M seed led by Bessemer, with YC (Fall 2026), Tobi Lütke and others. It had a single founder, Can Celik, at the time of the raise. No revenue, customers or pricing are disclosed. "Herdr Cloud" is a waitlist: a relay that connects the user's own machines without SSH setup. It doesn't host agents.

## Who else serves this customer
- **Anthropic** already gives Claude Code users much of this for free. Agent view (`claude agents`) shows sessions as working, needs input, idle, completed or failed. A supervisor process keeps them alive through disconnects and sleep. Remote Control lets users check in from the phone app with push notifications.
- **OpenAI's Codex app** has project threads, worktrees and a review queue.
- **GitHub Agent HQ / Mission Control** runs Claude, Codex and Copilot from one dashboard, including on GitHub Mobile, sold through Copilot Pro+ and Enterprise.
- **Startups:** Conductor ($22M Series A, free), Superset ($20 per seat per month Pro plan), cmux (22,000+ stars) and Omnara (mobile). tmux or Zellij plus Tailscale is the free do-it-yourself option.
- **Does an incumbent own the data or the buying channel?** Partly, yes. Anthropic and OpenAI own the agent sessions, the subscriptions and the enterprise admin controls. GitHub owns the team buying channel and is itself neutral across vendors. Herdr owns only the terminal layer.

## 1. The strongest version
A neutral fleet layer for developers whose agents run on machines they own: laptop, workstation, dev servers. The free runtime stays the way users come in. The paid part is Herdr Cloud: an end-to-end encrypted relay, notifications on the phone, and one fleet view across machines, at about $10–20 per month, the same range as Termius for syncing SSH connections. Later a team tier adds a shared fleet view, routing blocked agents to the right person, Slack alerts, and audit trails of agent sessions.

The target is people who mix vendors (Claude, Codex, open-source agents), not single-vendor laptop users. The socket API is also worth pitching as the foundation that orchestration tools like Conductor and Superset build on.

## 2. Ratings
| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | 40,600 stars, about 8,500 Homebrew installs a month and 1,324 plugins show strong pull, though that is usage, not willingness to pay. |
| Value over what customers use today | 3 | Claude Code's agent view and Remote Control already cover background sessions, a "needs input" state and phone check-in for free; Herdr's real advantages are working across vendors and remote machines. |
| Market size | 3 | The paid layer is a relay and team features priced per seat, like Termius at $10–30 per user per month, sold only to developers running several agents at once. |
| Risk (5 = low) | 2 | Anthropic, OpenAI and GitHub all ship first-party fleet views and bundle them into subscriptions people already pay for, and Herdr's state detection depends on reading other vendors' screens. |

## 3. What would kill it, and the fastest test
**What kills it:** users don't pay. Most developers use mainly one vendor, and that vendor's free tools handle the common case. Tailscale plus SSH covers remote access for free. Teams buy agent oversight through GitHub or Anthropic admin consoles. The result would be a hugely popular free tool, like tmux, with no business behind it.

**Fastest test:** turn the Herdr Cloud waitlist into paid preorders. Offer a $15 per month card-on-file preorder to the waitlist and to recent installers for two weeks, and ask at checkout which agents they run. As a working bar I picked myself: at least 1,000 paid, or 5% of the waitlist, with most payers mixing vendors, supports backing it. Under 1% confirms the risk.

**What I'm unsure of:** the traction and the team are exceptional. My pass is about whether the paid layer can hold up against the platforms that own the agents, not about adoption. A strong result on the preorder test would flip this verdict.

Sources:
- [herdr.dev](https://herdr.dev/)
- [herdr GitHub](https://github.com/ogulcancelik/herdr)
- [Herdr seed blog post](https://herdr.dev/blog/herdr-raised-a-seed/)
- [Herdr Cloud waitlist](https://herdr.dev/cloud/)
- [RuntimeWire on the seed](https://runtimewire.com/article/herdr-raises-6m-seed-ai-agent-runtime)
- [Homebrew herdr analytics](https://formulae.brew.sh/api/formula/herdr.json)
- [MindStudio on Herdr](https://www.mindstudio.ai/blog/herdr-terminal-agent-multiplexer)
- [Claude Code agent view](https://code.claude.com/docs/en/agent-view)
- [Claude Code Remote Control](https://code.claude.com/docs/en/remote-control)
- [GitHub Agent HQ](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/)
- [OpenAI Codex app](https://openai.com/index/introducing-the-codex-app/)
- [Conductor overview](https://rustman.org/wiki/conductor-parallel-agents/)
- [Superset](https://superset.sh/parallel-coding-agents)
- [cmux](https://github.com/manaflow-ai/cmux)
- [Termius plans](https://docs.termius.com/administration/billing-and-plans)

VERDICT: PASS
