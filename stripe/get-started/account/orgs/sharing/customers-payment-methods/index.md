---
title: "Share customers and payment methods across accounts in an organization"
source: "https://docs.stripe.com/get-started/account/orgs/sharing/customers-payment-methods"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:42:35.249Z"
content_hash: "7bd0f35dcf970acd4fb791e2707de1927e991cb3af541207b2c200b1007dcd90"
---

Many growing businesses expand to multiple Stripe accounts to keep finances from different business lines separate, or because the business operates in multiple regions with different legal entities. As a multi-entity business, you can share customers and payment methods across accounts in an organization to avoid:

*   Recollecting payment methods or contact information multiple times from the same customer
*   Introducing inconsistencies in a customer’s contact and payment details between accounts
*   Maintaining and updating duplicate records

## Interested in sharing customers and payment methods across your organization?

Provide your email address to request access.

## Limitations

Customer and payment method sharing is currently in [public preview](https://docs.stripe.com/release-phases) with the following restrictions:

*   You can only share payment methods ([pm\_](https://docs.stripe.com/api/payment_methods/object)) of type `card`. This includes cards that originate from a [wallet](https://docs.stripe.com/payments/wallets), such as Apple Pay, Google Pay, and Link.
*   You can’t share legacy sources ([src\_](https://docs.stripe.com/api/sources/object)), legacy cards ([card\_](https://docs.stripe.com/api/cards/object)), or legacy bank accounts ([ba\_](https://docs.stripe.com/api/customer_bank_accounts/object)).
*   You can attach other payment methods (such as ACH or Klarna) to a shared customer in one account, but they won’t be shared to other accounts in your organization.
*   You can’t disable sharing after enabling the feature.
*   You can’t share customers or payment methods between connected accounts, unless the connected accounts directly belong to an organization.
*   You can’t selectively share individual customers or payment methods. When you turn on sharing, all customers and payment methods are shared.
*   You can’t charge shared cards issued from India off session.

## Before you begin

1.  [Create an organization](https://docs.stripe.com/get-started/account/orgs/build#create-org) across your [multiple standalone accounts](https://docs.stripe.com/get-started/account/orgs/setup#standalone-accounts).
2.  [Create a sandbox environment](https://docs.stripe.com/get-started/account/orgs/build#create-organization-sandboxes) for your organization and its accounts so you can test your integration before putting it in production.

#### Get customer consent

Your customers must consent to share customer data and payment methods before you enable sharing across your accounts and legal entities. Consent collection is the responsibility of businesses, not Stripe.

## Enable sharing for accounts within your organization

You can enable sharing for a specific group of accounts in your organization or for all accounts.

1.  From your [organization settings](https://dashboard.stripe.com/org/settings) in the Dashboard, click **Customer and payment method sharing** to get started.
2.  Select the accounts to enable sharing for, and click **Share**. You must select at least two.
3.  Name your sharing group. Accounts can only belong to one group.
4.  Check the box to confirm that you obtained consent from your customers to share contact and payment method information across accounts in your organization.
5.  Click **Enable**.

#### Sharing is irreversible

You can enable sharing for unshared accounts at any time, but you can’t revert sharing for enabled accounts. You must contact Stripe if you want to disable sharing.

## How sharing works

After one account in the sharing group creates a customer, Stripe automatically creates that customer in all other accounts in the group. Each account in the sharing group maintains its own instance of the shared customer, but all instances have the same customer ID.

Any account in the sharing group can update the customer through the Dashboard or the API. Updates to the following fields of the `Customer` object sync across all account instances in the sharing group:

*   [name](https://docs.stripe.com/api/customers/object#customer_object-name)
*   [email](https://docs.stripe.com/api/customers/object#customer_object-email)
*   [address](https://docs.stripe.com/api/customers/object#customer_object-address)
*   [phone](https://docs.stripe.com/api/customers/object#customer_object-phone)
*   [description](https://docs.stripe.com/api/customers/object#customer_object-description)
*   [tax\_id](https://docs.stripe.com/api/customers/object#customer_object-tax-ids)
*   [preferred\_locales](https://docs.stripe.com/api/customers/object#customer_object-preferred_locales)
*   [metadata](https://docs.stripe.com/api/customers/object#customer_object-metadata)
*   [shipping](https://docs.stripe.com/api/customers/object#customer_object-shipping)
*   [business\_name](https://docs.stripe.com/api/customers/object#customer_object-business_name)
*   [tax\_exempt](https://docs.stripe.com/api/customers/object#customer_object-tax_exempt)
*   [invoice\_prefix](https://docs.stripe.com/api/customers/object#customer_object-invoice_prefix)

Updates to other fields within an account save to the `Customer` instance of the account making the update, but don’t sync to other accounts in the sharing group. It’s possible for the same customer to have different values for the same unshared field across different account instances. This protects the integrity of customer data that might be proprietary, sensitive, or only relevant to one account.

### Payment methods

Unlike Customer instances, Stripe creates the payment method only in the originating account. However, any account in the sharing group can charge, update, and even delete this single payment method instance. Updating a shared payment method (including removal) affects its attached customers on all accounts in the sharing group. However, the following activity only applies to the originating account:

*   Stripe generates `payment_method.<action>` events only for the originating account.
*   Stripe charges [Card Account Updater (CAU)](https://docs.stripe.com/get-started/data-migrations/payment-method-imports#cau) fees only to the originating account.

### Event behavior

If an account updates any of the shared fields for a customer, Stripe generates separate `customer.updated` events for each account in the sharing group. If an account updates an unshared field for the customer, Stripe sends the `customer.updated` event to only that account.

If an account attaches a payment method to a customer, Stripe generates a single `payment_method.attached` event for only the originating account.

We recommend all accounts in a sharing group listen for events using an [organization-level webhook](https://docs.stripe.com/webhooks#webhook-endpoint-def) so you’re aware of shared payment method activity.

## Sample integration use cases Server-side

The following sections provide code samples that illustrate how accounts in an organization sharing group might retrieve and use shared data. These examples reflect an organization with the following setup:

## Rocket Deliveries

Account 2

#### Visa Credit Card

Payment Method 456

A standard organization setup with three standalone accounts.

### Create a Customer during checkout

A customer makes a payment to one of the accounts in a sharing group (Rocket Rides). The [CheckoutSession](https://docs.stripe.com/api/checkout/sessions/create) enables `customer_creation` and `payment_method_save`.

`const stripe = require('stripe')('{{SECRET_KEY_ROCKET_RIDES}}');  const session = await stripe.checkout.sessions.`

`create`

`({   customer_creation: 'always',   line_items: [     {       price_data: {         currency: 'usd',         product_data: {           name: 'ride_service',         },         unit_amount: 2000,       },       quantity: 1,     },   ],   mode: 'payment',   ui_mode: 'embedded_page',   return_url: '[https://checkout.rocket-rides.com/checkout/return?session_id={CHECKOUT_SESSION_ID}](https://checkout.rocket-rides.com/checkout/return?session_id={CHECKOUT_SESSION_ID})',   saved_payment_method_options: {     payment_method_save: 'enabled',   }, });`

After payment completion, Stripe shares the new customer and payment method to the other accounts in the sharing group. Stripe triggers the following events:

*   `customer.created` for each account’s instance of the customer
*   `payment_method.attached` event for only the originating account

### Update shared customer data from another account

Rocket Deliveries updates the shared customer originally saved by Rocket Rides.

`const stripe = require('stripe')('{{SECRET_KEY_ROCKET_DELIVERIES}}');  const customer = await stripe.customers.`

`update`

`(   '{{CUSTOMER_ID}}',   {     email: 'jenny@example.com',     metadata: {       door: "front"     },   } );`

Stripe triggers the `customer.updated` event for each account in the sharing group. Each account’s instance of the customer gets the `email` and `metadata` update because those customer fields are shared.

### Retrieve a customer’s shared payment methods

All accounts in a sharing group can list a customer’s saved card type payment methods to use or update them.

If a customer has multiple payment methods saved across many accounts in a sharing group, Stripe limits the retrieval accounts to prioritize performance. We retrieve payment methods from only the requesting account and the four accounts with the most recently attached payment methods.

`const stripe = require('stripe')('{{SECRET_KEY_ROCKET_REPAIRS}}');  const paymentMethods = await stripe.customers.listPaymentMethods(`

`'{{CUSTOMER_ID}}'`

`);`

### Update a customer’s shared payment methods

Updates to a shared payment method (including removal) sync to all accounts in the sharing group and trigger the `payment_method.updated` or `payment_method.detached` event.

`const stripe = require('stripe')('{{SECRET_KEY_ROCKET_REPAIRS}}');  const paymentMethod = await stripe.paymentMethods.`

`update`

`(   '{{PAYMENT_METHOD_ID}}',   {     "  billing_details  ": {       "  address  ": {         "  city  ": "South San Francisco",         "  country  ": "us",         "  line1  ": "354 Oyster Point Boulevard",         "  line2  ": null,         "  postal_code  ": "94080",         "  state  ": "CA"       }     },   } );`

#### Consider recurring payments

Changes to payment methods can affect ongoing subscriptions using that payment method, so exercise caution.

### Accept a payment using a shared payment method Server-side

You can charge a payment method saved in one account (for example, Rocket Rides) for a payment created by another account in the sharing group (for example, Rocket Repairs).

`const stripe = require('stripe')('{{SECRET_KEY_ROCKET_REPAIRS}}');  const session = await stripe.checkout.sessions.`

`create`

`({   customer: '{{CUSTOMER_ID}}',   line_items: [     {       price_data: {         currency: 'usd',         product_data: {           name: 'tow_service',         },         unit_amount: 5000,       },       quantity: 1,     },   ],   mode: 'payment',   ui_mode: 'embedded_page',   return_url: '[https://checkout.rocket-repairs.com/checkout/return?session_id={CHECKOUT_SESSION_ID}](https://checkout.rocket-repairs.com/checkout/return?session_id={CHECKOUT_SESSION_ID})',   saved_payment_method_options: {     payment_method_save: 'enabled',   }, });`

Payments appear on the **Transactions** page for the corresponding account and the organization. Accounts can’t see each other’s payments, even when they’re part of the sharing group.

### Create a subscription using a shared payment method Server-side

You can also create a subscription for a customer originally saved by another account in the sharing group.

`const stripe = require('stripe')('{{SECRET_KEY_ROCKET_REPAIRS}}');  const session = await stripe.checkout.sessions.`

`create`

`({   customer: '{{CUSTOMER_ID}}',   line_items: [     {       price_data: {         currency: 'usd',         product_data: {           name: 'basic-roadside-service',         },         unit_amount: 2500,       },       quantity: 1,     },   ],   mode: 'subscription',   ui_mode: 'embedded_page',   return_url: '[https://checkout.rocket-repairs.com/checkout/return?session_id={CHECKOUT_SESSION_ID}](https://checkout.rocket-repairs.com/checkout/return?session_id={CHECKOUT_SESSION_ID})',   saved_payment_method_options: {     payment_method_save: 'enabled',   }, });`
