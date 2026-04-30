---
title: "Cartes Bancaires with Apple Pay"
source: "https://docs.stripe.com/apple-pay/cartes-bancaires"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:57:17.686Z"
content_hash: "e9a3125f18260222a73340d31c5f6fcaefee8a558dc15134561988d3e179e858"
---

Use this guide to enable the [Cartes Bancaires](https://docs.stripe.com/payments/cartes-bancaires) payment method in your Apple Pay integration.

## Before you begin

To avoid issues with failed payments, take the following steps:

*   Add Cartes Bancaires to your list of enabled networks only if the transaction is in Euros.
*   Only enable Cartes Bancaires with Apple Pay if you support charges through Cartes Bancaires.
*   If you’re a platform using the [on\_behalf\_of](https://docs.stripe.com/api/payment_intents/create#create_payment_intent-on_behalf_of) parameter, make sure that the `on_behalf_of` account supports Cartes Bancaires charges. Check an account’s eligibility using the [Capabilities API](https://docs.stripe.com/api/capabilities).

[](#ios-add-cartes-bancaires-to-enabled-networks)

When your app starts, configure the SDK with Cartes Bancaires as an enabled Apple Pay network.

`StripeAPI.additionalEnabledApplePayNetworks = [.cartesBancaires]`

[](#ios-test-apple-pay)

Apple Pay Wallet can’t save Stripe test card information. Instead, Stripe recognizes when you’re using your test API keys and provides a successful test card token for you to use. This allows you to make test payments using a live card without any charges being applied.

Make sure you test using a Cartes Bancaires card obtained from one of the [Apple Pay participating banks](https://support.apple.com/en-us/109516).
