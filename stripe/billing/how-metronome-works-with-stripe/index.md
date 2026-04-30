---
title: "How Metronome works with Stripe"
source: "https://docs.stripe.com/billing/how-metronome-works-with-stripe"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:10:06.859Z"
content_hash: "92000ffa0939788f9741ba9e5a7cb91fdad70a9d0adf67ee4ef72742af4f8b6e"
---

Metronome and Stripe provide end-to-end billing for advanced pricing models. Metronome handles usage-based billing, credit-based pricing, enterprise contracts, and multi-dimensional rating. Stripe handles payment collection, tax calculation, revenue recognition, data export, and helps screen for fraud with [Radar](https://docs.stripe.com/radar).

Your billing model and growth strategy inform how you choose to integrate Metronome with Stripe.

## Metronome-supported billing models

Metronome supports billing models for both product-led growth (PLG) and sales-led growth (SLG) strategies. You can combine these models to serve different customer segments and lifecycle stages within a single system.

### Self-serve and PLG models

*   Pure usage-based billing with automatic collection
*   Prepaid credit wallets with usage burn-down
*   Auto-recharge when balances drop below a threshold
*   Payment-gated credit purchases where credits release only on successful payment
*   Spend threshold models that cap exposure and reduce surprise bills
*   Subscription lifecycles including trials, tier upgrades and downgrades, and hybrid prepaid-plus-overage

See [Prepaid balance thresholds](https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/prepaid-balance-thresholds) and [Create a prepaid commit](https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit).

### Sales-led and enterprise models

*   Postpaid commits with minimum spend agreements and true-up invoicing for overages
*   Prepaid enterprise commits with burn-down and overage billing
*   Usage-based invoicing with net terms
*   Multi-wallet credit architectures with priority rules across scopes (for example, per-user pool first, then organization-level commit)
*   Multi-entity and multi-Stripe configurations for regional or contract-specific setups

See [Enterprise commit](https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/enterprise-commit) and [Create products and contracts](https://docs.metronome.com/guides/get-started/core-concepts/create-products-contracts).

Many companies run both growth strategies in parallel, for example, starting users on a free trial with spend thresholds, converting to prepaid credits with auto-recharge, and graduating enterprise customers to committed contracts. For in-depth walkthroughs, see [Billing model guides](https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/guides-home).

## Integration patterns

Metronome can operate in two ways alongside Stripe:

*   **Metronome independently**: Metronome handles all billing and metering, and pushes finalized invoices to Stripe for payment collection.
*   **Metronome with Stripe Subscriptions**: Stripe Subscriptions handles your recurring seat-based or flat-rate billing. Metronome runs alongside it, handling usage-based metering and billing separately. Both systems create invoices on the same Stripe Customer.

Both patterns use the same mechanism: Metronome pushes [finalized invoices](https://docs.metronome.com/integrations/invoice-integrations/stripe) to Stripe through the [Invoicing API](https://docs.stripe.com/api/invoices). This invoicing sync is one way, meaning Stripe doesn’t send invoice data back to Metronome. For more information, see [How invoicing works](https://docs.metronome.com/guides/get-started/core-concepts/how-invoicing-works).

For all Metronome invoices pushed to Stripe, Stripe payment status syncs back to Metronome automatically.

### When to choose each pattern

Choose **Metronome independently** if you’re migrating from an existing usage-based billing system, or starting from scratch. This pattern gives you the full range of Metronome’s billing platform features but requires custom integration work for some Stripe surfaces like Checkout. For architecture planning guidance, see [Planning your billing architecture](https://docs.metronome.com/guides/implement-metronome/planning-your-billing-architecture).

Choose **Metronome with Stripe Subscriptions** if you already use Stripe Subscriptions for recurring billing and want to add usage-based pricing alongside it. Your existing subscription flows (including Checkout, Adaptive Pricing, and Payment Links) continue to work as-is, and Metronome handles the usage metering and invoicing separately.

### Metronome independently

You send usage events to Metronome. Metronome processes them through metering, rating, and contract logic, then finalizes the invoices and pushes them to Stripe through the Invoicing API. Stripe handles payment collection, tax, revenue recognition, and reporting.

### Metronome with Stripe Subscriptions

Stripe Subscriptions manages your recurring pricing. Customers sign up through your existing flow (Checkout, Payment Links, or API). Separately, you send usage events to Metronome. Metronome processes them and pushes usage invoices to Stripe on the same Stripe Customer. The customer receives both subscription invoices (from Stripe) and usage invoices (from Metronome).

#### Configure Metronome with Stripe Subscriptions

1.  Determine when Metronome customers are created. The most common pattern is to create these objects when a new subscription is created in Stripe. Stripe [sends webhooks](https://docs.stripe.com/billing/subscriptions/webhooks) for these events that you can use to prompt creation in Metronome. Make sure the Stripe Customer ID is added to the Metronome customer.
2.  After the customer is created, create a contract with the associated credits or commits added (if applicable).
3.  Begin sending usage for the new customer. Metronome collects, aggregates, and rates the usage according to the contract and rate card.
4.  Any non-zero invoices are automatically forwarded to Stripe at the end of the billing period for these customers.

## Stripe product interoperability

Stripe product

Support level

Notes

[Invoicing](https://docs.stripe.com/invoicing)

Fully supported

Metronome invoices become standard Stripe invoices. Manages accounts receivable, collections, and dunning.

[Tax](https://docs.stripe.com/tax)

Fully supported

Calculates tax at invoice finalization. Also supports [Anrok](https://docs.metronome.com/integrations/tax-integrations/anrok) and [Avalara](https://docs.metronome.com/integrations/tax-integrations/avalara).

[Payments](https://docs.stripe.com/payments)

Fully supported

Processes payments, retries with [Smart Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries), screens fraud with [Radar](https://docs.stripe.com/radar).

[Revenue Recognition](https://docs.stripe.com/revenue-recognition)

Fully supported

Generates ASC 606 / IFRS 15 schedules. No additional configuration needed.

[Data Pipeline and Sigma](https://docs.stripe.com/stripe-data)

Partially supported

Queries Stripe invoice, charge, and payment data. Metronome-specific data (metering events, contract state, credit ledgers) requires [Metronome data export](https://docs.metronome.com/guides/reporting-insights/data-export/overview).

[Checkout](https://docs.stripe.com/payments/checkout)

Requires custom integration

Checkout is designed for subscription signups and one-time payments. Metronome invoices use Stripe’s invoice payment flows (automatic charge or hosted invoice page), not Checkout.

[Adaptive Pricing](https://docs.stripe.com/payments/currencies/localize-prices/adaptive-pricing)

Not directly applicable

Adaptive Pricing converts prices at checkout time. Metronome invoices arrive with amounts already calculated.

We’re actively increasing interoperability with Stripe.

## Metronome concepts for Stripe developers

Stripe analog

Metronome concept

Definition

[Meter](https://docs.stripe.com/api/billing/meter)

[Billable metric](https://docs.metronome.com/guides/get-started/core-concepts/create-billable-metrics)

Defines how to count customer usage (API calls, tokens, GB-hours). Supports SUM, COUNT, MAX, UNIQUE.

[Price](https://docs.stripe.com/api/prices)

[Rate](https://docs.metronome.com/guides/get-started/core-concepts/create-manage-rate-cards)

A price mapped to a billable metric through a **Rate Card**, a reusable pricing template.

[Subscription](https://docs.stripe.com/api/subscriptions) (loosely)

[Contract](https://docs.metronome.com/guides/get-started/core-concepts/create-products-contracts)

Enterprise agreement defining rate cards, commits, credits, and schedules.

[CreditGrant](https://docs.stripe.com/api/billing/credit-grant)

[Prepaid commit](https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/create-a-pre-paid-commit)

Upfront payment for committed usage. Credits draw down over time.

No direct analog

[Postpaid commit](https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/enterprise-commit)

Minimum spend agreement. True-up invoice if usage falls short.

[Credit balance](https://docs.stripe.com/api/billing/credit-balance-summary)

[Credit ledger](https://docs.metronome.com/api-reference/credits-and-commits/list-balances)

Tracks credit balances, drawdowns, expirations, and rollovers.

No direct analog

[Threshold billing](https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/prepaid-balance-thresholds)

Auto-recharge when credit balance drops below a threshold.

No direct analog

[Dimensional pricing](https://docs.metronome.com/guides/pricing-packaging/overview)

Price varies by attribute dimensions on the same metric.

## Invoice lifecycle

The invoice lifecycle is the same for both integration patterns:

1.  **Invoice finalization**: At the end of a billing period (or on a contract schedule), Metronome computes and finalizes an invoice.
2.  **Line item creation**: Metronome creates [InvoiceItem](https://docs.stripe.com/api/invoiceitems) objects on the Stripe Customer through the Stripe API. All line items are created before the Invoice object itself, so downstream listeners (tax providers, webhooks) see a complete invoice on creation.
3.  **Invoice creation**: Metronome calls [POST /v1/invoices](https://docs.stripe.com/api/invoices/create) on the Stripe Customer, which automatically attaches all pending line items.
4.  **Validation**: Metronome validates that the Stripe invoice total matches the Metronome invoice total within a rounding tolerance.
5.  **Finalization**: Depending on configuration, invoices are either auto-finalized or left in draft status for manual review. If a tax provider (Stripe Tax, Anrok, or Avalara) is configured, finalization might be deferred until the tax provider applies tax.
6.  **Webhook consumption**: Metronome listens for Stripe webhooks (`invoice.finalized`, `invoice.paid`, `invoice.payment_failed`, `invoice.payment_succeeded`, `invoice.voided`, `invoice.marked_uncollectible`, `invoice.deleted`) to track payment status and update invoice records. For the complete webhook-to-status mapping, see [Stripe invoice status tracking](https://docs.metronome.com/integrations/invoice-integrations/stripe#track-stripe-invoice-statuses-in-metronome).

### Invoice attributes

The following table shows which system controls each invoice attribute after Metronome pushes an invoice to Stripe:

Invoice attribute

Controlled by

Line items (names, quantities, unit amounts)

Metronome

Sub-line item breakdowns (tiered pricing, presentation group keys)

Metronome (configurable through [group keys](https://docs.metronome.com/guides/get-started/core-concepts/create-products-contracts#group-keys))

Invoice metadata (`metronome_invoice_id`, `client_id`, `environment`)

Metronome ([entity mapping rules](https://docs.metronome.com/integrations/invoice-integrations/stripe#create-optional-entity-mapping-rules))

Service period dates on line items

Metronome

Collection method (`send_invoice` or `charge_automatically`)

[Configurable per customer](https://docs.metronome.com/integrations/invoice-integrations/stripe#set-the-customer-billing-configuration)

Days until due (for example, Net 30)

[Configurable per customer](https://docs.metronome.com/integrations/invoice-integrations/stripe#configure-optional-global-integration-settings-available)

Draft or auto-finalize behavior

[Account-level configuration](https://docs.metronome.com/integrations/invoice-integrations/stripe#configure-optional-global-integration-settings-available)

Tax calculation

[Stripe Tax](https://docs.metronome.com/integrations/tax-integrations/stripe-tax), [Anrok](https://docs.metronome.com/integrations/tax-integrations/anrok), or [Avalara](https://docs.metronome.com/integrations/tax-integrations/avalara) (applied after Metronome creates line items)

Payment method, Radar fraud screening, [Smart Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries)

Stripe

Invoice presentation, branding, header/footer

Stripe

Invoice available payment methods

Stripe

## Payments

After a Metronome invoice is finalized in Stripe, the following Stripe Payments features are available:

*   **Automatic collection**: Uses the customer’s default payment method. Metronome supports both `charge_automatically` (Stripe charges the payment method) and `send_invoice` (Stripe emails the customer) [collection methods](https://docs.metronome.com/integrations/invoice-integrations/stripe#set-the-customer-billing-configuration).
*   [**Smart Retries**](https://docs.stripe.com/billing/revenue-recovery/smart-retries): Stripe uses machine learning to choose optimal retry times for failed payments.
*   [**Dunning and revenue recovery**](https://docs.stripe.com/billing/revenue-recovery): Stripe sends failed-payment emails and handles the retry lifecycle. Enable [Stripe’s dunning and revenue recovery](https://docs.stripe.com/billing/revenue-recovery) on your Stripe account to automate failed-payment follow-up.
*   **Radar**: Screens for fraud on card payments.
*   **Global payment methods**: All payment methods supported by Stripe Invoicing are available (cards, ACH, SEPA, wire, and others).
*   **Payment method management**: Stripe is the system of record for customer payment methods.

### Payment-gated commits

Metronome supports [payment-gated commits](https://docs.metronome.com/guides/pricing-packaging/apply-credits-and-commits/manual-payment-gated-commits) (including [threshold billing and auto-recharge](https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/prepaid-balance-thresholds)), where a Stripe invoice must be paid before credits are released. This includes support for ACH with a 13-day payment window.

If a payment-gated auto-recharge payment fails, Metronome voids the invoice and disables the contract’s auto-recharge. You follow up with the customer and manually re-enable the contract. For the complete workflow, see [Prepaid balance threshold](https://docs.metronome.com/guides/customers-billing/optimize-customer-experience/prepaid-balance-thresholds).

### Payment failures

Metronome tracks Stripe invoice payment status through webhooks. Stripe handles payment collection and retry logic. The failure path depends on how the invoice is configured:

*   **`charge_automatically` invoices**: Stripe owns the retry cycle. If [Smart Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries) are enabled, Stripe uses machine learning to choose optimal retry times (up to 8 attempts within a configurable window). Metronome receives `invoice.payment_failed` and updates the invoice status to `PAYMENT_FAILED`, but takes no retry action.
*   **`send_invoice` invoices**: Stripe emails the invoice to the customer with payment instructions. If payment isn’t received by the due date, the invoice remains in open status in Stripe. Metronome tracks the status, but payment reminders and follow-up are handled by Stripe’s [dunning and revenue recovery](https://docs.stripe.com/billing/revenue-recovery).
*   **Payment-gated threshold billing**: If a payment-gated auto-recharge invoice fails, Metronome sets the contract’s `is_enabled` field to false and voids the invoice. You then need to re-enable the threshold billing before it can be dispatched.

Metronome fires `invoice.billing_provider_error` webhooks when there’s an error sending an invoice to Stripe (for example, the Stripe customer doesn’t exist or lacks a valid payment method). Errors that occur entirely within Stripe are reported through [Stripe webhooks](https://docs.stripe.com/webhooks) directly. For the full list of Metronome events, see [Metronome webhook types](https://docs.metronome.com/guides/platform-configuration/setup-webhooks).

### Post-invoice operations

After Metronome pushes an invoice to Stripe, you manage the following operations directly in Stripe or your other systems (for example, your ERP or CRM):

*   **Refunds**: Process refunds in Stripe through the Dashboard or [Refunds API](https://docs.stripe.com/refunds), your ERP, or your CRM. To credit future billings within Metronome, see [Issue credit memos](https://docs.metronome.com/guides/invoices/invoice-optimization/issue-credit-memos).
*   **Invoice adjustments**: Use the [Metronome Credits API](https://docs.metronome.com/api-reference/credits-and-commits/create-a-credit) to issue a credit, then void and regenerate the invoice in Metronome and resync it to Stripe.
*   **Invoice voiding**: Metronome and Stripe maintain independent invoice records. Void the invoice in both systems (and any other downstream system) to keep records in sync.

## Get started

1.  **Plan your billing architecture**: Determine whether to use Metronome independently or as a usage sidecar. See [Planning your billing architecture](https://docs.metronome.com/guides/implement-metronome/planning-your-billing-architecture).
2.  **Connect Metronome to Stripe**: Follow [Invoice with Stripe](https://docs.metronome.com/integrations/invoice-integrations/stripe).
3.  **Configure tax**: Set up [Stripe Tax](https://docs.metronome.com/integrations/tax-integrations/stripe-tax), [Anrok](https://docs.metronome.com/integrations/tax-integrations/anrok), or [Avalara](https://docs.metronome.com/integrations/tax-integrations/avalara).
4.  **Enable Smart Retries**: [Enable Smart Retries](https://docs.stripe.com/billing/revenue-recovery/smart-retries) to maximize payment success rates.
5.  **Set up data exports**: Configure [Metronome data export](https://docs.metronome.com/guides/reporting-insights/data-export/overview) and [Data Pipeline](https://docs.stripe.com/stripe-data/access-data-in-warehouse).
6.  **Listen for webhooks**: Set up listeners for [Metronome webhooks](https://docs.metronome.com/guides/platform-configuration/setup-webhooks) and [Stripe webhooks](https://docs.stripe.com/webhooks).
7.  **Review the production checklist**: See the [Metronome production checklist](https://docs.metronome.com/guides/implement-metronome/production-checklist).

## See also

*   [How Metronome works](https://docs.metronome.com/guides/get-started/how-metronome-works)
*   [API quickstart](https://docs.metronome.com/guides/get-started/api-quickstart)
*   [Billing model guides](https://docs.metronome.com/guides/pricing-packaging/billing-model-guides/guides-home)
*   [Metronome API reference](https://docs.metronome.com/api-reference/introduction)
