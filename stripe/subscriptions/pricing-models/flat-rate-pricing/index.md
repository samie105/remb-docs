---
title: "Set up flat rate pricing"
source: "https://docs.stripe.com/subscriptions/pricing-models/flat-rate-pricing"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:19:25.512Z"
content_hash: "7c4dafaf9da2e00f406e8410e2f4fe35bf183dc396cf1bf5dd3088dfaf32feef"
---

## Set up flat rate pricing for your subscriptions.

SaaS businesses often offer their customers a choice of escalating service options. Customers choose a service tier and pay a flat rate for it. For example, imagine a business called [Typographic](https://typographic.io/) that sells a subscription webfont service. They offer three different service levels: Basic, Starter, and Enterprise. They offer a monthly and yearly price for each service level.

![](https://b.stripecdn.com/docs-statics-srv/assets/pricing_model-flat-rate.e99989aa8c2abe76edd607462840776e.png)

Flat-rate pricing model

In this example, Typographic has three products: `Basic`, `Starter`, and `Enterprise`. Each product has several different prices. The basic level has prices for 10 GBP per month and 100 GBP per year. Both prices are for the same `Basic` product, so they share the same product description on the customer’s receipt and invoice.

* * *

First, create the `Basic` product. To learn about all the options for creating a product, see the [prices guide](https://docs.stripe.com/products-prices/manage-prices#create-product).

1.  Go to [Product catalog](https://dashboard.stripe.com/products).
2.  Click **\+ Create product**.
3.  Enter a **Name** for the product.
4.  (Optional) Add a **Description**. The description appears at checkout, on the [customer portal](https://docs.stripe.com/customer-management), and in [quotes](https://docs.stripe.com/quotes).

Next, create the monthly price for the `Basic` product:

1.  Click **More pricing options**.
2.  Select **Recurring**.
3.  For **Choose your pricing model**, select **Flat rate**.
4.  For **Amount**, enter a price amount.
5.  For **Billing period**, select **Monthly**.
6.  Click **Next** to save the price.

Then, create the yearly price for the `Basic` product:

1.  Click **\+ Add another price**.
2.  Select **Recurring**.
3.  For **Choose your pricing model**, select **Flat rate**.
4.  For **Amount**, enter a price amount.
5.  For **Billing period**, select **Yearly**.
6.  Click **Next**.
7.  Click **Add product** to save the product and price. You can only edit the product and price until you create a subscription with them.
