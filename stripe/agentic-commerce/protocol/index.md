---
title: "Universal Commerce Protocol"
source: "https://docs.stripe.com/agentic-commerce/protocol"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:46:12.760Z"
content_hash: "226f96fc60f8eed9c1cc14a9d8d64e2ef51dd898f7370435637744572c0fb3d0"
---

## Learn how Universal Commerce Protocol (UCP) enables agentic commerce across platforms.

The [Universal Commerce Protocol](https://ucp.dev/) (UCP) is an open standard that lets different participants in commerce transactions interoperate, with support for checkout, identity linking, order tracking, and secure payment token exchange (Stripe is a member of the UCP Tech Council). Learn more at [ucp.dev](https://ucp.dev/).

## Key capabilities

UCP defines composable building blocks for commerce:

*   **Checkout**: Create and manage checkout flows including cart management, tax calculation, and payment, with or without human intervention.
*   **Identity linking**: OAuth 2.0 based authorization lets platforms act on a buyer’s behalf.
*   **Order**: Monitor the status of shipping, delivery, and returns with webhook-based lifecycle updates.
*   **Payment token exchange**: Platforms, businesses, and credential providers can securely exchange payment tokens and credentials.

## Stripe payment handlers for UCP

[UCP payment handlers](https://ucp.dev/latest/specification/payment-handler-guide/) define how payment instruments are acquired, exchanged, and processed between all participants in a transaction.

## See also

*   [UCP specification and documentation](https://ucp.dev/)
*   [UCP GitHub repository](https://github.com/Universal-Commerce-Protocol/ucp)
*   [UCP samples and reference implementations](https://github.com/Universal-Commerce-Protocol/samples)
