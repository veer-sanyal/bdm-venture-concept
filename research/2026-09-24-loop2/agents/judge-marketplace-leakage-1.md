**VERDICT: PASS.** The pain is real, but the money is too small. The chat tools marketplaces already pay for sit on the data this product needs, and the incentive idea is a one-time pricing change a marketplace can make on its own. I found no company pitching exactly this.

## Checking the concept's claims

- **Upwork quote: accurate.** The FY2022, FY2023 and FY2024 annual reports all say customers go around the marketplace to avoid fees and "it is difficult or impossible to measure the losses associated with circumvention." The report also says efforts to stop it "may be costly or counterproductive." I could not load the FY2025 report.
- **Airbnb 5.4%: true, but weaker than the pitch implies.**
  - It comes from a 2022 conference paper (ICIS 2022; Lin, Nian and Foutz), not a journal article.
  - It covers one city over one summer (Austin, 2019). The authors estimated it by matching bookings to phone location data.
  - Short-term rentals are not one of the target markets. The more useful finding is that Instant Book, which removes the back-and-forth messaging, cut off-platform deals by 9%.
- **Other research that matters here:**
  - **Trust cuts both ways.** A randomized trial on a freelance marketplace found that once the two sides trust each other enough, they leave more often (Gu & Zhu, 2021). That is exactly the loyal repeat pair this product targets.
  - **Messaging drives leakage.** When China blocked Skype, off-platform deals on a US freelance marketplace fell about 18% (Gu, 2024).
  - **The textbook fix is a pricing rule.** Charge more on early transactions and less on later ones (Enache & Rhodes, 2025). Once set, a pricing rule needs no ongoing software.
- **The loyal-pair discount already exists.** Upwork charged 20%, then 10%, then 5% as a freelancer's lifetime billings with a client grew, until 2023. Since May 2025 its fee (0% to over 15%) is again lower when a pair has more history together.

## Who already serves this customer

- **The chat tools already own the data and the purchase.** Stream, CometChat and Sendbird run the in-app messaging for most mid-sized marketplaces.
  - Stream's AI moderation flags attempts to move conversations off the platform and names Peerspace as a customer.
  - CometChat ships a "platform circumvention" rule and masks contact details; it published on this exact problem in July 2026.
  - Sendbird detects phone numbers and connects to Hive's AI moderation.
  - All three block rather than offer incentives. But marketplaces add these features to contracts they already have, and any outside vendor must get message history from them or from the marketplace.
- **Wholesale marketplaces have finance options.** Hokodo, Mondu and Resolve sell payment terms at checkout specifically as a reason for buyers to stay on the platform.
- **Many services marketplaces have avoided the problem.** Thumbtack and Angi charge sellers per lead instead of a commission, so there is little commission left to lose.

## 1. The strongest version

Drop "we spot at-risk chats in real time" as the product; the chat vendors already do the detection. Sell measurement and incentive testing for mid-sized commission marketplaces where money is held for a period and repeat pairs matter: B2B wholesale, and high-value services such as agencies and clinical staffing.

- **The paid audit is the product.** It measures which repeat pairs swapped contact details and then went quiet, and how much sales volume that represents. It also tells the marketplace what its pricing should be (fee by pair history, lower fees after the first job).
- **The ongoing part is the incentive plus a holdout group.** Offers the platform can fund, such as payment terms, escrow or insurance, are delivered as an add-on inside Stream, Sendbird or CometChat, with a holdout proving the effect. Pricing is a platform fee plus a share of recovered commission.

## 2. Ratings

| Criterion | Score | Evidence |
|---|---|---|
| Customer need | 3 | Upwork calls circumvention a material risk in every annual report, and blocking Skype alone moved leakage 18%. But much of the market chose per-lead or subscription models to sidestep it. |
| Value over what they use today | 2 | Detection is already built into their chat tools, and the loyal-pair discount is a fee setting Upwork runs itself. What is new is only the holdout measurement and nudges. |
| Market size | 2 | My rough estimate: a $100M marketplace at a 12% take rate losing 5% of sales, with 20% of that won back, recovers about $120K of commission. A 25% share of that is about $30K a year before discount costs. Even at a $1B marketplace, a few hundred customers only add up to tens of millions. |
| Risk (5 = low) | 2 | Marketplaces must hand over message histories (a privacy problem), the discount cuts fees on pairs who would have stayed anyway, and smaller marketplaces lack the volume to show a clear holdout result. Trust research says the leakers are the pairs that value the platform least. |

## 3. What kills it, and the fastest test

**What kills it:**
- The money a marketplace can recover is below about $100K a year of commission.
- Marketplaces will not share message data with an outside vendor.
- The best fix turns out to be a one-time pricing change, which makes this a consulting job, not a recurring software business.

**Fastest test (3 to 4 weeks):** offer the paid audit at $10–20K to 15 mid-sized wholesale or services marketplaces, ideally ones already on Stream or Sendbird. Kill it if either of these happens:
- Fewer than 3 pay and hand over exported message and transaction logs within 30 days.
- The completed audits show that pairs who swapped contacts and then stopped buying account for less than about 3% of sales volume.

That one test checks willingness to pay, data access and the size of the prize together.

Sources:
- [Upwork FY2024 10-K](https://www.sec.gov/Archives/edgar/data/1627475/000162747525000011/upwk-20241231.htm) and [FY2022 10-K](https://www.sec.gov/Archives/edgar/data/1627475/000162747523000010/upwk-20221231.htm)
- [Lin, Nian & Foutz, ICIS 2022 (Airbnb)](https://aisel.aisnet.org/icis2022/sharing_econ/sharing_econ/12/)
- [Gu & Zhu, Management Science 2021](https://pubsonline.informs.org/doi/10.1287/mnsc.2020.3583)
- [Gu, Management Science 2024](https://ideas.repec.org/a/inm/ormnsc/v70y2024i11p7868-7891.html)
- [Enache & Rhodes, Management Science 2025](https://pubsonline.informs.org/doi/10.1287/mnsc.2025.02150)
- [Upwork freelancer fee (Upwork Help)](https://support.upwork.com/hc/en-us/articles/211062538-Learn-about-the-Freelancer-Service-Fee) and [fee history summary](https://freelancercalculator.com/upwork-service-fee-2026-official-guide/)
- [CometChat: The Buyer-Seller Conversation Nobody Owns](https://www.cometchat.com/blog/the-buyer-seller-conversation-nobody-owns)
- [Stream marketplace moderation](https://getstream.io/blog/marketplace-content-moderation/) and [Stream Moderation](https://getstream.io/moderation/)
- [Sendbird Advanced Moderation](https://sendbird.com/docs/advanced-moderation/guide/v1/overview)
- [Hokodo on disintermediation](https://www.hokodo.co/resources/how-to-prevent-disintermediation-on-your-b2b-marketplace)
- [Thumbtack lead pricing](https://help.thumbtack.com/article/pay-for-leads)

VERDICT: PASS