---
title: "Set up usage-based pricing models"
source: "https://docs.stripe.com/subscriptions/pricing-models/usage-based-pricing"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:20:24.049Z"
content_hash: "9098b2ed5c73cad908dd180c3c1a9f851fdd3d84a8647fa2a28f8d549b381746"
---

Usage-based pricing enables you to charge based on a customer’s usage of your product or service. Usage-based pricing includes models such as:

*   [Fixed fee and overage](#fixed-fee-overage)
*   [Pay as you go](#pay-as-you-go)
*   [Credit burndown](#credit-burndown)

## Fixed fee and overage

Use the fixed fee and overage model to charge a flat rate per month for your service at the beginning of the period. The flat rate has some included usage entitlement, and any additional usage (overage) charges at the end of the period.

You can use the Stripe Dashboard or API to set this up with two prices within the same product. For example, imagine an AI business called Hypernian introduces an advanced model called Hypernian Pro. Priced at 200 GBP per month, this model includes 100,000 tokens. They charge any usage above the included tokens at an additional rate of 0.001 GBP per token.

1.  On the [Product catalog](https://dashboard.stripe.com/test/products) page, click **Create product**.
    
2.  On the **Add a product** page, do the following:
    
    *   For **Name**, enter the name of your product. For the Hypernian example, enter “Hypernian.”
    *   (Optional) For **Description**, add a description that appears at checkout in the [customer portal](https://docs.stripe.com/customer-management) and in [quotes](https://docs.stripe.com/quotes).
    *   Under **Billing period**, select **More pricing options**.
3.  On the **Add price** page, do the following:
    
    *   Under **Choose your pricing model**, select **Flat rate**.
    *   Under **Price**, set the **Amount** to 200 GBP.
    *   Click **Next**
4.  To add a second recurring price to the product, click **Add another price** on the **Add a product** page.
    
5.  On the **Add price** page, do the following:
    
    *   Under **Choose your pricing model**, select **Usage-based**, **Per tier**, and **Graduated**.
        
    *   Under **Price**, create two graduated pricing tiers:
        
        First unit
        
        Last unit
        
        Per unit
        
        Flat rate
        
        **First tier**
        
        0
        
        100,000
        
        0 GBP
        
        0 GBP
        
        **Second tier**
        
        100,001
        
        ∞
        
        0.001 GBP
        
        0 GBP
        
6.  Under **Meter**, create a new meter to record usage. For the Hypernian example, use the meter name “hypernian\_api\_tokens.”
    
7.  Click **Next**.
    
8.  Click **Add product**. When you create subscriptions, specify both prices.
    

## Pay as you go

The pay as you go model (also called “in arrears billing”) lets you track usage incurred over a determined period, then charge the customer at the end of the period.

You can use any of the following pricing strategies:

*   **Per unit**: Charge the same amount for each unit.
*   **Per package**: Charge an amount for a package or bundle of units or usage.
*   **Volume-based pricing**: Charge the subscription item at the tier that corresponds to the usage amount at the end of the period.
*   **Graduated pricing**: Charge for the usage in each tier instead of applying a single price to all usage.

This model might cause customers to accumulate significant usage, and affect their payment method status at the end of the month.

## Credit burndown

The credit burndown model lets you collect prepayment for usage-based products and services. Customers can use [billing credits](https://docs.stripe.com/billing/subscriptions/usage-based/billing-credits) to pay an initial amount, and then apply their billing credits as they use the product.

For example, Hypernian wants to sell a large enterprise contract to an existing self-serve customer for their new Hypernian Model. The customer commits to pay 100000 GBP up front for Hypernian, so they can get 120000 GBP of billing credit usage to use within 1 year.

#### Collect prepayment from a customer

1.  On the [Invoices](https://dashboard.stripe.com/invoices) page, click **Create invoice**.
2.  Select your customer from the **Customer** dropdown.
3.  Select the correct currency from the **Currency** dropdown.
4.  Under **Items**, select **Add a new line item**.
5.  Under **Item details**, do the following:
    *   For **Item**, enter “Hypernian Credits.”
    *   For **Price**, enter “100,000.”
    *   Click **Save**.
6.  Click **Send invoice**.

After your customer pays the invoice, you can grant them billing credits.

#### Grant billing credits to a customer

1.  On the [Customers](https://dashboard.stripe.com/test/customers) page, select the customer name.
2.  On the customer page, under **Credit grants**, click the plus (**+**) symbol.
3.  On the **New credit grant** page, do the following:
    *   For **Name**, enter a name for your credit grant.
    *   For **Amount**, specify the amount of the credit grant. For the Hypernian example, enter “120,000.”
    *   Under **Expiry date**, specify the date, if any, when the credits expire. For the Hypernian example, select **Specific date** and set a date 12 months from now.
    *   Click **Create grant**.
