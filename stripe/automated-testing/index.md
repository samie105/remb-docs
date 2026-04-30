---
title: "Automated testing"
source: "https://docs.stripe.com/automated-testing"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:49:52.661Z"
content_hash: "38141373027b3666d8dcf9d9715b3aafad2ebe8afe5077e056bf261000800c43"
---

Automated testing is a common part of application development, both for server and client-side code. Frontend interfaces, like [Stripe Checkout](https://docs.stripe.com/payments/checkout) or the [Payment Element](https://docs.stripe.com/payments/payment-element), have security measures in place that prevent automated testing, and Stripe APIs are rate limited. However, you can simulate the output of our interfaces and API requests using mock data to test your application behavior and its ability to [handle errors](https://docs.stripe.com/error-handling).

## Client side testing

If you want to test your application’s ability to recover from errors, such as transaction declines when using the Payment Element, you can return a simulated [error object](https://docs.stripe.com/api/errors) by hard-coding error objects in your test code, or creating an API service that returns mock errors in an HTTP response. The error object represents what the [confirmPayment function](https://docs.stripe.com/js/payment_intents/confirm_payment) returns when a card is declined. The following section shows you how to generate a simulated error object.

### Generating an error object

First, manually use a Stripe UI element, such as the [Payment Element](https://docs.stripe.com/js/element/payment_element), to produce an error object by confirming a test PaymentIntent using one of the [test card numbers](https://docs.stripe.com/testing#declined-payments) for declined payments. Log the error during the confirmation process, as shown below.

`const { error } = await stripe.confirmPayment({   elements,   confirmParams: {     return_url: '[https://example.com](https://example.com/)'   }, }) ; if (error) {   console.log(error) }`

This produces an error object logged to the browser console that resembles the one shown below. The specifics for properties such as `error_code` depend on the card used and the type of error it generates.

`{   "charge": "{{CHARGE_ID}}",   "code": "card_declined",   "decline_code": "generic_decline",   "doc_url": "https://docs.stripe.com/error-codes#card-declined",   "message": "Your card has been declined.",   "payment_intent": {"id": "{{PAYMENT_INTENT_ID}}", …},   "payment_method": {"id": "{{PAYMENT_METHOD_ID}}", …},   "request_log_url": "https://dashboard.stripe.com/test/logs/req_xxxxxxx",   "type": "card_error" }`

Modify your tests to return this error object instead of calling Stripe.js functions and the Stripe APIs. You can use different [test cards](https://docs.stripe.com/testing#declined-payments) to generate errors with different error codes to make sure your application properly handles each type of error.

## Server side testing

You can use the same approach when testing server-side API calls. You can generate Stripe API responses manually for various errors and mock the response returned in back-end automated testing.

For example, to write a test to validate that your application can correctly handle an off-session payment requiring 3DS, you can generate the response by creating a Payment Intent with the Payment Method `pm_card_authenticationRequired` and confirm set to `true`.

`curl https://api.stripe.com/v1/payment_intents \  -u "`

`sk_test_REDACTED`

`:" \  -d amount=2099 \  -d currency=usd \  -d payment_method=pm_card_authenticationRequired \  -d confirm=true \  -d off_session=true`

This generates a Payment Intent with a status of `requires_confirmation`, and other properties associated with [3DS Authentication](https://docs.stripe.com/payments/3d-secure) like `next_action`.

`{   "id": "{{PAYMENT_INTENT_ID}}",   "object": "payment_intent",   ... 	"next_action": {         "type": "use_stripe_sdk",     ...   },   ...   "status": "requires_confirmation",   ... }`

Generating PaymentIntent objects that reflect different stages of the [Payment lifecycle](https://docs.stripe.com/payments/paymentintents/lifecycle) allows you to test your application’s behavior as the PaymentIntent transitions through various states. Use this approach in your automated testing to make sure your integration can successfully respond to different outcomes, such as requesting that the customer comes back on-session to authenticate a payment that requires a next action.

#### When to use this approach

The above examples reference testing the behavior of your application and are suitable to use in a continuous integration test suite. When you need to perform tests to validate the response of the Stripe API, you can make requests to the API in a testing environment. You can also use Stripe API requests to periodically validate that Stripe API responses haven’t changed, but perform these tests infrequently to avoid [rate limits](https://docs.stripe.com/rate-limits).
