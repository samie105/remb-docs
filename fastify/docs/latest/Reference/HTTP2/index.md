---
title: "HTTP2"
source: "https://fastify.dev/docs/latest/Reference/HTTP2/"
canonical_url: "https://fastify.io/docs/latest/Reference/HTTP2/"
docset: "fastify"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:44.234Z"
content_hash: "1df7b46afe0fa80a225ea8801779b2b5727a56d7e001da8da59033b849fc1616"
menu_path: ["HTTP2"]
section_path: []
nav_prev: {"path": "fastify/docs/latest/Reference/Decorators/index.md", "title": "Decorators"}
nav_next: {"path": "fastify/docs/latest/Reference/LTS/index.md", "title": "LTS"}
---

Version: latest (v5.8.x)

## HTTP2[​](#http2 "Direct link to HTTP2")

_Fastify_ supports HTTP2 over HTTPS (h2) or plaintext (h2c).

Currently, none of the HTTP2-specific APIs are available through _Fastify_, but Node's `req` and `res` can be accessed through the `Request` and `Reply` interfaces. PRs are welcome.

### Secure (HTTPS)[​](#secure-https "Direct link to Secure (HTTPS)")

HTTP2 is supported in all modern browsers **only over a secure connection**:

```
'use strict'const fs = require('node:fs')const path = require('node:path')const fastify = require('fastify')({  http2: true,  https: {    key: fs.readFileSync(path.join(__dirname, '..', 'https', 'fastify.key')),    cert: fs.readFileSync(path.join(__dirname, '..', 'https', 'fastify.cert'))  }})fastify.get('/', function (request, reply) {  reply.code(200).send({ hello: 'world' })})fastify.listen({ port: 3000 })
```

[ALPN negotiation](https://datatracker.ietf.org/doc/html/rfc7301) allows support for both HTTPS and HTTP/2 over the same socket. Node core `req` and `res` objects can be either [HTTP/1](https://nodejs.org/api/http.html) or [HTTP/2](https://nodejs.org/api/http2.html). _Fastify_ supports this out of the box:

```
'use strict'const fs = require('node:fs')const path = require('node:path')const fastify = require('fastify')({  http2: true,  https: {    allowHTTP1: true, // fallback support for HTTP1    key: fs.readFileSync(path.join(__dirname, '..', 'https', 'fastify.key')),    cert: fs.readFileSync(path.join(__dirname, '..', 'https', 'fastify.cert'))  }})// this route can be accessed through both protocolsfastify.get('/', function (request, reply) {  reply.code(200).send({ hello: 'world' })})fastify.listen({ port: 3000 })
```

Test the new server with:

```
$ npx h2url https://localhost:3000
```

### Plain or insecure[​](#plain-or-insecure "Direct link to Plain or insecure")

For microservices, HTTP2 can connect in plain text, but this is not supported by browsers.

```
'use strict'const fastify = require('fastify')({  http2: true})fastify.get('/', function (request, reply) {  reply.code(200).send({ hello: 'world' })})fastify.listen({ port: 3000 })
```

Test the new server with:

```
$ npx h2url http://localhost:3000
```

