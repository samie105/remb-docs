---
title: "Mixed interval subscriptions"
source: "https://docs.stripe.com/billing/subscriptions/mixed-interval"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:22:43.843Z"
content_hash: "a08c51aee00edfad21eef76901c14bfea9d42786e0c5e293e3e0ae9e253513f1"
---

You can include multiple [subscription](https://docs.stripe.com/billing/subscriptions/overview) items with different prices and billing periods on a single subscription and Stripe automatically handles invoice generation.

For example, if you offer a service with an annual [flat rate](https://docs.stripe.com/products-prices/pricing-models#flat-rate), plus a monthly [usage-based fee](https://docs.stripe.com/billing/subscriptions/usage-based), you can include both prices as items on the same subscription. Stripe generates a single, combined invoice when item-level billing periods align and separate invoices when billing periods diverge.

#### Note

Mixed interval subscriptions must use [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode). You must upgrade your API version to `2025-06-30.basil` or later to use flexible billing mode in the Dashboard and API.

## Create a mixed interval subscription

1.  Go to the [Subscriptions](https://dashboard.stripe.com/subscriptions) page in the Dashboard.
2.  Select **+Create Subscription**.
3.  Under **Billing and payment collection**, set **Billing mode** to **Flexible**.
4.  Add products that bill on different intervals, such as monthy and yearly billing periods. Learn how to manage [products and prices](https://docs.stripe.com/products-prices/manage-prices).
5.  Configure your **Subscription options**.
6.  Click **Create the subscription**.

## Add mixed interval items to an existing subscription

1.  Go to the [Subscriptions](https://dashboard.stripe.com/subscriptions) page in the Dashboard.
2.  Find the subscripton, click its overflow menu (), and click **Update Subscription**.
3.  Add products that bill on different intervals, such as monthy and yearly billing periods. Learn how to manage [products and prices](https://docs.stripe.com/products-prices/manage-prices).
4.  Click **Update Subscription**.

## Cancel a subscription

Canceling a mixed interval subscription or schedule cancels all the subscription items, regardless of their interval.

Subscriptions have a single behavior for [dunning](https://docs.stripe.com/billing/revenue-recovery/smart-retries). If all retries for a payment fail, even if the failing payment is for an invoice related to only one of the items on the subscription, Stripe cancels the entire subscription and marks it as unpaid or past due, depending on your configured dunning settings.

Learn more about [canceling or deleting subscriptions](https://docs.stripe.com/no-code/subscriptions#create-subscriptions).

## Billing periods for mixed interval subscriptions

Each subscription item has its own [current\_period\_start](https://docs.stripe.com/api/subscriptions/object#subscription_object-items-data-current_period_start) and [current\_period\_end](https://docs.stripe.com/api/subscriptions/object#subscription_object-items-data-current_period_end). [Subscription items](https://docs.stripe.com/api/subscription_items/object) track their respective billing periods directly instead of as a top-level shared billing period on the [subscription](https://docs.stripe.com/api/subscriptions/object) resource.

For example, a subscription created on January 1 with a monthly, bimonthly, and quarterly item has the following periods:

current\_period\_start

current\_period\_end

Monthly item

January 1

February 1

Bi-monthly item

January 1

March 1

Quarterly item

January 1

April 1

Subscription

January 1

February 1

After renewal on February 1 (`subscription.current_period_end`), the subscription’s current period adjusts to match the latest `current_period_start` and earliest `current_period_end` of all the items:

current\_period\_start

current\_period\_end

Monthly item

February 1

March 1

Bi-monthly item

January 1

March 1

Quarterly item

January 1

April 1

Subscription

February 1

March 1

After cycling a third time:

current\_period\_start

current\_period\_end

Monthly item

March 1

April 1

Bi-monthly item

March 1

May 1

Quarterly item

January 1

April 1

Subscription

March 1

April 1

### Free trial

The item-level billing period dates are affected by free trial end dates, similar to regular subscriptions. When the subscription has a future-dated [trial\_end](https://docs.stripe.com/api/subscriptions/object#subscription_object-trial_end), all the `current_period_end` dates (subscription and items) are set to the `trial_end` date.

### Pause at trial end and resume

You can configure a mixed interval subscription to pause at trial end when the payment method is missing through the [trial\_settings.end\_behavior.missing\_payment\_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-trial_settings-end_behavior-missing_payment_method) parameter as with regular subscriptions. You can [resume](https://docs.stripe.com/billing/subscriptions/trials/free-trials?how=api#resume-a-paused-subscription) paused subscriptions using [stripe.subscription.resume](https://docs.stripe.com/api/subscriptions/resume), as with regular subscriptions.

#### Note

When resuming a mixed interval subscription with `billing_cycle_anchor: 'unchanged'` and `proration_behavior: 'none'`, the debit proration for the partial period between the date of resumption and the end of the current billing period for each of the items aren’t generated or billed. See an example below:

For a mixed interval subscription with a monthly and a bimonthly item with

*   `billing_cycle_anchor` = January 1
*   `trial_end` = February 1
*   `trial_settings.end_behavior.missing_payment_method` = “pause”

This example assumes this subscription is paused on February 1 because of a missing payment method, and the subscription resumes on February 15 with `proration_behavior: 'none'`:

billing\_cycle\_anchor: ‘unchanged’

billing\_cycle\_anchor: ‘now’

Monthly item

Item current period: February 1–March 1

*   Not billing for this period, so no new invoice is created
*   Monthly item is next billed on March 1 for the period March 1–April 1

Item current period: February 15–March 15

*   Generates a new invoice, and bills for a monthly item from February 15–March 15

Bimonthly item

Item current period: February 1–April 1

*   Not billing for this period, so no new invoice is created
*   Bimonthly item is next billed on April 1 for the period April 1–June 1

Item current period: February 15–April 15

*   Generates a new invoice and bills for a monthly item from February 15–April 15

Subscription

*   billing\_cycle\_anchor: February 1
*   Subscription transitions to active immediately

*   Generate a subscription pending update for billing\_cycle\_anchor: February 15 (applied when resumed invoice is paid)
*   Subscription remains paused until resumption invoice is paid

### Interval alignment

In mixed interval subscriptions, every item’s price interval (the combination of `price.recurring.interval` and `price.recurring.interval_count`) must be a multiple of the shortest price interval in the subscription. Some price interval combinations aren’t supported for mixed interval subscriptions.

*   **Examples of supported interval combinations**:
    
    *   1 month, 3 months
    *   1 month, 1 year
    *   1 day, 1 week
    *   1 day, 3 months
    *   1 day, 2 years
    *   2 weeks, 4 weeks
    *   2 months, 4 months, 6 months
*   **Examples of unsupported interval combinations**:
    
    *   2 months, 3 months
    *   4 months, 6 months
    *   1 week, 1 month
    *   2 days, 1 week
    *   5 months, 1 year

## Limitations

Mixed interval subscriptions are subject to the following limitations:

*   The deprecated [cancel\_at\_period\_end](https://docs.stripe.com/api/subscriptions/update#update_subscription-cancel_at_period_end) can’t detect which subscription item’s `current_period_end` to use as the cancellation date, so defaults to `min_period_end`. Alternatively:
    *   Use the `cancel_at` parameter to cancel a subscription on a future date.
    *   Use the `min_period_end` or `max_period_end` helpers to determine which item’s end period triggers the subscription cancelation.
*   Mixed interval subscriptions can’t calculate total [iterations](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-phases-iterations) accurately. Use `duration` to specify the subscription schedule instead.
*   You can’t apply a retention coupon on mixed interval subscriptions through the customer portal.
*   You currently can’t create mixed interval subscriptions on [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions/create).
