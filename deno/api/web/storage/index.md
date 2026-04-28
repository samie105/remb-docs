---
title: "Storage - Web documentation"
source: "https://docs.deno.com/api/web/storage"
canonical_url: "https://docs.deno.com/api/web/storage"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T18:00:18.482Z"
content_hash: "34c29169fb56bf51d54936db18362cf38077884395aac91545f9050ea7956f57"
menu_path: ["Storage - Web documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/api/web/platform/index.md", "title": "Platform - Web documentation"}
nav_next: {"path": "deno/api/web/streams/index.md", "title": "Streams - Web documentation"}
---

I

v

[Storage](./././~/Storage "Storage")

This Web Storage API interface provides access to a particular domain's session or local storage. It allows, for example, the addition, modification, or deletion of stored data items.

-   [clear](./././~/Storage#method_clear_0)
-   [getItem](./././~/Storage#method_getitem_0)
-   [key](./././~/Storage#method_key_0)
-   [length](./././~/Storage#property_length)
-   [prototype](./././~/Storage#property_prototype)
-   [removeItem](./././~/Storage#method_removeitem_0)
-   [setItem](./././~/Storage#method_setitem_0)

v

[localStorage](./././~/localStorage "localStorage")

Deno's `localStorage` API provides a way to store key-value pairs in a web-like environment, similar to the Web Storage API found in browsers. It allows developers to persist data across sessions in a Deno application. This API is particularly useful for applications that require a simple and effective way to store data locally.

v

[sessionStorage](./././~/sessionStorage "sessionStorage")

Deno's `sessionStorage` API operates similarly to the [`localStorage`](./././~/localStorage) API, but it is intended for storing data temporarily for the duration of a session. Data stored in sessionStorage is cleared when the application session or process ends. This makes it suitable for temporary data that you do not need to persist across user sessions.
