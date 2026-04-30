---
title: "OPay"
source: "https://developer.flutterwave.com/docs/opay#"
canonical_url: "https://developer.flutterwave.com/docs/opay"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:33:21.061Z"
content_hash: "f749f22f4a50ff58249cc6d80ca2a5b3b6e813f25c60ec8bd5089d5849461f2b"
menu_path: ["OPay"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/ussd/index.md", "title": "USSD"}
nav_next: {"path": "flutterwave/docs/introduction-3/index.md", "title": "Introduction"}
---

The payment with OPay provides a seamless way to accept payments from customers with OPay wallets. Customers can securely authorize transactions directly from their OPay wallets, and funds are deposited into your Flutterwave account.

Whether you're a merchant expanding your payment options or an OPay customer seeking convenience and security, this method simplifies the overall payment experience.

> ## 🚧
> 
> Feature Availability
> 
> This payment method is only available for **NGN** (Nigerian Naira) transactions.

Before you begin, ensure the following prerequisites are met:

1.  Read the [introduction section](../introduction-1/index.md) of this documentation.
2.  Retrieve your API keys from the [Flutterwave dashboard](https://app.flutterwave.com/).

> ## 👍
> 
> Customer Experience Tip
> 
> OPay customers must **log into their wallets** to authorize payments. Inform users in-app when they select this payment method to avoid confusion.

When a customer chooses OPay, they are redirected to the OPay platform to log in and authorize the transaction.

![](https://files.readme.io/61ac8412e0afa95234b4aac419e4d9cab59921804ce82837551e3e44934d2ecc-opay.png)

After authorization, the customer's wallet is debited, and Flutterwave sends a **webhook notification** to your server confirming the successful transaction.

To collect payments using OPay, follow these key steps:

1.  **Initiate Transaction**: Collect the customer’s details and define the transaction parameters (`amount`, `currency`, `tx_ref`, etc.).
2.  **Redirect to OPay**: Send the customer to the OPay authorization page to log in and complete the transaction.
3.  **Verify Payment**: After receiving the webhook or polling the transaction endpoint, confirm:
    1.  status = "successful"
    2.  Correct amount
    3.  Matching customer\_id
    4.  Valid transaction\_id

Only provide value after successful verification.

> ## 🚧
> 
> Integration Method
> 
> This guide follows the general integration flow. Please refer to the [orchestrator flow](https://developer.flutterwave.com/v4.0/docs/payment-orchestrator-flow) for the alternative integration method.

To create a new customer, send a request to the [create customer endpoint](https://developer.flutterwave.com/v4.0/reference/customers_create) with relevant fields such as `name`, `email`, `phone`, and `address`.

While only the email field is required, we recommend collecting as much customer information as possible to support robust transaction records and future payments.

To retrieve existing customer details, use the [retrieve customer endpoint](https://developer.flutterwave.com/v4.0/reference/customers_get). This is useful when initiating payments for returning users.

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
   "status":"success",
   "message":"Customer created",
   "data":{
      "id":"cus_dc0FUyBpd0",
      "address":{
         "city":"Shirley",
         "country":"US",
         "line1":"175 E Parkview Dr",
         "line2":"",
         "postal_code":"11967",
         "state":"New York"
      },
      "email":"Johndoe@example.com",
      "name":{
         "first":"John",
         "middle":"Agba",
         "last":"Doe"
      },
      "phone":{
         "country_code":"1",
         "number":"6313958745"
      },
      "meta":{
         
      },
      "created_datetime":"2024-12-25T20:16:38.246410457Z"
   }
}
```

To create an OPay payment method, send a request to the [create payment method endpoint](https://developer.flutterwave.com/v4.0/reference/payment_methods_post) and set the `type` to `opay`.

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

You'll see a response similar to this:

```json
{
  "status": "success",
  "message": "Payment method created",
  "data": {
    "type": "opay",
    "opay": {},
    "id": "pmd_uF9ADr9LvH",
    "meta": {},
    "created_datetime": "2024-12-26T14:38:25.179075400Z"
  }
}
```

To initiate an OPay charge, send a request to the [create charge endpoint](https://developer.flutterwave.com/v4.0/reference/charges_post) with the following parameters:

-   `customer_id`: The ID returned from Step 1 (customer creation).
-   `payment_method_id`: The ID returned from step 2 (payment method creation).
-   Transaction details including: `amount`, `currency`, and a unique `reference` for the transaction.

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "currency":"NGN",
   "customer_id":"cus_dc0FUyBpd0",
   "payment_method_id":"pmd_uF9ADr9LvH",
   "amount":200,
   "reference":"ex61m23j6a3y0k34o9ilrri"
}'
```

You'll get a response similar to this:

```json
{
   "status":"success",
   "message":"Charge created",
   "data":{
      "id":"chg_nONgeAGY97",
      "amount":200,
      "fees":[
         {
            "type":"vat",
            "amount":0
         },
         {
            "type":"app",
            "amount":0
         },
         {
            "type":"merchant",
            "amount":0
         },
         {
            "type":"stamp_duty",
            "amount":0
         }
      ],
      "currency":"NGN",
      "customer_id":"cus_dc0FUyBpd0",
      "settled":false,
      "settlement_id":[],
      "meta":{},
      "next_action":{
         "type":"redirect_url",
         "redirect_url":{
            "url":"https://developer-sandbox-ui-sit.flutterwave.cloud/redirects?opay&token=eyJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJZCI6ImNiYThhMTkwLTE2OGUtNGNmZS05NmY5LTE2NDZhYjFhOWNkYiIsImNoYXJnZUlkIjoiY2hnX25PTmdlQUdZOTciLCJzdWIiOiJjYmE4YTE5MC0xNjhlLTRjZmUtOTZmOS0xNjQ2YWIxYTljZGIiLCJpYXQiOjE3MzgzMTc3MTAsImV4cCI6MTczODMxODAxMH0.QgLoZYfNhHJOJJvOsLA9eLoxOjGF0qnuehPMgMP4zD4"
         }
      },
      "payment_method_details":{
         "type":"opay",
         "opay":{},
         "id":"pmd_uF9ADr9LvH",
         "meta":{},
         "created_datetime":"2024-12-26T14:38:25.179Z"
      },
      "reference":"ex61m23j6a3y0k34o9ilrri",
      "status":"pending",
      "processor_response":{
         "type":"pending",
         "code":"02"
      },
      "created_datetime":"2025-01-31T10:01:50.209460744Z"
   }
}
```

The response from the charge initiation contains the `next_action` object with a redirect URL. This URL routes the customer to the OPay interface to authorise and complete the payment.

```json
{
   "status":"success",
   "message":"Charge created",
   "data":{
      "id":"chg_nONgeAGY97",
      "amount":200,
      "fees":[
         {
            "type":"vat",
            "amount":0
         },
         {
            "type":"app",
            "amount":0
         },
         {
            "type":"merchant",
            "amount":0
         },
         {
            "type":"stamp_duty",
            "amount":0
         }
      ],
      "currency":"NGN",
      "customer_id":"cus_dc0FUyBpd0",
      "settled":false,
      "settlement_id":[],
      "meta":{},
      "next_action":{
         "type":"redirect_url",
         "redirect_url":{
            "url":"https://developer-sandbox-ui-sit.flutterwave.cloud/redirects?opay&token=eyJhbGciOiJIUzI1NiJ9.eyJjbGllbnRJZCI6ImNiYThhMTkwLTE2OGUtNGNmZS05NmY5LTE2NDZhYjFhOWNkYiIsImNoYXJnZUlkIjoiY2hnX25PTmdlQUdZOTciLCJzdWIiOiJjYmE4YTE5MC0xNjhlLTRjZmUtOTZmOS0xNjQ2YWIxYTljZGIiLCJpYXQiOjE3MzgzMTc3MTAsImV4cCI6MTczODMxODAxMH0.QgLoZYfNhHJOJJvOsLA9eLoxOjGF0qnuehPMgMP4zD4"
         }
      },
      "payment_method_details":{
         "type":"opay",
         "opay":{},
         "id":"pmd_uF9ADr9LvH",
         "meta":{},
         "created_datetime":"2024-12-26T14:38:25.179Z"
      },
      "reference":"ex61m23j6a3y0k34o9ilrri",
      "status":"pending",
      "processor_response":{
         "type":"pending",
         "code":"02"
      },
      "created_datetime":"2025-01-31T10:01:50.209460744Z"
   }
}
```

![](https://files.readme.io/1749cd80a973284ca71cc3ed76dcf90325151b5982e76ab59e39913a67e10fec-opay.png) ![](https://files.readme.io/28316a74ed2fbe56634ed76c1341b60d67bba654c7c4d02176b9db2291a3df91-opay-2.png)

Flutterwave will then send a **webhook notification** with the final transaction status once the payment is completed and funds are received.

Refer to the next section to learn how to verify the transaction.

Before you provide value to the customer, confirm the transaction's final status and amount. You can verify the transaction information either using webhooks or by retrieving the charge details:

-   **_Webhooks_**: It is important to have webhooks enabled on your Flutterwave dashboard. If you have webhooks enabled, we'll call your webhook URL with the payment details when the transaction is completed or fails. Below is a sample webhook payload;

```json
{
  "webhook_id": "wbk_z8BBd4nvlPxrg0GGTEFw",
  "timestamp": 1738317739798,
  "type": "charge.completed",
  "data": {
    "id": "chg_nONgeAGY97",
    "amount": 200,
    "currency": "NGN",
    "customer": {
      "id": "cus_dc0FUyBpd0",
      "address": {
        "city": "Shirley",
        "country": "US",
        "line1": "175 E Parkview Dr",
        "line2": "",
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
      "created_datetime": "2024-12-25T20:16:38.246Z"
    },
    "description": null,
    "meta": {},
    "payment_method": {
      "type": "opay",
      "opay": {},
      "id": "pmd_uF9ADr9LvH",
      "customer_id": null,
      "meta": {},
      "device_fingerprint": null,
      "client_ip": null,
      "created_datetime": "2024-12-26T14:38:25.179Z"
    },
    "redirect_url": null,
    "reference": "ex61m23j6a3y0k34o9ilrri",
    "status": "succeeded",
    "processor_response": {
      "type": "approved",
      "code": "00"
    },
    "created_datetime": "2025-01-31T10:01:50.209Z"
  }
}
```

-   **_Retrieve the Charge_**: You can manually check the status of a charge by calling the [retrieve a charge endpoint](https://developer.flutterwave.com/v4.0/reference/charges_get) using the charge ID, which is returned in the `data.id` field of the response after successfully initiating a charge.

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
    "id": "chg_LgTqLXDGXq",
    "amount": 200,
    "currency": "NGN",
    "customer_id": "cus_dc0FUyBpd0",
    "settled": false,
    "settlement_id": [],
    "meta": {},
    "payment_method_details": {
      "type": "opay",
      "opay": {},
      "id": "pmd_uF9ADr9LvH",
      "meta": {},
      "created_datetime": "2024-12-26T14:38:25.179Z"
    },
    "reference": "ex61m23j6a3y0kk4o8ilrri",
    "status": "succeeded",
    "processor_response": {
      "type": "approved",
      "code": "00"
    },
    "created_datetime": "2024-12-27T08:52:18.128Z"
  }
}
```

Testing your integration requires no extra configuration or special data. Initiate the OPay charge, and we'll return a redirect link to our mock page, where you can simulate both successful and failed customer attempts.

![](https://files.readme.io/e1be24ccb1c071dc0432602f624dfd9154e560c6ffa88c346b8d0816a72fd8a6-Screenshot_2025-02-25_at_14.28.25.png) ![](https://files.readme.io/a80f441fef117be69c669bedd5318ed9b98418dedbe6907ddb16d1484652945c-Screenshot_2025-02-25_at_14.28.41.png) ![](https://files.readme.io/50ac57217b99b11bb46fa8d78e1915f7556d44384225f7718d89f9844df5601e-Screenshot_2025-02-25_at_14.31.02.png)

That’s it! You’ve successfully integrated the OPay payment method. It doesn't end there, there is more:

-   Learn about [settlements](https://developer.flutterwave.com/v4.0/docs/settlements) of successful payments into your Flutterwave balance.
-   For cases where [refunds](https://developer.flutterwave.com/v4.0/docs/refunds) are necessary, see the refunds guide for more information on how to process transaction refunds.

Updated 7 months ago

* * *
