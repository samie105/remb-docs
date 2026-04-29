---
title: "Error Handling"
source: "https://bun.com/docs/runtime/http/error-handling"
canonical_url: "https://bun.com/docs/runtime/http/error-handling"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:00:01.690Z"
content_hash: "a6cb6ae05af725fb6136c815ffbc5efa454148fdccc009878f5a737cfad9c3e5"
menu_path: ["Error Handling"]
section_path: []
nav_prev: {"path": "../cookies/index.md", "title": "Cookies"}
nav_next: {"path": "../metrics/index.md", "title": "Metrics"}
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

To activate development mode, set `development: true`.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)server.ts

```
Bun.serve({
  development: true, 
  fetch(req) {
    throw new Error("woops!");
  },
});
```

In development mode, Bun will surface errors in-browser with a built-in error page.

![Bun's built-in 500 page](https://mintcdn.com/bun-1dd33a4e/PY1574V41bdK8wNs/images/exception_page.png?fit=max&auto=format&n=PY1574V41bdK8wNs&q=85&s=26f9bec162e97288f1f0d736773b2b6e)

### 

[​

](#error-callback)

`error` callback

To handle server-side errors, implement an `error` handler. This function should return a `Response` to serve to the client when an error occurs. This response will supersede Bun’s default error page in `development` mode.

```
Bun.serve({
  fetch(req) {
    throw new Error("woops!");
  },
  error(error) {
    return new Response(`<pre>${error}\n${error.stack}</pre>`, {
      headers: {
        "Content-Type": "text/html",
      },
    });
  },
});
```

[Learn more about debugging in Bun](/docs/runtime/debugger)

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/runtime/http/error-handling.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /runtime/http/error-handling>)

[

TLS

Previous

](/docs/runtime/http/tls)[

Metrics

Next

](/docs/runtime/http/metrics)

![Bun's built-in 500 page](https://mintcdn.com/bun-1dd33a4e/PY1574V41bdK8wNs/images/exception_page.png?w=840&fit=max&auto=format&n=PY1574V41bdK8wNs&q=85&s=5c605029819509b6e1dbba7ff684ef4f)
