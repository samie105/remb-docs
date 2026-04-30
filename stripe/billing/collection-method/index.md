---
title: "Billing collection methods"
source: "https://docs.stripe.com/billing/collection-method"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T13:06:50.594Z"
content_hash: "f934e65de7d0b6da3185a5ac68bf587f84854c503ead713903b754d6fa268ca6"
---

You can set your preferred payment collection method when creating [invoices](https://docs.stripe.com/api/invoices) and [subscriptions](https://docs.stripe.com/billing/subscriptions/creating) using either the Dashboard or API.

## Automatic charging versus manual payments

The collection method determines how Stripe processes the payment for both products. To collect payments for invoices and subscriptions, you can select from these methods:

*   Automatic charging
*   Manual payments

#### Note

Manual payment methods, such as wire transfers, have more rigorous tracking and reconciliation processes, which [enterprise clients](#enterprise-clients-wire-transfers) often require for high transaction volumes. Some payment methods, such as [bank transfers](https://docs.stripe.com/invoicing/bank-transfer), only support `send_invoice` and can’t be charged automatically.

### Set a collection method for an invoice

To set a collection method for an invoice through the Invoicing API, use the [collection\_method](https://docs.stripe.com/api/invoices/object#invoice_object-collection_method) attribute.

*   `charge_automatically`: Lets you automatically charge a customer’s default payment method to pay invoices.
*   `send_invoice`: Sends an invoice for manual payment. Unlike automatic charging which requires immediate payment, you can give the customer an adjustable payment window. You can use the [Hosted Invoice Page](https://docs.stripe.com/invoicing/hosted-invoice-page) and set up [email notifications and reminders](https://docs.stripe.com/invoicing/send-email#customer-emails) to facilitate payment.

### Set a collection method for a subscription

To set a collection method for a subscription through the Subscriptions API, use the [collection\_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-collection_method) attribute. If you change the collection method for a subscription, only subsequently created subscription invoices use the new collection method.

*   `charge_automatically`: Tells Stripe to automatically charge your customer’s default payment method to pay the invoice generated for each billing period.
*   `send_invoice`: Generates an invoice for each billing period, and requires manual payment. Unlike automatic charging which requires immediate payment, you can give the customer an adjustable payment window.

### Due dates for manual payment invoices

You can configure the due date for invoices that use the `send_invoice` [collection method](#set-collection-method-invoice) to receive manual payments. You can also configure up to three reminders, starting at 10 days before the due date and ending at 60 days after.

You can also take additional action on the subscription 30, 60, or 90 days after an invoice becomes past due. The options are:

Setting

Description

Cancel the subscription

The subscription changes to a `canceled` status after the maximum number of days defined in the retry schedule.

Mark the subscription as unpaid

The subscription changes to an `unpaid` status after the maximum number of days defined in the retry schedule. Invoices continue to generate and either stay in a `draft` status or transition to a status specified in your invoice settings.

Leave the subscription past due

The subscription remains in a `past_due` status after the maximum number of days defined in the retry schedule. Invoices continue to be generated into an `open` status.

## Collection methods and failed payments

Depending on the collection method, failed payments generate different [subscription statuses](https://docs.stripe.com/api/subscriptions/object#subscription_object-status) and [invoice statuses](https://docs.stripe.com/api/invoices/object#invoice_object-status).

### Failed subscription payments

Creating a subscription with a [payment\_behavior](https://docs.stripe.com/api/subscriptions/create#create_subscription-payment_behavior) of `allow_incomplete`, and the `collection_method` set to `charge_automatically`, immediately attempts payment and marks the subscription `status` as `incomplete` if the initial payment attempt doesn’t succeed.

Passing a `payment_behavior` of `default_incomplete` will always initialize subscriptions with an `incomplete` status if the first invoice requires payment. The resulting PaymentIntent must be confirmed in a separate request to attempt payment.

For both `allow_incomplete` and `default_incomplete`, the subscription becomes `active` after the first invoice is paid. Subscriptions that don’t require payment upon creation (like those that are trialing) will immediately have a status of `active`. If the first invoice remains unpaid after 23 hours, the subscription is set to `incomplete_expired`. This status is final and irreversible, voiding the open invoice and preventing future invoices.

### Failed recurring charges

If a payment fails or if it requires customer authentication, the subscription’s `status` is set to `past_due` and the PaymentIntent status is either `requires_payment_method` or `requires_action`.

To manage these scenarios, set up a [webhook endpoint](https://docs.stripe.com/webhooks) and listen to the [customer.subscription.updated](https://docs.stripe.com/api/events/types#event_types-customer.subscription.updated) event so you’re notified when subscriptions enter a `past_due` status:

`{   "id": "sub_E8uXk63MAbZbto",   "object": "subscription",   ...   "status": "past_due",   "latest_invoice": "in_1EMLu1ClCIKljWvsfTjRFAxa" }`

For these subscriptions, you need to redirect your customers to your application to collect a different payment method, allowing them to complete the payment. You can use an email or a mobile push notification. Stripe provides built-in reminder emails to handle this case, which you can configure in your Dashboard [billing settings](https://dashboard.stripe.com/account/billing/automatic).

When your customer returns to your application, reuse either your [payment failure flow](https://docs.stripe.com/billing/subscriptions/overview#requires-payment-method) or [customer action flow](https://docs.stripe.com/billing/subscriptions/overview#requires-action), depending on the status of the associated PaymentIntent. After the payment succeeds, the status of the subscription is `active` and the invoice is `paid`.

### Failed incomplete subscriptions

When a subscription has a status of `incomplete`, you can only update attributes that won’t result in the creation of an invoice or invoice item, such as its [metadata](https://docs.stripe.com/api/subscriptions/object#subscription_object-metadata), [save\_default\_payment\_method](https://docs.stripe.com/api/subscriptions/object#subscription_object-payment_settings-save_default_payment_method), and [description](https://docs.stripe.com/api/subscriptions/object#subscription_object-description).

If a payment to renew the subscription fails when you’ve set it to charge automatically, the subscription transitions to `past_due` and Stripe may mark it as `canceled` or `unpaid` (depending on your [subscriptions settings](https://dashboard.stripe.com/settings/billing/automatic)) after Stripe exhausts all payment retry attempts.

On the other hand, if the subscription’s `collection_method` is set to `send_invoice`, it becomes `past_due` when its invoice remains unpaid by the due date. If the customer still hasn’t paid the invoice after you extend the deadline, Stripe may mark the subscription as `canceled` or `unpaid`, which again depends on your subscription settings.

When a subscription has a status of `unpaid`, Stripe creates future invoices but leaves them as drafts. In this case, you have the option to [resend](https://docs.stripe.com/api/invoices/send) the `past due` invoice and any created draft invoices to collect payment. Use this feature if you’re trying to collect payment for unpaid months (such as when you continue to provide the goods or services related to an unpaid subscription) or leave them closed and unpaid when you stop providing goods or services.

### Failed invoicing payments

Invoices not associated with subscriptions that have their `collection_method` set to `charge_automatically` and [auto-advancement](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection) disabled, remain `open` if an initial payment attempt fails. Because auto-advancement is disabled, Stripe doesn’t automatically close the invoices, retry them, or transition them to a different status. Learn more about [failed payment notifications](https://docs.stripe.com/invoicing/automatic-collection#failed-payment-notifications) and [managing invoices sent to customers](https://docs.stripe.com/invoicing/automatic-collection#manage-invoices-sent-customers).

If [auto-advancement](https://docs.stripe.com/invoicing/integration/automatic-advancement-collection) is enabled for the invoice, Stripe may automatically mark the invoice as `uncollectible` (depending on your [invoice status settings](https://dashboard.stripe.com/settings/billing/automatic)) after Stripe exhausts all payment retry attempts.

When the collection method is set to `send_invoice`, the invoice requires manual payment. If the invoice remains unpaid past the due date, the status becomes `past_due`, indicating an overdue invoice. If you extend the payment deadline and the customer still hasn’t paid, you can leave the invoice as `past_due` or transition it to `uncollectible` or `void`.

## Enterprise clients and wire transfers

For enterprise clients, manual payment methods, such as wire transfers, offer some advantages. These payment methods often involve more rigorous tracking and reconciliation processes compared to automated methods, which is crucial for enterprises that deal with high transaction volumes. By setting the `collection_method` to `send_invoice`, you can generate clear and well-documented invoices that enterprise clients can pay using wire transfers—a commonly preferred payment method for this type of client.

## See also

*   [Automatic collection](https://docs.stripe.com/invoicing/automatic-collection)
*   [Automatic charging](https://docs.stripe.com/invoicing/automatic-charging)
*   [Subscription invoices](https://docs.stripe.com/billing/invoices/subscription)
*   [Status transitions and finalization](https://docs.stripe.com/invoicing/integration/workflow-transitions)
