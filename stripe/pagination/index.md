---
title: "How pagination works"
source: "https://docs.stripe.com/pagination"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:54:38.162Z"
content_hash: "f059369c72172ec1adaba634990e321eba6d26554271961935234518c4c19449"
---

## Learn how to paginate results for list and search endpoints.

The Stripe API has list and search endpoints that can return multiple objects, such as listing Customers or searching for PaymentIntents. To mitigate negative impacts to performance, these endpoints don’t return all results at once. Instead, Stripe returns one page of results per API call, with each page containing up to 10 results by default. Use the [limit](https://docs.stripe.com/api/pagination#pagination-limit) parameter to change the number of results per page.

For example, this is an API request to list Customers, with a `limit` of 3:

`curl -G https://api.stripe.com/v1/customers \  -u "`

`sk_test_REDACTED`

`:" \  -d limit=3`

The response from Stripe contains one page with 3 results:

`{   "data": [     {       "id": "cus_005",       "object": "customer",       "name": "John Doe",     },     {       "id": "cus_004",       "object": "customer",       "name": "Jane Doe",     },     {       "id": "cus_003",       "object": "customer",       "name": "Jenny Rosen",     },   ],   "has_more": true,   /* ... */ }`

Keep in mind the following details when using these endpoints:

*   Objects are inside the `data` property.
*   Objects are in reverse chronological order, meaning the most recently created object is the first one.
*   The `has_more` property indicates if there are additional objects that weren’t returned in this request.

Instead of looping over the `data` array to go through objects, you should paginate results. This prevents you from missing some objects when the [has\_more](https://docs.stripe.com/api/pagination#pagination-has_more) parameter is `true`.

To retrieve all objects, use the auto-pagination feature. This automatically makes multiple API calls until `has_more` becomes `false`.

#### Note

When using auto-pagination with a list endpoint and setting [ending\_before](https://docs.stripe.com/api/pagination#pagination-ending_before), the results are in chronological order, meaning the most recently created customer is the last one.

Follow these steps to manually paginate results. This process is different when calling a list endpoint or a search endpoint.

1.  Make an API call to list the objects that you want to find.

`curl https://api.stripe.com/v1/customers \  -u "`

`sk_test_REDACTED`

`:"`

1.  In the response, check the value of [has\_more](https://docs.stripe.com/api/pagination#pagination-has_more):

*   If the value is `false`, you’ve retrieved all the objects.
*   If the value is `true`, get the ID of the last object returned, and make a new API call with the [starting\_after](https://docs.stripe.com/api/pagination#pagination-starting_after) parameter set.

Repeat this step until you’ve retrieved all of the objects that you want to find.

`curl -G https://api.stripe.com/v1/customers \  -u "`

`sk_test_REDACTED`

`:" \  -d starting_after={{LAST_CUSTOMER_ID}}`
