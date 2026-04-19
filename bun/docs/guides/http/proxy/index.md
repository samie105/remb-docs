---
title: "Proxy HTTP requests using fetch()"
source: "https://bun.com/docs/guides/http/proxy"
canonical_url: "https://bun.com/docs/guides/http/proxy"
docset: "bun"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:07.039Z"
content_hash: "384901a16bf56d9ea0f34904c982ea06909d8b0591ed6e8beefbbbd324728211"
menu_path: ["Proxy HTTP requests using fetch()"]
section_path: []
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

In Bun, `fetch` supports sending requests through an HTTP or HTTPS proxy. This is useful on corporate networks or when you need to ensure a request is sent through a specific IP address.

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)proxy.ts

```
await fetch("https://example.com", {
  // The URL of the proxy server
  proxy: "https://username:password@proxy.example.com:8080",
});
```

* * *

The `proxy` option can be a URL string or an object with `url` and optional `headers`. The URL can include the username and password if the proxy requires authentication. It can be `http://` or `https://`.

* * *

## 

[​

](#custom-proxy-headers)

Custom proxy headers

To send custom headers to the proxy server (useful for proxy authentication tokens, custom routing, etc.), use the object format:

![https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z\_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z\_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b](https://mintcdn.com/bun-1dd33a4e/JUhaF6Mf68z_zHyy/icons/typescript.svg?fit=max&auto=format&n=JUhaF6Mf68z_zHyy&q=85&s=7ac549adaea8d5487d8fbd58cc3ea35b)proxy-headers.ts

```
await fetch("https://example.com", {
  proxy: {
    url: "https://proxy.example.com:8080",
    headers: {
      "Proxy-Authorization": "Bearer my-token",
      "X-Proxy-Region": "us-east-1",
    },
  },
});
```

The `headers` property accepts a plain object or a `Headers` instance. These headers are sent directly to the proxy server in `CONNECT` requests (for HTTPS targets) or in the proxy request (for HTTP targets). If you provide a `Proxy-Authorization` header, it will override any credentials specified in the proxy URL.

* * *

## 

[​

](#environment-variables)

Environment variables

You can also set the `$HTTP_PROXY` or `$HTTPS_PROXY` environment variable to the proxy URL. This is useful when you want to use the same proxy for all requests.

terminal

```
HTTPS_PROXY=https://username:password@proxy.example.com:8080 bun run index.ts
```

Was this page helpful?

[Suggest edits](https://github.com/oven-sh/bun/edit/main/docs/guides/http/proxy.mdx)[Raise issue](<https://github.com/oven-sh/bun/issues/new?title=Issue on docs&body=Path: /guides/http/proxy>)

[

Configure TLS on an HTTP server

Previous

](/docs/guides/http/tls)[

Stream a file as an HTTP Response

Next

](/docs/guides/http/stream-file)
