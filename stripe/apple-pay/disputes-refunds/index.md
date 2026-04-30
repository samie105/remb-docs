---
title: "Apple Pay liability shift, disputes, and refunds"
source: "https://docs.stripe.com/apple-pay/disputes-refunds"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:55:58.942Z"
content_hash: "763ed2e2bb2f21808b483150c354251517a149cc411aa3f406fd08319b37dfb7"
---

## Learn how to manage disputed or refunded Apple Pay payments.

Post payment activities can include disputes and refunds. When these use cases happen, learn how to address disputed payments, understand the nuances of liability shifts for Apple Pay charges, and manage refunds effectively.

## Disputes

Users must authenticate payments with their Apple Pay accounts, helping to reduce the risk of fraud or unrecognized payments. However, users can still dispute transactions after they complete payment. You can submit evidence to contest a dispute directly. The dispute process is the same as that for card payments. Learn about how to [manage disputes](https://docs.stripe.com/disputes/responding).

## Liability shift for Apple Pay charges

Apple Pay supports [liability shift](https://docs.stripe.com/payments/3d-secure/authentication-flow#disputed-payments) globally for all the major networks. For Visa, liability shift is limited to devices running iOS 16.2 and above. Devices running on iOS versions below 16.2 only receive liability shift on Visa if the card was issued in Europe.

## Refunds

You can partially or fully refund any successful Apple Pay payment. The refund process is the same as that for card payments. See [Refund and cancel payments](https://docs.stripe.com/refunds) for instructions on initiating or managing refunds.
