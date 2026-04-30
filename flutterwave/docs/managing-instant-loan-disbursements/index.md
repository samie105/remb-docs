---
title: "Loan disbursements"
source: "https://developer.flutterwave.com/docs/managing-instant-loan-disbursements#"
canonical_url: "https://developer.flutterwave.com/docs/managing-instant-loan-disbursements"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:34:18.916Z"
content_hash: "86d0de79ad9daf968832c040ab677c925b4dd1a43b5d7c710f2350a021a92b70"
menu_path: ["Loan disbursements"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/telecommunications/index.md", "title": "Telecommunications"}
nav_next: {"path": "flutterwave/docs/real-time-fx-conversion/index.md", "title": "Real-time FX conversion"}
---

## Loan disbursements

Learn how to disburse loan payments to customers using our Payout and Bank APIs.

This guide will cover the following:

1.  Transfer APIs: Managing instant loan disbursements for customers.
2.  Collection APIs

Before we dive into using the transfer feature, let’s consider a scenario:

Imagine you’re a developer at a fintech company providing instant loans. Once a customer’s loan application is approved, the next step is to disburse the funds immediately to their bank account to meet their expectations for speed and reliability. The payment terms agreed with the customers include:

-   Disbursement Amount: NGN 1,000,000.
-   Bank Name: Access Bank.
-   Account Name: Aduke Enterprise Limited.
-   Account Number: 0690000031

With Flutterwave’s Transfer API, you can seamlessly automate this process. The API ensures that funds are sent instantly to the customer’s account, eliminating delays and creating a smooth, efficient experience.

Here’s how you use the Transfer API to disburse funds:

1.  **Get the Bank Code**: To initiate a payout, you need the bank code. Bank codes are unique identifiers that every bank has, and it's required to process the payout.

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

  

2.  **Verify the Bank Details**: To ensure you’re transferring funds to the right account, use the account look-up endpoint to verify the account.

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
    "account_name": "Aduke Enterprise Limited"
  }
}
```

  

3.  **Create a Payout Request**: Use the transfers endpoint to specify the recipient’s details and the amount to be transferred.

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
    "source_currency": "NGN",  
    "amount": {  
      "applies_to": "source_currency",  
      "value": 1000000  
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
-   `payement_instruction` defines how Flutterwave should handle your transfer request. In your case, you’ve instructed Flutterwave to pay your customer in NGN (`destination_currency`) from your NGN Flutterwave account (`source_currency`). You can also process international transfers by specifying the currency while Flutterwave manages the conversion and other operational overheads.

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
        "source_currency": "NGN",
        "destination_currency": "NGN",
        "amount": {
            "value": 1000000,
            "applies_to": "destination_currency"
        },
        "recipient": {
            "type": "bank",
            "name": {
                "first": "Aduke Enterprise Limited",
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

4.  Monitor the Transfer Status: If you need to check the status of a transfer, you can use any of the following methods:
    -   **Retrieve Transfer Endpoint**: Query the endpoint directly to get the status of the transfer.
    -   **Webhook** (Recommended): Set up a webhook to receive real-time updates on the transfer status.
    -   **Callback URL**: Use a callback URL, if available, to handle status updates.

To learn more about implementing the transfer API and other edge cases you can handle with it, check out the following resources:

-   [Transfer API documentation](https://developer.flutterwave.com/reference/direct_transfers_post).
-   Authentication with OAuth2.0.
-   Bank API documentation.

Updated 7 months ago

* * *
