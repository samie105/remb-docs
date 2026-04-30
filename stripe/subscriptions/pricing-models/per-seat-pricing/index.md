---
title: "Set up per-seat pricing"
source: "https://docs.stripe.com/subscriptions/pricing-models/per-seat-pricing"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:19:44.772Z"
content_hash: "0b493d420ee54a567e1f3638eb33dfed097016cfab859bec959de1802b5c1591"
---

## Set up per-seat pricing for your subscriptions.

Per-seat pricing is a linear pricing model where the number of seats (for example, software licenses) maps to the number of units (for example, users). For example, imagine a business called [Typographic](https://typographic.io/) that wants to offer a per-seat plan. Typographic’s customers pick how many seats they’ll use, and Typographic charges based on that amount. In this example, a customer chooses and pays for three seats, which represents access for three of their users.

![](https://b.stripecdn.com/docs-statics-srv/assets/pricing_model-per-seat.8ed5ad9243ad6ae1c38b072cbb4ce07a.png)

Per-seat pricing model

To model this scenario, Typographic creates a product with a flat-rate price where each unit represents a user. When Typographic creates a subscription for a customer, the customer specifies the number of users for that subscription.

First, create the `Per-seat` product. To learn about all the options for creating a product, see the [prices guide](https://docs.stripe.com/products-prices/manage-prices#create-product).

1.  Go to [Product catalog](https://dashboard.stripe.com/products).
2.  Click **\+ Create product**.
3.  Enter a **Name** for the product.
4.  (Optional) Add a **Description**. The description appears at checkout, on the [customer portal](https://docs.stripe.com/customer-management), and in [quotes](https://docs.stripe.com/quotes).

Next, create the monthly price for the product:

1.  Select **Recurring**.
2.  For **Amount**, enter a price amount.
3.  For **Billing period**, select **Monthly**.
4.  Click **Add product** to save the product and price. You can only edit the product and price until you create a subscription with them.

To create a subscription using that price:

1.  Go to the **Billing** > **Subscriptions** page.
2.  Click **\+ Create subscription**.
3.  Find or add a customer.
4.  Search for the product you created and select the price you want to use.
5.  (Optional) Select **Collect tax automatically** to use Stripe Tax.
6.  Click **Start subscription** to start it immediately. To schedule a subscription, switch to the classic editor, and click **Schedule subscription**. To learn more, see [Subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules?dashboard-or-api=dashboard#managing).
