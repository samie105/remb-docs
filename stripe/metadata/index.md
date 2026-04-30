---
title: "Metadata"
source: "https://docs.stripe.com/metadata"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:53:58.152Z"
content_hash: "478e58663c7578d33ceda017c617904c76abd67251e282469f636d70b0bb974b"
---

[Metadata](https://docs.stripe.com/api/metadata) is an attribute on certain Stripe objects that lets you store more information, structured as key-value pairs, to these objects for your own use and reference. For example, you can store your user’s unique identifier from your system on a [Stripe Customer](https://docs.stripe.com/api/customers) object.

## Configuration

### Data

You can add 50 total key-value pairs within these data limits:

*   **key**: 40 character limit. Square brackets (`[` `]`) can’t be included in keys.
*   **value**: 500 character limit.

If your system requires more space than this, store your data in your external database and use a key-value pair to store the external object’s `ID` in `metadata`.

Unless you use metadata with [Radar](https://docs.stripe.com/radar), Stripe doesn’t use metadata—for example, to authorize or decline a charge. Additionally, metadata isn’t visible to your customers unless you choose to show it.

#### Security tip

Never store sensitive information, such as bank account information or credit card details, to metadata.

### Requests

Stripe only returns metadata when you use a [secret key](https://docs.stripe.com/keys#obtain-api-keys) in your requests. We redact metadata from objects in response to publishable key requests, such as Stripe.js or Mobile SDKs client-side requests.

Add key-values pairs to metadata, update metadata values, and replace keys using the API. You can combine different actions into a single request to perform multiple metadata additions, updates, and deletions simultaneously.

### Add key-value pairs

To add key-value pairs to metadata when creating an object, provide the keys and values in the object creation request.

`curl https://api.stripe.com/v1/customers \  -u "`

`sk_test_REDACTED`

`:" \  -d "name=Jenny Rosen" \  -d "metadata[cms_id]=6573"`

`{   "id": "cus_NffrFeUfNV2Hib",   "object": "customer",   ...   "metadata": {     "cms_id": "6573"   },   ... }`

### Add key-value pairs to existing metadata

To add key-value pairs to an existing object’s metadata, provide the keys and values in an update request. This parameter uses a merge mechanism, which allows you to add new key-value pairs to an object in an update call without affecting any existing metadata. For example, if a `Customer` object has `key1` and `key2`, when you update it to add `key3`, the updated object contains all three keys.

`curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}} \  -u "`

`sk_test_REDACTED`

`:" \  -d "metadata[loyalty_program]=no"`

`{   "id": "cus_NffrFeUfNV2Hib",   "object": "customer",   ...   "metadata": {     "cms_id": "6573"   },   ... }`

`{   "id": "cus_NffrFeUfNV2Hib",   "object": "customer",   ...   "metadata": {       "loyalty_program": "no",       "cms_id": "6573"   },   ... }`

### Update metadata values

To update the value for an existing key in metadata, pass in the new value using the existing key. For example, you can update a [Customer](https://docs.stripe.com/api/customers) object with an existing key-value pair of `"loyalty_program": "no"` to`"loyalty_program": "yes"`.

`curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}} \  -u "`

`sk_test_REDACTED`

`:" \  -d "metadata[loyalty_program]=yes"`

`{   "id": "cus_NffrFeUfNV2Hib",   "object": "customer",   ...   "metadata": {     "loyalty_program": "no"   },   ... }`

`{   "id": "cus_NffrFeUfNV2Hib",   "object": "customer",   ...   "metadata": {     "loyalty_program": "yes"   },   ... }`

### Update metadata keys

To update a key that has an existing value, delete the key and pass its value to a new key. For example, you can update a [Customer](https://docs.stripe.com/api/customers) object to [delete](https://docs.stripe.com/metadata#delete-single-key) its `"loyalty_program"` key and pass the key’s value of `"yes"` to a new `"rewards_program"` key.

`curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}} \  -u "`

`sk_test_REDACTED`

`:" \  -d "metadata[loyalty_program]=" \   -d "metadata[rewards_program]=yes"`

`{   "id": "cus_NffrFeUfNV2Hib",   "object": "customer",   ...   "metadata": {     "loyalty_program": "yes"   },   ... }`

`{   "id": "cus_NffrFeUfNV2Hib",   "object": "customer",   ...   "metadata": {     "rewards_program": "yes"   },   ... }`

Delete a single key or an entire set of keys using the API.

### Delete a single key

Pass in the key with an empty string as the value to remove the key from the metadata.

`curl https://api.stripe.com/v1/customers/{{CUSTOMER_ID}} \  -u "`

`sk_test_REDACTED`

`:" \  -d "metadata[loyalty_program]=yes" \   -d "metadata[loyalty_member_id]="`

`{   "id": "cus_NffrFeUfNV2Hib",   "object": "customer",   ...   "metadata": {     "loyalty_program": "yes",     "loyalty_member_id": "12345678"   },   ... }`

`{   "id": "cus_NffrFeUfNV2Hib",   "object": "customer",   ...   "metadata": {     "loyalty_program": "yes"   },   ... }`

### Delete all keys

Pass an empty object as the value for the `metadata` attribute to delete all of the keys simultaneously.

`curl https://api.stripe.com/v1/customers/`

`{{CUSTOMER_ID}}`

  `-u sk_test_REDACTED -d "metadata"=""`

`{   "id": "cus_NffrFeUfNV2Hib",   "object": "customer",   ...   "metadata": {     "loyalty_program": "yes",     "loyalty_member_id": "12345678"   },   ... }`

`{   "id": "cus_NffrFeUfNV2Hib",   "object": "customer",   ...   "metadata": {}   ... }`

An object’s metadata doesn’t automatically copy to related objects. To view an object’s metadata, you must inspect that object. To retrieve metadata from a related object, build custom logic to find and inspect the related object. To explicitly copy metadata from one object to another, you need to build your own flow.

### Exceptions

In certain cases, we copy metadata from one object to another for backwards compatibility and other unique scenarios.

Object mapping

Description

[PaymentIntent](https://docs.stripe.com/api/payment_intents) to [Charge](https://docs.stripe.com/api/charges)

When a PaymentIntent creates a Charge, the metadata copies to the Charge in a one-time snapshot. Updates to the PaymentIntent’s metadata won’t apply to the Charge.

[Payment Link](https://docs.stripe.com/api/payment_links/payment_links) to [Checkout Session](https://docs.stripe.com/api/checkout/sessions)

When a Payment Link creates a Checkout Session, the metadata copies to the Checkout Session in a one-time snapshot. Updates to the Payment Link’s metadata won’t apply to the Checkout Session.

[Subscription](https://docs.stripe.com/api/subscriptions) to [Invoice](https://docs.stripe.com/api/invoices)

When a Subscription creates an Invoice, the metadata copies to the Invoice object’s [parent.subscription\_details.metadata](https://docs.stripe.com/api/invoices/object#invoice_object-parent-subscription_details-metadata) attribute in a one-time snapshot. Updates to the subscription’s metadata won’t apply to the Invoice.

[Subscription](https://docs.stripe.com/api/subscriptions) to [Invoice Line Item](https://docs.stripe.com/api/invoice-line-item/object)

When an Invoice Line Item’s [type](https://docs.stripe.com/api/invoice-line-item/object#invoice_line_item_object-type) is set to `subscription`, it presents the subscription’s current metadata.

## Set metadata indirectly

Some endpoints accept a `metadata` parameter nested inside of another parameter. You can use these parameters when you create an object to set metadata on an underlying object. For example, you can use `payment_intent_data.metadata` when you create a Checkout Session to provide and set metadata on the underlying PaymentIntent the session creates.

## Events and webhook endpoints

When Stripe sends an [Event](https://docs.stripe.com/api/events) to your [webhook endpoint](https://docs.stripe.com/webhooks), it includes the corresponding object and any metadata the object contains. This allows your webhook handler to receive any metadata that you set on Stripe objects and pass it to downstream processes, such as order fulfillment.

For example, to include a cart ID when a customer makes a purchase using a [Checkout Session](https://docs.stripe.com/api/checkout/sessions), provide it as metadata when you create the Checkout Session:

`curl https://api.stripe.com/v1/checkout/sessions \  -u "`

`sk_test_REDACTED`

`:" \   --data-urlencode "success_url=[https://example.com/success](https://example.com/success)" \   -d mode=payment \  -d "line_items[0][price]=price_1MotwRLkdIwHu7ixYcPLm5uZ" \   -d "line_items[0][quantity]=1" \   -d "metadata[cart_id]=6943"`

When the customer completes the checkout process, Stripe sends a [checkout.session.completed](https://docs.stripe.com/api/events/types#event_types-checkout.session.completed) event containing the Checkout Session object’s metadata to your webhook endpoint. You must configure your webhook to listen for that event so you can access the metadata and use it when processing data.

`{   "id": "evt_1P8pqUAgEBCHsfP6JfNctbLv",   "object": "event",   "api_version": "2022-11-15",   "created": 1713903702,   "data": {     "object": {       "id": "cs_test_a1aDQuoXLoddIOV9iOvZRgKAtPoRIfFkYHBWxF9AQAPlGG3STB1ndqqaUw",       "object": "checkout.session",       ...       "metadata": {         "cart_id": "6943"       },`

You can search for existing metadata on supported objects by using specific formatting. This includes searching for records with a specific value for a metadata field or checking if a metadata key is present on an object. Learn more about [searching for metadata](https://docs.stripe.com/search#metadata).

## Prevent fraud with metadata and Radar

Use metadata with Radar to create custom rules that help prevent fraud. Learn more about [Radar metadata attributes](https://docs.stripe.com/radar/rules/reference#metadata-attributes).
