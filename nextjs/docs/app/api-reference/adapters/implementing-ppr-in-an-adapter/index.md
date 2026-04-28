---
title: "Implementing PPR in an Adapter"
source: "https://nextjs.org/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter"
canonical_url: "https://nextjs.org/docs/app/api-reference/adapters/implementing-ppr-in-an-adapter"
docset: "nextjs"
kind: "framework"
adapter: "nextjs"
last_crawled_at: "2026-04-27T18:04:36.978Z"
content_hash: "53bd539d6c06afd20fa3e943299fddcacd984a4dad69748808d2e597c81b6b91"
menu_path: ["Implementing PPR in an Adapter"]
section_path: []
version: "latest"
content_language: "en"
nav_prev: {"path": "nextjs/docs/app/api-reference/adapters/routing-with-next-routing/index.md", "title": "Routing with @next/routing"}
nav_next: {"path": "nextjs/docs/app/api-reference/adapters/runtime-integration/index.md", "title": "Runtime Integration"}
---

# Implementing PPR in an Adapter

Last updated April 23, 2026

For partially prerendered app routes, `onBuildComplete` gives you the data needed to seed and resume PPR:

-   `outputs.prerenders[].fallback.filePath`: path to the generated fallback shell (for example HTML)
-   `outputs.prerenders[].fallback.postponedState`: serialized postponed state used to resume rendering

## 1\. Seed shell + postponed state at build time[](#1-seed-shell--postponed-state-at-build-time)

my-adapter.ts

```
import { readFile } from 'node:fs/promises'
 
async function seedPprEntries(outputs: AdapterOutputs) {
  for (const prerender of outputs.prerenders) {
    const fallback = prerender.fallback
    if (!fallback?.filePath || !fallback.postponedState) continue
 
    const shell = await readFile(fallback.filePath, 'utf8')
    await platformCache.set(prerender.pathname, {
      shell,
      postponedState: fallback.postponedState,
      initialHeaders: fallback.initialHeaders,
      initialStatus: fallback.initialStatus,
      initialRevalidate: fallback.initialRevalidate,
      initialExpiration: fallback.initialExpiration,
    })
  }
}
```

## 2\. Runtime flow: serve cached shell and resume in background[](#2-runtime-flow-serve-cached-shell-and-resume-in-background)

At request time, you can stream a single response that is the concatenation of:

1.  cached HTML shell stream
2.  resumed render stream (generated after invoking `handler` with postponed state)

```
Client
  | GET /ppr-route
  v
Adapter Router
  |
  |-- read cached shell + postponedState ---> Platform Cache
  |<------------- cache hit -----------------|
  |
  |-- create responseStream = concat(shellStream, resumedStream)
  |
  |-- start piping shellStream ------------> Client (first bytes)
  |
  |-- invoke handler(req, res, { requestMeta: { postponed } })
  |   -------------------------------------> Entrypoint (handler)
  |   <------------------------------------- resumed chunks/cache entry
  |
  |-- append resumed chunks to resumedStream
  |
  '-- client receives one HTTP response:
      [shell bytes........][resumed bytes........]
```

## 3\. Update cache with `requestMeta.onCacheEntryV2`[](#3-update-cache-with-requestmetaoncacheentryv2)

`requestMeta.onCacheEntryV2` is called when a response cache entry is looked up or generated. Use it to persist updated shell/postponed data.

-   `requestMeta.onCacheEntry` still works, but is deprecated.
-   Prefer `requestMeta.onCacheEntryV2`.
-   If your adapter uses an internal `onCacheCallback` abstraction, wire it to `requestMeta.onCacheEntryV2`.

my-adapter.ts

```
await handler(req, res, {
  waitUntil,
  requestMeta: {
    postponed: cachedPprEntry?.postponedState,
    onCacheEntryV2: async (cacheEntry, meta) => {
      if (cacheEntry.value?.kind === 'APP_PAGE') {
        const html =
          cacheEntry.value.html &&
          typeof cacheEntry.value.html.toUnchunkedString === 'function'
            ? cacheEntry.value.html.toUnchunkedString()
            : null
 
        await platformCache.set(meta.url || req.url || '/', {
          shell: html,
          postponedState: cacheEntry.value.postponed,
          headers: cacheEntry.value.headers,
          status: cacheEntry.value.status,
          cacheControl: cacheEntry.cacheControl,
        })
      }
 
      // Return true only if your adapter already wrote the response itself.
      return false
    },
  },
})
```

```
Entrypoint (handler)
  | onCacheEntryV2(cacheEntry, { url })
  v
requestMeta.onCacheEntryV2 callback
  |
  |-- if APP_PAGE ---> persist html + postponedState + headers ---> Platform Cache
  |
  '-- return false: continue normal Next.js response flow
      return true:  adapter already handled response (short-circuit)
```

Was this helpful?
