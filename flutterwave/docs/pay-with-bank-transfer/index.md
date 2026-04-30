---
title: "Pay With Bank Transfer"
source: "https://developer.flutterwave.com/docs/pay-with-bank-transfer#"
canonical_url: "https://developer.flutterwave.com/docs/pay-with-bank-transfer"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:15.123Z"
content_hash: "519597103dd3e90cb999ab0342c109db439b415d4dbe37a79397c7cd14f182b8"
menu_path: ["Pay With Bank Transfer"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/mobile-money/index.md", "title": "Mobile Money"}
nav_next: {"path": "flutterwave/docs/ussd/index.md", "title": "USSD"}
---

Pay with bank transfer (`PWBT`) allows you to receive payments via bank transfers initiated by customers. Each payment is made into a virtual bank account linked to your settlement wallet.

You can generate either a **dynamic** or **static** virtual bank account to accept these payments:

-   **Dynamic accounts** are generated per transaction and expire after use. Ideal for one-time payments.
-   **Static accounts** are permanent and reusable, making them suitable for recurring payments.

PWBT is currently available for transactions in **NGN** (Nigerian Naira) and **GHS** (Ghanaian Cedi) only.

Before integrating PWBT, complete the following steps:

-   Retrieve your [API keys from the dashboard](https://app.flutterwave.com/).
-   Notify your customers that they will need to complete the payment by initiating a transfer from their bank account.

When a customer selects **PWBT** as their payment method, a unique bank account is generated for that transaction. To complete the payment, the customer must:

1.  Open their banking app or log in to internet banking.
2.  Transfer the exact amount to the provided virtual account details.
3.  Once the transfer is received, the payment is automatically verified and marked as successful. Both the customer and the merchant receive a confirmation.

The transaction is only successful once the customer initiates and completes the transfer to the provided virtual account.

Follow these steps to accept payments via bank transfer:

1.  **Generate the virtual account details**: Create a static or dynamic virtual bank account linked to the transaction.
    
2.  **Display the account details to the customer** – Prompt the customer to transfer the specified amount to the generated account.
    
3.  **Listen for webhooks** – Monitor the webhook events associated with the virtual account to detect successful transfers.
    
4.  **Verify the payment** – Before fulfilling the order or service, confirm:
    
    -   `status` is `successful`
    -   `amount` matches the expected amount
    -   `customer_id` is valid
    -   `id` (transaction reference) is consistent with the original request

You can receive payments through either a **static** or **dynamic** virtual account. Although both types look and feel the same to customers, they operate quite differently.

Static virtual accounts (also called permanent accounts) do not expire. Once created, they can be assigned to a single customer and reused for multiple transactions.

> ## 📘
> 
> Static Account Validity
> 
> Static accounts return an expiry date set to **1000 years** from their creation date.

> ## 🚧
> 
> You need to specify `amount` as `0` when creating a static virtual account.

To create a static virtual account, collect the following customer information:

1.  Customer name, preferably the first and last name.
2.  Customer email.
3.  The Customer's national identification number. For NGN virtual accounts, either of the following is required:
    1.  Bank Verification Number (BVN)
    2.  National Identification Number (NIN)

Use the Customer's personal Identification information (PII): the name and email to [create a customer](https://developer.flutterwave.com/reference/customers_create) object. Store the `customer_id` from the response for the next step.

```curl
curl --location 'https://developersandbox-api.flutterwave.com/customers' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--data-raw '{
  "name": {
    "first": "Cornelius",
    "last": "Ashley-Osuzoka"
  },
  "email": "cornelius@devxpay.com"
}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Customer created",
    "data": {
        "id": "cus_WWVaC0InrN",
        "email": "cornelius@devxpay.com",
        "name": {
            "first": "Cornelius",
            "last": "Ashley-Osuzoka"
        },
        "meta": {},
        "created_datetime": "2025-06-02T07:40:48.637002170Z"
    }
}
```

Use the `customer_id` along with other required details to create the virtual account using the [create virtual account endpoint](https://developer.flutterwave.com/reference/virtual_accounts_post).

> ## 🚧
> 
> You must set `amount` to `0` when creating a static virtual account. Since these accounts are reusable, they do not have a fixed amount.

```curl
curl --location 'https://developersandbox-api.flutterwave.com/virtual-accounts' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--header 'Content-Type: application/json' \
--data '{
    "reference": "1ca9e18f-f038-436f-b32b-3b7facdb1e13",
    "customer_id": "cus_WWVaC0InrN",
    "amount": 0,
    "currency": "NGN",
    "account_type": "static",
    "narration": "Cornelius Ashley-Osuzoka",
    "bvn": "12345678901"
}'
```

On a successful request, you'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Virtual account created",
    "data": {
        "id": "van_b6v7ZkuLug",
        "amount": 0,
        "account_number": "3788163576",
        "reference": "deac44b2-f8bd-4492-be07-bc25e5c4b159",
        "account_bank_name": "WEMA BANK",
        "account_type": "static",
        "status": "active",
        "account_expiration_datetime": "3024-10-03T07:46:47.519984192Z",
        "note": "Please make a bank transfer to Cornelius Ashley-Osuzoka",
        "customer_id": "cus_WWVaC0InrN",
        "created_datetime": "2025-06-02T07:46:47.529511629Z",
        "meta": {}
    }
}
```

A failed response looks like this:

```json
{
    "status": "failed",
    "error": {
        "type": "REQUEST_NOT_VALID",
        "code": "10400",
        "message": "Request is not valid",
        "validation_errors": [
            {
                "field_name": "bvn",
                "message": "bvn must be exactly 11 characters long and a signed integer"
            }
        ]
    }
}
```

Dynamic virtual accounts are temporary and expire after a set period. They're intended for one-time use or time-bound payments.

> ## ❗️
> 
> Dynamic Account Usage
> 
> Do **not** allow customers to save dynamic account details. These details are non-reusable and expire after the specified duration.

You must define an expiry when creating a dynamic account.

-   Maximum expiry: 365 days (or `31536000` seconds)
-   Default (if not specified): 1 hour (3600 seconds)

To create a dynamic account, you'll first need to set up the customer object.

```curl
curl --location 'https://developersandbox-api.flutterwave.com/customers' \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--data-raw '{
  "name": {
    "first": "Cornelius",
    "last": "Ashley-Osuzoka"
  },
  "email": "cornelius@devxpay.com"
}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Customer created",
    "data": {
        "id": "cus_WWVaC0InrN",
        "email": "cornelius@devxpay.com",
        "name": {
            "first": "Cornelius",
            "last": "Ashley-Osuzoka"
        },
        "meta": {},
        "created_datetime": "2025-06-02T07:40:48.637002170Z"
    }
}
```

Send the `customer_id` and other relevant information to the [create virtual account endpoint](https://developer.flutterwave.com/reference/virtual_accounts_post). Be sure to set `account_type` to `dynamic` and specify the `expiry` period.

```curl
curl --location 'https://developersandbox-api.flutterwave.com/virtual-accounts' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--header 'Content-Type: application/json' \
--data '{
    "reference": "a4d5f6b8-a785-4d41-8932-50fd8288aec8",
    "customer_id": "cus_WWVaC0InrN",
    "expiry": 60,
    "amount": 1500,
    "currency": "NGN",
    "account_type": "dynamic",
    "narration": "Cornelius Ashley-Osuzoka"
}'
```

On a successful request, you'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Virtual account created",
    "data": {
        "id": "van_fRiLt0WNsj",
        "amount": 1500,
        "account_number": "4032866864",
        "reference": "9d961ebf-6e51-4970-a334-af6a39325930",
        "account_bank_name": "WEMA BANK",
        "account_type": "dynamic",
        "status": "active",
        "account_expiration_datetime": "2025-06-02T08:03:21.369640550Z",
        "note": "Please make a bank transfer to Cornelius Ashley-Osuzoka",
        "customer_id": "cus_WWVaC0InrN",
        "created_datetime": "2025-06-02T08:02:21.383710209Z",
        "meta": {}
    }
}
```

