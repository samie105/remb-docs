---
title: "Set payment methods per-subscription"
source: "https://docs.stripe.com/billing/subscriptions/payment-methods-setting"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:24:04.684Z"
content_hash: "9a6f5dd1af99b105671414b9568b185cb629a8601e502e2ec775f06413e13842"
---

The subscription [payment\_settings](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings) parameter lets you set specific payment methods on individual subscriptions. This allows more flexibility than a single `default_payment_method` or less granular customer settings.

To enable payment methods, you first need to activate them in your [account settings](https://dashboard.stripe.com/settings/payment_methods) in the Stripe Dashboard.

In some situations, there might be restrictions that prevent certain payment methods from being used for a subscription. For example, a payment method might only operate in one currency, or have limitations on the amount that a customer can pay. Stripe doesn’t automatically select a payment method if limitations prevent it from being used. Learn more about [payment method support](https://docs.stripe.com/payments/payment-methods/payment-method-support#product-support).

## Manually select payment methods

You can override the payment methods that a customer can use to pay a subscription by changing its [payment settings](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings).

`curl https://api.stripe.com/v1/subscriptions/sub_49ty4767H20z6a \  -u "`

`sk_test_REDACTED`

`:" \  -d "payment_settings[payment_method_types][]=card" \   -d "payment_settings[payment_method_types][]=customer_balance"`

If you configured a default payment method on either the customer (represented as a customer-configured [Account](https://docs.stripe.com/api/v2/core/accounts/update#v2_update_accounts-response-configuration-customer-billing-default_payment_method) or a [Customer](https://docs.stripe.com/api/customers/object#customer_object-invoice_settings-default_payment_method)) or the [Subscription](https://docs.stripe.com/api/subscriptions/object#subscription_object-default_payment_method), include it in the list of `payment_method_types`. Otherwise, that method won’t be used and payment might fail.

## Payment method priority

By default, customers can pay a subscription’s generated [invoice](https://docs.stripe.com/api/invoices) with any of the enabled payment methods in your [Invoice default payment method configuration](https://dashboard.stripe.com/settings/billing/invoice). This takes precedence over the older [default\_source](https://docs.stripe.com/api/customers/object#customer_object-default_source) customer setting.

If set, a subscription’s `payment_settings.payment_method_types` takes priority over default invoice settings, but only for that specific subscription. Payment method types are passed onto the subscription’s [setup intent](https://docs.stripe.com/api/setup_intents) and invoices.

You can further specify a subscription’s `default_payment_method`, or the older `default_source`, to prioritize which payment method is attempted.

If you enable **Save customer payment information** in the Dashboard invoice settings or the [save\_default\_payment\_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-save_default_payment_method) parameter of the `Subscription`, any payment method the customer uses to pay the invoice becomes the new default.

## Enable customers to update their payment method

From the Dashboard, you can generate single-use links that let customers update the payment method on an automatically billed subscription.

You can generate an update link from two places:

*   On the **Subscription details** page for the subscription, click the **Actions** menu and select **Share payment update link**.
*   On the [Subscriptions page](https://dashboard.stripe.com/subscriptions), find the subscription and click its overflow menu (), then select **Share payment update link**.

In the **Share payment update link** dialog, you can email the link directly to the customer or copy it to share another way. You can also deactivate all of the subscription’s existing payment update links.

You can generate links only for subscriptions that have Billing set to `Auto`. The menu item doesn’t appear for subscriptions with Billing set to `Send`.

Subscription payment update links have the following restrictions:

*   A link can only update the payment method on the associated subscription, and can’t change the customer’s default payment method.
*   The subscription’s status must be `active`, `past_due`, or `trialing`. It can’t be `unpaid` or ended.
*   The new payment method must be a card.
*   Each link only allows a customer to update their payment details one time.
*   If unused, a link expires after 30 days.

## Payment method errors

Payment method errors can prevent a subscription from being created. This can happen when:

*   You manually select a payment method but a restriction, such as supported currencies, prevents it from being used.
*   A payment method isn’t activated for your account

Errors can also occur at time of payment, and Stripe can’t finalize the invoice. See invoicing [payment method errors](https://docs.stripe.com/invoicing/payment-methods#payment-method-errors) for details.

## Payment method options

Some payment methods have additional options that you can set to customize how a customer pays. See the [payment method options](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings) documentation for details.
