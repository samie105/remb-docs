---
title: "Chargebacks"
source: "https://developer.flutterwave.com/docs/chargebacks-1#"
canonical_url: "https://developer.flutterwave.com/docs/chargebacks-1"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:58.658Z"
content_hash: "88746610a8f4d7d9d3468764a531ea0ee58635bc77ab2b1dcce4d35477e6a3f2"
menu_path: ["Chargebacks"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/refunds/index.md", "title": "Refunds"}
nav_next: {"path": "flutterwave/docs/reporting-vat/index.md", "title": "Reporting VAT"}
---

Customers may dispute a transaction if they do not receive the value they paid for. When this happens, a **chargeback** is initiated through the customer’s bank and must be promptly addressed by the merchant.

As a merchant, you can either accept the chargeback (and refund the customer) or **dispute** it by submitting compelling evidence that the transaction was valid.

  

1.  The customer contacts their **issuing bank** to initiate a dispute.
2.  The issuing bank raises a **chargeback request**, which is routed through Flutterwave to the merchant.
3.  A **lien** (hold) is placed on the disputed amount in the merchant's settlement or payout balance.
4.  The merchant reviews and **responds** to the chargeback.
    -   If the merchant **does not respond**, the amount is debited automatically.
    -   If the merchant responds, Flutterwave enters into arbitration with the bank.
5.  Based on the outcome:
    -   If the merchant **wins**, the lien is lifted, and the amount is released.
    -   If the chargeback is **upheld**, the amount is debited permanently.

When a chargeback is raised, follow these steps:

1.  **Review the Disputed Transaction**: Examine the details and gather evidence (e.g. receipts, delivery proof, service logs).
2.  **Decide on your Response**: Based on your review, decide how to proceed:
    1.  **Accept** the chargeback if the customer did not receive the expected value.
    2.  **Dispute** it if you have **proof of value delivery** or **authorization**.

If you decide to accept a chargeback, you'll need to retrieve the relevant chargeback details. There are three ways to fetch it:

-   Flutterwave notifies you about chargebacks via your email. You can get the `chargeback_id` from the email sent.
-   We also send webhooks to your server when a chargeback is raised. This notification service is available on request.
-   Query the [get all chargeback endpoint](https://developer.flutterwave.com/v4.0/reference/chargebacks_list) to fetch details of all chargebacks raised against your account.

```json
curl  --request GET \  
--url 'https://developersandbox-api.flutterwave.com/chargebacks' \
--header 'X-Trace-Id: {{UNIQUE_TRACE_ID}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API_ACCESS_TOKEN}}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Chargebacks fetched",
    "meta": {
        "page_info": {
            "total": 2,
            "current_page": 1,
            "total_pages": 1
        }
    },
    "data": [
        {
            "id": "chb_KJ5rAYbkvt",
            "charge_id": "chg_RjxhF6IgxQ",
            "amount": 200,
            "meta": {},
            "stage": "new",
            "status": "accepted",
            "type": "local",
            "due_datetime": "2025-01-28T11:45:06.714Z",
            "created_datetime": "2025-01-27T11:45:06.715Z",
            "updated_datetime": "2025-01-27T11:45:31.190Z",
            "comment": "Chargeback accepted after review. Issue resolved in favor of the customer."
        },
        {
            "id": "chb_QYZyN5BBvE",
            "charge_id": "chg_Ppj3WCkVHk",
            "amount": 200,
            "meta": {},
            "stage": "new",
            "status": "declined",
            "type": "local",
            "due_datetime": "2025-01-28T10:13:41.845Z",
            "created_datetime": "2025-01-27T10:13:41.845Z",
            "updated_datetime": "2025-01-27T11:45:20.126Z",
            "uploaded_proof": "https://www.example-website.com/media/proof.png",
            "comment": "We provided value to the customer for the reported transaction. See image in proof for more information"
        }
    ]
}
```

Then accept the chargeback by sending a request to the [update chargeback endpoint](https://developer.flutterwave.com/v4.0/reference/chargeback_put) with the `status` set to `"accepted"`.

```json
curl  --request PUT \
--url 'https://developersandbox-api.flutterwave.com/chargebacks/chb_KJ5rAYbkvt' \
--header 'X-Trace-Id: {{UNIQUE_TRACE_ID}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API_ACCESS_TOKEN}}' \
--data '
{
  "status": "accepted",
  "comment": "Chargeback accepted after review. Issue resolved in favor of the customer."
}
'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Chargeback updated",
    "data": {
        "id": "chb_KJ5rAYbkvt",
        "charge_id": "chg_RjxhF6IgxQ",
        "amount": 200,
        "meta": {},
        "stage": "new",
        "status": "accepted",
        "type": "local",
        "due_datetime": "2025-01-28T11:45:06.714Z",
        "created_datetime": "2025-01-27T11:45:06.715Z",
        "updated_datetime": "2025-01-27T11:45:31.190Z",
        "comment": "Chargeback accepted after review. Issue resolved in favor of the customer."
    }
}
```

When declining a chargeback, use the chargeback `id` and the link to the uploaded proof to decline the chargeback.

Send a request to the [update chargeback endpoint](https://developer.flutterwave.com/v4.0/reference/chargeback_put) with the `status` set to `declined` and the link to the evidence passed as `uploaded_proof`.

```json
curl --request PUT\
--url 'https://developersandbox-api.flutterwave.com/chargebacks/chb_QYZyN5BBvE' 
--header 'X-Trace-Id: {{UNIQUE_TRACE_ID}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API_ACCESS_TOKEN}}' \
--data '
{
  "status": "declined",
  "uploaded_proof": "https://www.example-website.com/media/proof.png",
  "comment": "We provided value to the customer for the reported transaction. See image in proof for more information"
}
'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Chargeback updated",
    "data": {
        "id": "chb_QYZyN5BBvE",
        "charge_id": "chg_Ppj3WCkVHk",
        "amount": 200,
        "meta": {},
        "stage": "new",
        "status": "declined",
        "type": "local",
        "due_datetime": "2025-01-28T10:13:41.845Z",
        "created_datetime": "2025-01-27T10:13:41.845Z",
        "updated_datetime": "2025-01-27T10:26:18.382Z",
        "uploaded_proof": "https://www.example-website.com/media/proof.png",
        "comment": "We provided value to the customer for the reported transaction. See image in proof for more information"
    }
}
```

When a chargeback is initiated, Flutterwave will update you at each stage of the process. Below are the statuses to be aware of:

| Status | Meaning |
| --- | --- |
| `initiated` | The customer's bank has raised a chargeback against Flutterwave’s acquirer bank. The right amount is withheld from the merchant's balance, and the merchant is notified. |
| `pending` | Flutterwave has notified the merchant, but no action has been taken yet. |
| `accepted` | The merchant has accepted the chargeback. |
| `declined` | The merchant denied the chargeback with a claim of proof. |
| `won` | The merchant’s proof of denying the claim has been accepted and the funds are released. |
| `lost` | The dispute failed, or a lack of response from the merchant before the due date (48 hours). This means the customer will receive a refund. |
| `reversed` | The amount withheld from the merchant's balance has been restored. |

As part of the dispute resolution process, Flutterwave keeps you informed throughout each stage. Here are the important stages in the process:

| Status | Meaning |
| --- | --- |
| `new` | A new chargeback with no previous occurrence. |
| `second` | A subsequent chargeback on the same transaction after closure. |
| `pre-arbitration` | Final opportunity to resolve the dispute before full arbitration. Allows submission of new evidence. |
| `arbitration` | The chargeback dispute has escalated to the card schemes or issuing bank for final resolution. |
| `invalid` | The chargeback was found to be invalid due to incorrect parameters or timing. |

You can simulate chargebacks during testing to understand how your application handles them.

To initiate a test chargeback, send a request to the [create chargeback endpoint](https://developer.flutterwave.com/v4.0/reference/chargebacks_post) with the `charge_id`, `amount`, transaction `type` (local or international), and chargeback `expiry`.

> ## 🚧
> 
> Available on Sandbox Only
> 
> The create chargeback endpoint is only available in Sandbox. Do not use in production.

When sending the request, ensure that:

-   The `charge_id` must match the ID of a previously completed test payment.
-   The `amount` must equal the full transaction amount.

```json
curl  --request POST  \
--url 'https://developersandbox-api.flutterwave.com/chargebacks' \
--header 'X-Trace-Id: {{UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{UNIQUE_IDEMPOTENCY_KEY}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API_ACCESS_TOKEN}}' \
--data '
{
  "charge_id": "chg_Ppj3WCkVHk",
  "amount": 200,
  "type": "local",
  "expiry": 24
}
'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Chargeback created",
    "data": {
        "id": "chb_QYZyN5BBvE",
        "charge_id": "chg_Ppj3WCkVHk",
        "amount": 200,
        "meta": {},
        "stage": "new",
        "status": "initiated",
        "type": "local",
        "due_datetime": "2025-01-28T10:13:41.845073299Z",
        "created_datetime": "2025-01-27T10:13:41.845153199Z",
        "updated_datetime": "2025-01-27T10:13:41.845153199Z"
    }
}
```

Updated 7 months ago

* * *
