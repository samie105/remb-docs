---
title: "Apple Pay merchant tokens"
source: "https://docs.stripe.com/apple-pay/merchant-tokens"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:56:18.989Z"
content_hash: "09be9e56bcd4da4cb6bef4acc4c2358bdded5fb886b2c726205faa8d2e974b9f"
---

## Learn how to use Apple Pay merchant tokens for recurring, deferred, and automatic reload payments.

An [Apple Pay merchant token (MPAN)](https://developer.apple.com/apple-pay/merchant-tokens/) ties together a payment card, a business, and a customer, and enables the wallet holder to manage access to a card stored in their Apple wallet. Apple Pay’s latest guidelines recommend merchant tokens over device tokens (DPANs) because merchant tokens:

*   Allow for continuity across multiple devices
*   Enable recurring payments independent of a device
*   Keep payment information active in a new device even when its removed from a lost or stolen device

## Merchant token types

You can use Apple Pay to request an MPAN in three ways. Each type of request has different parameters that affect how the user is presented with Apple Wallet. Almost all request types provide the option to supply a `managementURL`, which routes customers to a webpage to manage their payment methods. If you request an MPAN and the issuer supports MPAN generation, you receive an MPAN. Otherwise, you receive a DPAN.

MPAN request type

Use case

Support

Recurring [PKRecurringPaymentRequest](https://developer.apple.com/documentation/passkit/pkrecurringpaymentrequest)

Issues an MPAN for use in a recurring payment such as a subscription.

*   [Apple Pay on the Web](https://developer.apple.com/documentation/apple_pay_on_the_web)
*   iOS > v16.0

Automatic reload [PKAutomaticReloadPaymentRequest](https://developer.apple.com/documentation/passkit/pkautomaticreloadpaymentrequest)

Issues an MPAN for use in a store card top-up or prepaid account. Supported parameters:

*   `automaticReloadBilling` shows billing details when you present Apple Pay.

*   [Apple Pay on the Web](https://developer.apple.com/documentation/apple_pay_on_the_web)
*   iOS > v16.0

Deferred payment [PKDeferredPaymentRequest](https://developer.apple.com/documentation/passkit/pkdeferredpaymentrequest)

Issues an MPAN for use in reservations such as hotels. Supported parameters:

*   `freeCancellationDate` shows the cancellation deadline when you present Apple Pay.
*   `billingAgreement` shows the terms of service when you present Apple Pay.

*   [Apple Pay on the Web](https://developer.apple.com/documentation/apple_pay_on_the_web)
*   Xcode 14.3
*   iOS > v16.4

## Add Apple Pay merchant tokens

You can add a [merchant token](https://developer.apple.com/apple-pay/merchant-tokens/) when presenting Apple Pay in the Express Checkout Element, web Payment Element, and mobile Payment Element. Stripe automatically handles merchant token requests in Stripe Checkout integrations.

1.  Set up [Express Checkout Element integration](https://docs.stripe.com/elements/express-checkout-element/accept-a-payment).
2.  Pass the `applePay` object relevant to your MPAN use case (choose from the drop-down to see use case code samples).
3.  Include relevant parameters for your use case.

`elements.create('expressCheckout', {   applePay: {     recurringPaymentRequest: {       paymentDescription: "Standard Subscription",       regularBilling: {         amount: 1000,         label: "Standard Package",         recurringPaymentStartDate: new Date("2023-03-31"),         recurringPaymentEndDate: new Date("2024-03-31"),         recurringPaymentIntervalUnit: "year",         recurringPaymentIntervalCount: 1,       },       billingAgreement: "billing agreement",       managementURL: "[https://stripe.com](https://stripe.com/)",     },   }, });`

## Merchant token auth rate monitoring

For Sigma users, the `charges` table contains a `card_token_type` enum field to indicate the charge is using an `mpan` or `dpan` card. The following Sigma query example calculates the MPAN auth rate:

`-- deduplicated MPAN auth rate select   100.0 * count(     case       when charge_outcome in ('authorized', 'manual_review') then 1     end   ) / count(*) as deduplicated_auth_rate_pct,   count(*) as n_attempts from   authentication_report_attempts a   join charges c on c.id = a.charge_id where   c.created >= date('2021-01-01')   and c.card_tokenization_method = 'apple_pay'   -- The new field added to charges table.   and c.card_token_type = 'mpan'   -- deduplicate multiple manual retries to a single representative charge   and is_final_attempt`
