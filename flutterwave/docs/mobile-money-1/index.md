---
title: "Mobile Money Transfers"
source: "https://developer.flutterwave.com/docs/mobile-money-1#"
canonical_url: "https://developer.flutterwave.com/docs/mobile-money-1"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:46.906Z"
content_hash: "6de7d34a1611d1fe27a151824ee76377e166e38411335e81aa6aad24e0cd0e3e"
menu_path: ["Mobile Money Transfers"]
section_path: []
tab_variants: ["GHS_MOMO_PAYOUT","KES_MOMO_PAYOUT","TZS_MOMO_PAYOUT","XAF(CM)_MOMO_PAYOUT","XOF(CI)_MOMO_PAYOUT","XOF(SN)_MOMO_PAYOUT","RWF_MOMO_PAYOUT","MWK_MOMO_PAYOUT","GHS Payout","KES Payout","TZS Payout","XAF(CM) Payout","XOF(CI) Payout","XOF(SN) Payout","RWF Payout","MWK Payout","200 OK","400 Bad Request"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/bank-transfer/index.md", "title": "Bank Account Transfers"}
nav_next: {"path": "flutterwave/docs/wallet-to-wallet/index.md", "title": "Wallet-to-Wallet"}
---

Flutterwave allows customers to transfer funds directly from their Flutterwave balance to a mobile money wallet. This feature enables merchants to seamlessly process payouts into wallets linked to recipients' mobile numbers.

Before initiating a mobile money transfer:

-   Whitelist your IP addresses
-   Ensure your balance has sufficient funds. You can fund your balance by one of the following methods:
    -   Directly funding via [collections](../introduction-1/index.md).
    -   Indirect funding by converting funds from a different currency balance (i.e., wallet-to-wallet transfers).

Each successful mobile money transfer follows a two-step process:

-   Initiate Payout
-   Verify Payout

> ## 🚧
> 
> Integration Method
> 
> This guide follows the direct transfer flow for demonstration. Please refer to the [general transfer flow](https://developer.flutterwave.com/v4.0/docs/general-transfer-flow) for the alternative integration method.

To initiate a mobile money transfer, send a request to the [create transfer endpoint](https://developer.flutterwave.com/reference/direct_transfers_post) with the following required parameters:

-   `action`: Specifies how the transfer should be processed. Accepted values are `instant`, `deferred`, or `scheduled`.
-   `type`: Specifies the type of transfer. Use `"mobile_money"` for mobile money transfers.
-   `payment_instruction`: An object containing details of the payment, including:
    -   `amount`
    -   `currency` (`source_currency` and `destination_currency`)
    -   Recipient details, such as the phone number linked to the mobile money wallet and the associated [mobile money network](https://developer.flutterwave.com/reference/mobile_networks_get).

#### GHS\_MOMO\_PAYOUT

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "destination_currency":"GHS"
   },
   "type":"mobile_money",
   "narration":"GHS MOMO TRANSFER EXAMPLE",
   "reference":"REF-00107099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "destination_currency":"KES"
   },
   "type":"mobile_money",
   "narration":"KES MOMO TRANSFER EXAMPLE",
   "reference":"REF-001GVSDVDSU2Y"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "mobile_money":{
            "msisdn":"2559012345678",
            "network":"airtel"
         }
      },
      "destination_currency":"TZS"
   },
   "type":"mobile_money",
   "narration":"TZS MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "destination_currency":"XAF"
   },
   "type":"mobile_money",
   "narration":"XAF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00100IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-0010099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00108099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         }
      },
      "destination_currency":"RWF"
   },
   "type":"mobile_money",
   "narration":"RWF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00147099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "destination_currency":"MWK"
   },
   "type":"mobile_money",
   "narration":"MWK MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "destination_currency":"ETB"
   },
   "type":"mobile_money",
   "narration":"ETB MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "destination_currency":"UGX"
   },
   "type":"mobile_money",
   "narration":"UGX MOMO TRANSFER EXAMPLE",
   "reference":"REF-001OEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "destination_currency":"ZMW"
   },
   "type":"mobile_money",
   "narration":"ZMW MOMO TRANSFER EXAMPLE",
   "reference":"REF-001O9EDeWDSUYB"
}'
```

#### KES\_MOMO\_PAYOUT

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "destination_currency":"GHS"
   },
   "type":"mobile_money",
   "narration":"GHS MOMO TRANSFER EXAMPLE",
   "reference":"REF-00107099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "destination_currency":"KES"
   },
   "type":"mobile_money",
   "narration":"KES MOMO TRANSFER EXAMPLE",
   "reference":"REF-001GVSDVDSU2Y"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "mobile_money":{
            "msisdn":"2559012345678",
            "network":"airtel"
         }
      },
      "destination_currency":"TZS"
   },
   "type":"mobile_money",
   "narration":"TZS MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "destination_currency":"XAF"
   },
   "type":"mobile_money",
   "narration":"XAF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00100IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-0010099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00108099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         }
      },
      "destination_currency":"RWF"
   },
   "type":"mobile_money",
   "narration":"RWF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00147099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "destination_currency":"MWK"
   },
   "type":"mobile_money",
   "narration":"MWK MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "destination_currency":"ETB"
   },
   "type":"mobile_money",
   "narration":"ETB MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "destination_currency":"UGX"
   },
   "type":"mobile_money",
   "narration":"UGX MOMO TRANSFER EXAMPLE",
   "reference":"REF-001OEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "destination_currency":"ZMW"
   },
   "type":"mobile_money",
   "narration":"ZMW MOMO TRANSFER EXAMPLE",
   "reference":"REF-001O9EDeWDSUYB"
}'
```

