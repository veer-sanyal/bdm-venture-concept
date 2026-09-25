I found a company whose pitch matches this one almost exactly, so I judged it as this team: **Agent Relay** (agentrelay.com, github.com/AgentWorkforce/relay, backed by Y Combinator). As you asked, I didn't read any local project files. My web search allowance ran out partway through, so the last few checks were done by opening primary sources directly.

## Claims checked against primary sources

| Claim | What I found |
|---|---|
| Code is public on GitHub | True. Apache-2.0 licence, about 850 stars, 66 forks, about 4,950 commits. |
| Works with Claude Code, Codex and OpenCode | True. The docs also list Cursor, Grok and hosted agents, plus a shared protocol for agents to find each other. |
| Channels, direct messages, threads, searchable history | True, with delivery receipts. |
| Checked, resumable multi-step workflows | True. Workflows are written in TypeScript, keep their state across restarts, and retry failed steps. |
| Connections to GitHub, Linear and Slack | True, plus Notion. They appear to the agent as ordinary files it can list and search. |
| Hosted cloud and self-hosting | True. The cloud has a free tier. Self-hosting with support goes through a contact email. |
| Enterprise licence revenue | Not verified. The pricing page returns "not found" and no prices are published. |
| Usage | The `agent-relay` command-line tool had 30.6k npm downloads in the last month; its SDK package had 161k, which is probably inflated by automated installs. No customer logos. |

## Who else serves this customer
- **Anthropic (Claude Code) already ships most of this for Claude-only teams.** Its features cover agent teams with a shared task list and mailbox, messaging between sessions (including other machines and the cloud), one screen to watch and steer many sessions, remote control, and a way to push outside events into a session. Two gaps remain. Agent teams are still experimental and don't survive a resumed session. Cross-machine messaging needs a claude.ai login, so it doesn't work on Amazon Bedrock, Google Cloud or Microsoft Foundry.
- **GitHub Agent HQ** has been generally available since 4 February 2026. It is a "mission control" that runs Claude, Codex and Copilot side by side for Copilot Pro+ and Enterprise customers. It connects to Slack, Linear and Jira, and Google, Cognition and xAI agents are joining.
- **Linear** launched coding sessions in June 2026. You assign an issue and Claude Code or Codex does the work, paid with Linear's AI credits. Linear says this resolves about 30% of its own incoming bug reports.
- **Conductor** raised a $22M Series A in March 2026. It runs parallel agents in isolated copies of the codebase, reports 10x user growth, and has dozens of engineers each at Google, Meta and others.
- **Others:** Imbue's Sculptor, Omnara ($500K seed), Cursor and Codex cloud agents.
- **A warning sign:** Bloop, the company behind Vibe Kanban, shut down on 10 April 2026. It had thousands of daily users, but "the vast majority are free users and we couldn't find a business model."

**Does an incumbent own the data or the buying channel?** Yes. GitHub owns the code, the pull requests and the Copilot Enterprise purchase, and already sells the vendor-neutral "watch every agent" screen. Linear owns the work queue. Anthropic and OpenAI own the agent runtimes and keep adding coordination features.

## 1. Strongest version
Don't sell "Slack for agents." Sell a **self-hosted control plane for mixed-vendor agent fleets**. Its core would be durable workflows, human approval gates and a full audit trail, running inside the customer's own network.

- **Buyer:** the platform or developer-productivity team at a company with 300+ engineers that pays for two or more agent vendors. A typical case is Copilot Enterprise plus Claude on Bedrock.
- **Why these buyers:** they get the least from the vendors' own cloud features. Anthropic's cross-machine messaging doesn't reach Bedrock, Google Cloud or Foundry, and GitHub's mission control lives on GitHub's cloud.
- **What it sells:** workflows that finish and can be audited ("the multi-step job completed, was checked, and a human approved it"), not chat between agents.
- **Revenue:** mainly enterprise self-hosted licences. The open-source code is the distribution channel.

## 2. Ratings for that version
- **Customer need: 3/5.** Anthropic, GitHub and Linear all built multi-agent coordination within a year, so the pain is real. But I found no evidence that teams need agents from *different vendors* to hand work to each other.
- **Value over what customers use today: 2/5.** Claude Code already has native teams, messaging, a shared view and remote control, and GitHub Agent HQ already gives a multi-vendor view. What's left is mixed-vendor durable workflows and self-hosting.
- **Market size: 3/5.** Spending on coding agents is large and growing. But this is a thin layer between the vendors and GitHub, and its enterprise pool is roughly companies running several vendors under self-hosting requirements.
- **Risk: 2/5.** Bloop shut down with a popular free orchestration tool and no business model. Every missing feature here is on some incumbent's roadmap, and the open-source licence makes the core easy to copy.

## 3. What would kill it, and the fastest test
**What kills it:** enterprises settle on one or two vendors and accept that vendor's native coordination plus GitHub Agent HQ as the neutral layer. Mixed-vendor, self-hosted orchestration then stays a free open-source convenience that nobody pays for, which is how Vibe Kanban ended.

**Fastest test:** in 3 weeks, go to 15 platform or developer-productivity leads at companies with 300+ engineers that already pay for two or more agent vendors. Ask each for a *paid* self-hosted pilot (for example $25k) to run one real multi-step workflow that spans vendors and has an approval gate. Fewer than 3 signed pilots kills it. Interest, open-source stars or free sign-ups don't count.

Sources:
- [Agent Relay site](https://agentrelay.com/)
- [Agent Relay GitHub repo](https://github.com/AgentWorkforce/relay)
- [Agent Relay docs](https://agentrelay.com/docs/introduction)
- [npm download API (agent-relay)](https://api.npmjs.org/downloads/point/last-month/agent-relay)
- [Claude Code agent teams](https://code.claude.com/docs/en/agent-teams)
- [Claude Code cross-session messaging](https://code.claude.com/docs/en/cross-session-messaging)
- [GitHub Agent HQ announcement](https://github.blog/news-insights/company-news/welcome-home-agents/)
- [Agent HQ launch coverage](https://creati.ai/ai-news/2026-02-04/github-agent-hq-claude-codex-ai-integration/)
- [Linear coding sessions changelog](https://linear.app/changelog/2026-06-11-coding-sessions)
- [Conductor Series A post](https://www.conductor.build/blog/series-a)
- [Vibe Kanban shutdown post](https://www.vibekanban.com/blog/shutdown)
- [Omnara on Crunchbase](https://www.crunchbase.com/organization/omnara)
- [Imbue Sculptor](https://imbue.com/product/sculptor)

VERDICT: PASS
