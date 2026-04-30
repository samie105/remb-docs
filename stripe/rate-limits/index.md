---
title: "Rate limits"
source: "https://docs.stripe.com/rate-limits"
docset: "stripe"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-30T12:54:57.725Z"
content_hash: "84296a4b3e40a35831f98501791aabf99860a6496295d9dd09220b6784cd0de2"
---

We use safeguards against bursts of incoming traffic to maximize API stability. If you send many requests in quick succession, you might receive `429` error responses.

## API limiters

We enforce several API limiters, including rate and concurrency limiters. Treat limits as maximums and avoid unnecessary load. To prevent abuse, we might reduce your limits. For advice on handling `429` errors, see [Handling limiting gracefully](#handling-limiting-gracefully). If you see a rise in rate-limited requests, [contact Stripe Support](https://support.stripe.com/).

Request a limit increase for high-traffic applications through [Stripe Support](https://support.stripe.com/). If you request a large increase, [contact Stripe Support](https://support.stripe.com/) at least 6 weeks in advance.

### Rate limiter

The basic rate limiter restricts the number of API requests per second as follows:

*   **Live mode**: 100 operations
*   [Sandbox](https://docs.stripe.com/sandboxes): 25 operations

Calls to individual resources have stricter limits, and also count against global limits. API endpoints have a default limit of 25 requests per second. Stripe may increase rate limits for specific accounts based on usage.

*   [Payment Intents API](https://docs.stripe.com/api/payment_intents): 1000 update operations per PaymentIntent, per hour.
*   [Files API](https://docs.stripe.com/api/files): 20 read operations and 20 write operations per second.
*   [Search API](https://docs.stripe.com/search#rate-limits): 20 read operations per second.
*   [Subscriptions API](https://docs.stripe.com/api/subscriptions):
    *   10 new invoices per subscription, per minute.
    *   20 new invoices per subscription, per day.
    *   200 quantity updates per subscription, per hour.
*   [Create Payout API](https://docs.stripe.com/api/payouts/create): 15 requests per second and 30 concurrent requests per business.
*   [Connect](https://docs.stripe.com/connect): Platforms can create up to 5 accounts per second in sandbox and 30 accounts per second in live mode.
*   [Issuing](https://docs.stripe.com/issuing): Card creation has rate limits that depend on the country and business’s industry.

Calls to the [Meter events endpoint](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api#rate-limits) in live mode are subject to a separate rate limit, and don’t count against the basic limits. The limit is 1000 calls per second per Stripe account. In a sandbox, calls to the Meter events endpoint count toward the basic limit. For Connect platforms, calls on a connected account to the Meter events endpoint also count toward the basic limit.

### Rate limited requests

Requests that are rate limited return the `Stripe-Rate-Limited-Reason` header with values that indicate which rate limit the request exceeded. Possible values for this header are:

*   `global-concurrency`: Your requests have exceeded the global concurrency limit. You can prevent this by sending fewer simultaneous requests.
*   `global-rate`: Your requests have exceeded the global rate limit. You can prevent this by sending requests at a lower rate.
*   `endpoint-concurrency`: Your requests to this specific API endpoint have exceeded the concurrency limit. You can prevent this by sending fewer simultaneous requests to this specific endpoint.
*   `endpoint-rate`: Your requests to this specific API endpoint have exceeded the rate limit. You can prevent this by sending requests to this endpoint at a lower rate.
*   `resource-specific`: You’ve hit a rate limit related to a specific API resource. Refer to the documentation for that resource for more information.

If a request returns a `429` status code without these headers, it wasn’t the result of a rate limiter (for example, it may be a lock timeout).

### Concurrency limiter

The concurrency limiter restricts the number of concurrent active requests. Problems with this limiter are less common than with the rate limiter, but they likely indicate the existence of resource-intensive, long-lived requests.

Calls to the [Meter events endpoint](https://docs.stripe.com/billing/subscriptions/usage-based/recording-usage-api#rate-limits) are limited to one concurrent call per customer per meter.

## Common causes and mitigations

Rate limiting can occur under a variety of conditions, but it’s most common in these scenarios:

*   Running **a large volume of closely-spaced requests** can lead to rate limiting. Often this is part of an analytical or migration operation. When engaging in these activities, you should try to control the request rate on the client side (see [Handling limiting gracefully](#handling-limiting-gracefully)).
    
*   Issuing **many long-lived requests** can trigger limiting. Requests vary in the amount of Stripe server resources they use, and more resource-intensive requests can take longer and run the risk of causing the concurrency limiter to shed new requests. Resource requirements vary widely, but list requests and requests that include expansions generally use more resources and take longer to run. We suggest profiling the duration of Stripe API requests and watching for timeouts to try and spot those that are unexpectedly slow.
    
*   A sudden increase in charge volume, such as a **flash sale**, might result in rate limiting. We try to set our rates high enough that legitimate payment traffic never exceeds the limits, but if you suspect that an upcoming event might push you over the limits listed above, [contact Stripe Support](https://support.stripe.com/).
    

## Handle limiting

Watch for `429` status codes and implement a retry mechanism to handle rate limiting. Follow an exponential backoff schedule to reduce request volume when necessary, and add randomness to the backoff schedule to avoid a [thundering herd effect](https://en.wikipedia.org/wiki/Thundering_herd_problem).

You can only optimize individual requests to a limited degree, so an even more sophisticated approach would be to control traffic to Stripe at a global level, and throttle it back if you detect substantial rate limiting. A common technique for controlling rate is to implement something like a [token bucket rate limiting algorithm](https://en.wikipedia.org/wiki/Token_bucket) on the client-side. Ready-made and mature implementations for token bucket are available in almost any programming language.

## Object lock timeouts

Integrations might encounter errors with HTTP status `429`, code `lock_timeout`, and this message:

> This object can’t be accessed right now because another API request or Stripe process currently accessing it. If you see this error intermittently, retry the request. If you see this error frequently and are making multiple concurrent requests to a single object, make your requests serially or at a lower rate.

The Stripe API locks objects on some operations so that concurrent workloads don’t interfere and produce an inconsistent result. The error above is caused by a request trying to acquire a lock that’s already held elsewhere, and timing out after it couldn’t be acquired in time. Stripe doesn’t process these failed requests, which means they’re not assigned a [request ID](https://docs.stripe.com/api/request_ids).

Lock timeouts have a different cause than rate limiting, but their mitigations are similar. As with rate limiting errors, we recommend retrying on an exponential backoff schedule (see [Handling limiting gracefully](#handling-limiting-gracefully)). But unlike rate limiting errors, the automatic retry mechanisms built into Stripe’s [SDKs](https://docs.stripe.com/sdks) retry `429`s caused by lock timeouts:

`Stripe.max_network_retries = 2`

Lock contention is caused by concurrent access on related objects. Integrations can vastly reduce this by making sure that mutations on the same object are queued up and run sequentially instead. Concurrent operations against the API are still okay, but try to make sure simultaneous operations operate only on unique objects. It’s also possible to see lock contention caused by a conflict with an internal Stripe background process. This should be rare, but because it’s beyond user control, we recommend that all integrations are able to retry requests.

## Load testing

It’s common for users to prepare for a major sales event by load testing their systems, with the Stripe API running in a sandbox as part of it. We generally discourage this practice because API limits are lower in a sandbox, so the load test is likely to hit limits that it wouldn’t hit in production. A sandbox is also not a perfect stand-in for live API calls, and that can be somewhat misleading. For example, creating a charge in live mode sends a request to a payment gateway and that request is mocked in a sandbox, resulting in significantly different latency profiles.

As an alternative, we recommend building integrations so that they have a configurable system for mocking out requests to the Stripe API, which you can enable for load tests. For realistic results, they should simulate latency by sleeping for a time that you determine by sampling the durations of real live mode Stripe API calls, as seen from the perspective of the integration.

## API read request allocations

Stripe provides access to its read (GET) API requests to facilitate reasonable lookup activity related to payment integrations. To maximize quality of service for all users, Stripe provides the following allocations for read requests based on transaction count:

*   Your account’s read API requests must not exceed an average of 500 per transaction. For example, if you process 100 transactions in 30 days, you must not exceed 50,000 read API requests during that period.
    
*   When using Connect, a platform and its connected accounts have distinct read API allowances:
    
    *   Each connected account has their own allocation for requests they initiate (500 requests per transaction).
    *   Connect platforms use a separate allocation to make read requests on behalf of their connected accounts using either their secret API key or OAuth access tokens. This allocation is also 500 requests per transaction based on the aggregate transaction count across its connected accounts.
*   Ratios are calculated over a rolling 30‑day period (the most recent 30 days).
    
*   Every account, regardless of transaction count, has a minimum allocation of 10,000 read requests per month.
    
*   Write API requests have no allocation limit.
    

Calls to the following API endpoints are excluded from the above allocation limits:

*   [Data products](https://docs.stripe.com/stripe-data)
*   [Reporting products](https://docs.stripe.com/stripe-reports)
*   [Tax products](https://docs.stripe.com/tax)

To reduce your API request volume, consider using [Stripe Data Pipeline](https://stripe.com/data-pipeline) for a complete export of API data to your local database or provider.

#### Filter requests to limit paginated calls

Some list endpoints return [multiple pages](https://docs.stripe.com/api/pagination) of results and might require multiple requests to return the full set of API objects for a list operation. Apply filters when possible to narrow your list results.