#### TZS\_MOMO\_PAYOUT

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "destination_currency":"GHS"
   },
   "type":"mobile_money",
   "narration":"GHS MOMO TRANSFER EXAMPLE",
   "reference":"REF-00107099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "destination_currency":"KES"
   },
   "type":"mobile_money",
   "narration":"KES MOMO TRANSFER EXAMPLE",
   "reference":"REF-001GVSDVDSU2Y"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "mobile_money":{
            "msisdn":"2559012345678",
            "network":"airtel"
         }
      },
      "destination_currency":"TZS"
   },
   "type":"mobile_money",
   "narration":"TZS MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "destination_currency":"XAF"
   },
   "type":"mobile_money",
   "narration":"XAF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00100IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-0010099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00108099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         }
      },
      "destination_currency":"RWF"
   },
   "type":"mobile_money",
   "narration":"RWF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00147099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "destination_currency":"MWK"
   },
   "type":"mobile_money",
   "narration":"MWK MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "destination_currency":"ETB"
   },
   "type":"mobile_money",
   "narration":"ETB MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "destination_currency":"UGX"
   },
   "type":"mobile_money",
   "narration":"UGX MOMO TRANSFER EXAMPLE",
   "reference":"REF-001OEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "destination_currency":"ZMW"
   },
   "type":"mobile_money",
   "narration":"ZMW MOMO TRANSFER EXAMPLE",
   "reference":"REF-001O9EDeWDSUYB"
}'
```

#### XAF(CM)\_MOMO\_PAYOUT

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "destination_currency":"GHS"
   },
   "type":"mobile_money",
   "narration":"GHS MOMO TRANSFER EXAMPLE",
   "reference":"REF-00107099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "destination_currency":"KES"
   },
   "type":"mobile_money",
   "narration":"KES MOMO TRANSFER EXAMPLE",
   "reference":"REF-001GVSDVDSU2Y"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "mobile_money":{
            "msisdn":"2559012345678",
            "network":"airtel"
         }
      },
      "destination_currency":"TZS"
   },
   "type":"mobile_money",
   "narration":"TZS MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "destination_currency":"XAF"
   },
   "type":"mobile_money",
   "narration":"XAF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00100IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-0010099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00108099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         }
      },
      "destination_currency":"RWF"
   },
   "type":"mobile_money",
   "narration":"RWF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00147099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "destination_currency":"MWK"
   },
   "type":"mobile_money",
   "narration":"MWK MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "destination_currency":"ETB"
   },
   "type":"mobile_money",
   "narration":"ETB MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "destination_currency":"UGX"
   },
   "type":"mobile_money",
   "narration":"UGX MOMO TRANSFER EXAMPLE",
   "reference":"REF-001OEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "destination_currency":"ZMW"
   },
   "type":"mobile_money",
   "narration":"ZMW MOMO TRANSFER EXAMPLE",
   "reference":"REF-001O9EDeWDSUYB"
}'
```

