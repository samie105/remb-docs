---
title: "Set up payment methods for subscriptions with no initial payment"
source: "https://docs.stripe.com/billing/subscriptions/deferred-payment"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:18:25.445Z"
content_hash: "0088b6bee8076b7cf5eebfe937acd836e0f4a198dd40ed9b31ec6c0ba7cee18d"
---

Subscriptions that include [free trials](https://docs.stripe.com/billing/subscriptions/trials), [usage-based billing](https://docs.stripe.com/products-prices/pricing-models#usage-based-pricing), invoices with coupons, or applied customer credit balances often result in non-payment invoices. This means you don’t immediately charge your customer when you create the subscription.

Although you don’t charge customers for the first invoice, authenticating and authorizing their card can help increase successful completion of the first non-zero payment. These types of payments are known as off-session payments. To manage these scenarios, Stripe uses [SetupIntents](https://docs.stripe.com/api/setup_intents).

## Use SetupIntents

You can use [SetupIntents](https://docs.stripe.com/api/setup_intents) to:

*   Collect payment information.
*   Authenticate your customer’s card to claim [exemptions](https://stripe.com/guides/strong-customer-authentication#exemptions-to-strong-customer-authentication) later.
*   Authorize your customer’s card without charging it.

Authenticating payments allows your customer to grant permissions to charge their card. [Strong Customer Authentication](https://docs.stripe.com/strong-customer-authentication) requires this, and [3DS](https://docs.stripe.com/payments/3d-secure) is a common way to complete it. Collecting payment method information and authorizing it ensures that you can successfully charge the payment method.

In off-session scenarios, SetupIntents enable you to charge customers for their first non-zero payment without having to return them to your website or app for authentication. This reduces friction for your customers.

Stripe automatically creates SetupIntents for subscriptions that don’t require an initial payment. The authentication and authorization process also completes at this point, if required. If both succeed or aren’t required, no action is necessary, and the `subscription.pending_setup_intent` field is `null`. If either step fails, Stripe recommends using the SetupIntent on your front end to resolve the issue while your customer is on-session.

The [pending\_setup\_intent](https://docs.stripe.com/api/subscriptions/object#subscription_object-pending_setup_intent) field on a subscription doesn’t cancel automatically when the subscription ends. Listen for [customer.subscription.deleted](https://docs.stripe.com/billing/subscriptions/webhooks#events) events and manually [cancel a subscription SetupIntent](https://docs.stripe.com/api/setup_intents/cancel) if needed.

The next two sections explain how to manage scenarios where authentication or authorization fail.

## Manage authentication failures Client-side

Authentication failures occur when Stripe is unable to authenticate your customer with their card issuer. When this happens, the `status` of the SetupIntent is set to `requires_action`.

![How to handle subscription payment authentication failures.](https://b.stripecdn.com/docs-statics-srv/assets/authentication_failure.2eaec43cac8c688f0ff3438fbe3b50e4.svg)

To resolve these scenarios, call [confirmCardSetup](https://docs.stripe.com/js#stripe-confirm-card-setup) on your front end so your customer can complete the authentication flow manually. The code example below [expands](https://docs.stripe.com/api/expanding_objects) the [pending\_setup\_intent](https://docs.stripe.com/api/subscriptions/object#subscription_object-pending_setup_intent) to complete the flow.

`const {pending_setup_intent} = subscription;  if (pending_setup_intent) {   const {client_secret, status} = subscription.pending_setup_intent;    if (status === "requires_action") {     const {setupIntent, error} = await stripe.confirmCardSetup(client_secret);      if (error) {       // Display error.message in your UI.     } else {       // The setup has succeeded. Display a success message.     }   } }`

After completing this flow, authorization executes if it’s required. If authorization succeeds, or if it’s not required, `pending_setup_intent` is updated to `null` upon completion.

Payment authorization failures occur when Stripe can’t verify that a card can be charged. This sets the [status](https://docs.stripe.com/api/setup_intents/object#setup_intent_object-status) of the SetupIntent to `requires_payment_method`, which usually means that subsequent charges with that card fail.

![How to handle subscription payment authorization failures.](https://b.stripecdn.com/docs-statics-srv/assets/authorization_failure.0b6ca4a2e2bbeba11710bf22fb0a5d00.svg)

To resolve these scenarios, [collect a new payment method](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method), then update the default payment method for your customer or the subscription. The code example below [expands](https://docs.stripe.com/api/expanding_objects) the [pending\_setup\_intent](https://docs.stripe.com/api/subscriptions/object#subscription_object-pending_setup_intent) to complete the flow.

`const {pending_setup_intent, latest_invoice} = subscription;  if (pending_setup_intent) {   const {client_secret, status} = subscription.pending_setup_intent;    if (status === "requires_action") {     const {setupIntent, error} = await stripe.confirmCardSetup(client_secret);      if (error) {       // Display error.message in your UI.     } else {       // The setup has succeeded. Display a success message.     }   } else if (status === "requires_payment_method") {     // Collect new payment method.   } }`