A failed response looks like this:

```json
{
    "status": "failed",
    "error": {
        "type": "REQUEST_NOT_VALID",
        "code": "10400",
        "message": "Request is not valid",
        "validation_errors": [
            {
                "field_name": "bvn",
                "message": "bvn must be exactly 11 characters long and a signed integer"
            }
        ]
    }
}
```

> ## ❗️
> 
> Webhook Requirement
> 
> Before proceeding, ensure you’ve read our [webhook management guide](../webhooks/index.md) for proper webhook setup and handling.

When a customer completes a transfer to a virtual account, Flutterwave sends a `charge.completed` webhook to your configured webhook URL. This webhook contains details about the transaction and the associated customer.

```json
{
  "webhook_id": "wbk_xCBGoxP44NzL74hcCJiV",
  "timestamp": 1748850422635,
  "type": "charge.completed",
  "data": {
    "id": "chg_zH0BLoNltt",
    "amount": 175,
    "currency": "NGN",
    "customer": {
      "id": "cus_WWVaC0InrN",
      "address": null,
      "email": "cornelius@devxpay.com",
      "name": {
        "first": "Cornelius",
        "middle": null,
        "last": "Ashley-Osuzoka"
      },
      "phone": null,
      "meta": {},
      "created_datetime": "2025-06-02T07:40:48.637Z"
    },
    "description": null,
    "meta": {},
    "payment_method": {
      "type": "bank_transfer",
      "bank_transfer": {
        "account_expires_in": null,
        "account_display_name": null,
        "account_type": null
      },
      "id": "pmd_NzbQZvbnPj",
      "customer_id": null,
      "meta": {},
      "device_fingerprint": null,
      "client_ip": null,
      "created_datetime": "2025-06-02T07:46:47.520Z"
    },
    "redirect_url": null,
    "reference": "deac44b2-f8bd-4492-be07-bc25e5c4b159",
    "status": "succeeded",
    "processor_response": {
      "type": "approved",
      "code": "00"
    },
    "created_datetime": "2025-06-02T07:47:02.537812148Z"
  }
}
```

