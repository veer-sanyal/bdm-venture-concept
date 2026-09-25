Herdr is a real project, and the pitch matches it almost exactly, so I treated it as this team. I checked its claims against its own website, GitHub, its blog and vendor documentation. I did not read any local project files.

**What checks out**
- **Product:** It is an open-source (Apache-2.0) runtime written in Rust. A background server owns the agents' terminals and survives the client detaching. Agents show as working, blocked or idle. It connects to other machines over SSH, has a phone-sized layout, a command line, a socket API and a plugin marketplace. It works with about 22 agent tools. ([GitHub](https://github.com/herdrdev/herdr), [herdr.dev](https://herdr.dev/), [Copes deep dive](https://flaviocopes.com/herdr/))
- **Traction:** About 40k GitHub stars and 1,324 plugins. It raised a $6M seed led by Bessemer, with Y Combinator (Fall 2026 batch) and Tobi Lütke. Until then it was built by one person, Can Celik. ([blog](https://herdr.dev/blog/herdr-raised-a-seed/), [RuntimeWire](https://runtimewire.com/article/herdr-raises-6m-seed-ai-agent-runtime))
- **"Over a million installs" is overstated.** The site's 1,046,795 figure is GitHub release downloads plus Homebrew installs, per a search-result summary of its stats page. I couldn't open that page (it redirects to the homepage). The tool updates itself and ships a stable release every 1–2 weeks, so every update counts as another download. The count went from 340k in August to 1.05M in late September. The product has no telemetry, so nobody knows how many people actually use it.
- **Surviving a restart is partial.** If the server restarts, the running agents stop and only the layout comes back. Detection works mostly by reading the agent's on-screen prompts, which is fragile.
- **No revenue yet.** "Herdr Cloud" (no SSH needed) is marked "coming soon," with no prices and no team plan.

**Who else serves this customer**
- **Anthropic already owns the biggest agent's users and buying channel.** Claude Code's Agent View shows every session as working, needs input or completed. A supervisor process keeps sessions running with no terminal open. Remote Control lets you drive it from phone or browser. It all comes with the Pro and Max plans people already pay for, but it only covers Claude. ([docs](https://code.claude.com/docs/en/agent-view), [Remote Control](https://claudefa.st/blog/guide/development/remote-control-guide))
- **OpenAI** has the Codex app, with parallel agents, worktrees, a cloud option and mobile control.
- **GitHub** owns the team purchase: Agent HQ's "Mission Control" handles Copilot, Claude and Codex across web, VS Code, mobile and the command line, but for GitHub-hosted agents only.
- **Others:** cmux (Manaflow, macOS, 26k stars, dual license), Conductor ($22M Series A), Superset ($20 per seat per month), Emdash, plus plain tmux and Zellij.

**1. The strongest version**
Stop selling it as a better terminal multiplexer. Sell it as the vendor-neutral control plane for coding agents running on machines the vendors don't host: dev servers, remote VMs and sandboxes. The runtime stays free. The paid product is a hosted relay (no SSH, phone alerts when an agent is blocked), a team-wide queue across machines, and session audit and history. It fits teams that mix Claude, Codex and Cursor on shared remote boxes. There, neither Anthropic's single-vendor view nor GitHub's hosted-only Mission Control fully covers them.

**2. Ratings**

| Dimension | Score | Evidence |
|---|---|---|
| Customer need | 4 | About 40k stars in roughly five months, and Anthropic built the same queue itself. (This is desk research, not customer validation.) |
| Value over today | 2 | For the dominant agent, Claude Code's Agent View, background supervisor and Remote Control already do the queue, persistence and phone check-in at no extra cost. Herdr's real extra is cross-vendor and multi-machine. |
| Market size | 3 | Only the multi-agent, multi-machine subset of coding-agent users is paid-addressable. Tools in this category charge about $20 per seat per month (Superset), and mostly-free multiplexers like tmux and Zellij anchor the price near zero. |
| Risk (5 = low) | 2 | The model vendors keep shipping the same features to their own users. Screen-reading detection breaks when agent screens change. Real usage is unknown behind a download count swollen by updates. |

**3. What would kill it, and the fastest test**
- **The killer:** teams won't pay for a relay and team view, because each vendor's own tool is "good enough" and cross-vendor setups turn out to be rare.
- **The fastest test:** put a priced Herdr Cloud team plan, with a card taken up front, in front of the existing users via the site, README and update notice. Run it for two weeks.
  - It passes if at least 50 teams prepay.
  - It passes only if most of those teams run more than one vendor's agents or remote machines.
  - Also add an opt-in ping to count weekly active servers, so the funnel has a real denominator.

VERDICT: PASS