#### XOF(CI)\_MOMO\_PAYOUT

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "destination_currency":"GHS"
   },
   "type":"mobile_money",
   "narration":"GHS MOMO TRANSFER EXAMPLE",
   "reference":"REF-00107099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "destination_currency":"KES"
   },
   "type":"mobile_money",
   "narration":"KES MOMO TRANSFER EXAMPLE",
   "reference":"REF-001GVSDVDSU2Y"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "mobile_money":{
            "msisdn":"2559012345678",
            "network":"airtel"
         }
      },
      "destination_currency":"TZS"
   },
   "type":"mobile_money",
   "narration":"TZS MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "destination_currency":"XAF"
   },
   "type":"mobile_money",
   "narration":"XAF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00100IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-0010099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00108099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         }
      },
      "destination_currency":"RWF"
   },
   "type":"mobile_money",
   "narration":"RWF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00147099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "destination_currency":"MWK"
   },
   "type":"mobile_money",
   "narration":"MWK MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "destination_currency":"ETB"
   },
   "type":"mobile_money",
   "narration":"ETB MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "destination_currency":"UGX"
   },
   "type":"mobile_money",
   "narration":"UGX MOMO TRANSFER EXAMPLE",
   "reference":"REF-001OEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "destination_currency":"ZMW"
   },
   "type":"mobile_money",
   "narration":"ZMW MOMO TRANSFER EXAMPLE",
   "reference":"REF-001O9EDeWDSUYB"
}'
```

#### XOF(SN)\_MOMO\_PAYOUT

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "destination_currency":"GHS"
   },
   "type":"mobile_money",
   "narration":"GHS MOMO TRANSFER EXAMPLE",
   "reference":"REF-00107099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "destination_currency":"KES"
   },
   "type":"mobile_money",
   "narration":"KES MOMO TRANSFER EXAMPLE",
   "reference":"REF-001GVSDVDSU2Y"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "mobile_money":{
            "msisdn":"2559012345678",
            "network":"airtel"
         }
      },
      "destination_currency":"TZS"
   },
   "type":"mobile_money",
   "narration":"TZS MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "destination_currency":"XAF"
   },
   "type":"mobile_money",
   "narration":"XAF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00100IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-0010099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00108099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         }
      },
      "destination_currency":"RWF"
   },
   "type":"mobile_money",
   "narration":"RWF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00147099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "destination_currency":"MWK"
   },
   "type":"mobile_money",
   "narration":"MWK MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "destination_currency":"ETB"
   },
   "type":"mobile_money",
   "narration":"ETB MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "destination_currency":"UGX"
   },
   "type":"mobile_money",
   "narration":"UGX MOMO TRANSFER EXAMPLE",
   "reference":"REF-001OEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "destination_currency":"ZMW"
   },
   "type":"mobile_money",
   "narration":"ZMW MOMO TRANSFER EXAMPLE",
   "reference":"REF-001O9EDeWDSUYB"
}'
```

#### RWF\_MOMO\_PAYOUT

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "destination_currency":"GHS"
   },
   "type":"mobile_money",
   "narration":"GHS MOMO TRANSFER EXAMPLE",
   "reference":"REF-00107099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "destination_currency":"KES"
   },
   "type":"mobile_money",
   "narration":"KES MOMO TRANSFER EXAMPLE",
   "reference":"REF-001GVSDVDSU2Y"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "mobile_money":{
            "msisdn":"2559012345678",
            "network":"airtel"
         }
      },
      "destination_currency":"TZS"
   },
   "type":"mobile_money",
   "narration":"TZS MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "destination_currency":"XAF"
   },
   "type":"mobile_money",
   "narration":"XAF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00100IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-0010099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00108099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         }
      },
      "destination_currency":"RWF"
   },
   "type":"mobile_money",
   "narration":"RWF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00147099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "destination_currency":"MWK"
   },
   "type":"mobile_money",
   "narration":"MWK MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "destination_currency":"ETB"
   },
   "type":"mobile_money",
   "narration":"ETB MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "destination_currency":"UGX"
   },
   "type":"mobile_money",
   "narration":"UGX MOMO TRANSFER EXAMPLE",
   "reference":"REF-001OEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "destination_currency":"ZMW"
   },
   "type":"mobile_money",
   "narration":"ZMW MOMO TRANSFER EXAMPLE",
   "reference":"REF-001O9EDeWDSUYB"
}'
```

#### MWK\_MOMO\_PAYOUT

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/direct-transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "action":"instant",
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "destination_currency":"GHS"
   },
   "type":"mobile_money",
   "narration":"GHS MOMO TRANSFER EXAMPLE",
   "reference":"REF-00107099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "destination_currency":"KES"
   },
   "type":"mobile_money",
   "narration":"KES MOMO TRANSFER EXAMPLE",
   "reference":"REF-001GVSDVDSU2Y"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "mobile_money":{
            "msisdn":"2559012345678",
            "network":"airtel"
         }
      },
      "destination_currency":"TZS"
   },
   "type":"mobile_money",
   "narration":"TZS MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "destination_currency":"XAF"
   },
   "type":"mobile_money",
   "narration":"XAF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00100IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-0010099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "destination_currency":"XOF"
   },
   "type":"mobile_money",
   "narration":"XOF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00108099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         }
      },
      "destination_currency":"RWF"
   },
   "type":"mobile_money",
   "narration":"RWF MOMO TRANSFER EXAMPLE",
   "reference":"REF-00147099IEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "destination_currency":"MWK"
   },
   "type":"mobile_money",
   "narration":"MWK MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "destination_currency":"ETB"
   },
   "type":"mobile_money",
   "narration":"ETB MOMO TRANSFER EXAMPLE",
   "reference":"REF-001JYDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "destination_currency":"UGX"
   },
   "type":"mobile_money",
   "narration":"UGX MOMO TRANSFER EXAMPLE",
   "reference":"REF-001OEDeWDSUYB"
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
   "payment_instruction":{
      "source_currency":"NGN",
      "amount":{
         "applies_to":"destination_currency",
         "value":1000
      },
      "recipient":{
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "destination_currency":"ZMW"
   },
   "type":"mobile_money",
   "narration":"ZMW MOMO TRANSFER EXAMPLE",
   "reference":"REF-001O9EDeWDSUYB"
}'
```

