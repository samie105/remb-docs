---
title: "Modify subscriptions"
source: "https://docs.stripe.com/billing/subscriptions/change"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:17:46.199Z"
content_hash: "263d59fd7f3740bb7aca59b970657e741c50818acf71a7d24d05503e83f882d7"
---

You can change existing subscriptions without having to cancel and recreate them. Set up the [customer portal](https://docs.stripe.com/customer-management) to let your customers manage their own subscriptions and billing details through a Stripe-hosted page.

For changes that automatically create a new [subscription invoice](https://docs.stripe.com/billing/invoices/subscription), use [pending updates](https://docs.stripe.com/billing/subscriptions/pending-updates) so that the updates are only applied if the new invoice is successfully paid.

## Billing impacts

Not all subscription changes affect billing or generate prorations:

*   _Billing-related updates_ create prorations and can generate invoices. These include changing prices, quantities, billing periods, or adding or removing subscription items.
*   _Non-billing updates_ apply immediately without prorations. These include updating metadata, payment methods, tax settings, or [applying or removing discounts](https://docs.stripe.com/billing/subscriptions/coupons#update-a-subscription).

To see billing impacts before making changes, [preview prorations](https://docs.stripe.com/billing/subscriptions/prorations#preview-proration).

### Configuration updates

Configuration updates, like metadata and payment methods, don’t generate invoices with `proration_behavior=always_invoice` because they don’t change the amount owed for the current billing period. For a complete list, see [What doesn’t trigger prorations](https://docs.stripe.com/billing/subscriptions/prorations#no-prorations).

### Discounts

Updating only coupons or promotion codes doesn’t create proration invoice items. The new discount applies to the next invoice.

However, if you combine a non-prorating discount change with a proration-triggering update in the same API call (for example, changing an item quantity and modifying a discount), Stripe calculates the proration using the updated discount state. See [Discount changes and prorations](https://docs.stripe.com/billing/subscriptions/prorations#discount-changes-and-prorations) for details.

## Use cases
