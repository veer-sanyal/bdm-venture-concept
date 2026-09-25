# Judge, P3 (control: Kailash Labs), judge 1 of 3 — loop 2, 2026-09-25

Saved by the orchestrator from the judge's final reply. Scores: need 3, value 3, market 4, risk 2 (total 12). VERDICT: PASS.

The judge matched the pitch to NemoStation / Kailash Labs ("auto vision factory", Marlin-2B) and treated it as this team.

## Claims checked
- Headline benchmark overstated. The YC listing says Marlin "matches Gemini-2.5-flash"; the [model card](https://huggingface.co/NemoStation/Marlin-2B) says: DREAM-1K captioning lands between Tarsier-34B and Gemini-1.5-Pro; TimeLens-Bench "matches Gemini-2.0-Flash", +6.4 mIoU over Qwen2.5-VL-7B; tops CaReBench. The [site](https://nemostation.com/) says "competitive with Gemini-2.5". Academic benchmarks, not security or factory footage.
- Marlin is a general model (Qwen3.5-2B on ~400K public clips labelled by Gemini-3-Flash, one H100); shows capability, not customer-specific distillation. ~3.3K downloads last month; no customers, pricing or on-prem offer found.
- Cost problem real at 24/7: ~100 tokens/sec ([docs](https://ai.google.dev/gemini-api/docs/video-understanding)); at [list prices](https://ai.google.dev/gemini-api/docs/pricing) one always-on camera costs ~$300–950/yr; ~$0.3–1M/yr per 1,000 cameras. [Twelve Labs](https://www.twelvelabs.io/pricing) indexes at $2.52/hour. A 2B model on own hardware could cut this ~10x; frame sampling, motion gating and price cuts narrow the gap.

## Who else serves this customer
- Security platforms own footage and channel: [Milestone](https://www.milestonesys.com/company/news/press-releases/milestone-launches-vision-language-model/) (traffic VLM on Cosmos Reason, 75,000 hours, inside XProtect and sold to third parties); [Verkada](https://www.securityworldmarket.com/int/News/Product-News/verkada-launches-ai-powered-search1); Genetec.
- NVIDIA's free on-prem [video search and summarization blueprint](https://github.com/NVIDIA-AI-Blueprints/video-search-and-summarization).
- Distillation/on-prem sellers: [Roboflow](https://blog.roboflow.com/fine-tune-deploy-qwen2-5-vl/), [Twelve Labs air-gapped](https://www.twelvelabs.io/blog/air-gapped-deployment), [Inference.net ClipTagger-12b](https://inference.net/blog/cliptagger-12b/) (15–17x cheaper), YC's OnDeck AI and OpenVector.
- Manufacturing and logistics less locked up (integrators, machine-vision vendors).

## 1. Strongest version
A model supplier for companies that build video products: custom small video models for mid-tier VMS makers, camera/NVR makers, security-AI startups, fleet dashcam makers; per-model build fee plus per-stream or per-device license. Goes through the channel owners; turns custom builds into recurring per-device revenue. Second wedge: video archives.

## 2. Ratings
| | Score | Evidence |
|---|---|---|
| Need | 3 | Demand shows up through platforms (Milestone, Verkada, NVIDIA); no end enterprises found asking for custom models |
| Value | 3 | ~10x cheaper than Gemini Flash at 24/7 and on-prem, but Cosmos Reason with free fine-tuning, Roboflow and Milestone cover much of it |
| Market | 4 | AI video analytics [$5–6B in 2025 to ~$17B by 2031](https://www.mordorintelligence.com/industry-reports/global-ai-video-analytics-market); the model-supplier slice is smaller |
| Risk | 2 | Custom-model services low margin and commoditizing; Flash-Lite $0.10/M and falling; channel owners building their own; benchmark overstated |

## 3. Kill and fastest test
Kill: task fine-tuning becomes a checkbox in NVIDIA tools or existing VMS, and frontier prices fall 5–10x more. Test: two-week bake-off with one or two platform buyers on one real task and ~100 hours of their footage, against Cosmos Reason fine-tuned and Gemini Flash-Lite with frame sampling, ending in a paid-pilot ask.
