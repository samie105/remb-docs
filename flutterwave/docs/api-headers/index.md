---
title: "Supported Request Headers"
source: "https://developer.flutterwave.com/docs/api-headers#"
canonical_url: "https://developer.flutterwave.com/docs/api-headers"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:32:38.144Z"
content_hash: "2d860513da1b84aad124611fff727a7576ab49ae42d582ca5fbdab930a56501b"
menu_path: ["Supported Request Headers"]
section_path: []
tab_variants: ["Example","401 Unauthorized"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/authentication/index.md", "title": "Authentication"}
nav_next: {"path": "flutterwave/docs/encryption/index.md", "title": "Encryption"}
---

## Supported Request Headers

Correctly use API headers in your requests.

In our v4 API, we've introduced some changes to how request headers work. Each header serves a specific purpose and helps us process your request more efficiently. In this section, we’ll walk through each one and explain how to use them in your requests.

> ## 📘
> 
> Prerequisites
> 
> We assume you're familiar with APIs and have used them before. If you're new to APIs, [this beginner-friendly guide](https://flutterwave.com/us/blog/getting-started-with-apis) can help you get started.

Your API requests should include the following headers:

1.  `Authorization`,
2.  `X-Idempotency-Key`.
3.  `Content-Type`,
4.  `X-Trace-Id`,
5.  `X-Scenario-Key`.

  

> ## 🚧
> 
> Generating Tokens
> 
> See the [authentication section](https://developer.flutterwave.com/v4.0/docs/authentication) to learn how to generate your token and use this header.

Use this header to securely pass your access token along with your request. We use it to verify your identity and access level. If the token is missing or invalid, you'll get a `401 Unauthorized` error.

#### Example

```curl
curl --location 'https://developersandbox-api.flutterwave.com/customers?page=1' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json'
```

```json
{
    "status": "failed",
    "error": {
        "type": "UNAUTHORIZED",
        "code": "10401",
        "message": "Unauthorized"
    }
}
```

#### 401 Unauthorized

```curl
curl --location 'https://developersandbox-api.flutterwave.com/customers?page=1' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json'
```

```json
{
    "status": "failed",
    "error": {
        "type": "UNAUTHORIZED",
        "code": "10401",
        "message": "Unauthorized"
    }
}
```

This header helps prevent accidental duplicate transactions. If your request is retried (due to a timeout or network issue), it lets us process the request just once.

1.  It must be a string using only alphanumeric ASCII characters.
2.  Its length should be between 12 and 255 characters.

```curl
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
}
'
```

> ## 🚧
> 
> Distinct Idempotency keys
> 
> Each `X-Idempotency-Key` must be unique per request. If you reuse a key, we’ll return the original response from the first request instead of processing a new one.

Set this header to `application/json` to let our servers know to expect JSON data. This helps us read and respond to your requests correctly.

```curl
curl --location 'https://developersandbox-api.flutterwave.com/customers?page=1' \
--header 'Content-Type: application/json'
```

The `X-Trace-Id` header helps track and debug API requests by assigning a unique identifier to each request.

When you send a request and include a trace ID, our servers log this ID and attach it to responses, helping you track the request’s flow. If an issue occurs, you can provide this ID to our support team for faster troubleshooting.

1.  It must be a string using only alphanumeric ASCII characters.
2.  Its length should be between 12 and 255 characters.

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/customers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
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
}
'
```

  

> ## 🚧
> 
> Scenario Keys
> 
> See the [Testing section](https://developer.flutterwave.com/v4.0/docs/testing) for details on how to use this header.

This header lets you simulate different responses for testing purposes. You can mock scenarios like successful payments or failed transfers without changing your code.

If you pass an invalid key, we'll default to a `pending` status, which simulates an incomplete payment.

Updated 5 months ago

* * *
