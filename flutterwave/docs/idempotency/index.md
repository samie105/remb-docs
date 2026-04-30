---
title: "Idempotency"
source: "https://developer.flutterwave.com/docs/idempotency#"
canonical_url: "https://developer.flutterwave.com/docs/idempotency"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:32:46.922Z"
content_hash: "1cb879741e259bf3e1ebbe442ee4b43b224b63965de26b84a6c49a7dba0f9f09"
menu_path: ["Idempotency"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/webhooks/index.md", "title": "Webhooks"}
nav_next: {"path": "flutterwave/docs/testing/index.md", "title": "Testing"}
---

For all `POST` endpoints, include an idempotency key in the request header (`X-Idempotency-Key`). This ensures that repeated requests are treated as a single operation, preventing accidental duplicate transactions.

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/customers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "address":{
      "city":"Gotham",
      "country":"US",
      "line1":"221B Baker Street",
      "line2":"",
      "postal_code":"94105",
      "state":"Colorado"
   },
   "name":{
      "first":"King",
      "middle":"Leo",
      "last":"James"
   },
   "phone":{
      "country_code":"1",
      "number":"6313958745"
   },
   "email":"james@example.com"
}'
```

When a subsequent request is made with the same idempotency key, **we return the original response associated with the first request that used that key**. This ensures that no duplicate objects are created on our end.

For such requests, **the response will include the header `X-Idempotency-Cache-Hit: true` to indicate that the result was retrieved from an already existing idempotency key.**

1.  Always ensure that your transaction, transfer, customer creation, and refund requests are idempotent by including an **idempotency** key when creating these resources.
2.  We recommend using a **UUID** string as your idempotency key for each request to ensure uniqueness.
3.  Always retry on network errors or `5xx` status codes. It is safe to do so with the same key.

Updated 5 months ago

* * *