> ## 🚧
> 
> Handling Mobile Number
> 
> The `msisdn` field must contain the recipient’s mobile number **starting with the country code**.
> 
> -   For example, a `GHS` mobile money transfer should begin with `233`.
> -   For `XAF` and `XOF` transfers, include the country field explicitly in the request.

You can initiate **scheduled** or **deferred** mobile money transfers by setting the `action` field to `scheduled` or `deferred`.

For **scheduled** transfers, include the `disburse_option` object in the request. This object defines when the transfer should be executed and must contain:

-   `date_time`: The exact date and time to trigger the transfer.
-   `timezone`: The timezone for the scheduled time.

Refer to the [transfer overview](../introduction-3/index.md#full-example) for a complete walkthrough on creating and managing these transfer types.

> ## 💱
> 
> Handling International Transfers
> 
> To manage cross-currency payouts, refer to the [managing currency](../direct-transfer-flow/index.md#cross-currency-transfers) section.

When you successfully initiate a mobile money transfer, the API returns a response similar to the following:

#### GHS Payout

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_5JnyBhdTdj42zA",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00107099IEDeWDSUYB",
      "status":"NEW",
      "narration":"GHS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_R8XvW9gXRP",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"GHS",
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:10:38.039Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_MNk7e9ups3VgZh",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001GVSDVDSU2Y",
      "status":"NEW",
      "narration":"KES MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"KES",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_VgJamvD4fE",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"KES",
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:21:47.932Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_O13h3LmPak5LBk",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JEDeWDSUYB",
      "status":"NEW",
      "narration":"TZS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"TZS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_MQzTgQgkQe",
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "currency":"TZS",
         "mobile_money":{
            "network":"airtel",
            "msisdn":"2559012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:31:11.232Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_fTdRGZIG7OGe20",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00100IEDeWDSUYB",
      "status":"NEW",
      "narration":"XAF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XAF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_8z3I4ICHIL",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XAF",
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:35:12.797Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_EJ2vQnQvFzeBFK",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-0010099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_c1ZhDIPcm7",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:39:23.780Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_p5kyu7ZCrgQpgI",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00108099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_ckorR5bbk0",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:43:40.755Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_pZwUKMs9usU5QD",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00147099IEDeWDSUYB",
      "status":"NEW",
      "narration":"RWF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"RWF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"RWF",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         },
         "id":"rcm_q1boxqkoC3"
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-13T05:13:14.569373217Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ESaFaZjxqnNmm2",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDWDSUYB",
      "status":"NEW",
      "narration":"MWK MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_YfQrGYgC5B",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"MWK",
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:49:04.563Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ktnCglatt92k8n",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDeWDSUYB",
      "status":"NEW",
      "narration":"ETB MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_uodrObhEa5",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ETB",
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:51:36.235Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_V5zoB57shPwgac",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001OEDeWDSUYB",
      "status":"NEW",
      "narration":"UGX MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"UGX",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_yJBzZTFEnj",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"UGX",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T12:59:15.403332030Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ejDNIQngjLzUTx",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001O9EDeWDSUYB",
      "status":"NEW",
      "narration":"ZMW MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ZMW",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_1aaTfsip3I",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ZMW",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T13:02:53.774008555Z"
   }
}
```

#### KES Payout

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_5JnyBhdTdj42zA",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00107099IEDeWDSUYB",
      "status":"NEW",
      "narration":"GHS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_R8XvW9gXRP",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"GHS",
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:10:38.039Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_MNk7e9ups3VgZh",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001GVSDVDSU2Y",
      "status":"NEW",
      "narration":"KES MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"KES",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_VgJamvD4fE",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"KES",
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:21:47.932Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_O13h3LmPak5LBk",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JEDeWDSUYB",
      "status":"NEW",
      "narration":"TZS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"TZS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_MQzTgQgkQe",
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "currency":"TZS",
         "mobile_money":{
            "network":"airtel",
            "msisdn":"2559012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:31:11.232Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_fTdRGZIG7OGe20",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00100IEDeWDSUYB",
      "status":"NEW",
      "narration":"XAF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XAF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_8z3I4ICHIL",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XAF",
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:35:12.797Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_EJ2vQnQvFzeBFK",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-0010099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_c1ZhDIPcm7",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:39:23.780Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_p5kyu7ZCrgQpgI",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00108099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_ckorR5bbk0",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:43:40.755Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_pZwUKMs9usU5QD",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00147099IEDeWDSUYB",
      "status":"NEW",
      "narration":"RWF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"RWF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"RWF",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         },
         "id":"rcm_q1boxqkoC3"
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-13T05:13:14.569373217Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ESaFaZjxqnNmm2",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDWDSUYB",
      "status":"NEW",
      "narration":"MWK MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_YfQrGYgC5B",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"MWK",
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:49:04.563Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ktnCglatt92k8n",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDeWDSUYB",
      "status":"NEW",
      "narration":"ETB MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_uodrObhEa5",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ETB",
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:51:36.235Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_V5zoB57shPwgac",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001OEDeWDSUYB",
      "status":"NEW",
      "narration":"UGX MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"UGX",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_yJBzZTFEnj",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"UGX",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T12:59:15.403332030Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ejDNIQngjLzUTx",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001O9EDeWDSUYB",
      "status":"NEW",
      "narration":"ZMW MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ZMW",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_1aaTfsip3I",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ZMW",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T13:02:53.774008555Z"
   }
}
```

