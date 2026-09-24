## Team fit: bureau-dispute investigation software

This is desk research only. No customer has confirmed any of it.

### What stands between two students and this market

Building the model is not the hard part. Three things gate the business:

1. **A customer that lets them touch its disputes.** Bureau disputes reach the lender through e-OSCAR, the dispute system the credit bureaus own and run through a company called OLDE. An outside vendor gets in only when a lender signs e-OSCAR's API license plus an "Addendum Regarding Utilization of Third-Party Service Provider." The lender's own e-OSCAR account costs $90 to register. I found no "certified e-OSCAR middleware" program. The certification that does exist is RMAI's Certified Receivables Vendor (CRV). RMAI is the debt-buyer trade group, and its standards cover chain of title, disputes and credit reporting. So the investor's "certified middleware" framing should become "licensed through the customer, with CRV later."
2. **Being allowed near consumer data.** Lenders' vendor-risk teams will ask for a SOC 2 report, an outside audit of the vendor's security controls. A Type I report takes about 6 to 12 weeks and costs $10k to $25k with a small audit firm and automation tooling. A Type II needs a months-long observation window, so it cannot happen this semester.
3. **An incumbent already owns the channel.** Sonnet, formerly Palinode and bought by Provana in February 2025, automates e-OSCAR and direct-dispute work. Provana says it handles over 1 million disputes a month for 200+ clients. It integrates with the collection and loan systems these customers already run (Jack Henry, Fiserv, Genesys, DAKCS, Nortridge, Ontario Systems), and its triage is checklist-based. Bridgeforce also sells a disputes module. WebRecon has owned the litigious-consumer data since 2009.

The opening that looks real is the one the investor named: pulling the account-level documents for purchased debt and writing a file that defense counsel can use. The legal basis is *Hinkle v. Midland* (11th Cir. 2016). The court held that a jury could find a debt buyer willfully violated the FCRA when it marked accounts "verified" after checking only its own electronic records, even though its purchase contract let it request documents from the seller. The pitch is "the Hinkle-proof file," not "faster ACDVs" (an ACDV is the dispute form e-OSCAR sends the lender). Sonnet already sells speed.

### What they need, and how to get it this semester

| Need | How to get it by December |
|---|---|
| **Domain fluency** | CDIA's FCRA Certificate for Data Furnishers (2 to 4 hours, from $65) and its Metro 2 e-learning course (2 to 3 hours). Metro 2 is the credit-reporting data format. Also read FCRA §1681s-2(b), *Hinkle*, and the NCLC chapter on e-OSCAR. About 2 weeks. |
| **A data corpus with no customer** | Lost FCRA §1681s-2(b) cases on CourtListener and PACER. Summary-judgment filings often attach the actual ACDVs and investigation notes. Read 20 to 30 opinions where the furnisher lost and pull out what an unreasonable record looks like. That becomes the product spec, the demo data and the pitch evidence. I have not checked how often ACDVs appear as exhibits, so test it in week 1. |
| **Credibility with buyers** | One advisor from each side. A consumer-finance defense attorney says what a usable file contains. A plaintiff FCRA attorney says what wins against one. Add a retired dispute-operations manager from a debt buyer if one turns up. Cold email works because these people get few student requests. |
| **Security posture** | Deploy inside the customer's own cloud account, so the consumer data and e-OSCAR credentials never leave it. That lightens the vendor review a lot. Write the security policies now in a SOC 2 automation tool's startup tier. Pay for the Type I audit only after a signed letter of intent (LOI) or a grant covers it. |
| **Litigation-risk scoring** | License WebRecon's litigant feed instead of building one. A student-built repeat-plaintiff list will not beat a 16-year-old dataset. |
| **First customers** | Target mid-size RMAI-certified debt buyers and regional subprime auto and installment lenders. Skip the top five buyers, which run dispute operations in-house or through Provana. Search LinkedIn for titles like Credit Reporting Manager, Dispute Resolution Manager and Compliance Officer. insideARM and the Purdue alumni network are warm channels. The RMAI Annual Conference (Las Vegas, Feb 8 to 11, 2027) is where the whole buyer list shows up. Plan to arrive with a demo and a pilot in progress. |

