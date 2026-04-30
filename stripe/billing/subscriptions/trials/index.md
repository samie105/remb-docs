---
title: "Configure trial offers on subscriptions"
source: "https://docs.stripe.com/billing/subscriptions/trials"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:23:05.592Z"
content_hash: "96c8d5aff6338c6d94e60f925b5857f37b153399e32bafb314fecc8f9d23a501"
---

![](https://b.stripecdn.com/docs-statics-srv/assets/trial-offer.2128af954f90482fce40e29d1604a01b.png)

Use the [Trial Offer](https://docs.stripe.com/api/product-catalog/trial-offer?api-version=2026-03-25.preview) API to manage both free and paid introductory periods for your [subscriptions](https://docs.stripe.com/subscriptions) with a single API integration. Trial offers enable you to qualify high-intent leads, reduce trial abuse, and provide discounted rates to your customers for a limited duration (for example, 1 GBP for the first week of an offer).

## Use cases

With trial offers, you can run promotional pricing and product offering experiments directly in Stripe. Common use cases for trial offers include:

Use case

Description

**Discounted trials**

To improve trial-to-paid conversion and generate revenue, you can set up discounted trials. For example, you offer a reduced introductory price of 4 GBP for 4 weeks or a free 7-day trial.

**Free trials**

To offer a free trial subscription, include a 0 GBP item in the subscription.

**Upgrade trials**

To upsell premium features, you can configure upgrade trials. For example, you offer a customer on a basic plan a 7-day trial to access premium features at the basic rate. Then, when the trial ends, you automatically convert them to the premium rate.

**Item-level trials**

To sell add-ons, AI packs, and other feature bundles, you can set up item-level trials. You can offer customers a trial for a single line item in a subscription while billing other items at their regular price.

## Before you begin

*   Your integration must be on [2026-03-25.preview](https://docs.stripe.com/changelog?channel=preview#2026-03-25.preview). You must specify that [Stripe version](https://docs.stripe.com/api/versioning) in your request header to access preview features.
*   You must upgrade your subscription from `classic` [billing mode](https://docs.stripe.com/api/subscriptions/create#create_subscription-billing_mode) to [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode) to use trial offers.

### Limitations

*   Trial offers apply to recurring subscription items only. Non-recurring items aren’t eligible for paid trials or discounted trial pricing.
*   Dashboard and customer portal support is limited during public preview. You can use both the dashboard and customer portal to view trial offers created using the API, but you can’t use them to create, manage, or modify trial offer items.
*   You can’t modify the trial length after you create the subscription or schedule trial extensions and reductions.
*   [Trial Offer API](https://docs.stripe.com/api/product-catalog/trial-offer?api-version=2026-03-25.preview) and [trial\_end](https://docs.stripe.com/api/subscriptions/update#update_subscription-trial_end) limitations:
    *   You can’t use trial offers and the legacy `trial_end` parameter together. We recommend using the Trial Offer API to configure discounted trials and free trials.
    *   If you use [Checkout](https://docs.stripe.com/payments/checkout), you can’t use trial offers. To create trialing subscriptions through Checkout, you must use legacy free trials with `trial_end`. See [Configure free trials](https://docs.stripe.com/payments/checkout/free-trials).

## How trial offers work

[Products](https://docs.stripe.com/api/products) describe the specific goods or services you offer to your customers and [Prices](https://docs.stripe.com/api/prices) define the unit cost. A subscription charges a customer for those products, at the specified price, on a recurring basis. When you create a trial offer, you specify a trial price and a duration of the trial for a product. When the trial ends, the subscription automatically transitions to the regular price or another price you configure.

Trial offers don’t replace [products or prices](https://docs.stripe.com/products-prices/how-products-and-prices-work). `Trial Offer` is a separate object that attaches a discounted or free price to a [Subscription item](https://docs.stripe.com/api/subscription_items) for a limited time, without modifying the item’s underlying [price](https://docs.stripe.com/api/subscription_items/object?#subscription_item_object-price).

## Create a trial offer

To [create a trial offer](https://docs.stripe.com/api/product-catalog/trial-offer/create?api-version=2026-03-25.preview), pass a [price](https://docs.stripe.com/api/product-catalog/trial-offer/create?api-version=2026-03-25.preview#create_product_catalog_trial_offer-price) using the [price.id](https://docs.stripe.com/api/prices/object#price_object-id) to define the cost during the trial period. You can set this to 0 GBP for free trials or any positive amount for paid trials. Next, set the trial [duration.type](https://docs.stripe.com/api/product-catalog/trial-offer/create?api-version=2026-03-25.preview#create_product_catalog_trial_offer-duration-type) to `relative` (based on billing intervals) or `timestamp` (based on an absolute date). For relative duration, use [iterations](https://docs.stripe.com/api/product-catalog/trial-offer/object?api-version=2026-03-25.preview#product_catalog_trial_offer_object-duration-relative-iterations) to define the number of billing intervals. Then, define what happens when the trial ends using the [end\_behavior](https://docs.stripe.com/api/product-catalog/trial-offer/create?api-version=2026-03-25.preview#create_product_catalog_trial_offer-end_behavior). Use `transition` to specify the [price.id](https://docs.stripe.com/api/prices/object#price_object-id) that the subscription transitions to when the trial ends.

### Create a trial offer with a relative duration

`curl https://api.stripe.com/v1/product_catalog/trial_offers \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "price=  {{PRICE_ID}}  " \   -d "duration[relative][iterations]=1" \   -d "duration[type]=relative" \   -d "end_behavior[transition][price]=  {{PRICE_ID}}  "`

### Create a trial offer with a timestamp duration

`curl https://api.stripe.com/v1/product_catalog/trial_offers \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "price=  {{PRICE_ID}}  " \   -d "duration[type]=timestamp" \   -d "end_behavior[transition][price]=  {{PRICE_ID}}  "`

## Attach a trial offer to a new subscription

To attach a trial offer to a [subscription](https://docs.stripe.com/api/subscriptions/object), specify the [trial\_offer.id](https://docs.stripe.com/api/product-catalog/trial-offer/object?api-version=2026-03-25.preview#product_catalog_trial_offer_object-id) in the [items.current\_trial.trial\_offer](https://docs.stripe.com/api/subscriptions/update#update_subscription-items-current_trial) parameter:

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "customer_account=  {{CUSTOMER_ACCOUNT_ID}}  " \   -d "billing_mode[type]=flexible" \   -d "items[0][current_trial][trial_offer]=to_123" \   -d "items[0][quantity]=1"`

## Update subscriptions with a trial offer

### Add a trial offer to an existing subscription

To add a trial offer to an existing subscription, specify the [trial\_offer.id](https://docs.stripe.com/api/product-catalog/trial-offer/object?api-version=2026-03-25.preview#product_catalog_trial_offer_object-id) in the [items.current\_trial.trial\_offer](https://docs.stripe.com/api/subscriptions/update#update_subscription-items-current_trial) parameter:

`curl https://api.stripe.com/v1/subscriptions/`

`{{SUBSCRIPTION_ID}}`

 `\  -u "  sk_test_REDACTED  :" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "items[0][current_trial][trial_offer]=to_123"`

### Add a trial offer to a subscription with existing items

To add a trial offer as another item to a subscription that has existing items, add an item to the [items](https://docs.stripe.com/api/subscriptions/update#update_subscription-items) array and specify the [trial\_offer.id](https://docs.stripe.com/api/product-catalog/trial-offer/object?api-version=2026-03-25.preview#product_catalog_trial_offer_object-id) in the [items.current\_trial.trial\_offer](https://docs.stripe.com/api/subscriptions/update#update_subscription-items-current_trial) parameter:

`curl https://api.stripe.com/v1/subscriptions/`

`{{SUBSCRIPTION_ID}}`

 `\  -u "  sk_test_REDACTED  :" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "items[0][id]=  {{SUBSCRIPTION_ITEM_ID}}  " \   -d "items[1][current_trial][trial_offer]=to_123" \   -d "items[1][quantity]=1"`

### Convert a subscription item to a trial offer

To convert an existing subscription item to a trial offer, include the [items.id](https://docs.stripe.com/api/subscriptions/update#update_subscription-items-id) and specify the [trial\_offer.id](https://docs.stripe.com/api/product-catalog/trial-offer/object?api-version=2026-03-25.preview#product_catalog_trial_offer_object-id) in the [items.current\_trial.trial\_offer](https://docs.stripe.com/api/subscriptions/update#update_subscription-items-current_trial) parameter:

`curl https://api.stripe.com/v1/subscriptions/`

`{{SUBSCRIPTION_ID}}`

 `\  -u "  sk_test_REDACTED  :" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "items[0][id]=  {{SUBSCRIPTION_ITEM_ID}}  " \   -d "items[0][current_trial][trial_offer]=to_123"`

### Change the item quantity for a trial offer

To modify the item [quantity](https://docs.stripe.com/api/subscriptions/update#update_subscription-items-quantity) for a trial offer, update the subscription:

`curl https://api.stripe.com/v1/subscriptions/`

`{{SUBSCRIPTION_ID}}`

 `\  -u "  sk_test_REDACTED  :" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "items[0][id]=  {{SUBSCRIPTION_ITEM_ID}}  " \   -d "items[0][quantity]=2"`

## Add a trial offer to a subscription schedule

You can only use timestamp trial offers with [subscription schedules](https://docs.stripe.com/api/subscription_schedules). Unlike relative duration trials, which end after a set number of billing intervals, timestamp trials end on an absolute date. To create one, set the trial offer’s [duration.type](https://docs.stripe.com/api/product-catalog/trial-offer/object?api-version=2026-03-25.preview#product_catalog_trial_offer_object-duration-type) to `timestamp`:

`curl https://api.stripe.com/v1/product_catalog/trial_offers \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "price=  {{PRICE_ID}}  " \   -d "duration[type]=timestamp" \   -d "end_behavior[transition][price]=  {{PRICE_ID}}  "`

Next, use [phases.items.trial\_offer](https://docs.stripe.com/api/subscription_schedules/create?api-version=2026-03-25.preview#create_subscription_schedule-phases-items-trial_offer) to attach the trial offer to the schedule [phase](https://docs.stripe.com/api/subscription_schedules/create?#create_subscription_schedule-phases) of the subscription schedule:

`curl https://api.stripe.com/v1/subscription_schedules \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "customer_account=  {{CUSTOMER_ACCOUNT_ID}}  " \   -d start_date=1610403705 \  -d "phases[0][items][0][trial_offer]=to_123" \   -d "phases[0][end_date]=1610403706"`

## View subscriptions with trial offers

When you [retrieve a subscription](https://docs.stripe.com/api/subscriptions/retrieve), the response includes the configuration for each item, including trial offers:

`curl https://api.stripe.com/v1/subscriptions/`

`{{SUBSCRIPTION_ID}}`

 `\  -u "  sk_test_REDACTED  :" \  -H "Stripe-Version: 2026-03-25.preview"`

## Cancel a subscription at the end of a paid trial

To cancel the subscription when the paid trial ends, create a subscription with a trial offer and set the [cancel\_at](https://docs.stripe.com/api/subscriptions/update?#update_subscription-cancel_at) parameter to the end of the trial period.

This pattern supports opt-in renewals by ensuring customers aren’t converted to a recurring subscription by default.

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "customer_account=  {{CUSTOMER_ACCOUNT_ID}}  " \   -d "items[0][current_trial][trial_offer]=to_123" \   -d "items[0][quantity]=1" \   -d cancel_at=1610403706`

## Use trial offers with other features

### Trial offers with usage-based billing

When creating a [Price](https://docs.stripe.com/api/prices/object) object, you can specify a metered price instead of a recurring price and attach it to a trial offer. This lets you offer the same [usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based) functionality at a discounted price.

To use a metered price, set the [usage\_type](https://docs.stripe.com/api/prices/object?#price_object-recurring-usage_type) to `metered` and add an existing [meter](https://docs.stripe.com/api/prices/object?#price_object-recurring-meter) to track usage.

`curl https://api.stripe.com/v1/prices \  -u "`

`sk_test_REDACTED`

`:" \  -d currency=usd \  -d billing_scheme=per_unit \  -d unit_amount=1 \  -d "recurring[interval]=week" \   -d "recurring[usage_type]=metered" \   -d "recurring[meter]=mtr_123" \   -d "product_data[name]=Trial Period Price"`

Next, attach the price to a trial offer as you would with any other recurring price:

`curl https://api.stripe.com/v1/product_catalog/trial_offers \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "price=  {{PRICE_ID}}  " \   -d "duration[relative][iterations]=1" \   -d "duration[type]=timestamp" \   -d "end_behavior[transition][price]=  {{PRICE_ID}}  "`

## Additional considerations

### Subscription trialing status and trial offer

When using trial offers, a subscription’s `status` is determined by the price of the trial:

*   **Free Trials (0 GBP)**: If a subscription only contains trial offers, and all trial offer prices are set to 0 GBP, the subscription status is `trialing`. This matches the legacy `trial_end` behavior and is ideal for “no-card-required” or standard free trial flows.
*   **Paid Trials (>0 GBP)**: If the subscription has a regular price item, or the trial offers have a non-zero price, the subscription status will be `active`, `incomplete`, or `past_due`. This behavior mimics other subscriptions without trial offers. Because a paid trial requires an immediate successful payment to begin, the subscription follows the standard `PaymentIntent` lifecycle. This ensures that your existing billing logic—such as webhooks for successful payments—remains consistent, whether the customer is paying a promotional price or the full recurring amount.

### Events

Every time a trial changes, it triggers [Events](https://docs.stripe.com/api#event_types). Make sure that your integration handles them. For example, you might want to email a customer before a trial ends. Learn more about [handling subscription events](https://docs.stripe.com/billing/subscriptions/webhooks#events).

The following table describes the events that trigger before a free trial ends, when a trial subscription pauses or cancels, and when a subscription resumes and becomes active.

Event

Description

Use case

`customer.subscription.deleted`

Sent when a subscription ends.

Stop providing access to your product in response to this event. The subscription moves to the `canceled` status and sends this event after a free trial ends without a payment method, and if the subscription’s `missing_payment_method` end behavior is set to `cancel`.

`customer.subscription.resumed`

Sent when a subscription is no longer paused. When you receive this event, grant the customer access to the product if they lost access while the subscription was paused.

Paused subscriptions are converted into active subscriptions they resume. Resuming a subscription might generate an invoice and corresponding Payment Intent that must be paid before the subscription moves out of the `paused` status.

`customer.subscription.paused`

Sent when a subscription is fully paused. Invoicing won’t occur until the subscription resumes. When you receive this event, you can revoke the customer’s access to the product until they add a payment method and the subscription resumes.

Stop providing access to your product in response to this event. The subscription moves to the `paused` status and sends this event after a free trial ends without a payment method and if the subscription’s `missing_payment_method` end behavior is set to `pause`. The subscription remains `paused` until explicitly resumed.

`customer.subscription.trial_will_end`

Sent 3 days before the trial period ends. If the trial is less than 3 days, it triggers this event immediately.

Configure the subscription to automatically send an email to your customer 3 days before the trial period ends.

### Setting a billing anchor when a trial offer ends

When a trial offer ends and transitions to the regular recurring price, customers need to begin a fresh billing cycle immediately. By default, the subscription’s [billing\_cycle\_anchor](https://docs.stripe.com/api/subscriptions/object#subscription_object-trial_settings-end_behavior-billing_cycle_anchor) automatically resets to the time the trial ends (now). This ensures that your customers are charged the full amount for their first regular interval immediately, without generating prorations.

If you don’t want your `billing_cycle_anchor` to change, you can set it to `unchanged`.

Configuration options for `billing_cycle_anchor` include:

*   `now` (default): Resets the subscription’s `billing_cycle_anchor` to the exact time the trial offer completes. This creates a new billing cycle for the regular price and generates a full-amount invoice with no proration.
*   `unchanged`: Maintains the original anchor from when the subscription was first created. The period between the trial end and the next natural anchor date are billed as a prorated amount.

For example, if you offer a 7-day trial for 1 GBP and want the first 20 GBP monthly charge to cover a full month starting on day 8:

1.  Jan 1: Subscription created with a 7-day trial offer.
2.  Jan 8: Trial ends. The `billing_cycle_anchor` automatically resets to Jan 8.
3.  Invoice: Stripe generates an invoice for the full 20 GBP recurring price for the period of Jan 8–Feb 8. No proration is applied.

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: 2026-03-25.preview" \  -d "customer_account=  {{CUSTOMER_ACCOUNT_ID}}  " \   -d "items[0][price]=  {{PRICE_ID}}  " \   -d "items[0][current_trial][trial_offer]={{TRIAL_OFFER_ID}}" \   -d "trial_settings[end_behavior][billing_cycle_anchor]=unchanged"`

## See also

*   [Products and prices](https://docs.stripe.com/products-prices/overview)
*   [Prices](https://docs.stripe.com/api#prices)
*   [Subscriptions](https://docs.stripe.com/api#subscriptions)
*   [Managing subscription billing periods](https://docs.stripe.com/billing/subscriptions/billing-cycle)
