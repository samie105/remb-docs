---
title: "Include-dependent response values in API v2"
source: "https://docs.stripe.com/api-includable-response-values"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:51:55.693Z"
content_hash: "959fb09cc1ea3b809aba85d592800aa7adc30c5bbfc93817d525a7ce90d0c5df"
---

Some API v2 responses contain null values for certain properties by default, regardless of their actual values. That reduces the size of response payloads while maintaining the basic response structure. To retrieve the actual values for those properties, specify them in the `include` array request parameter.

To determine whether you need to use the `include` parameter in a given request, look at the request description. The `include` parameter’s enum values represent the response properties that depend on the `include` parameter.

#### Endpoint dependency

Whether a response property defaults to null depends on the request endpoint, not the object that the endpoint references. If multiple endpoints return data from the same object, a particular property can depend on `include` in one endpoint and return its actual value by default for a different endpoint.

A hash property can depend on a single `include` value, or on multiple `include` values associated with its child properties. For example, when updating an Account, to return actual values for the entire `identity` hash, specify `identity` in the `include` parameter. Otherwise, the `identity` hash is null in the response. However, to return actual values for the `configuration` hash, you must specify individual configurations in the request. If you specify at least one configuration, but not all of them, specified configurations return actual values and unspecified configurations return null. If you don’t specify any configurations, the `configuration` hash is null in the response.

The following example updates an `Account` to add the `customer` and `merchant` configurations, but doesn’t specify any properties in the `include` parameter:

`curl -X POST https://api.stripe.com/v2/core/accounts/acct_123 \  -H "Authorization: Bearer` 

`sk_test_REDACTED`

`" \  -H "Stripe-Version: preview" \   --json '{     "configuration": {         "customer": {             "capabilities": {                 "automatic_indirect_tax": {                     "requested": true                 }             }         },         "merchant": {             "capabilities": {                 "card_payments": {                     "requested": true                 }             }         }     }   }'`

The response might look like this:

`{   "id": "acct_123",   "object": "v2.core.account",   "applied_configurations": [     "customer",     "merchant"   ],   "configuration": null,   "contact_email": "furever@example.com",   "created": "2025-06-09T21:16:03.000Z",   "dashboard": "full",   "defaults": null,   "display_name": "Furever",   "identity": null,   "livemode": true,   "metadata": {},   "requirements": null }`

This example makes the same request, but specifies `configuration.customer` and `identity` in the `include` parameter:

`curl -X POST https://api.stripe.com/v2/core/accounts/acct_123 \  -H "Authorization: Bearer` 

`sk_test_REDACTED`

`" \  -H "Stripe-Version: preview" \   --json '{     "configuration": {         "customer": {             "capabilities": {                 "automatic_indirect_tax": {                     "requested": true                 }             }         },         "merchant": {             "capabilities": {                 "card_payments": {                     "requested": true                 }             }         }     },     "include": [         "configuration.customer",         "identity"     ]   }'`

The response includes details about the `customer` configuration and `identity`, but returns null for all other configurations:

`{   "id": "acct_123",   "object": "v2.core.account",   "applied_configurations": [     "customer",     "merchant"   ],   "configuration": {     "customer": {       "automatic_indirect_tax": {         ...       },       "billing": {         ...       },       "capabilities": {         ...       },       ...     },     "merchant": null,     "recipient": null   },   "contact_email": "furever@example.com",   "created": "2025-06-09T21:16:03.000Z",   "dashboard": "full",   "defaults": null,   "display_name": "Furever",   "identity": {     "business_details": {       "doing_business_as": "FurEver",       "id_numbers": [         {           "type": "us_ein"         }       ],       "product_description": "Saas pet grooming platform at furever.dev using Connect embedded components",       "structure": "sole_proprietorship",       "url": "[http://accessible.stripe.com](http://accessible.stripe.com/)"     },     "country": "US"   },   "livemode": true,   "metadata": {},   "requirements": null }`
