---
title: "Sales-led B2B billing"
source: "https://docs.stripe.com/billing/subscriptions/sales-led-billing"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:26:26.902Z"
content_hash: "503ad19cab8aafc6f1cff866adb8c3f550f9e13b5e9c6946e8d929526a709133"
---

Stripe Billing enables you to set up and automate workflows for your sales team. This guide explains how to model complex sales contracts, use Quotes to negotiate them with your customers, create sales-negotiated deals in the Stripe Dashboard, and update or renew such contracts. If a feature in this guide doesn’t have a Beta label, then it’s publicly available.

## Request early access

## Interested in getting early access to Sales-led B2B billing features?

Sales-led B2B billing features provide enhanced capabilities for enterprise billing workflows, including custom pricing, contract management, and advanced invoicing options. Provide your email below for private preview access.

## Overview

Sales-led B2B billing features allow sales-focused businesses to track and manage sales and fulfillment processes end-to-end. A typical sales deal flow is an iterative process that lasts as long as the lifecycle of your customer. It starts with a quote that the sales team creates and finalizes with the customer. After finalizing the quote, your team shapes the deal in Stripe Billing. Throughout the lifecycle of the deal, events like end of term renewals, upselling new products, and amending mid-cycle changes require you to make changes to the existing deal or create a new one. Using the Stripe sales-led B2B billing features, you can automate and manage the end-to-end deal flow within Stripe.

See the following diagram for a visual representation of a common deal lifecycle.

