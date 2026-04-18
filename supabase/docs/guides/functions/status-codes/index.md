---
title: "Status codes"
source: "https://supabase.com/docs/guides/functions/status-codes"
canonical_url: "https://supabase.com/docs/guides/functions/status-codes"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:45:33.211Z"
content_hash: "a83467a0a0261acd96867568b0351e059f20cd77a5bc383947dfc878a53a5d9f"
menu_path: ["Edge Functions","Edge Functions","Platform","Platform","Status codes","Status codes"]
section_path: ["Edge Functions","Edge Functions","Platform","Platform","Status codes","Status codes"]
---
# 

Status codes

## 

Understand HTTP status codes returned by Edge Functions to properly debug issues and handle responses.

* * *

## Success Responses[#](#success-responses)

### 2XX Success[#](#2xx-success)

Your Edge Function executed successfully and returned a valid response. This includes any status code in the 200-299 range that your function explicitly returns.

### 3XX Redirect[#](#3xx-redirect)

Your Edge Function used the `Response.redirect()` API to redirect the client to a different URL. This is a normal response when implementing authentication flows or URL forwarding.

* * *

## Client Errors[#](#client-errors)

These errors indicate issues with the request itself, which typically require changing how the function is called.

### 401 Unauthorized[#](#401-unauthorized)

**Cause:** The Edge Function has JWT verification enabled, but the request was made with an invalid or missing JWT token.

**Solution:**

*   Ensure you're passing a valid JWT token in the `Authorization` header
*   Check that your token hasn't expired
*   For webhooks or public endpoints, consider disabling JWT verification

### 404 Not Found[#](#404-not-found)

**Cause:** The requested Edge Function doesn't exist or the URL path is incorrect.

**Solution:**

*   Verify the function name and project reference in your request URL
*   Check that the function has been deployed successfully

### 405 Method Not Allowed[#](#405-method-not-allowed)

**Cause:** You're using an unsupported HTTP method. Edge Functions only support: `GET`, `POST`, `PUT`, `PATCH`, `DELETE`, and `OPTIONS`.

**Solution:** Update your request to use a supported HTTP method.

* * *

## Server Errors[#](#server-errors)

These errors indicate issues with the function execution or underlying platform.

### 500 Internal Server Error[#](#500-internal-server-error)

**Cause:** Your Edge Function threw an uncaught exception (`WORKER_ERROR`).

**Common causes:**

*   Unhandled JavaScript errors in your function code
*   Missing error handling for async operations
*   Invalid JSON parsing

**Solution:** Check your Edge Function logs to identify the specific error and add proper error handling to your code.

```
1// ✅ Good error handling2try {3  const result = await someAsyncOperation()4  return new Response(JSON.stringify(result))5} catch (error) {6  console.error('Function error:', error)7  return new Response('Internal error', { status: 500 })8}
```

You can see the output in the [Edge Function Logs](/docs/guides/functions/logging).

### 503 Service Unavailable[#](#503-service-unavailable)

**Cause:** Your Edge Function failed to start (`BOOT_ERROR`).

**Common causes:**

*   Syntax errors preventing the function from loading
*   Import errors or missing dependencies
*   Invalid function configuration

**Solution:** Check your Edge Function logs and verify your function code can be executed locally with `supabase functions serve`.

### 504 Gateway Timeout[#](#504-gateway-timeout)

**Cause:** Your Edge Function didn't respond within the [request timeout limit](/docs/guides/functions/limits).

**Common causes:**

*   Long-running database queries
*   Slow external API calls
*   Infinite loops or blocking operations

**Solution:**

*   Optimize slow operations
*   Add timeout handling to external requests
*   Consider breaking large operations into smaller chunks

### 546 Resource Limit (Custom Error Code)[#](#546-resource-limit-custom-error-code)

**Cause:** Your Edge Function execution was stopped due to exceeding resource limits (`WORKER_LIMIT`). Edge Function logs should provide which [resource limit](/docs/guides/functions/limits) was exceeded.

**Common causes:**

*   Memory usage exceeded available limits
*   CPU time exceeded execution quotas
*   Too many concurrent operations

**Solution:** Check your Edge Function logs to see which resource limit was exceeded, then optimize your function accordingly.
