**Near-exact match.** Papaya (YC Fall 2026, papaya.fyi, 3 people) makes this pitch almost word for word. Its product wraps the model client in one line, runs "200+ research-backed analyses" on context, caching, subagents and tool calls, ranks the fixes by effect on quality, latency and cost, and delivers approved fixes as pull requests. It also accepts exports from other observability tools. It names no customers and no pricing. I treated Papaya as this team.

**Primary-source check of the key claims**
- **Caching rarely hits.** True. Datadog's State of AI Engineering (July 2026) found "only 28% of LLM call spans show any cached-read input tokens" on models that support caching. System prompts are 69% of all input tokens. On Anthropic's price list, a cache read costs 0.1x the normal input price, so the savings are real. [Datadog report](https://www.datadoghq.com/state-of-ai-engineering/), [Anthropic caching docs](https://platform.claude.com/docs/en/build-with-claude/prompt-caching)
- **Context grows every turn.** True. In the same Datadog report, tokens per request doubled year over year for the median customer and quadrupled for the top 10%. Chroma tested 18 models and every one got worse as the input grew. [Chroma](https://www.trychroma.com/research/context-rot)
- **Subagents are expensive.** True. Anthropic says multi-agent systems use about 15x the tokens of a chat, and that its early subagents duplicated work. [Anthropic](https://www.anthropic.com/engineering/multi-agent-research-system)
- **Tool calls fail.** Partly true. Datadog saw 2 to 5% of LLM calls return errors, and rate limits caused about a third of those failures. That is an infrastructure problem more than a prompt problem.

**Who else serves this customer**
- LangSmith Insights clusters production traces into failure modes. LangSmith Fetch hands traces to Claude Code or Cursor so a coding agent can propose code fixes. [LangChain](https://docs.langchain.com/langsmith/insights), [Fetch](https://blog.langchain.com/introducing-langsmith-fetch/)
- Braintrust's Loop agent builds datasets from production logs and proposes prompt fixes. Braintrust raised $80M at an $800M valuation in February 2026. [Loop](https://www.braintrust.dev/blog/loop), [SiliconANGLE](https://siliconangle.com/2026/02/17/braintrust-lands-80m-series-b-funding-round-become-observability-layer-ai/)
- Arize's Alyx is sold as a "self-improving agents" loop. [Arize](https://arize.com/alyx/)
- Raindrop has raised $50M, detects agent issues and replays production traffic against proposed changes. [PR Newswire](https://www.prnewswire.com/news-releases/raindrop-raises-15-million-to-detect-critical-ai-agent-failures-302628853.html)
- Kelet clusters failures across sessions and generates prompt patches. [Kelet](https://kelet.ai/)
- Datadog now shows cache hit rates per workflow. [Datadog blog](https://www.datadoghq.com/blog/monitor-prompt-caching-optimize-token-usage/)
- ClickHouse bought Langfuse in January 2026. Langfuse is used by 63 of the Fortune 500. [ClickHouse](https://clickhouse.com/blog/clickhouse-acquires-langfuse-open-source-llm-observability)

**Does an incumbent own the data or the buying channel?** Yes, both. Among teams with agents in production, 94% already have observability and 71.5% have full tracing ([LangChain survey](https://www.langchain.com/state-of-agent-engineering), 1,340 responses). Those traces already sit in Datadog, LangSmith, Langfuse or Braintrust. The platform team that would buy this already pays one of those vendors, and each of them is shipping a "find problems in traces and fix them" agent.

## 1. Strongest version
Stop being another place traces get stored. Read the traces the team already has in Langfuse, LangSmith, Datadog or OpenTelemetry, so there is no new SDK in the request path and no new security review.

Lead with the cost and latency fixes, because anyone can check them against the provider bill: cache layout, trimming context that grows each turn, routing easy calls to a cheaper model, and removing redundant tool calls and retries. Before any PR is proposed, replay it against real production runs to show quality holds.

Sell to companies spending $20K or more a month on inference, and charge a share of the savings the bill confirms rather than per agent. The PR into the customer's own codebase is the real difference from the incumbents. Their fix loops mostly stop at clusters, datasets or prompts stored on their own platform.

## 2. Ratings
- **Customer need: 4.** Only 28% of cache-capable LLM calls hit the cache, and tokens per request doubled at the median in a year (Datadog, July 2026).
- **Value over what customers use today: 2.** LangSmith Insights, Braintrust Loop, Arize Alyx, Raindrop and Kelet already find failure patterns in production traces and propose fixes. LangSmith Fetch plus Claude Code gets most teams to a code PR for close to nothing.
- **Market size: 3.** Buyers do pay here: Braintrust at $800M, Raindrop's $50M, Langfuse bought by a $15B company. But this is one feature of those platforms, and savings-based revenue is capped at a slice of a single line item, the inference bill.
- **Risk: 2.** Incumbents own the traces and the budget. The fixes are largely one-time: a cache layout, once fixed, stays fixed. Model providers keep making caching more automatic.

## 3. What would kill it
The value is a one-time cleanup rather than a subscription. After the first five to ten merged PRs, a second month of traces turns up few new fixes, customers cancel, and it becomes a consulting engagement. Meanwhile Braintrust or LangSmith ships "recommended fixes as PRs" on data it already holds.

**Fastest test.** Take the existing users who merged fixes in their first analysis. Rerun the analysis on their next 30 days of traces and count newly merged PRs that come with savings confirmed on the bill. Papaya already claims customer results, so this can run within days on data it already has. Near zero new merges means no recurring business.

VERDICT: PASS
