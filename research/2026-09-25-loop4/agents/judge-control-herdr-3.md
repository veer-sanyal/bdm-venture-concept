**Herdr is this company.** Herdr (herdr.dev, github.com/herdrdev/herdr) matches the pitch almost word for word, so I judged it as the team. It is an Apache-2.0 Rust tool built by one founder, Can Celik. It started in March 2026, is in YC's Fall 2026 batch, and raised a $6M seed led by Bessemer in September 2026.

## Checking the claims against primary sources

- **Background server, sessions survive disconnects, restore after restart:** true. The README and heise both confirm it.
- **Queue of working, blocked and done agents:** true. heise lists the states as working, blocked, done, idle and unknown. For some agents, including Claude Code, Herdr works out the state by reading the bottom of the terminal screen and matching known patterns. Flavio Copes, who reviewed it, says detection "is not perfect."
- **Command line, socket API and plugins:** true. There is a plugin marketplace and it supports 22 agent CLIs.
- **Check in from a phone:** only partly true. There is no phone app. You SSH in from a phone and the interface squeezes to fit a narrow screen. The feature that would connect your machines "without configuring SSH" is Herdr Cloud, which the site lists as "coming soon."
- **"Over a million installs" overstates users.** The site says "1,046,795 installs." That is the total of GitHub release downloads, and self-updates and remote-helper downloads fetch those same files, so repeat downloads count again. A better signal: the v0.9.1 release got about 78k downloads in its first 9 days. That points to tens of thousands of active installs, maybe low hundreds of thousands, not a million users. It has about 40k GitHub stars.
- **Revenue from hosted and team features:** none exists yet. There is no pricing and no paid tier.

## Who else serves this customer

- **Anthropic (Claude Code):**
  - Agent View shipped in May 2026. A background supervisor runs sessions that survive closing the terminal and machine sleep, but not shutdown.
  - It sorts them into a queue: Working, Needs input, Completed.
  - Remote Control, out of preview since August 2026, lets you drive a local session from the Claude phone app.
- **OpenAI:** the Codex app runs many agents at once, each in its own copy of the repo.
- **GitHub:** Agent HQ "mission control" manages Claude, Codex and Copilot agents from web, VS Code, phone and CLI.
- **Independents:** cmux (a Mac terminal, 26.6k stars), Conductor ($22M Series A), Superset, Agent Deck, Omnara ($9/month phone app), and plain tmux with Tailscale.

**Who owns the customer.** Anthropic, OpenAI and GitHub already own this customer's data (the agent sessions themselves) and the buying channel (Claude Max/Team, ChatGPT and Copilot seats). They are adding these features to subscriptions developers already pay for.

## 1. Strongest version

Drop "persistent terminal" as the product and become the vendor-neutral control plane for mixed fleets of agents across many machines:

- **Free:** the open-source runtime stays free and spreads usage.
- **Paid Herdr Cloud:** connects laptops, dev servers and cloud sandboxes with no SSH. It gives one attention queue across agents from different vendors on web and phone, and sends approval prompts to your phone.
- **Team tier:** shared views of agent sessions, audit logs of which permission prompts were approved, and policy.
- **Possibly later:** hosted always-on machines, which adds compute margin.

The target customer is 10–200 person engineering teams whose developers use two or more agent vendors on remote machines. That is exactly the group the labs' single-vendor tools don't cover.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | About 40k stars and about 78k downloads of one release in 9 days. Anthropic built the same supervisor and queue, which confirms the pain is real. |
| Value over what customers use today | 2 | Claude Code users already get sessions that survive closing the terminal, a needs-input queue and phone control in their existing plan. What's left for Herdr is the users who mix vendors and machines. |
| Market size | 3 | Developers running several CLI agents is a large and growing group. But the paid layer is a relay and team seat, and terminal tools historically monetize poorly: tmux and Zellij earn nothing. |
| Risk (5 = low) | 2 | Labs keep bundling the features, reading screens to detect agent state is fragile, and nobody has paid for anything yet. |

## 3. What kills it, and the fastest test

**What kills it:** developers never pay for Herdr Cloud or team features. Two reasons it could happen:
- Most heavy users settle on one vendor, whose own tools give them the queue and phone access free.
- Mixed-vendor users are happy with tmux, Tailscale and SSH.

**Fastest test:** put a paid pre-order for Herdr Cloud in front of existing users, in the update notice and the README, at roughly $15 per developer per month. Ask one question in the flow: which agent vendors do you run? Within 2 weeks, count paid deposits against weekly active installs, which you can estimate from stable-release downloads.

- **Pass:** at least 1–2% convert, and most of them run two or more vendors.
- **Fail:** fewer than 0.3% convert.

Asking people whether they would pay doesn't count, and desk research is not customer validation.

The runtime clearly has pull. But the paying layer is what the labs are giving away inside subscriptions they already sell, and Herdr has no evidence yet that anyone will pay for the part that remains.

Sources:
- [herdrdev/herdr on GitHub](https://github.com/herdrdev/herdr) and [its releases](https://github.com/herdrdev/herdr/releases)
- [herdr.dev](https://herdr.dev/) and the [seed announcement](https://herdr.dev/blog/herdr-raised-a-seed/)
- [heise](https://www.heise.de/en/news/Herdr-Terminal-multiplexer-sorts-fleets-of-coding-agents-11450324.html)
- [Flavio Copes' review](https://flaviocopes.com/herdr/)
- [runtimewire on the $6M seed](https://runtimewire.com/article/herdr-raises-6m-seed-ai-agent-runtime)
- [Herdr update docs](https://herdr.dev/docs/install/)
- [Claude Code Agent View docs](https://code.claude.com/docs/en/agent-view)
- [Claude Code Remote Control docs](https://code.claude.com/docs/en/remote-control)
- [OpenAI Codex app](https://openai.com/index/introducing-the-codex-app/)
- [GitHub Agent HQ](https://github.blog/news-insights/company-news/welcome-home-agents/)
- [cmux](https://github.com/manaflow-ai/cmux)
- [Conductor and the parallel-agent tools](https://rustman.org/wiki/conductor-parallel-agents/)
- [Omnara](https://ycombinator.com/companies/omnara)

VERDICT: PASS
