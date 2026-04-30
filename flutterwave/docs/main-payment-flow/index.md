---
title: "General Flow"
source: "https://developer.flutterwave.com/docs/main-payment-flow#"
canonical_url: "https://developer.flutterwave.com/docs/main-payment-flow"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:00.666Z"
content_hash: "99bc88cb261dcbbfc79cc498514c71f6a6559ad4eb5ed415cc2df08127894087"
menu_path: ["General Flow"]
section_path: []
tab_variants: ["Card","Mobile Money","OPay","requires_pin","requires_otp","requires_additional_fields","redirect_url","payment_instruction"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/introduction-1/index.md", "title": "Introduction"}
nav_next: {"path": "flutterwave/docs/payment-orchestrator-flow/index.md", "title": "Orchestrator Flow"}
---

The general payment flow gives you more control over how payments are handled. It lets you to customize the experience to fit your product. In this flow, you’ll manage the customer, payment method, and charge information on your server.

This flow has five key steps:

1.  Create and manage the `customer` entity.
2.  Create a `payment_method` for the customer. Some methods, like USSD and bank transfers, can be reused across customers.
3.  Initiate the charge using `customer_id` and `payment_method_id`.
4.  Authorize the payment, based on the method’s requirements.
5.  Verify the payment status. This is especially important for asynchronous methods like mobile money, USSD, and bank transfers.

Before you start, go through our [quickstart section](https://developer.flutterwave.com/v4.0/docs/quick-start). It covers essential setup steps for using our APIs.

You need the following setup to follow this guide:

1.  **Test account**
    1.  [API credentials](https://app.flutterwave.com/login) (client ID and client secret) for authenticating your requests.
    2.  A [webhook](https://developer.flutterwave.com/v4.0/docs/webhooks) URL to receive payment status updates.
2.  **Feature approvals**
    1.  Some payment methods require additional approval. See the payment methods section for more details.

To create a customer, collect their information like `name`, `email`, `mobile_number`, and `address`. Only the `email` is required, but we recommend collecting as much information as possible. This helps you:

-   **Enhance user experience**: Autofill forms using saved customer details, making the checkout process smoother.
-   **Personalize interactions**: Use customer data for targeted promotions and retention strategies.
-   **Improve security and compliance**: Reduce fraud, chargebacks, and ensure regulatory compliance with comprehensive customer information.

A sample request looks like this:

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/customers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--data '{
  "address": {
    "city": "Gotham",
    "country": "US",
    "line1": "221B Baker Street",
    "line2": "",
    "postal_code": "94105",
    "state": "Colorado"
  },
  "name": {
    "first": "King",
    "middle": "Leo",
    "last": "James"
  },
  "phone": {
    "country_code": "1",
    "number": "6313958745"
  },
  "email": "james@example.com"
}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Customer created",
    "data": {
        "id": "cus_J0PvwvJB2n",
        "address": {
            "city": "Gotham",
            "country": "US",
            "line1": "221B Baker Street",
            "line2": "",
            "postal_code": "94105",
            "state": "Colorado"
        },
        "email": "james@example.com",
        "name": {
            "first": "King",
            "middle": "Leo",
            "last": "James"
        },
        "phone": {
            "country_code": "1",
            "number": "6313958745"
        },
        "meta": {},
        "created_datetime": "2024-12-03T13:54:21.546559974Z"
    }
}
```

Once you’ve created the customer, the next step is to collect their payment details. Flutterwave allows you to choose from different payment methods, such as cards, mobile money, wallets, and other APMs.

To create a payment method, send a request to the [create payment method](https://developer.flutterwave.com/v4.0/reference/payment_methods_post) endpoint with the required details.

#### Card

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/payment-methods' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
    "type": "card",
    "card": {
        "nonce": "w2zQDGCf1QXA",
        "encrypted_card_number": "Li/5y8DsxwD/FrDZgAS4AmFQDE8Pn1ed1BvjY3j0QoY=",
        "encrypted_expiry_month": "LyWZtiCL4oU7K65fWsOoA9B3",
        "encrypted_expiry_year": "LC8FYIrkmK6oMULiBskRx9L3",
        "encrypted_cvv": "Kiv9mwKcebmwbjWEN0Fd/ZBK2A=="
    }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/payment-methods' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "type": "mobile_money",
   "mobile_money": {
       "country_code": "233",
       "network": "MTN",
       "phone_number": "9012345678"
   }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/payment-methods' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "type":"opay"
}'
```

#### Mobile Money

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/payment-methods' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
    "type": "card",
    "card": {
        "nonce": "w2zQDGCf1QXA",
        "encrypted_card_number": "Li/5y8DsxwD/FrDZgAS4AmFQDE8Pn1ed1BvjY3j0QoY=",
        "encrypted_expiry_month": "LyWZtiCL4oU7K65fWsOoA9B3",
        "encrypted_expiry_year": "LC8FYIrkmK6oMULiBskRx9L3",
        "encrypted_cvv": "Kiv9mwKcebmwbjWEN0Fd/ZBK2A=="
    }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/payment-methods' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "type": "mobile_money",
   "mobile_money": {
       "country_code": "233",
       "network": "MTN",
       "phone_number": "9012345678"
   }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/payment-methods' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "type":"opay"
}'
```

#### OPay

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/payment-methods' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
    "type": "card",
    "card": {
        "nonce": "w2zQDGCf1QXA",
        "encrypted_card_number": "Li/5y8DsxwD/FrDZgAS4AmFQDE8Pn1ed1BvjY3j0QoY=",
        "encrypted_expiry_month": "LyWZtiCL4oU7K65fWsOoA9B3",
        "encrypted_expiry_year": "LC8FYIrkmK6oMULiBskRx9L3",
        "encrypted_cvv": "Kiv9mwKcebmwbjWEN0Fd/ZBK2A=="
    }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/payment-methods' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "type": "mobile_money",
   "mobile_money": {
       "country_code": "233",
       "network": "MTN",
       "phone_number": "9012345678"
   }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/payment-methods' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "type":"opay"
}'
```

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Payment method created",
    "data": {
        "type": "card",
        "card": {
            "expiry_month": 8,
            "expiry_year": 32,
            "first6": "123412",
            "last4": "2222",
            "network": "mastercard"
        },
        "id": "pmd_wlVhaYmkl2",
        "meta": {},
        "created_datetime": "2024-12-03T14:29:26.650973145Z"
    }
}
```

To [charge a customer](https://developer.flutterwave.com/v4.0/reference/charges_post), use their `customer_id` and `payment_method_id`. You’ll also need to specify the transaction amount, currency, and a unique reference.

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "reference": "cedfa85a-a803-4a06-a586-0f81fb9b9f22",
   "currency": "USD",
   "customer_id": "cus_IpH7CKCUtD",
   "payment_method_id": "pmd_wlVhaYmkl2",
   "redirect_url":"https://custom-redirect.com",
   "amount": 1234.56,
   "meta":{
     "person_name": "King James",
     "role": "Developer"
   }
 }
'
```

