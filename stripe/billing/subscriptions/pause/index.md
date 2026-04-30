---
title: "Pause subscriptions"
source: "https://docs.stripe.com/billing/subscriptions/pause"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:23:25.232Z"
content_hash: "c8bbaa64ce1f95ce7e2ebfa1200bd8dbc49dc5ae9bf1dc5ad38c4ae3aa297727"
---

Pausing a subscription lets you temporarily suspend both service delivery and invoice generation. The ability to pause a subscription helps you support customer scenarios such as vacations, temporary non‑usage, or goodwill pauses to prevent churn.

To use the Pause subscription endpoint, the subscription must use [flexible billing mode](https://docs.stripe.com/billing/subscriptions/billing-mode).

## Interested in getting early access to the Pause subscription endpoint?

With the Pause subscription endpoint, you can temporarily suspend servicing and invoicing. Provide your email for private preview access.

Other similar pause behaviors currently supported on a subscription are:

*   [Pause payment collection](https://docs.stripe.com/billing/subscriptions/pause-payment): Service delivery and invoice generation continue, but collection on invoices is paused.
*   [Pause on free trial-end without a payment method](https://docs.stripe.com/billing/subscriptions/trials/free-trials#create-free-trials-without-payment): The trial-end pause behaves more like a true pause, but it only applies to a specific, system-triggered scenario.

The ability to pause subscriptions is useful for:

*   Merchant teams that want API control over subscription lifecycle without canceling subscriptions.
*   Backend engineers building retention flows or support tooling that needs a true pause state.
*   Developers validating billing, entitlement revocation, and webhook handling for paused windows.

You can pause subscriptions with the Pause subscription endpoint. The pause takes effect immediately. After a subscription is paused:

*   The subscription status updates to `paused`.
*   You get notified about the status change via the [customer.subscription.paused](https://docs.stripe.com/api/events/types#event_types-customer.subscription.paused), [customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated), and [entitlements.active\_entitlement\_summary.updated](https://docs.stripe.com/api/events/types#event_types-entitlements.active_entitlement_summary.updated) webhooks, enabling you to de-provision service delivery accordingly.
*   Invoice generation is paused for the entire pause duration, though existing subscription invoices advance without affecting the paused status.
*   The [current\_period\_end](https://docs.stripe.com/api/subscriptions/object#subscription_object-items-data-current_period_end) updates to the time when you paused the subscription.
*   You can use the `bill_for` parameter to control billing behavior at pause time, including creating credit prorations for unused licensed time and creating debits for metered usage in the current period. You can invoice immediately or create pending invoice items.

You can’t pause a subscription if it:

*   Uses [send\_invoice](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method) collection
*   Uses billing mode [classic](https://docs.stripe.com/api/subscriptions/object#subscription_object-billing_mode-type)
*   Is in a trial period, has an attached trial offer, or has been canceled
*   Has an attached [schedule](https://docs.stripe.com/billing/subscriptions/subscription-schedules)
*   Has an attached [cadence](https://docs.stripe.com/api/v2/billing-cadences?api-version=preview)

Similarly, you can’t attach a schedule or cadence to a paused subscription.

If you pause a subscription that uses a coupon, the coupon retains its original validity and the pause doesn’t extend its duration.

This example demonstrates how to use the API to immediately pause an active subscription:

`curl https://api.stripe.com/v1/subscriptions/sub_1234567890/pause \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: preview" \  -d type=subscription \  -d "bill_for[unused_time_from][type]=now" \   -d "bill_for[outstanding_usage_through][type]=now" \   -d invoicing_behavior=pending_invoice_item`

The customer portal reflects that a subscription is paused, but your subscribers can’t use it to pause subscriptions themselves.

## Resume subscriptions

You need to manually resume the subscription using the [API](https://docs.stripe.com/api/subscriptions/resume?api-version=preview). Resume is only available on subscriptions that use [charge\_automatically](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method) collection. If resuming doesn’t generate an invoice, the subscription status updates to `active` immediately. If resuming generates an invoice, Stripe finalizes the invoice immediately but doesn’t attempt payment in-request. You must attempt payment manually using the [Pay invoice endpoint](https://docs.stripe.com/api/invoices/pay).

*   If payment succeeds, the subscription status updates to `active`.
*   If payment fails, the subscription status updates to `past_due`.
*   If you don’t attempt payment within 23 hours, the invoice is voided and the subscription status stays `paused`.

After a subscription’s status updates to `active`:

*   Invoicing resumes.
*   The billing cycle anchor is optionally reset.
*   You get notified about the status change via the [customer.subscription.resumed](https://docs.stripe.com/api/events/types#event_types-customer.subscription.resumed), [customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated), and [entitlements.active\_entitlement\_summary.updated](https://docs.stripe.com/api/events/types#event_types-entitlements.active_entitlement_summary.updated) webhooks, enabling you to re-provision service delivery accordingly.

This example demonstrates how to immediately resume a paused subscription using the API:

`curl https://api.stripe.com/v1/subscriptions/sub_1234567890/resume \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: preview" \  -d billing_cycle_anchor=unchanged \  -d proration_behavior=create_prorations`

## Identify pause and resume events

Stripe sends the following events for paused and resumed subscriptions.

Example webhook payload for `customer.subscription.paused` (key fields shown):

`{   "id": "evt_1SrpXjRnJ89Z4rKkFxe9waAz",   "object": "event",   ...   "data": {     "object": {       "id": "sub_1SrpWtRnJ89Z4rKknfSwXkBc",       "object": "subscription",       ...       "latest_invoice": "in_1SrpWtRnJ89Z4rKkzYBCF1MY",       ...       "status": "paused",       ...     }   },   ...   "type": "customer.subscription.paused" }`
