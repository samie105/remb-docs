---
title: "Real-time FX conversion"
source: "https://developer.flutterwave.com/docs/real-time-fx-conversion#"
canonical_url: "https://developer.flutterwave.com/docs/real-time-fx-conversion"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:34:21.144Z"
content_hash: "7cf4479d6134fb53a611e275f3152fcb7ca92d66aeb501983d9ad97c420470ec"
menu_path: ["Real-time FX conversion"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/managing-instant-loan-disbursements/index.md", "title": "Loan disbursements"}
nav_next: {"path": "flutterwave/docs/quickstart/index.md", "title": "Charging a Card"}
---

Before we dive into using the rate conversion and payout service feature, let’s consider a scenario:

Imagine you’ve been tasked, as a developer, with building a remittance service that helps customers send money from the United States to Nigeria. Your goal is to ensure accurate and real-time currency conversion so recipients always receive the correct amount in Nigerian Naira (NGN).

Here’s how to use the Rate Conversion and Payout API for remittance:

1.  **Fetch Live Exchange Rate** : Use the rate conversion API to retrieve real-time exchange rates between USD and NGN. For example, if a customer wants to send 300 USD to their family in Nigeria, you’ll do the following:

```json
curl --request POST  
     --url 'https://developersandbox-api.flutterwave.com/transfers/rates'  
     --header 'accept: application/json'  
     --header 'content-type: application/json'  
     --data '  
{  
  "source": {
    "currency": "NGN"
  },
  "destination": {
    "currency": "USD",
    "amount": 300
  }  
}  
'
```

You’ll get a response similar to this:

```json
{
    "status": "success",
    "message": "Rate created",
    "data": {
        "id": "rex_JtA0MDnO0ITr",
        "rate": "1728.614990",
        "source": {
            "amount": "518584.497070",
            "currency": "NGN"
        },
        "destination": {
            "amount": "300",
            "currency": "USD"
        },
        "created_datetime": "2025-06-25T12:54:25.710Z"
    }
}
```

> ## 🚧
> 
> Querying Rates
> 
> Fetching the live exchange rate is optional. Flutterwave automatically uses real-time rates when you start a transfer. However, we recommend showing users the current rate before they confirm the transfer. This builds trust and avoids surprises.

  

2.  **Get the Bank Code**: To initiate a payout, you need the bank code. Bank codes are unique identifiers that every bank has, and it's required to process the payout.

```json
curl --request GET  
     --url 'https://developersandbox-api.flutterwave.com/banks?country=NG'  
     --header 'X-Trace-Id: {{REPLACE_WITH_UNIQUE_IDENTIFIER}}'  
     --header 'accept: application/json'  
     --header 'authorization: Bearer {{REPLACE_WITH_API_ACCESS_TOKEN}}'
```

You’ll get a response similar to this:

```json
{
  "status": "success",
  "message": "Bank list retrieved successfully",
  "data": [
    {
      "id": "bnk_cYjd92Qk",
      "code": "044",
      "name": "Access Bank"
    }
    .......
  ]
}
```

  

3.  **Verify the Bank Details**: To ensure you’re transferring funds to the right account, use the account look-up endpoint to verify the account.

```json
curl --request POST  
     --url 'https://developersandbox-api.flutterwave.com/banks/account-resolve'  
     --header 'X-Trace-Id: {{REPLACE_WITH_UNIQUE_IDENTIFIER}}'  
     --header 'authorization: Bearer {{REPLACE_WITH_API_ACCESS_TOKEN}}'  
     --header 'content-type: application/json'  
     --data '  
{  
  "account": {  
    "code": "044",  
    "number": "0690000031"  
  },  
  "currency": "NGN"  
}  
'
```

You’ll get a response similar to this:

```json
{
  "status": "success",
  "message": "Bank details retrieved successfully",
  "data": {
    "bank_code": "044",
    "account_number": "0690000031",
    "account_name": "John Doe"
  }
}
```

  

4.  **Create a Payout Request**: Use the transfers endpoint to specify the recipient’s details and the amount to be transferred.

```json
curl --request POST  
     --url 'https://developersandbox-api.flutterwave.com/direct-transfers'  
     --header 'X-Trace-Id: {{REPLACE_WITH_UNIQUE_IDENTIFIER}}'  
     --header 'authorization: Bearer {{REPLACE_WITH_API_ACCESS_TOKEN}}'  
     --header 'content-type: application/json'  
     --data '  
{  
  "action": "instant",  
  "payment_instruction": {  
    "source_currency": "USD",  
    "amount": {  
      "applies_to": "source_currency",  
      "value": 300  
    },  
    "recipient": {  
      "bank": {  
        "account_number": "0690000031",  
        "code": "044"  
      }  
    },  
    "destination_currency": "NGN"  
  },  
  "type": "bank"  
}  
'
```

The key aspects to consider when using the Transfer API are the `action` and the `payment_instruction` parameters.

-   `action`: This defines when Flutterwave processes your transfer request. In your case, you’ve chosen an instant transfer. Alternatively, you can defer the transfer or schedule it for a later time.
-   `payement_instruction` defines how Flutterwave should handle your transfer request. In your case, you’ve instructed Flutterwave to pay your customer in NGN (`destination_currency`) from your USD Flutterwave account (`source_currency`). Flutterwave retrieves the current exchange rate and transfers the equivalent amount in Naira to the recipient’s account.

You’ll get a response similar to this:

```json
{
    "status": "success",
    "message": "Transfer created",
    "data": {
        "id": "trf_KfuyB4YprRt0RD",
        "type": "bank",
        "action": "instant",
        "reference": "3d8e2e08-d4bd-4f8c-951a-d68e98eea80b",
        "status": "NEW",
        "source_currency": "USD",
        "destination_currency": "NGN",
        "amount": {
            "value": 300,
            "applies_to": "source_currency"
        },
        "recipient": {
            "type": "bank",
            "name": {
                "first": "John Doe",
                "last": ""
            },
            "currency": "NGN",
            "bank": {
                "account_number": "0690000031",
                "code": "044"
            },
            "id": "rcb_qcwLZGHj7l"
        },
        "meta": {},
        "created_datetime": "2025-01-21T09:55:59.157510874Z"
    }
}
```

  

5.  **Monitor the Transfer Status**: If you need to check the status of a transfer, you can use any of the following methods:
    -   Retrieve Transfer Endpoint: Query the endpoint directly to get the status of the transfer.
    -   Webhook (Recommended): Set up a webhook to receive real-time updates on the transfer status.
    -   Callback URL: Use a callback URL, if available, to handle status updates.

To learn more about implementing the rate conversion and transfer APIs and other edge cases you can handle with it, check out the following resources:

-   [Transfer API documentation](https://developer.flutterwave.com/reference/direct_transfers_post).
-   [Rate conversion documentation](https://developer.flutterwave.com/reference/transfer_rates_post).

Updated 7 months ago

* * *