### Semester sequence

- **Weeks 1 to 3.** Finish the CDIA courses, build the case-law corpus, and start 25 discovery calls. Ask each person three things. What does your investigation file look like today? Have you lost or settled a §1681s-2(b) case over it? Do you use Sonnet or build your own?
- **Weeks 3 to 8.** Offer a pilot that needs no integration. Ask a customer for 50 to 100 closed disputes, redacted, plus any FCRA suits they were served on those accounts. Return a gap report showing which "verified" responses lacked account-level documents. It needs no e-OSCAR license and no SOC 2, and it shows the product's value directly.
- **Weeks 8 to 14.** Turn one gap report into a paid pilot or LOI at $1 to $3 per dispute, limited to identity and ownership disputes on purchased debt. The customer's legal team starts the e-OSCAR third-party addendum. Start SOC 2 Type I if the LOI funds it.

By the end of the semester, a realistic target is a demo built on public-record disputes, two advisors, and one or two LOIs. A live e-OSCAR integration and a SOC 2 report are unlikely by December. CRV certification and pricing tied to settlement spend belong after the first customer.

### Signals that should stop them

- Most dispute managers say "Sonnet already does this."
- No customer will share even a redacted sample.
- Lenders' legal teams refuse to sign the third-party addendum for a pre-revenue student company.
- Debt buyers reject "default to delete." Deleting a tradeline removes pressure to pay, so compliance and collections may disagree inside the same company. Ask this on every call.

One side note: the pitch's lawsuit numbers hold up. WebRecon reported FCRA filings up 37.4% year to date in February 2026 and up 44.6% through July. I did not check the 6.6 million CFPB complaint figure.

Sources:
- [e-OSCAR API license and third-party addendum](https://www.e-oscar.org/services-by-e-oscar)
- [e-OSCAR getting started ($90 registration)](https://www.e-oscar.org/gettingstarted)
- [e-OSCAR vendor management](https://www.e-oscar.org/vendor-management)
- [Provana Sonnet dispute solution](https://provana.com/provanas-end-to-end-dispute-management-solution/)
- [Provana acquires Palinode](https://www.businesswire.com/news/home/20250205372163/en/Provana-Acquires-Palinode-Further-Strengthening-Dispute-Solutions-for-Financial-Institutions)
- [Nortridge integrates Sonnet](https://nortridge.com/press-releases/nortridge-software-launches-integration-of-sonnet-by-palinode-to-provide-lenders-with-tool-to-remain-compliant-amidst-credit-report-disputes/)
- [DAKCS and Palinode partner on e-OSCAR disputes](https://www.insidearm.com/news/00045319-dakcs-software-systems-inc-and-palinode-j/)
- [Bridgeforce on e-OSCAR](https://bridgeforcedatasolutions.com/what-is-e-oscar/)
- [WebRecon collection agency products](https://webrecon.com/solutions/collection-agencies)
- [Hinkle v. Midland (CourtListener)](https://www.courtlistener.com/opinion/4237224/teri-lynn-hinkle-v-midland-credit-management-inc/)
- [insideARM on Hinkle](https://www.insidearm.com/news/00041954-11th-cir-holds-fcra-reasonable-investigat/)
- [CDIA FCRA Certificate for Data Furnishers](https://www.cdiaonline.org/certificate-program-for-data-furnishers/)
- [CDIA Metro 2 e-learning](https://www.cdiaonline.org/metro-2-e-learning-system/)
- [RMAI certification program](https://rmaintl.org/certification-education/)
- [RMAI events](https://rmaintl.org/events/)
- [SOC 2 Type I timeline and cost](https://www.complyjet.com/blog/soc-2-for-startups)
- [Vanta: SOC 2 for startups](https://www.vanta.com/collection/soc-2/soc-2-for-startups)
- [FTI Consulting on automated dispute handling (AFSA)](https://afsaonline.org/2023/01/16/how-automated-credit-dispute-handling-can-reduce-costs-by-90/)
- [July 2026 FCRA litigation update](https://www.shipkevich.com/july-2026-litigation-update-fcra-filings-continue-to-climb-as-other-consumer-litigation-pulls-back-ytd-figures-still-high/)
