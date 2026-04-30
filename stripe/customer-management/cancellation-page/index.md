---
title: "Add a cancellation page to the customer portal"
source: "https://docs.stripe.com/customer-management/cancellation-page"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:07:09.633Z"
content_hash: "fc2efc8b1e776e4c553f7b92e308e0aeecdc76fbd6be5a479f4fa1ef91fb1503"
---

## Allow your customers to cancel their subscriptions in the customer portal.

In the customer portal, you can let your customers cancel their subscriptions. This option is enabled by default.

You can also enable other options to:

*   [Collect a cancellation reason](#collect-cancellation-reason)
*   [Deflect cancellations](#cancellation-deflection)

Configure these options in the [customer portal settings](https://dashboard.stripe.com/settings/billing/portal) page of the Stripe Dashboard.

You can also create a [customized deep link workflow](https://docs.stripe.com/customer-management/portal-deep-links) for cancellations.

Cancellation at period end is handled differently in the customer portal depending on billing mode. [Learn how billing mode affects cancellations](https://docs.stripe.com/billing/subscriptions/billing-mode/compare#cancellations-in-the-customer-portal).

## Collect a cancellation reason

After a customer cancels their subscription, you can collect a reason for their cancellation. In the customer portal settings, you can select the reasons that your customers see from the following list.

*   It’s too expensive
*   I need more features
*   I found an alternative
*   I no longer need it
*   Customer service was less than expected
*   Ease of use was less than expected
*   Quality was less than expected
*   Other reason

If a customer selects **Other reason**, they can optionally enter additional free text.

### Finding cancellation reasons

You can find the cancellation reasons that users select in the following places:

*   **Billing** > **Subscriptions** > subscription details page
*   [Stripe Sigma](https://dashboard.stripe.com/sigma/queries)
    *   Learn how to [get started with Sigma](https://docs.stripe.com/stripe-data/how-sigma-works) and how to [use templates to query Billing data](https://docs.stripe.com/stripe-data/query-billing-data).
*   The `subscription.updated` webhook
    *   Learn more about [subscription webhook events](https://docs.stripe.com/billing/subscriptions/webhooks#events).

## Deflect cancellations in the customer portal

When a customer cancels their subscription in the customer portal, you can attempt to deflect the cancellation by offering a retention coupon.

To set up a retention coupon to deflect cancellations:

1.  Go to the **Settings** > **customer portal** [page](https://dashboard.stripe.com/settings/billing/portal).
2.  Expand the Cancellations section.
3.  Select a coupon in the drop-down under **Retention Coupon**.

If you don’t have a coupon already, you can build one inline. [Learn more about coupons](https://docs.stripe.com/billing/subscriptions/coupons).