![Deal flow](https://b.stripecdn.com/docs-statics-srv/assets/deal-flow.5b5d78bfd1e971b5143da8f450c506bf.png)

## Model your contract

Quotes allow you to deliver estimated pricing for requested sales deals and can help facilitate negotiation before beginning a subscription or invoice. You can offer pre-sales deal pricing by creating a quote for the customer. Whether your sold deal requires a single invoice, a subscription, or a multiphase ramp up deal, use quotes to provide your customers with a price estimate, including any discounts or taxes.

Your sales team can start drafting a quote in the Stripe dashboard or automate the creation of one using the Stripe API. The quote remains in draft mode during the initial negotiation. After you finalize the quote you can send it to the customer for approval. Upon approving the quote, your sales team can convert the approved quote to a deployed deal containing a subscription, invoice, or multiphase installment plan.

You don’t use quotes exclusively during the initial deal creation process. You also use quotes when customers renew, buy additional products mid-cycle (upsell), or request changes to their existing deals. In all of these scenarios, the sales team typically negotiates a new quote and uses the approved quote to apply an amendment to the existing deal or create a new deal. These functionalities work directly with Stripe subscriptions, subscription schedules, and invoices to provide flexibility with building a complex deal process.

Learn more about some of the existing Stripe [quote functionalities](https://docs.stripe.com/quotes) and sign up in the [form above](#request-early-access) to get access to some of the more advanced deal flow quoting capabilities.

If you’re using a third-party quoting tool to create and finalize your quotes, you can use one of our [apps](https://docs.stripe.com/use-stripe-apps) to create your sold deals within Stripe. For example, the [Stripe Billing app for Salesforce](https://docs.stripe.com/use-stripe-apps/stripe-app-for-salesforce/overview) enables your sales team to manage subscriptions on Stripe directly on Salesforce.

### Model your pricing

Using Stripe Products and Prices, you can model your subscription pricing model and one-off charges. Both subscriptions and invoices work with Products and Prices. In many sales deal scenarios, the sales team overrides the original price based on the negotiated deal. Ad-hoc prices allow your team to override predefined prices. If you already have a product catalog in another system, you can also [import that product catalog](https://docs.stripe.com/products-prices/manage-prices#import-products-prices) into Stripe using the API.

## Create a contract

Sales deals can become very complex. You might have billing period durations with different pricing models, discounts, and advanced fee structures. A simple scenario is when you ramp up your pricing over a period of three years. Stripe Billing’s [subscription schedules](https://docs.stripe.com/billing/subscriptions/subscription-schedules) enable your sales team to create these deals. Your subscriptions can be basic flat rate monthly deals or complex multi-year ramp ups.

The following sections describe some of the sales-led B2B billing capabilities for creating a sales deal.

### Create contract subscriptions

Stripe’s sales-led B2B billing features work on top of Stripe Billing, our subscriptions platform. Stripe Billing allows you to create subscriptions and update different aspects of subscriptions, such as the billing period and the subscription price. You can use subscription schedules to automate these updates over time. Subscription schedules are made up of phases that define how and when changes to a subscription occur. For example, you can set a subscription schedule to begin a subscription on a future date. Here is a quick video of how to create complex multi-phase subscription schedules using the Stripe Billing dashboard:

Subscription schedules in the Dashboard

### Create contract invoices

Stripe’s sales-led B2B billing features also work on top of Stripe Invoicing, allowing you to [create invoices](https://docs.stripe.com/invoicing) with complex fee structures, automated sales taxes, and due date modifications. Converting a quote automatically creates an invoice. You can also create them manually from the Stripe Dashboard. After you create the invoice, you can also send the invoice link to your users to pay it through a hosted invoice page. Stripe Invoicing automates the email reminders for any past due and failed payments.

### Prebill customers in advance Beta

Some customers pay for a certain number of billing periods when they sign the deal. Sales prebills the customer when the deal is created. Using the Stripe prebilling feature, you can charge customers for more than the next service period. This enables use cases such as charging customers up front for their first 3 months when they sign up for your service, or charging early for an upcoming renewal.

A prebilled subscription continues to cycle naturally, but no invoices are generated based on the recurring price until the prebilled period has ended. Prebilling creates an invoice immediately with the current period plus the number of additional cycles to collect up front. Afterward, a prebilled subscription continues to cycle naturally. One-off subscription invoices are generated at the time of renewal if pending invoice items are created during the prebilled period.

### Offer trials and discounts Beta

Sales teams often offer trials and discounts during deal negotiations to incentivize customers. You can offer free time-based trials such as a 14-day free trial before sending the invoices, or paid trials that have a promotional price for the first 2 months of the deal.

### Additional discount features

You can apply multiple discounts to each phase of a given subscription. You can also apply discounts at a line-item level for each price-point you sell.

## Update a contract Beta

Deals get updated often. For example, the customer might be approaching the end of the deal and need a renewal plan, they might be buying a new product soon after the closing, or requesting a change to the originally agreed upon contract. All of these reasons cause sales teams to create an amendment. Amendments allow your sales team to apply updates to deals without managing the complex changes that need to happen to every phase of the subscription. You can apply amendments directly to an existing deal or apply them through a new quote agreement.

Changes to a deal such as upgrading or downgrading can result in prorated charges. You can configure your deal to enable proration charges when you apply amendments. You can also decide to handle prorations differently for different phases of the deal using Stripe’s advanced proration features.

You can prebill customers, offer different trials, and apply additional discounts during the deal update process. Your sales team can apply these changes from the Stripe Dashboard or automate it through our [third-party apps](https://docs.stripe.com/use-stripe-apps).

## Let customers manage invoices and subscriptions

You can use the Stripe customer portal as a no-code way to manage subscriptions and invoices. You can configure the customer portal to allow certain subscription management features for your customers. After you create and amend deals, customers can go to the customer portal to manage their payment method, download invoices, and pay invoices. Your sales team can share a direct link to the customer portal with your customers or your product team to integrate it inside your SaaS application.

You can also use the Stripe API and webhooks to automatically apply the deal updates inside your SaaS app or sync with third-party tools.

## Migrate old deals to new pricing Beta

If you have deals that you need to update to a new pricing model, it might be time consuming to update those deals manually. With the price migration toolkit, you can migrate all or a portion of your existing deals to new pricing models.

If you have subscriptions from other sources, like an internal homegrown billing system or a third-party billing solution, you can [import them into Stripe Billing](https://docs.stripe.com/billing/subscriptions/migrate-subscriptions). If you’re also moving payment processors from a third-party to Stripe Payments, you can use our data migration process to request a migration on your behalf. To request support on data migration, contact [billing-migrations@stripe.com](mailto:billing-migrations@stripe.com).

## Billing features

Here’s a list of Stripe’s sales-led B2B billing capabilities. If you’re interested in getting early access to some of these beta features, you can sign up in the [form above](#request-early-access).

Component

Description

**Quotes**

Use [quotes](https://docs.stripe.com/quotes) to combine recurring and one-off line items so you can provide your customers with a price estimate, including any discounts or taxes.

**Advanced multi-phase quotes**

Beta

Create quotes with multiple phases that correspond to your sales process phases.

**Invoices**

Use [Stripe Invoicing](https://docs.stripe.com/invoicing) to create, customize, and send invoices to customers. Automatically charge your customer’s payment method on file, or email them the invoice with or without a link to a payment page.

**Hosted invoice page**

Use the [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page#set-payment-methods) to securely collect payment from your customers. From the Hosted Invoice Page, you can configure invoices to allow payment with one or more of the [supported payment methods](https://docs.stripe.com/invoicing/payment-methods).

**Subscriptions**

Create subscriptions and multi-phase subscription schedules to model your complex deal flow.

**Prebilling**

Beta

Prebill customers ahead of schedule. Prebilling lets you charge customers in advance for upcoming billing periods.

**Advanced discounts**

Beta

Apply multiple discounts to subscriptions or individual line items.

**Prorate scheduled changes upfront**

Beta

By default, prorations might occur when the subscription is updated. When updates are scheduled for the same billing period, simplify prorations by prorating for all the scheduled changes up front rather than every time the updates happen.

**Price migrations**

Beta

Use price migration to move customers from an old pricing model to a new pricing model.

**Amendments**

Beta

Use amendments to update an existing multi-phase contract.

**Paid trials**

Beta

Charge a fee for trial days.

**Customer portal**

Let your customers manage their subscriptions through a Stripe-hosted [customer portal](https://docs.stripe.com/customer-management) without writing any code.
