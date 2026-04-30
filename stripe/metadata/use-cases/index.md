---
title: "Metadata use cases"
source: "https://docs.stripe.com/metadata/use-cases"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:53:37.436Z"
content_hash: "a98ff5aad6d695a043ca5efc4711895dc32ac25896caa46e2aefe5e5ce423373"
---

Use [metadata](https://docs.stripe.com/api/metadata) to store your important data on Stripe objects with these common examples. The following use cases aren’t exhaustive; how you use metadata depends on your specific use cases.

#### Security tip

Don’t include sensitive data in `metadata`, such as PII, bank account details, or customer card details.

## Store IDs for objects or records

You can use metadata in Stripe objects to store IDs that belong to objects or records from your other systems. This allows you to build references between Stripe objects and their related resources from your other systems.

### Order or cart ID

When you create IDs to track your customers’ carts, you can store those IDs as metadata on [Checkout Sessions](https://docs.stripe.com/api/checkout/sessions). This allows you to use the related Stripe object to locate the associated cart in your system after the checkout process is complete.

Store the cart ID in the metadata of the Checkout Session after you create it:

`curl https://api.stripe.com/v1/checkout/sessions \  -u "`

`sk_test_REDACTED`

`:" \   --data-urlencode "success_url=[https://example.com/success](https://example.com/success)" \   -d mode=payment \  -d "line_items[0][price]=price_1MotwRLkdIwHu7ixYcPLm5uZ" \   -d "line_items[0][quantity]=1" \   -d "metadata[cart_id]=cart_6943"`

Then, you can view, update, or delete the ID on the `Checkout Session` object. It also appears in the events sent to your webhook endpoint that contain that Checkout Session (including the `checkout.session.completed` event).

`{   "id": "evt_1PYCL6CzbZon1zn9VivIehz7",   "object": "event",   "api_version": "2024-06-20",   "created": 1719948368,   "data": {     "object": {       "id": "cs_test_a1Znb7gdtlLEPzSi8qMIJzvsSPpIBMKFWovXx0h0O43WS411PpICgCqKjw",       "object": "checkout.session",       ...       "metadata": {         "cart_id": "cart_6943"       },       ...     }   },   ...   "type": "checkout.session.completed" }`

### Customer or CMS ID

You can associate the [Customers](https://docs.stripe.com/api/customers) you create in Stripe with your customer management system (CMS) records to help track and manage your customers.

Store the ID of the customer record from your CMS in the metadata of the Customer you create in Stripe.

`curl https://api.stripe.com/v1/customers \  -u "`

`sk_test_REDACTED`

`:" \  -d "name=Jenny Rosen" \  -d "metadata[cms_id]=cust_6573"`

Stripe includes this information in the events sent to your webhook endpoint that contain that Customer object. For example, when you receive `customer.updated` events, you can use the stored ID to identify the record you need to update in your CMS.

`{   "id": "evt_1PajAGCzbZon1zn9FUsn7IoG",   "object": "event",   "api_version": "2024-06-20",   "created": 1720551204,   "data": {     "object": {       "id": "cus_QRcNyZh9aZHXnI",       "object": "customer",       ...       "metadata": {         "cms_id": "cust_6573"       },       ...     }   },   ...   "type": "customer.updated" }`

## Track order fulfillment

Use metadata to store data that facilitates or tracks your order fulfillment processes.

### Price or Product ID on a payment intent

When you directly create [payment intents](https://docs.stripe.com/api/payment_intents), you can associate them with your [products](https://docs.stripe.com/api/products) or [prices](https://docs.stripe.com/api/prices) using metadata. This allows you to store the ID of the associated objects on the payment intent, which lacks an existing field that associates them with a price or product.

`curl https://api.stripe.com/v1/payment_intents \  -u "`

`sk_test_REDACTED`

`:" \  -d amount=2000 \  -d currency=usd \  -d "automatic_payment_methods[enabled]=true" \   -d "metadata[price_id]=price_1MoBy5LkdIwHu7ixZhnattbh" \   -d "metadata[product_id]=prod_NWjs8kKbJWmuuc"`

You can locate the ID of the associated object in events that include that payment intent, such as `payment_intent.succeeded` events. Then, pass the metadata from the event to your downstream processes (for example, order fulfillment or inventory management).

`{   "id": "evt_3PajIyCzbZon1zn90b9Wvsqf",   "object": "event",   "api_version": "2024-06-20",   "created": 1720551759,   "data": {     "object": {       "id": "pi_3PajIyCzbZon1zn901xQeOdi",       "object": "payment_intent",       ...       "metadata": {         "price_id": "price_1MoBy5LkdIwHu7ixZhnattbh",         "product_id": "prod_NWjs8kKbJWmuuc"       }       ...     }   },   ...   "type": "payment_intent.succeeded" }`

### Fulfillment status and tracking

After you begin your order fulfillment flow, you can use metadata to record the current fulfillment status on the associated Stripe object. This allows you to retrieve an object from Stripe, and receive both the payment status and fulfillment status simultaneously.

`curl https://api.stripe.com/v1/payment_intents \  -u "`

`sk_test_REDACTED`

`:" \  -d amount=2000 \  -d currency=usd \  -d "automatic_payment_methods[enabled]=true" \   -d "metadata[fulfillment_status]=fulfillment_not_started"`

To update the current fulfillment status:

`curl https://api.stripe.com/v1/payment_intents/{{INTENT_ID}} \  -u "`

`sk_test_REDACTED`

`:" \  -d "metadata[fulfillment_status]=shipping_label_created"`

## Track affiliate links

In [some cases](https://docs.stripe.com/metadata#exceptions), Stripe copies `metadata` from the original object to a related object. If you have affiliates hosting [Payment Links](https://docs.stripe.com/api/payment_links) on their sites and offer incentives for sales originating from those links, you can use this behavior in your affiliate tracking.

When you create payment links, you can populate `metadata` to track your affiliate:

`curl https://api.stripe.com/v1/payment_links \  -u "`

`sk_test_REDACTED`

`:" \  -d "line_items[0][price]=price_1MotwRLkdIwHu7ixYcPLm5uZ" \   -d "line_items[0][quantity]=1" \   -d "metadata[affiliate]=afl_7920"`

Every time a customer uses that link to complete a purchase, Stripe creates a [Checkout Session](https://docs.stripe.com/api/checkout/sessions) that inherits the metadata that you provided on the payment link. You can monitor `checkout.session.completed` events to receive notifications from Stripe when a customer completes a purchase. You can then pull your affiliate tracking details from the Checkout Session’s metadata to attribute the sale accurately.

`{  "id": "evt_1PajfeCzbZon1zn9S7pNlQkU",  "object": "event",  "api_version": "2024-06-20",  "created": 1720553150,  "data": {    "object": {       "id": "cs_test_a1zgRtgzjvamTgTnqMqIaqP6zehBIkaM03iYzxNjZiJ7FMDRRhibd5w3gL",       "object": "checkout.session",       ...       "metadata": {         "affiliate": "afl_7920"       },       ...     }   },   ...   "type": "checkout.session.completed" }`

## Store notes

You can use metadata to store notes on objects. For example, to create a note of a customer’s preferred call time, add metadata to the [Customer](https://docs.stripe.com/api/customers) object:

`curl https://api.stripe.com/v1/customers \  -u "`

`sk_test_REDACTED`

`:" \  -d "name=Jenny Rosen" \   --data-urlencode "metadata[call_window]=10:00 AM - 2:00 PM"`

To store a note that details why an [Invoice](https://docs.stripe.com/api/invoices) was voided, you can use the `metadata` on the `Invoice` object:

`curl https://api.stripe.com/v1/invoices/{{INVOICE_ID}} \  -u "`

`sk_test_REDACTED`

`:" \   --data-urlencode "metadata[void_reason]=Duplicate of Invoice #011"`

The placement of your metadata determines which event types contain the information you provide. Similarly, if you’re tracking certain event types in your integration, it determines where you place your metadata.

Certain object creation endpoints contain multiple fields for your metadata: one for storing metadata directly on the object being created, and others for setting metadata on downstream-created objects. Learn more about the [indirect metadata fields](https://docs.stripe.com/metadata#set-indirectly).

The following example creates a [Checkout Session](https://docs.stripe.com/api/checkout/sessions) that generates a subscription when completed. This uses the top-level `metadata` field, and the `subscription_data.metadata` field:

`curl https://api.stripe.com/v1/checkout/sessions \  -u "`

`sk_test_REDACTED`

`:" \   --data-urlencode "success_url=[https://example.com/success](https://example.com/success)" \   -d mode=subscription \  -d "line_items[0][price]=price_1MotwRLkdIwHu7ixYcPLm5uZ" \   -d "line_items[0][quantity]=1" \   -d "metadata[checkout_metadata]=Checkout Session metadata goes here" \  -d "subscription_data[metadata][subscription_metadata]=Subscription metadata goes here"`

You can set metadata on the object that you create (in this case, the Checkout Session). After your customer completes the checkout process, the metadata previously provided in `subscription_data.metadata` is set on the newly created [Subscription](https://docs.stripe.com/api/subscriptions) object. This determines which events include the metadata. For example, events that contain a Checkout Session, such as `checkout.session.completed`, contain values provided through the top-level `metadata` parameter.

`{   "id": "evt_1PakshCzbZon1zn9PlQwJYn0",   "object": "event",   "api_version": "2024-06-20",   "created": 1720557803,   "data": {     "object": {       "id": "cs_test_a1lsYmNYnEqQAxHT9knVy8v7u7m5ChjKtyB3M68ovMCjUQgCADsCkUviUU",       "object": "checkout.session",       ...       "metadata": {         "checkout_metadata": "Checkout Session metadata goes here"       },       ...     }   },   ...   "type": "checkout.session.completed" }`

Events that contain a `Subscription` object, such as `customer.subscription.created`, contain values provided through `subscription_data.metadata`. However, because that event contains a Subscription object, Stripe provides the values in the top-level `metadata` field on the Subscription object.

`{   "id": "evt_1PaksgCzbZon1zn9x9u3MTSC",   "object": "event",   "api_version": "2024-06-20",   "created": 1720557800,   "data": {     "object": {       "id": "sub_1PaksdCzbZon1zn9D6DQjr9L",       "object": "subscription",       ...       "metadata": {         "subscription_metadata": "Subscription metadata goes here"       },       ...     }   },   ...   "type": "customer.subscription.created" }`

You can access the metadata you provide in `subscription_data.metadata` in the [invoice](https://docs.stripe.com/api/invoices) events. This occurs because the subscription’s metadata is transferred to `subscription_details.metadata` on the `Invoice` objects created by the subscription.

`{   "id": "evt_1PaksgCzbZon1zn9wD24BlvY",   "object": "event",   "api_version": "2024-06-20",   "created": 1720557800,   "data": {     "object": {       "id": "in_1PaksdCzbZon1zn9Z4bl0z7k",       "object": "invoice",       ...       "subscription_details": {         "metadata": {           "subscription_metadata": "Subscription metadata goes here"         }         ...       }     }   },   ...   "type": "invoice.finalized" }`

Use metadata fields in Stripe to store data directly or store an external lookup key to access additional data from your own database, minimizing the information you need to retrieve.

### Store structured data

Metadata can accept any string, including those representing structured data such as JSON, up to [500 characters](https://docs.stripe.com/metadata#data). You can use it to store more data within your metadata fields, reducing the number of keys you need to access to retrieve all your information.

`curl https://api.stripe.com/v1/accounts \  -u "`

`sk_test_REDACTED`

`:" \   --data-urlencode "metadata[account_details]={\"sourcing_details\":{\"found_from\":\"web_search\",\"referrer\":\"user_123\",\"joined\":\"2024-01-01\"},\"tier_information\":{\"tier\":\"silver\",\"total_sales\":35,\"next_tier_at\":50,\"next_tier\":\"gold\"}}"`

### Store metadata externally

To associate more data with an object than the [500 characters](https://docs.stripe.com/metadata#data) the provided metadata fields allow, store the excess data in your own database. You can then use metadata to store the ID or lookup key for accessing that information. This approach is similar to storing the ID of any other record in your system.

`curl https://api.stripe.com/v1/accounts \  -u "`

`sk_test_REDACTED`

`:" \  -d "metadata[account_details_lookup_key]=rec_a1b2c3"`

You can use metadata with other Stripe APIs and products to enhance their flexibility and extensibility.

### Radar

You can write Radar rules to [reference metadata](https://docs.stripe.com/radar/rules/reference#metadata-attributes) values and use them to determine if a rule triggers its associated action for a transaction.

#### Perform initial review of customer transactions

You can set up a flow to flag a [customer’s](https://docs.stripe.com/api/customers) initial transaction for review, then update the customer’s details to omit subsequent transactions from review.

`curl https://api.stripe.com/v1/customers \  -u "`

`sk_test_REDACTED`

`:" \  -d "name=Jenny Rosen" \  -d "metadata[verified_customer]=false"`

`` Review if ::customer:verified_customer:: != `'true'` ``

`curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}} \  -u "`

`sk_test_REDACTED`

`:" \  -d "metadata[verified_customer]=true"`

Stripe only triggers this rule for payments if `verified_customer` is set to `false` on the customer. Customers who have that set to `true` aren’t affected.

#### Split testing rules

You can use metadata with Radar to create A/B testing scenarios for new rules, allowing you to evaluate a new rule’s effectiveness before implementing it across your entire customer base.

`curl https://api.stripe.com/v1/payment_intents \  -u "`

`sk_test_REDACTED`

`:" \  -d amount=2000 \  -d currency=usd \  -d "automatic_payment_methods[enabled]=true" \   -d "metadata[experiment_group]=treatment"`

`curl https://api.stripe.com/v1/payment_intents \  -u "`

`sk_test_REDACTED`

`:" \  -d amount=2000 \  -d currency=usd \  -d "automatic_payment_methods[enabled]=true" \   -d "metadata[experiment_group]=control"`

`` Block if ::experiment_group:: = `'treatment'` and :card_funding: = `'prepaid'` ``

Stripe only triggers this rule for payments that you label as part of the treatment group. It doesn’t affect payments set to `control` as their `experiment_group`.

### The Search API

Use the [Search API](https://docs.stripe.com/search#metadata) to query and filter results based on the metadata that you set on the [supported objects](https://docs.stripe.com/search#supported-query-fields-for-each-resource) you’re searching for.

For example, you can track your “premium” customers by adding metadata to the [Customer](https://docs.stripe.com/api/customers) object. To offer them exclusive promotions, use the Search API to identify customers marked as `premium`, then reach out to them with the promotion.

`curl https://api.stripe.com/v1/customers \  -u "`

`sk_test_REDACTED`

`:" \  -d "name=Jenny Rosen" \  -d "metadata[service_tier]=premium"`

`curl -G https://api.stripe.com/v1/customers/search \  -u "`

`sk_test_REDACTED`

`:" \   --data-urlencode "query=metadata['service_tier']:'premium'"`

Objects must be [indexed](https://docs.stripe.com/search#data-freshness) before they appear in results from the Search API. The objects won’t show up in search results until that indexing completes.
