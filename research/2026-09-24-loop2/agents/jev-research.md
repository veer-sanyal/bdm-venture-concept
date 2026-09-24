# Jev research (orchestrator's seed research), 2026-09-24

Desk research only; not customer validation.

I researched Jev from the web only, without reading any local files. One correction first: Jev launched on **2026-09-15**, not the 18th ([Startup Fortune](https://startupfortune.com/typesafe-ais-decision-model-jev-becomes-vercels-fastest-adopted-launch/), [jevaiguide](https://jevaiguide.com/faq/jev-waitlist/)). MarkTechPost's launch article is dated 09-19 ([MarkTechPost](https://www.marktechpost.com/2026/09/19/typesafe-ai-releases-jev/)).

## 1. What Jev is

- **What it does:** It answers a set of typed questions about a "state" you send and returns probabilities, not text. TypeSafe calls this a "System One model" ([blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev)). There is one endpoint, `POST https://api.typesafe.ai/v1/systemone`, which takes `state` (a string, an object or an array), `model` and a map of `questions` ([API](https://docs.typesafe.ai/api.md)).
- **Question types** ([API](https://docs.typesafe.ai/api.md)):
  - **Noul:** a yes/no question; returns a value from 0 to 1.
  - **Choice:** picks one option, up to 255 options; returns the choice, every option's probability and a confidence.
  - **Score:** rates against 2 to 10 ordered levels; returns a probability-weighted score, the probabilities and a confidence.
  - All questions in a request are answered in parallel against the same state ([intro](https://docs.typesafe.ai/introduction)).
  - An HN summary said Choice allows only 10 options. The API docs say that limit applies to Score levels, not Choice.
- **What it cannot do:** It does not generate text, write code or chat. It is not a drop-in model for coding agents ([coding-agents doc](https://docs.typesafe.ai/introduction/coding-agents.md)).
- **Model, limits and pricing** ([Models](https://docs.typesafe.ai/models.md)):
  - The model is `jev-1.13.0`, with aliases `jev-latest` and `jev-preview`.
  - Price: **$0.042 per million input tokens; output tokens are free.**
  - Rate limits: 250,000 tokens/s and 1,200 requests/min. The docs say these are "adjusting dynamically" and "can change without notice".
  - Context: 64k tokens per request, of which 32k covers the state plus the longest question. Cloudflare lists 32k ([Cloudflare](https://developers.cloudflare.com/ai/models/typesafe/jev/)).
  - Input is text only; English works best.
  - There is no fine-tuning or LoRA: every account uses the same weights.
  - TypeSafe does not train on customer data. Zero data retention is offered for enterprise only.
- **Latency:** TypeSafe claims 70 to 500 ms end to end ([blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev)).
- **Deployment:** API only, with no on-prem option found.
  - Python and JS SDKs are available ([llms.txt](https://docs.typesafe.ai/llms.txt)).
  - It is also available through Vercel AI Gateway, OpenRouter and Cloudflare Workers AI. Cloudflare only proxies to TypeSafe's own infrastructure ([Cloudflare](https://developers.cloudflare.com/ai/models/typesafe/jev/), [Langfuse PR](https://github.com/langfuse/langfuse/pull/17798)).
- **Access:** The waitlist was dropped on 09-20 UTC with $5 of free credit ([X](https://x.com/typesafeai/status/2101786156572823624), [explainx](https://explainx.ai/blog/jev-general-availability-no-waitlist-2026)). On 09-22 TypeSafe paused new signups because of demand ([X](https://x.com/typesafeai/status/2102281508950307159)). I dated both posts from their IDs; the posts themselves returned HTTP 402.

## 2. Strengths and weaknesses

**What TypeSafe claims:**
- "Zero hallucinations", "never makes type errors" and "calibrated" output. It says the hallucination figure is "not empirical": what is guaranteed is that answers match the schema ([blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev)).
- 193.6x faster and 444.6x cheaper than LLMs ([home](https://typesafe.ai/)). These numbers come from TypeSafe's own workflow evals, which it concedes are "on the higher end of real world gains" and possibly biased ([blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev)).
- TypeSafe's own list of known weaknesses ([jaggedness](https://docs.typesafe.ai/model-jaggedness/jev-1.13.md)):
  - Reads instructions very literally.
  - Cannot do counting, arithmetic or date comparison.
  - Struggles with questions that need several steps of reasoning.
  - Accuracy falls ("context rot") as irrelevant content is added to the state.
  - Can be steered by adversarial content in the state.
  - A Noul and its negation can sum to 1.19.
  - Cannot generate text.

**Independent tests:**
- **Social-science labelling** (Ibrahim & Zaki, 18 tasks, 7,977 items) ([arXiv 2609.24574](https://arxiv.org/abs/2609.24574)):
  - Jev lost to frontier LLMs on 14 of 15 tasks, by a median of 11.6 macro-F1 points, at about 44x lower cost.
  - Sending low-confidence items to an LLM matched the LLM alone at a quarter to half of its cost.
- **Phishing** (2,000 emails) ([jev-phishing-bench](https://github.com/anisselbd/jev-phishing-bench), [beri.net](https://www.beri.net/article/typesafe-jev-typed-decision-model-calibration-decomposition-shadow-eval)):
  - Asked as one question: Jev 62.6% against Claude Haiku 4.5 at 81.3%.
  - Split into five questions plus logistic regression fitted on 1,000 labels: Jev 95.0% against Haiku 93.2% (not significant).
  - Jev was 12x to 27x cheaper, with a median latency of 239 ms against 687 ms.
- **Rubric grading** (Good Start Labs, 6,003 checks) ([Good Start Labs](https://goodstartlabs.com/research/verification-is-the-bottleneck)):
  - Jev agreed with Claude Fable 5.1 91.5% of the time.
  - Cost per million verdicts: $160 for Jev, against $33,000 for Fable 5.1 and $260 for DeepSeek V4.1 Flash.
  - Latency was about 0.5 s.
- **Kubernetes command risk** (60 cases) ([dev.to](https://dev.to/webofmike/i-benchmarked-jev-on-agent-tool-call-risk-calibration-held-49i3)): 91.7% accuracy, p50 about 420 ms. The author says n is too small to conclude much.
- **Aggregator review** ([dev.to/gde](https://dev.to/gde/jev-after-eight-days-of-independent-tests-level-with-mid-price-llms-behind-the-frontier-1kln)):
  - Verdict: level with mid-price LLMs and 6.5 to 11.5 points behind the frontier.
  - Swapping the order of options changed 32.5% of answers.
  - Russian accuracy fell by 11 points.
  - 0 invalid answers in 23,703 calls.
  - Its claim that the speedup over Haiku is only 2.9x appears to come from the same phishing benchmark, which reported median latencies of 239 ms and 687 ms.
  - I checked only one of the preprints it cites.

**Calibration evidence:** TypeSafe publishes no ECE, reliability plot or Brier score ([blog](https://typesafe.ai/blog/introducing-system-one-models-and-jev)). Independent measurements:
- **scienthoon** ([repo](https://github.com/scienthoon/jev-ood-calibration)):
  - On 900 synthetic tickets it had never seen: ECE 0.107, which is 4.4x the noise floor. Choice and Score answers were overconfident; yes/no answers were underconfident.
  - On OpenBookQA, CommonsenseQA and HellaSwag it was well calibrated (ECE 0.024 to 0.032).
  - The `confidence` field was a worse signal than the top probability.
- **Ibrahim & Zaki** ([arXiv](https://arxiv.org/abs/2609.24574)): better calibrated than 16 of 19 LLMs; items above 0.9 confidence had a median accuracy of 0.815.
- **Phishing benchmark:** ECE 0.154 on the single-question version ([beri.net](https://www.beri.net/article/typesafe-jev-typed-decision-model-calibration-decomposition-shadow-eval)).
- **Die-roll test:** about 83% confidence against 19% accuracy on a random six-sided die ([Substack](https://aiagentssimplified.substack.com/p/the-dark-side-of-jev-83-confidence)).

## 3. Actual usage so far

After nine days, usage is mostly integrations, demos and benchmarks. I found no named production customers ([ts2.tech](https://ts2.tech/en/typesafe-ai-raises-40-million-for-jev-but-its-445x-cost-claim-is-still-self-tested/)).

- **Adoption figures:** Secondary reports say Vercel counted about 13% of paid AI Gateway teams using Jev within 24 hours ([Startup Fortune](https://startupfortune.com/typesafe-ais-decision-model-jev-becomes-vercels-fastest-adopted-launch/), [VentureBeat](https://venturebeat.com/security/companies-are-putting-jev-in-charge-of-ai-agent-decisions-and-prompt-injection-can-influence-the-verdict)). I did not see a primary Vercel source.
- **Integrations:**
  - Vercel documents six ways to call it, including the AI SDK, TanStack AI, Cloudflare Workers and LangChain's `TypeSafeClassifier` ([Vercel](https://vercel.com/i/jev-integrations)).
  - Langfuse offers "Jev as a judge" for evals ([Langfuse](https://langfuse.com/docs/evaluation/evaluation-methods/jev-as-a-judge)).
  - openevals is built on Jev ([GitHub](https://github.com/memovai/openevals)).
- **Hobby demos** collected in [awesome-jev](https://github.com/Amal-David/awesome-jev) (via [HN](https://news.ycombinator.com/item?id=49802160)):
  - Grocery-list categorisation that went from 30 to 60 s down to under 1 s ([mealplannr](https://mealplannr.io/lists)).
  - Restoring spaces while you type ([nospace](https://levmiseri.com/nospace)).
  - A Hacker News feed personaliser ([hn4me](https://hn4me.xyz)).
  - A Chrome extension that filters AI slop from Twitter ([clean-twitter](https://github.com/midplane/clean-twitter)).
  - A prompt-injection detector ([gpu.studio](https://gpu.studio/jev)).
- **Complaints:**
  - On HN (1,979 points), people disputed "can't hallucinate" and the "frontier model" label. One commenter rebuilt similar functionality in about 2 hours with open-weight models. Others suspected astroturfing ([HN](https://news.ycombinator.com/item?id=49717558), [HN](https://news.ycombinator.com/item?id=49802160)).
  - Open-weight replicas already exist, such as Nimble-9B and Luce ([dev.to/gde](https://dev.to/gde/jev-after-eight-days-of-independent-tests-level-with-mid-price-llms-behind-the-frontier-1kln)).

## 4. What it makes possible

- **Near-zero cost per decision:**
  - About $17 per million calls (about $0.0000173 each) for a small classification ([dev.to](https://dev.to/webofmike/i-benchmarked-jev-on-agent-tool-call-risk-calibration-held-49i3)).
  - $0.038 per 1,000 emails, against $0.46 to $1.02 for Haiku ([beri.net](https://www.beri.net/article/typesafe-jev-typed-decision-model-calibration-decomposition-shadow-eval)).
  - $160 per million rubric verdicts ([Good Start Labs](https://goodstartlabs.com/research/verification-is-the-bottleneck)).
  - Together these make it affordable to grade every item, or ask many small questions per item, where that used to mean sampling.
- **Sub-second answers:** Measured medians were 239 to 420 ms. That fits interactive UI and agent pre-action checks, which a 3 to 8 s LLM call does not ([beri.net](https://www.beri.net/article/typesafe-jev-typed-decision-model-calibration-decomposition-shadow-eval), [home](https://typesafe.ai/)).
- **Cheaper accuracy by decomposition:** Many atomic questions per call cost little extra latency. Splitting one judgment into several signals plus a small trained combiner lifted phishing accuracy from 62.6% to 95%.
- **Confidence routing:** Sending only low-confidence items to an LLM matched LLM-only quality at 25 to 50% of the cost ([arXiv](https://arxiv.org/abs/2609.24574)).
- **Valid output every time:** Every answer matched the schema (0 invalid answers across 4,621 and 23,703 calls) ([repo](https://github.com/scienthoon/jev-ood-calibration), [dev.to/gde](https://dev.to/gde/jev-after-eight-days-of-independent-tests-level-with-mid-price-llms-behind-the-frontier-1kln)).

## 5. Open questions and risks

- **Headline speed and cost figures are self-tested.** The ground truth was the average of two LLMs ([ts2.tech](https://ts2.tech/en/typesafe-ai-raises-40-million-for-jev-but-its-445x-cost-claim-is-still-self-tested/)). A TypeSafe employee reportedly measured only a 15.9% end-to-end speedup after replacing one step of a real pipeline ([greennode](https://greennode.ai/blog/what-is-jev)); I did not find the primary source.
- **Calibration depends on the task:** it is good on in-distribution benchmarks and off by a measurable amount elsewhere. Users need labelled data to tune thresholds.
- **Prompt injection:** An injected fake approval dropped the block probability for `rm -rf ~/.ssh` from 0.76 to 0.48 ([VentureBeat](https://venturebeat.com/security/companies-are-putting-jev-in-charge-of-ai-agent-decisions-and-prompt-injection-can-influence-the-verdict)). Changing the order of options also changes answers.
- **Lock-in and opacity:**
  - It is only available through a proprietary API, with no fine-tuning and no published RLCD method or architecture ([Models](https://docs.typesafe.ai/models.md), [HN](https://news.ycombinator.com/item?id=49717558)).
  - The aliases move between versions, so thresholds need version pinning.
- **Capacity:** rate limits can change without notice, and signups were paused on 09-22.
- **Funding and pricing:** TypeSafe raised a $40M seed led by DCVC ([ts2.tech](https://ts2.tech/en/typesafe-ai-raises-40-million-for-jev-but-its-445x-cost-claim-is-still-self-tested/)). No revenue has been disclosed, and it is unclear whether free output and $0.042 per million tokens can last.