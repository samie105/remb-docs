---
title: "Migrate subscriptions to Stripe Billing"
source: "https://docs.stripe.com/billing/subscriptions/migrate-subscriptions"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:22:24.354Z"
content_hash: "cf3157cb698787c4252b061ed91777fc578a08e263aac9d3ae9f7acc6de2ab45"
---

You can import existing [subscriptions](https://docs.stripe.com/billing/subscriptions/creating) from third-party billing systems (such as Zuora, Recurly, Chargify, or Chargebee) into Stripe Billing. You can also migrate subscriptions from an in-house billing system or from a different Stripe account.

Use the [Billing migration toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit) to migrate your subscriptions without writing code. Alternatively, you can use the [Stripe APIs](https://docs.stripe.com/billing/subscriptions/import-subscriptions) to import subscriptions with manual scripts.

## Before you begin

You must know:

*   Your current payment processor.
*   Your current subscription provider.
*   Your [pricing model](https://docs.stripe.com/products-prices/pricing-models).

## Getting started

[](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit "Migrate subscriptions using toolkit")

[Migrate subscriptions using toolkit](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit "Migrate subscriptions using toolkit")

[

Use the Billing migration toolkit to migrate your subscriptions to Stripe.

](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit "Migrate subscriptions using toolkit")

[](https://docs.stripe.com/billing/subscriptions/import-subscriptions "Migrate subscriptions with APIs")

[Migrate subscriptions with APIs](https://docs.stripe.com/billing/subscriptions/import-subscriptions "Migrate subscriptions with APIs")

[

Learn how to migrate your subscriptions to Stripe using Stripe APIs.

](https://docs.stripe.com/billing/subscriptions/import-subscriptions "Migrate subscriptions with APIs")

## Migration stages

A typical migration process consists of the following stages:

1.  [Set up your billing integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions).
2.  [Migrate your customer and payment processor information](https://docs.stripe.com/get-started/data-migrations/pan-import).
3.  [Import your subscriptions to Stripe Billing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit).

### Migration decision matrix

The migration process varies slightly depending on a few factors. Use the following decision matrix to understand the required steps for your situation.

**My customer and payment data is in an external system**

**My customer and payment data is already in Stripe**

**Migrate subscription data from a third party**

*   [Set up a Stripe Billing integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
*   [Request a PAN data import from your current processor](https://docs.stripe.com/get-started/data-migrations/pan-import)
*   [Use the Billing toolkit to migrate subscriptions data to Stripe Billing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit)

*   [Set up a Stripe Billing integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
*   [Use the Billing toolkit to migrate subscriptions data to Stripe Billing](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit)

**Migrate subscription data between Stripe accounts**

*   [Set up a Stripe Billing integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
*   [Copy PAN data across Stripe accounts](https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve)
*   [Billing migration within Stripe accounts](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#within-Stripe-accounts)

*   [Set up a Stripe Billing integration](https://docs.stripe.com/billing/subscriptions/build-subscriptions)
*   [Copy PAN data across Stripe accounts](https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve)
*   [Billing migration within Stripe accounts](https://docs.stripe.com/billing/subscriptions/import-subscriptions-toolkit#within-Stripe-accounts)
