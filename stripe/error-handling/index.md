---
title: "Error handling"
source: "https://docs.stripe.com/error-handling"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:51:15.259Z"
content_hash: "949bb9962f7a45ffcc5d78c04fd100aa286baf49b70d76a8043bb0843bfe3fb2"
---

Stripe offers many kinds of errors. They can reflect external events, like declined payments and network interruptions, or code problems, like invalid API calls.

## Parse error data

When Stripe returns an error to your API request, you receive details about the error that help you understand how to apply the handling suggestions in this guide. These details also help you provide important information to Stripe support, if needed.

Property

Description

`code`

The error code.

`doc_url`

A link to the Stripe documentation for the specific error code.

`message`

A description of the reason for the error.

`param`

The parameter of the request that caused the error.

`request_log_url`

A link to the Stripe Dashboard where you can see detailed logs about the originating request and the error.

Request ID

A unique identifier for the originating request that errored. The error response header includes this value (string beginning with `req`), but you can specify a print in your request, as shown in the code samples in this guide.

`type`

A reference to the error category this error belongs to.

To handle errors, use some or all of the techniques in the table below. No matter what technique you use, you can follow up with our [recommended responses for each error type](#error-types).

Technique

Purpose

When needed

[Catch exceptions](#catch-exceptions)

Recover when an API call can’t continue

Always

[Monitor webhooks](#monitor-webhooks)

React to notifications from Stripe

Sometimes

[Get stored information about failures](#use-stored-information)

Investigate past problems and support other techniques

Sometimes

## Catch exceptions

If an immediate problem prevents an API call from continuing, the Stripe Ruby library raises an exception. It’s a best practice to catch and handle exceptions.

To catch an exception, use Ruby’s `rescue` keyword. Catch `Stripe::StripeError` or its subclasses to handle Stripe-specific exceptions only. Each subclass represents a different kind of exception. When you catch an exception, you can [use its class to choose a response](#error-types).

`require 'stripe'  # Don't put any keys in code. See [https://docs.stripe.com/keys-best-practices.](https://docs.stripe.com/keys-best-practices) client = Stripe::StripeClient.new(`

`'sk_test_REDACTED'`

`)  def example_function(params)   begin     client.v1.payment_intents.  create  (params)   rescue Stripe::CardError => e     puts "A payment error occurred: #{e.error.message} (request id: #{e.request_id})"   rescue Stripe::InvalidRequestError => e     puts "An invalid request occurred. (request id: #{e.request_id})"   # Add additional catch cases for other Stripe exception types as needed.   # See all exception types at [https://docs.stripe.com/api/errors/handling?lang=ruby](https://docs.stripe.com/api/errors/handling?lang=ruby)   rescue Stripe::StripeError => e     # All other Stripe errors     puts "Status: #{e.http_status}, Code: #{e.code}, Message: #{e.message}, Request ID: #{e.request_id}"   else     puts "No error."   end end`

After setting up exception handling, test it on a variety of data, including [test cards](https://docs.stripe.com/testing), to simulate different payment outcomes.

`example_function(   # The required parameter currency is missing,   amount: 2000,   confirm: true,   payment_method:` 

`'pm_card_visa'`

`, )`

`An invalid request occurred.`

## Monitor webhooks

Stripe notifies you about many kinds of problems using [webhooks](https://docs.stripe.com/webhooks). This includes problems that don’t follow immediately after an API call. For example:

*   You lose a dispute.
*   A recurring payment fails after months of success.
*   Your frontend [confirms](https://docs.stripe.com/api/payment_intents/confirm) a payment, but goes offline before finding out the payment fails. (The backend still receives webhook notification, even though it wasn’t the one to make the API call.)

You don’t need to handle every webhook event type. In fact, some integrations don’t handle any.

In your webhook handler, start with the basic steps from the [webhook builder](https://docs.stripe.com/webhooks/quickstart): get an event object and use the event type to find out what happened. Then, if the event type indicates an error, follow these extra steps:

1.  Access [event.data.object](https://docs.stripe.com/api/events/object#event_object-data-object) to retrieve the affected object.
2.  [Use stored information](#use-stored-information) on the affected object to gain context, including an error object.
3.  [Use its type to choose a response](#error-types).

`require 'stripe' require 'sinatra'  client = Stripe::StripeClient.new(ENV.fetch('STRIPE_API_KEY')) post '/webhook' do   payload = request.body.read   data = JSON.parse(payload, symbolize_names: true)    # Get the event object   event = Stripe::Event.construct_from(data)    # Use the event type to find out what happened   case event.type   when 'payment_intent.payment_failed'      # Get the object affected     payment_intent = event.data.object      # Use stored information to get an error object     e = payment_intent.last_payment_error      # Use its type to choose a response     case e.type     when 'card_error'       puts "A payment error occurred: #{e.message}"     when 'invalid_request'       puts "An invalid request occurred."     else       puts "Another problem occurred, maybe unrelated to Stripe."     end   end    content_type 'application/json'   {     status: 'success'   }.to_json end`

To test how your integration responds to webhook events, you can [trigger webhook events locally](https://docs.stripe.com/webhooks#test-webhook). After completing the setup steps at that link, trigger a failed payment to see the resulting error message.

`stripe trigger payment_intent.payment_failed`

`A payment error occurred: Your card was declined.`

## Get stored information about failures

Many objects store information about failures. That means that if something already went wrong, you can retrieve the object and examine it to learn more. In many cases, stored information is in the form of an error object, and you can [use its type to choose a response](#error-types).

For instance:

1.  Retrieve a specific payment intent.
2.  Check if it experienced a payment error by determining if [last\_payment\_error](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-last_payment_error) is empty.
3.  If it did, log the error, including its type and the affected object.

`require 'stripe' # Don't put any keys in code. See [https://docs.stripe.com/keys-best-practices.](https://docs.stripe.com/keys-best-practices) client = Stripe::StripeClient.new(`

`'sk_test_REDACTED'`

`)  payment_intent = client.v1.payment_intents.  retrieve  (  '{{PAYMENT_INTENT_ID}}'  ) e = payment_intent.last_payment_error if !e.nil?   puts "PaymentIntent #{payment_intent.id} experienced a #{e.type}." end`

Here are common objects that store information about failures.

To test code that uses stored information about failures, you often need to simulate failed transactions. You can often do this using [test cards](https://docs.stripe.com/testing) or test bank numbers. For example:

*   [Simulate a declined payment](https://docs.stripe.com/testing#declined-payments), for creating failed Charges, PaymentIntents, SetupIntents, and so on.
*   [Simulate a failed payout](https://docs.stripe.com/connect/testing#account-numbers).
*   [Simulate a failed refund](https://docs.stripe.com/testing#refunds).

## Types of error and responses

In the Stripe Ruby library, error objects belong to `stripe.error.StripeError` and its subclasses. Use the documentation for each class for advice on responding.

Name

Class

Description

Payment error

[Stripe::CardError](#payment-errors)

An error occurred during a payment, involving one of these situations:

*   [Payment blocked for suspected fraud](#payment-blocked)
*   [Payment declined by the issuer](#payment-declined).
*   [Other payment errors](#other-payment-errors).

Invalid request error

[Stripe::InvalidRequestError](#invalid-request-errors)

You made an API call with the wrong parameters, in the wrong state, or in an invalid way.

Connection error

[Stripe::APIConnectionError](#connection-errors)

There was a network problem between your server and Stripe.

API error

[Stripe::APIError](#api-errors)

Something went wrong on Stripe’s end. (These are rare.)

Authentication error

[Stripe::AuthenticationError](#authentication-errors)

Stripe can’t authenticate you with the information provided.

Idempotency error

[Stripe::IdempotencyError](#idempotency-errors)

You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests) for something unexpected, like replaying a request but passing different parameters.

Permission error

[Stripe::PermissionError](#permission-errors)

The API key used for this request doesn’t have the necessary permissions.

Rate limit error

[Stripe::RateLimitError](#rate-limit-errors)

You made too many API calls in too short a time.

Signature verification error

[Stripe::SignatureVerificationError](#signature-verification-errors)

You’re using [webhook](https://docs.stripe.com/webhooks) [signature verification](https://docs.stripe.com/webhooks#verify-events) and couldn’t verify that a webhook event is authentic.

## Payment errors

Payment errors—sometimes called “card errors” for historical reasons—cover a wide range of common problems. They come in three categories:

*   [Payment blocked for suspected fraud](#payment-blocked)
*   [Payment declined by the issuer](#payment-declined)
*   [Other payment errors](#other-payment-errors)

To distinguish these categories or get more information about how to respond, consult the [error code](https://docs.stripe.com/error-codes), [decline code](https://docs.stripe.com/declines/codes), and [charge outcome](https://docs.stripe.com/api/charges/object#charge_object-outcome).

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-latest_charge). See the example below for a demonstration.)

`require 'stripe'  def example_function(params) # Don't put any keys in code. See [https://docs.stripe.com/keys-best-practices.](https://docs.stripe.com/keys-best-practices) # Find your keys at [https://dashboard.stripe.com/apikeys.](https://dashboard.stripe.com/apikeys) client = Stripe::StripeClient.new(`

`'sk_test_REDACTED'`

`)   begin     client.v1.payment_intents.create(params)   rescue Stripe::CardError => e     charge = client.v1.charges.retrieve(e.error.payment_intent.latest_charge)     if charge.outcome.type == 'blocked'       puts 'Payment blocked for suspected fraud.'     elsif e.code == 'card_declined'       puts 'Payment declined by the issuer.'     elsif e.code == 'expired_card'       puts 'Card expired.'     else       puts 'Other card error.'     end   end end`

Users on API version [2022-08-01](https://docs.stripe.com/upgrades#2022-08-01) or older:

(To find the charge outcome from an error object, first get the [Payment Intent that’s involved](https://docs.stripe.com/api/errors#errors-payment_intent) and the [latest Charge it created](https://docs.stripe.com/api/payment_intents/object#payment_intent_object-charges-data). See the example below for a demonstration.)

`require 'stripe'  def example_function(params) # Don't put any keys in code. See [https://docs.stripe.com/keys-best-practices.](https://docs.stripe.com/keys-best-practices) # Find your keys at [https://dashboard.stripe.com/apikeys.](https://dashboard.stripe.com/apikeys) client = Stripe::StripeClient.new(`

`'sk_test_REDACTED'`

`)   begin     client.v1.payment_intents.  create  (params)   rescue Stripe::CardError => e     if e.error.payment_intent.charges.data[0].outcome.type == 'blocked'       puts 'Payment blocked for suspected fraud.'     elsif e.code == 'card_declined'       puts 'Payment declined by the issuer.'     elsif e.code == 'expired_card'       puts 'Card expired.'     else       puts 'Other card error.'     end   end end`

You can trigger some common kinds of payment error with test cards. Consult these lists for options:

*   [Simulating payments blocked for fraud risk](https://docs.stripe.com/testing#fraud-prevention)
*   [Simulating declined payments and other card errors](https://docs.stripe.com/testing#declined-payments)

The test code below demonstrates a few possibilities.

`example_function(   currency: 'usd',   amount: 2000,   confirm: true,   payment_method:` 

`'pm_card_radarBlock'`

`, )`

`Payment blocked for suspected fraud.`

### Payment blocked for suspected fraud

**Type**

`Stripe::CardError`

**Codes**

`# Don't put any keys in code. See [https://docs.stripe.com/keys-best-practices.](https://docs.stripe.com/keys-best-practices) # Find your keys at [https://dashboard.stripe.com/apikeys.](https://dashboard.stripe.com/apikeys) client = Stripe::StripeClient.new(`

`'sk_test_REDACTED'`

`) charge = client.v1.charges.  retrieve  (e.error.payment_intent.latest_charge) charge.outcome.type == 'blocked'`

Users on API version [2022-08-01](https://docs.stripe.com/upgrades#2022-08-01) or older:

**Codes**

`e.error.payment_intent.charges.data[0].outcome.type == 'blocked'`

**Problem**

Stripe’s fraud prevention system, [Radar](https://docs.stripe.com/radar), blocked the payment

**Solutions**

This error can occur when your integration is working correctly. Catch it and prompt the customer for a different payment method.

To block fewer legitimate payments, try these:

*   [Optimize your Radar integration](https://docs.stripe.com/radar/optimize-risk-factors) to collect more detailed information.
*   Use [Payment Links](https://docs.stripe.com/payment-links), [Checkout](https://docs.stripe.com/payments/checkout), or [Stripe Elements](https://docs.stripe.com/payments/elements) for prebuilt optimized form elements.

[Radar for Fraud Teams](https://docs.stripe.com/radar) customers have these additional options:

*   To exempt a specific payment, add it to your allowlist. Radar for Fraud Teams
*   To change your risk tolerance, adjust your [risk settings](https://docs.stripe.com/radar/risk-settings). Radar for Fraud Teams
*   To change the criteria for blocking a payment, use [custom rules](https://docs.stripe.com/radar/rules). Radar for Fraud Teams

You can test your integration’s settings with [test cards that simulate fraud](https://docs.stripe.com/radar/testing). If you have custom Radar rules, follow the testing advice in the [Radar documentation](https://docs.stripe.com/radar/testing).

### Payment declined by the issuer

### Other payment errors

**Type**

`Stripe::CardError`

**Problem**

Another payment error occurred.

**Solutions**

This error can occur when your integration is working correctly. Use the error code to determine what next steps are appropriate. See the [documentation on error codes](https://docs.stripe.com/error-codes) for appropriate responses to each code.

## Invalid request errors

**Type**

`Stripe::InvalidRequestError`

**Problem**

You made an API call with the wrong parameters, in the wrong state, or in an invalid way.

**Solutions**

In most cases, the problem is with the request itself. Either its parameters are invalid or it can’t be carried out in your integration’s current state.

*   Consult the [error code documentation](https://docs.stripe.com/error-codes) for details on the problem.
*   For convenience, you can follow the link at for documentation about the error code.
*   If the error involves a specific parameter, use to determine which one.

## Connection errors

**Type**

`Stripe::APIConnectionError`

**Problem**

There was a network problem between your server and Stripe.

**Solutions**

Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

To find out if it succeeded, you can:

*   Retrieve the relevant object from Stripe and check its status.
*   Listen for webhook notification that the operation succeeded or failed.

To help recover from connection errors, you can:

*   When creating or updating an object, use an [idempotency key](https://docs.stripe.com/api/idempotent_requests). Then, if a connection error occurs, you can safely repeat the request without risk of creating a second object or performing the update twice. Repeat the request with the same idempotency key until you receive a clear success or failure. For advanced advice on this strategy, see [Low-level error handling](https://docs.stripe.com/error-low-level#idempotency).
*   Turn on [automatic retries](https://github.com/stripe/stripe-java?tab=readme-ov-file#configuring-automatic-retries). Then, Stripe generates idempotency keys for you, and repeats requests for you when it’s safe to do so.

This error can mask others. It’s possible that when the connection error resolves, some other error becomes apparent. Check for errors in all of these solutions just as you would in the original request.

## API errors

**Type**

`Stripe::APIError`

**Problem**

Something went wrong on Stripe’s end. (These are rare.)

**Solutions**

Treat the result of the API call as indeterminate. That is, don’t assume that it succeeded or that it failed.

Rely on [webhooks](https://docs.stripe.com/webhooks) for information about the outcome. Whenever possible, Stripe fires webhooks for any new objects we create as we solve a problem.

To set your integration up for maximum robustness in unusual situations, see [this advanced discussion of server errors.](https://docs.stripe.com/error-low-level#server-errors)

## Authentication errors

**Type**

`Stripe::AuthenticationError`

**Problem**

Stripe can’t authenticate you with the information provided.

**Solutions**

*   Use the correct [API key](https://docs.stripe.com/keys).
*   Make sure you aren’t using a key that you [“rotated” or revoked](https://docs.stripe.com/keys#rolling-keys).

## Idempotency errors

**Type**

`Stripe::IdempotencyError`

**Problem**

You used an [idempotency key](https://docs.stripe.com/api/idempotent_requests) for something unexpected, like replaying a request but passing different parameters.

**Solutions**

*   After you use an idempotency key, only reuse it for identical API calls.
*   Use idempotency keys under the limit of 255 characters.

## Permission errors

**Type**

`Stripe::PermissionError`

**Problem**

The API key used for this request doesn’t have the necessary permissions.

**Solutions**

*   Make sure you aren’t using a [restricted API key](https://docs.stripe.com/keys-best-practices#limit-access) for a service it doesn’t have access to.
*   Don’t perform actions in the Dashboard while logged in as a [user role](https://docs.stripe.com/get-started/account/teams/roles) that lacks permission.

## Rate limit errors

**Type**

`Stripe::RateLimitError`

**Problem**

You made too many API calls in too short a time.

**Solutions**

*   If a single API call triggers this error, wait and try it again.
*   To handle rate-limiting automatically, retry the API call after a delay, and increase the delay exponentially if the error continues. See the documentation on [rate limits](https://docs.stripe.com/rate-limits) for further advice.
*   If you anticipate a large increase in traffic and want to request an increased rate limit, [contact support](https://support.stripe.com/) in advance.

## Signature verification errors

**Type**

`Stripe::SignatureVerificationError`

**Problem**

You’re using [webhook](https://docs.stripe.com/webhooks) [signature verification](https://docs.stripe.com/webhooks#verify-events) and couldn’t verify that a webhook event is authentic.

**Solutions**

This error can occur when your integration is working correctly. If you use webhook signature verification and a third party attempts to send you a fake or malicious webhook, then verification fails and this error is the result. Catch it and respond with a `400 Bad Request` status code.

If you receive this error when you shouldn’t—for instance, with webhooks that you know originate with Stripe—then see the documentation on [checking webhook signatures](https://docs.stripe.com/webhooks#verify-events) for further advice. In particular, make sure you’re using the correct endpoint secret. This is different from your API key.
