## Investor memo: agent optimization after deployment

**The same company already exists.** Papaya (YC Fall 2026, papaya.fyi, 3 founders, SF) pitches almost exactly this. Its site says "One line ,  wraps any LLM or agent client". It runs "200+ research-backed analyses across context, prompts, prompt caching, subagents, and tool calls", ranks each recommendation by impact, attaches the production runs behind it, and turns approved changes into pull requests. Following your instruction, I treat Papaya as this team. Its public claims are an average 10% quality gain, "$25K+ annualized savings per workflow" and "62.4% cost reduction" on specific issues. It names no customers, so none of these numbers can be checked. I could not verify the pricing (free tier for one agent). The site also offers a second way in, reading from the customer's existing observability tool. That matters later.

### Checking the pitch's claims against primary sources

- **Caching that never hits is real and silent.** Anthropic's docs say a prompt below the minimum length is processed uncached "no error is returned". A cache breakpoint on content that changes every request pays the write premium (1.25x the input price) and never gets the cheaper reads (0.05x to 0.1x). Datadog's 2026 State of AI Engineering report covers telemetry from more than 1,000 organizations. It found that system prompts are 69% of input tokens, yet only 28% of LLM call spans show any cached reads.
- **Context growth is real.** Datadog found that tokens per request more than doubled year over year for the median customer and quadrupled for power users.
- **Chatty subagents are real but a minority case.** Anthropic measured multi-agent systems at about 15x the tokens of chat. But Datadog found 59% of agent requests make a single service call and only 18% make three or more. Subagent-heavy setups are a small share of production today.
- **Failed tool calls are mostly not fixable in code.** 2% of LLM spans errored, and almost a third of those failures were rate limits. That is a capacity problem, not something a pull request fixes.

### Who already serves this customer

- **LangSmith Engine** (public beta since May 13, 2026) "clusters production failures into named issues, diagnoses root causes against your code, and drafts PRs". It flags token blowouts and latency spikes, and it can open a GitHub pull request. It costs about $1.50 per compute unit, at 5 to 30 units per run and a run every 6 hours.
- **Datadog Agent Observability** already traces cache behavior for Anthropic and OpenAI calls and publishes advice on caching.
- **Braintrust** ($80M Series B at an $800M valuation, February 2026) has Loop, which analyzes logs and suggests prompt revisions.
- **Others:** Galileo Signals, Arize AX with its Alyx assistant, and Atla (YC S23, $5.5M, which clusters failure patterns into fixes sized as small pull requests). Raindrop raised a $35M Series A on September 17, 2026 for monitoring agent failures in production.
- **The category is consolidating.** ClickHouse bought Langfuse (January 2026), Helicone was acquired and is in maintenance mode, and Humanloop wound down after joining Anthropic.

**Do incumbents own the data and the buying channel? Yes.** A team running agents at real volume already sends its traces to Datadog, LangSmith, Langfuse or Braintrust, and that tool already has a budget line. Papaya's option to read from those tools admits this: the data sits with the incumbent, and the incumbent can ship the same checks. LangSmith already has.

### 1. The strongest version

Narrow it to cost and latency, and let quality follow. Quality fixes are the crowded part (LangSmith Engine, Atla, Raindrop, Galileo) and hard to prove. A dollar saving shows up on the customer's model bill.

- **Customer:** teams spending roughly $20k or more per month on Anthropic or OpenAI tokens for agents.
- **Checks:** only the mechanical ones that can be proven. Examples are misplaced cache breakpoints, prompts below the cacheable minimum, tool definitions that change and void the whole cache, context that grows without pruning, and duplicate subagent prefixes.
- **Data access:** read-only from the trace store the team already has (Datadog, LangSmith, Langfuse, OpenTelemetry). This removes install friction.
- **Continuous value:** a check on every pull request that replays recent traces, so a regression in cache or context behavior is caught before it merges. This answers "I fixed it once, why keep paying."
- **Pricing:** a share of verified token savings rather than per agent. This sells to finance as well as engineering.

### 2. Ratings for that version

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Only 28% of LLM call spans show cached reads while 69% of input tokens are system prompts (Datadog 2026). |
| Value over what customers use today | 2 | LangSmith Engine already clusters production failures, finds root causes in code and opens GitHub PRs, inside a tool the customer already pays for. |
| Market size | 3 | Braintrust at $800M shows real observability spend, but optimization is being sold as an add-on to that spend (Engine is metered on top of LangSmith Plus). |
| Risk (5 = low) | 2 | The incumbents hold the traces and the budget line, and the providers set cache rules (OpenAI caches automatically; Anthropic's rules change by model). |

### 3. What would kill it, and the fastest test

**What kills it:** the value is a one-time audit rather than a subscription. A team fixes its caching and context problems in the first month, and the savings stop repeating. After that, a trace-store owner (LangSmith, Datadog, Braintrust) adds the same checks to a plan the customer already has, and there is nothing left to charge for.

**The single fastest test is a month-two check.** Connect read-only to the existing trace stores of 10 teams running agents at volume. Deliver the first analysis, get the fixes merged, then run it again on weeks 2 to 4. Measure the dollar value of new findings in the second run against the first. If later findings are under about 20% of the first run's value, this is a consulting deliverable and not a recurring product. In the same pilot, ask each team to pay the planned price for month two before they see month two's results. Fewer than 3 of 10 paying confirms the same answer.

VERDICT: PASS

Sources:
- [Papaya site](https://papaya.fyi) · [YC profile](https://www.ycombinator.com/companies/papaya) · [Launch YC post](https://www.ycombinator.com/launches/U2g-papaya-continuous-optimization-for-your-ai-agents) · [American Bazaar on Papaya](https://americanbazaaronline.com/2026/09/16/papaya-ai-y-combinator-fall-2026-488282/)
- [Anthropic prompt caching docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) · [Anthropic multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)
- [Datadog State of AI Engineering](https://www.datadoghq.com/state-of-ai-engineering/) · [Datadog on prompt caching](https://www.datadoghq.com/blog/monitor-prompt-caching-optimize-token-usage/)
- [Introducing LangSmith Engine](https://www.langchain.com/blog/introducing-langsmith-engine) · [LangSmith pricing](https://www.langchain.com/pricing) · [VentureBeat on Engine](https://venturebeat.com/orchestration/langsmith-engine-closes-the-agent-debugging-loop-automatically-but-multi-model-enterprises-still-need-a-neutral-layer)
- [Braintrust Series B, SiliconANGLE](https://siliconangle.com/2026/02/17/braintrust-lands-80m-series-b-funding-round-become-observability-layer-ai/) · [Braintrust pricing](https://www.braintrust.dev/pricing)
- [Atla Launch YC](https://www.ycombinator.com/launches/OLM-atla-the-improvement-engine-for-ai-agents) · [Raindrop Series A](https://thenextweb.com/news/raindrop-series-a-50m-crv-agent-failures-simulations)
- [ClickHouse acquires Langfuse](https://clickhouse.com/blog/clickhouse-raises-400-million-series-d-acquires-langfuse-launches-postgres) · [Grepture 2026 landscape](https://grepture.com/blog/llm-observability-tools-comparison)
