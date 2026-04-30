---
title: "Shared payment tokens"
source: "https://docs.stripe.com/agentic-commerce/concepts/shared-payment-tokens"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:46:32.947Z"
content_hash: "dd46861c7a8383830c7118b6cdb450cf50df87d89e9b0321b906191f391d3315"
---

As the seller, you receive a [shared payment token (SPT)](https://docs.stripe.com/api/shared-payment/granted-token) from the agent. An SPT is a scoped grant to use the customer’s payment method. The agent grants SPTs to your [Stripe profile](https://docs.stripe.com/get-started/account/profile), each with usage and expiration limits.

Issues `SharedPaymentToken`

Creates `PaymentIntent` with `SharedPaymentToken`

Payment method registration and processing

## Before you begin

*   By using SPTs, you agree to the [terms of service](https://stripe.com/legal/ssa-services-terms#stripe-agentic-commerce-seller-services-preview).
*   If you don’t already have a Stripe account, [create one](https://stripe.com/register).
*   Make sure you create your [Stripe profile](https://docs.stripe.com/get-started/account/profile) in the Stripe Dashboard.

## Test receiving an SPT

Use test helpers to simulate receiving an SPT granted by the agent. The following request grants your account an SPT using a test payment method and simulates limits that agents might set, such as currency, maximum amount, and expiration window.

`curl https://api.stripe.com/v1/test_helpers/shared_payment/granted_tokens \  -u "`

`sk_test_REDACTED`

`:" \  -d payment_method=pm_card_visa \  -d "usage_limits[currency]=usd" \   -d "usage_limits[max_amount]=1000" \   -d "usage_limits[expires_at]=1751587220"`

### Set usage limits

Use the `usage_limits` parameter to specify the maximum amount and expiration window. The agent sets the maximum amount to match the total amount of the transaction.

### Specify the payment method

Use the `payment_method` parameter to specify the payment method the customer selected for the purchase.

After you receive a granted `SharedPaymentToken`, create a `PaymentIntent` to complete the payment.

`curl https://api.stripe.com/v1/payment_intents \  -u "`

`sk_test_REDACTED`

`:" \  -d amount=1000 \  -d currency=usd \  -d "payment_method_data[shared_payment_granted_token]=spt_123" \   -d confirm=true`

When you confirm a `PaymentIntent` with the SPT, Stripe sets `payment_method` to a new `PaymentMethod` cloned from the customer’s original payment method. Subsequent events, such as refunds and reporting, behave as if you provided the `PaymentMethod` directly.

You can retrieve details about the granted `SharedPaymentToken`, including limited information about the underlying payment method, such as the card brand, last four digits, and usage limits.

`curl https://api.stripe.com/v1/shared_payment/granted_tokens/spt_123 \  -u "`

`sk_test_REDACTED`

`:"`

`{   "id": "spt_123",   "object": "shared_payment.granted_token",   "created": 1751500820,   "deactivated_at": null,   "deactivated_reason": null,   "usage_limits": {     "currency": "usd",     "expires_at": 1780145177,     "max_amount": 1000   }   ... }`

### Listen for webhook events

We send events to you and the agent when:

*   You use a granted SPT to accept a payment.
*   The agent revokes a granted SPT. You can’t create a payment with a revoked SPT.

Event

Description

Use case

`shared_payment.granted_token.deactivated`

The SPT has been deactivated (revoked or expired).

Listen for this event to know when you can no longer use the SPT.
