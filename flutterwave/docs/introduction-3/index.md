---
title: "Introduction"
source: "https://developer.flutterwave.com/docs/introduction-3#"
canonical_url: "https://developer.flutterwave.com/docs/introduction-3"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:25.222Z"
content_hash: "e4a687c4999577be73f86f8ca5329d80ebb1ab4072977ca0618a4a4cfef488ac"
menu_path: ["Introduction"]
section_path: []
tab_variants: ["Example Request","200 Ok","Example Request","200 Ok","400 Bad Request"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/opay/index.md", "title": "OPay"}
nav_next: {"path": "flutterwave/docs/general-transfer-flow/index.md", "title": "General Transfer Flow"}
---

Flutterwave Transfers provides a suite of services that enable you to send money seamlessly to bank accounts, mobile numbers, wallets, and even through cash pickups. Depending on your business model, you can choose from the following options to facilitate transfers:

You can complete a transfer using either of the following flows:

-   **[Transfer Orchestrator](https://developer.flutterwave.com/v4.0/docs/direct-transfer-flow)** - This flow supports one-time transfers. Using this flow, it is quicker to initiate your transfer requests as all information is collected at once.
-   **[General Transfer Flow](https://developer.flutterwave.com/v4.0/docs/general-transfer-flow)** - This supports recurring transfers best, i.e. transfers made to the same recipient or transfers requiring the same sender information. It is a customizable flow that offers more control over the payout process and user experience.

  

> ## ❗️
> 
> To effectively use through these instructions, You'll need API credentials. Sign up for test credentials [here](https://onboarding.flutterwave.com/signup/steps/670fd6ca31db5a18fd7d03a7).

This guide demonstrates the orchestrator flow for one-time transfers. Read this [explainer](https://developer.flutterwave.com/v4.0/docs/general-transfer-flow) to initiate recurring transfers on your account.

Use the identity endpoint to generate your auth token. Read more about our API authentication [here](https://developer.flutterwave.com/v4.0/docs/authentication).

```curl
curl --location 'https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{YOUR_CLIENT_ID}}' \
--data-urlencode 'client_secret={{YOUR_CLIENT_SECRET}}' \
--data-urlencode 'grant_type=client_credentials'
```

[Validate](https://developer.flutterwave.com/reference/bank_account_resolve_post) your customer's bank account information. This step is important to ensure that your transfer is processed successfully to the correct recipient.

#### Example Request

```curl
curl --request POST \
     --url https://developersandbox-api.flutterwave.com/banks/account-resolve \
     --header 'content-type: application/json' \
     --data '
{
  "account": {
    "code": "044",
    "number": "0690000040"
  },
  "currency": "NGN"
}
'
```

```json
{
  "status": "success",
  "message": "string",
  "data": {
    "bank_code": "044",
    "account_number": "0690000040",
    "account_name": "Alex James"
  }
}
```

#### 200 Ok

```curl
curl --request POST \
     --url https://developersandbox-api.flutterwave.com/banks/account-resolve \
     --header 'content-type: application/json' \
     --data '
{
  "account": {
    "code": "044",
    "number": "0690000040"
  },
  "currency": "NGN"
}
'
```

```json
{
  "status": "success",
  "message": "string",
  "data": {
    "bank_code": "044",
    "account_number": "0690000040",
    "account_name": "Alex James"
  }
}
```

Send the transfer reference, payment instruction and transfer type to initiate the transfer. Read more about initiating transfers [here](https://developer.flutterwave.com/reference/direct_transfers_post).

#### Example Request

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
      "value": 1000
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

```json
{
    "status": "failed",
    "error": {
        "type": "REFERENCE_ALREADY_EXISTS",
        "code": "201409",
        "message": "Transfer with reference already exists",
        "validation_errors": []
    }
}
```

#### 200 Ok

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
      "value": 1000
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

```json
{
    "status": "failed",
    "error": {
        "type": "REFERENCE_ALREADY_EXISTS",
        "code": "201409",
        "message": "Transfer with reference already exists",
        "validation_errors": []
    }
}
```

#### 400 Bad Request

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
      "value": 1000
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

```json
{
    "status": "failed",
    "error": {
        "type": "REFERENCE_ALREADY_EXISTS",
        "code": "201409",
        "message": "Transfer with reference already exists",
        "validation_errors": []
    }
}
```

Before closing out the transfer, confirm its final status. See more details about status retrieval [here](https://developer.flutterwave.com/reference/transfer_get).

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

  

Updated 7 months ago

* * *
