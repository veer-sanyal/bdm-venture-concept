**Note:** This is desk research only. No customers were contacted, so none of this counts as customer validation.

**Exact match:** Vorelios (YC Fall 2026, two founders) pitches "foundation models that learn physics end-to-end and deliver the same results in seconds." I treat it as this team, not a competitor, and I judged the idea only.

## Checking the key claims
- **"Solves take hours or days."** True, but that gap is shrinking. GPU solvers now run full-vehicle high-fidelity CFD "in hours—not days" (Cadence Millennium). An LES run of an aircraft in landing configuration takes under 14 hours on two GPU nodes.
- **"Predicts physics in seconds."** Shown in public research. Emmi's AB-UPT model predicts drag within 1% on 45-million-cell cars in under 34 seconds (arXiv 2502.09692). The catch: it works within a product family. Even Neural Concept says "major topology changes or radically different regimes require retraining." Detecting when a model is outside what it was trained on is still an open research problem (arXiv 2607.10333).
- **"Differentiable, so it can drive optimization."** True, but not unique. Adjoint solvers and optiSLang+SimAI already run optimization loops, and every competitor offers this.
- **The need is real and paid for.** PhysicsX raised a $300M Series C in June 2026 at about $2.4B, with booked revenue tripled. Neural Concept raised $100M in December 2025; it has 4x enterprise revenue in 18 months, and customers include GM, Safran and several F1 teams. Luminary raised a $72M Series B (Joby, Piper, Otto, Honda).

## Who else serves this customer
- **Incumbents own both the data and the buying channel.** Simulation results are produced in, and stored by, Ansys (now Synopsys), Siemens (now with Altair), Dassault and Cadence tools. Each now bundles a surrogate trainer into licenses customers already hold: Ansys SimAI Pro/Premium and Siemens Simcenter PhysicsAI ("up to 1,000x faster").
- **NVIDIA gives away the core model.** PhysicsNeMo with DoMINO is open source and available as a NIM, and GM itself published an SAE paper using it.
- **Funded specialists:** PhysicsX, Neural Concept, Luminary (open SHIFT foundation models), BeyondMath ($18.5M seed) and Navier AI (YC W24).
- **Two signals about the category:**
  - Mistral bought Emmi AI in May 2026, so big AI labs are moving in.
  - Navier AI began with physics foundation models and moved to agents.

## 1. Strongest version
A pretrained external-aerodynamics model for airframe teams that have no simulation archive: drone, UAV, defense and eVTOL startups, plus motorsport.
- **Why this niche:** SimAI and PhysicsAI need years of the customer's own solver runs. This version works from day one, using CFD data the company generates itself, and improves with a few dozen of the customer's cases.
- **Trust built in:** every prediction comes with a calibrated confidence score, low-confidence designs go automatically to a solver, and the results tell the engineer how to rank designs.
- **Pricing:** per seat plus usage, sold alongside open solvers such as OpenFOAM or cloud CFD, not against the Ansys or Siemens enterprise agreement.

## 2. Ratings
| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | PhysicsX tripled booked revenue and Neural Concept 4x'd enterprise revenue, so buyers are paying now. |
| Value over today | 2 | SimAI and PhysicsAI are bundled into existing licenses, DoMINO is free, and pretraining hasn't been shown to beat fine-tuning on the customer's own data. |
| Market size | 4 | CAE software is about $8–13B a year (analyst ranges vary), and PhysicsX's $2.4B valuation shows the physics-AI layer can be large. |
| Risk (5 = low) | 2 | Five or more well-funded rivals plus incumbents that own the channel. Confidence on new shapes is unsolved, which is a problem in safety-critical work, and faster GPU solvers shrink the speed gain. |

**Total: 12/20.**

## 3. What kills it
Pretraining doesn't carry over to new designs. If a customer's own few dozen runs, used to train a free DoMINO or SimAI model, match the foundation model's accuracy, then the "foundation" is worth nothing. The company becomes a services shop, competing with free tools and with features incumbents already bundle.

**Fastest test (about 2–3 weeks):** a blind bake-off with one drone or eVTOL design partner.
1. The partner hands over 10–20 archived CFD cases the model has never seen.
2. Compare three things on those cases:
   - the pretrained model with no fine-tuning, and again after fine-tuning on 10 cases;
   - DoMINO trained from scratch on those same 10 cases;
   - the partner's solver, as ground truth.
3. Before starting, the partner names the accuracy they would act on, for example drag within 2% and the correct ranking of the top three designs.

If the pretrained model doesn't clearly beat the free baseline at that threshold, stop.

VERDICT: PASS

Sources:
- [Vorelios, YC](https://www.ycombinator.com/companies/vorelios)
- [PhysicsX Series C](https://www.physicsx.ai/newsroom/physicsx-announces-300m-series-c-to-accelerate-physics-ai-for-industrial-engineering)
- [Neural Concept $100M](https://www.businesswire.com/news/home/20251218764112/en/Neural-Concept-Closes-$100M-Funding-Round-Led-by-Growth-Equity-at-Goldman-Sachs-Alternatives-to-Scale-AI-Native-Engineering)
- [Luminary $72M](https://siliconangle.com/2025/09/15/luminary-cloud-raises-72m-advance-ai-driven-physical-product-design/)
- [Luminary SHIFT-SUV](https://www.prnewswire.com/news-releases/luminary-cloud-unveils-first-physics-ai-open-source-automotive-foundation-model-for-suv-aerodynamics-in-collaboration-with-honda-and-nvidia-302424056.html)
- [Mistral acquires Emmi](https://www.emmi.ai/news/mistral-ai-acquires-emmi-ai)
- [AB-UPT paper](https://arxiv.org/abs/2502.09692)
- [Ansys SimAI 2026 R1](https://ansys.synopsys.com/blog/introducing-ansys-geomai-software)
- [Siemens Simcenter PhysicsAI](https://www.siemens.com/en-us/products/simcenter/engineering-data-science-ai/physicsai/)
- [Siemens Simcenter summer 2026](https://news.siemens.com/en-us/siemens-simcenter-summer-2026/)
- [NVIDIA DoMINO](https://docs.nvidia.com/physicsnemo/latest/physicsnemo/examples/cfd/external_aerodynamics/domino/README.html)
- [SAE GM PhysicsNeMo paper](https://saemobilus.sae.org/papers/automotive-aerodynamics-surrogate-modeling-using-nvidia-physicsnemo-mid-sized-suv-gm-dataset-2026-01-0600)
- [Cadence Millennium](https://www.cadence.com/en_US/home/tools/system-analysis/computational-fluid-dynamics/millennium-m1.html)
- [BeyondMath seed](https://tech.eu/2026/02/25/beyondmath-secures-185m-to-expand-the-worlds-largest-foundational-physics-ai-model/)
- [Navier AI](https://navier.ai/)
- [Burhop, AI surrogates in CFD/FEA](https://burhop.substack.com/p/ai-surrogates-in-cfd-and-fea)
- [NeuroForge OOD trust paper](https://arxiv.org/html/2607.10333)
- [CAE market estimates](https://www.grandviewresearch.com/industry-analysis/computer-aided-engineering-cae-market)

VERDICT: PASS
