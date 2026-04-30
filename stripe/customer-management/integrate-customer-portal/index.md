---
title: "Integrate the customer portal with the API"
source: "https://docs.stripe.com/customer-management/integrate-customer-portal"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:07:49.243Z"
content_hash: "44b32166c065ecf0ec76ea5b5c1b992b1779d8c74cf2098fc26fe6a3a8e5abaa"
---

With the customer portal, you can provide subscription, billing, and invoicing management to your customers without building it yourself. After you configure and integrate the portal, customers redirect to a co-branded dashboard where they can manage their account based on the functionality you configured.

To integrate your application with the customer portal:

1.  [Configure](#configure) the portal’s features and user interface (UI). You can do this in the Dashboard.
2.  [Implement a redirect](#redirect) to integrate the portal with your application.
3.  [Listen to webhooks](#webhooks) to receive updates to customers’ subscriptions and payment methods.
4.  [Launch the portal](#launch) in your production environment.

You can optionally [customize](#customize) portal sessions to enable different features for different customers.

#### Use the Accounts v2 API to represent customers

[](#configure)

First, you need to [register for a Stripe account](https://dashboard.stripe.com/register/).

Before you integrate the customer portal, use the Dashboard to define what your users can do with the portal. Choose your settings for [sandboxes](https://docs.stripe.com/sandboxes) and live mode, based on your product and price catalog.

#### Common mistake

If you’re using the customer portal with Stripe Connect, make sure you configure the customer portal for the platform, not a connected account.

If you want to create multiple portal configurations for different sets of customers (or if you’re a [Connect](https://docs.stripe.com/connect) platform and want to manage configurations for your connected accounts), you can do so using the [API](https://docs.stripe.com/api/customer_portal/configurations/object):

`curl https://api.stripe.com/v1/billing_portal/configurations \  -u "`

`sk_test_REDACTED`

`:" \  -d "features[invoice_history][enabled]=true"`

### Set a product catalog

If you allow customers to upgrade, downgrade, or change the quantities of their subscriptions, you must also set a product catalog. This includes the products and prices that your customers can upgrade or downgrade to, and the subscriptions they can update quantities on. See how to [create a product](https://docs.stripe.com/products-prices/manage-prices#create-product) for more details about creating products and prices. If you’re using the customer portal for invoicing only, you don’t need to set a product catalog.

The portal displays the following attributes of your product catalog:

*   **Product name and description**—These attributes are editable in the Dashboard and API.
*   **Quantity restrictions per product**—These attributes are editable in the Dashboard.
*   **Price amount, currency, and billing interval**—These attributes are fixed, and you can only set them when you create them in the Dashboard and API.

### Enable tax ID collection

If you use [Stripe Tax](https://docs.stripe.com/tax) to automatically collect taxes for subscriptions or invoices, you can let customers set and update their tax IDs in the customer portal. Stripe Billing adds the tax IDs to the customers’ [invoices](https://docs.stripe.com/api/invoices). To allow customers to set their tax IDs, go to the [Customer portal settings](https://dashboard.stripe.com/settings/billing/portal) and toggle on **Tax ID**. For more information, see how customer tax IDs work with [subscriptions](https://docs.stripe.com/billing/customer/tax-ids) and [invoices](https://docs.stripe.com/invoicing/taxes/account-tax-ids).

Learn how to [set up Stripe Tax](https://docs.stripe.com/tax/set-up), [collect taxes for recurring payments](https://docs.stripe.com/billing/taxes/collect-taxes), [collect taxes in your custom payment flows](https://docs.stripe.com/tax/custom#existing-customer) and [set tax rates for line items and invoices](https://docs.stripe.com/tax/invoicing).

### Preview and test

As you configure your settings, click **Preview** to preview the portal. This launches a read-only version of the portal that lets you see how your customers might manage their subscriptions and billing details.

After saving your settings, you can launch the portal and test it by using a customer in a sandbox. Go to a customer in the Dashboard, click **Actions**, and then select **Open customer portal**.

You can only preview the portal as a read-only version when your Dashboard is in a sandbox. If you can’t preview and test the portal, check your settings to make sure that your configuration is saved in a sandbox. For previewing and testing to work, you also need to have edit permissions in the Dashboard.

[](#redirect)

A portal session is the entry point into the customer portal. It provides a unique, temporary link to the portal. When a customer wants to manage their billing or invoicing, create a new portal session and redirect them to the session’s `url`.

On your site, add a button that customers can click to enter the portal. Use a POST request to create a portal session:

`<form method="POST" action="/create-customer-portal-session">   <button type="submit">Manage billing</button> </form>`

Next, add an endpoint that creates a portal session and redirects your customers. Make sure to authenticate customers on your site before creating sessions for them. To [create a session](https://docs.stripe.com/api/customer_portal/sessions/create), you need the customer’s ID and a `return_url`, which is required if a default return URL isn’t set in the Dashboard configuration.

When you create a portal session, Stripe returns the `portal session object`, which contains the session’s [short-lived URL](https://docs.stripe.com/api/customer_portal/sessions/object?lang=curl#portal_session_object-url) that your customers use to access the customer portal.

`curl https://api.stripe.com/v1/billing_portal/sessions \  -u "`

`sk_test_REDACTED`

`:" \  -d "customer_account=  {{CUSTOMER_ACCOUNT_ID}}  " \   --data-urlencode "return_url=[https://example.com/account](https://example.com/account)"`

[](#webhooks)

When subscriptions are upgraded, downgraded, or canceled, you need to make sure that customers receive only the products or services they’re actively subscribed to. Stripe sends notifications of these changes to your integration using [webhooks](https://docs.stripe.com/webhooks). In the `Event` object, look at the ID for the subscription or the customer to determine which customer the event applies to.

When your customers update their billing information in the customer portal, it’s important to update your customer records. Listen for changes using the `customer.updated` or `v2.core.account[configuration.customer].updated` webhook.

Stripe also sends notifications if an invoice is paid to your integration using [webhooks](https://docs.stripe.com/webhooks). In the `Event` object, look at the ID for the invoice or the customer to determine which customer the event applies to.

If you haven’t set up a webhook endpoint with Stripe before, you can use Stripe’s [webhooks documentation](https://docs.stripe.com/webhooks) to get started, and then listen for the events described below.

Event

Description

[customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated)

Listen to this to monitor subscription upgrades and downgrades. For upgrades, check the `subscription.items.data[0].price` attribute in the subscription object to find the price the customer is subscribed to. Then, grant access to the new product. For downgrades, check the same attribute and adjust or revoke access as needed.

When a customer uses the portal to upgrade or downgrade a subscription with a [trial](https://docs.stripe.com/billing/subscriptions/trials), the subscription’s trial ends immediately when switching to the new price.

[customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated)

Listen to this to monitor updates to the subscription quantity. When you receive this event, check the `subscription.items.data[0].quantity` attribute to find the quantity the customer is subscribed to. Then, grant access to the new quantity.

[customer.subscription.deleted](https://docs.stripe.com/api/events/types#event_types-customer.subscription.deleted)

Listen to this to monitor subscription cancellations. When you receive this event, revoke the customer’s access to the product. If you configure the portal to cancel subscriptions at the end of a billing period, listen to the [customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated) event to be notified of cancellations before they occur. For flexible [billing mode](https://docs.stripe.com/api/subscriptions/object#subscription_object-billing_mode) subscriptions, if `cancel_at` is not `null`, the subscription is canceled at the end of its billing period. For classic billing mode subscriptions, check that `cancel_at_period_end` is `true`.

If a customer changes their mind, they can reactivate their subscription prior to the end of the billing period. When they do this, a [customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated) event is sent. For flexible billing mode subscriptions, check that `cancel_at` is `null` to confirm reactivation. For classic billing mode, check that `cancel_at_period_end` is `false`.

[payment\_method.attached](https://docs.stripe.com/api/events/types#event_types-payment_method.attached)

Occurs when a customer adds a payment method.

[payment\_method.detached](https://docs.stripe.com/api/events/types#event_types-payment_method.detached)

Occurs when a customer removes a payment method.

[customer.updated](https://docs.stripe.com/api/events/types#event_types-customer.updated)

Occurs when a [Customer](https://docs.stripe.com/api/customers/object) object is updated. Check the `invoice_settings.default_payment_method` attribute to find the payment method that the customer selected as the new default. If you have subscriptions that override the customer-level default payment method, customers can remove this override. Check the subscription’s `default_payment_method` attribute when you receive this event to see if the override was removed. Use this webhook to update any relevant information in your database. All updates must be treated as billing information changes only. Don’t use the customer billing email address as a login credential.

[v2.core.account\[configuration.customer\].updated](https://docs.stripe.com/api/v2/core/events/event-types#v2_event_types-v2.core.account%5Bconfiguration.customer%5D.updated)

Occurs when a customer-configured `Account`’s [customer configuration](https://docs.stripe.com/api/v2/core/accounts/object#v2_account_object-configuration-customer) is updated. Check the `configuration.customer.billing.default_payment_method` attribute to find the payment method that the customer selected as the new default. If you have subscriptions that override the customer-level default payment method, customers can remove this override. Check the subscription’s `default_payment_method` attribute when you receive this event to see if the override was removed. Use this webhook to update any relevant information in your database. All updates must be treated as billing information changes only. Don’t use the customer billing email address as a login credential.

[customer.tax\_id.created](https://docs.stripe.com/api/events/types#event_types-customer.tax_id.created)

Occurs when customers manage their tax IDs. Stripe can validate some types of tax IDs. Learn more in the [tax IDs guide](https://docs.stripe.com/billing/customer/tax-ids).

[customer.tax\_id.deleted](https://docs.stripe.com/api/events/types#event_types-customer.tax_id.deleted)

Occurs when customers manage their tax IDs. Stripe can validate some types of tax IDs. Learn more in the [tax IDs guide](https://docs.stripe.com/billing/customer/tax-ids).

[customer.tax\_id.updated](https://docs.stripe.com/api/events/types#event_types-customer.tax_id.updated)

Listen to this to get validation updates about customer tax IDs. Learn more in the [tax IDs guide](https://docs.stripe.com/billing/customer/tax-ids).

[billing\_portal.configuration.created](https://docs.stripe.com/api/events/types#event_types-billing_portal.configuration.created)

Occurs when a configuration is created.

[billing\_portal.configuration.updated](https://docs.stripe.com/api/events/types#event_types-billing_portal.configuration.updated)

Occurs when a configuration is updated.

[billing\_portal.session.created](https://docs.stripe.com/api/events/types#event_types-billing_portal.session.created)

Occurs when a portal session is created.

[](#launch)

Make sure to test the portal before enabling it in production.

When you create a portal session, Stripe returns the `portal session` object, which contains the session’s [short-lived URL](https://docs.stripe.com/api/customer_portal/sessions/object?lang=curl#portal_session_object-url) that your customers must use to access the customer portal. You can also create one shareable link for each configuration of the portal with the [login\_page](https://docs.stripe.com/api/customer_portal/configurations/object#portal_configuration_object-login_page) parameter.

*   Turn off **View test data** in the Dashboard.
*   [Configure](https://dashboard.stripe.com/settings/billing/portal) the portal in live mode.
*   Add your [webhooks](https://dashboard.stripe.com/webhooks) in live mode.

Stripe maintains multiple distinct sets of portal configurations: one for live mode and one for each sandbox. To help you validate your integration, making changes in one mode doesn’t affect your configuration in the other.