Use the `data.id` from the webhook to [verify the transaction](https://developer.flutterwave.com/reference/charges_get).

```curl
curl --location 'https://developersandbox-api.flutterwave.com/charges/chg_HJRm0DeDIN' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Charge fetched",
    "data": {
        "id": "chg_zH0BLoNltt",
        "amount": 175,
        "fees": [
            {
                "type": "vat",
                "amount": 0
            },
            {
                "type": "app",
                "amount": 0
            },
            {
                "type": "merchant",
                "amount": 0
            },
            {
                "type": "stamp_duty",
                "amount": 0
            }
        ],
        "currency": "NGN",
        "customer_id": "cus_WWVaC0InrN",
        "settled": true,
        "settlement_id": [
            "stm_XPx038OwdI"
        ],
        "meta": {},
        "payment_method_details": {
            "type": "bank_transfer",
            "bank_transfer": {},
            "id": "pmd_NzbQZvbnPj",
            "meta": {},
            "created_datetime": "2025-06-02T07:46:47.520Z"
        },
        "reference": "deac44b2-f8bd-4492-be07-bc25e5c4b159",
        "status": "succeeded",
        "processor_response": {
            "type": "approved",
            "code": "00"
        },
        "created_datetime": "2025-06-02T07:47:02.945Z"
    }
}
```

Before confirming payment or fulfilling an order:

-   `status` is succeeded.
-   `amount` matches the expected charge.
-   `currency` is correct.
-   `customer_id` matches the user.
-   `reference` is consistent with your internal tracking.

After verifying your transaction, you can track all the payments made into a virtual account by [querying the charge list](https://developer.flutterwave.com/reference/charges_list) using the virtual account's ID.

```curl
curl --location 'https://developersandbox-api.flutterwave.com/charges?virtual_account_id=van_b6v7ZkuLug' \
--header 'Accept: application/json' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Charges fetched",
    "meta": {
        "page_info": {
            "total": 1,
            "current_page": 1,
            "total_pages": 1
        }
    },
    "data": [
        {
            "id": "chg_zH0BLoNltt",
            "amount": 175,
            "fees": [
                {
                    "type": "vat",
                    "amount": 0
                },
                {
                    "type": "app",
                    "amount": 0
                },
                {
                    "type": "merchant",
                    "amount": 0
                },
                {
                    "type": "stamp_duty",
                    "amount": 0
                }
            ],
            "currency": "NGN",
            "customer_id": "cus_WWVaC0InrN",
            "settled": true,
            "settlement_id": [
                "stm_XPx038OwdI"
            ],
            "meta": {},
            "payment_method_details": {
                "type": "bank_transfer",
                "bank_transfer": {},
                "id": "pmd_NzbQZvbnPj",
                "meta": {},
                "created_datetime": "2025-06-02T07:46:47.520Z"
            },
            "reference": "deac44b2-f8bd-4492-be07-bc25e5c4b159",
            "status": "succeeded",
            "processor_response": {
                "type": "approved",
                "code": "00"
            },
            "created_datetime": "2025-06-02T07:47:02.945Z"
        }
    ]
}
```

Use the `X-Scenario-Key` header to simulate transaction outcomes during testing.

Simulate a successful transaction by specifying `issuer:approved`.

```curl
curl --location 'https://developersandbox-api.flutterwave.com/virtual-accounts' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'X-Scenario-Key: issuer:approved' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--header 'Content-Type: application/json' \
--data '{
    "reference": "cb0e10d5-f59e-424b-af44-65445ae4472b",
    "customer_id": "cus_WWVaC0InrN",
    "amount": 1500,
    "currency": "NGN",
    "account_type": "static",
    "narration": "Cornelius Ashley-Osuzoka",
    "bvn": "12345678901"
}'
```

A failed transfer using the `issuer:failed`.

```curl
curl --location 'https://developersandbox-api.flutterwave.com/virtual-accounts' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'X-Scenario-Key: issuer:failed' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--header 'Content-Type: application/json' \
--data '{
    "reference": "cb0e10d5-f59e-424b-af44-65445ae4472b",
    "customer_id": "cus_WWVaC0InrN",
    "amount": 1500,
    "currency": "NGN",
    "account_type": "static",
    "narration": "Cornelius Ashley-Osuzoka",
    "bvn": "12345678901"
}'
```

That’s it! You’ve now successfully integrated the bank transfer payment method. It doesn't end there, there is more:

-   Learn about [settlements](https://developer.flutterwave.com/v4.0/docs/settlements) of successful payments into your Flutterwave balance.
-   For cases where [refunds](https://developer.flutterwave.com/v4.0/docs/refunds) are necessary, see the refunds guide for more information on how to process transaction refunds.

Updated 3 months ago

* * *
