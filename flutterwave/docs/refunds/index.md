---
title: "Refunds"
source: "https://developer.flutterwave.com/docs/refunds#"
canonical_url: "https://developer.flutterwave.com/docs/refunds"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:56.296Z"
content_hash: "60d35a4f213048bfb7cc9013c9d32c73bec4515e2f2feaadd3b0260bc519c78d"
menu_path: ["Refunds"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/settlements/index.md", "title": "Settlements"}
nav_next: {"path": "flutterwave/docs/chargebacks-1/index.md", "title": "Chargebacks"}
---

Refunds allow merchants to return funds to customers for various reasons, such as order cancellations or product unavailability. Using our API, you can seamlessly initiate **full** or **partial refunds**, track their status, and monitor refund trends.

Refunds may be initiated for several reasons. Common scenarios include:

1.  A customer requests a refund due to dissatisfaction with a product or service.
2.  A customer accidentally overpays (e.g., incorrect pricing or quantity).
3.  A customer pays for an out-of-stock or unavailable item.

To process a refund, send a request to the [refunds endpoint](https://developer.flutterwave.com/v4.0/reference/refunds_post) using the transaction `id`.

Your request must include:

-   `amount`: The exact amount to be refunded.
-   `reason`: A brief note explaining the refund (e.g., Order Cancelled).

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/refunds' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "amount":2000,
   "reason":"duplicate",
   "charge_id":"chg_Jwb2Y7ZbJQ"
}'
```

You'll get a response similar to this:

```json
{
  "message": "Refund Initiated",
  "data": {
    "id": "rfd_eHwAkSdZ48",
    "amount_refunded": 2000,
    "meta": {},
    "reason": "duplicate",
    "status": "completed",
    "charge_id": "chg_Jwb2Y7ZbJQ",
    "created_datetime": "2025-02-13T12:12:22.013525130Z"
  }
}
```

> ## 🚧
> 
> Partial refunds
> 
> To initiate a part or partial refund, ensure that the refund amount is smaller than the transaction amount. You can initiate several partial refunds on the same transaction provided that the sum of the individual refunds are equal to the original transaction amount.

The refund will be deducted from your available balance or the next settlement.

When a Refund is first initiated, its status is `new`. After some time, the refund is picked up for processing and its status changes to `pending`. If all goes well, the refund is completed and marked as`succeeded`, else, it fails and we update the `pending` status to `failed`.

To track the final status, choose one of the following methods:

-   **Callback URL**: Include a `callbackurl` field in your request. We'll notify this URL once the refund is completed or fails.
-   **Manually Status Check**: Query the [fetch refunds endpoint](https://developer.flutterwave.com/v4.0/reference/refunds_get) using the refund`id` to retrieve its current status.
-   **Webhooks**: If webhooks are enabled, we'll send a notification with the refund status to your webhook URL when processing completes.

Card refunds are completed between 3-15 days after the refund is initiated. Refunds to mobile money wallets take 3-5 days, while refunds to bank accounts are completed in 24 hours.

You can analyze your refund activity by retrieving a list of past refunds. Use filters when querying the Fetch Refunds endpoint to narrow results:

-   `page`: Page number to retrieve
-   `from`: Start date
-   `to`: End date
-   `size`: Number of results per page

```json
curl --request GET \
--url 'https://developersandbox-api.flutterwave.com/refunds?page=1&size=10' \
--header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: <YOUR_UNIQUE_TRACE_ID>' \
--header 'X-Idempotency-Key: <YOUR_UNIQUE_INDEMPOTENCY_KEY>' \
```

You'll get a response similar to this:

```json
{
  "status": "success",
  "message": "Refunds fetched",
  "meta": {
    "page_info": {
      "total": 3,
      "current_page": 1,
      "total_pages": 1
    }
  },
  "data": [
    {
      "id": "rfd_VBwFTccOHT",
      "amount_refunded": 2000,
      "meta": {},
      "reason": "duplicate",
      "status": "succeeded",
      "charge_id": "chg_ujfv5xWlpX",
      "created_datetime": "2025-02-07T11:08:17.517Z"
    },
    {
      "id": "rfd_9NHHGAilL6",
      "amount_refunded": 150,
      "meta": {},
      "reason": "duplicate",
      "status": "succeeded",
      "charge_id": "chg_5BBk3iB0oZ",
      "created_datetime": "2025-02-07T09:25:55.555Z"
    },
    {
      "id": "rfd_tSl3PQV6Sc",
      "amount_refunded": 150,
      "meta": {},
      "reason": "duplicate",
      "status": "succeeded",
      "charge_id": "chg_HvYp0jE07i",
      "created_datetime": "2025-02-06T09:31:52.243Z"
    }
  ]
}
```

Updated 7 months ago

* * *
