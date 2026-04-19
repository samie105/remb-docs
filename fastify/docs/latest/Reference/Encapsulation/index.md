---
title: "Encapsulation"
source: "https://fastify.dev/docs/latest/Reference/Encapsulation/"
canonical_url: "https://fastify.io/docs/latest/Reference/Encapsulation/"
docset: "fastify"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:32.442Z"
content_hash: "c700cdbf85648113e079d44a46cc5685af88c8c76628e65aac9c9cfb99e15794"
menu_path: ["Encapsulation"]
section_path: []
nav_prev: {"path": "fastify/docs/latest/Reference/Decorators/index.md", "title": "Decorators"}
nav_next: {"path": "fastify/docs/latest/Reference/Errors/index.md", "title": "Errors"}
---

# curl -H 'authorization: Bearer abc123' http://127.0.0.1:8000/one{"answer":42}# curl http://127.0.0.1:8000/two{"answer":42,"foo":"foo"}# curl http://127.0.0.1:8000/three{"answer":42,"foo":"foo","bar":"bar"}
```

## Sharing Between Contexts[​](#sharing-between-contexts "Direct link to Sharing Between Contexts")

Each context in the prior example inherits _only_ from its parent contexts. Parent contexts cannot access entities within their descendant contexts. If needed, encapsulation can be broken using [fastify-plugin](https://github.com/fastify/fastify-plugin), making anything registered in a descendant context available to the parent context.

To allow `publicContext` access to the `bar` decorator in `grandchildContext`, rewrite the code as follows:

```
'use strict'const fastify = require('fastify')()const fastifyPlugin = require('fastify-plugin')fastify.decorateRequest('answer', 42)// `authenticatedContext` omitted for clarityfastify.register(async function publicContext (childServer) {  childServer.decorateRequest('foo', 'foo')  childServer.route({    path: '/two',    method: 'GET',    handler (request, response) {      response.send({        answer: request.answer,        foo: request.foo,        bar: request.bar      })    }  })  childServer.register(fastifyPlugin(grandchildContext))  async function grandchildContext (grandchildServer) {    grandchildServer.decorateRequest('bar', 'bar')    grandchildServer.route({      path: '/three',      method: 'GET',      handler (request, response) {        response.send({          answer: request.answer,          foo: request.foo,          bar: request.bar        })      }    })  }})fastify.listen({ port: 8000 })
```

Restarting the server and re-issuing the requests for `/two` and `/three`:

```
# curl http://127.0.0.1:8000/two{"answer":42,"foo":"foo","bar":"bar"}# curl http://127.0.0.1:8000/three{"answer":42,"foo":"foo","bar":"bar"}
```