#### TZS Payout

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_5JnyBhdTdj42zA",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00107099IEDeWDSUYB",
      "status":"NEW",
      "narration":"GHS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_R8XvW9gXRP",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"GHS",
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:10:38.039Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_MNk7e9ups3VgZh",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001GVSDVDSU2Y",
      "status":"NEW",
      "narration":"KES MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"KES",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_VgJamvD4fE",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"KES",
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:21:47.932Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_O13h3LmPak5LBk",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JEDeWDSUYB",
      "status":"NEW",
      "narration":"TZS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"TZS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_MQzTgQgkQe",
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "currency":"TZS",
         "mobile_money":{
            "network":"airtel",
            "msisdn":"2559012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:31:11.232Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_fTdRGZIG7OGe20",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00100IEDeWDSUYB",
      "status":"NEW",
      "narration":"XAF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XAF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_8z3I4ICHIL",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XAF",
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:35:12.797Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_EJ2vQnQvFzeBFK",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-0010099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_c1ZhDIPcm7",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:39:23.780Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_p5kyu7ZCrgQpgI",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00108099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_ckorR5bbk0",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:43:40.755Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_pZwUKMs9usU5QD",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00147099IEDeWDSUYB",
      "status":"NEW",
      "narration":"RWF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"RWF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"RWF",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         },
         "id":"rcm_q1boxqkoC3"
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-13T05:13:14.569373217Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ESaFaZjxqnNmm2",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDWDSUYB",
      "status":"NEW",
      "narration":"MWK MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_YfQrGYgC5B",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"MWK",
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:49:04.563Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ktnCglatt92k8n",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDeWDSUYB",
      "status":"NEW",
      "narration":"ETB MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_uodrObhEa5",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ETB",
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:51:36.235Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_V5zoB57shPwgac",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001OEDeWDSUYB",
      "status":"NEW",
      "narration":"UGX MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"UGX",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_yJBzZTFEnj",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"UGX",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T12:59:15.403332030Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ejDNIQngjLzUTx",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001O9EDeWDSUYB",
      "status":"NEW",
      "narration":"ZMW MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ZMW",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_1aaTfsip3I",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ZMW",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T13:02:53.774008555Z"
   }
}
```

#### XAF(CM) Payout

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_5JnyBhdTdj42zA",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00107099IEDeWDSUYB",
      "status":"NEW",
      "narration":"GHS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_R8XvW9gXRP",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"GHS",
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:10:38.039Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_MNk7e9ups3VgZh",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001GVSDVDSU2Y",
      "status":"NEW",
      "narration":"KES MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"KES",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_VgJamvD4fE",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"KES",
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:21:47.932Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_O13h3LmPak5LBk",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JEDeWDSUYB",
      "status":"NEW",
      "narration":"TZS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"TZS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_MQzTgQgkQe",
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "currency":"TZS",
         "mobile_money":{
            "network":"airtel",
            "msisdn":"2559012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:31:11.232Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_fTdRGZIG7OGe20",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00100IEDeWDSUYB",
      "status":"NEW",
      "narration":"XAF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XAF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_8z3I4ICHIL",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XAF",
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:35:12.797Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_EJ2vQnQvFzeBFK",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-0010099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_c1ZhDIPcm7",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:39:23.780Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_p5kyu7ZCrgQpgI",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00108099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_ckorR5bbk0",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:43:40.755Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_pZwUKMs9usU5QD",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00147099IEDeWDSUYB",
      "status":"NEW",
      "narration":"RWF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"RWF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"RWF",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         },
         "id":"rcm_q1boxqkoC3"
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-13T05:13:14.569373217Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ESaFaZjxqnNmm2",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDWDSUYB",
      "status":"NEW",
      "narration":"MWK MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_YfQrGYgC5B",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"MWK",
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:49:04.563Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ktnCglatt92k8n",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDeWDSUYB",
      "status":"NEW",
      "narration":"ETB MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_uodrObhEa5",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ETB",
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:51:36.235Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_V5zoB57shPwgac",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001OEDeWDSUYB",
      "status":"NEW",
      "narration":"UGX MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"UGX",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_yJBzZTFEnj",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"UGX",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T12:59:15.403332030Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ejDNIQngjLzUTx",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001O9EDeWDSUYB",
      "status":"NEW",
      "narration":"ZMW MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ZMW",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_1aaTfsip3I",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ZMW",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T13:02:53.774008555Z"
   }
}
```

