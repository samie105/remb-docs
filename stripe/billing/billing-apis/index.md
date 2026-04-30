---
title: "About the Billing APIs"
source: "https://docs.stripe.com/billing/billing-apis"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:06:31.094Z"
content_hash: "3157f0e9c37e6f0ca7433f5bb609928b7fbec2738af300d40ff82804f34e84b1"
---

We recommend using [Checkout Sessions to create subscriptions](https://docs.stripe.com/billing/quickstart). A Checkout Session gives your customer a payment page where they enter their payment details. Stripe then creates the customer, activates the subscription, and handles payment using the Billing API objects described below.

When you create a [subscription](https://docs.stripe.com/billing/subscriptions/creating), Stripe automatically generates an [`Invoice`](https://docs.stripe.com/api/invoices) object at each billing cycle. Each `Invoice` automatically creates a [`PaymentIntent`](https://docs.stripe.com/payments/payment-intents) object to collect payment from the customer’s stored payment method. After you create the subscription, Stripe manages the rest of the billing lifecycle.

A subscription has:

*   A [Product](https://docs.stripe.com/api/products) to model what’s being sold.
*   A [Price](https://docs.stripe.com/api/prices) to determine the interval and amount to charge.
*   An object that represents a customer to store the [Payment Methods](https://docs.stripe.com/api/payment_methods) used to make each recurring payment. Depending on how you model your customers, this can be either a [customer-configured Account](https://docs.stripe.com/api/v2/core/accounts/object#v2_account_object-configuration-customer-applied) or a [Customer](https://docs.stripe.com/api/customers).

#### Use the Accounts v2 API to represent customers

default\_payment\_method

`pm_1234`

customer\_account

`acct_1234`

items.data.price

`price_1234`

contact\_email

`jennyrosen@example.com`

customer\_account

`acct_1234`

A diagram illustrating common billing objects and their relationships

## API object definitions

Resource

Definition

[Account configured as a customer](https://docs.stripe.com/api/v2/core/accounts/create#v2_create_accounts-configuration-customer)

Represents a customer in the Accounts v2 API who purchases a subscription. Configure an `Account` object as a customer and associate it with a subscription to make and track recurring charges and to manage the products that they subscribe to. For more information, see the [Use Accounts as customers guide](https://docs.stripe.com/connect/use-accounts-as-customers).

[Customer](https://docs.stripe.com/api/customers)

Represents a customer in the Customers API who purchases a subscription. Use the `Customer` object associated with a subscription to make and track recurring charges and to manage the products that they subscribe to.

[Entitlement](https://docs.stripe.com/api/entitlements/active-entitlement)

Represents a customer’s access to a feature included in a service product that they subscribe to. When you create a subscription for a customer’s recurring purchase of a product, an active entitlement is automatically created for each feature associated with that product. When a customer accesses your services, use their active entitlements to enable the features included in their subscription.

[Feature](https://docs.stripe.com/api/entitlements/feature)

Represents a function or ability that your customers can access when they subscribe to a service product. You can include features in a product by creating ProductFeatures.

[Invoice](https://docs.stripe.com/api/invoices)

A statement of amounts a customer owes that tracks payment statuses from draft through paid or otherwise finalized. Subscriptions automatically generate invoices.

[PaymentIntent](https://docs.stripe.com/api/payment_intents)

A way to build dynamic payment flows. A PaymentIntent tracks the lifecycle of a customer checkout flow and triggers additional authentication steps when required by regulatory mandates, custom Radar fraud rules, or redirect-based payment methods. Invoices automatically create PaymentIntents.

[PaymentMethod](https://docs.stripe.com/api/payment_methods)

A customer’s payment methods that they use to pay for your products. For example, you can store a credit card on a customer-configured `Account` or `Customer` object and use it to make recurring payments for that customer. Typically used with the Payment Intents or Setup Intents APIs.

[Price](https://docs.stripe.com/api/prices)

Defines the unit price, currency, and billing cycle for a product.

[Product](https://docs.stripe.com/api/products)

A good or service that your business sells. A service product can include one or more features.

[ProductFeature](https://docs.stripe.com/api/product-feature)

Represents a single feature’s inclusion in a single product. Each product is associated with a ProductFeature for each feature that it includes, and each feature is associated with a ProductFeature for each product that includes it.

[Subscription](https://docs.stripe.com/api/subscriptions)

Represents a customer’s scheduled recurring purchase of a product. Use a subscription to collect payments and provide repeated delivery of or continuous access to a product.

Here’s an example of how products, features, and entitlements work together. Imagine that you want to set up a recurring service that offers two tiers: a standard product with basic functionality, and an advanced product that adds extended functionality.

1.  You create two features: `basic_features` and `extended_features`.
2.  You create two products: `standard_product` and `advanced_product`.
3.  For the standard product, you create one ProductFeature that associates `basic_features` with `standard_product`.
4.  For the advanced product, you create two ProductFeatures: one that associates `basic_features` with `advanced_product` and one that associates `extended_features` with `advanced_product`.

A customer, `first_customer`, subscribes to the standard product. When you create the subscription, Stripe automatically creates an Entitlement that associates `first_customer` with `basic_features`.

Another customer, `second_customer`, subscribes to the advanced product. When you create the Subscription, Stripe automatically creates two Entitlements: one that associates `second_customer` with `basic_features`, and one that associates `second_customer` with `extended_features`.

You can determine which features to provision for a customer by [retrieving their active entitlements or listening to the Active Entitlement Summary event](https://docs.stripe.com/billing/entitlements#entitlements). You don’t have to retrieve their subscriptions, products, and features.
