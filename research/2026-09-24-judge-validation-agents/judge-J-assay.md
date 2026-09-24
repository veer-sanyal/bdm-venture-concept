## Claim check

| Claim in the pitch | What primary or near-primary sources show |
|---|---|
| Companies recheck every AI output | True at first, but it doesn't last. In a [Solventum autonomous-coding case](https://www.solventum.com/en-us/home/health-information-technology/resources-education/case-studies/ai-in-healthcare-autonomous-medical-coding-journey/) (quoted from search snippet), a health system started with 100% QA review. Once it trusted the tool, "95% of accepted confident codes are no longer reviewed." It got there with no outside certificate. |
| Nobody can prove the error rate on unchecked work | Partly true. Vendors publish their own numbers. [Fathom](https://fathomhealth.com/) claims 90%+ automation and 96%+ accuracy "through ongoing audit programs". [CodaMetrix](https://www.codametrix.com/) claims over 96% automation. [Vic.ai](https://www.vic.ai/) claims 85% of invoices with no human touch and 97 to 99% accuracy. [IKS Health](https://ikshealth.com/insights/press-releases/iks-health-announces-launch-of-audit-ready-autonomous-coding-capabilities/) (Apr 2026) routes low-confidence codes to humans. What is missing is an independent, blind measurement with a stated confidence level. |
| The statistics are established | True, and open to anyone. [Learn then Test](https://arxiv.org/abs/2110.01052) (Angelopoulos, Bates et al.) is exactly this method: it picks the confidence threshold so that error among auto-passed items stays under α at confidence 1−δ. Scale AI published [READY](https://arxiv.org/html/2609.02095) in Sept 2026. It picks the cheapest human-review policy that meets a reliability target and qualifies it on held-out cases. [Hyperscience](https://help.hyperscience.ai/v41/docs/transcription-accuracy-and-automation) already re-sets its threshold every night, from QA samples, to hit a customer-set target accuracy. |
| An auditor can read the certificate | Weak. The document a financial auditor relies on for a third party's controls is a [SOC 1 report](https://www.aicpa-cima.com/cpe-learning/publication/reporting-on-an-examination-of-controls-at-a-service-organization-relevant-to-user-entities-internal-control-over-financial-reporting-soc-1-guide), and only a CPA firm can issue one (AT-C 320). [PCAOB AS 2315](https://pcaobus.org/oversight/standards/auditing-standards/details/AS2315) has the auditor set its own tolerable rate and sample. A software vendor's certificate is at most evidence for a control the company runs itself, which the auditor then tests. |
| A payer can read the certificate | Not verified against a primary source. Payers run their own post-payment audits, and I found no payer that accepts a provider-side accuracy certificate. Treat this claim as false until someone shows otherwise. |
| Blinding matters | Supported. Automation-bias research finds people follow wrong automated advice more often ([HDSR 2026](https://hdsr.mitpress.mit.edu/pub/nrcn4h7d/release/2)). Blind redo is the one piece here that is new. |

The sampling cost is my own calculation (Clopper-Pearson one-sided bound, 80% chance of passing). To certify under 2% error at 95% confidence:
- If the true error among auto-passed items is 0.5%, it takes about 400 blind redos per workflow per month.
- At 1%, about 975.
- At 1.5%, about 4,375.

That number does not shrink with volume. At roughly 8 minutes per chart, 975 medical-coding redos is about 130 staff hours a month for each workflow. Only high-volume workflows can carry that.

## Who already serves this customer

- **The AI vendors own the data and the thresholds.** Fathom, CodaMetrix, Solventum, IKS, Vic.ai and Hyperscience each measure accuracy and route by confidence inside their own products.
- **MDaudit owns the medical-coding audit workflow.** It says it is used by [70 of the top 100 US health systems](https://intuitionlabs.ai/software/medical-coding-computer-assisted-coding-cac/coding-auditing-and-compliance/mdaudit). It already publishes guidance on [auditing autonomous coding](https://mdaudit.com/blog/auditing-autonomous-medical-coding-systems/), with a 95% accuracy target and risk-based sampling, and sells an AI "Auditor Assist" product. This is the incumbent in the buying channel.
- **Assurance and insurance players sell to the "prove it to buyers" need that vendors would pay for.**
  - [Armilla](https://www.armilla.ai/ai-performance-warranty-brief) pays out if accuracy drops below a verified threshold. The warranty is backed by Swiss Re and Chaucer.
  - [AIUC-1](https://aiuc.com/) is an insured certification that re-tests every quarter.
  - [PwC Assurance for AI](https://www.pwc.com/us/en/about-us/newsroom/assurance-ai-press-release.html) launched June 2025.
  - [KPMG AI Trust](https://kpmg.com/sg/en/home/insights/2025/05/kpmg-launches-ai-trust-services-to-transform-ai-governance-enabled-by-servicenow.html) launched May 2025.
- **Eval platforms already have review queues.** [LangSmith, Braintrust and Arize](https://www.langchain.com/resources/langsmith-vs-braintrust) all have human-review queues on production traces. [Cleanlab](https://cleanlab.ai/blog/trustworthy-language-model/) claims under 1% error while reviewing under 20% of items.

## 1. The strongest version

Drop the idea that one certificate can be read by controllers, auditors and payers alike. Start in one vertical, **health-system autonomous coding**, and sell to the health system's own compliance and revenue-integrity team. It is not a certificate for vendors to wave at buyers.

The product is a vendor-neutral qualification loop:
- Draw a monthly blind sample from each specialty and code family.
- Have the system's own coders redo those charts without seeing the AI's answer.
- Use Learn-then-Test to set which charts go straight to billing.
- Detect drift and pull a code family back to human review automatically when it fails.

The output is compliance evidence the health system owns. A second product is the same measurement sold as underwriting data to warranty providers like Armilla or AIUC. Collecting the "vendor pays" revenue this way avoids the conflict of the AI vendor paying for its own grade, the same problem credit-rating agencies have.

## 2. Ratings (strongest version)

- **Customer need: 3.** The need is real, but health systems already cut review from 100% to about 5% of confident codes using the vendor's own data (Solventum case).
- **Value over what customers use today: 2.** Hyperscience already re-sets thresholds from QA samples to a target accuracy, the AI vendors run audit programs, and MDaudit sits in the audit workflow. What this adds is blinding, independence and a confidence bound, and nobody yet requires those.
- **Market size: 2.** The US coding market is [$21.6B](https://www.grandviewresearch.com/industry-analysis/us-medical-coding-market), but certification is a thin slice of it. The fixed cost of about 1,000 redos per workflow per month limits the product to high-volume workflows, and the vendor-paid phase is a few hundred AI vendors.
- **Risk: 2 (5 means low risk).**
  - Incumbents hold both the data and the channel.
  - Scale AI has published the method.
  - The certificate has no regulatory standing, because only CPA firms issue attestations auditors rely on and payers audit on their own.

## 3. What would kill it, and the fastest test

**What kills it.** Buyers already stop reviewing on the vendor's numbers, and the certificate changes nothing for the controller, auditor or payer. Everything else is secondary. If that holds, the product is a feature MDaudit or a Big Four assurance practice adds.

**Fastest test (about two weeks).**
1. Build a mock monthly certificate from one real autonomous-coding deployment.
2. Show it to 10 HIM or compliance leaders who already run autonomous coding. Ask each whether their compliance officer would approve a lower review rate on the strength of it, and for a paid one-month pilot LOI at about $3k.
3. Put the same question to 3 external audit partners, asking whether they would test fewer items because of it.

If fewer than 2 of the 10 commit, and no audit partner says it would reduce their testing, kill it.

The statistics are open-source and the blind protocol is easy to copy. The buying channel belongs to MDaudit and to the AI vendors, and the certificate's claimed readers either do not accept outside certificates (payers) or accept them only from CPA firms (auditors).

VERDICT: PASS
