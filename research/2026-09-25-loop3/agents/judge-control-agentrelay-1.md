Agent Relay (agentrelay.com, AgentWorkforce/relay, YC Fall 2026) matches this pitch almost word for word. Its YC listing has nearly the same description, so I treated it as this team. I didn't read any local project files.

## What checks out and what doesn't

- **Public code, cloud, self-hosting: true.** The repo is Apache-2.0 with about 850 stars and 66 forks. It contains messaging, GitHub/Linear/Notion/Slack integrations, shared sessions, and TypeScript "Flows" with checks and human approval steps. There is a free cloud tier. Self-hosting is set up with the team's help.
- **Early usage signal.** In the last month npm shows 161k downloads of `@agent-relay/sdk` and 31k of `agent-relay`. Automated installs could inflate that, so treat it as a signal, not proof.
- **No public pricing.** `/pricing` returns a 404. I found no paying customers named anywhere.
- **"Teams run several agents at once" is only partly supported.** 70% of engineers use 2–4 AI tools (Pragmatic Engineer, 906 respondents). Claude Code is used at work by 39% of developers, Codex by 16% and OpenCode by 7% (JetBrains, 15k+ respondents). But using several tools is not the same as needing agents to hand work to each other. JetBrains has no data on coordinated multi-agent use.
- **"Agents can't hand off" and "jobs die with the session" are mostly out of date within a single vendor:**
  - Claude Code has agent teams with a lead agent and messaging between teammates, though still experimental.
  - Claude Managed Agents added a coordinator with up to 20 specialist agents in May 2026.
  - Codex made subagents generally available in March 2026.
  - Cursor 3 collects local and cloud agents into one Agents Window, with triggers from Slack, Linear and GitHub.
  - The real remaining gap is handoffs between agents from different vendors, and running on the customer's own hardware.
- **Name clash.** Coder (the self-hosted development environment company) launched a product also called "Agent Relay" in September 2026. It runs Cursor and Claude Code agents inside customers' own workspaces, with an audit trail tied to each human user.

## Who else serves this customer

- **GitHub Agent HQ.** It runs Claude, Codex and Copilot side by side from one control view, sold through Copilot Pro+ and Enterprise.
- **Multica.** Open source, about 51k stars, supports 26 agent command-line tools, can be self-hosted, and has a hosted cloud. Same buyer, same promise.
- **Pentagon (YC S26).** Pitched as a "control plane for agent-native work".
- **Coder's Agent Relay, Traycer, Orca**, plus more than 100 projects on the awesome-agent-orchestrators list.

**Does an incumbent own the data or the buying channel? Yes.**
- GitHub owns the repositories, pull requests and enterprise Copilot contracts, and already sells a vendor-neutral view of all agents.
- Coder owns the self-hosted development infrastructure deal at regulated enterprises.
- Anthropic, OpenAI and Cursor own the agent sessions themselves.

## 1. The strongest version

Drop "chat for agents" as the product. Sell a self-hosted, vendor-neutral pipeline for agent work (like CI, but for agents) to platform and developer-experience teams at companies of 200+ engineers that are required to run more than one agent vendor.

- The product is the checked, resumable, auditable Flows running on the customer's own hardware: step-level retries, human approval gates, a full record of every session, and one audit trail across Claude, Codex and open-source agents.
- Messaging is plumbing underneath, not the thing being sold.
- Revenue is an enterprise license priced per workflow run or per seat, with the cloud tier acting as the funnel.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 3 | Using several tools is common (70% use 2–4), but I found no primary data showing teams need cross-vendor handoffs. |
| Value over what customers use today | 2 | Claude Code agent teams, Managed Agents, Codex subagents, Cursor 3 and GitHub Agent HQ already cover coordination, visibility and durability within each vendor. |
| Market size | 4 | Claude Code alone reaches 39% of professional developers. Platform-team tooling budgets are large if cross-vendor becomes the norm. |
| Risk (5 = low) | 2 | GitHub and Coder own the neutral layer and the buying channel, Multica has about 60x the open-source mindshare, and the product name collides with Coder's. |

## 3. What would kill it, and the fastest test

**What kills it:** enterprises standardize on one or two vendors and use that vendor's built-in multi-agent features. Or they buy the "neutral" layer as part of a bundle they already pay for (GitHub Copilot Enterprise or Coder). Either way, a standalone cross-vendor, self-hosted pipeline never becomes its own budget line.

**Fastest test:** offer a paid self-hosted Flows pilot (about $3–5k/month) to 20 platform-engineering leads at companies already running two or more agent vendors in production.
- If at least 3 sign within 3 weeks, that is evidence of a budget GitHub and Coder don't already cover.
- If fewer sign, the gap is a feature for them to add, not a company.

Everything above is desk research. None of it is customer validation.

**Reasoning for the verdict:** the only clearly unserved gap is cross-vendor coordination on the customer's own hardware. GitHub is already selling a vendor-neutral view through a channel it owns, and Coder is targeting self-hosted enterprises under the same product name. Multica has the open-source mindshare for the same promise. The rest of the pitch is being shipped by the agent vendors themselves.

Sources:
- [agentrelay.com](https://agentrelay.com/)
- [YC: Agent Relay](https://www.ycombinator.com/companies/agent-relay)
- [GitHub: AgentWorkforce/relay](https://github.com/AgentWorkforce/relay)
- [Coder: Introducing Agent Relay](https://coder.com/blog/introducing-agent-relay-cloud-hosted-agents-self-hosted-execution)
- [GitHub Changelog: Claude and Codex on GitHub](https://github.blog/changelog/2026-02-04-claude-and-codex-are-now-available-in-public-preview-on-github/)
- [GitHub Blog: Agent HQ](https://github.blog/news-insights/company-news/pick-your-agent-use-claude-and-codex-on-agent-hq/)
- [Claude Code agent teams docs](https://code.claude.com/docs/en/agent-teams)
- [Anthropic: New in Claude Managed Agents](https://claude.com/blog/new-in-claude-managed-agents)
- [Cursor 3 Agents Window](https://www.digitalapplied.com/blog/cursor-3-agents-window-complete-guide)
- [Multica](https://github.com/multica-ai/multica)
- [YC: Pentagon](https://www.ycombinator.com/companies/pentagon)
- [awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators)
- [JetBrains: AI coding agent adoption 2026](https://blog.jetbrains.com/research/2026/08/ai-coding-agent-adoption-2026/)
- [Pragmatic Engineer: AI tooling 2026](https://newsletter.pragmaticengineer.com/p/ai-tooling-2026)
- [Codex subagents](https://www.firecrawl.dev/blog/codex-multi-agent-orchestration)

VERDICT: PASS
