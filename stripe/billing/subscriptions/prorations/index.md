---
title: "Prorations"
source: "https://docs.stripe.com/billing/subscriptions/prorations"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:25:45.376Z"
content_hash: "4b3134d90dfd526439ad209cbb27b9d7c510220a2aba46647410b0a6b49c85c3"
---

The most complex aspect of changing existing subscriptions are prorations, where the customer is charged a percentage of a subscription’s cost to reflect partial use. This page explains how prorations work with subscriptions and how to manage prorations for your customers.

## How prorations work

For example, [upgrading or downgrading](https://docs.stripe.com/billing/subscriptions/change-price) a subscription can result in prorated charges. If a customer upgrades from a 10 USD monthly plan to a 20 USD option, they’re charged prorated amounts for the time spent on each option. Assuming the change occurred halfway through the billing period, the customer is billed an additional 5 USD: -5 USD for unused time on the initial price, and 10 USD for the remaining time on the new price.

Proration ensures that customers are billed accurately, but a proration can result in different payment amounts than you might expect. Negative prorations aren’t automatically refunded and positive prorations aren’t immediately billed, although you can do both manually.

You can [preview a proration](#preview-proration) to view the amount before applying the changes. To learn more about [how credit prorations work](#credit-prorations), read our guide.

### Prorations and discounts

All [invoice items](https://docs.stripe.com/api/invoiceitems/object#invoiceitem_object) that are prorations (`prorations=true`) are set to `discountable=false`. Discounts applied to an invoice containing prorations are only applied to [invoice items](https://docs.stripe.com/api/invoiceitems/object#invoiceitem_object-discounts) and [invoice line items](https://docs.stripe.com/api/invoice-line-item/object#invoice_line_item_object-discounts) that aren’t prorations. Any discounts previously applied to the subscription and affecting the amount of the proration are reflected in the proration invoice item’s amount.

Non-prorations show discount adjustments in [discount\_amounts](https://docs.stripe.com/api/invoice-line-item/object#invoice_line_item_object-discount_amounts).

#### Discount changes and prorations

Updating subscription-level promotion codes, coupons, or discounts by themselves doesn’t create proration invoice items. Only changes that affect billable amounts for the current billing cycle create prorations, such as:

*   Changing a subscription item’s `price` or `quantity`
*   Adding or removing subscription items
*   Changing billing cycle anchors or proration behavior

When you make a change that creates a proration, Stripe computes the proration amounts using the subscription’s current pricing and discounting state at the time the proration is calculated. If you modify discounts as part of the same API call that also triggers prorations (for example, changing an item quantity and modifying a discount in a single update), the proration debit or credit is calculated using the modified discounts.

For example:

*   **Updating only a subscription item’s metadata or applying or removing a discount:** No proration invoice items are created, and no immediate proration charges or credits appear on the upcoming invoice.
*   **Updating a subscription item’s quantity and removing a discount in the same call:** Proration invoice items are created for the quantity change, and the proration amounts reflect prices after the discount change—the modified discount is used in the proration calculation.

For more information about how discounts work on subscriptions, including how `duration=once` coupons are consumed and removed from `subscription.discounts`, see [Coupons and promotion codes](https://docs.stripe.com/billing/subscriptions/coupons#coupon-duration).

### What triggers prorations

By default, the following scenarios result in a proration:

Update

Description

Changing [items](https://docs.stripe.com/api/subscriptions/update#update_subscription-items)

Adding a new item or removing an existing item

Changing [price](https://docs.stripe.com/api/subscriptions/update#update_subscription-items-price)

Changing to a price with a different base cost or billing period

Changing [quantity](https://docs.stripe.com/api/subscriptions/update#update_subscription-items-quantity)

Increasing or decreasing the quantity on a subscription item

Adding [trial\_end](https://docs.stripe.com/api/subscriptions/update#update_subscription-trial_end) or [trial\_from\_plan](https://docs.stripe.com/api/subscriptions/update#update_subscription-trial_from_plan)

Adding a trial period to an active subscription

Changing [billing\_cycle\_anchor](https://docs.stripe.com/api/subscriptions/update#update_subscription-billing_cycle_anchor)

Resetting the billing period to a new date

Setting [cancel\_at](https://docs.stripe.com/api/subscriptions/update#update_subscription-cancel_at)

Canceling a subscription mid-period (not at period end)

### What doesn’t trigger prorations

Many subscription updates don’t affect billing or generate prorations. Make these updates at any time without creating _proration_ invoice items:

#### Note

These updates don’t generate proration invoice items with `proration_behavior=create_prorations` or generate invoices with proration invoice items with `proration_behavior=always_invoice` because they don’t change the billing amount for the current period.

### Manually creating your own prorations

To calculate your own prorations outside of Stripe and add them to the subscription, pass [add\_invoice\_items](https://docs.stripe.com/api/subscription_schedules/create#create_subscription_schedule-add_invoice_items) with a negative `unit_amount` (equal to the calculated proration amount) to these endpoints:

*   [CreateSubscription](https://docs.stripe.com/api/subscriptions/create)
*   [UpdateSubscription](https://docs.stripe.com/api/subscriptions/update)
*   [CreateSubscriptionSchedule](https://docs.stripe.com/api/subscription_schedules/create)
*   [UpdateSubscriptionSchedule](https://docs.stripe.com/api/subscription_schedules/update)

### When prorations are applied

Prorations only apply to charges that occur ahead of the billing period. [Usage-based billing](https://docs.stripe.com/billing/subscriptions/usage-based) isn’t subject to proration.

The prorated amount is calculated as soon as the API updates the subscription. The current billing period’s start and end times are used to calculate the cost of the subscription before and after the change.

### Prorations and unpaid invoices

Stripe calculates prorations based on the subscription’s status at the time of an update, assuming that any previous invoices for the subscription will eventually be paid. If a customer changes their subscription while having an unpaid invoice for the current period, they might receive a credit for unused time on the higher-priced plan, even if they haven’t paid for that time yet.

To avoid crediting for unpaid time, you can disable prorations when the subscription’s latest invoice is unpaid. When updating the subscription, set [proration\_behavior](https://docs.stripe.com/api/subscriptions/update?update_subscription-proration_behavior=#update_subscription-proration_behavior) to `none`. Select one of the following approaches:

1.  **To keep the original billing period:** Manually [create a one-off invoice](https://docs.stripe.com/api/invoices/create) for any new charges.
2.  **To charge immediately for the new plan and reset the billing period:** Set `billing_cycle_anchor` to `now`. For more details, see [Reset the billing period to the current time](https://docs.stripe.com/billing/subscriptions/billing-cycle#reset-the-billing-period-to-the-current-time).

Either of these approaches can lead to double payment if the customer eventually pays the old invoice. To avoid this, [void the unpaid invoice](https://docs.stripe.com/api/invoices/void).

### Taxes and prorations

For information about how taxes work with prorations, see [Collect taxes for recurring payments](https://docs.stripe.com/billing/taxes/collect-taxes).

## Credit prorations

Credit prorations are issued when customers downgrade their subscriptions or cancel subscription items before the end of their billing period. Stripe offers two approaches for calculating credit prorations, depending on whether you set your subscription’s [billing\_mode](https://docs.stripe.com/billing/subscriptions/billing-mode#differences-between-classic-and-flexible-billing-mode) to `classic` or `flexible`.

### Calculation logic with no prorations

In the following scenario, you upgrade a 10 GBP monthly subscription to 20 GBP with the `proration_behavior` set to `none` for 10 days. There’s no previous debit to base it on. Later, you downgrade the subscription to 10 GBP per month with the `proration_behavior` set to `always_invoice`.

To set up this scenario, first you [create a subscription](https://docs.stripe.com/api/subscriptions/create) for 10 GBP per month on April 1:

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -d "items[0][price]=price_10_monthly"`

The response includes the invoice that’s created for this subscription:

Create subscription response

`{   "id": "sub_123",   "latest_invoice": {     "id": "in_123",     "total": 1000,     "currency": "usd"   } }`

Then, on April 11, you [upgrade the subscription](https://docs.stripe.com/billing/subscriptions/change-price#changing) to 20 GBP per month without creating prorations:

`curl https://api.stripe.com/v1/subscriptions/sub_123 \  -u "`

`sk_test_REDACTED`

`:" \  -d "items[0][id]=sub_item_1" \   -d "items[0][price]=price_20_monthly" \   -d proration_behavior=none`

The latest invoice remains unchanged because `proration_behavior` is `none`:

Upgrade subscription response

`{   "id": "sub_123",   "latest_invoice": {     "id": "in_123"   } }`

Finally, on April 21, you [downgrade the subscription](https://docs.stripe.com/billing/subscriptions/change-price#changing) to 10 GBP per month and create prorations:

`curl https://api.stripe.com/v1/subscriptions/sub_123 \  -u "`

`sk_test_REDACTED`

`:" \  -d "items[0][id]=sub_item_1" \   -d "items[0][price]=price_10_monthly" \   -d proration_behavior=always_invoice`

**Classic**

**Flexible**

The `billing_mode=classic` proration calculation logic creates a credit proration based on the current price, even though the customer never paid the 20 GBP monthly rate. The latest invoice credits a third of the month for 20 GBP (-6.67 GBP), even though the customer never paid for the `price_20_monthly` price. It also debits a third of the month for 10 GBP (3.33 GBP).

The calculation logic enabled with `billing_mode=flexible` creates a credit proration based on the last price billed for the subscription item. In this case, the latest invoice credits a third of a month for the 10 GBP monthly price billed on April 1 (3.33 GBP) and debits a third of the month for the 10 GBP price (3.33 GBP). The credit and debit cancel out so the invoice total is 0 GBP.

`# billing_mode = classic   {     "id": "sub_123",     "latest_invoice": {       "id": "in_456",       "total": -334,       "currency": "usd"     }   }`

`# billing_mode = flexible   {     "id": "sub_123",     "latest_invoice": {       "id": "in_456",       "total": 0,       "currency": "usd"     }   }`

### Calculation logic for coupons applied to multiple subscription items

Stripe weights the `amount_off` coupon on the credit proration to prevent over-billing.

In the following scenario, a 5 GBP coupon is unevenly allocated to a 25 GBP monthly subscription for a 10 GBP item and 20 GBP item.

To set up this scenario, you create a subscription with multiple items and a coupon on February 1:

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -d "items[0][price]=price_10_monthly" \   -d "items[1][price]=price_20_monthly" \   -d "discounts[0][coupon]=five_dollars_off"`

Which returns this response:

Create subscription with multiple items and a coupon response

`{   "id": "sub_123",   "latest_invoice": {     "id": "in_123",     "total": 2500,     "currency": "usd",     "lines": {       "data": [       {         "id": "ili_1",         "amount": 1000,         "price": "price_10_monthly",         "discount_amounts": [{           "discount": "di_a",           "amount": 166 }] },       {         "id": "ili_2",         "amount": 2000,         "price": "price_20_monthly",         "discount_amounts": [{           "discount": "di_a",           "amount": 334           }]         }     ] }   } }`

To cancel the 10 GBP monthly subscription item:

`curl https://api.stripe.com/v1/subscription_items/si_10_monthly \  -u "`

`sk_test_REDACTED`

`:" \  -d proration_behavior=create_prorations`

When a subscription item is deleted, the `billing_mode` associated with that subscription affects how the proration is calculated as follows:

**Classic**

**Flexible**

The default behavior distributes a 5 GBP coupon to each item (2.5 GBP each), canceling the cheaper item (5 GBP) and resulting in a refund of 2.5 GBP. Stripe calculates the total with the formula `-0.5 x (10 USD price - 5 USD coupon) = -2.50 USD`.

The flexible behavior reflects the proportional discount applied to the canceled item, rather than potentially applying the full discount amount to the proration calculation. Stripe calculates the total using the formula `-0.5 x (10 USD price - 1.66 USD discount amount) = -4.17 USD`.

`# billing_mode = classic   {     "id": "sub_123",     "latest_invoice": {       "id": "in_456",       "total": -250,       "currency": "usd"     }   }`

`# billing_mode = flexible   {     "id": "sub_123",     "latest_invoice": {       "id": "in_789",       "total": -417,       "currency": "usd"     }   }`

## Preview a proration

You can [create a preview invoice](https://docs.stripe.com/api/invoices/create_preview) to preview changes to a subscription. This API call doesn’t modify the subscription. Instead, it returns the upcoming [invoice](https://docs.stripe.com/api/invoices) based only on the parameters that you pass. Changing the `price` or `quantity` both result in a proration. This example changes the `price` and sets a date for the proration.

`# Don't put any keys in code. See [https://docs.stripe.com/keys-best-practices.](https://docs.stripe.com/keys-best-practices) # Find your keys at [https://dashboard.stripe.com/apikeys.](https://dashboard.stripe.com/apikeys) client = Stripe::StripeClient.new(`

`'sk_test_REDACTED'`

`)  # Set proration date to this moment: proration_date = Time.now.to_i  subscription = client.v1.subscriptions.retrieve('sub_49ty4767H20z6a')  # See what the next invoice would look like with a price switch # and proration set: items = [{   id: subscription.items.data[0].id,   price: 'price_CBb6IXqvTLXp3f', # Switch to new price }]  invoice = client.v1.invoices.create_preview({   customer_account: 'acct_4fdAW5ftNQow1a',   subscription: 'sub_49ty4767H20z6a',   subscription_details: {     items: items,     proration_date: proration_date,   } })`

You can expand the example response below to see:

*   The credit for unused time at the previous price on lines 36-38.
*   The cost for time spent at the new price on lines 107-109.
*   The new subtotal and total for the invoice on lines 276-279.

`{   "id": "upcoming_in_1OujwkClCIKljWvsq5v2ICAN",   "account_country": "US",   "account_name": "Test account",   "amount_due": 3627,   "amount_paid": 0,   "amount_remaining": 3627,   "application_fee_amount": null,   "attempt_count": 0,   "attempted": false,`

Use this information to confirm the changes with the customer before modifying the subscription. Because Stripe prorates to the second, prorated amounts might change between the time they’re previewed and the time the update is made. To avoid this, pass in a `subscription_details.proration_date` value when creating a preview. When you update the subscription, pass the same date using the `proration_date` parameter on a subscription so that the proration is calculated at the same time.

## Control proration behavior

Prorating is controlled by the [proration\_behavior](https://docs.stripe.com/api/subscriptions/update#update_subscription-proration_behavior) parameter, which has three possible parameter options: `create_prorations`, `always_invoice`, and `none`.

### Default behavior

The default parameter for `proration_behavior` is `create_prorations`, which creates proration invoice items when applicable. These proration items are only invoiced immediately under [certain conditions](https://docs.stripe.com/billing/subscriptions/change-price#immediate-payment).

### Create immediate prorations

To bill a customer immediately for a change to a subscription on the same billing period, set `proration_behavior` to `always_invoice` when you modify the subscription. This calculates the proration, then immediately generates an invoice.

### Disable prorations

To disable prorations on a per-request basis, set the `proration_behavior` parameter to `none`. No parameter turns off all future prorations for a subscription. To disable prorations indefinitely, set `proration_behavior` to `none` for every request that generates prorations:

`curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \   -u` 

`sk_test_REDACTED`

`: \   -d "items[0][id]"="si_1AkFf6LlRB0eXbMtRFjYiJ0J" \   -d "items[0][price]"="price_CBb6IXqvTLXp3f" \   -d "proration_behavior"="none"`

When prorations are disabled, customers are billed the full amount at the new price when the next invoice is generated.
