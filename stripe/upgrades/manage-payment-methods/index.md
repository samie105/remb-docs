---
title: "Manage default payment methods in the Dashboard"
source: "https://docs.stripe.com/upgrades/manage-payment-methods"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:54:18.247Z"
content_hash: "aa4fe82353d55d6df384208014481370092f08877766f31439306c7aca62535c"
---

## Upgrade your API to manage payment methods in the Dashboard by default.

On August 16, 2023, Stripe [updated the selection process](http://stripe.com/blog/dynamic-payment-methods) for default payment methods that apply to PaymentIntents and SetupIntents created with the [/v1/payment\_intents](https://docs.stripe.com/api/payment_intents) and [/v1/setup\_intents](https://docs.stripe.com/api/setup_intents) APIs.

In prior versions of the Stripe API, if you didn’t specify a [payment\_method\_types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types) parameter during the creation request, Stripe would default to using the card payment method for both PaymentIntents and SetupIntents.

Moving forward, Stripe applies eligible payment methods that you manage from your [Dashboard](https://dashboard.stripe.com/settings/payment_methods) to your PaymentIntents and SetupIntents by default if you don’t specify the `payment_method_types` parameter in the creation request.

### Payment methods

By default, Stripe enables cards and other common payment methods. You can turn individual payment methods on or off in the [Stripe Dashboard](https://dashboard.stripe.com/settings/payment_methods). In Checkout, Stripe evaluates the currency and any restrictions, then dynamically presents the supported payment methods to the customer.

To see how your payment methods appear to customers, enter a transaction ID or set an order amount and currency in the Dashboard.

You can enable Apple Pay and Google Pay in your [payment methods settings](https://dashboard.stripe.com/settings/payment_methods). By default, Apple Pay is enabled and Google Pay is disabled. However, in some cases Stripe filters them out even when they’re enabled. We filter Google Pay if you [enable automatic tax](https://docs.stripe.com/tax/checkout) without collecting a shipping address.

Checkout’s Stripe-hosted pages don’t need integration changes to enable Apple Pay or Google Pay. Stripe handles these payments the same way as other card payments.

## Update your payment flows

Choose from the upgrade path that matches your current Stripe integration:

If your integration uses Card Element or individual payment method Elements, we recommend migrating to the [Payment Element](https://docs.stripe.com/payments/payment-element/migration). This single, unified integration allows you to accept over 25 different payment methods.

### Create the PaymentIntent

In this version of the API, specifying the [automatic\_payment\_methods.enabled](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-automatic_payment_methods-enabled) parameter is optional. If you don’t specify it, Stripe assumes a value of `true`, which enables its functionality by default.

`curl https://api.stripe.com/v1/payment_intents \  -u "`

`sk_test_REDACTED`

`:" \  -d amount=1099 \  -d currency=usd`

### Client-side confirmations with Stripe.js

If your integration uses Stripe.js to confirm payments with [confirmPayment](https://docs.stripe.com/js/payment_intents/confirm_payment) or by [payment method](https://docs.stripe.com/js/payment_intents/payment_method), your existing processes remains the same and requires no further changes.

When you confirm payments, we recommend that you provide the [return\_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url) parameter. This allows you to accept payment methods that [require redirect](https://docs.stripe.com/payments/payment-methods/payment-method-support#additional-api-supportability).

``const form = document.getElementById('payment-form');  form.addEventListener('submit', async (event) => {   event.preventDefault();    const {error} = await stripe.confirmPayment({     //`Elements` instance that was used to create the Payment Element     elements,     confirmParams: {       return_url: '[https://example.com/return_url](https://example.com/return_url)',     },   });    if (error) {     // This point will only be reached if there is an immediate error when     // confirming the payment. Show error to your customer (for example, payment     // details incomplete)     const messageContainer = document.querySelector('#error-message');     messageContainer.textContent = error.message;   } else {     // Your customer will be redirected to your `return_url`. For some payment     // methods like iDEAL, your customer will be redirected to an intermediate     // site first to authorize the payment, then redirected to the `return_url`.   } });``

### Server-side confirmation

If you use server-side confirmation, you must use the [return\_url](https://docs.stripe.com/api/payment_intents/confirm#confirm_payment_intent-return_url) parameter in your integration.

`curl https://api.stripe.com/v1/payment_intents \  -u "`

`sk_test_REDACTED`

`:" \  -d amount=1099 \  -d currency=usd \  -d confirm=true \  -d "payment_method=  {{PAYMENT_METHOD_ID}}  " \   --data-urlencode "return_url=[https://example.com/return_url](https://example.com/return_url)"`

Alternatively, you can create the PaymentIntent or SetupIntent with the [automatic\_payment\_methods.allow\_redirects](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-automatic_payment_methods-allow_redirects) parameter set to `never`. This disables the `return_url` requirement on confirmation. You can still manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods), but the [payment methods that require redirects](https://docs.stripe.com/payments/bank-redirects#bank-redirects-api-support) aren’t eligible.

`curl https://api.stripe.com/v1/payment_intents \  -u "`

`sk_test_REDACTED`

`:" \  -d amount=1099 \  -d currency=usd \  -d confirm=true \  -d "payment_method=  {{PAYMENT_METHOD_ID}}  " \   -d "automatic_payment_methods[enabled]=true" \   -d "automatic_payment_methods[allow_redirects]=never"`

Lastly, you can create the PaymentIntent or SetupIntent with the [payment\_method\_types](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-payment_method_types) parameter. This also disables the `return_url` requirement on confirmation. With this option, you can’t manage payment methods from the [Dashboard](https://dashboard.stripe.com/settings/payment_methods).

`curl https://api.stripe.com/v1/payment_intents \  -u "`

`sk_test_REDACTED`

`:" \  -d amount=1099 \  -d currency=usd \  -d confirm=true \  -d "payment_method=  {{PAYMENT_METHOD_ID}}  " \   -d "payment_method_types[]=card"`
