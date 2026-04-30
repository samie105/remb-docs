---
title: "General Transfer Flow"
source: "https://developer.flutterwave.com/docs/general-transfer-flow#"
canonical_url: "https://developer.flutterwave.com/docs/general-transfer-flow"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:28.755Z"
content_hash: "30d37440bd897d9cb7bbdf6ee868caeb8175b13ae0c6ce41067b2f02bec3d79f"
menu_path: ["General Transfer Flow"]
section_path: []
tab_variants: ["NGN","EGP","NGN 200 OK","EGP 200 OK"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/introduction-3/index.md", "title": "Introduction"}
nav_next: {"path": "flutterwave/docs/direct-transfer-flow/index.md", "title": "Transfer Orchestrator"}
---

The general transfer flow gives you more control over how payouts are handled. It lets you customize the experience to fit your product. In this flow, you’ll manage the recipient and sender information on your server.

This flow has four key steps:

1.  Create a transfer recipient entity.
2.  Create a transfer sender entity (optional).
3.  Initiate the transfer.
4.  Verify the transfer status.

Before you start, go through our [quickstart](https://developer.flutterwave.com/v4.0/docs/quick-start) section. It covers essential setup steps for using our APIs.  
You need the following setup to follow this guide:

-   [API credentials](https://app.flutterwave.com/login) (client ID and client secret) for authenticating your requests.
-   A [webhook](https://developer.flutterwave.com/v4.0/docs/webhooks) URL to receive payment status updates.
-   Whitelist your IP addresses
-   Ensure your balance has sufficient funds. You can fund your balance using one of the following methods:
    -   Directly funding via [collections](../introduction-1/index.md).
    -   Indirect funding by converting funds from a different currency balance (i.e., wallet-to-wallet transfers).

To create a transfer recipient, start by collecting the recipient’s destination account information. This typically includes either bank account or mobile money wallet details. Once gathered, send a request to the [create transfer recipient endpoint](https://developer.flutterwave.com/v4.0/reference/transfers_recipients_create).

The required fields depend on the `type` parameter (e.g., `bank_ngn`), which defines the transfer type for a specific currency. Based on the selected type, additional recipient fields may be required.

Refer to the [transfer recipient endpoint](https://developer.flutterwave.com/v4.0/reference/transfers_recipients_create) for a complete list of parameters supported for each type.

Below are sample requests for creating a transfer recipient using the following type values

#### NGN

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/transfers/recipients' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "type": "bank_ngn",
  "bank": {
    "account_number": "0690000031",
    "code": "044"
  }
}'
```

```curl
curl --request POST \
--url 'https://api.flutterwave.cloud/developersandbox/transfers/recipients' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "type":"bank_egp",
   "bank":{
      "code":"ADIB",
      "account_number":"123456789"
   },
   "name":{
      "first":"Steve",
      "last":"Mark",
      "middle":"Jade"
   },
   "national_identification":{
      "type":"PASSPORT",
      "identifier":"FLY998754",
      "expiration_date":"2029-06-01"
   },
   "phone":{
      "country_code":"20",
      "number":"9012345678"
   },
   "address":{
      "line1":"7A, Awesome Apartments",
      "line2":"Sweet Street",
      "postal_code":"123456",
      "state":"Super State",
      "city":"Cool City",
      "country":"EG"
   },
   "email":"jade@gmail.com"
}'
```

#### EGP

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/transfers/recipients' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "type": "bank_ngn",
  "bank": {
    "account_number": "0690000031",
    "code": "044"
  }
}'
```

```curl
curl --request POST \
--url 'https://api.flutterwave.cloud/developersandbox/transfers/recipients' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "type":"bank_egp",
   "bank":{
      "code":"ADIB",
      "account_number":"123456789"
   },
   "name":{
      "first":"Steve",
      "last":"Mark",
      "middle":"Jade"
   },
   "national_identification":{
      "type":"PASSPORT",
      "identifier":"FLY998754",
      "expiration_date":"2029-06-01"
   },
   "phone":{
      "country_code":"20",
      "number":"9012345678"
   },
   "address":{
      "line1":"7A, Awesome Apartments",
      "line2":"Sweet Street",
      "postal_code":"123456",
      "state":"Super State",
      "city":"Cool City",
      "country":"EG"
   },
   "email":"jade@gmail.com"
}'
```

You'll get a response similar to this:

#### NGN 200 OK

```json
{
  "status": "success",
  "message": "Recipient created",
  "data": {
    "type": "bank",
    "id": "rcb_B9aAgsdzzl",
    "name": {
      "first": "Ajadi",
      "last": "Jackson"
    },
    "currency": "NGN",
    "bank": {
      "account_number": "0690001032",
      "code": "044"
    }
  }
}
```

```json
{
   "status":"success",
   "message":"Recipient created",
   "data":{
      "type":"bank",
      "id":"rcb_gFoQprtdrL",
      "name":{
         "first":"Steve",
         "middle":"Jade",
         "last":"Mark"
      },
      "currency":"EGP",
      "national_identification":{
         "type":"PASSPORT",
         "identifier":"FLY998754",
         "expiration_date":"2029-06-01"
      },
      "phone":{
         "country_code":"20",
         "number":"9012345678"
      },
      "email":"jade@gmail.com",
      "address":{
         "city":"Cool City",
         "country":"EG",
         "line1":"7A, Awesome Apartments",
         "line2":"Sweet Street",
         "postal_code":"123456",
         "state":"Super State"
      },
      "bank":{
         "account_number":"123456789",
         "code":"ADIB"
      }
   }
}
```

#### EGP 200 OK

```json
{
  "status": "success",
  "message": "Recipient created",
  "data": {
    "type": "bank",
    "id": "rcb_B9aAgsdzzl",
    "name": {
      "first": "Ajadi",
      "last": "Jackson"
    },
    "currency": "NGN",
    "bank": {
      "account_number": "0690001032",
      "code": "044"
    }
  }
}
```

```json
{
   "status":"success",
   "message":"Recipient created",
   "data":{
      "type":"bank",
      "id":"rcb_gFoQprtdrL",
      "name":{
         "first":"Steve",
         "middle":"Jade",
         "last":"Mark"
      },
      "currency":"EGP",
      "national_identification":{
         "type":"PASSPORT",
         "identifier":"FLY998754",
         "expiration_date":"2029-06-01"
      },
      "phone":{
         "country_code":"20",
         "number":"9012345678"
      },
      "email":"jade@gmail.com",
      "address":{
         "city":"Cool City",
         "country":"EG",
         "line1":"7A, Awesome Apartments",
         "line2":"Sweet Street",
         "postal_code":"123456",
         "state":"Super State"
      },
      "bank":{
         "account_number":"123456789",
         "code":"ADIB"
      }
   }
}
```

  

> ## 📘
> 
> Getting Bank Code and Supported Mobile Money Network
> 
> -   Use the [retrieve banks endpoint](https://developer.flutterwave.com/v4.0/reference/banks_get) to get a list of banks and their codes. For some countries (e.g., Ghana), you may also need to call the [retrieve bank branches](https://developer.flutterwave.com/v4.0/reference/bank_branches_get) endpoint to get branch codes.
> -   Use the Retrieve [mobile networks endpoint](https://developer.flutterwave.com/v4.0/reference/mobile_networks_get) to fetch available mobile money networks by country and pass the appropriate `network` value.

  

> ## 🚧
> 
> Transfer Sender
> 
> The transfer sender entity is only required for transfers in `EGP`, `INR`, `EUR`, and `GBP`.

To create a transfer sender, collect the sender’s information and send a request to the [create transfer sender endpoint](https://developer.flutterwave.com/v4.0/reference/transfers_senders_create).

The required parameters depend on the `type` parameter (e.g., `bank_egp`), which specifies the transfer type for a particular currency. Depending on the selected type, you may need to provide details such as `name`, `email`, `phone`, `address`, `date_of_birth`, or `national_identification`.

Refer to the [transfer sender endpoint](https://developer.flutterwave.com/v4.0/reference/transfers_senders_create) for a full list of required fields based on the type.

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/transfers/senders' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "type": "bank_egp",
  "name": {
    "first": "Jake",
    "middle": "Leo",
    "last": "Smith"
  },
  "national_identification": {
    "type": "NATIONAL_ID",
    "identifier": "B01123075",
    "expiration_date": "2027-08-23"
  },
  "phone": {
    "country_code": "234",
    "number": "8067554433"
  },
  "address": {
    "country": "NG",
    "city": "Lagos",
    "state": "Lagos",
    "line1": "Crystal estate",
    "postal_code": "100223 ",
    "line2": "H2"
  },
  "date_of_birth": "1994-04-09",
  "email": "jsmith@gmail.com"
}'
```

You'll get a response similar to this:

```json
{
  "status": "success",
  "message": "Sender created",
  "data": {
    "id": "sdr_Cv7RMxkjNu",
    "name": {
      "first": "Jake",
      "middle": "Leo",
      "last": "Smith"
    },
    "national_identification": {
      "type": "NATIONAL_ID",
      "identifier": "B01123075",
      "expiration_date": "2027-08-23"
    },
    "phone": {
      "country_code": "234",
      "number": "8067554433"
    },
    "date_of_birth": "1994-04-09",
    "email": "jsmith@gmail.com",
    "address": {
      "city": "Lagos",
      "country": "NG",
      "line1": "Crystal estate",
      "line2": "H2",
      "postal_code": "100223 ",
      "state": "Lagos"
    }
  }
}
```

To initiate a transfer, send a request to the [Create Transfer endpoint](https://developer.flutterwave.com/v4.0/reference/transfers_post). Proceed to include the following important parameters in your payout request;

-   `action`: Specifies how the transfer should be processed. Accepted values are: `instant`, `deferred`, or `scheduled`.
-   `payment_instruction`: An object containing details of the payment, including:
    -   `amount`,
    -   `source_currency`,
    -   `recipient_id`,
    -   `sender_id` (optional)

Below are sample requests based on the possible transfer `action`:

To transfer the funds immediately, send a request to the [create transfer endpoint](https://developer.flutterwave.com/v4.0/reference/transfers_post).

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "reference":"95e25053-8ee4-42770-a29-af4004dyf9462d",
   "narration":"Test transfer",
   "meta":{
      "username":"Madyson.Jones43",
      "email":"bolamigbeakinlua@gmail.com"
   },
   "payment_instruction":{
      "source_currency":"EGP",
      "amount":{
         "applies_to":"source_currency",
         "value":100
      },
      "recipient_id":"rcb_gFoQprtdrL",
      "sender_id":"sdr_Cv7RMxkjNu"
   }
}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_mDiIM2FzB3ATisAQQAUyE",
        "type": "bank",
        "action": "instant",
        "reference": "95e25053-8ee4-42770-a29-af4004dyf9462d",
        "status": "NEW",
        "narration": "Test transfer",
        "source_currency": "EGP",
        "destination_currency": "EGP",
        "amount": {
            "value": 100,
            "applies_to": "source_currency"
        },
        "recipient": {
            "type": "bank",
            "id": "rcb_gFoQprtdrL",
            "name": {
                "first": "Steve",
                "middle": "Jade",
                "last": "Mark"
            },
            "currency": "EGP",
            "national_identification": {
                "type": "PASSPORT",
                "identifier": "FLY998754",
                "expiration_date": "2029-06-01"
            },
            "phone": {
                "country_code": "20",
                "number": "9012345678"
            },
            "email": "jade@gmail.com",
            "address": {
                "city": "Cool City",
                "country": "EG",
                "line1": "7A, Awesome Apartments",
                "line2": "Sweet Street",
                "postal_code": "123456",
                "state": "Super State"
            },
            "bank": {
                "account_number": "123456789",
                "code": "ADIB"
            }
        },
        "sender": {
            "id": "sdr_Cv7RMxkjNu",
            "name": {
                "first": "Jake",
                "middle": "Leo",
                "last": "Smith"
            },
            "national_identification": {
                "type": "NATIONAL_ID",
                "identifier": "B01123075",
                "expiration_date": "2027-08-23"
            },
            "phone": {
                "country_code": "234",
                "number": "8067554433"
            },
            "date_of_birth": "1994-04-09",
            "email": "jsmith@gmail.com",
            "address": {
                "city": "Lagos",
                "country": "NG",
                "line1": "Crystal estate",
                "line2": "H2",
                "postal_code": "100223 ",
                "state": "Lagos"
            }
        },
        "meta": {
            "username": "Madyson.Jones43",
            "email": "bolamigbeakinlua@gmail.com"
        },
        "created_datetime": "2025-06-25T08:46:52.790Z"
    }
}
```

To initiate a transfer that will be processed later, send a request similar to the instant transfer, but set the action parameter to `deferred`.

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"deferred",
   "reference":"95e25053-8ee4-42670-a29-af4004dyf9462d",
   "narration":"Test transfer",
   "meta":{
      "username":"Madyson.Jones43",
      "email":"bolamigbeakinlua@gmail.com"
   },
   "payment_instruction":{
      "source_currency":"EGP",
      "amount":{
         "applies_to":"source_currency",
         "value":100
      },
      "recipient_id":"rcb_gFoQprtdrL",
      "sender_id":"sdr_Cv7RMxkjNu"
   }
}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_6Di84IgPPEtg6MGMDCpWr",
        "type": "bank",
        "action": "deferred",
        "reference": "95e25053-8ee4-42670-a29-af4004dyf9462d",
        "status": "NEW",
        "narration": "Test transfer",
        "source_currency": "EGP",
        "destination_currency": "EGP",
        "amount": {
            "value": 100,
            "applies_to": "source_currency"
        },
        "recipient": {
            "type": "bank",
            "id": "rcb_gFoQprtdrL",
            "name": {
                "first": "Steve",
                "middle": "Jade",
                "last": "Mark"
            },
            "currency": "EGP",
            "national_identification": {
                "type": "PASSPORT",
                "identifier": "FLY998754",
                "expiration_date": "2029-06-01"
            },
            "phone": {
                "country_code": "20",
                "number": "9012345678"
            },
            "email": "jade@gmail.com",
            "address": {
                "city": "Cool City",
                "country": "EG",
                "line1": "7A, Awesome Apartments",
                "line2": "Sweet Street",
                "postal_code": "123456",
                "state": "Super State"
            },
            "bank": {
                "account_number": "123456789",
                "code": "ADIB"
            }
        },
        "sender": {
            "id": "sdr_Cv7RMxkjNu",
            "name": {
                "first": "Jake",
                "middle": "Leo",
                "last": "Smith"
            },
            "national_identification": {
                "type": "NATIONAL_ID",
                "identifier": "B01123075",
                "expiration_date": "2027-08-23"
            },
            "phone": {
                "country_code": "234",
                "number": "8067554433"
            },
            "date_of_birth": "1994-04-09",
            "email": "jsmith@gmail.com",
            "address": {
                "city": "Lagos",
                "country": "NG",
                "line1": "Crystal estate",
                "line2": "H2",
                "postal_code": "100223 ",
                "state": "Lagos"
            }
        },
        "meta": {
            "username": "Madyson.Jones43",
            "email": "bolamigbeakinlua@gmail.com"
        },
        "created_datetime": "2025-06-25T10:21:45.104Z"
    }
}
```

To **complete a deferred transfer**, call the [update transfer endpoint](https://developer.flutterwave.com/v4.0/reference/transfer_put), pass the transfer `id`, and update the action parameter by setting `action` to `instant` to process the transfer or set it to `close` to cancel it.

To schedule a transfer for a future date, set the action parameter to `scheduled` and include a `disburse_option` with the desired date time, and timezone.

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"scheduled",
   "disburse_option":{
      "date_time":"2025-10-25 13:52:30",
      "timezone":"UTC"
   },
   "reference":"95e25053-8ee4-42070-a29-af4004dyf9462d",
   "narration":"Test transfer",
   "meta":{
      "username":"Madyson.Jones43",
      "email":"bolamigbeakinlua@gmail.com"
   },
   "payment_instruction":{
      "source_currency":"EGP",
      "amount":{
         "applies_to":"source_currency",
         "value":100
      },
      "recipient_id":"rcb_gFoQprtdrL",
      "sender_id":"sdr_Cv7RMxkjNu"
   }
}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_vQSphUlHqnZywSnEoaOra",
        "type": "bank",
        "action": "scheduled",
        "reference": "95e25053-8ee4-42070-a29-af4004dyf9462d",
        "status": "NEW",
        "narration": "Test transfer",
        "source_currency": "EGP",
        "destination_currency": "EGP",
        "amount": {
            "value": 100,
            "applies_to": "source_currency"
        },
        "disburse_option": {
            "date_time": "2025-10-25 13:52:30",
            "timezone": "UTC"
        },
        "recipient": {
            "type": "bank",
            "id": "rcb_gFoQprtdrL",
            "name": {
                "first": "Steve",
                "middle": "Jade",
                "last": "Mark"
            },
            "currency": "EGP",
            "national_identification": {
                "type": "PASSPORT",
                "identifier": "FLY998754",
                "expiration_date": "2029-06-01"
            },
            "phone": {
                "country_code": "20",
                "number": "9012345678"
            },
            "email": "jade@gmail.com",
            "address": {
                "city": "Cool City",
                "country": "EG",
                "line1": "7A, Awesome Apartments",
                "line2": "Sweet Street",
                "postal_code": "123456",
                "state": "Super State"
            },
            "bank": {
                "account_number": "123456789",
                "code": "ADIB"
            }
        },
        "sender": {
            "id": "sdr_Cv7RMxkjNu",
            "name": {
                "first": "Jake",
                "middle": "Leo",
                "last": "Smith"
            },
            "national_identification": {
                "type": "NATIONAL_ID",
                "identifier": "B01123075",
                "expiration_date": "2027-08-23"
            },
            "phone": {
                "country_code": "234",
                "number": "8067554433"
            },
            "date_of_birth": "1994-04-09",
            "email": "jsmith@gmail.com",
            "address": {
                "city": "Lagos",
                "country": "NG",
                "line1": "Crystal estate",
                "line2": "H2",
                "postal_code": "100223 ",
                "state": "Lagos"
            }
        },
        "meta": {
            "username": "Madyson.Jones43",
            "email": "bolamigbeakinlua@gmail.com"
        },
        "created_datetime": "2025-06-25T10:25:16.811Z"
    }
}
```

The `data.status` field in the response will always return `NEW` upon initiating a transfer. This indicates that the transfer has been successfully initiated, but not yet completed.

To determine the final status, you must verify the payout. See the [verify transfer status](#step-4-verify-the-transfer-status) section for more details.

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
