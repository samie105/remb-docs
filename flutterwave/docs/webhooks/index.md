---
title: "Webhooks"
source: "https://developer.flutterwave.com/docs/webhooks#"
canonical_url: "https://developer.flutterwave.com/docs/webhooks"
docset: "flutterwave"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-29T23:32:45.321Z"
content_hash: "61d2d163b3fc656dbe5710658a6ec8d276e53613f457d94d62dbcc61e939937b"
menu_path: ["Webhooks"]
section_path: []
tab_variants: ["Node.js","PHP","Python"]
content_language: "de"
nav_prev: {"path": "flutterwave/docs/common-errors/index.md", "title": "Errors"}
nav_next: {"path": "flutterwave/docs/idempotency/index.md", "title": "Idempotency"}
---

# In a Django-like app:
import os

@require_POST
@csrf_exempt
def webhook(request):
    secret_hash = os.getenv("FLW_SECRET_HASH")
    signature = request.headers.get("flutterwave-signature")
    if signature == None or (signature != secret_hash):
        # This request isn't from Flutterwave; discard
        return HttpResponse(status=401)
    payload = request.body
    # It's a good idea to log all received events.
    log(payload)
    # Do something (that doesn't take too long) with the payload
    return HttpResponse(status=200)
```

#### PHP

```javascript
// In an Express-like app:

app.post("/flw-webhook", (req, res) => {
    // If you specified a secret hash, check for the signature
    const secretHash = process.env.FLW_SECRET_HASH;
    const signature = req.headers["flutterwave-signature"];
    if (!signature || (signature !== secretHash)) {
        // This request isn't from Flutterwave; discard
        res.status(401).end();
    }
    const payload = req.body;
    // It's a good idea to log all received events.
    log(payload);
    // Do something (that doesn't take too long) with the payload
    res.status(200).end()
});
```

```php
// In a Laravel-like app:

Route::post('/flw-webhook', function (\Illuminate\Http\Request $request) {
    // If you specified a secret hash, check for the signature
    $secretHash = config('services.flutterwave.secret_hash');
    $signature = $request->header('flutterwave-signature');
    if (!$signature || ($signature !== $secretHash)) {
        // This request isn't from Flutterwave; discard
        abort(401);
    }
    $payload = $request->all();
    // It's a good idea to log all received events.
    Log::info($payload);
    // Do something (that doesn't take too long) with the payload
    return response(200);
});
```

```python
# In a Django-like app:
import os

@require_POST
@csrf_exempt
def webhook(request):
    secret_hash = os.getenv("FLW_SECRET_HASH")
    signature = request.headers.get("flutterwave-signature")
    if signature == None or (signature != secret_hash):
        # This request isn't from Flutterwave; discard
        return HttpResponse(status=401)
    payload = request.body
    # It's a good idea to log all received events.
    log(payload)
    # Do something (that doesn't take too long) with the payload
    return HttpResponse(status=200)
```

#### Python

```javascript
// In an Express-like app:

app.post("/flw-webhook", (req, res) => {
    // If you specified a secret hash, check for the signature
    const secretHash = process.env.FLW_SECRET_HASH;
    const signature = req.headers["flutterwave-signature"];
    if (!signature || (signature !== secretHash)) {
        // This request isn't from Flutterwave; discard
        res.status(401).end();
    }
    const payload = req.body;
    // It's a good idea to log all received events.
    log(payload);
    // Do something (that doesn't take too long) with the payload
    res.status(200).end()
});
```

```php
// In a Laravel-like app:

Route::post('/flw-webhook', function (\Illuminate\Http\Request $request) {
    // If you specified a secret hash, check for the signature
    $secretHash = config('services.flutterwave.secret_hash');
    $signature = $request->header('flutterwave-signature');
    if (!$signature || ($signature !== $secretHash)) {
        // This request isn't from Flutterwave; discard
        abort(401);
    }
    $payload = $request->all();
    // It's a good idea to log all received events.
    Log::info($payload);
    // Do something (that doesn't take too long) with the payload
    return response(200);
});
```

```python
# In a Django-like app:
import os

@require_POST
@csrf_exempt
def webhook(request):
    secret_hash = os.getenv("FLW_SECRET_HASH")
    signature = request.headers.get("flutterwave-signature")
    if signature == None or (signature != secret_hash):
        # This request isn't from Flutterwave; discard
        return HttpResponse(status=401)
    payload = request.body
    # It's a good idea to log all received events.
    log(payload)
    # Do something (that doesn't take too long) with the payload
    return HttpResponse(status=200)
```

Before giving value to a customer based on a webhook notification, always re-query our API to verify the transaction details. This helps confirm that the data returned is consistent with what you’re expecting and has not been compromised.

For example, when you receive a successful payment notification, call the [transaction verification endpoint](https://developer.flutterwave.com/reference/charges_get) to confirm that the `status`, `amount`, `currency`, and `tx_ref` match the expected value in your system before confirming the customer's order.

```javascript
const payload = req.body;
const response = await flw.Transaction.verify({id: payload.id});
if (
    response.data.status === "successful"
    && response.data.amount === expectedAmount
    && response.data.currency === expectedCurrency
    && response.data.tx_ref === expectedReference ) {
    // Success! Confirm the customer's payment
} else {
    // Inform the customer their payment was unsuccessful
}
```

Have a backup strategy in place, in case your webhook endpoint fails. For instance, if your webhook endpoint is throwing server errors, you won't know about any new customer payments because webhook requests will fail.

To get around this, we recommend setting up a background job that polls for the status of any pending transactions at regular intervals (for instance, every hour) using the [transaction verification endpoint](https://developer.flutterwave.com/reference/charges_get), till a successful or failed response is returned.

Remember, your webhook URL is public, and anyone can send a fake payload. We recommend using a [signature](#verifying-webhook-signatures) so you can be sure the requests you get are from Flutterwave.

Your webhook endpoint needs to respond within a certain time limit, or we'll consider it a failure and try again. Avoid doing long-running tasks or network calls in your webhook endpoint so you don't hit the timeout.

If your framework supports it, you can have your webhook endpoint immediately return a `200` status code, and then perform the rest of its duties; otherwise, you should dispatch any long-running tasks to a job queue, and then respond.

Occasionally, we might send the same webhook event more than once. You should make your event processing _idempotent_ (calling the webhook multiple times will have the same effect), so you don't end up giving a customer value multiple times.

One way of doing this is recording the events you've processed, and then checking if the status has changed before processing the duplicate event:

```javascript
const payload = req.body;
const existingEvent = await PaymentEvent.where({id: payload.id}).find();
if (existingEvent.status === payload.status) {
    // The status hasn't changed,
    // so it's probably just a duplicate event
    // and we can discard it
    res.status(200).end();
}

// Record this event
await PaymentEvent.save(payload);
// Process event...
```

Updated 3 months ago

* * *
