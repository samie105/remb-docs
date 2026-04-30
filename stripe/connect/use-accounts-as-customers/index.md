---
title: "Represent customers using Account objects"
source: "https://docs.stripe.com/connect/use-accounts-as-customers"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:11:26.027Z"
content_hash: "ec923bd6d9f032b9e53d34e1a477515fcda800c60c693b8d1fd9ed4611c4c8d5"
---

## Interested in getting early access to the Accounts v2 API preview?

We're in the process of rolling out the Accounts v2 preview. To request access, enter your email address below.

The Accounts v2 API uses [configurations](https://docs.stripe.com/connect/account-capabilities?accounts-namespace=v2#configurations) to enable functionality for `Account` objects. When using the v2 API, you can represent a customer using an `Account` object instead of a `Customer` object by assigning the [customer configuration](https://docs.stripe.com/api/v2/core/accounts/create#v2_create_accounts-configuration-customer) to the `Account`. When making a request that accepts a `Customer` ID as the argument to the `customer` parameter, instead provide the `Account` ID as the argument to the `customer_account` parameter.

The following example creates an `Account` with the `customer` configuration and requests the common `automatic_indirect_tax` capability, which is part of the `customer` configuration. Requesting the capability is optional; you can simply add the configuration by specifying `configuration.customer`.

`curl -X POST https://api.stripe.com/v2/core/accounts \  -H "Authorization: Bearer` 

`sk_test_REDACTED`

`" \  -H "Stripe-Version: $latestPreviewApiVersion" \   --json '{     "contact_email": "jenny.rosen@example.com",     "display_name": "Jenny Rosen",     "identity": {         "country": "us",         "individual": {             "given_name": "Jenny Rosen"         }     },     "configuration": {         "customer": {             "capabilities": {                 "automatic_indirect_tax": {                     "requested": true                 }             }         }     },     "include": [         "configuration.customer",         "identity"     ]   }'`

When you enable the Accounts v2 API, your Stripe-hosted integrations, such as Checkout, create `Accounts` with the `customer` configuration instead of `Customer` objects. If your code references `Customer` objects, we recommend that you update it to reference customer-configured `Account` objects instead.

## Provide an Account as the customer

API requests such as `Subscriptions` and `SetupIntents` require you to specify a customer. These requests accept either the `customer` or `customer_account` parameter. The following example creates a subscription and specifies the customer by passing an `Account` ID as the `customer_account`.

`curl https://api.stripe.com/v1/subscriptions \  -u "`

`sk_test_REDACTED`

`:" \  -H "Stripe-Version: $latestPreviewApiVersion" \  -d customer_account=acct_xxxxx \  -d "items[0][price]=price_CBb6IXqvTLXp3f" \   -d "items[0][quantity]=5"`

## Reference Accounts in Customers v1 integrations

A request that specifies `customer_account` returns both `customer` and `customer_account` properties, with correspondingly formatted values. This maintains compatibility with existing Billing and Payments integrations.

`{   "id": "sub_1Mow234",   .   .   .   "customer": "cus_xxxxx",   "customer_account": "acct_xxxxx" }`

You can also retrieve or update customer-configured Accounts using the `/v1/customers` endpoint.

`curl -X POST https://api.stripe.com/v1/customers/acct_1234 \  -u "`

`sk_test_REDACTED`

`:"`

## Accounts v2 webhooks

Webhooks for Accounts v2 send [thin events](https://docs.stripe.com/event-destinations#thin-events).

Action

v1 event

v2 event

Customer created

`customer.created`

Accounts v2 sends separate events indicating the account creation and the customer configuration:

*   `v2.core.account.created`
*   `v2.core.account[configuration.customer].updated`

Billing address updated

`customer.updated`

`v2.core.account[identity].updated`

Subscription actions

`customer.subscription.[action]`

None; use the v1 event

Customer deleted

`customer.deleted`

`v2.core.account.closed`

## Customer invoice properties

## Reference an Account ID with a Customers endpoint

The Accounts v2 API doesn’t have endpoints for every customer function. To perform the following actions for an `Account` object, use the `v1/customers` endpoint and pass the `Account` ID (`acct_xxxxx`) as the path parameter.

Use case

v1 endpoint with account ID

Manage cash balances

*   `v1/customers/acct_xxxxx/cash_balances`
*   `v1/customers/acct_xxxxx/cash_balances/:id`

Manage cash balance transactions

*   `GET v1/customers/acct_xxxxx/cash_balance_transactions`
*   `GET v1/customers/acct_xxxxx/cash_balance_transactions/:id`
*   `POST v1/test_helpers/customers/acct_xxxxx/fund_cash_balance`
*   `POST v1/customers/acct_xxxxx/funding_instructions`
*   `GET v1/customers/acct_xxxxx/funding_instructions`

Manage invoice credit balance

For `Account` objects, the [ending\_balance](https://docs.stripe.com/api/invoices/object?api-version=preview#invoice_object-ending_balance) of the account’s most recently finalized invoice corresponds to the `Customer` object’s `invoice_credit_balance`.

*   `POST v1/customers/acct_xxxxx/balance_transactions`
*   `POST v1/customers/acct_xxxxx/balance_transactions/:id`
*   `GET v1/customers/acct_xxxxx/balance_transactions/:id`
*   `GET v1/customers/acct_xxxxx/balance_transactions`

## Customer-Account object property map

The following table describes how properties of `Customer` objects correspond to properties of customer-configured `Account` objects. Except where noted, Stripe copies the mapped values when generating an `Account` corresponding to an existing `Customer`.

Mapped values remain synchronized. For example, if you set `identity.country` on an `Account`, then when you pass that `Account` ID as the `customer_account` to a v1 endpoint, the returned `country` contains the same value.

Customers v1 property

Accounts v2 property

Notes

`address`

{all properties}

`identity.business_details.address` or `identity.individual.address`

When Stripe associates a v1 `Customer` with a v2 `Account`, `address` is only included if it passes validation. `address.country` (string in v1 and enum in v2) is only included if it matches either a valid enum or country name, ignoring case and any special characters.

`country`

`identity.country`

When Stripe associates a v1 `Customer` with a v2 `Account`, `address.country` (string) only copies to `identity.country` (enum) if it matches either a valid enum or country name, ignoring case and any special characters.

`business_name`

`identity.business_details.registered_name`

`created`

{not mapped}

When Stripe associates a v1 `Customer` with a v2 `Account`, the `Account`’s `created` property reflects the timestamp when the `Account` was created, not the original `Customer`.

`currency`

{not mapped}

The v2 `Account`’s `defaults.currency` property doesn’t apply to the `customer` configuration.

`customer_account`

`id`

When Stripe associates a v1 `Customer` with a v2 `Account`, the `Customer`’s `customer_account` property contains the ID of that `Account`. The ID of the `Customer` isn’t available on the `Account`. Users who create v2 `Accounts` representing customers don’t need to use a v1 `Customer` ID.

`description`

{not mapped}

The v1 `Customer` `description` isn’t available on the v2 `Account`. However, it appears (read-only) on the customer details page in the Dashboard.

`email`

`contact_email`

`id`

{not mapped}

The ID of the v1 `Customer` isn’t available on the v2 `Account`. Users who create v2 `Accounts` representing customers don’t need to use a v1 `Customer` ID.

`individual_name`

`display_name`

When Stripe associates a v1 `Customer` with a v2 `Account`, it only copies `individual_name` if the `Customer`’s `name` is null.

`invoice_prefix`

`configuration.customer.billing.invoice.prefix`

`invoice_settings`

`custom_fields`

`configuration.customer.billing.invoice.custom_fields`

The `Account` array is limited to 4 elements.

`default_payment_method`

`configuration.customer.billing.invoice.default_payment_method`

`footer`

`configuration.customer.billing.invoice.footer`

`rendering_options`

`configuration.customer.billing.invoice.rendering`

When Stripe associates a v1 `Customer` with a v2 `Account`, `invoice_settings.rendering_options.amount_tax_display` (string) only copies to `configuration.customer.billing.invoice.rendering.amount_tax_display` (enum) if it matches an enum value (`include_inclusive_tax` or `exclude_tax`).

`livemode`

`livemode`

`metadata`

`metadata`

`name`

`display_name`

When Stripe associates a v1 `Customer` with a v2 `Account`, if `name` is null, the `Customer`’s `individual_name` copies to `display_name`.

`next_invoice_sequence`

`configuration.customer.billing.invoice.next_sequence`

`phone`

`identity.business_details.phone or identity.individual.phone`

`preferred_locales`

`defaults.locales`

The `Customer` property `preferred_locales` is a nullable array of strings, and the `Account` property `defaults.locales` is a nullable array of enums. When Stripe associates a v1 `Customer` with a v2 `Account`, a given `preferred_locales` string is only included if it matches a `defaults.locales` enum value, ignoring case and any special characters.

`shipping`

`configuration.customer.shipping`

`subscriptions`

{not mapped}

The v2 `Account` object doesn’t include an array of subscriptions. To retrieve a customer’s subscriptions, use the Subscriptions API and filter by `customer` or `customer_account`.

`tax`

`automatic_tax`

`configuration.customer.capabilities.automatic_indirect_tax.status` {value not synchronized}

The `Account` property is only available after requesting the Automatic Indirect Tax capability. Also, it doesn’t have an equivalent to the `Customer` property’s `not_collecting` value. It only indicates the status of the capability.

`ip_address`

`configuration.customer.automatic_indirect_tax.ip_address`

`location`

`configuration.customer.automatic_indirect_tax.location` {value not synchronized}

When Stripe associates a v1 `Customer` with a v2 `Account`, `tax.location` isn’t automatically included. You must request the Automatic Indirect Tax capability to set `configuration.customer.automatic_indirect_tax.location`.

`provider`

{not mapped}

If a `Customer` is associated with a third-party tax provider, Stripe doesn’t automatically associate that `Customer` with an `Account`.

`tax_exempt`

`configuration.customer.automatic_indirect_tax.exempt`

`tax_ids`

{not mapped}

The v2 `Account` object doesn’t include an array of tax IDs. To retrieve a customer’s tax IDs, use the Tax IDs API and filter by `owner.customer` or `owner.customer_account`.

`test_clock`

`configuration.customer.test_clock`

## Enable the Accounts v2 preview

Previously, the Accounts v2 API was only available to Connect platforms. It’s now available in preview for all Stripe users.

Accounts v2 gives you a unified way to represent your users across Stripe products. Instead of using `Customer` objects, which only provide functionality for storing payment methods and making recurring payments, you can use `Account` objects, which offer greater flexibility through the use of configurations when additional functionality is required.

To enable the preview:

1.  Go to [Account previews and features](https://dashboard.stripe.com/settings/features/product-previews) in your Dashboard.
2.  Enable the **Reusable payment methods for Global Payouts** toggle. If you don’t see the toggle, request access using the form at the top of this page.

When you opt in, your existing `Customer` objects are automatically synced with corresponding customer-configured v2 `Account` objects. When you create a new customer in the Dashboard, it generates a customer-configured `Account` object, not a `Customer` object. You can use these `Accounts` in [most integrations that reference Customer objects](#reference-accounts-in-customers-v1-integrations).

Enabling the Accounts v2 preview also enables [reusable payment credentials for Global Payouts](https://docs.stripe.com/global-payouts/credential-reuse), which let you store and reuse payment methods across Global Payouts transactions.

## Limitations and opting out

The Accounts v2 preview doesn’t support the following features:

*   [Cloning customers](https://docs.stripe.com/get-started/data-migrations/pan-copy-self-serve)
*   [Sharing customers and payment methods in an organization](https://docs.stripe.com/get-started/account/orgs/sharing/customers-payment-methods)
*   Third-party tax integrations (Stripe Tax is supported)

To opt out, turn off the toggle in [Account previews and features](https://dashboard.stripe.com/settings/features/product-previews).

Opting out doesn’t revert existing `Customer` objects that are already associated with v2 `Account` objects. If you need unsupported functionality for those customers, you need to create new `Customer` objects for them.
