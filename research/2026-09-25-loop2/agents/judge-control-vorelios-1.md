I checked the concept against primary sources. A company with almost exactly this pitch exists: **Vorelios**, in YC's Fall 2026 batch. Its site says it is building "a foundation model for engineering physics" that starts with aerodynamics, is differentiable, and evaluates "50,793 designs in the time a conventional solver completes one" (about 14 hours). As instructed, I treated it as this team, not a competitor. The site names no customers and says it wants "to work closely with a small number of engineering teams."

## Key claims checked

- **Solves are slow and expensive: true.** Each case in DrivAerNet++ used 256 cores. The original DrivAerNet dataset took about 352,000 CPU hours in total. DrivAerML uses hybrid RANS-LES, "the highest-fidelity scale-resolving CFD approach routinely deployed by the automotive industry."
- **Seconds instead of hours: true inside the training distribution.** Siemens says its PhysicsAI is "up to 1,000x faster" than a solver. Emmi and Luminary make similar claims.
- **Works on new kinds of designs: not proven.** A 2025 benchmark ("Geometry Matters", arXiv 2501.01453) found "all models struggle with out-of-distribution generalization." A one-model-for-everything pitch depends on exactly this.
- **Differentiable, with solvers kept for final checks: real, but no longer a differentiator.** Every major competitor offers it.

## Who already serves this customer

| Player | Status (primary sources) |
|---|---|
| PhysicsX | $300M Series C in June 2026 at about $2.4B, building "Large Physics Models". Recognized revenue doubled and customer count more than doubled year on year. Backed by NVIDIA and Siemens. |
| Neural Concept | $100M Series C in December 2025, led by Goldman Sachs. More than 50 enterprise customers, including GM, GE Vernova, Safran, Renault and several F1 teams. |
| Luminary Cloud | $72M Series B in September 2025. Already ships pretrained aero models (SHIFT-SUV with Honda, SHIFT-Wing, drone, submarine and pump models). Customers include Northrop, Joby and Otto. |
| Emmi AI | Transformer-based physics models. Bought by Mistral in May 2026. |
| NVIDIA | DoMINO car-aero model, trained on 3,200 simulations, available free as a packaged service in the open-source PhysicsNeMo framework. |
| Ansys (Synopsys) and Siemens | Sell AI prediction add-ons (SimAI, PhysicsAI) inside the simulation tools engineers already use. Siemens has folded Altair's tools into its Simcenter suite (July 2026 release). |

**Does an incumbent own the data or buying channel? Yes, at large manufacturers.** Ansys/Synopsys, Siemens/Altair and Dassault hold the enterprise license agreements, the simulation tools, and the data pipelines and file formats that sit in them. They now sell AI add-ons through that same channel. The customer owns its simulation archive, but the incumbents control where it lives and how it is bought. The channel is less locked among younger drone, eVTOL and defense-aero firms.

## 1. Strongest version

A general "foundation model for all physics" means racing PhysicsX, NVIDIA and Mistral with far less money, and a two-person startup won't win that. The narrower version with the best chance:

- **Customer:** the fast-growing group of drone, eVTOL and small defense-aero companies. They have 1 to 5 aerodynamicists, small archives of past simulation results, and can't afford PhysicsX-style engagements.
- **Product:** a pretrained external-aero model that is useful on day one without the customer's own training data. It fine-tunes on a few dozen of their runs, does gradient-driven shape optimization, and has a built-in "verify top N in OpenFOAM/SU2" step.
- **Pricing:** usage-based, self-serve pilot, then per-team licenses.
- **The edge:** zero-shot accuracy, meaning accurate predictions before any customer data. SimAI, PhysicsAI and Neural Concept all need hundreds of customer runs for training. Luminary is the direct threat to this version, and the edge holds only if Vorelios's zero-shot accuracy clearly beats Luminary's SHIFT models and NVIDIA's DoMINO.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 4 | Buyers already pay: Neural Concept has more than 50 enterprise customers including GM, Safran and F1 teams, and PhysicsX's recognized revenue doubled year on year. |
| Value over today | 2 | Faster, differentiable prediction is already bundled into Ansys and Siemens tools, offered free by NVIDIA, and pretrained by Luminary. The one open edge (zero-shot accuracy on new designs) is unproven in the literature. |
| Market size | 3 | CAE software is about $8–13B (analyst estimates vary by scope). The AI-prediction slice for small aero firms is a small part of that, though it could widen to other physics later. |
| Risk (5 = low) | 2 | Training data is very expensive to generate (about 352,000 CPU hours for one car dataset). Generalization to new designs is unproven. Rivals have $100–300M rounds, and incumbents bundle the feature into existing licenses. |

