---
title: "Bill customers in advance"
source: "https://docs.stripe.com/billing/subscriptions/prebilling"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:24:44.347Z"
content_hash: "9a072c6b4e008311e697efdda97d2f7067076590c81427375537a7e6dca0abf3"
---

## Use prebilling to bill your customers now for future cycles or upcoming renewals.

With prebilling, you can bill customers in advance for multiple service periods, as opposed to the typical billing cycle for licensed prices, where you bill a customer for one service period. You can enable prebilling when you start a subscription or for upcoming renewals.

Here are some example use cases for prebilling:

*   Create a monthly subscription and prebill for the first 45 days.
*   When a monthly subscription has an upcoming renewal in 7 days, prebill and send the customer the renewal invoice now.
*   Prebill now for the next 2 months from the time of renewal.

You can use prebilling when you create or update a subscription. Prebilling applies at the item-level: you can prebill for a specific item, set of items, or all items on a subscription. You can adjust the time range for prebilling at the item level, but it must cover at least one service period. For example, if you prebill an item with a monthly price, you must prebill for at least one month.

## Limitations

During public preview, prebilling has the following limitations:

*   Prebilling isn’t available for [subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules), or subscriptions backed by a subscription schedule.
*   You can only use coupons with [percent\_off](https://docs.stripe.com/api/coupons/object#coupon_object-percent_off) and a [duration](https://docs.stripe.com/api/coupons/object#coupon_object-duration) of `once` or `forever` with prebilling.
*   Prebilling is applied immediately when you create or update a subscription and configure [billing\_schedules](https://docs.stripe.com/api/subscriptions/create?api-version=preview#create_subscription-billing_schedules).
*   You can’t use prebilling on subscriptions that have been [migrated from classic to flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode#migrate-existing-subscriptions-to-flexible-billing-mode).
*   You can’t enable prebilling if all the subscription items have usage-based prices. Prebilling doesn’t apply to any usage-based prices in a subscription. You can’t set [applies\_to\[price\]](https://docs.stripe.com/api/subscriptions/create?api-version=preview#create_subscription-billing_schedules-applies_to) if the price has [usage\_type=metered](https://docs.stripe.com/api/prices/object?api-version=preview#price_object-recurring-usage_type).
*   You must enable proration for subscriptions to use prebilling. You can’t set [proration\_behavior](https://docs.stripe.com/api/subscriptions/create?api-version=preview#create_subscription-proration_behavior) to `none`.
*   You can only enable prebilling up to the scheduled cancellation time if you update a subscription that’s been scheduled for cancellation.
*   You can’t use prebilling if [payment\_behavior](https://docs.stripe.com/api/subscriptions/create?api-version=preview#create_subscription-payment_behavior) is set to `pending_if_incomplete`.

## Before you begin

To use prebilling, you must:

*   Create subscriptions with flexible billing mode enabled. [Learn more about flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode).
*   Have an integration on Stripe API version [2025-09-30.preview](https://docs.stripe.com/changelog#2025-09-30.preview) or later. Learn how to [upgrade your API version](https://docs.stripe.com/upgrades#how-can-i-upgrade-my-api).

## Set up prebilling

You can enable prebilling when you create or update a subscription in the Dashboard or through the API.

When you set the end date for prebilling:

*   The end date can’t be sooner than the start of the shortest billing period on the subscription. For example, if the shortest billing period on the subscription is monthly, the end date for prebilling must be at least a month from the start of the billing period.
*   The end date can’t be later than the end of 12 cycles of the shortest billing period on the subscription. For example, if the shortest billing period on the subscription is monthly, the end date for prebilling can’t be more than 12 months from the start of the billing period.

To create a subscription with prebilling in the Dashboard:

1.  Go to the [Subscriptions page](https://dashboard.stripe.com/subscriptions?status=active).
2.  Click **\+ Create subscription**.
3.  In the **Subscription settings** section, enable **Bill upfront**.
4.  Select the end date for prebilling. All items in the subscription are prebilled until the date you select.
5.  In the **Advanced settings** section, set **Billing mode** to **Flexible**.
6.  Click **Create subscription**.

To update an existing subscription:

#### Note

The subscription must already be in `billing_mode=flexible` to enable prebilling. See the [Limitations](https://docs.stripe.com/billing/subscriptions/prebilling#limitations) for more details.

1.  Go to the [Subscriptions page](https://dashboard.stripe.com/subscriptions?status=active).
2.  Click the subscription to update, then select **Actions** > **Update subscription**.
3.  In the **Subscription settings** section, enable **Bill upfront**.
4.  Select the end date for prebilling. All items in the subscription are prebilled until the date you select.
5.  Click **Update subscription**.