After initiating the charge, the API will return a `data.next_action` object in the response. This tells you what’s needed to complete the payment.

There are five kinds of `next_action` results:

1.  `requires_pin`
2.  `requires_otp`
3.  `redirect_url`
4.  `requires_additional_fields`
5.  `payment_Instructions`

`requires_pin`, `requires_otp`, and `requires_additional_fields` are customer inputs for authorizing card transactions with their banks. Actions like entering pins, soft tokens (OTPs), and billing addresses all fall under this category.

For these types of authorization, [update the transaction](https://developer.flutterwave.com/v4.0/reference/charges_put) with the authorization object to complete them.

#### requires\_pin

```json
{
    "authorization": {
        "type": "pin",
        "pin": {
            "nonce": "w2zQDGCf1QXA",
            "encrypted_pin": "LC8FYIrkmK6oMULiBskRx9L3"
        }
    }
}
```

```json
{
    "authorization": {
        "type": "otp",
        "otp": {
            "code": "123456"
        }
    }
}
```

```json
{
   "authorization":{
      "type":"avs",
      "avs":{
         "address":{
            "city":"Gotham",
            "country":"US",
            "line1":"221B Baker Street",
            "line2":"Coker Estate",
            "postal_code":"94105",
            "state":"Colorado"
         }
      }
   }
}
```

#### requires\_otp

```json
{
    "authorization": {
        "type": "pin",
        "pin": {
            "nonce": "w2zQDGCf1QXA",
            "encrypted_pin": "LC8FYIrkmK6oMULiBskRx9L3"
        }
    }
}
```

```json
{
    "authorization": {
        "type": "otp",
        "otp": {
            "code": "123456"
        }
    }
}
```

```json
{
   "authorization":{
      "type":"avs",
      "avs":{
         "address":{
            "city":"Gotham",
            "country":"US",
            "line1":"221B Baker Street",
            "line2":"Coker Estate",
            "postal_code":"94105",
            "state":"Colorado"
         }
      }
   }
}
```

#### requires\_additional\_fields

```json
{
    "authorization": {
        "type": "pin",
        "pin": {
            "nonce": "w2zQDGCf1QXA",
            "encrypted_pin": "LC8FYIrkmK6oMULiBskRx9L3"
        }
    }
}
```

```json
{
    "authorization": {
        "type": "otp",
        "otp": {
            "code": "123456"
        }
    }
}
```

```json
{
   "authorization":{
      "type":"avs",
      "avs":{
         "address":{
            "city":"Gotham",
            "country":"US",
            "line1":"221B Baker Street",
            "line2":"Coker Estate",
            "postal_code":"94105",
            "state":"Colorado"
         }
      }
   }
}
```

Redirects contain instructions for the merchant to redirect their customers to. These are typically used to complete 3DS card payments and mobile money transactions. In this scenario, the customer's transactions remain pending until redirection is completed.

In some cases, you would be required to perform some action offline. We communicate these actions as `payment_instructions`. This class of `next_action` is used mostly in USSD and pay with bank transfer payments.

#### redirect\_url

```json
{
    "status": "success",
    "message": "Charge created",
    "data": {
        "id": "chg_RCDsCBDyaV",
        ...
        "next_action": {
            "type": "redirect_url",
            "redirect_url": {
                "url": "https://developer-sandbox-ui-sit.flutterwave.cloud/redirects?card&token=eyJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJZCI6ImFjODMxOTNlLWFhMmItNDc2ZS1hZTNjLTMxYmVmMTc4NDUxZCIsImNoYXJnZUlkIjoiY2hnX1JDRHNDQkR5YVYiLCJzdWIiOiJhYzgzMTkzZS1hYTJiLTQ3NmUtYWUzYy0zMWJlZjE3ODQ1MWQiLCJpYXQiOjE3MzA5NjQ1MTIsImV4cCI6MTczMDk2NDgxMn0.tMv1VZ4WevvZ_dg37AzYnhj0Z1YtXK_tQIOJcErNscI"
            }
        },
        "payment_method_details": {},
        "status": "pending",
        ...
    }
}
```

```json
{
    "status": "success",
    "message": "Charge created",
    "data": {
        "id": "chg_RCDsCBDyaV",
        ...
        "next_action": {
            "type": "payment_instruction",
            "payment_instruction": {
                "note": "Please authorise this payment on your mobile number: 2339012345678. It may take a few minutes to confirm this payment."
            }
        },
        "payment_method_details": {},
        "status": "pending",
        ...
    }
}
```

#### payment\_instruction

```json
{
    "status": "success",
    "message": "Charge created",
    "data": {
        "id": "chg_RCDsCBDyaV",
        ...
        "next_action": {
            "type": "redirect_url",
            "redirect_url": {
                "url": "https://developer-sandbox-ui-sit.flutterwave.cloud/redirects?card&token=eyJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJZCI6ImFjODMxOTNlLWFhMmItNDc2ZS1hZTNjLTMxYmVmMTc4NDUxZCIsImNoYXJnZUlkIjoiY2hnX1JDRHNDQkR5YVYiLCJzdWIiOiJhYzgzMTkzZS1hYTJiLTQ3NmUtYWUzYy0zMWJlZjE3ODQ1MWQiLCJpYXQiOjE3MzA5NjQ1MTIsImV4cCI6MTczMDk2NDgxMn0.tMv1VZ4WevvZ_dg37AzYnhj0Z1YtXK_tQIOJcErNscI"
            }
        },
        "payment_method_details": {},
        "status": "pending",
        ...
    }
}
```

```json
{
    "status": "success",
    "message": "Charge created",
    "data": {
        "id": "chg_RCDsCBDyaV",
        ...
        "next_action": {
            "type": "payment_instruction",
            "payment_instruction": {
                "note": "Please authorise this payment on your mobile number: 2339012345678. It may take a few minutes to confirm this payment."
            }
        },
        "payment_method_details": {},
        "status": "pending",
        ...
    }
}
```

This final step is important to close out the payment. Query the transaction information and verify the transaction's `reference`, `amount` and `status` before giving value to the customer.

You can either:

-   Use your webhook to listen for payment status updates.
-   Call the [verify transaction](https://developer.flutterwave.com/v4.0/reference/charges_get) endpoint to confirm the status manually.

You'll get a response similar to this:

```json
{
    "status": "success",
    "message": "Charge updated",
    "data": {
        "id": "chg_VoUhmFMhmF",
        "amount": 1500.25,
        "currency": "NGN",
        "customer": "cus_EFE4TQhBSf",
        "meta": {},
        "next_action": {
            "type": "requires_pin"
        },
        "payment_method_details": {
            "type": "card",
            "card": {
                "expiry_month": 8,
                "expiry_year": 2024,
                "first6": "123412",
                "last4": "4444",
                "network": "mastercard"
            },
            "id": "pmd_NkWibrRJIy",
            "customer": "cus_EFE4TQhBSf",
            "meta": {}
        },
        "redirect_url": "https://custom-redirect.com",
        "reference": "XYZ123",
        "status": "succeeded",
        "issuer_response": {
            "type": "approved",
            "code": "00"
        }
    }
}
```

Updated 3 months ago

* * *