Total: 11 out of 20.

## 3. What would kill it, and the fastest test

**Killer:** on a real customer's own designs, the pretrained model is not accurate enough to rank designs correctly without fine-tuning on that customer's data. It then becomes one more surrogate trained on the customer's data, which the customer can already get inside Ansys or Siemens, or free from NVIDIA.

**Fastest test (about 2 weeks):**
1. Get 2 or 3 drone or eVTOL teams to hand over about 20 designs each that they have already solved, with no training on their data.
2. Predict lift, drag and moments zero-shot, and do the same with Luminary SHIFT-Wing and NVIDIA DoMINO as free baselines.
3. **Kill** if the model's design ranking doesn't match the solver's closely (roughly Spearman below 0.9, or drag error of more than a few percent), or if it doesn't clearly beat the free baselines.
4. **Continue** if it does, and at least one team agrees to a paid pilot.

This is all desk research, not customer validation. No engineer has been asked whether they would switch or pay.

Sources:
- [Vorelios site](https://vorelios.com/) · [Vorelios YC profile](https://www.ycombinator.com/companies/vorelios)
- [PhysicsX $300M Series C](https://www.physicsx.ai/newsroom/physicsx-announces-300m-series-c-to-accelerate-physics-ai-for-industrial-engineering)
- [Neural Concept $100M Series C](https://www.neuralconcept.com/post/neural-concept-closes-100m-funding-round-led-by-growth-equity-at-goldman-sachs-alternatives-to-scale-ai-native-engineering) · [SiliconANGLE coverage](https://siliconangle.com/2025/12/18/ai-aided-design-software-startup-neural-concept-raises-100m-accelerate-product-engineering/)
- [Luminary $72M Series B](https://luminary.ai/resources/luminary-cloud-secures-72m-series-b-to-lead-the-physics-ai-era/) · [Luminary SHIFT-SUV](https://luminary.ai/resources/luminary-cloud-unveils-first-physics-ai-open-source-automotive-foundation-model-for-suv-aerodynamics-in-collaboration-with-honda-and-nvidia/) · [Washington Technology on SHIFT defense models](https://www.washingtontechnology.com/companies/2026/01/luminary-cloud-expands-physics-ai-toolkit-defense-focused-models/410679/)
- [Mistral acquires Emmi (The Next Web)](https://thenextweb.com/news/mistral-emmi-ai-physics-vienna-industrial)
- [Ansys SimAI 2026 R1](https://ansys.synopsys.com/blog/introducing-ansys-geomai-software) · [Siemens Simcenter PhysicsAI](https://www.siemens.com/en-us/products/simcenter/engineering-data-science-ai/physicsai/) · [Siemens unified Simcenter, July 2026](https://www.prnewswire.com/news-releases/siemens-accelerates-engineering-simulation-with-a-unified-ai-powered-simcenter-portfolio-302835381.html)
- [NVIDIA DoMINO NIM](https://docs.nvidia.com/nim/physicsnemo/domino-automotive-aero/latest/overview.html)
- [DrivAerML](https://arxiv.org/abs/2408.11969v2) · [DrivAerNet](https://arxiv.org/pdf/2403.08055) · [DrivAerNet++](https://arxiv.org/pdf/2406.09624) · [Geometry Matters benchmark](https://arxiv.org/pdf/2501.01453) · [NeurIPS 2024 ML4CFD retrospective](https://arxiv.org/abs/2506.08516)
- [CAE market size (MarketsandMarkets)](https://www.marketsandmarkets.com/Market-Reports/computer-aided-engineering-market-33357366.html) · [Ansys revenue (Wikipedia)](https://en.wikipedia.org/wiki/Ansys)

VERDICT: PASS
