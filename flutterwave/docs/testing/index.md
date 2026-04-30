---
title: "Testing"
source: "https://developer.flutterwave.com/docs/testing#"
canonical_url: "https://developer.flutterwave.com/docs/testing"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:32:51.422Z"
content_hash: "637db3818508c6e34672731ad3f013f6c127fc82794349fc2fc033a8b2aa16b4"
menu_path: ["Testing"]
section_path: []
content_language: "de"
nav_prev: {"path": "flutterwave/docs/idempotency/index.md", "title": "Idempotency"}
nav_next: {"path": "flutterwave/docs/best-practices/index.md", "title": "Best Practices"}
---

## Testing

Test your API integration with custom data.

> ## ❗️
> 
> Data Retention
> 
> We archive your test data after 30 days. Once test data is archived, it can't be accessed again.

Use the `X-Scenario-Key` header to simulate different test scenarios in the sandbox environment. Check out the sections below to see supported scenario keys.

To test card transactions, pass a scenario key in this format:  
`scenario:<value>&issuer:<value>`

-   `scenario` defines the authentication flow you want to test.
-   `issuer` defines the processor response to simulate.

> ## 🚧
> 
> Default Behaviour
> 
> If you omit the `X-Scenario-Key` header, all mock card transactions defaults to a `noauth` flow.

```json
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Scenario-Key: scenario:auth_pin&issuer:approved' \
--data '{
    "amount": 1000,
    "currency": "NGN",
    "reference": "94ee715b-9c4b-4700-811b-c93a6f7ce07b",
    "customer_id": "cus_c44nro7QZe",
    "payment_method_id": "pmd_kKhbTyKhl4",
    "redirect_url": "https://example.com",
    "authorization": {
        "type": "pin",
        "pin": {
            "nonce": "WQC6lrkhRM5B",
            "encrypted_pin": "JQuCpsT0JlP3F0LVeaUvGkb/6rM="
        }
    },
    "recurring": false
}'
```

`scenario:<scenario_value>`

| Scenario | Meaning |
| --- | --- |
| `auth_pin` | Mock PIN authentication. Prompts the customer to enter their PIN and OTP. |
| `auth_pin_3ds` | Mock a failover from `PIN` to `3DS`. The customer first enters their PIN, then gets redirected to the 3DS flow. |
| `auth_3ds` | Mock a 3DS authentication. Returns a redirect URL to send the customer to their bank for charge authorization. |
| `auth_avs` | Mock the `noauth` (AVS) flow. Prompts the customer to enter their billing address to complete the payment. |

`issuer:<issuer_value>`

You can simulate different issuer responses for each authentication model. These represent actual responses from providers after payment processing. Use these to test failure, success, and edge cases.

We recommend that you test as much as you can to build high reliability for your application. Here are the available issuer response values:

-   `already_reversed`
-   `approved`
-   `blocked_first_use`
-   `cannot_complete_violation_of_law`
-   `cannot_verify_pin`
-   `do_not_honor`
-   `error`
-   `exceeds_approval_amount_limit`
-   `exceeds_withdrawal_limit`
-   `expired_card`
-   `file_temporarily_not_available`
-   `incorrect_pin`
-   `insufficient_funds`
-   `invalid_account_number`
-   `invalid_amount`
-   `invalid_cvv`
-   `invalid_merchant`
-   `invalid_restricted_service_code`
-   `invalid_transaction`
-   `issuer_unavailable`
-   `lost_card_pick_up`
-   `negative_cvv_result`
-   `no_action_taken`
-   `no_checking_account`
-   `no_reason_to_decline`
-   `no_savings_account`
-   `no_such_issuer`
-   `partial_approval`
-   `pick_up_card_fraud`
-   `pick_up_card_no_fraud`
-   `pin_data_required`
-   `pin_entry_tries_exceeded`
-   `refer_to_issuer`
-   `refer_to_issuer_special_condition`
-   `reenter_transaction`
-   `security_violation`
-   `stolen_card_pick_up`
-   `suspected_fraud`
-   `system_error`
-   `transaction_does_not_fulfill_aml_req`
-   `transaction_not_permitted_card`
-   `transaction_not_permitted_terminal`
-   `unable_to_locate_record_in_file`
-   `unable_to_route_transaction`
-   `unsolicited_reversal`

You can mock a successful 3D Secure (3DS) transaction by specifying the `scenario:auth_3ds&issuer:approved` key:

```json
// Successful 3DS transaction
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Scenario-Key: scenario:auth_3ds&issuer:approved' \
--data '{}
'
```

Mock a failed transaction due to an incorrect PIN:

