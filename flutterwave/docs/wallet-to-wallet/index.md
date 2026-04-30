---
title: "Wallet-to-Wallet"
source: "https://developer.flutterwave.com/docs/wallet-to-wallet#"
canonical_url: "https://developer.flutterwave.com/docs/wallet-to-wallet"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:50.653Z"
content_hash: "5aa63b641618d697cffcefda899739fc908c0501f6e4e0f459b7d0d13fb3d462"
menu_path: ["Wallet-to-Wallet"]
section_path: []
tab_variants: ["200 OK","400 Bad Request"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/mobile-money-1/index.md", "title": "Mobile Money Transfers"}
nav_next: {"path": "flutterwave/docs/settlements/index.md", "title": "Settlements"}
---

Flutterwave enables you to transfer funds directly from your available balance to another Flutterwave merchant using **wallet-to-wallet** transfers. This feature allows you to make payouts from your preferred currency balance to the recipient’s balance in their chosen currency, supporting seamless cross-currency transactions within the Flutterwave ecosystem.

-   Whitelist your IP addresses.
-   Ensure your balance has sufficient funds. You can fund your balance by one of the following methods:
    -   Directly funding via [collections](../introduction-1/index.md).
    -   Indirect funding by converting funds from a different currency balance (i.e., wallet-to-wallet transfers).

Every successful wallet-to-wallet transfer follows a two-step process:

-   Initiate Payout
-   Verify Payout

> ## 🚧
> 
> Integration Method
> 
> This guide follows the direct transfer flow for demonstration. Please refer to the [general transfer flow](https://developer.flutterwave.com/v4.0/docs/general-transfer-flow) for the alternative integration method.

To initiate a wallet-to-wallet transfer, send a request to the [create transfer endpoint](https://developer.flutterwave.com/reference/transfers_post) with the following required parameters:

-   `action`: Specifies how the transfer should be processed. Accepted values are `instant`, `deferred`, or `scheduled`.
-   `type`: Specifies the type of transfer. Use `"wallet"` for wallet-to-wallet transfers.
-   `payment_instruction`: An object containing details of the payment, including:
    -   `amount`
    -   `currency` (`source_currency` and `destination_currency`)
    -   Recipient details, such as the payment provider, which is always `flutterwave` and the Flutterwave merchant identifier.

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
      "value": 100
    },
    "recipient": {
      "wallet": {
        "provider": "flutterwave",
        "identifier": "00118468"
      }
    },
    "destination_currency": "NGN"
  },
  "type": "wallet",
  "narration": "TESTING WALLET TRANSFERS",
  "reference": "KYERIREYI-JGSJSJGSDJ"
}'
```

> ## 🚧
> 
> Handling Identifier
> 
> The `identifier` field represents the recipient's merchant ID linked to their Flutterwave account i.e. their MID.

You can also initiate **scheduled** or **deferred** wallet-to-wallet transfers by setting the `action` field to `scheduled` or `deferred`.

For **scheduled** transfers, include the `disburse_option` object in the request. This object defines when the transfer should be executed and must contain:

-   `date_time`: The exact date and time to trigger the transfer.
-   `timezone`: The timezone for the scheduled time.

Refer to the [transfer overview](../introduction-3/index.md#full-example) for a complete walkthrough on creating and managing these transfer types.

> ## 💱
> 
> Handling International Transfers
> 
> To manage cross-currency payouts, refer to the [managing currency](../direct-transfer-flow/index.md#cross-currency-transfers) section.

When you successfully initiate a wallet-to-wallet transfer, the API returns a response similar to this:

```json
{
   "status":"success",
   "message":"Transfer created",
   "data":{
      "id":"trf_KDLtJacafRur4K",
      "type":"wallet",
      "action":"instant",
      "reference":"KYERIREYI-JGSJSJGSDJ",
      "status":"NEW",
      "narration":"TESTING WALLET TRANSFERS",
      "source_currency":"NGN",
      "destination_currency":"NGN",
      "amount":{
         "value":100,
         "applies_to":"destination_currency"
      },
      "recipient":{
         "type":"wallet",
         "id":"rcw_Gf547Peqq5",
         "name":{
            "first":"Ajadi",
            "last":"Trailers & Co."
         },
         "currency":"NGN",
         "wallet":{
            "provider":"flutterwave",
            "identifier":"00118468"
         }
      },
      "meta":{},
      "created_datetime":"2025-06-04T21:47:16.417Z"
   }
}
```

The`data.status` field in the response will always return `NEW` upon initiating a transfer. This indicates that the transfer has been **successfully initiated**, but **not yet completed**. To determine the final status, you must verify the payout.

There are three ways to verify the final status of a wallet-to-wallet transfer:

**Webhooks (Recommended):**  
Enable **webhooks** on your Flutterwave dashboard to receive automatic transfer status updates.  
When the transfer completes (or fails), Flutterwave will send a POST request to your configured webhook URL with the transfer details.

```json
{
   "webhook_id":"wbk_T1n3neXA7Wn52mnOIDBI",
   "timestamp":1749073636445,
   "type":"transfer.disburse",
   "data":{
      "id":"trf_KDLtJacafRur4K",
      "type":"WALLET",
      "source_currency":"NGN",
      "destination_currency":"NGN",
      "amount":100,
      "reference":"KYERIREYI-JGSJSJGSDJii",
      "status":"SUCCESSFUL",
      "wallet":{
         "provider":"flutterwave",
         "identifier":"00118468"
      },
      "fee":{
         "currency":"NGN",
         "value":1
      },
      "debit_information":{
         "currency":"NGN",
         "actual_debit_amount":100,
         "rate_used":0.00123,
         "vat":7.5
      },
      "payment_information":{
         "proof":"489483145598277415954270427727"
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
    "id": "trf_TovqwXP5McNbwI",
    "type": "wallet",
    "action": "instant",
    "reference": "KYERIREYI-JGSJSJGSDJ",
    "status": "NEW",
    "narration": "TESTING WALLET TRANSFERS",
    "source_currency": "NGN",
    "destination_currency": "NGN",
    "amount": {
      "value": 100,
      "applies_to": "destination_currency"
    },
    "recipient": {
      "type": "wallet",
      "currency": "NGN",
      "wallet": {
        "provider": "flutterwave",
        "identifier": "00118468"
      },
      "id": "rcw_MZGa8LPctK"
    },
    "meta": {},
    "created_datetime": "2024-12-11T08:57:49.040Z"
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
    "id": "trf_TovqwXP5McNbwI",
    "type": "wallet",
    "action": "instant",
    "reference": "KYERIREYI-JGSJSJGSDJ",
    "status": "NEW",
    "narration": "TESTING WALLET TRANSFERS",
    "source_currency": "NGN",
    "destination_currency": "NGN",
    "amount": {
      "value": 100,
      "applies_to": "destination_currency"
    },
    "recipient": {
      "type": "wallet",
      "currency": "NGN",
      "wallet": {
        "provider": "flutterwave",
        "identifier": "00118468"
      },
      "id": "rcw_MZGa8LPctK"
    },
    "meta": {},
    "created_datetime": "2024-12-11T08:57:49.040Z"
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

The wallet-to-wallet transfer feature also supports transferring funds between different currency balances within the **same Flutterwave account**, known as **intra-wallet** transfers. This allows for seamless movement of funds across multiple currency balances tied to a single account.

The request format for an intra-wallet transfer is similar to a standard wallet-to-wallet transfer, with a few key differences:

-   Set your own Flutterwave merchant ID as the `identifier`.
-   Specify:
    -   `source_currency`: The currency balance to debit.
    -   `destination_currency`: The target currency balance to credit.

This functionality is especially useful for internal FX conversion or operational fund rebalancing.

Check out the [testing section](../direct-transfer-flow/index.md#testing-transfers) to learn how to simulate various transfer scenarios.

Updated 7 months ago

* * *
