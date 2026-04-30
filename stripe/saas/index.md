---
title: "Integrate a SaaS business on Stripe"
source: "https://docs.stripe.com/saas"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:12:26.762Z"
content_hash: "35abe9ebb95dc3d4abedfa98798cc1121bc0801c503ae863ae95358afa2ace98"
---

Many Stripe users have a SaaS business model that involves subscriptions or recurring payments. This guide describes the unique actions you need to take in your Stripe integration to support typical SaaS business models. To help get you started more quickly, this guide presents no-code options where available.

## Product modeling

Set up pricing structures for different products. Stripe Billing supports many types of pricing models, including:

*   Flat rate-Good-better-best
*   Per-seat
*   Usage-based pricing
*   Tiered pricing
*   Multiple prices
*   Multiple products in a subscription

Learn more about [product modeling](https://docs.stripe.com/products-prices/pricing-models).

## Display pricing information

The pricing table is an embeddable UI component that displays pricing models for different subscription options. With pricing tables, customers can view pricing information and select a subscription. After selecting a subscription, they can complete the purchase with Stripe Checkout. Learn more about [pricing tables for SaaS businesses](https://docs.stripe.com/payments/checkout/pricing-table).

![Pricing table is an embedded UI that displays pricing information and takes customers to Checkout.](https://b.stripecdn.com/docs-statics-srv/assets/pricing-table-embed.b27a06fcd84b57a8866a8b4b62323fdc.png)

Embed a pricing table on your website to display pricing details and convert customers to checkout.

## Enable discounts

Use discounts to acquire new subscribers. You can create coupons and apply them to a subscription or create a customer-facing promotion code that customers can apply at checkout. Learn more about [discounts for subscriptions](https://docs.stripe.com/billing/subscriptions/coupons).

## Offer trials

Let customers try your product before subscribing. With Stripe Checkout, they can sign up for a trial without submitting payment information. You can configure a subscription to automatically send a reminder email when the trial is about to expire. Learn more about [trials](https://docs.stripe.com/payments/checkout/free-trials).

## Manage subscriptions

The customer portal lets customers manage their subscriptions in a self-serve environment where they can:

*   Update their subscription
*   Cancel their subscription
*   Add or update a payment method
*   Update billing and shipping information
*   Review their invoice history

Learn more about [integrating the customer portal](https://docs.stripe.com/customer-management).

![Customer portal](https://b.stripecdn.com/docs-statics-srv/assets/customer-portal.c7a8337f3b8ef35b9c55595187508996.png)

Customer portal

## Set up invoices

Invoices represent how much money a customer owes, and Stripe automatically generates one for every subscription billing period. You can also create an invoice manually for custom deals or one-time payments. When an invoice is due, Stripe tries to collect payment by either automatically charging the payment method on file, or emailing the invoice. Learn more about [invoices](https://docs.stripe.com/invoicing).

![Hosted Invoice Page](https://b.stripecdn.com/docs-statics-srv/assets/hosted-invoice-page-guide.df3cc5a1e4180c338269aacdfa792180.png)

Hosted Invoice Page

[

## Monitor subscription activity



](#monitor)

Monitor subscriptions in the Dashboard or set up webhook endpoints and listen for events. Learn more about [subscriptions and webhooks](https://docs.stripe.com/billing/subscriptions/webhooks).

You can also use [Affiliate and referral Stripe Apps](https://marketplace.stripe.com/categories/affiliate_and_referrals) to set up and manage referral and affiliate programs with Stripe, get customer information, and automate commission adjustments from the Stripe Dashboard.

## Reduce involuntary churn

Use recovery tools like Smart Retries and reminder emails to recover revenue that would be lost to involuntary churn. Learn more about [revenue recovery tools](https://docs.stripe.com/billing/revenue-recovery).

## Manage sales tax

After you register to collect taxes, Stripe Tax determines your customer’s location, and automatically calculates and collects the correct amount of tax at checkout. Stripe Tax supports sales tax, VAT, and GST. Learn more about [Stripe Tax](https://docs.stripe.com/tax).

## Automate revenue recognition

Use Stripe Revenue Recognition to automate revenue reporting and stay compliant with rules for accrual accounting. Stripe Revenue Recognition automates revenue accounting based on your payments and billing transactions.

Learn more about [Revenue Recognition](https://docs.stripe.com/revenue-recognition).

## Test your integration

Test your integration to make sure it behaves as you expect. With simulations, you can simulate how a subscription integration would handle events such as trials and payment failures over a billing period. Learn more about [testing subscriptions integrations](https://docs.stripe.com/billing/testing).
