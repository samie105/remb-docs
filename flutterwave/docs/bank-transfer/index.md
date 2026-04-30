---
title: "Bank Account Transfers"
source: "https://developer.flutterwave.com/docs/bank-transfer#"
canonical_url: "https://developer.flutterwave.com/docs/bank-transfer"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:42.331Z"
content_hash: "2e56be1681c1ec522b56896a952982eefd6ef70625e2ded1a162f5217c6c9a05"
menu_path: ["Bank Account Transfers"]
section_path: []
tab_variants: ["AUD Bank Payout","EGP Bank Payout","ETB Bank Payout","EUR Bank Payout","GHS Bank Payout","INR Bank Payout","MWK Bank Payout","NGN Bank Payout","AUD Bank Transfer","EGP Bank Transfer","ETB Bank Transfer","EUR Bank Transfer","GHS Bank Transfer","INR Bank Transfer","MWK Bank Transfer","NGN Bank Transfer","200 OK","400 Bad Request"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/direct-transfer-flow/index.md", "title": "Transfer Orchestrator"}
nav_next: {"path": "flutterwave/docs/mobile-money-1/index.md", "title": "Mobile Money Transfers"}
---

Flutterwave allows customers to transfer funds directly from their Flutterwave balance to a bank account. This feature enables merchants to seamlessly process payouts to local or international bank accounts.

Before initiating a transfer, complete the following:

-   Whitelist your IP addresses.
-   Ensure your balance has sufficient funds. You can fund your balance using one of the following methods:
    -   Directly funding via [collections](../introduction-1/index.md).
    -   Indirect funding by converting funds from a different currency balance (i.e., wallet-to-wallet transfers).

Each successful bank transfer follows a two-step process:

-   Initiate the payout
-   Verify the payout

  

> ## 🚧
> 
> Integration Method
> 
> This guide follows the direct transfer flow for demonstration. Please refer to the [general transfer flow](https://developer.flutterwave.com/v4.0/docs/general-transfer-flow) for the alternative integration method.

To initiate a bank transfer, send a request to the [create transfer endpoint](https://developer.flutterwave.com/reference/direct_transfers_post) with the following required parameters:

-   `action`: Specifies how the transfer should be processed. Accepted values are: `instant`, `deferred`, or `scheduled`.
-   `type`: Specifies the transfer method. Use `bank` for bank account transfers.
-   `payment_instruction`: An object containing transfer details of the payment, including:
    -   `amount`
    -   `currency` (`source_currency` and `destination_currency`)
    -   Recipient information, including destination bank account details.

  

#### AUD Bank Payout

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "AUD",
    "recipient": {
      "bank": {
        "routing_number": "062123",
        "swift_code": "BANK123",
        "name": "Commonwealth Bank of Australia",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "61",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "AU"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "recipient":{
         "bank":{
            "code":"ADIB",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         }
      },
      "sender":{
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "email":"alex@great.com",
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "address":{
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "date_of_birth":"1980-11-25",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ETB",
    "destination_currency": "ETB",
    "recipient": {
      "bank": {
        "code": "7",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "EUR",
    "recipient": {
      "bank": {
        "name": "Continental Bank of Europe",
        "swift_code": "DEUTDEFF",
        "account_number": "9876543210"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "49",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "DE"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "GHS",
    "destination_currency": "GHS",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "25562284",
        "branch": "001",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"INR",
      "destination_currency":"INR",
      "recipient":{
         "bank":{
            "code":"SBIN",
            "branch":"SBIN0015615",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"IN"
         }
      },
      "sender":{
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "MWK",
    "destination_currency": "MWK",
    "recipient": {
      "bank": {
        "code": "20474000",
        "branch": "1812061ZP6",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "NGN",
    "recipient": {
      "bank": {
        "code": "044",
        "account_number": "0690000031"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "USD",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "125200057",
        "routing_number": "021000021",
        "swift_code": "BOFAUS3N",
        "account_type": "checking",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "1",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "US"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ZAR",
    "destination_currency": "ZAR",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "ABSA",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "27",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "ZA"
      }
    }
  }
}'
```

#### EGP Bank Payout

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "AUD",
    "recipient": {
      "bank": {
        "routing_number": "062123",
        "swift_code": "BANK123",
        "name": "Commonwealth Bank of Australia",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "61",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "AU"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "recipient":{
         "bank":{
            "code":"ADIB",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         }
      },
      "sender":{
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "email":"alex@great.com",
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "address":{
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "date_of_birth":"1980-11-25",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ETB",
    "destination_currency": "ETB",
    "recipient": {
      "bank": {
        "code": "7",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "EUR",
    "recipient": {
      "bank": {
        "name": "Continental Bank of Europe",
        "swift_code": "DEUTDEFF",
        "account_number": "9876543210"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "49",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "DE"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "GHS",
    "destination_currency": "GHS",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "25562284",
        "branch": "001",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"INR",
      "destination_currency":"INR",
      "recipient":{
         "bank":{
            "code":"SBIN",
            "branch":"SBIN0015615",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"IN"
         }
      },
      "sender":{
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "MWK",
    "destination_currency": "MWK",
    "recipient": {
      "bank": {
        "code": "20474000",
        "branch": "1812061ZP6",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "NGN",
    "recipient": {
      "bank": {
        "code": "044",
        "account_number": "0690000031"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "USD",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "125200057",
        "routing_number": "021000021",
        "swift_code": "BOFAUS3N",
        "account_type": "checking",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "1",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "US"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ZAR",
    "destination_currency": "ZAR",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "ABSA",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "27",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "ZA"
      }
    }
  }
}'
```

#### ETB Bank Payout

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "AUD",
    "recipient": {
      "bank": {
        "routing_number": "062123",
        "swift_code": "BANK123",
        "name": "Commonwealth Bank of Australia",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "61",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "AU"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "recipient":{
         "bank":{
            "code":"ADIB",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         }
      },
      "sender":{
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "email":"alex@great.com",
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "address":{
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "date_of_birth":"1980-11-25",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ETB",
    "destination_currency": "ETB",
    "recipient": {
      "bank": {
        "code": "7",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "EUR",
    "recipient": {
      "bank": {
        "name": "Continental Bank of Europe",
        "swift_code": "DEUTDEFF",
        "account_number": "9876543210"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "49",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "DE"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "GHS",
    "destination_currency": "GHS",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "25562284",
        "branch": "001",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"INR",
      "destination_currency":"INR",
      "recipient":{
         "bank":{
            "code":"SBIN",
            "branch":"SBIN0015615",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"IN"
         }
      },
      "sender":{
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "MWK",
    "destination_currency": "MWK",
    "recipient": {
      "bank": {
        "code": "20474000",
        "branch": "1812061ZP6",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "NGN",
    "recipient": {
      "bank": {
        "code": "044",
        "account_number": "0690000031"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "USD",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "125200057",
        "routing_number": "021000021",
        "swift_code": "BOFAUS3N",
        "account_type": "checking",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "1",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "US"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ZAR",
    "destination_currency": "ZAR",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "ABSA",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "27",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "ZA"
      }
    }
  }
}'
```

#### EUR Bank Payout

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "AUD",
    "recipient": {
      "bank": {
        "routing_number": "062123",
        "swift_code": "BANK123",
        "name": "Commonwealth Bank of Australia",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "61",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "AU"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "recipient":{
         "bank":{
            "code":"ADIB",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         }
      },
      "sender":{
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "email":"alex@great.com",
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "address":{
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "date_of_birth":"1980-11-25",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ETB",
    "destination_currency": "ETB",
    "recipient": {
      "bank": {
        "code": "7",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "EUR",
    "recipient": {
      "bank": {
        "name": "Continental Bank of Europe",
        "swift_code": "DEUTDEFF",
        "account_number": "9876543210"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "49",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "DE"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "GHS",
    "destination_currency": "GHS",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "25562284",
        "branch": "001",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"INR",
      "destination_currency":"INR",
      "recipient":{
         "bank":{
            "code":"SBIN",
            "branch":"SBIN0015615",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"IN"
         }
      },
      "sender":{
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "MWK",
    "destination_currency": "MWK",
    "recipient": {
      "bank": {
        "code": "20474000",
        "branch": "1812061ZP6",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "NGN",
    "recipient": {
      "bank": {
        "code": "044",
        "account_number": "0690000031"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "USD",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "125200057",
        "routing_number": "021000021",
        "swift_code": "BOFAUS3N",
        "account_type": "checking",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "1",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "US"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ZAR",
    "destination_currency": "ZAR",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "ABSA",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "27",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "ZA"
      }
    }
  }
}'
```

#### GHS Bank Payout

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "AUD",
    "recipient": {
      "bank": {
        "routing_number": "062123",
        "swift_code": "BANK123",
        "name": "Commonwealth Bank of Australia",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "61",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "AU"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "recipient":{
         "bank":{
            "code":"ADIB",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         }
      },
      "sender":{
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "email":"alex@great.com",
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "address":{
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "date_of_birth":"1980-11-25",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ETB",
    "destination_currency": "ETB",
    "recipient": {
      "bank": {
        "code": "7",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "EUR",
    "recipient": {
      "bank": {
        "name": "Continental Bank of Europe",
        "swift_code": "DEUTDEFF",
        "account_number": "9876543210"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "49",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "DE"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "GHS",
    "destination_currency": "GHS",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "25562284",
        "branch": "001",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"INR",
      "destination_currency":"INR",
      "recipient":{
         "bank":{
            "code":"SBIN",
            "branch":"SBIN0015615",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"IN"
         }
      },
      "sender":{
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "MWK",
    "destination_currency": "MWK",
    "recipient": {
      "bank": {
        "code": "20474000",
        "branch": "1812061ZP6",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "NGN",
    "recipient": {
      "bank": {
        "code": "044",
        "account_number": "0690000031"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "USD",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "125200057",
        "routing_number": "021000021",
        "swift_code": "BOFAUS3N",
        "account_type": "checking",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "1",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "US"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ZAR",
    "destination_currency": "ZAR",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "ABSA",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "27",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "ZA"
      }
    }
  }
}'
```

#### INR Bank Payout

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "AUD",
    "recipient": {
      "bank": {
        "routing_number": "062123",
        "swift_code": "BANK123",
        "name": "Commonwealth Bank of Australia",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "61",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "AU"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "recipient":{
         "bank":{
            "code":"ADIB",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         }
      },
      "sender":{
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "email":"alex@great.com",
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "address":{
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "date_of_birth":"1980-11-25",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ETB",
    "destination_currency": "ETB",
    "recipient": {
      "bank": {
        "code": "7",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "EUR",
    "recipient": {
      "bank": {
        "name": "Continental Bank of Europe",
        "swift_code": "DEUTDEFF",
        "account_number": "9876543210"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "49",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "DE"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "GHS",
    "destination_currency": "GHS",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "25562284",
        "branch": "001",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"INR",
      "destination_currency":"INR",
      "recipient":{
         "bank":{
            "code":"SBIN",
            "branch":"SBIN0015615",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"IN"
         }
      },
      "sender":{
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "MWK",
    "destination_currency": "MWK",
    "recipient": {
      "bank": {
        "code": "20474000",
        "branch": "1812061ZP6",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "NGN",
    "recipient": {
      "bank": {
        "code": "044",
        "account_number": "0690000031"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "USD",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "125200057",
        "routing_number": "021000021",
        "swift_code": "BOFAUS3N",
        "account_type": "checking",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "1",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "US"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ZAR",
    "destination_currency": "ZAR",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "ABSA",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "27",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "ZA"
      }
    }
  }
}'
```

#### MWK Bank Payout

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "AUD",
    "recipient": {
      "bank": {
        "routing_number": "062123",
        "swift_code": "BANK123",
        "name": "Commonwealth Bank of Australia",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "61",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "AU"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "recipient":{
         "bank":{
            "code":"ADIB",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         }
      },
      "sender":{
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "email":"alex@great.com",
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "address":{
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "date_of_birth":"1980-11-25",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ETB",
    "destination_currency": "ETB",
    "recipient": {
      "bank": {
        "code": "7",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "EUR",
    "recipient": {
      "bank": {
        "name": "Continental Bank of Europe",
        "swift_code": "DEUTDEFF",
        "account_number": "9876543210"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "49",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "DE"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "GHS",
    "destination_currency": "GHS",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "25562284",
        "branch": "001",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"INR",
      "destination_currency":"INR",
      "recipient":{
         "bank":{
            "code":"SBIN",
            "branch":"SBIN0015615",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"IN"
         }
      },
      "sender":{
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "MWK",
    "destination_currency": "MWK",
    "recipient": {
      "bank": {
        "code": "20474000",
        "branch": "1812061ZP6",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "NGN",
    "recipient": {
      "bank": {
        "code": "044",
        "account_number": "0690000031"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "USD",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "125200057",
        "routing_number": "021000021",
        "swift_code": "BOFAUS3N",
        "account_type": "checking",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "1",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "US"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ZAR",
    "destination_currency": "ZAR",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "ABSA",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "27",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "ZA"
      }
    }
  }
}'
```

#### NGN Bank Payout

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "AUD",
    "recipient": {
      "bank": {
        "routing_number": "062123",
        "swift_code": "BANK123",
        "name": "Commonwealth Bank of Australia",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "61",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "AU"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "recipient":{
         "bank":{
            "code":"ADIB",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         }
      },
      "sender":{
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "email":"alex@great.com",
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "address":{
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"EG"
         },
         "date_of_birth":"1980-11-25",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ETB",
    "destination_currency": "ETB",
    "recipient": {
      "bank": {
        "code": "7",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "EUR",
    "recipient": {
      "bank": {
        "name": "Continental Bank of Europe",
        "swift_code": "DEUTDEFF",
        "account_number": "9876543210"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "49",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "DE"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "GHS",
    "destination_currency": "GHS",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "25562284",
        "branch": "001",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "type":"bank",
   "callback_url":"https://www.company.com/callback",
   "narration":"Testing transfers",
   "reference":"{{YOUR_UNIQUE_REFERENCE}}",
   "payment_instruction":{
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "source_currency":"INR",
      "destination_currency":"INR",
      "recipient":{
         "bank":{
            "code":"SBIN",
            "branch":"SBIN0015615",
            "account_number":"123456789"
         },
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "email":"user@example.com",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "address":{
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "city":"Cool City",
            "state":"Super State",
            "country":"IN"
         }
      },
      "sender":{
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      }
   }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "MWK",
    "destination_currency": "MWK",
    "recipient": {
      "bank": {
        "code": "20474000",
        "branch": "1812061ZP6",
        "account_number": "123456789"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "NGN",
    "recipient": {
      "bank": {
        "code": "044",
        "account_number": "0690000031"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "USD",
    "destination_currency": "USD",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "125200057",
        "routing_number": "021000021",
        "swift_code": "BOFAUS3N",
        "account_type": "checking",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "1",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "US"
      }
    }
  }
}'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
  "action": "instant",
  "type": "bank",
  "callback_url": "https://www.company.com/callback",
  "narration": "Testing transfers",
  "reference": "{{YOUR_UNIQUE_REFERENCE}}",
  "payment_instruction": {
    "amount": {
      "value": 1000,
      "applies_to": "destination_currency"
    },
    "source_currency": "ZAR",
    "destination_currency": "ZAR",
    "recipient": {
      "type": "bank",
      "bank": {
        "code": "ABSA",
        "account_number": "1234567890"
      },
      "name": {
        "first": "Bob",
        "middle": "The",
        "last": "Builder"
      },
      "email": "user@example.com",
      "phone": {
        "country_code": "27",
        "number": "9012345678"
      },
      "address": {
        "line1": "7A, Awesome Apartments",
        "line2": "Sweet Street",
        "postal_code": "123456",
        "city": "Cool City",
        "state": "Super State",
        "country": "ZA"
      }
    }
  }
}'
```

> ## 🚧
> 
> Getting Bank and Branch Codes
> 
> To complete a bank transfer, you may need to provide both the bank code and bank branch code (if required for the destination country). Retrieve this information using the available Bank APIs:
> 
> -   [Retrieve banks endpoint](https://developer.flutterwave.com/reference/banks_get): Fetches a list of bank codes available for a specific country.
> -   [Retrieve bank branches endpoint](https://developer.flutterwave.com/reference/bank_branches_get): Fetches a list of bank branches for a specific bank. Required only for certain currency transfers (e.g., GHS bank transfers).

You can initiate **scheduled** or **deferred** bank transfers by setting the `action` field to `scheduled` or `deferred`.

For **scheduled** transfers, include the `disburse_option` object in your request. This object defines when the transfer should be executed and must contain:

-   `date_time`: The exact date and time to trigger the transfer.
-   `timezone`: The timezone for the scheduled time.

Refer to the [transfer overview](../introduction-3/index.md#full-example) for a complete walkthrough on creating and managing these transfer types.

> ## 💱
> 
> Handling International Transfers
> 
> To manage cross-currency payouts, refer to the [managing currency](../direct-transfer-flow/index.md#cross-currency-transfers) section.

When you successfully initiate a bank transfer, the API returns a response similar to the following:

#### AUD Bank Transfer

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_HHB2Yrc3LUyooR",
      "type":"bank",
      "action":"instant",
      "reference":"duyiebieuei8eieu89383jhdjhdy",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"AUD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_v3jeBmSUxC",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"AUD",
         "phone":{
            "country_code":"61",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"AU",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "name":"Commonwealth Bank of Australia",
            "routing_number":"CTBAAU",
            "swift_code":"BANK123"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:04:36.072Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_mm2c4ax7p3YDNB",
      "type":"bank",
      "action":"instant",
      "reference":"kjvdcoihudfoidfpofjiof9r",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_pvu4uNFiT7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EGP",
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         },
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "email":"user@example.com",
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
      },
      "sender":{
         "id":"sdr_tGCFUvSdVu",
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         },
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "date_of_birth":"1980-11-25",
         "email":"alex@great.com",
         "address":{
            "city":"Cool City",
            "country":"EG",
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:29:48.366Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_zksyU4F4kFGZi7",
      "type":"bank",
      "action":"instant",
      "reference":"778989JHUTGHJGHJYUYIUY",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ETB",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ExC7XZKoC1",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ETB",
         "bank":{
            "account_number":"123456789",
            "code":"7"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:37:41.658Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_03mgMQvkcD1J4Q",
      "type":"bank",
      "action":"instant",
      "reference":"duuidiudodudududj77262",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"EUR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_2fh9yl2PCl",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EUR",
         "phone":{
            "country_code":"49",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"DE",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"9876543210",
            "name":"Continental Bank of Europe",
            "swift_code":"DEUTDEFF"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:42:32.080Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_psJZCQCkOcQl06",
      "type":"bank",
      "action":"instant",
      "reference":"jguyfghgyt7675hjg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"GHS",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ykW6hU75cU",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"GHS",
         "bank":{
            "account_number":"1234567890",
            "code":"25562284",
            "branch":"001"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:46:29.584Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_Gr4gqFAiDheMvc",
      "type":"bank",
      "action":"instant",
      "reference":"FYFTHGHGHJGhgyt57",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"INR",
      "destination_currency":"INR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_hKd3HybtHa",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"INR",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"IN",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "code":"SBIN",
            "branch":"SBIN0015615"
         }
      },
      "sender":{
         "id":"sdr_M37FKMARWj",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2025-06-02T16:53:09.632Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_t8w0OGSNOdV4P5",
      "type":"bank",
      "action":"instant",
      "reference":"GGUGTUYUHIIUIOU7",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"MWK",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_t68rd2GfZ7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"MWK",
         "bank":{
            "account_number":"123456789",
            "code":"20474000",
            "branch":"1812061ZP6"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:59:32.628Z"
   }
}
```

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "c3104347-5ebf-41bd-957c-7666df028bbe",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "USD",
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
            "id": "rcb_gsLlPvnOLy"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374991375Z"
    }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_NvhGENkNcnBI2t",
      "type":"bank",
      "action":"instant",
      "reference":"ugujbuujyujgjb7889",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"USD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_Yro1zlIF7I",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"USD",
         "phone":{
            "country_code":"1",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"US",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "account_type":"checking",
            "code":"125200057",
            "routing_number":"021000021",
            "swift_code":"BOFAUS3N"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:07:00.549Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_bf65ZmcvRt5tq3",
      "type":"bank",
      "action":"instant",
      "reference":"jhgvjhgjjyyiy79hg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ZAR",
      "destination_currency":"ZAR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_mQnFh6aMOB",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ZAR",
         "phone":{
            "country_code":"27",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"ZA",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "code":"ABSA"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:10:26.917Z"
   }
}
```

#### EGP Bank Transfer

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_HHB2Yrc3LUyooR",
      "type":"bank",
      "action":"instant",
      "reference":"duyiebieuei8eieu89383jhdjhdy",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"AUD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_v3jeBmSUxC",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"AUD",
         "phone":{
            "country_code":"61",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"AU",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "name":"Commonwealth Bank of Australia",
            "routing_number":"CTBAAU",
            "swift_code":"BANK123"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:04:36.072Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_mm2c4ax7p3YDNB",
      "type":"bank",
      "action":"instant",
      "reference":"kjvdcoihudfoidfpofjiof9r",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_pvu4uNFiT7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EGP",
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         },
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "email":"user@example.com",
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
      },
      "sender":{
         "id":"sdr_tGCFUvSdVu",
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         },
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "date_of_birth":"1980-11-25",
         "email":"alex@great.com",
         "address":{
            "city":"Cool City",
            "country":"EG",
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:29:48.366Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_zksyU4F4kFGZi7",
      "type":"bank",
      "action":"instant",
      "reference":"778989JHUTGHJGHJYUYIUY",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ETB",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ExC7XZKoC1",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ETB",
         "bank":{
            "account_number":"123456789",
            "code":"7"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:37:41.658Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_03mgMQvkcD1J4Q",
      "type":"bank",
      "action":"instant",
      "reference":"duuidiudodudududj77262",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"EUR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_2fh9yl2PCl",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EUR",
         "phone":{
            "country_code":"49",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"DE",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"9876543210",
            "name":"Continental Bank of Europe",
            "swift_code":"DEUTDEFF"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:42:32.080Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_psJZCQCkOcQl06",
      "type":"bank",
      "action":"instant",
      "reference":"jguyfghgyt7675hjg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"GHS",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ykW6hU75cU",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"GHS",
         "bank":{
            "account_number":"1234567890",
            "code":"25562284",
            "branch":"001"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:46:29.584Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_Gr4gqFAiDheMvc",
      "type":"bank",
      "action":"instant",
      "reference":"FYFTHGHGHJGhgyt57",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"INR",
      "destination_currency":"INR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_hKd3HybtHa",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"INR",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"IN",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "code":"SBIN",
            "branch":"SBIN0015615"
         }
      },
      "sender":{
         "id":"sdr_M37FKMARWj",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2025-06-02T16:53:09.632Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_t8w0OGSNOdV4P5",
      "type":"bank",
      "action":"instant",
      "reference":"GGUGTUYUHIIUIOU7",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"MWK",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_t68rd2GfZ7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"MWK",
         "bank":{
            "account_number":"123456789",
            "code":"20474000",
            "branch":"1812061ZP6"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:59:32.628Z"
   }
}
```

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "c3104347-5ebf-41bd-957c-7666df028bbe",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "USD",
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
            "id": "rcb_gsLlPvnOLy"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374991375Z"
    }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_NvhGENkNcnBI2t",
      "type":"bank",
      "action":"instant",
      "reference":"ugujbuujyujgjb7889",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"USD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_Yro1zlIF7I",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"USD",
         "phone":{
            "country_code":"1",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"US",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "account_type":"checking",
            "code":"125200057",
            "routing_number":"021000021",
            "swift_code":"BOFAUS3N"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:07:00.549Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_bf65ZmcvRt5tq3",
      "type":"bank",
      "action":"instant",
      "reference":"jhgvjhgjjyyiy79hg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ZAR",
      "destination_currency":"ZAR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_mQnFh6aMOB",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ZAR",
         "phone":{
            "country_code":"27",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"ZA",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "code":"ABSA"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:10:26.917Z"
   }
}
```

#### ETB Bank Transfer

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_HHB2Yrc3LUyooR",
      "type":"bank",
      "action":"instant",
      "reference":"duyiebieuei8eieu89383jhdjhdy",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"AUD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_v3jeBmSUxC",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"AUD",
         "phone":{
            "country_code":"61",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"AU",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "name":"Commonwealth Bank of Australia",
            "routing_number":"CTBAAU",
            "swift_code":"BANK123"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:04:36.072Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_mm2c4ax7p3YDNB",
      "type":"bank",
      "action":"instant",
      "reference":"kjvdcoihudfoidfpofjiof9r",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_pvu4uNFiT7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EGP",
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         },
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "email":"user@example.com",
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
      },
      "sender":{
         "id":"sdr_tGCFUvSdVu",
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         },
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "date_of_birth":"1980-11-25",
         "email":"alex@great.com",
         "address":{
            "city":"Cool City",
            "country":"EG",
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:29:48.366Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_zksyU4F4kFGZi7",
      "type":"bank",
      "action":"instant",
      "reference":"778989JHUTGHJGHJYUYIUY",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ETB",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ExC7XZKoC1",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ETB",
         "bank":{
            "account_number":"123456789",
            "code":"7"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:37:41.658Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_03mgMQvkcD1J4Q",
      "type":"bank",
      "action":"instant",
      "reference":"duuidiudodudududj77262",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"EUR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_2fh9yl2PCl",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EUR",
         "phone":{
            "country_code":"49",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"DE",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"9876543210",
            "name":"Continental Bank of Europe",
            "swift_code":"DEUTDEFF"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:42:32.080Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_psJZCQCkOcQl06",
      "type":"bank",
      "action":"instant",
      "reference":"jguyfghgyt7675hjg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"GHS",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ykW6hU75cU",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"GHS",
         "bank":{
            "account_number":"1234567890",
            "code":"25562284",
            "branch":"001"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:46:29.584Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_Gr4gqFAiDheMvc",
      "type":"bank",
      "action":"instant",
      "reference":"FYFTHGHGHJGhgyt57",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"INR",
      "destination_currency":"INR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_hKd3HybtHa",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"INR",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"IN",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "code":"SBIN",
            "branch":"SBIN0015615"
         }
      },
      "sender":{
         "id":"sdr_M37FKMARWj",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2025-06-02T16:53:09.632Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_t8w0OGSNOdV4P5",
      "type":"bank",
      "action":"instant",
      "reference":"GGUGTUYUHIIUIOU7",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"MWK",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_t68rd2GfZ7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"MWK",
         "bank":{
            "account_number":"123456789",
            "code":"20474000",
            "branch":"1812061ZP6"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:59:32.628Z"
   }
}
```

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "c3104347-5ebf-41bd-957c-7666df028bbe",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "USD",
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
            "id": "rcb_gsLlPvnOLy"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374991375Z"
    }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_NvhGENkNcnBI2t",
      "type":"bank",
      "action":"instant",
      "reference":"ugujbuujyujgjb7889",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"USD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_Yro1zlIF7I",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"USD",
         "phone":{
            "country_code":"1",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"US",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "account_type":"checking",
            "code":"125200057",
            "routing_number":"021000021",
            "swift_code":"BOFAUS3N"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:07:00.549Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_bf65ZmcvRt5tq3",
      "type":"bank",
      "action":"instant",
      "reference":"jhgvjhgjjyyiy79hg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ZAR",
      "destination_currency":"ZAR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_mQnFh6aMOB",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ZAR",
         "phone":{
            "country_code":"27",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"ZA",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "code":"ABSA"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:10:26.917Z"
   }
}
```

#### EUR Bank Transfer

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_HHB2Yrc3LUyooR",
      "type":"bank",
      "action":"instant",
      "reference":"duyiebieuei8eieu89383jhdjhdy",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"AUD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_v3jeBmSUxC",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"AUD",
         "phone":{
            "country_code":"61",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"AU",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "name":"Commonwealth Bank of Australia",
            "routing_number":"CTBAAU",
            "swift_code":"BANK123"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:04:36.072Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_mm2c4ax7p3YDNB",
      "type":"bank",
      "action":"instant",
      "reference":"kjvdcoihudfoidfpofjiof9r",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_pvu4uNFiT7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EGP",
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         },
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "email":"user@example.com",
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
      },
      "sender":{
         "id":"sdr_tGCFUvSdVu",
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         },
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "date_of_birth":"1980-11-25",
         "email":"alex@great.com",
         "address":{
            "city":"Cool City",
            "country":"EG",
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:29:48.366Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_zksyU4F4kFGZi7",
      "type":"bank",
      "action":"instant",
      "reference":"778989JHUTGHJGHJYUYIUY",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ETB",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ExC7XZKoC1",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ETB",
         "bank":{
            "account_number":"123456789",
            "code":"7"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:37:41.658Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_03mgMQvkcD1J4Q",
      "type":"bank",
      "action":"instant",
      "reference":"duuidiudodudududj77262",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"EUR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_2fh9yl2PCl",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EUR",
         "phone":{
            "country_code":"49",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"DE",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"9876543210",
            "name":"Continental Bank of Europe",
            "swift_code":"DEUTDEFF"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:42:32.080Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_psJZCQCkOcQl06",
      "type":"bank",
      "action":"instant",
      "reference":"jguyfghgyt7675hjg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"GHS",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ykW6hU75cU",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"GHS",
         "bank":{
            "account_number":"1234567890",
            "code":"25562284",
            "branch":"001"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:46:29.584Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_Gr4gqFAiDheMvc",
      "type":"bank",
      "action":"instant",
      "reference":"FYFTHGHGHJGhgyt57",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"INR",
      "destination_currency":"INR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_hKd3HybtHa",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"INR",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"IN",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "code":"SBIN",
            "branch":"SBIN0015615"
         }
      },
      "sender":{
         "id":"sdr_M37FKMARWj",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2025-06-02T16:53:09.632Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_t8w0OGSNOdV4P5",
      "type":"bank",
      "action":"instant",
      "reference":"GGUGTUYUHIIUIOU7",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"MWK",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_t68rd2GfZ7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"MWK",
         "bank":{
            "account_number":"123456789",
            "code":"20474000",
            "branch":"1812061ZP6"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:59:32.628Z"
   }
}
```

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "c3104347-5ebf-41bd-957c-7666df028bbe",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "USD",
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
            "id": "rcb_gsLlPvnOLy"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374991375Z"
    }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_NvhGENkNcnBI2t",
      "type":"bank",
      "action":"instant",
      "reference":"ugujbuujyujgjb7889",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"USD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_Yro1zlIF7I",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"USD",
         "phone":{
            "country_code":"1",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"US",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "account_type":"checking",
            "code":"125200057",
            "routing_number":"021000021",
            "swift_code":"BOFAUS3N"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:07:00.549Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_bf65ZmcvRt5tq3",
      "type":"bank",
      "action":"instant",
      "reference":"jhgvjhgjjyyiy79hg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ZAR",
      "destination_currency":"ZAR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_mQnFh6aMOB",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ZAR",
         "phone":{
            "country_code":"27",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"ZA",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "code":"ABSA"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:10:26.917Z"
   }
}
```

#### GHS Bank Transfer

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_HHB2Yrc3LUyooR",
      "type":"bank",
      "action":"instant",
      "reference":"duyiebieuei8eieu89383jhdjhdy",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"AUD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_v3jeBmSUxC",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"AUD",
         "phone":{
            "country_code":"61",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"AU",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "name":"Commonwealth Bank of Australia",
            "routing_number":"CTBAAU",
            "swift_code":"BANK123"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:04:36.072Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_mm2c4ax7p3YDNB",
      "type":"bank",
      "action":"instant",
      "reference":"kjvdcoihudfoidfpofjiof9r",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_pvu4uNFiT7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EGP",
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         },
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "email":"user@example.com",
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
      },
      "sender":{
         "id":"sdr_tGCFUvSdVu",
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         },
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "date_of_birth":"1980-11-25",
         "email":"alex@great.com",
         "address":{
            "city":"Cool City",
            "country":"EG",
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:29:48.366Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_zksyU4F4kFGZi7",
      "type":"bank",
      "action":"instant",
      "reference":"778989JHUTGHJGHJYUYIUY",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ETB",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ExC7XZKoC1",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ETB",
         "bank":{
            "account_number":"123456789",
            "code":"7"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:37:41.658Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_03mgMQvkcD1J4Q",
      "type":"bank",
      "action":"instant",
      "reference":"duuidiudodudududj77262",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"EUR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_2fh9yl2PCl",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EUR",
         "phone":{
            "country_code":"49",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"DE",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"9876543210",
            "name":"Continental Bank of Europe",
            "swift_code":"DEUTDEFF"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:42:32.080Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_psJZCQCkOcQl06",
      "type":"bank",
      "action":"instant",
      "reference":"jguyfghgyt7675hjg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"GHS",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ykW6hU75cU",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"GHS",
         "bank":{
            "account_number":"1234567890",
            "code":"25562284",
            "branch":"001"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:46:29.584Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_Gr4gqFAiDheMvc",
      "type":"bank",
      "action":"instant",
      "reference":"FYFTHGHGHJGhgyt57",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"INR",
      "destination_currency":"INR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_hKd3HybtHa",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"INR",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"IN",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "code":"SBIN",
            "branch":"SBIN0015615"
         }
      },
      "sender":{
         "id":"sdr_M37FKMARWj",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2025-06-02T16:53:09.632Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_t8w0OGSNOdV4P5",
      "type":"bank",
      "action":"instant",
      "reference":"GGUGTUYUHIIUIOU7",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"MWK",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_t68rd2GfZ7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"MWK",
         "bank":{
            "account_number":"123456789",
            "code":"20474000",
            "branch":"1812061ZP6"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:59:32.628Z"
   }
}
```

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "c3104347-5ebf-41bd-957c-7666df028bbe",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "USD",
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
            "id": "rcb_gsLlPvnOLy"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374991375Z"
    }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_NvhGENkNcnBI2t",
      "type":"bank",
      "action":"instant",
      "reference":"ugujbuujyujgjb7889",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"USD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_Yro1zlIF7I",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"USD",
         "phone":{
            "country_code":"1",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"US",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "account_type":"checking",
            "code":"125200057",
            "routing_number":"021000021",
            "swift_code":"BOFAUS3N"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:07:00.549Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_bf65ZmcvRt5tq3",
      "type":"bank",
      "action":"instant",
      "reference":"jhgvjhgjjyyiy79hg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ZAR",
      "destination_currency":"ZAR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_mQnFh6aMOB",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ZAR",
         "phone":{
            "country_code":"27",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"ZA",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "code":"ABSA"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:10:26.917Z"
   }
}
```

#### INR Bank Transfer

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_HHB2Yrc3LUyooR",
      "type":"bank",
      "action":"instant",
      "reference":"duyiebieuei8eieu89383jhdjhdy",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"AUD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_v3jeBmSUxC",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"AUD",
         "phone":{
            "country_code":"61",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"AU",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "name":"Commonwealth Bank of Australia",
            "routing_number":"CTBAAU",
            "swift_code":"BANK123"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:04:36.072Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_mm2c4ax7p3YDNB",
      "type":"bank",
      "action":"instant",
      "reference":"kjvdcoihudfoidfpofjiof9r",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_pvu4uNFiT7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EGP",
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         },
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "email":"user@example.com",
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
      },
      "sender":{
         "id":"sdr_tGCFUvSdVu",
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         },
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "date_of_birth":"1980-11-25",
         "email":"alex@great.com",
         "address":{
            "city":"Cool City",
            "country":"EG",
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:29:48.366Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_zksyU4F4kFGZi7",
      "type":"bank",
      "action":"instant",
      "reference":"778989JHUTGHJGHJYUYIUY",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ETB",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ExC7XZKoC1",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ETB",
         "bank":{
            "account_number":"123456789",
            "code":"7"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:37:41.658Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_03mgMQvkcD1J4Q",
      "type":"bank",
      "action":"instant",
      "reference":"duuidiudodudududj77262",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"EUR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_2fh9yl2PCl",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EUR",
         "phone":{
            "country_code":"49",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"DE",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"9876543210",
            "name":"Continental Bank of Europe",
            "swift_code":"DEUTDEFF"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:42:32.080Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_psJZCQCkOcQl06",
      "type":"bank",
      "action":"instant",
      "reference":"jguyfghgyt7675hjg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"GHS",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ykW6hU75cU",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"GHS",
         "bank":{
            "account_number":"1234567890",
            "code":"25562284",
            "branch":"001"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:46:29.584Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_Gr4gqFAiDheMvc",
      "type":"bank",
      "action":"instant",
      "reference":"FYFTHGHGHJGhgyt57",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"INR",
      "destination_currency":"INR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_hKd3HybtHa",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"INR",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"IN",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "code":"SBIN",
            "branch":"SBIN0015615"
         }
      },
      "sender":{
         "id":"sdr_M37FKMARWj",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2025-06-02T16:53:09.632Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_t8w0OGSNOdV4P5",
      "type":"bank",
      "action":"instant",
      "reference":"GGUGTUYUHIIUIOU7",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"MWK",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_t68rd2GfZ7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"MWK",
         "bank":{
            "account_number":"123456789",
            "code":"20474000",
            "branch":"1812061ZP6"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:59:32.628Z"
   }
}
```

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "c3104347-5ebf-41bd-957c-7666df028bbe",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "USD",
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
            "id": "rcb_gsLlPvnOLy"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374991375Z"
    }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_NvhGENkNcnBI2t",
      "type":"bank",
      "action":"instant",
      "reference":"ugujbuujyujgjb7889",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"USD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_Yro1zlIF7I",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"USD",
         "phone":{
            "country_code":"1",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"US",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "account_type":"checking",
            "code":"125200057",
            "routing_number":"021000021",
            "swift_code":"BOFAUS3N"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:07:00.549Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_bf65ZmcvRt5tq3",
      "type":"bank",
      "action":"instant",
      "reference":"jhgvjhgjjyyiy79hg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ZAR",
      "destination_currency":"ZAR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_mQnFh6aMOB",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ZAR",
         "phone":{
            "country_code":"27",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"ZA",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "code":"ABSA"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:10:26.917Z"
   }
}
```

#### MWK Bank Transfer

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_HHB2Yrc3LUyooR",
      "type":"bank",
      "action":"instant",
      "reference":"duyiebieuei8eieu89383jhdjhdy",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"AUD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_v3jeBmSUxC",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"AUD",
         "phone":{
            "country_code":"61",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"AU",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "name":"Commonwealth Bank of Australia",
            "routing_number":"CTBAAU",
            "swift_code":"BANK123"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:04:36.072Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_mm2c4ax7p3YDNB",
      "type":"bank",
      "action":"instant",
      "reference":"kjvdcoihudfoidfpofjiof9r",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_pvu4uNFiT7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EGP",
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         },
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "email":"user@example.com",
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
      },
      "sender":{
         "id":"sdr_tGCFUvSdVu",
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         },
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "date_of_birth":"1980-11-25",
         "email":"alex@great.com",
         "address":{
            "city":"Cool City",
            "country":"EG",
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:29:48.366Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_zksyU4F4kFGZi7",
      "type":"bank",
      "action":"instant",
      "reference":"778989JHUTGHJGHJYUYIUY",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ETB",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ExC7XZKoC1",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ETB",
         "bank":{
            "account_number":"123456789",
            "code":"7"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:37:41.658Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_03mgMQvkcD1J4Q",
      "type":"bank",
      "action":"instant",
      "reference":"duuidiudodudududj77262",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"EUR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_2fh9yl2PCl",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EUR",
         "phone":{
            "country_code":"49",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"DE",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"9876543210",
            "name":"Continental Bank of Europe",
            "swift_code":"DEUTDEFF"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:42:32.080Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_psJZCQCkOcQl06",
      "type":"bank",
      "action":"instant",
      "reference":"jguyfghgyt7675hjg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"GHS",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ykW6hU75cU",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"GHS",
         "bank":{
            "account_number":"1234567890",
            "code":"25562284",
            "branch":"001"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:46:29.584Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_Gr4gqFAiDheMvc",
      "type":"bank",
      "action":"instant",
      "reference":"FYFTHGHGHJGhgyt57",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"INR",
      "destination_currency":"INR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_hKd3HybtHa",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"INR",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"IN",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "code":"SBIN",
            "branch":"SBIN0015615"
         }
      },
      "sender":{
         "id":"sdr_M37FKMARWj",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2025-06-02T16:53:09.632Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_t8w0OGSNOdV4P5",
      "type":"bank",
      "action":"instant",
      "reference":"GGUGTUYUHIIUIOU7",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"MWK",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_t68rd2GfZ7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"MWK",
         "bank":{
            "account_number":"123456789",
            "code":"20474000",
            "branch":"1812061ZP6"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:59:32.628Z"
   }
}
```

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "c3104347-5ebf-41bd-957c-7666df028bbe",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "USD",
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
            "id": "rcb_gsLlPvnOLy"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374991375Z"
    }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_NvhGENkNcnBI2t",
      "type":"bank",
      "action":"instant",
      "reference":"ugujbuujyujgjb7889",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"USD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_Yro1zlIF7I",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"USD",
         "phone":{
            "country_code":"1",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"US",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "account_type":"checking",
            "code":"125200057",
            "routing_number":"021000021",
            "swift_code":"BOFAUS3N"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:07:00.549Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_bf65ZmcvRt5tq3",
      "type":"bank",
      "action":"instant",
      "reference":"jhgvjhgjjyyiy79hg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ZAR",
      "destination_currency":"ZAR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_mQnFh6aMOB",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ZAR",
         "phone":{
            "country_code":"27",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"ZA",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "code":"ABSA"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:10:26.917Z"
   }
}
```

#### NGN Bank Transfer

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_HHB2Yrc3LUyooR",
      "type":"bank",
      "action":"instant",
      "reference":"duyiebieuei8eieu89383jhdjhdy",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"AUD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_v3jeBmSUxC",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"AUD",
         "phone":{
            "country_code":"61",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"AU",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "name":"Commonwealth Bank of Australia",
            "routing_number":"CTBAAU",
            "swift_code":"BANK123"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:04:36.072Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_mm2c4ax7p3YDNB",
      "type":"bank",
      "action":"instant",
      "reference":"kjvdcoihudfoidfpofjiof9r",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"EGP",
      "destination_currency":"EGP",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_pvu4uNFiT7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EGP",
         "national_identification":{
            "type":"NATIONAL_ID",
            "identifier":"1234567890",
            "expiration_date":"2029-11-15"
         },
         "phone":{
            "country_code":"20",
            "number":"9012345678"
         },
         "email":"user@example.com",
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
      },
      "sender":{
         "id":"sdr_tGCFUvSdVu",
         "name":{
            "first":"Alexander",
            "middle":"The",
            "last":"Great"
         },
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-12-25"
         },
         "phone":{
            "country_code":"20",
            "number":"8012345679"
         },
         "date_of_birth":"1980-11-25",
         "email":"alex@great.com",
         "address":{
            "city":"Cool City",
            "country":"EG",
            "line1":"3B, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:29:48.366Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_zksyU4F4kFGZi7",
      "type":"bank",
      "action":"instant",
      "reference":"778989JHUTGHJGHJYUYIUY",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ETB",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ExC7XZKoC1",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ETB",
         "bank":{
            "account_number":"123456789",
            "code":"7"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:37:41.658Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_03mgMQvkcD1J4Q",
      "type":"bank",
      "action":"instant",
      "reference":"duuidiudodudududj77262",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"EUR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_2fh9yl2PCl",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"EUR",
         "phone":{
            "country_code":"49",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"DE",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"9876543210",
            "name":"Continental Bank of Europe",
            "swift_code":"DEUTDEFF"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:42:32.080Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_psJZCQCkOcQl06",
      "type":"bank",
      "action":"instant",
      "reference":"jguyfghgyt7675hjg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"GHS",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_ykW6hU75cU",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"GHS",
         "bank":{
            "account_number":"1234567890",
            "code":"25562284",
            "branch":"001"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:46:29.584Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_Gr4gqFAiDheMvc",
      "type":"bank",
      "action":"instant",
      "reference":"FYFTHGHGHJGhgyt57",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"INR",
      "destination_currency":"INR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_hKd3HybtHa",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"INR",
         "phone":{
            "country_code":"91",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"IN",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"123456789",
            "code":"SBIN",
            "branch":"SBIN0015615"
         }
      },
      "sender":{
         "id":"sdr_M37FKMARWj",
         "national_identification":{
            "type":"PASSPORT",
            "identifier":"0987654321",
            "expiration_date":"2028-11-25"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2025-06-02T16:53:09.632Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_t8w0OGSNOdV4P5",
      "type":"bank",
      "action":"instant",
      "reference":"GGUGTUYUHIIUIOU7",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"MWK",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_t68rd2GfZ7",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"MWK",
         "bank":{
            "account_number":"123456789",
            "code":"20474000",
            "branch":"1812061ZP6"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T16:59:32.628Z"
   }
}
```

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "c3104347-5ebf-41bd-957c-7666df028bbe",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "USD",
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
            "id": "rcb_gsLlPvnOLy"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374991375Z"
    }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_NvhGENkNcnBI2t",
      "type":"bank",
      "action":"instant",
      "reference":"ugujbuujyujgjb7889",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"USD",
      "destination_currency":"USD",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_Yro1zlIF7I",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"USD",
         "phone":{
            "country_code":"1",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"US",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "account_type":"checking",
            "code":"125200057",
            "routing_number":"021000021",
            "swift_code":"BOFAUS3N"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:07:00.549Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_bf65ZmcvRt5tq3",
      "type":"bank",
      "action":"instant",
      "reference":"jhgvjhgjjyyiy79hg",
      "status":"NEW",
      "narration":"Testing transfers",
      "source_currency":"ZAR",
      "destination_currency":"ZAR",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "callback_url":"https://www.company.com/callback",
      "recipient":{
         "type":"bank",
         "id":"rcb_mQnFh6aMOB",
         "name":{
            "first":"Bob",
            "middle":"The",
            "last":"Builder"
         },
         "currency":"ZAR",
         "phone":{
            "country_code":"27",
            "number":"9012345678"
         },
         "email":"user@example.com",
         "address":{
            "city":"Cool City",
            "country":"ZA",
            "line1":"7A, Awesome Apartments",
            "line2":"Sweet Street",
            "postal_code":"123456",
            "state":"Super State"
         },
         "bank":{
            "account_number":"1234567890",
            "code":"ABSA"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-02T17:10:26.917Z"
   }
}
```

The`data.status` field in the response will always return `NEW` upon initiating a transfer. This indicates that the transfer has been **successfully initiated**, but **not yet completed**. To determine the final status, you must verify the payout.

There are three ways to verify the final status of a bank transfer:

**Webhooks (Recommended)**  
Enable **webhooks** on your Flutterwave dashboard to receive automatic transfer status updates.  
When the transfer completes (or fails), Flutterwave will send a POST request to your configured webhook URL with the transfer details.

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

**Callback**  
If you included a `callback_url` in your transfer request, Flutterwave will send a POST request to that URL once the transfer completes or fails.  
This behaves similarly to webhooks but is specific to each transfer.

**Query Payout Status**  
To manually check the status of a transfer:

1.  Use the `id` value from the `data.id` field in the transfer initiation response.
2.  Send a `GET` request to the [retrieve a transfer endpoint](https://developer.flutterwave.com/reference/transfer_get), passing the id as a path parameter.

This is useful for polling or verifying status in systems where webhooks or callbacks are not used.

```curl
curl --request GET \
--url 'https://developersandbox-api.flutterwave.com/transfers/trf_iWUfJopFYdyBmB' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
```

You'll get a response like this:

#### 200 OK

```json
{
    "status": "success",
    "message": "Transfer fetched",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "c3104347-5ebf-41bd-957c-7666df028bbe",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "USD",
        "destination_currency": "NGN",
        "amount": {
            "value": 1000,
            "applies_to": "destination_currency"
        },
        "fee": {
            "currency": "NGN",
            "value": 10.0
        },
        "callback_url": "https://www.company.com/callback",
        "recipient": {
            "type": "bank",
            "currency": "NGN",
            "bank": {
                "account_number": "0690000031",
                "code": "044"
            },
            "id": "rcb_gsLlPvnOLy"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374Z"
    }
}
```

```json
{
   "status":"failed",
   "error":{
      "type":"TRANSFER_NOT_FOUND",
      "code":"301404",
      "message":"Transfer not found",
      "validation_errors":[
         
      ]
   }
}
```

#### 400 Bad Request

```json
{
    "status": "success",
    "message": "Transfer fetched",
    "data": {
        "id": "trf_iWUfJopFYdyBmB",
        "type": "bank",
        "action": "instant",
        "reference": "c3104347-5ebf-41bd-957c-7666df028bbe",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "USD",
        "destination_currency": "NGN",
        "amount": {
            "value": 1000,
            "applies_to": "destination_currency"
        },
        "fee": {
            "currency": "NGN",
            "value": 10.0
        },
        "callback_url": "https://www.company.com/callback",
        "recipient": {
            "type": "bank",
            "currency": "NGN",
            "bank": {
                "account_number": "0690000031",
                "code": "044"
            },
            "id": "rcb_gsLlPvnOLy"
        },
        "meta": {},
        "created_datetime": "2024-12-10T13:49:06.374Z"
    }
}
```

```json
{
   "status":"failed",
   "error":{
      "type":"TRANSFER_NOT_FOUND",
      "code":"301404",
      "message":"Transfer not found",
      "validation_errors":[
         
      ]
   }
}
```

Check out the [testing section](../direct-transfer-flow/index.md#testing-transfers) to learn how to simulate various transfer scenarios.

Updated 7 months ago

* * *
