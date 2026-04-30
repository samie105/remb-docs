---
title: "Transfer Orchestrator"
source: "https://developer.flutterwave.com/docs/direct-transfer-flow#"
canonical_url: "https://developer.flutterwave.com/docs/direct-transfer-flow"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:32.580Z"
content_hash: "06f416b271809e8f9333c5391912226b775e2739c6660064765a9c889c2f8ae3"
menu_path: ["Transfer Orchestrator"]
section_path: []
tab_variants: ["Source Currency","Destination Currency"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/general-transfer-flow/index.md", "title": "General Transfer Flow"}
nav_next: {"path": "flutterwave/docs/bank-transfer/index.md", "title": "Bank Account Transfers"}
---

Unlike the general transfer flow, which requires you to create recipient and sender entities separately, the direct transfer flow lets you set up both in a single request.

This flow has two key steps:

1.  Initiate the transfer on the transfer type.
2.  Verify the transfer status.

Before you start, go through our [quickstart](https://developer.flutterwave.com/v4.0/docs/quick-start) section. It covers essential setup steps for using our APIs.  
You need the following setup to follow this guide:

-   [API credentials](https://app.flutterwave.com/login) (client ID and client secret) for authenticating your requests.
-   A [webhook](https://developer.flutterwave.com/v4.0/docs/webhooks) URL to receive payment status updates.
-   Whitelist your IP addresses
-   Ensure your balance has sufficient funds. You can fund your balance using one of the following methods:
    -   Directly funding via [collections](https://developer.flutterwave.com/v4.0/docs/introduction-1).
    -   Indirect funding by converting funds from a different currency balance (i.e., wallet-to-wallet transfers).

To initiate a direct transfer, send a transfer request to the [Create direct transfer endpoint](https://developer.flutterwave.com/v4.0/reference/direct_transfers_post) with the following parameters:

-   `action`: Specifies how the transfer should be processed. Accepted values are: `instant`, `deferred`, or `scheduled`.
-   `type`: Specifies the transfer method. Available methods are `bank`, `mobile_moeny`, and `wallet`.
-   `payment_instruction`: An object containing details of the payment, including:
    -   `amount`,
    -   `source_currency`,
    -   `recipient` object,
    -   `sender` object (optional)

Below are sample requests based on the possible transfer `action`:

To transfer the funds immediately, send a request to the [Create a direct transfer endpoint](https://developer.flutterwave.com/v4.0/reference/direct_transfers_post).

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "payment_instruction": {
    "source_currency": "NGN",
    "amount": {
      "applies_to": "destination_currency",
      "value": 50000
    },
    "recipient": {
      "bank": {
        "account_number": "0122333334",
        "code": "044"
      }
    },
    "destination_currency": "NGN"
  },
  "type": "bank",
  "reference": "574874568ufdgjhvbjhcdbchb"
}'
```

You'll get a response similar to this:

```json
{
  "status": "success",
  "message": "Transfer created",
  "data": {
    "id": "trf_pGoKPGH7rEgY4v",
    "type": "bank",
    "reference": "574874568ufdgjhvbjhcdbchb",
    "status": "NEW",
    "source_currency": "NGN",
    "destination_currency": "NGN",
    "amount": {
      "value": 50000,
      "applies_to": "destination_currency"
    },
    "recipient": {
      "type": "bank",
      "bank": {
        "account_number": "0122333334",
        "code": "044"
      }
    },
    "meta": {},
    "created_datetime": "2024-12-05T12:36:20.069512926Z"
  }
}
```

To initiate a direct transfer that will be processed later, send a request similar to the instant transfer, but set the action parameter to `deferred`.

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "deferred",
  "payment_instruction": {
    "source_currency": "NGN",
    "amount": {
      "applies_to": "destination_currency",
      "value": 50000
    },
    "recipient": {
      "bank": {
        "account_number": "0122333334",
        "code": "044"
      }
    },
    "destination_currency": "NGN"
  },
  "type": "bank",
  "reference": "57487456fff8ufdgjihvbjhcdbchb"
}'
```

You'll get a response similar to this:

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_Pd6KueVSrrUiBF",
      "type":"bank",
      "action":"deferred",
      "reference":"57487456fff8ufdgjihvbjhcdbchb",
      "status":"NEW",
      "source_currency":"NGN",
      "destination_currency":"NGN",
      "amount":{
         "value":50000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"bank",
         "id":"rcb_1IkjUDnrt1",
         "name":{
            "first":"Ajadi",
            "last":"Jackson"
         },
         "currency":"NGN",
         "bank":{
            "account_number":"0122333334",
            "code":"044"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T10:32:22.457Z"
   }
}
```

To **complete a deferred transfer**, call the [update transfer endpoint](https://developer.flutterwave.com/v4.0/reference/transfer_put), pass the transfer `id`, and update the action parameter by setting `action` to `instant` to process the transfer or set it to `close` to cancel it.

To schedule a transfer for a future date, set the action parameter to `scheduled` and include a `disburse_option` with the desired datetime and timezone.

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "scheduled",
  "disburse_option": {
    "date_time": "2025-10-25 13:52:30",
    "timezone": "UTC"
  },
  "payment_instruction": {
    "source_currency": "NGN",
    "amount": {
      "applies_to": "destination_currency",
      "value": 50000
    },
    "recipient": {
      "bank": {
        "account_number": "0122333334",
        "code": "044"
      }
    },
    "destination_currency": "NGN"
  },
  "type": "bank",
  "reference": "57487456fffi8ufdgjhvbjhcdbchbfff"
}'
```

You'll get a response similar to this:

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_PfQSOvcuyET5Di",
      "type":"bank",
      "action":"scheduled",
      "reference":"57487456fffi8ufdgjhvbjhcdbchbfff",
      "status":"NEW",
      "source_currency":"NGN",
      "destination_currency":"NGN",
      "amount":{
         "value":50000,
         "applies_to":"destination_currency"
      },
      "disburse_option":{
         "date_time":"2025-10-25 13:52:30",
         "timezone":"UTC"
      },
      "recipient":{
         "type":"bank",
         "id":"rcb_1IkjUDnrt1",
         "name":{
            "first":"Ajadi",
            "last":"Jackson"
         },
         "currency":"NGN",
         "bank":{
            "account_number":"0122333334",
            "code":"044"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T10:51:02.222Z"
   }
}
```

The `data.status` field in the response will always return `NEW` upon initiating a transfer. This indicates that the transfer has been successfully initiated, but not yet completed.

To determine the final status, you must verify the payout. See the [verify transfer](#step-2-verify-the-transfer-status) section for more details.

You can verify a transfer’s status to determine whether it was successful, pending, or failed. When you initiate a transfer, the response includes:

-   `data.id`: Unique identifier for the transfer. Use this to track, manage, or update the transfer.
-   `data.status`: Current status of the transfer. When a transfer is first created, the status is always `NEW`. It can also change to:
    -   `PENDING`: Transfer is in progress.
    -   `SUCCESSFUL`: Transfer was completed successfully.
    -   `FAILED`: Transfer could not be processed.

You can get the status of a transfer using any of the following options:

-   Webhooks
-   Callback URL
-   Retrieve Transfer Endpoint

If you have webhooks enabled, Flutterwave automatically notifies your webhook URL when a transfer is completed or fails. This is the most efficient way to monitor transfer status in real time.

```json
{
  "webhook_id": "wbk_rp0bjKyAWA52ViM8xlZ0",
  "timestamp": 1739877172874,
  "type": "transfer.disburse",
  "data": {
    "id": "trf_yMZATJ11yVPNkZ",
    "type": "BANK",
    "source_currency": "NGN",
    "destination_currency": "NGN",
    "amount": 50000,
    "reference": "5748745ug8ufdgjhveyebjhcdbchb",
    "status": "SUCCESSFUL",
    "bank": {
      "account_number": "0122333334",
      "code": "044",
      "branch": null,
      "name": null,
      "routing_number": null,
      "swift_code": null
    },
    "fee": {
      "currency": "NGN",
      "value": 500
    },
    "debit_information": {
      "currency": "NGN",
      "actual_debit_amount": 50000,
      "rate_used": 0.00123,
      "vat": 3750
    },
    "payment_information": {
      "proof": "504828363550713897092362940989"
    },
    "meta": {}
  }
}
```

If you provide a `callback_url` when creating the transfer, Flutterwave will call this URL with details of completed or failed transfers.

```json
{
  "webhook_id": "wbk_rp0bjKyAWA52ViM8xlZ0",
  "timestamp": 1739877172874,
  "type": "transfer.disburse",
  "data": {
    "id": "trf_yMZATJ11yVPNkZ",
    "type": "BANK",
    "source_currency": "NGN",
    "destination_currency": "NGN",
    "amount": 50000,
    "reference": "5748745ug8ufdgjhveyebjhcdbchb",
    "status": "SUCCESSFUL",
    "bank": {
      "account_number": "0122333334",
      "code": "044",
      "branch": null,
      "name": null,
      "routing_number": null,
      "swift_code": null
    },
    "fee": {
      "currency": "NGN",
      "value": 500
    },
    "debit_information": {
      "currency": "NGN",
      "actual_debit_amount": 50000,
      "rate_used": 0.00123,
      "vat": 3750
    },
    "payment_information": {
      "proof": "504828363550713897092362940989"
    },
    "meta": {}
  }
}
```

You can manually check the current status of a transfer by calling the [retrieve transfer endpoint](https://developer.flutterwave.com/v4.0/reference/transfer_get) and providing the transfer ID. This should be done periodically to avoid rate limiting.

```json
curl --request GET \
--url 'https://developersandbox-api.flutterwave.com/transfers/{REPLACE_WITH_TRANSFER_ID}' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
```

You'll get a response similar to this:

```json
{
  "status": "success",
  "message": "Transfer fetched",
  "data": {
    "id": "trf_ighwLOK9pHxoo9",
    "type": "bank",
    "action": "instant",
    "reference": "5748745ug8ufdgjhveyyeebjhcdbchb",
    "status": "SUCCESSFUL",
    "source_currency": "NGN",
    "destination_currency": "NGN",
    "amount": {
      "value": 50000,
      "applies_to": "destination_currency"
    },
    "fee": {
      "currency": "NGN",
      "value": 500
    },
    "debit_information": {
      "currency": "NGN",
      "actual_debit_amount": 50000,
      "rate_used": 0.00123,
      "vat": 3750
    },
    "payment_information": {
      "proof": "754119292904667985302775753026"
    },
    "callback_url": "https://webhook.site/352c4518-7797-4044-becc-669fc5b1e928",
    "recipient": {
      "type": "bank",
      "id": "rcb_TDk7vKxUkj",
      "name": {
        "first": "Ajadi",
        "last": "Jackson"
      },
      "currency": "NGN",
      "bank": {
        "account_number": "0122333334",
        "code": "044"
      }
    },
    "meta": {},
    "created_datetime": "2025-02-18T11:20:37.282Z"
  }
}
```

A cross-currency transfer is a financial transaction where money is sent between countries involving different currencies. In this case, the sender's currency is converted into the recipient's local currency before delivery.

You can specify the transfer amount in either the **source currency** or the **destination currency**. This depends on your intent:

-   Use the **source currency** if you want to define exactly how much is deducted from your payout balance.
-   Use the **destination currency** if you want to ensure the recipient receives a specific amount.

For example:

-   If you want to pay your customer in **NGN** (`destination_currency`) from your **NGN** (`source_currency`) Flutterwave account, you can either specify the `source_currency` or `destination_currency` when making your request.
    
    #### Source Currency
    
    ```json
    "payment_instruction": {
        "source_currency": "NGN",
        "amount": {
          "applies_to": "source_currency",
          "value": 1000
    },
    ```
    
    ```json
    "payment_instruction": {
        "source_currency": "NGN",
        "amount": {
          "applies_to": "destination_currency",
          "value": 1000
    },
    ```
    
    #### Destination Currency
    
    ```json
    "payment_instruction": {
        "source_currency": "NGN",
        "amount": {
          "applies_to": "source_currency",
          "value": 1000
    },
    ```
    
    ```json
    "payment_instruction": {
        "source_currency": "NGN",
        "amount": {
          "applies_to": "destination_currency",
          "value": 1000
    },
    ```
    
-   If you want to pay your customer in **USD** (`destination_currency`) from your **NGN** (`source_currency`) Flutterwave account, Flutterwave will convert your available NGN to USD using the current exchange rate. A request will look like this:
    
    ```json
    "payment_instruction": {
        "source_currency": "NGN",
        "destination_currency": "USD",
          "amount": {
            "applies_to": "destination_currency",
            "value": 1000
    },
    ```
    

Transfer limits are based on the `destination_currency`. If you attempt to send an amount outside the allowed range, Flutterwave returns an error like this:

```shell
{
    "status": "failed",
    "error": {
        "type": "TRANSFER_AMOUNT_LIMIT",
        "code": "228400",
        "message": "Amount must be at least 100NGN.",
        "validation_errors": []
    }
}
```

For cross-currency transfers where the `source_currency` differs from the `destination_currency`, the source amount will be converted into the destination currency. If the converted amount exceeds or falls below the allowed limits for the destination currency, the transfer will fail.

> ## 📘
> 
> Integration Tip
> 
> Before initiating the transfer, use the [rate conversion endpoint](https://developer.flutterwave.com/v4.0/reference/transfer_rates_post) to ensure the converted amount falls within the permitted range.

Depending on whether you want to test the successful or failed transfers in your integration, follow these steps to simulate the payment experience in test mode:

1.  To test the successful transfers, send a request without adding any extra headers. This is the default testing flow for all transfers.
2.  For failed transfers, update the charge request header with the appropriate `X-Scenario-Key`. You can find the complete list of test scenario keys in the [test helpers section](../testing/index.md).

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: <YOUR_UNIQUE_TRACE_ID>' \
--header 'X-Idempotency-Key: <YOUR_UNIQUE_INDEMPOTENCY_KEY>' \
--header 'X-Scenario-Key: scenario:successful' \
--data '{
  "action": "instant",
  "payment_instruction": {
    "source_currency": "NGN",
    "amount": {
      "applies_to": "destination_currency",
      "value": 50000
    },
    "recipient": {
      "bank": {
        "account_number": "0122333334",
        "code": "044"
      }
    },
    "destination_currency": "NGN"
  },
  "type": "bank",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}"
}'
```

You'll get a response like this:

```json
{
  "status": "success",
  "message": "Transfer created",
  "data": {
    "id": "trf_pGoKPGH7rEgY4v",
    "type": "bank",
    "reference": "574874568ufdgjhvbjhcdbchb",
    "status": "NEW",
    "source_currency": "NGN",
    "destination_currency": "NGN",
    "amount": {
      "value": 50000,
      "applies_to": "destination_currency"
    },
    "recipient": {
      "type": "bank",
      "bank": {
        "account_number": "0122333334",
        "code": "044"
      }
    },
    "meta": {},
    "created_datetime": "2024-12-05T12:36:20.069512926Z"
  }
}
```

Updated 7 months ago

* * *
