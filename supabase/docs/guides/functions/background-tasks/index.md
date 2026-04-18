---
title: "Background Tasks"
source: "https://supabase.com/docs/guides/functions/background-tasks"
canonical_url: "https://supabase.com/docs/guides/functions/background-tasks"
docset: "supabase"
kind: "platform"
adapter: "generic"
last_crawled_at: "2026-04-18T16:43:48.328Z"
content_hash: "b1d9c4cce3e096cd9bd8e8c01e4b0a3d6695b32c025b8349f4eb863e12c7177d"
menu_path: ["Edge Functions","Edge Functions","Advanced Features","Advanced Features","Background Tasks","Background Tasks"]
section_path: ["Edge Functions","Edge Functions","Advanced Features","Advanced Features","Background Tasks","Background Tasks"]
nav_prev: {"path": "supabase/docs/guides/functions/auth-legacy-jwt/index.md", "title": "Integrating With Supabase Auth"}
nav_next: {"path": "supabase/docs/guides/functions/compression/index.md", "title": "Handling Compressed Requests"}
---

# 

Background Tasks

## 

Run background tasks in an Edge Function outside of the request handler.

* * *

Edge Function instances can process background tasks outside of the request handler. Background tasks are useful for asynchronous operations like uploading a file to Storage, updating a database, or sending events to a logging service. You can respond to the request immediately and leave the task running in the background.

This allows you to:

*   Respond quickly to users while processing continues
*   Handle async operations without blocking the response

* * *

## Overview[#](#overview)

You can use `EdgeRuntime.waitUntil(promise)` to explicitly mark background tasks. The Function instance continues to run until the promise provided to `waitUntil` completes.

```
1// Mark the asyncLongRunningTask's returned promise as a background task.2// ⚠️ We are NOT using `await` because we don't want it to block!3EdgeRuntime.waitUntil(asyncLongRunningTask())45Deno.serve(async (req) => {6  return new Response(...)7})
```

You can call `EdgeRuntime.waitUntil` in the request handler too. This will not block the request.

```
1Deno.serve(async (req) => {2  // Won't block the request, runs in background.3  EdgeRuntime.waitUntil(asyncLongRunningTask())45  return new Response(...)6})
```

You can listen to the `beforeunload` event handler to be notified when the Function is about to be shut down.

```
1EdgeRuntime.waitUntil(asyncLongRunningTask())23// Use beforeunload event handler to be notified when function is about to shutdown4addEventListener('beforeunload', (ev) => {5  console.log('Function will be shutdown due to', ev.detail?.reason)6  // Save state or log the current progress7})89Deno.serve(async (req) => {10  return new Response(...)11})
```

## Handling errors[#](#handling-errors)

We recommend using `try`/`catch` blocks within your background task function to handle errors.

You can also add an event listener to [`unhandledrejection`](https://developer.mozilla.org/en-US/docs/Web/API/Window/unhandledrejection_event) to handle any promises without a rejection handler.

```
1addEventListener('unhandledrejection', (ev) => {2  console.log('unhandledrejection', ev.reason)3  ev.preventDefault()4})
```

The maximum duration is capped based on the wall-clock, CPU, and memory limits. The function will shut down when it reaches one of these [limits](/docs/guides/functions/limits).

* * *

## Testing background tasks locally[#](#testing-background-tasks-locally)

When testing Edge Functions locally with Supabase CLI, the instances are terminated automatically after a request is completed. This will prevent background tasks from running to completion.

To prevent that, you can update the `supabase/config.toml` with the following settings:

```
1[edge_runtime]2policy = "per_worker"
```