```json
// Incorrect pin transaction
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Scenario-Key: scenario:auth_pin&issuer:incorrect_pin' \
--data '{
    "amount": 1000,
    "currency": "NGN",
    "reference": "94ee715b-9c4b-4700-811b-c93a6f7ce07b",
    "customer_id": "cus_c44nro7QZe",
    "payment_method_id": "pmd_kKhbTyKhl4",
    "redirect_url": "https://example.com",
    "authorization": {
        "type": "pin",
        "pin": {
            "nonce": "WQC6lrkhRM5B",
            "encrypted_pin": "JQuCpsT0JlP3F0LVeaUvGkb/6rM="
        }
    },
    "recurring": false
}
'
```

Mock a declined transaction due to insufficient funds during Address Verification System (AVS) checks:

```json
// Insufficient funds AVS transaction
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Scenario-Key: scenario:auth_avs&issuer:insufficient_funds' \
--data '{}
'
```

Test Mobile Money transactions using one of two flows:

1.  The default flow prompts the customer to authorize payment via a notification on their mobile device.
2.  The redirect flow sends the customer to an authorization page.

Scenario 1 is the default flow for mobile money on the sandbox environment. To trigger this scenario, you don't need to pass the `X-Scenario-Key` header in your request.

To simulate the redirect flow, pass `scenario:auth_redirect` in the header.

```json
// Redirect auth for Mobile Money transactions
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/charges' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Scenario-Key: scenario:auth_redirect' \
--data '{}
'
```

Test transfer transactions the same way as card transactions: define a scenario using the `X-Scenario-Key` header.

Available transfer scenarios:

-   `successful`
-   `account_resolved_failed`
-   `amount_below_limit_error`
-   `amount_exceed_limit_error`
-   `blocked_bank`
-   `currency_amount_below_limit`
-   `currency_amount_exceed_limit`
-   `day_limit_error`
-   `day_transfer_limit_exceeded`
-   `disabled_transfer`
-   `duplicate_reference`
-   `file_too_large`
-   `insufficient_balance`
-   `invalid_amount`
-   `invalid_amount_validation`
-   `invalid_bulk_data`
-   `invalid_currency`
-   `invalid_payouts`
-   `invalid_reference`
-   `invalid_reference_length`
-   `invalid_wallet_currency`
-   `month_limit_error`
-   `month_transfer_limit_exceeded`
-   `no_account_found`
-   `payout_creation_error`
-   `unavailable_transfer_option`

You can mock a successful transfer request using the `scenario:successful` key:

```json
// Successful transfer
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Scenario-Key: scenario:successful' \
--data '{
  "action": "instant",
  "disburse_option": {
    "timezone": "Africa/Cairo"
  },
  "payment_instruction": {
    "source_currency": "USD",
    "amount": {
      "applies_to": "destination_currency",
      "value": 3500
    },
    "recipient_id": "rcb_aErW4535uiF8S"
  },
  "callback_url": "https://custom-redirect.com"
}'
```

Mock a failed transfer due to an invalid currency:

```json
// Invalid Currency
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Scenario-Key: scenario:invalid_currency' \
--data '{
  "action": "instant",
  "disburse_option": {
    "timezone": "Africa/Cairo"
  },
  "payment_instruction": {
    "source_currency": "USD",
    "amount": {
      "applies_to": "destination_currency",
      "value": 3500
    },
    "recipient_id": "rcb_aErW4535uiF8S"
  },
  "callback_url": "https://custom-redirect.com"
}'
```

Mock a failed transfer caused by insufficient balance:

```json
// Insufficient balance
curl --request POST \
--url 'https://developersandbox-api.flutterwave.com/transfers' \
--header 'Authorization: Bearer {{YOUR_ACCESS_TOKEN}}' \
--header 'Content-Type: application/json' \
--header 'X-Trace-Id: {{YOUR_UNIQUE_TRACE_ID}}' \
--header 'X-Scenario-Key: scenario:insufficient_balance' \
--data '{
  "action": "instant",
  "disburse_option": {
    "timezone": "Africa/Cairo"
  },
  "payment_instruction": {
    "source_currency": "USD",
    "amount": {
      "applies_to": "destination_currency",
      "value": 3500
    },
    "recipient_id": "rcb_aErW4535uiF8S"
  },
  "callback_url": "https://custom-redirect.com"
}'
```

  

> ## ❗️
> 
> Default Transfer Testing
> 
> If you do not pass the `X-Scenario-Key` header, the transfer remains in a `pending` state and no webhook is sent for the test.

Updated 3 months ago

* * *
