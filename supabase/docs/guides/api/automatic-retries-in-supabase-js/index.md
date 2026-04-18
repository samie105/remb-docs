---
title: "How to do automatic retries with supabase-js"
source: "https://supabase.com/docs/guides/api/automatic-retries-in-supabase-js"
canonical_url: "https://supabase.com/docs/guides/api/automatic-retries-in-supabase-js"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:58.733Z"
content_hash: "2c7eff5a282043a08b50730876b1843b9bff5c4ac5c5bc125b0c6185bddd42a4"
menu_path: ["How to do automatic retries with supabase-js"]
section_path: []
nav_prev: {"path": "supabase/docs/guides/api/api-keys/index.md", "title": "Understanding API keys"}
nav_next: {"path": "supabase/docs/guides/api/creating-routes/index.md", "title": "Creating API Routes"}
---

# 

How to do automatic retries with `supabase-js`

## 

Learn how to configure automatic retries for your Supabase API requests.

* * *

##### Important

You should only enable retries if your requests fail with network errors (e.g. 520 status from Cloudflare). A high number of retries have the potential to exhaust the Data API connection pool, which could result in lower throughput and failed requests.

## Built-in retries for PostgREST queries[#](#built-in-retries-for-postgrest-queries)

Starting with `supabase-js` v2.102.0, PostgREST queries (`.from()`, `.rpc()`) include built-in automatic retries for transient errors. Retries are **enabled by default** and use exponential backoff with jitter.

Retryable errors include HTTP status codes 408 (Request Timeout), 409 (Conflict), 503 (Service Unavailable), and 504 (Gateway Timeout), as well as network failures. Only idempotent HTTP methods (GET, HEAD, OPTIONS) and POST requests (used by PostgREST) are retried.

### Disable built-in retries[#](#disable-built-in-retries)

If you prefer to handle retries yourself, you can disable the built-in retry behavior:

```
1import { createClient } from '@supabase/supabase-js'23const supabase = createClient('https://your-project-id.supabase.co', 'your-anon-key', {4  db: {5    retry: false,6  },7})
```

## Custom retries with `fetch-retry`[#](#custom-retries-with-fetch-retry)

For more control over retry behavior, or to add retries to non-PostgREST requests (auth, storage, functions), you can use the `fetch-retry` package. This approach wraps the native `fetch` function and applies to all requests made by the client.

### 1\. Install dependencies[#](#1-install-dependencies)

To get started, ensure you have both `supabase-js` and `fetch-retry` installed in your project:

```
1npm install @supabase/supabase-js fetch-retry
```

### 2\. Wrap the fetch function[#](#2-wrap-the-fetch-function)

The `fetch-retry` package works by wrapping the native `fetch` function. You can create a custom fetch instance with retry logic and pass it to the `supabase-js` client.

```
1import { createClient } from '@supabase/supabase-js'2import fetchRetry from 'fetch-retry'34// Wrap the global fetch with fetch-retry5const fetchWithRetry = fetchRetry(fetch)67// Create a Supabase client instance with the custom fetch8const supabase = createClient('https://your-project-id.supabase.co', 'sb_publishable_...', {9  global: {10    fetch: fetchWithRetry,11  },12})
```

### 3\. Configure retry options[#](#3-configure-retry-options)

You can configure `fetch-retry` options to control retry behavior, such as the number of retries, retry delay, and which errors should trigger a retry.

Here is an example with custom retry options:

```
1const fetchWithRetry = fetchRetry(fetch, {2  retries: 3, // Number of retry attempts3  retryDelay: (attempt) => Math.min(1000 * 2 ** attempt, 30000), // Exponential backoff4  retryOn: [520], // Retry only on Cloudflare errors5})
```

In this example, the `retryDelay` function implements an exponential backoff strategy, and retries are triggered only for specific HTTP status codes.

### 4\. Using the Supabase client[#](#4-using-the-supabase-client)

With `fetch-retry` integrated, you can use the Supabase client as usual. The retry logic will automatically apply to all network requests made by `supabase-js`.

```
1async function fetchData() {2  const { data, error } = await supabase.from('your_table').select('*')34  if (error) {5    console.error('Error fetching data:', error)6  } else {7    console.log('Fetched data:', data)8  }9}1011fetchData()
```

### 5\. Fine-tuning retries for specific requests[#](#5-fine-tuning-retries-for-specific-requests)

If you need different retry logic for certain requests, you can use the `retryOn` with a custom function to inspect the URL or response and decide whether to retry the request.

```
1const fetchWithRetry = fetchRetry(fetch, {2  retryDelay: (attempt) => Math.min(1000 * 2 ** attempt, 30000),3  retryOn: (attempt, error, response) => {4    const shouldRetry5      = (attempt: number, error: Error | null, response: Response | null) =>6        attempt < 37          && response8          && response.status == 520 // Cloudflare errors9          && response.url.includes('rpc/your_stored_procedure')1011    if (shouldRetry(attempt, error, response)) {12      console.log(`Retrying request... Attempt #${attempt}`, response)13      return true14    }1516    return false17  }18})1920async function yourStoredProcedure() {21  const { data, error } = await supabase22    .rpc('your_stored_procedure', { param1: 'value1' });2324  if (error) {25    console.log('Error executing RPC:', error);26  } else {27    console.log('Response:', data);28  }29}3031yourStoredProcedure();
```

By using `retryOn` with a custom function, you can define specific conditions for retrying requests. In this example, the retry logic is applied only to requests targeting a specific stored procedure.

## Conclusion[#](#conclusion)

For most use cases, the built-in PostgREST retry mechanism is sufficient. Use `fetch-retry` when you need retries on non-PostgREST requests or need fine-grained control over retry behavior.

