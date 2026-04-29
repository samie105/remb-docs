---
title: "Fetch - Deno documentation"
source: "https://docs.deno.com/api/deno/fetch"
canonical_url: "https://docs.deno.com/api/deno/fetch"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:52:13.026Z"
content_hash: "3f977ab7bda04a8fd63fc25e9cb502df8d38d5e4d84dfae51af953f1277d428d"
menu_path: ["Fetch - Deno documentation"]
section_path: []
content_language: "en"
nav_prev: {"path": "../errors/index.md", "title": "Errors - Deno documentation"}
nav_next: {"path": "../ffi/index.md", "title": "FFI - Deno documentation"}
---

c

[Deno.HttpClient](./././~/Deno.HttpClient "Deno.HttpClient")

A custom `HttpClient` for use with `fetch` function. This is designed to allow custom certificates or proxies to be used with `fetch()`.

-   [close](./././~/Deno.HttpClient#method_close_0)

f

[Deno.createHttpClient](./././~/Deno.createHttpClient "Deno.createHttpClient")

Create a custom HttpClient to use with `fetch`. This is an extension of the web platform Fetch API which allows Deno to use custom TLS CA certificates and connect via a proxy while using `fetch()`.

I

[Deno.BasicAuth](./././~/Deno.BasicAuth "Deno.BasicAuth")

Basic authentication credentials to be used with a [`Deno.Proxy`](./././~/Deno.Proxy) server when specifying [`Deno.CreateHttpClientOptions`](./././~/Deno.CreateHttpClientOptions).

-   [password](./././~/Deno.BasicAuth#property_password)
-   [username](./././~/Deno.BasicAuth#property_username)

I

[Deno.CreateHttpClientOptions](./././~/Deno.CreateHttpClientOptions "Deno.CreateHttpClientOptions")

The options used when creating a [`Deno.HttpClient`](./././~/Deno.HttpClient).

-   [allowHost](./././~/Deno.CreateHttpClientOptions#property_allowhost)
-   [caCerts](./././~/Deno.CreateHttpClientOptions#property_cacerts)
-   [http1](./././~/Deno.CreateHttpClientOptions#property_http1)
-   [http2](./././~/Deno.CreateHttpClientOptions#property_http2)
-   [localAddress](./././~/Deno.CreateHttpClientOptions#property_localaddress)
-   [poolIdleTimeout](./././~/Deno.CreateHttpClientOptions#property_poolidletimeout)
-   [poolMaxIdlePerHost](./././~/Deno.CreateHttpClientOptions#property_poolmaxidleperhost)
-   [proxy](./././~/Deno.CreateHttpClientOptions#property_proxy)

T

[Deno.Proxy](./././~/Deno.Proxy "Deno.Proxy")

The definition for alternative transports (or proxies) in [`Deno.CreateHttpClientOptions`](./././~/Deno.CreateHttpClientOptions).
