---
title: "Orchestrator Flow"
source: "https://developer.flutterwave.com/docs/payment-orchestrator-flow#"
canonical_url: "https://developer.flutterwave.com/docs/payment-orchestrator-flow"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:05.074Z"
content_hash: "eed60a75e9de63ca65c177ee9e46f2625d8c9893319ed54427d264397dcfcd98"
menu_path: ["Orchestrator Flow"]
section_path: []
tab_variants: ["Mobile Money","OPay","USSD","requires_pin","requires_otp","requires_additional_fields","redirect_url","payment_instruction"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/main-payment-flow/index.md", "title": "General Flow"}
nav_next: {"path": "flutterwave/docs/card/index.md", "title": "Card Payments"}
---

Unlike the [general payment flow](https://developer.flutterwave.com/v4.0/docs/main-payment-flow), which requires you to create `customer` and `payment_method` entities separately, the **payment orchestrator** lets you set up both in a single request. Here’s a visual overview of what happens when you call the orchestrator endpoint:

While we don't recommend this method for every integration, it is great for situations where you want to charge the customer quickly and would not be repeating the charge. This flow supports all our payment methods (see the full list of [supported payment methods](https://developer.flutterwave.com/v4.0/docs/introduction-1)).

Before you start, go through our [quickstart section](https://developer.flutterwave.com/v4.0/docs/quick-start). It covers essential setup steps for using our APIs.

You need the following setup to follow this guide:

1.  **Test account**
    1.  [API credentials](https://app.flutterwave.com/login) (client ID and client secret) for authenticating your requests.
    2.  A [webhook](https://developer.flutterwave.com/v4.0/docs/webhooks) URL to receive payment status updates.
2.  **Feature approvals**
    1.  Some payment methods require additional approval. See the [payment methods section](https://developer.flutterwave.com/v4.0/docs/introduction-1) for more details.

To initiate a charge, collect the customer’s PII, payment information, and transaction details such as:

-   `amount`
-   `currency`
-   `reference`
-   `redirect_url`

Then, send your request to the [orchestrator endpoint](https://developer.flutterwave.com/v4.0/reference/orchestration_direct_charge_post).

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--header 'X-Scenario-Key: scenario:auth_pin&issuer:approved' \
--data '{
    "amount": 1234.56,
    "currency": "USD",
    "reference": "YOUR_EXAMPLE_REFERENCE",
    "payment_method": {
        "type": "card",
        "card": {
            "nonce": "n0Ad6mOzVnLI",
            "encrypted_expiry_month": "sQpvQEb7GrUCjPuEN/NmHiPl",
            "encrypted_expiry_year": "sgHNEDkJ/RmwuWWq/RymToU5",
            "encrypted_card_number": "sAE3hEDaDQ+yLzo4Py+Lx15OZjBGduHu/DcdILh3En0=",
            "encrypted_cvv": "tAUzH7Qjma7diGdi7938F/ESNA=="
        }
    },
    "redirect_url": "https://custom-redirect.com",
    "customer": {
        "address": {
            "country": "US",
            "city": "Gotham",
            "state": "Colorado",
            "postal_code": "94105",
            "line1": "221B Baker Street"
        },
        "phone": {
            "country_code": "41",
            "number": "7069423351"
        },
        "name": {
            "first": "King",
            "middle": "Leo",
            "last": "James"
        },
        "email": "james@example.com"
    }
}'
```

Depending on the payment method you choose to charge your customer with, your request would vary slightly. Here are more examples to aid your integration.

#### Mobile Money

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'X-Trace-Id: {{UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{UNIQUE_IDEMPOTENCY_KEY}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API_ACCESS_TOKEN}}' \
--data-raw '{
    "amount": 1234.56,
    "currency": "GHS",
    "reference": "YOUR_EXAMPLE_REFERENCE",
    "customer": {
        "address": {
            "country": "US",
            "city": "Gotham",
            "state": "Colorado",
            "postal_code": "94105",
            "line1": "221B Baker Street"
        },
        "email": "james@example.com",
        "meta": {},
        "name": {
            "first": "King",
            "middle": "Leo",
            "last": "James"
        },
        "phone": {
            "country_code": "233",
            "number": "9012345678"
        }
    },
    "payment_method": {
        "type": "mobile_money",
        "mobile_money": {
            "country_code": "233",
            "network": "MTN",
            "phone_number": "9012345678"
        }
    }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "amount":1234.56,
   "currency":"NGN",
   "reference":"YOUR_EXAMPLE_REFERENCE",
   "payment_method":{
      "type":"opay"
   },
   "redirect_url":"http://www.google.com",
   "customer":{
      "address":{
         "country": "US",
         "city": "Gotham",
         "state": "Colorado",
         "postal_code": "94105",
         "line1": "221B Baker Street"
      },
      "phone":{
         "country_code":"1",
         "number":"7069423351"
      },
      "name":{
         "first": "King",
         "middle": "Leo",
         "last": "James"
      },
      "email":"james@example.com"
   }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
    "reference": "YOUR_EXAMPLE_REFERENCE",
    "currency": "NGN",
    "amount": 1234.56,
    "payment_method": {
        "type": "ussd",
        "ussd": {
            "account_bank":"044"
        }
    },
   "redirect_url":"http://www.custom-redirect.com",
   "customer":{
      "address":{
        "country": "US",
        "city": "Gotham",
        "state": "Colorado",
        "postal_code": "94105",
        "line1": "221B Baker Street"
      },
      "phone":{
         "country_code":"1",
         "number":9069423351
      },
      "name":{
         "first": "King",
         "middle": "Leo",
         "last": "James"
      },
      "email":"james@example.com"
   }
}'
```

#### OPay

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'X-Trace-Id: {{UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{UNIQUE_IDEMPOTENCY_KEY}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API_ACCESS_TOKEN}}' \
--data-raw '{
    "amount": 1234.56,
    "currency": "GHS",
    "reference": "YOUR_EXAMPLE_REFERENCE",
    "customer": {
        "address": {
            "country": "US",
            "city": "Gotham",
            "state": "Colorado",
            "postal_code": "94105",
            "line1": "221B Baker Street"
        },
        "email": "james@example.com",
        "meta": {},
        "name": {
            "first": "King",
            "middle": "Leo",
            "last": "James"
        },
        "phone": {
            "country_code": "233",
            "number": "9012345678"
        }
    },
    "payment_method": {
        "type": "mobile_money",
        "mobile_money": {
            "country_code": "233",
            "network": "MTN",
            "phone_number": "9012345678"
        }
    }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "amount":1234.56,
   "currency":"NGN",
   "reference":"YOUR_EXAMPLE_REFERENCE",
   "payment_method":{
      "type":"opay"
   },
   "redirect_url":"http://www.google.com",
   "customer":{
      "address":{
         "country": "US",
         "city": "Gotham",
         "state": "Colorado",
         "postal_code": "94105",
         "line1": "221B Baker Street"
      },
      "phone":{
         "country_code":"1",
         "number":"7069423351"
      },
      "name":{
         "first": "King",
         "middle": "Leo",
         "last": "James"
      },
      "email":"james@example.com"
   }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
    "reference": "YOUR_EXAMPLE_REFERENCE",
    "currency": "NGN",
    "amount": 1234.56,
    "payment_method": {
        "type": "ussd",
        "ussd": {
            "account_bank":"044"
        }
    },
   "redirect_url":"http://www.custom-redirect.com",
   "customer":{
      "address":{
        "country": "US",
        "city": "Gotham",
        "state": "Colorado",
        "postal_code": "94105",
        "line1": "221B Baker Street"
      },
      "phone":{
         "country_code":"1",
         "number":9069423351
      },
      "name":{
         "first": "King",
         "middle": "Leo",
         "last": "James"
      },
      "email":"james@example.com"
   }
}'
```

#### USSD

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'X-Trace-Id: {{UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{UNIQUE_IDEMPOTENCY_KEY}}' \
--header 'Content-Type: application/json' \
--header 'Authorization: Bearer {{API_ACCESS_TOKEN}}' \
--data-raw '{
    "amount": 1234.56,
    "currency": "GHS",
    "reference": "YOUR_EXAMPLE_REFERENCE",
    "customer": {
        "address": {
            "country": "US",
            "city": "Gotham",
            "state": "Colorado",
            "postal_code": "94105",
            "line1": "221B Baker Street"
        },
        "email": "james@example.com",
        "meta": {},
        "name": {
            "first": "King",
            "middle": "Leo",
            "last": "James"
        },
        "phone": {
            "country_code": "233",
            "number": "9012345678"
        }
    },
    "payment_method": {
        "type": "mobile_money",
        "mobile_money": {
            "country_code": "233",
            "network": "MTN",
            "phone_number": "9012345678"
        }
    }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "amount":1234.56,
   "currency":"NGN",
   "reference":"YOUR_EXAMPLE_REFERENCE",
   "payment_method":{
      "type":"opay"
   },
   "redirect_url":"http://www.google.com",
   "customer":{
      "address":{
         "country": "US",
         "city": "Gotham",
         "state": "Colorado",
         "postal_code": "94105",
         "line1": "221B Baker Street"
      },
      "phone":{
         "country_code":"1",
         "number":"7069423351"
      },
      "name":{
         "first": "King",
         "middle": "Leo",
         "last": "James"
      },
      "email":"james@example.com"
   }
}'
```

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
    "reference": "YOUR_EXAMPLE_REFERENCE",
    "currency": "NGN",
    "amount": 1234.56,
    "payment_method": {
        "type": "ussd",
        "ussd": {
            "account_bank":"044"
        }
    },
   "redirect_url":"http://www.custom-redirect.com",
   "customer":{
      "address":{
        "country": "US",
        "city": "Gotham",
        "state": "Colorado",
        "postal_code": "94105",
        "line1": "221B Baker Street"
      },
      "phone":{
         "country_code":"1",
         "number":9069423351
      },
      "name":{
         "first": "King",
         "middle": "Leo",
         "last": "James"
      },
      "email":"james@example.com"
   }
}'
```

You can send additional information with your request. Check the [API reference](https://developer.flutterwave.com/v4.0/reference/orchestration_direct_charge_post) for the full list of supported parameters.

> ## 🚧
> 
> Required Parameters
> 
> While the orchestrator simplifies integration, you still need to include the required fields for `customer` and `payment_method`. See the API reference for [customers API](https://developer.flutterwave.com/v4.0/reference/customers_create) and [payment methods API](https://developer.flutterwave.com/v4.0/reference/payment_methods_post) to see the full list.

After you initiate a charge, the API returns a `data.next_action` object that describes how to complete the payment.

Possible `next_action` values:

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
        "redirect_url": "www.flutterwave.com",
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
