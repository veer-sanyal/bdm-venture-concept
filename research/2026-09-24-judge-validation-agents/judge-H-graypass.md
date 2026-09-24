I'd pass. The problem exists, but the version that could win is narrow. It would sit between Okta, which controls the login and session, and Stripe, Castle and Sardine, which already get called at the moment of payment risk. Visa now owns the category leader.

**What the research changed**
- **Hijacked sessions are declining.** The 2025 Verizon Data Breach Investigations Report names session-token theft as a way to get around multi-factor login. But Chrome turned on Device Bound Session Credentials by default on Windows in April 2026. They tie the session cookie to a hardware key on the device, so a stolen cookie is useless elsewhere. Microsoft Entra's Token Protection does the same. What's left is an attacker working on the victim's own device through remote access, or the real user being tricked.
- **The biggest fraud numbers don't fit the product.** In the 2025 AFP payments fraud survey, 79% of organizations saw attempted or actual payments fraud, and business email compromise (fake emails that trick staff into paying) was the top method at 63%. In that fraud a real employee changes vendor bank details in their own session because an email fooled them. Typing and mouse patterns would match that user's normal pattern, so the check passes. The same goes for a "pressured employee."
- **The AI-agent use case gives the product nothing to measure.** An agent produces no typing or mouse movement, so the only thing you can check is the human approving it. Auth0 already sells that approval step: it pauses the agent and sends the user a push request to confirm.
- **The standards claim holds.** NIST SP 800-63B-4 section 5.3 "Session Monitoring" names typing cadence as a signal and says to reauthenticate, end the session or notify support.
- **Accuracy in real use is weaker than the headline studies.** Lab tests report error rates as low as 0.29%. Free-text typing studies vary widely, and one that mimicked current writing habits got 5.1% to 10.4% equal error rate, the point where false accepts equal false rejects. A payout change or admin grant takes a few clicks, so there is very little typing to judge.

**Who already serves this customer**
- **Banks:** BioCatch had $185M annual recurring revenue in 2025 from about 350 banks, and Visa is buying it for $2.4B. Experian bought NeuroID (2024), LexisNexis owns BehavioSec, Mastercard owns NuData, and Ping bought Keyless (January 2026).
- **Checks inside software apps:** Castle charges $0.005 per risk check and has a documented profile-update event. Sardine scores in-session typing and swiping. Transmit Security's Mosaic includes behavioral biometrics.
- **Checking the person behind each high-risk action:** IronVest ActionID sells exactly this to banks.
- **Workforce and login:** Okta Identity Threat Protection re-checks risk during the session and forces reauthentication. TypingDNA ActiveLock does continuous typing verification on the desktop and cites the NIST section.

## 1. Strongest version

A per-action decision service for money-movement changes on software platforms that pay out money: payroll direct-deposit changes, accounts-payable vendor bank edits, and payout accounts on marketplaces and vertical software with built-in payments. It sells to the platform's risk team, not the security team.

It wouldn't pitch the behavioral signal as catching fraud alone. It would combine behavior with device binding and detection of remote-access tools to cut unnecessary re-verification prompts. The signed decision record would serve as liability evidence when a customer disputes a loss. Drop workforce admin rights (Okta's territory) and AI agents (Auth0's).

## 2. Ratings for that version

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 3 | Payout-redirect fraud is real, but its biggest source is the real user being deceived, which behavior matching can't flag. |
| Value over today | 2 | Buyers already combine step-up prompts, Okta's in-session checks, device-bound sessions and $0.005 risk calls. The extra lift from behavior on a few clicks is unproven. |
| Market size | 2 | The category leader reached $185M ARR by selling to banks, and non-bank software platforms are a smaller pool. |
| Risk (5 = low) | 2 | GDPR Article 9 covers behavioral data used for unique identification, Illinois BIPA carries statutory damages, and incumbents can add this to products buyers already use. |

**Do incumbents own the data or the buying channel?** Yes. Okta owns the session and the security buyer. Stripe (Radar, Connect) and Sardine or Castle already get called at the moment of payout risk. BioCatch/Visa owns banks. A startup would be asking the platform to add a second risk call next to one it already makes.

## 3. What would kill it

It dies if, in real payout-change fraud on these platforms, few cases involve someone other than the account owner at the keyboard. It also dies if the device, IP and session signals these platforms already have flag most of those cases.

**Fastest test:** call 10 heads of fraud or risk at payroll, accounts-payable and payout platforms. Ask each for last year's count and dollar losses from payout changes made by someone other than the account owner, and how many their current tools flagged. That fits in about two weeks and needs no data access. Stop if the typical platform loses under about $250K a year on these cases, or if its existing tools already flag most of them.

VERDICT: PASS

Sources:
- [Visa acquires BioCatch (Biometric Update)](https://www.biometricupdate.com/202608/visa-acquires-behavioral-biometrics-pioneer-biocatch-amid-fraud-prevention-build-up)
- [BioCatch revenue (Sacra)](https://sacra.com/c/biocatch/)
- [Experian acquires NeuroID](https://www.experianplc.com/newsroom/press-releases/2024/experian-acquires-behavioral-analytics-pioneer-neuroid)
- [Ping acquires Keyless](https://www.fintechfutures.com/m-a/ping-identity-acquires-uk-biometrics-firm-keyless)
- [Okta Identity Threat Protection](https://help.okta.com/oie/en-us/content/topics/itp/overview.htm)
- [Auth0 for AI agents](https://auth0.com/blog/agents-can-be-useful-or-secure/)
- [IronVest ActionID](https://ironvest.com/technology/actionid)
- [TypingDNA on NIST 800-63B-4 session monitoring](https://blog.typingdna.com/nist-sp-800-63b-rev-4-session-monitoring/)
- [NIST SP 800-63B-4](https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-63B-4.pdf)
- [Chrome device-bound sessions now generally available (Google Workspace)](https://workspaceupdates.googleblog.com/2026/05/prevent-account-takeovers-with-DBSC-now-generally-available-in-the-Chrome-browser-for-Windows.html)
- [Entra Token Protection](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-token-protection)
- [Verizon 2025 DBIR takeaways (Descope)](https://www.descope.com/blog/post/dbir-2025)
- [2025 AFP Payments Fraud and Control Survey highlights (Truist)](https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2025-afp-payments-fraud-control-survey-report-key-highlights.pdf)
- [Castle pricing](https://castle.io/pricing/)
- [Sardine account takeover](https://www.sardine.ai/account-takeover-protection)
- [Transmit Security Mosaic](https://transmitsecurity.com/platform)
- [Keystroke dynamics survey (arXiv)](https://arxiv.org/html/2303.04605v2)
- [Biometric privacy regimes (Lewis Rice)](https://www.lewisrice.com/publications/privacy-regimes-for-protecting-biometric-information)
