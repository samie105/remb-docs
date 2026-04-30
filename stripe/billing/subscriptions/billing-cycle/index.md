---
title: "Set the subscription billing renewal date"
source: "https://docs.stripe.com/billing/subscriptions/billing-cycle"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:14:26.130Z"
content_hash: "e1b8146e2f0244d7e11e04a0aae45c1f65328a73670f981059f862ee76ed3abc"
---

A subscription’s billing period depends on two factors:

*   The recurring interval of its [price](https://docs.stripe.com/products-prices/overview) or prices, such as monthly, yearly, weekly, and so on.
*   The [billing cycle anchor](https://docs.stripe.com/api/subscriptions/object#subscription_object-billing_cycle_anchor) is the reference point that aligns future billing period dates. It sets the day of week for `week` intervals, the day of month for `month` and `year` intervals, and the month of year for `year` intervals. The default value is either the subscription creation date or the trial end date (if you’re using a trial period). You can also explicitly set this value at the time you create the subscription.

#### Note

Billing cycle anchors are UNIX timestamps in seconds from the current epoch.

The following are examples of monthly subscriptions with different billing periods:

*   A monthly subscription with a billing cycle anchor date of September 2 always bills on the 2nd day of the month.
*   A monthly subscription with a billing cycle anchor date of January 31 bills the last day of the month closest to the anchor date, so February 28 (or February 29 in a leap year), then March 31, April 30, and so on.
*   A weekly subscription with a billing cycle anchor date of Friday, June 3 bills every Friday thereafter.

Full billing periods start on the first full [invoice](https://docs.stripe.com/api/invoices) date, which is often the same as the billing cycle anchor and is always interval-aligned with it.

## Specify the billing cycle anchor for new subscriptions

There are two ways to set the billing cycle anchor on new subscriptions:

*   Use `billing_cycle_anchor_config` to calculate the timestamp for you (monthly or yearly subscriptions only).
*   Use `billing_cycle_anchor` to accept the timestamp directly.

If you’re creating a monthly or yearly subscription, we recommend using the `billing_cycle_anchor_config` parameter because it automatically factors in short months and leap years for you. If you’re creating a daily or weekly subscription, or if you prefer to set the renewal date of your subscription using a timestamp, use the `billing_cycle_anchor` parameter directly.

### Use billing\_cycle\_anchor\_config

To create an integration with monthly and yearly subscriptions, use `billing_cycle_anchor_config` on [create subscription](https://docs.stripe.com/api#create_subscription) to specify the day of the month on which to anchor.

Set `day_of_month` to `31` to create a monthly subscription that renews at the end of the month, even in months with less than 31 days. If a month has less than 31 days, the subscription renews on the last day of that month.

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -d "customer=  {{CUSTOMER_ID}}  " \   -d "items[0][price]=  {{PRICE_ID}}  " \   -d "billing_cycle_anchor_config[day_of_month]=31"`

You can also specify `month` to control the month of year for the anchor on multi-month and yearly subscriptions.

To cycle your yearly subscriptions on the first of July, create a yearly subscription with a `month` of `7` and `day_of_month` of `1`.

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -d "customer=  {{CUSTOMER_ID}}  " \   -d "items[0][price]=  {{PRICE_ID}}  " \   -d "billing_cycle_anchor_config[month]=7" \   -d "billing_cycle_anchor_config[day_of_month]=1"`

You can specify the exact month, day, hour, minute, and second for the billing cycle anchor by using `billing_cycle_anchor_config`. If you don’t specify the hour, minute, and second, they default to the values of the subscription creation time.

The billing cycle anchor uses Coordinated Universal Time (UTC). For example, if you create a subscription using `billing_cycle_anchor_config` at 5 PM EST without specifying the hour, the time is recorded in the system as 10 PM UTC.

`billing_cycle_anchor_config` doesn’t support anchoring on a backdated start date.

For example, if you have an existing monthly subscription with a `billing_cycle_anchor` timestamp that contains the day of the month, hour, minute, and second of 15, 12, 30, and 0, you can align a new monthly subscription with it. To do this, set `day_of_month`, `hour`, `minute`, and `second` to match those same values, respectively.

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -d "customer=  {{CUSTOMER_ID}}  " \   -d "items[0][price]=  {{PRICE_ID}}  " \   -d "billing_cycle_anchor_config[day_of_month]=15" \   -d "billing_cycle_anchor_config[hour]=12" \   -d "billing_cycle_anchor_config[minute]=30" \   -d "billing_cycle_anchor_config[second]=0"`

If you use `billing_cycle_anchor_config`, it might result in a `billing_cycle_anchor` that’s more than one billing period in the future. However, the date for the first full invoice always falls within one billing period from the creation of the subscription or the ending of a free trial.

For example, assume that you create a two-month interval subscription in February and you cycle it at the end of every month by setting `day_of_month` to `31`. The next month that has 31 days on two-month intervals from February is August, which results in a billing cycle anchor on August 31. However, the first full invoice date for this subscription still occurs in February. There’s an initial, prorated period from subscription creation until February 28 (or 29 during a leap year), followed by a full two-month billing period.

### Use billing\_cycle\_anchor

You can create a subscription with an explicit billing cycle anchor using the Subscriptions API or Checkout.

Call [create subscription](https://docs.stripe.com/api#create_subscription), setting a timestamp for `billing_cycle_anchor`.

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -d "customer_account=  {{CUSTOMER_ACCOUNT_ID}}  " \   -d "items[0][price]=  {{PRICE_ID}}  " \   -d billing_cycle_anchor=1611008505`

### Configure proration behavior

Regardless of which API parameter you use, Stripe automatically creates a prorated invoice to bill for the period between the subscription creation date and the first full invoice date.

If you don’t want to immediately charge a customer for the period between the subscription creation and the first full invoice date, either:

*   [Disable the proration](https://docs.stripe.com/billing/subscriptions/prorations#disable-prorations) by setting `proration_behavior` to `none`, making the initial period up to the first full invoice date free. This action doesn’t generate an invoice at all until the first billing period.
*   [Combine a trial with the billing\_cycle\_anchor](https://docs.stripe.com/billing/subscriptions/trials/free-trials#combine-trial-anchor) by setting `trial_end` to a timestamp representing the date when the free trial ends. Depending on the duration of the free trial and the number of days until the first full invoice date, this option might result in a prorated invoice following the trial period. For example, a free trial is 7 days and the billing renewal is monthly on the 1st. If the customer subscribes on the 15th, we generate a prorated invoice on the 22nd for the period between the 22nd and the 1st, then invoice for the full amount on the 1st of each month thereafter. If a customer subscribes on the 28th, the free trial extends past the 1st, generating a prorated invoice until the next month.

## Change the billing period on existing subscriptions

Use the [Subscriptions API](https://docs.stripe.com/api/subscriptions/update) or [Dashboard](https://dashboard.stripe.com/subscriptions) to change the billing date of an existing subscription through one of the following options:

*   Reset the billing cycle anchor to the current time.
*   Add a [free trial](https://docs.stripe.com/billing/subscriptions/trials) to automatically set the anchor date to the end of the trial. Trials typically start when you create a subscription, but you can also apply them to existing subscriptions, allowing you to credit the customer for the days left in the previous cycle that they already paid.

Your billing cycle date changes in these scenarios. However, if you create or update a subscription with `billing_mode[type]=flexible`, the billing cycle anchor remains unchanged. Learn more about [configuring flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode) and its [limitations](https://docs.stripe.com/billing/subscriptions/billing-mode#limitations).

*   If all prices are zero-amount, adding one or more paid prices immediately resets the billing period. See the [change subscription prices guide](https://docs.stripe.com/billing/subscriptions/change-price#handle-zero-amount-prices-and-quantities) for more information.
*   The `billing_cycle_anchor` resets to the [cancel\_at](https://docs.stripe.com/api/subscriptions/object#subscription_object-cancel_at) date when creating a subscription with `cancel_at` set to a date before the subscription renews next, or modifying an existing `cancel_at` date on a subscription with a `billing_cycle_anchor` in the future of the new `cancel_at` date.
*   The `billing_cycle_anchor` resets to the current time when switching to a price with a different [recurring.interval](https://docs.stripe.com/api/prices/object#price_object-recurring).

### Reset the billing period to the current time

To reset the billing cycle anchor to the current time, make an update request with `billing_cycle_anchor` set to `now`. This sets the billing cycle anchor to the time of the update request. After you reset the billing cycle anchor, Stripe immediately sends an invoice. [Enable proration](https://docs.stripe.com/api/subscriptions/create#create_subscription-proration_behavior) to credit the customer for any days already paid in the previous period. Disabling proration might result in overcharging your customer.

Call [update the subscription](https://docs.stripe.com/api#update_subscription), setting `billing_cycle_anchor` to `now` and `proration_behavior` to `create_prorations` to prevent overcharging the customer for any days they already paid in the previous cycle.

`curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \  -u "`

`sk_test_REDACTED`

`:" \  -d billing_cycle_anchor=now \  -d proration_behavior=create_prorations`

### Change the billing period using a trial period

You can change the billing cycle anchor by using a [free trial](https://docs.stripe.com/billing/subscriptions/trials) to automatically set the billing cycle anchor date to the `trial_end` date.

For example, if a customer has an active subscription originally set to bill next on July 23, and on July 15 you introduce a trial period ending on August 1:

*   The customer receives a 0 USD invoice on July 15. They already paid through July 23 in the previous cycle, so the “free” period only applies to July 24 through July 31.
*   The customer isn’t billed on July 23.
*   The new cycle billed on August 1 is a full cycle at the normal rate, then again on the 1st of each month after that.

Optionally, you can prevent prorations when you update a subscription to start a trial by using `proration_behavior=none`. In most cases, if you’re using the trial period to change the billing period without issuing a prorated invoice, you disable proration because the length of the trial period accounts for the portion already paid from the previous billing period.

Call [update subscription](https://docs.stripe.com/api#update_subscription), setting `trial_end` to a Unix timestamp representing the end date for the trial and `proration_behavior` to `none`. Setting the `trial_end` sets the billing cycle anchor to the same date.

`curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \  -u "`

`sk_test_REDACTED`

`:" \  -d trial_end=1627801200 \  -d proration_behavior=none`

## Usage-based billing

With [usage-based billing](https://docs.stripe.com/products-prices/pricing-models), the price paid by the customer varies based on consumption during the billing period. When changing the billing period results in ending a subscription’s service period early, you charge the customer for the usage accrued during the shortened billing period.

### Thresholds

In addition to the regular cycle, you can configure subscriptions to bill whenever the amount due reaches a [threshold](https://docs.stripe.com/billing/subscriptions/usage-based/thresholds).

If you have a subscription configured to invoice this way, you can set it up to reset the subscription service period when it hits the threshold.
