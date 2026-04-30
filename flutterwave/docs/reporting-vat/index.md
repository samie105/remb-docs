---
title: "Reporting VAT"
source: "https://developer.flutterwave.com/docs/reporting-vat"
canonical_url: "https://developer.flutterwave.com/docs/reporting-vat"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:31:43.244Z"
content_hash: "cee5be99c6ed8f150bb3d5b36faae015301f28a1c49cc2e26771fa065d18b09b"
menu_path: ["Reporting VAT"]
section_path: []
tab_variants: ["Sample (General flow)","Sample (Orchestrator flow)"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/chargebacks-1/index.md", "title": "Chargebacks"}
nav_next: {"path": "flutterwave/docs/fintechs/index.md", "title": "Fintechs"}
---

## Reporting VAT

Understanding how to report tax information (VAT)

> ## 📘
> 
> This applies to transactions of NGN Merchants only.

Flutterwave allows you to report tax information (VAT) for every transaction your customer makes, irrespective of the payment type. This helps your reconciliation and transaction audit. You'll need to calculate the value of the VAT (7.5% of the transaction amount, excluding processing fees) and pass `merchant_vat_amount` into your request.

#### Sample (General flow)

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "reference": "cedfa85a-a803-4a06-a586-0f81fb9b9f22",
   "currency": "NGN",
   "customer_id": "cus_IpH7CKCUtD",
   "payment_method_id": "pmd_wlVhaYmkl2",
   "merchant_vat_amount": 7.5,
   "redirect_url":"https://custom-redirect.com",
   "amount": 1234.56,
   "meta":{
     "person_name": "King James",
     "role": "Developer"
   }
 }'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--header 'X-Scenario-Key: scenario:auth_pin&issuer:approved' \
--data '{
    "amount": 1234.56,
    "currency": "NGN",
    "reference": "YOUR_EXAMPLE_REFERENCE",
    "merchant_vat_amount": 7.5,
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
            "country": "NG",
            "city": "Lagos Island",
            "state": "Lagos",
            "postal_code": "101223",
            "line1": "2C Coker Road"
        },
        "phone": {
            "country_code": "234",
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

#### Sample (Orchestrator flow)

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--data '{
   "reference": "cedfa85a-a803-4a06-a586-0f81fb9b9f22",
   "currency": "NGN",
   "customer_id": "cus_IpH7CKCUtD",
   "payment_method_id": "pmd_wlVhaYmkl2",
   "merchant_vat_amount": 7.5,
   "redirect_url":"https://custom-redirect.com",
   "amount": 1234.56,
   "meta":{
     "person_name": "King James",
     "role": "Developer"
   }
 }'
```

```curl
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/orchestration/direct-charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Idempotency-Key: {{YOUR_UNIQUE_INDEMPOTENCY_KEY}}' \
--header 'X-Scenario-Key: scenario:auth_pin&issuer:approved' \
--data '{
    "amount": 1234.56,
    "currency": "NGN",
    "reference": "YOUR_EXAMPLE_REFERENCE",
    "merchant_vat_amount": 7.5,
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
            "country": "NG",
            "city": "Lagos Island",
            "state": "Lagos",
            "postal_code": "101223",
            "line1": "2C Coker Road"
        },
        "phone": {
            "country_code": "234",
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

After sending the VAT information, we report this to the Federal Internal Revenue Service. You'll need to ensure that the correct value is passed for recording-keeping and accurate auditing with the FIRS.

Updated 3 months ago

* * *
