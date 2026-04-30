---
title: "Settlements"
source: "https://developer.flutterwave.com/docs/settlements#"
canonical_url: "https://developer.flutterwave.com/docs/settlements"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:52.904Z"
content_hash: "bff001fc1eeae90832d1d45e9a63b0e4f7147668f5236f1ec1896e983f1574fa"
menu_path: ["Settlements"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/wallet-to-wallet/index.md", "title": "Wallet-to-Wallet"}
nav_next: {"path": "flutterwave/docs/refunds/index.md", "title": "Refunds"}
---

A transaction is not considered complete until the funds are delivered to your account. This process is called **settlement**.

After a customer makes a payment using their preferred method, Flutterwave holds the funds for a short period before settling them into your account. The **settlement timeline** [varies by payment method](https://flutterwave.com/ng/support/payments/settlement-schedule).

Before settlement is completed, the collected funds appear as your collection balance on the dashboard. Once settled, funds are transferred to either:

-   Your linked **bank account**, or
-   Your **Flutterwave for Business (F4B) wallet** (payout balance).

![](https://files.readme.io/f386b03576c02ed56291a036cb4c2c946c5d69ca594cd8db1331a404aa0c776c-7dc3ad86e77294daa965798c6f98b7675c9f0a0bef6585ebfe6eecf2565630da-image.png)

Settlements are supported for all payment methods.

Successful transactions can either be settled successfully or flagged:

1.  **Successful Settlements**: Funds are settled to your bank account or wallet as expected.
2.  **Flagged Settlements**: Funds are withheld due to compliance or other issues. You can view the settlement details to understand the reason, and should contact [Flutterwave Support](https://flutterwave.com/ng/support/submit-request) for assistance.

  

> ## 🚧
> 
> Live Transactions Only
> 
> Only transactions made in **live/production** mode are eligible for settlement. Ensure that your account has been approved for settlement.

1.  **Add your Preferred Settlement Account**: Provide your bank account details or configure [your F4B wallet](https://flutterwave.com/ng/support/payments/settlement-in-different-currencies) in the [dashboard settings](https://app.flutterwave.com/).
2.  **Meet the Minimum Settlement Threshold**: Settlements are processed once your cumulative balance exceeds the [minimum threshold](https://flutterwave.com/ng/support/payments/minimum-settlement-threshold). If your balance is below this amount, Flutterwave will batch your funds, which may result in delayed settlement.

You can access and manage all settlement data in two ways:

-   **Dashboard**: View your settlement history, current balances, and associated transactions.
-   **API**: Use the [list settlement endpoint](https://developer.flutterwave.com/v4.0/reference/settlement_list) to programmatically retrieve settlement details.

![](https://files.readme.io/bf51aeceead548d3ec73537330300ca4408fdd693d5eb2e05de0568234538565-752d41338670001a2b7fe5ce848b063c90137eda0b5c237e5460530dc5f6ca61-image.png)

A settlement report contains a list of transactions and other details such as:

1.  `status`: The current status of the settlement (e.g., SUCCESSFUL, PENDING).
2.  `destination`: Where the funds were sent (e.g., bank account or F4B wallet).
3.  Settlement Timestamp: The exact time the settlement was processed.
4.  `type`: Indicates whether the settlement was local or international.

Settlement reconciliation allows you to track payments, maintain accurate financial records, and resolve any discrepancies. It provides greater financial visibility and control over your transaction flows.

To retrieve settlement data, query the [list settlements endpoint](https://developer.flutterwave.com/v4.0/reference/settlement_list).  
Use the following filters to narrow down your results:

-   `page`: Page number of the results.
-   `from`: Start date for the settlement query.
-   `to`: End date for the settlement query.
-   `size`: Number of records to return per page.

```json
curl --request GET \
--url 'https://developersandbox-api.flutterwave.com/settlements?page=1&size=10' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
```

You'll get a response similar to this:

```json
{
  "status": "success",
  "message": "Settlements fetched",
  "meta": {
    "page_info": {
      "total": 10,
      "current_page": 1,
      "total_pages": 1
    }
  },
  "data": [
    {
      "id": "stm_xpNivHNWmP",
      "net_amount": 150,
      "gross_amount": 150,
      "currency": "USD",
      "meta": {},
      "status": "completed",
      "due_datetime": "2024-12-25T22:00:00.011Z",
      "fees": [
        {
          "type": "stamp_duty",
          "amount": 0
        },
        {
          "type": "charge_fee",
          "amount": 0
        }
      ],
      "destination": "wallet",
      "charge_count": "1",
      "created_datetime": "2024-12-25T22:00:00.011Z"
    },
    {
      "id": "stm_xURpuClRd5",
      "net_amount": 200,
      "gross_amount": 200,
      "currency": "NGN",
      "meta": {},
      "status": "completed",
      "due_datetime": "2024-12-27T09:00:00.025Z",
      "fees": [
        {
          "type": "stamp_duty",
          "amount": 0
        },
        {
          "type": "charge_fee",
          "amount": 0
        }
      ],
      "destination": "wallet",
      "charge_count": "1",
      "created_datetime": "2024-12-27T09:00:00.025Z"
    },
    {
      "id": "stm_lRP73jTEUD",
      "net_amount": 150,
      "gross_amount": 150,
      "currency": "NGN",
      "meta": {},
      "status": "completed",
      "due_datetime": "2025-01-21T16:00:00.010Z",
      "fees": [
        {
          "type": "stamp_duty",
          "amount": 0
        },
        {
          "type": "charge_fee",
          "amount": 0
        }
      ],
      "destination": "wallet",
      "charge_count": "1",
      "created_datetime": "2025-01-21T16:00:00.010Z"
    },
    {
      "id": "stm_e80g4BVER5",
      "net_amount": 150,
      "gross_amount": 150,
      "currency": "NGN",
      "meta": {},
      "status": "completed",
      "due_datetime": "2025-01-21T20:00:00.196Z",
      "fees": [
        {
          "type": "stamp_duty",
          "amount": 0
        },
        {
          "type": "charge_fee",
          "amount": 0
        }
      ],
      "destination": "wallet",
      "charge_count": "1",
      "created_datetime": "2025-01-21T20:00:00.196Z"
    },
    {
      "id": "stm_HFk2sqcM1c",
      "net_amount": 200,
      "gross_amount": 200,
      "currency": "NGN",
      "meta": {},
      "status": "completed",
      "due_datetime": "2025-01-31T11:00:00.020Z",
      "fees": [
        {
          "type": "stamp_duty",
          "amount": 0
        },
        {
          "type": "charge_fee",
          "amount": 0
        }
      ],
      "destination": "wallet",
      "charge_count": "1",
      "created_datetime": "2025-01-31T11:00:00.020Z"
    },
    {
      "id": "stm_YQkhQsAZnQ",
      "net_amount": 150,
      "gross_amount": 150,
      "currency": "USD",
      "meta": {},
      "status": "completed",
      "due_datetime": "2025-01-31T11:00:00.048Z",
      "fees": [
        {
          "type": "stamp_duty",
          "amount": 0
        },
        {
          "type": "charge_fee",
          "amount": 0
        }
      ],
      "destination": "wallet",
      "charge_count": "1",
      "created_datetime": "2025-01-31T11:00:00.048Z"
    },
    {
      "id": "stm_Wk38LvV5Hz",
      "net_amount": 150,
      "gross_amount": 150,
      "currency": "NGN",
      "meta": {},
      "status": "completed",
      "due_datetime": "2025-02-05T15:00:00.022Z",
      "fees": [
        {
          "type": "stamp_duty",
          "amount": 0
        },
        {
          "type": "charge_fee",
          "amount": 0
        }
      ],
      "destination": "wallet",
      "charge_count": "1",
      "created_datetime": "2025-02-05T15:00:00.022Z"
    },
    {
      "id": "stm_TIrjYoJE8V",
      "net_amount": 300,
      "gross_amount": 300,
      "currency": "NGN",
      "meta": {},
      "status": "completed",
      "due_datetime": "2025-02-07T10:00:00.034Z",
      "fees": [
        {
          "type": "stamp_duty",
          "amount": 0
        },
        {
          "type": "charge_fee",
          "amount": 0
        }
      ],
      "destination": "wallet",
      "charge_count": "2",
      "created_datetime": "2025-02-07T10:00:00.034Z"
    },
    {
      "id": "stm_tsjRlAMkoN",
      "net_amount": 2000,
      "gross_amount": 2000,
      "currency": "NGN",
      "meta": {},
      "status": "completed",
      "due_datetime": "2025-02-07T11:00:00.137Z",
      "fees": [
        {
          "type": "stamp_duty",
          "amount": 0
        },
        {
          "type": "charge_fee",
          "amount": 0
        }
      ],
      "destination": "wallet",
      "charge_count": "1",
      "created_datetime": "2025-02-07T11:00:00.137Z"
    },
    {
      "id": "stm_JJo3vjtffW",
      "net_amount": 2000,
      "gross_amount": 2000,
      "currency": "NGN",
      "meta": {},
      "status": "completed",
      "due_datetime": "2025-02-07T12:00:00.022Z",
      "fees": [
        {
          "type": "stamp_duty",
          "amount": 0
        },
        {
          "type": "charge_fee",
          "amount": 0
        }
      ],
      "destination": "wallet",
      "charge_count": "1",
      "created_datetime": "2025-02-07T12:00:00.022Z"
    }
  ]
}
```

To retrieve the details of a specific settlement, include the settlement ID in your request.

```json
curl --request GET \
--url 'https://developersandbox-api.flutterwave.com/settlements/id' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
```

You'll get a response similar to this:

```json
{
  "status": "success",
  "message": "Settlement fetched",
  "data": {
    "id": "stm_xpNivHNWmP",
    "net_amount": 150,
    "gross_amount": 150,
    "currency": "USD",
    "meta": {},
    "status": "completed",
    "due_datetime": "2024-12-25T22:00:00.011Z",
    "fees": [
      {
        "type": "stamp_duty",
        "amount": 0
      },
      {
        "type": "charge_fee",
        "amount": 0
      }
    ],
    "destination": "wallet",
    "charge_count": "1",
    "charges": [],
    "created_datetime": "2024-12-25T22:00:00.011Z"
  },
  "meta": {
    "page_info": {
      "total": 1,
      "current_page": 1,
      "total_pages": 0
    }
  }
}
```

Updated 6 months ago

* * *