#### XOF(CI) Payout

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_5JnyBhdTdj42zA",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00107099IEDeWDSUYB",
      "status":"NEW",
      "narration":"GHS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_R8XvW9gXRP",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"GHS",
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:10:38.039Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_MNk7e9ups3VgZh",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001GVSDVDSU2Y",
      "status":"NEW",
      "narration":"KES MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"KES",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_VgJamvD4fE",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"KES",
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:21:47.932Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_O13h3LmPak5LBk",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JEDeWDSUYB",
      "status":"NEW",
      "narration":"TZS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"TZS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_MQzTgQgkQe",
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "currency":"TZS",
         "mobile_money":{
            "network":"airtel",
            "msisdn":"2559012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:31:11.232Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_fTdRGZIG7OGe20",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00100IEDeWDSUYB",
      "status":"NEW",
      "narration":"XAF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XAF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_8z3I4ICHIL",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XAF",
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:35:12.797Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_EJ2vQnQvFzeBFK",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-0010099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_c1ZhDIPcm7",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:39:23.780Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_p5kyu7ZCrgQpgI",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00108099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_ckorR5bbk0",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:43:40.755Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_pZwUKMs9usU5QD",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00147099IEDeWDSUYB",
      "status":"NEW",
      "narration":"RWF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"RWF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"RWF",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         },
         "id":"rcm_q1boxqkoC3"
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-13T05:13:14.569373217Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ESaFaZjxqnNmm2",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDWDSUYB",
      "status":"NEW",
      "narration":"MWK MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_YfQrGYgC5B",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"MWK",
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:49:04.563Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ktnCglatt92k8n",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDeWDSUYB",
      "status":"NEW",
      "narration":"ETB MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_uodrObhEa5",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ETB",
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:51:36.235Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_V5zoB57shPwgac",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001OEDeWDSUYB",
      "status":"NEW",
      "narration":"UGX MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"UGX",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_yJBzZTFEnj",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"UGX",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T12:59:15.403332030Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ejDNIQngjLzUTx",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001O9EDeWDSUYB",
      "status":"NEW",
      "narration":"ZMW MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ZMW",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_1aaTfsip3I",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ZMW",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T13:02:53.774008555Z"
   }
}
```

#### XOF(SN) Payout

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_5JnyBhdTdj42zA",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00107099IEDeWDSUYB",
      "status":"NEW",
      "narration":"GHS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_R8XvW9gXRP",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"GHS",
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:10:38.039Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_MNk7e9ups3VgZh",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001GVSDVDSU2Y",
      "status":"NEW",
      "narration":"KES MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"KES",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_VgJamvD4fE",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"KES",
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:21:47.932Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_O13h3LmPak5LBk",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JEDeWDSUYB",
      "status":"NEW",
      "narration":"TZS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"TZS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_MQzTgQgkQe",
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "currency":"TZS",
         "mobile_money":{
            "network":"airtel",
            "msisdn":"2559012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:31:11.232Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_fTdRGZIG7OGe20",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00100IEDeWDSUYB",
      "status":"NEW",
      "narration":"XAF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XAF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_8z3I4ICHIL",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XAF",
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:35:12.797Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_EJ2vQnQvFzeBFK",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-0010099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_c1ZhDIPcm7",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:39:23.780Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_p5kyu7ZCrgQpgI",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00108099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_ckorR5bbk0",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:43:40.755Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_pZwUKMs9usU5QD",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00147099IEDeWDSUYB",
      "status":"NEW",
      "narration":"RWF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"RWF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"RWF",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         },
         "id":"rcm_q1boxqkoC3"
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-13T05:13:14.569373217Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ESaFaZjxqnNmm2",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDWDSUYB",
      "status":"NEW",
      "narration":"MWK MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_YfQrGYgC5B",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"MWK",
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:49:04.563Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ktnCglatt92k8n",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDeWDSUYB",
      "status":"NEW",
      "narration":"ETB MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_uodrObhEa5",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ETB",
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:51:36.235Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_V5zoB57shPwgac",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001OEDeWDSUYB",
      "status":"NEW",
      "narration":"UGX MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"UGX",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_yJBzZTFEnj",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"UGX",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T12:59:15.403332030Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ejDNIQngjLzUTx",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001O9EDeWDSUYB",
      "status":"NEW",
      "narration":"ZMW MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ZMW",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_1aaTfsip3I",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ZMW",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T13:02:53.774008555Z"
   }
}
```

