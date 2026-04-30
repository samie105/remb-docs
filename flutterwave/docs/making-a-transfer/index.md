---
title: "Making a Transfer"
source: "https://developer.flutterwave.com/docs/making-a-transfer#"
canonical_url: "https://developer.flutterwave.com/docs/making-a-transfer"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:32:24.918Z"
content_hash: "c9056a5b615c67a583a66b12b46105a7deb68957b568beeca1de614e53412935"
menu_path: ["Making a Transfer"]
section_path: []
tab_variants: ["Example","200 Ok","Example","200 Ok","Example","201 Created"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/charging-a-card/index.md", "title": "Charging a Card"}
nav_next: {"path": "flutterwave/docs/integration-journey/index.md", "title": "Integration Journey"}
---

Follow these steps to initiate a transfer to an account.

1.  Log in to your [developer account](https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/auth?client_id=2e5450b8-ee6a-4e5d-b6db-cd9240b5bba3&redirect_uri=https%3A%2F%2Fdevelopersandbox.flutterwave.com%2Fexchange&response_type=code&scope=openid) to access your test credentials.
2.  Copy your API credentials from the main dashboard.

![](https://files.readme.io/47db2b3e9378a4d28aa2ffb04fa83ccb48e6aac4258745c0ec0dad41dcc1df27-test-mode-auth.png)

Send your `Client-Id` and `Client-Secret` to our authentication endpoint to generate your access token. Each token is valid for 10 minutes, after which you should generate a new token.

#### Example

```curl
curl -X POST 'https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{CLIENT_ID}}' \
--data-urlencode 'client_secret={{CLIENT_SECRET}}' \
--data-urlencode 'grant_type=client_credentials'
```

```json
{
    "access_token": "SAMPLE_TOKEN",
    "expires_in": 600,
    "refresh_expires_in": 0,
    "token_type": "Bearer",
    "not-before-policy": 0,
    "scope": "profile email"
}
```

#### 200 Ok

```curl
curl -X POST 'https://idp.flutterwave.com/realms/flutterwave/protocol/openid-connect/token' \
--header 'Content-Type: application/x-www-form-urlencoded' \
--data-urlencode 'client_id={{CLIENT_ID}}' \
--data-urlencode 'client_secret={{CLIENT_SECRET}}' \
--data-urlencode 'grant_type=client_credentials'
```

```json
{
    "access_token": "SAMPLE_TOKEN",
    "expires_in": 600,
    "refresh_expires_in": 0,
    "token_type": "Bearer",
    "not-before-policy": 0,
    "scope": "profile email"
}
```

[Create](https://developer.flutterwave.com/reference/transfers_recipients_create) an entity to store the recipient's banking information; this object links the recipient data to the transfer.

#### Example

```curl
curl --location 'https://developersandbox-api.flutterwave.com/transfers/recipients' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_IDEMPOTENCY_KEY}}' \
--data '{
  "type": "bank_ngn",
  "bank": {
    "account_number": "0690000031",
    "code": "044"
  }
}'
```

```json
{
  "status": "success",
  "message": "Recipient created",
  "data": {
    "type": "bank",
    "id": "rcb_B9aAgsdzzl",
    "name": {
      "first": "Tim",
      "last": "Jackson"
    },
    "currency": "NGN",
    "bank": {
      "account_number": "0690001031",
      "code": "044"
    }
  }
}
```

#### 200 Ok

```curl
curl --location 'https://developersandbox-api.flutterwave.com/transfers/recipients' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_IDEMPOTENCY_KEY}}' \
--data '{
  "type": "bank_ngn",
  "bank": {
    "account_number": "0690000031",
    "code": "044"
  }
}'
```

```json
{
  "status": "success",
  "message": "Recipient created",
  "data": {
    "type": "bank",
    "id": "rcb_B9aAgsdzzl",
    "name": {
      "first": "Tim",
      "last": "Jackson"
    },
    "currency": "NGN",
    "bank": {
      "account_number": "0690001031",
      "code": "044"
    }
  }
}
```

Save the recipient's id returned in the `response.data.id`.

Provide the `amount`, `recipient_id` and `currency` for the transfer. Specify `instant` as the `action` before sending your request to the create transfer [endpoint](https://developer.flutterwave.com/reference/transfers_post).

#### Example

```curl
curl --location 'https://developersandbox-api.flutterwave.com/transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--header 'X-Scenario-Key: scenario:successful' \
--data '{
    "action": "instant",
    "reference": "95e25053-8ee4-42770-a29-af4004dyf9462d",
    "narration": "Test transfer",
    "meta": {
        "username": "Madyson.Jones43"
    },
    "payment_instruction": {
        "source_currency": "NGN",
        "destination_currency": "NGN",
        "amount": {
            "applies_to": "destination_currency",
            "value": 1000
        },
        "recipient_id": "rcb_B9aAgsdzzl"
    }
}'
```

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "95e25053-8ee4-42770-a29-af4004dyf9462d",
        "status": "NEW",
        "narration": "Example Transfers",
        "source_currency": "NGN",
        "destination_currency": "NGN",
        "amount": {
            "value": 1000,
            "applies_to": "destination_currency"
        },
        "callback_url": "https://www.company.com/callback",
        "recipient": {
            "type": "bank",
            "currency": "NGN",
            "bank": {
                "account_number": "0690000031",
                "code": "044"
            },
            "id": "rcb_B9aAgsdzzl"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374991375Z"
    }
}
```

#### 201 Created

```curl
curl --location 'https://developersandbox-api.flutterwave.com/transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--header 'X-Scenario-Key: scenario:successful' \
--data '{
    "action": "instant",
    "reference": "95e25053-8ee4-42770-a29-af4004dyf9462d",
    "narration": "Test transfer",
    "meta": {
        "username": "Madyson.Jones43"
    },
    "payment_instruction": {
        "source_currency": "NGN",
        "destination_currency": "NGN",
        "amount": {
            "applies_to": "destination_currency",
            "value": 1000
        },
        "recipient_id": "rcb_B9aAgsdzzl"
    }
}'
```

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "95e25053-8ee4-42770-a29-af4004dyf9462d",
        "status": "NEW",
        "narration": "Example Transfers",
        "source_currency": "NGN",
        "destination_currency": "NGN",
        "amount": {
            "value": 1000,
            "applies_to": "destination_currency"
        },
        "callback_url": "https://www.company.com/callback",
        "recipient": {
            "type": "bank",
            "currency": "NGN",
            "bank": {
                "account_number": "0690000031",
                "code": "044"
            },
            "id": "rcb_B9aAgsdzzl"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374991375Z"
    }
}
```

Once the transfer is completed, we send you a `transfer.disburse` event via webhooks.

```json
{
  "webhook_id": "wbk_rp0bjKyAWA52ViM8xlZ0",
  "timestamp": 1739877172874,
  "type": "transfer.disburse",
  "data": {
    "id": "trf_iWUfJopFYdyBmB",
    "type": "BANK",
    "source_currency": "NGN",
    "destination_currency": "NGN",
    "amount": 1000,
    "reference": "95e25053-8ee4-42770-a29-af4004dyf9462d",
    "status": "SUCCESSFUL",
    "bank": {
      "account_number": "0690000031",
      "code": "044",
      "branch": null,
      "name": null,
      "routing_number": null,
      "swift_code": null
    },
    "fee": {
      "currency": "NGN",
      "value": 10
    },
    "debit_information": {
      "currency": "NGN",
      "actual_debit_amount": 1000,
      "rate_used": 0.00123,
      "vat": 375
    },
    "payment_information": {
      "proof": "504828363550713897092362940989"
    },
    "meta": {}
  }
}
```

Updated 5 months ago

* * *
