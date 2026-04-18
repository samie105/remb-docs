---
title: "Fetch - Deno documentation"
source: "https://docs.deno.com/api/deno/fetch"
canonical_url: "https://docs.deno.com/api/deno/fetch"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-18T17:08:56.163Z"
content_hash: "ba9a1744e19d4f1fd967102c873e54b2c3526fe58c2b72bde3d2b56b06039977"
menu_path: ["Fetch - Deno documentation"]
section_path: []
nav_prev: {"path": "deno/deno/api/deno/errors/index.md", "title": "Errors - Deno documentation"}
nav_next: {"path": "deno/deno/api/deno/ffi/index.md", "title": "FFI - Deno documentation"}
---

### Classes [#](#Classes)

c

[Deno.HttpClient](./././~/Deno.HttpClient "Deno.HttpClient")

A custom `HttpClient` for use with `fetch` function. This is designed to allow custom certificates or proxies to be used with `fetch()`.

*   [close](./././~/Deno.HttpClient#method_close_0)

### Functions [#](#Functions)

f

[Deno.createHttpClient](./././~/Deno.createHttpClient "Deno.createHttpClient")

Create a custom HttpClient to use with `fetch`. This is an extension of the web platform Fetch API which allows Deno to use custom TLS CA certificates and connect via a proxy while using `fetch()`.

### Interfaces [#](#Interfaces)

I

[Deno.BasicAuth](./././~/Deno.BasicAuth "Deno.BasicAuth")

Basic authentication credentials to be used with a [`Deno.Proxy`](./././~/Deno.Proxy) server when specifying [`Deno.CreateHttpClientOptions`](./././~/Deno.CreateHttpClientOptions).

*   [password](./././~/Deno.BasicAuth#property_password)
*   [username](./././~/Deno.BasicAuth#property_username)

I

[Deno.CreateHttpClientOptions](./././~/Deno.CreateHttpClientOptions "Deno.CreateHttpClientOptions")

The options used when creating a [`Deno.HttpClient`](./././~/Deno.HttpClient).

*   [allowHost](./././~/Deno.CreateHttpClientOptions#property_allowhost)
*   [caCerts](./././~/Deno.CreateHttpClientOptions#property_cacerts)
*   [http1](./././~/Deno.CreateHttpClientOptions#property_http1)
*   [http2](./././~/Deno.CreateHttpClientOptions#property_http2)
*   [localAddress](./././~/Deno.CreateHttpClientOptions#property_localaddress)
*   [poolIdleTimeout](./././~/Deno.CreateHttpClientOptions#property_poolidletimeout)
*   [poolMaxIdlePerHost](./././~/Deno.CreateHttpClientOptions#property_poolmaxidleperhost)
*   [proxy](./././~/Deno.CreateHttpClientOptions#property_proxy)

### Type Aliases [#](<#Type Aliases>)

T

[Deno.Proxy](./././~/Deno.Proxy "Deno.Proxy")

The definition for alternative transports (or proxies) in [`Deno.CreateHttpClientOptions`](./././~/Deno.CreateHttpClientOptions).