#### RWF Payout

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_5JnyBhdTdj42zA",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00107099IEDeWDSUYB",
      "status":"NEW",
      "narration":"GHS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_R8XvW9gXRP",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"GHS",
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:10:38.039Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_MNk7e9ups3VgZh",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001GVSDVDSU2Y",
      "status":"NEW",
      "narration":"KES MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"KES",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_VgJamvD4fE",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"KES",
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:21:47.932Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_O13h3LmPak5LBk",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JEDeWDSUYB",
      "status":"NEW",
      "narration":"TZS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"TZS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_MQzTgQgkQe",
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "currency":"TZS",
         "mobile_money":{
            "network":"airtel",
            "msisdn":"2559012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:31:11.232Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_fTdRGZIG7OGe20",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00100IEDeWDSUYB",
      "status":"NEW",
      "narration":"XAF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XAF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_8z3I4ICHIL",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XAF",
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:35:12.797Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_EJ2vQnQvFzeBFK",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-0010099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_c1ZhDIPcm7",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:39:23.780Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_p5kyu7ZCrgQpgI",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00108099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_ckorR5bbk0",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:43:40.755Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_pZwUKMs9usU5QD",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00147099IEDeWDSUYB",
      "status":"NEW",
      "narration":"RWF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"RWF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"RWF",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         },
         "id":"rcm_q1boxqkoC3"
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-13T05:13:14.569373217Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ESaFaZjxqnNmm2",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDWDSUYB",
      "status":"NEW",
      "narration":"MWK MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_YfQrGYgC5B",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"MWK",
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:49:04.563Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ktnCglatt92k8n",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDeWDSUYB",
      "status":"NEW",
      "narration":"ETB MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_uodrObhEa5",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ETB",
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:51:36.235Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_V5zoB57shPwgac",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001OEDeWDSUYB",
      "status":"NEW",
      "narration":"UGX MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"UGX",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_yJBzZTFEnj",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"UGX",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T12:59:15.403332030Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ejDNIQngjLzUTx",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001O9EDeWDSUYB",
      "status":"NEW",
      "narration":"ZMW MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ZMW",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_1aaTfsip3I",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ZMW",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T13:02:53.774008555Z"
   }
}
```

#### MWK Payout

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_5JnyBhdTdj42zA",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00107099IEDeWDSUYB",
      "status":"NEW",
      "narration":"GHS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"GHS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_R8XvW9gXRP",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"GHS",
         "mobile_money":{
            "network":"MTN",
            "msisdn":"2339012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:10:38.039Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_MNk7e9ups3VgZh",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001GVSDVDSU2Y",
      "status":"NEW",
      "narration":"KES MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"KES",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_VgJamvD4fE",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"KES",
         "mobile_money":{
            "network":"Mpesa",
            "msisdn":"2549012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:21:47.932Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_O13h3LmPak5LBk",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JEDeWDSUYB",
      "status":"NEW",
      "narration":"TZS MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"TZS",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_MQzTgQgkQe",
         "name":{
            "first":"John ",
            "last":"Doe"
         },
         "currency":"TZS",
         "mobile_money":{
            "network":"airtel",
            "msisdn":"2559012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:31:11.232Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_fTdRGZIG7OGe20",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00100IEDeWDSUYB",
      "status":"NEW",
      "narration":"XAF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XAF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_8z3I4ICHIL",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XAF",
         "mobile_money":{
            "network":"orangemoney",
            "country":"CM",
            "msisdn":"23709929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:35:12.797Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_EJ2vQnQvFzeBFK",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-0010099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_c1ZhDIPcm7",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"wave",
            "country":"CI",
            "msisdn":"22509929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:39:23.780Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_p5kyu7ZCrgQpgI",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00108099IEDeWDSUYB",
      "status":"NEW",
      "narration":"XOF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"XOF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_ckorR5bbk0",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"XOF",
         "mobile_money":{
            "network":"EMONEY",
            "country":"SN",
            "msisdn":"22109929220"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:43:40.755Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_pZwUKMs9usU5QD",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-00147099IEDeWDSUYB",
      "status":"NEW",
      "narration":"RWF MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"RWF",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"RWF",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2509012345678"
         },
         "id":"rcm_q1boxqkoC3"
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-13T05:13:14.569373217Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ESaFaZjxqnNmm2",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDWDSUYB",
      "status":"NEW",
      "narration":"MWK MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"MWK",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_YfQrGYgC5B",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"MWK",
         "mobile_money":{
            "network":"AIRTELMW",
            "msisdn":"2659012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:49:04.563Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ktnCglatt92k8n",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001JYDeWDSUYB",
      "status":"NEW",
      "narration":"ETB MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ETB",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_uodrObhEa5",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ETB",
         "mobile_money":{
            "network":"ETBAMOLE",
            "msisdn":"2519012345678"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T18:51:36.235Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_V5zoB57shPwgac",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001OEDeWDSUYB",
      "status":"NEW",
      "narration":"UGX MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"UGX",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_yJBzZTFEnj",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"UGX",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2569012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T12:59:15.403332030Z"
   }
}
```

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_ejDNIQngjLzUTx",
      "type":"mobile_money",
      "action":"instant",
      "reference":"REF-001O9EDeWDSUYB",
      "status":"NEW",
      "narration":"ZMW MOMO TRANSFER EXAMPLE",
      "source_currency":"NGN",
      "destination_currency":"ZMW",
      "amount":{
         "value":1000,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"mobile_money",
         "id":"rcm_1aaTfsip3I",
         "name":{
            "first":"John",
            "last":"Doe"
         },
         "currency":"ZMW",
         "mobile_money":{
            "network":"MPS",
            "msisdn":"2609012345678"
         }
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-12T13:02:53.774008555Z"
   }
}
```

The`data.status` field in the response will always return `NEW` upon initiating a transfer. This indicates that the transfer has been **successfully initiated**, but **not yet completed**. To determine the final status, you must verify the payout.

There are three ways to verify the final status of a mobile money transfer:

**Webhooks (Recommended):**  
Enable **webhooks** on your Flutterwave dashboard to receive automatic transfer status updates.  
When the transfer completes (or fails), Flutterwave will send a POST request to your configured webhook URL with the transfer details.

```json
{
   "webhook_id":"wbk_emXAIzd4Dd7495SG3NOX",
   "timestamp":1749071772784,
   "type":"transfer.disburse",
   "data":{
      "id":"trf_Fj62qmZOhSneRu",
      "type":"MOBILE_MONEY",
      "source_currency":"NGN",
      "destination_currency":"KES",
      "amount":1000,
      "reference":"REF-001GVSDVDSU2Yhgu",
      "status":"SUCCESSFUL",
      "mobile_money":{
         "network":"Mpesa",
         "country":null,
         "msisdn":"2549012345678"
      },
      "fee":{
         "currency":"KES",
         "value":10
      },
      "debit_information":{
         "currency":"KES",
         "actual_debit_amount":1000,
         "rate_used":0.00123,
         "vat":75
      },
      "payment_information":{
         "proof":"815423162782592573350591343763"
      },
      "meta":{}
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

```json
curl --request GET \
--url 'https://developersandbox-api.flutterwave.com/transfers/id' \
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
        "id": "trf_Hu3QERCeuWk8",
        "type": "mobile_money",
        "reference": "4dc065cc-08a3-4158-9f9b-e4e2f79120e7",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "NGN",
        "destination_currency": "RWF",
        "amount": {
            "value": 1000,
            "applies_to": "source_currency"
        },
        "callback_url": "https://www.flutterwave.com",
        "recipient": {
            "type": "mobile_money",
            "name": {
                "first": "Jane",
                "middle": "The",
                "last": "Janet"
            },
            "mobile_money": {
                "network": "MPS",
                "msisdn": "9012345678"
            }
        },
        "meta": {},
        "created_datetime": "2024-11-21T08:52:37.845Z"
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
        "id": "trf_Hu3QERCeuWk8",
        "type": "mobile_money",
        "reference": "4dc065cc-08a3-4158-9f9b-e4e2f79120e7",
        "status": "NEW",
        "narration": "Testing transfers",
        "source_currency": "NGN",
        "destination_currency": "RWF",
        "amount": {
            "value": 1000,
            "applies_to": "source_currency"
        },
        "callback_url": "https://www.flutterwave.com",
        "recipient": {
            "type": "mobile_money",
            "name": {
                "first": "Jane",
                "middle": "The",
                "last": "Janet"
            },
            "mobile_money": {
                "network": "MPS",
                "msisdn": "9012345678"
            }
        },
        "meta": {},
        "created_datetime": "2024-11-21T08:52:37.845Z"
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
