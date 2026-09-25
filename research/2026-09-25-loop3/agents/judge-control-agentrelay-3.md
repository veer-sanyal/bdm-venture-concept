Across vendors the problem is real, but the pitch overstates it: Anthropic, GitHub and Warp already cover most of it. The only defensible part is the vendor-neutral, self-hosted workflow layer, and nobody has shown yet that customers will pay for it. I lean pass.

**Who this is.** The concept is almost word for word Agent Relay (AgentWorkforce/relay, agentrelay.com). Its tagline is "Infrastructure for coding agents", and it offers channels, DMs and threads for Claude Code, Codex and OpenCode, plus shared sessions, file access to GitHub, Linear, Notion and Slack, TypeScript "Flows" with checks and human gates, and cloud or self-hosted deployment. It is Apache-2.0, with about 850 GitHub stars. The site lists Y Combinator, Hustle Fund and Active Capital as backers. I treat it as this team. Its npm packages had about 161k (SDK) and 31k (CLI) downloads in the last month, which may be inflated by automated installs. I found no public pricing (the pricing page returns 404) and no named customers.

**Checking the pitch's claims against primary sources**
- **"Agents can't hand work to each other":** out of date within Claude Code, true between vendors.
  - Claude Code now has cross-session messaging (ListAgents and SendMessage) on the same machine, across machines and to cloud sessions.
  - Claude Code's agent teams have a mailbox and a shared task list, though the feature is still experimental.
  - Neither reaches Codex or OpenCode.
- **"Humans can't see what every agent is doing":** partly out of date.
  - GitHub Agent HQ offers a "mission control" view across Copilot, Claude and Codex, with enterprise controls over which agents are allowed and audit logs.
  - Warp's Oz has one dashboard for Claude Code, Codex and Warp's own agent, and can run on the customer's infrastructure. It lists GitHub, Amazon, Nvidia and Ramp as users.
- **"Long jobs die when a session ends":** partly true. Claude's agent-team docs list "No session resumption" for teammates. Vendors' cloud sessions do survive.
- **The need is real at the top end.** Ramp built its own background agent, Inspect, on OpenCode, Modal, Slack and Cloudflare Durable Objects. It now writes about 30% of merged PRs. That shows the pain, but also that advanced teams build rather than buy.

**Does an incumbent own the data or the buying channel? Yes.**
- GitHub owns the repos, PRs and enterprise purchasing through Copilot Enterprise and Agent HQ controls.
- Anthropic and OpenAI own the session transcripts and the paid seats, and they keep adding coordination features.
- Linear and Slack own where humans hand out work. Linear already lists Cursor, Codex, Devin, Factory and Oz as agents you can assign issues to.
- Relay sits in the middle and owns none of these.

**1. Strongest version.** Drop "Slack for agents" and become an open, self-hostable toolkit for platform-engineering teams building their own internal background-agent system, like Ramp's Inspect. It would sell three things:
- **Durable workflows:** resumable, checked multi-step runs with human approval steps.
- **An auditable record:** of every agent session.
- **Any agent, including open ones:** Claude Code, Codex and OpenCode, running on the customer's own hardware.

The customer is a regulated or security-conscious company with 200 or more engineers that deliberately runs more than one agent vendor. Revenue is an enterprise self-hosted license, with the cloud service as a funnel for developers. Messaging becomes a feature, not the product.

**2. Ratings (for that version)**

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 3 | Ramp built Inspect in-house and it writes about 30% of merged PRs, so the pain is real. But Stack Overflow's 2025 survey found only about 31% of developers use agents regularly, and running several vendors at once is a subset of that. |
| Value over today | 2 | Claude Code already ships cross-machine messaging, agent teams and agent view. GitHub Agent HQ and Warp Oz already offer multi-agent dashboards, and Oz runs on the customer's own infrastructure. What's left is mainly OpenCode support, open source and air-gapped installs. |
| Market size | 3 | Oz's enterprise users show companies will pay for agent orchestration. But this version only reaches teams that run several vendors and install software themselves, which is much narrower. |
| Risk (5 = low) | 1 | Anthropic keeps shipping the exact pieces into Claude Code, GitHub owns enterprise purchasing, and Warp Oz is a funded company with enterprise customers going after the same buyer. |

**3. What kills it and the fastest test.** It dies if companies settle on one agent vendor, or if "Claude Code features plus Agent HQ or Oz" is good enough. Then the vendor-neutral layer is a feature nobody pays for, and the open-source version gets used for free.

The single fastest test is a paid pilot offer. Take 20 platform-engineering teams (for example, companies of issue authors in the repo, or teams known to run two or more agents in production). Offer a self-hosted enterprise license with a price and a two-week deadline. Pass if at least 3 sign a paid pilot or a priced letter of intent; fail if there are 0 or 1. Record why each "no" said no: Agent HQ, Oz, native Claude features, or building in-house. Everything above is desk research, so this test would be the first real customer evidence.

Sources:
- [AgentWorkforce/relay](https://github.com/AgentWorkforce/relay)
- [agentrelay.com](https://agentrelay.com/)
- [Agent Relay docs](https://agentrelay.com/docs/introduction)
- [Claude Code agent teams](https://code.claude.com/docs/en/agent-teams)
- [Claude Code cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging)
- [GitHub Agent HQ with Claude and Codex](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/)
- [Warp Oz](https://www.warp.dev/oz)
- [Warp multi-harness update](https://www.warp.dev/blog/multi-harness-cloud-agent-orchestration)
- [Linear agents](https://linear.app/agents)
- [Ramp Inspect](https://builders.ramp.com/post/why-we-built-our-background-agent)
- [Stack Overflow 2025 survey, AI section](https://survey.stackoverflow.co/2025/ai)
- npm download counts from api.npmjs.org

VERDICT: PASS
