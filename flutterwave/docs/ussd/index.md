---
title: "USSD"
source: "https://developer.flutterwave.com/docs/ussd#"
canonical_url: "https://developer.flutterwave.com/docs/ussd"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:18.024Z"
content_hash: "75b9133ce58b2d39f3bf27ac3215b0b8f5870f47fc74ac4a7dd98dc3d6863673"
menu_path: ["USSD"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/pay-with-bank-transfer/index.md", "title": "Pay With Bank Transfer"}
nav_next: {"path": "flutterwave/docs/opay/index.md", "title": "OPay"}
---

Unstructured Supplementary Service Data (USSD) payments provide a reliable, internet-free option for customers to complete transactions using their mobile devices. This is particularly useful for offline users.

Most Nigerian banks support USSD payments and allow customers to authenticate transactions using their PINs.

> ## 🚧
> 
> Feature Availability
> 
> USSD payments are only available for NGN (Nigerian Naira) collections.

Before you begin, ensure the following prerequisites are met:

1.  Read the [introduction section](../introduction-1/index.md) of this documentation.
2.  Retrieve your API keys from the [Flutterwave dashboard](https://app.flutterwave.com/).

To initiate a USSD payment, a USSD code (string) is generated for the customer. The format and length of this code vary by bank.

The customer dials the code using the phone number linked to their bank account and enters their PIN to authorize the transaction. Once authorized, the bank debits the customer's account and Flutterwave sends a successful webhook to your server.

Follow these steps to collect USSD payments from customers:

1.  Collect the customer's details and initiate the transaction. Ensure you include required fields such as `amount`, `currency` and transaction `reference`.
2.  Send the `bank_code` to generate the USSD string.
3.  Listen for webhooks to know when the customer has completed the payment.
4.  Verify the `status`, `amount`, `customer_id` and `transaction_id` before providing the value to the customer.

  

> ## 🚧
> 
> Integration method
> 
> This guide follows the general integration flow. Please refer to the [orchestrator flow](https://developer.flutterwave.com/v4.0/docs/payment-orchestrator-flow) for the alternative integration method.

Send a request to the [create customer endpoint](https://developer.flutterwave.com/v4.0/reference/customers_create) with relevant fields such as `name`, `email`, `phone`, and `address`.

While only the `email` field is required, we recommend collecting as much customer information as possible to support robust transaction records and future payments.

To retrieve existing customer details, use the [retreive customer endpoint](https://developer.flutterwave.com/v4.0/reference/customers_get). This is useful when initiating payments for returning users.

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/customers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "address":{
      "city":"Shirley",
      "country":"US",
      "line1":"175 E Parkview Dr",
      "line2":"",
      "postal_code":"11967",
      "state":"New York"
   },
   "name":{
      "first":"John",
      "middle":"Agba",
      "last":"Doe"
   },
   "phone":{
      "country_code":"1",
      "number":"6313958745"
   },
   "email":"Johndoe@example.com"
}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Customer created",
    "data": {
        "id": "cus_IpH7CKCUtD",
        "address": {
            "city": "Shirley",
            "country": "US",
            "line1": "175 E Parkview Dr",
            "postal_code": "11967",
            "state": "New York"
        },
        "email": "Johndoe@example.com",
        "name": {
            "first": "John",
            "middle": "Agba",
            "last": "Doe"
        },
        "phone": {
            "country_code": "1",
            "number": "6313958745"
        },
        "meta": {},
        "created_datetime": "2025-01-24T13:51:48.758121209Z"
    }
}
```

Retrieve the list of supported banks and display it to the customer for selection.

Use the [get banks endpoint](https://developer.flutterwave.com/v4.0/reference/banks_get) with the query parameter `country=NG` to fetch Nigerian bank codes.

```json
curl --request GET \
--url 'https://developersandbox-api.flutterwave.com/banks?country=NG' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
```

You'll get a response similar to this:

```json
{
  "status": "success",
  "message": "string",
  "data": [
    {
      "id": "bnk_cYjd92Qk",
      "code": "044",
      "name": "Access Bank"
    }
    ...
  ]
}
```

Create a USSD payment method by sending a request to the [create payment method endpoint](https://developer.flutterwave.com/v4.0/reference/payment_methods_post). In your request:

-   Set the `type` to `"ussd"`.
-   Include a `ussd` object with `account_bank` set to the `bank_code` obtained in Step 2 (Get the Account Bank Code).

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/payment-methods' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "type": "ussd",
  "ussd": {
    "account_bank": "044"
  }
}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Payment method created",
    "data": {
        "type": "ussd",
        "ussd": {
            "account_bank": "050"
        },
        "id": "pmd_ZAIDy7RYiL",
        "meta": {},
        "created_datetime": "2025-01-24T15:19:21.639115327Z"
    }
}
```

Initiate the USSD charge by sending a request to the [create charge endpoint](https://developer.flutterwave.com/reference/charges_post) with the following parameters:

-   `customer_id`: The ID returned from Step 1 (customer creation).
-   `payment_method_id`: The ID returned from Step 2 (payment method creation).
-   Transaction details including: `amount`, `currency`, and a unique `reference` for the transaction.

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
    "reference": "185878aa-5647-47b6-b4d5-2f34bf596814",
    "currency": "NGN",
    "customer_id": "cus_IpH7CKCUtD",
    "payment_method_id": "pmd_ZAIDy7RYiL",
    "redirect_url": "https://custom-redirect.com",
    "amount": 250,
    "meta": {
        "order_id": "WOO_534643534_53453",
        "product_desc": "Hand Bag"
    }
}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Charge created",
    "data": {
        "id": "chg_fDxiSR16UF",
        "amount": 250,
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
        "customer_id": "cus_IpH7CKCUtD",
        "settled": false,
        "settlement_id": [],
        "meta": {
            "order_id": "WOO_534643534_53453",
            "product_desc": "Hand Bag"
        },
        "next_action": {
            "type": "payment_instruction",
            "payment_instruction": {
                "note": "Please dial *1414# to complete this transaction"
            }
        },
        "payment_method_details": {
            "type": "ussd",
            "ussd": {
                "account_bank": "044"
            },
            "id": "pmd_ZAIDy7RYiL",
            "customer_id": "cus_IpH7CKCUtD",
            "meta": {},
            "created_datetime": "2025-01-24T11:34:29.674Z"
        },
        "redirect_url": "https://custom-redirect.com",
        "reference": "185878aa-5647-47b6-b4d5-2f34bf596814",
        "status": "pending",
        "processor_response": {
            "type": "pending",
            "code": "02"
        },
        "created_datetime": "2025-01-24T11:56:53.935554048Z"
    }
}
```

The response from the charge initiation contains the `next_action` object with a payment instruction. The instructions guide the customer on how to authorise and complete their payment.

```json
"next_action": {
      "type": "payment_instruction",
      "payment_instruction": {
         "note": "Please dial *1414# to complete this transaction"
       }
 }
```

For USSD payments, the customer gets a prompt to enter the PIN after dialling the USSD string on their mobile.

Flutterwave will then send a **webhook notification** with the final transaction status once the payment is completed and funds are received.

Before you provide value to the customer, confirm the transaction's final status and amount. You can verify the transaction information either using webhooks or by retrieving the charge details:

-   **Webhooks**: It is important to have webhooks enabled on your Flutterwave dashboard. If you have webhooks enabled, we'll call your webhook URL with the payment details when the transaction is completed or fails. Below is a sample webhook payload:

```json
{
  "webhook_id": "wbk_RBHC8wDvzKn1OrFCoZVU",
  "timestamp": 1737719972231,
  "type": "charge.completed",
  "data": {
    "id": "chg_fDxiSR16UF",
    "amount": 250,
    "currency": "NGN",
    "customer": {
      "id": "cus_IpH7CKCUtD",
      "address": null,
      "email": "Johndoe@example.com",
      "name": John Agba Doe,
      "phone":+16313958745,
      "meta": {},
      "created_datetime": "2024-11-30T11:27:03.179Z"
    },
    "description": null,
    "meta": {
	"order_id": "WOO_534643534_53453",
       "product_desc": "Hand Bag"
    },
    "payment_method": {
      "type": "ussd",
      "ussd": {
        "account_bank": "044"
      },
      "id": "pmd_asxEDBpcgj",
      "customer_id": "cus_IpH7CKCUtD",
      "meta": {},
      "device_fingerprint": null,
      "client_ip": null,
      "created_datetime": "2025-01-24T11:59:27.080Z"
    },
    "redirect_url": null,
    "reference": "185878aa-5647-47b6-b4d5-2f34bf596814",
    "status": "succeeded",
    "processor_response": {
      "type": "approved",
      "code": "00"
    },
    "created_datetime": "2025-01-24T11:59:27.088511152Z"
  }
}
```

  

-   **Retrieve the Charge**: You can manually check the status of a charge by calling the [retrieve a charge endpoint](https://developer.flutterwave.com/v4.0/reference/charges_get) using the charge ID, which is returned in the `data.id` field of the response after successfully initiating a charge.

```json
curl --request GET \
--url 'https://developersandbox-api.flutterwave.com/charges/id' \
--header 'Authorization: Bearer <YOUR_ACCESS_TOKEN>' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: <YOUR_UNIQUE_TRACE_ID>' \
--header 'X-Idempotency-Key: <YOUR_UNIQUE_INDEMPOTENCY_KEY>' \
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Charge fetched",
    "data": {
        "id": "chg_fDxiSR16UF",
        "amount": 250,
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
        "customer_id": "cus_IpH7CKCUtD",
        "settled": false,
        "settlement_id": [],
        "meta": {
            "order_id": "WOO_534643534_53453",
            "product_desc": "Hand Bag"
        },
        "next_action": {
            "type": "payment_instruction",
            "payment_instruction": {
                "note": "Please dial *1414# to complete this transaction"
            }
        },
        "payment_method_details": {
            "type": "ussd",
            "ussd": {
                "account_bank": "044"
            },
            "id": "pmd_ZAIDy7RYiL",
            "customer_id": "cus_IpH7CKCUtD",
            "meta": {},
            "created_datetime": "2025-01-24T11:34:29.674Z"
        },
        "redirect_url": "https://custom-redirect.com",
        "reference": "185878aa-5647-47b6-b4d5-2f34bf596814",
        "status": "pending",
        "processor_response": {
            "type": "pending",
            "code": "02"
        },
        "created_datetime": "2025-01-24T11:56:53.935Z"
    }
}
```

Testing your integration requires no extra configuration or special data. Initiate the USSD charge, and we'll return a response on how to complete the charge.

That’s it! You’ve completed your integration with USSD. It doesn't end there, there is more:

-   Learn about [settlements](https://developer.flutterwave.com/v4.0/docs/settlements) of successful payments into your Flutterwave balance.
-   For cases where [refunds](https://developer.flutterwave.com/v4.0/docs/refunds) are necessary, see the refunds guide for more information on how to process transaction refunds.

Updated 3 months ago

* * *
