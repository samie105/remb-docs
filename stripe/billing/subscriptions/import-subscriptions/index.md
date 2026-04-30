---
title: "Migrate subscriptions to Stripe Billing using Stripe APIs"
source: "https://docs.stripe.com/billing/subscriptions/import-subscriptions"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:21:23.437Z"
content_hash: "c7b916d9ffd6c1b81e4d2daef16bfd6f54c072eb7ea3d40f7d1fa4ba28d631a8"
---

After you import your customers and create a pricing model, you can start importing your subscriptions. You should be able to export subscription data from third-party systems through their UI or API. Contact your subscriptions processor if they don’t provide this option through either interface.

To import subscriptions, use your list of customers to create the appropriate subscription for each one. For example, if a subscriber has a monthly `Basic` pricing plan in your old model, use the monthly recurring price associated with that level when you create their subscription in Stripe.

### Make source data Stripe-compatible

Before you start importing subscriptions into Stripe, make sure that all of your source data is compatible with our expected format.

#### Important fields for migrating subscriptions

If you use relevant subscription data in your custom integration that Stripe doesn’t also use, you can apply your data to the `metadata` field of the subscriptions you create in Stripe. The following table describes other important fields to consider when importing subscriptions.

Field

Description

[customer](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-customer)

Make sure that you’ve properly mapped the customer ID from your source data to the new customer ID in Stripe.

[phases.items.price](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-phases-items-price)

Make sure that you’ve mapped the price ID from your source data to the new price ID in Stripe.

[current\_phase.start\_date](https://docs.stripe.com/api/subscription_schedules/object#subscription_schedule_object-current_phase-start_date)

Make sure that the subscription schedule you define in Stripe lines up with and maintains continuity from your original source data. For example, if a customer has 6 months left on a yearly subscription in your source system, make sure that `billing_cycle_anchor` and `start_date` reflect the correct mid-cycle term.

Third-party metadata

Import any additional data fields from your source data, which might include product names, plan names, and third-party application IDs.

Tax settings

Include any tax IDs, VAT IDs, or other tax information.

#### Prepare legacy prices

If you created placeholders for [legacy prices](#legacy-prices), you need to map those prices to the subscriptions and customers you’re importing. For each subscription with a legacy price, use the [price\_data](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data) parameter of the [Subscriptions](https://docs.stripe.com/api/subscriptions#subscriptions) API to pass in information about the price and subscription. The required fields are:

Parameter

Description

[currency](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data-currency)

Currency of the price, in three-letter ISO format.

[product](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data-product)

ID of the placeholder product. You can use this for all of the legacy prices.

[recurring](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data-recurring)

Information about the amount and frequency of the recurring price.

[recurring.interval](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data-recurring)

Frequency of the interval-`day`, `week`, `month`, or `year`.

[recurring.interval\_count](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data-recurring-interval_count)

Number of intervals between billings. For example, setting `interval=day` and `interval_count=30` means that you bill the customer every 30 days. The maximum interval is 1 year (1 year, 12 months, or 52 weeks).

[recurring.unit\_amount\_decimal](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data-unit_amount_decimal)

Same as [unit\_amount](https://docs.stripe.com/api/subscriptions/create#create_subscription-items-price_data-unit_amount), but allows you to specify more granular decimal amounts in cents, up to 12 decimals. You can only set one of `unit_amount` and `unit_amount_decimal`.

### Import subscription data into Stripe

After you’ve prepared your source data, you can start importing subscriptions into Stripe.

#### Testing

Use a [sandbox](https://docs.stripe.com/sandboxes) to run through the pricing model import process at least once before running the import in live mode. You need to remap your script:

*   If you wipe the data in a sandbox and rerun the import.
*   When you move to live mode, because the price IDs are different in a sandbox and live mode.

In a sandbox, you can use [test clocks](https://docs.stripe.com/billing/testing/test-clocks) to simulate subscriptions advancing through time. This allows you to see how the migrated subscriptions work in production.

#### Create subscriptions

While you can use the [Subscription](https://docs.stripe.com/api/subscriptions) API to create subscriptions, we recommend using the [Subscription Schedules](https://docs.stripe.com/api/subscription_schedules) API. With this API, you can schedule subscriptions to start in the future. For example, it’s the only way to start monthly subscriptions more than 30 days in advance. The ability to start subscriptions in the future also allows you to review the import before you start to bill your customers in production.

Additionally, the Subscription Schedules API provides `phases`, which provide much more flexibility in defining settings such as tax behavior, collection method, and coupon usage within more granular intervals. You can also define different behavior for different intervals. For example, you could apply a coupon only for the first 3 months of a yearly subscription.

Here’s how to create subscriptions that start on June 1, 2022 at 12:00 AM UTC.

`curl https://api.stripe.com/v1/subscription_schedules \  -u "`

`sk_test_REDACTED`

`:" \  -d "customer=  {{CUSTOMER_ID}}  " \   -d "default_settings[billing_cycle_anchor]=phase_start" \   -d "phases[0][items][0][price]=  {{PRICE_ID}}  " \   -d start_date=1654066801`
