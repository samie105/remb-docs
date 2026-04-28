---
title: "@std/http"
source: "https://docs.deno.com/runtime/reference/std/http/"
canonical_url: "https://docs.deno.com/runtime/reference/std/http/"
docset: "deno"
kind: "language"
adapter: "generic"
last_crawled_at: "2026-04-27T17:43:18.849Z"
content_hash: "2baa9e84ea8896c3c8b208f8750b966f5eda83204cb1fe528f939bf6fd57ddf2"
menu_path: ["@std/http"]
section_path: []
content_language: "en"
nav_prev: {"path": "deno/runtime/reference/std/html/index.md", "title": "@std/html"}
nav_next: {"path": "deno/runtime/reference/std/ini/index.md", "title": "@std/ini"}
---

**On this page**

-   [Overview](#overview)
    -   [Add to your project](#add-to-your-project)

## Overview

Provides user-friendly `serve` on top of Deno's native HTTP server and other utilities for creating HTTP servers and clients.

## File Server

A small program for serving local files over HTTP.

```js
deno run --allow-net --allow-read jsr:@std/http/file-server
Listening on:
- Local: http://localhost:8000
```

When the `--allow-sys=networkInterfaces` permission is provided, the file server will also display the local area network addresses that can be used to access the server.

## HTTP Status Code and Status Text

Helper for processing status code and status text.

## HTTP errors

Provides error classes for each HTTP error status code as well as utility functions for handling HTTP errors in a structured way.

## Methods

Provides helper functions and types to work with HTTP method strings safely.

## Negotiation

A set of functions which can be used to negotiate content types, encodings and languages when responding to requests.

> Note: some libraries include accept charset functionality by analyzing the `Accept-Charset` header. This is a legacy header that [clients omit and servers should ignore](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Accept-Charset) therefore is not provided.

## User agent handling

The [`UserAgent`](https://jsr.io/@std/http@1.1.0/doc/~/UserAgent) class provides user agent string parsing, allowing a user agent flag to be semantically understood.

For example to integrate the user agent provided in the header `User-Agent` in an http request would look like this:

```js
import { UserAgent } from "@std/http/user-agent";

Deno.serve((req) => {
  const userAgent = new UserAgent(req.headers.get("user-agent") ?? "");
  return new Response(`Hello, ${userAgent.browser.name}
    on ${userAgent.os.name} ${userAgent.os.version}!`);
});
```

### Routing

`route` provides an easy way to route requests to different handlers based on the request path and method.

```js
import { route, type Route } from "@std/http/unstable-route";
import { serveDir } from "@std/http/file-server";

const routes: Route[] = [
  {
    pattern: new URLPattern({ pathname: "/about" }),
    handler: () => new Response("About page"),
  },
  {
    pattern: new URLPattern({ pathname: "/users/:id" }),
    handler: (_req, _info, params) => new Response(params?.pathname.groups.id),
  },
  {
    pattern: new URLPattern({ pathname: "/static/*" }),
    handler: (req: Request) => serveDir(req)
  },
  {
    method: ["GET", "HEAD"],
    pattern: new URLPattern({ pathname: "/api" }),
    handler: (req: Request) => new Response(req.method === 'HEAD' ? null : 'ok'),
  },
];

function defaultHandler(_req: Request) {
  return new Response("Not found", { status: 404 });
}

Deno.serve(route(routes, defaultHandler));
```

### Add to your project

\>\_

```sh
deno add jsr:@std/http
```

[See all symbols in @std/http on](https://jsr.io/@std/http/doc)
