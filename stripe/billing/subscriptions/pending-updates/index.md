---
title: "Pending updates"
source: "https://docs.stripe.com/billing/subscriptions/pending-updates"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:24:24.981Z"
content_hash: "f77301c9a8d5a95d4ea0e48f8dca48ebff31df2432be01c9ee2a58b4b7e4d73a"
---

Updating a [subscription](https://docs.stripe.com/billing/subscriptions/creating) generates a new [invoice](https://docs.stripe.com/api/invoices) when:

*   The subscription requires payment for the first time, such as the end of a trial period.
*   The billing period changes.
*   Changing the subscription causes a proration and `proration_behavior=always_invoice`.

Many subscription updates don’t generate new invoices or trigger pending updates, including:

*   Configuration changes (payment methods, tax settings, retry settings)
*   Metadata updates on subscriptions or subscription items
*   Adding or updating coupons or promotion codes that apply to future invoices
*   Billing threshold adjustments
*   Setting `cancel_at_period_end` to `true`
*   Adding one-time charges with `add_invoice_items`

These updates apply immediately without payment implications. For a complete list, see [What doesn’t trigger prorations](https://docs.stripe.com/billing/subscriptions/prorations#no-prorations).

By default, Stripe applies updates regardless of whether payment on the new invoice succeeds. If payment fails, rolling back the updates is a manual process. You need to create a new invoice, prorate items on the invoice, and then initiate payment again. However, with the pending updates feature, you can make changes to subscriptions only if payment succeeds on the new invoice.

## Before you begin

You can use pending updates if the subscription’s [collection\_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method) is `charge_automatically` and the payment method is one of the following:

*   [Card](https://docs.stripe.com/payments/cards)
*   [Link](https://docs.stripe.com/payments/link)
*   [Alipay](https://docs.stripe.com/payments/alipay)
*   [Amazon Pay](https://docs.stripe.com/payments/amazon-pay)
*   [Afterpay/Clearpay](https://docs.stripe.com/payments/afterpay-clearpay)
*   [Apple Pay](https://docs.stripe.com/apple-pay)
*   [Cash App Pay](https://docs.stripe.com/payments/cash-app-pay)
*   [EPS](https://docs.stripe.com/payments/eps)
*   [GoPay](https://docs.stripe.com/payments/gopay)
*   [Google Pay](https://docs.stripe.com/google-pay)
*   [Kakao Pay](https://docs.stripe.com/payments/kakao-pay/accept-a-payment)
*   [Klarna](https://docs.stripe.com/payments/klarna)
*   [KR Card](https://docs.stripe.com/payments/kr-card/accept-a-payment)
*   [Naver Pay](https://docs.stripe.com/payments/naver-pay/accept-a-payment)
*   [NG Card](https://docs.stripe.com/payments/ng-card/accept-a-payment)
*   [PayPal](https://docs.stripe.com/payments/paypal)
*   [PayTo](https://docs.stripe.com/payments/payto)
*   [Pix](https://docs.stripe.com/payments/pix)
*   [PromptPay](https://docs.stripe.com/payments/promptpay)
*   [Revolut Pay](https://docs.stripe.com/payments/revolut-pay)
*   [Satispay](https://docs.stripe.com/payments/satispay)
*   [Stablecoins and crypto](https://docs.stripe.com/payments/stablecoin-payments)
*   [Swish](https://docs.stripe.com/payments/swish)
*   [TWINT](https://docs.stripe.com/payments/twint)
*   [UPI](https://docs.stripe.com/payments/upi)
*   [WeChat Pay](https://docs.stripe.com/payments/wechat-pay)

[](#update-subscription)

You can use pending updates with the [update subscription](https://docs.stripe.com/api/subscriptions/update), [create subscription item](https://docs.stripe.com/api/subscription_items/create), and [update subscription item](https://docs.stripe.com/api/subscription_items/update) calls. When you make the update, set `payment_behavior=pending_if_incomplete`. The example below adds a new price to a subscription. Because `proration_behavior=always_invoice`, an invoice is created and payment is attempted when the update is made.

`curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \   -u` 

`sk_test_REDACTED`

`: \   -d "payment_behavior"="pending_if_incomplete" \   -d "proration_behavior"="always_invoice" \   -d "items[0][id]"="si_09IkI4u3ZypJUk5onGUZpe8O" \   -d "items[0][price]"="price_CBb6IXqvTLXp3f"`

If payment succeeds, the subscription is updated. If payment fails, the `Subscription` object that’s returned contains a `pending_update` hash with the changes:

`{   "id": "sub_49ty4767H20z6a",   "object": "subscription",   "application_fee_percent": null,   "pending_update": {     "expires_at": 1571194285,     "subscription_items": [       {         "id": "si_09IkI4u3ZypJUk5onGUZpe8O",         "price": "price_CBb6IXqvTLXp3f"       }     ]   } }`

[

## Handle failed payments

Client-side





](#handling-failed-payments)

After making the update, check the `pending_update` hash on the subscription or listen for the `customer.subscription.updated` event in your [webhook](https://docs.stripe.com/webhooks). A populated `pending_update` hash means the payment failed and your subscription update isn’t applied.

Build logic to handle payment failures due to card declines and customer authentication requests:

*   For card declines, [attach a new payment method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method) to the customer. Then use the [pay](https://docs.stripe.com/api/invoices/pay) endpoint to pay the invoice that the update generates.
*   For customer authentication, follow the [requires action](https://docs.stripe.com/billing/subscriptions/overview#requires-action) flow.

A successful payment immediately applies the changes in the `pending_update` hash and updates the invoice to `paid`.

If payment fails again, the `pending_update` hash remains on the subscription with the original [expiry date](#expiration) and no changes are applied.

## Supported attributes for pending updates

Pending updates only support attributes that control proration behavior or generate new invoices.

The [update subscription](https://docs.stripe.com/api/subscriptions/update) endpoint supports the following attributes:

*   `expand`
*   `payment_behavior`
*   `proration_behavior`
*   `proration_date`
*   `billing_cycle_anchor`
*   `items`
    *   `price`
    *   `quantity`
*   `trial_end`
*   `trial_from_plan`
*   `add_invoice_items`

The [create subscription item](https://docs.stripe.com/api/subscription_items/create) and [update subscription item](https://docs.stripe.com/api/subscription_items/update) endpoints support the following attributes:

*   `expand`
*   `payment_behavior`
*   `proration_behavior`
*   `proration_date`
*   `price`
*   `quantity`

## Expired updates

If you don’t take any action after an update fails, Stripe voids the invoice and discards the update after it expires.

A pending update’s `expired_at` time matches the first occurrence of either the [trial end](https://docs.stripe.com/api/subscriptions/object#subscription_object-trial_end) or the earliest [items.current period end](https://docs.stripe.com/api/subscriptions/object##subscription_object-items-data-current_period_end). This applies if either time is within 23 hours of the update request. Otherwise, the expiration is 23 hours from the update request.

Stripe also automatically voids the invoice and removes the pending update if any of the following occurs:

*   The subscription reaches a billing threshold.
*   A subscription schedule linked to the subscription transitions to a new phase.

## Pending updates events

Use [webhooks](https://docs.stripe.com/webhooks) to listen for the following events related to pending updates. The events are the same whether you use `Customer` objects or customer-configured `Account` objects.

Event

Purpose

`customer.subscription.updated`

Receive notifications for subscriptions, checking for the `pending_updates` hash and [resolving payment failures](https://docs.stripe.com/billing/subscriptions/pending-updates#handling-failed-payments) if needed.

`customer.subscription.pending_update_applied`

Receive notifications when pending updates are applied so that you can take further actions like upgrading, downgrading, provisioning, or deprovisioning services.

`customer.subscription.pending_update_expired`

Receive notifications when pending updates expire or are automatically voided, and if needed, try the update request again.

## Pending updates and subscription schedules

You can use both pending updates and [subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules) to manage subscriptions. A schedule phase change discards a pending update and voids the associated invoice. Retry the update request after the phase transition if needed.

## Metered items

If a subscription includes metered items, Stripe bills any outstanding usage on the pending update invoice. However, if the pending update expires before payment, Stripe discards this usage, which prevents any subsequent invoices from billing for them.

If the pending update removes a metered price, Stripe disregards any usage reported between the pending update’s creation and the resulting invoice payment. You can’t bill for that usage. However, if `billing_mode=flexible` is on the subscription, Stripe bills for usage when removing a metered price.
