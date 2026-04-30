---
title: "Set up tiered pricing"
source: "https://docs.stripe.com/subscriptions/pricing-models/tiered-pricing"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:20:04.560Z"
content_hash: "0932723f9069dc5149d1f6509277837c27e066a557cadeb96c36936a0aefc52a"
---

Prices can represent tiers, allowing the unit cost to change with quantity or usage. Use tiers if you need non-linear pricing when `quantity` or [usage](https://docs.stripe.com/api/billing/meter-event) changes. To create [usage-based pricing models](https://docs.stripe.com/subscriptions/pricing-models/usage-based-pricing), you can combine tiered pricing with flat rates.

For example, imagine a business called [Typographic](https://typographic.io/) that wants to offer lower rates for customers who use more fonts per month. The following tiered pricing models show two different ways to adjust pricing as usage increases: [volume-based pricing](#volume-based-pricing) and [graduated pricing](#graduated-pricing). To demonstrate these approaches to tiered pricing, we’ll use the following tiers:

Number of fonts

Price per tier

**First tier**

1-5

7 GBP

**Second tier**

6-10

6.5 GBP

**Third tier**

11+

6 GBP

## Volume-based pricing

With volume-based pricing, the subscription item bills at the tier corresponding to the amount of usage at the end of the period. The entire `quantity` (or `usage`) is multiplied by the unit cost of the tier. Because the tier price applies to the entire `quantity` (or `usage`), the total might decrease when calculating the final cost.

For example, a customer with 5 fonts is charged 35 GBP (5 × 7 GBP) in November. If they use 6 fonts in December, then Typographic bills all fonts at the `6-10` rate. For December, Typographic charges 39 GBP (6 × 6.5 GBP).

Quantity and usage at end of the period

Unit cost

Total monthly cost

1

7 GBP

7 GBP

5

7 GBP

35 GBP

6

6.5 GBP

39 GBP

20

6 GBP

120 GBP

25

6 GBP

150 GBP

1.  Go to the [Product catalog](https://dashboard.stripe.com/products).
2.  Click **\+ Create product**.
3.  Enter a **Name** for the product.
4.  (Optional) Add a **Description**. The description appears at checkout, on the [customer portal](https://docs.stripe.com/customer-management), and in [quotes](https://docs.stripe.com/quotes).

Next, create the monthly price for the product:

1.  Click **More pricing options**.
2.  Select **Recurring**.
3.  For **Choose your pricing model**, select **Tiered pricing** and **Volume**.
4.  Under **Price**, create three tiers:
    
    First unit
    
    Last unit
    
    Per unit
    
    Flat rate
    
    First tier
    
    1
    
    5
    
    7 GBP
    
    0 GBP
    
    Second tier
    
    6
    
    10
    
    6.5 GBP
    
    0 GBP
    
    Third tier
    
    11
    
    ∞
    
    6 GBP
    
    0 GBP
    
5.  For **Billing period**, select **Monthly**.
6.  Click **Add product** to save the product and price. You can only edit the product and price until you create a subscription with them.

## Graduated pricing

Graduated pricing charges for the usage in each tier instead of applying a single price for overall usage. The `quantity` is multiplied by the amount for each tier and the totals for each tier are summed together.

For example, 5 fonts result in the same charge as volume-based pricing: 35 GBP total at 7 GBP per font. This changes as usage exceeds the first tier. Typographic charges a customer with more than 5 fonts 7 GBP per font for the first 5 fonts, then 6.5 GBP for fonts 6 through 10, and 6 GBP for any additional fonts. They charge a customer with 6 fonts 41.5 GBP, 35 GBP for the first 5 fonts and 6.5 GBP for the 6th font.

Quantity and usage at end of the period

Total for graduated tiered pricing

1

7 GBP

5

35 GBP

6

41.5 GBP

20

127.5 GBP

25

157.5 GBP

1.  Go to the [Product catalog](https://dashboard.stripe.com/products).
2.  Click **\+ Create product**.
3.  Enter a **Name** for the product.
4.  (Optional) Add a **Description**. The description appears at checkout, on the [customer portal](https://docs.stripe.com/customer-management), and in [quotes](https://docs.stripe.com/quotes).

Next, create the monthly price for the product:

1.  Click **More pricing options**.
2.  Select **Recurring**.
3.  For **Choose your pricing model**, select **Tiered pricing** and **Graduated**.
4.  Under **Price**, create three tiers:
    
    First unit
    
    Last unit
    
    Per unit
    
    Flat rate
    
    First tier
    
    1
    
    5
    
    7 GBP
    
    0 GBP
    
    Second tier
    
    6
    
    10
    
    6.5 GBP
    
    0 GBP
    
    Third tier
    
    11
    
    ∞
    
    6 GBP
    
    0 GBP
    
5.  For the **Billing period**, select **Monthly**.
6.  Click **Add product** to save the product and price. You can only edit the product and price until you create a subscription with them.

## Add a flat rate

You can specify a flat rate (`flat_amount`) to add to the [invoice](https://docs.stripe.com/api/invoices). This works for both volume and graduated pricing. For example, you can have a flat fee that increases when your customer exceeds certain usage thresholds:

Tier

Amount (unit cost)

Flat rate

1-5 (`up_to=5`)

5 GBP (`unit_amount=500`)

10 GBP (`flat_amount=1000`)

6-10 (`up_to=10`)

4 GBP (`unit_amount=400`)

20 GBP (`flat_amount=2000`)

10-15 (`up_to=15`)

3 GBP (`unit_amount=300`)

30 GBP (`flat_amount=3000`)

15-20 (`up_to=20`)

2 GBP (`unit_amount=200`)

40 GBP (`flat_amount=4000`)

20+ (`up_to=inf`)

1 GBP (`unit_amount=100`)

50 GBP (`flat_amount=5000`)

#### Volume-based pricing flat rate example

If `quantity` is `12` and `tiers_mode=volume`, the total amount billed is:

12 × 3 GBP + 30 GBP = 66 GBP

#### Graduated pricing flat rate example

If `quantity` is `12` and `tiers_mode=graduated`, the total amount billed is:

(5 × 5 GBP + 10 GBP) + (5 × 4 GBP + 20 GBP) + (2 × 3 GBP + 30 GBP) = 111 GBP

A tier can have either a `unit_amount` or a `flat_amount`, or both, but it must have at least one of the two. If `quantity` is `0`, the total amount is 10 GBP regardless of the tiered pricing model used. Stripe always bills the first flat rate tier when `quantity=0`. To bill `0` when there’s no usage, set up an `up_to=1` tier with an `unit_amount` equal to the flat rate and omit the `flat_amount`.
