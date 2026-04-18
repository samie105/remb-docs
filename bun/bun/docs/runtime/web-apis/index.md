---
title: "Web APIs"
source: "https://bun.com/docs/runtime/web-apis"
canonical_url: "https://bun.com/docs/runtime/web-apis"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:02:02.162Z"
content_hash: "076ae0d6770ef6f993d146a0bdbf724882be1aa450b719cc45783e4a63e1d057"
menu_path: ["Web APIs"]
section_path: []
nav_prev: {"path": "bun/bun/docs/runtime/watch-mode/index.md", "title": "Watch Mode"}
nav_next: {"path": "bun/bun/docs/runtime/utils/index.md", "title": "Utils"}
---

[Skip to main content](#content-area)

[Bun home page![light logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-dark.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=3f55cd23822028e40658b192c927f3e4)![dark logo](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/logo/logo-with-wordmark-light.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=8a0c5928d9dc3631f0d33e17c257e2ec)](/docs)

[Runtime

](/docs)[Package Manager

](/docs/pm/cli/install)[Bundler

](/docs/bundler)[Test Runner

](/docs/test)[Guides

](/docs/guides)[Reference

](https://bun.com/reference)[Blog

](https://bun.com/blog)[Feedback

](/docs/feedback)

Some Web APIs aren’t relevant in the context of a server-first runtime like Bun, such as the [DOM API](https://developer.mozilla.org/en-US/docs/Web/API/HTML_DOM_API#html_dom_api_interfaces) or [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API). Many others, though, are broadly useful outside of the browser context; when possible, Bun implements these Web-standard APIs instead of introducing new APIs. The following Web APIs are partially or completely supported.

Category

APIs

HTTP

[`fetch`](https://developer.mozilla.org/en-US/docs/Web/API/fetch), [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response), [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request), [`Headers`](https://developer.mozilla.org/en-US/docs/Web/API/Headers), [`AbortController`](https://developer.mozilla.org/en-US/docs/Web/API/AbortController), [`AbortSignal`](https://developer.mozilla.org/en-US/docs/Web/API/AbortSignal)

URLs

[`URL`](https://developer.mozilla.org/en-US/docs/Web/API/URL), [`URLSearchParams`](https://developer.mozilla.org/en-US/docs/Web/API/URLSearchParams)

Web Workers

[`Worker`](https://developer.mozilla.org/en-US/docs/Web/API/Worker), [`self.postMessage`](https://developer.mozilla.org/en-US/docs/Web/API/DedicatedWorkerGlobalScope/postMessage), [`structuredClone`](https://developer.mozilla.org/en-US/docs/Web/API/structuredClone), [`MessagePort`](https://developer.mozilla.org/en-US/docs/Web/API/MessagePort), [`MessageChannel`](https://developer.mozilla.org/en-US/docs/Web/API/MessageChannel), [`BroadcastChannel`](https://developer.mozilla.org/en-US/docs/Web/API/BroadcastChannel)

Streams

[`ReadableStream`](https://developer.mozilla.org/en-US/docs/Web/API/ReadableStream), [`WritableStream`](https://developer.mozilla.org/en-US/docs/Web/API/WritableStream), [`TransformStream`](https://developer.mozilla.org/en-US/docs/Web/API/TransformStream), [`ByteLengthQueuingStrategy`](https://developer.mozilla.org/en-US/docs/Web/API/ByteLengthQueuingStrategy), [`CountQueuingStrategy`](https://developer.mozilla.org/en-US/docs/Web/API/CountQueuingStrategy) and associated classes

Blob

[`Blob`](https://developer.mozilla.org/en-US/docs/Web/API/Blob)

WebSockets

[`WebSocket`](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket)

Encoding and decoding

[`atob`](https://developer.mozilla.org/en-US/docs/Web/API/atob), [`btoa`](https://developer.mozilla.org/en-US/docs/Web/API/btoa), [`TextEncoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextEncoder), [`TextDecoder`](https://developer.mozilla.org/en-US/docs/Web/API/TextDecoder)

JSON

[`JSON`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/JSON)

Timeouts

[`setTimeout`](https://developer.mozilla.org/en-US/docs/Web/API/setTimeout), [`clearTimeout`](https://developer.mozilla.org/en-US/docs/Web/API/clearTimeout)

Intervals

[`setInterval`](https://developer.mozilla.org/en-US/docs/Web/API/setInterval), [`clearInterval`](https://developer.mozilla.org/en-US/docs/Web/API/clearInterval)

Crypto

[`crypto`](https://developer.mozilla.org/en-US/docs/Web/API/Crypto), [`SubtleCrypto`](https://developer.mozilla.org/en-US/docs/Web/API/SubtleCrypto), [`CryptoKey`](https://developer.mozilla.org/en-US/docs/Web/API/CryptoKey)

Debugging

[`console`](https://developer.mozilla.org/en-US/docs/Web/API/console), [`performance`](https://developer.mozilla.org/en-US/docs/Web/API/Performance)

Microtasks

[`queueMicrotask`](https://developer.mozilla.org/en-US/docs/Web/API/queueMicrotask)

Errors

[`reportError`](https://developer.mozilla.org/en-US/docs/Web/API/reportError)

User interaction

[`alert`](https://developer.mozilla.org/en-US/docs/Web/API/Window/alert), [`confirm`](https://developer.mozilla.org/en-US/docs/Web/API/Window/confirm), [`prompt`](https://developer.mozilla.org/en-US/docs/Web/API/Window/prompt) (intended for interactive CLIs)

Realms

[`ShadowRealm`](https://github.com/tc39/proposal-shadowrealm)

Events

[`EventTarget`](https://developer.mozilla.org/en-US/docs/Web/API/EventTarget), [`Event`](https://developer.mozilla.org/en-US/docs/Web/API/Event), [`ErrorEvent`](https://developer.mozilla.org/en-US/docs/Web/API/ErrorEvent), [`CloseEvent`](https://developer.mozilla.org/en-US/docs/Web/API/CloseEvent), [`MessageEvent`](https://developer.mozilla.org/en-US/docs/Web/API/MessageEvent)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/web-apis.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/web-apis>)

[

Bun APIs

Previous

](/docs/runtime/bun-apis)[

Node.js Compatibility

Next

](/docs/runtime/nodejs-compat)


