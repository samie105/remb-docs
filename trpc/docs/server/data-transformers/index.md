---
title: "Data Transformers"
source: "https://trpc.io/docs/server/data-transformers"
canonical_url: "https://trpc.io/docs/server/data-transformers"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:47.271Z"
content_hash: "42c620d418c1fe4428e13e57339e7d7289fcd90fe35579806d1fc2c5a8bd476b"
menu_path: ["Data Transformers"]
section_path: []
nav_prev: {"path": "trpc/docs/server/context/index.md", "title": "Context"}
nav_next: {"path": "trpc/docs/server/error-formatting/index.md", "title": "Error Formatting"}
---

You are able to serialize the response data & input args. The transformers need to be added both to the server and the client.

## Using [superjson](https://github.com/blitz-js/superjson)[​](#using-superjson "Direct link to using-superjson")

SuperJSON allows us to transparently use, e.g., standard `Date`/`Map`/`Set`s over the wire between the server and client. That is, you can return any of these types from your API-resolver and use them in the client without having to recreate the objects from JSON.

### How to[​](#how-to "Direct link to How to")

#### 1\. Install[​](#1-install "Direct link to 1. Install")

bash

`yarn add superjson`

#### 2\. Add to your `initTRPC`[​](#2-add-to-your-inittrpc "Direct link to 2-add-to-your-inittrpc")

server/routers/\_app.ts

ts

`import { initTRPC } from '@trpc/server';`

`import superjson from 'superjson';`

`export const t = initTRPC.create({`

  `transformer: superjson,`

`});`

#### 3\. Add to `httpLink()`, `wsLink()`, etc[​](#3-add-to-httplink-wslink-etc "Direct link to 3-add-to-httplink-wslink-etc")

> TypeScript will guide you to where you need to add `transformer` as soon as you've added it on the `initTRPC`\-object

`createTRPCClient()`:

src/app/\_trpc/client.ts

ts

`import { createTRPCClient, httpLink } from '@trpc/client';`

`import type { AppRouter } from './server';`

`import superjson from 'superjson';`

`export const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpLink({`

      `url: 'http://localhost:3000',`

      `transformer: superjson,`

    `}),`

  `],`

`});`

## Using [devalue](https://github.com/Rich-Harris/devalue)[​](#using-devalue "Direct link to using-devalue")

Devalue works like superjson, focusing on performance and compact payloads, but at the cost of a less human-readable body.

### How to[​](#how-to-1 "Direct link to How to")

#### 1\. Install[​](#1-install-1 "Direct link to 1. Install")

bash

`yarn add devalue`

#### 2\. Add to `utils/trpc.ts`[​](#2-add-to-utilstrpcts "Direct link to 2-add-to-utilstrpcts")

Here we use `parse` and `stringify` as they [mitigate XSS](https://github.com/Rich-Harris/devalue?tab=readme-ov-file#xss-mitigation).

utils/trpc.ts

ts

`import { parse, stringify } from 'devalue';`

`// [...]`

`export const transformer = {`

  `deserialize: (object: any) => parse(object),`

  `serialize: (object: any) => stringify(object),`

`};`

#### 3\. Add to your `initTRPC`[​](#3-add-to-your-inittrpc "Direct link to 3-add-to-your-inittrpc")

server/routers/\_app.ts

ts

`import { initTRPC } from '@trpc/server';`

`import { transformer } from '../../utils/trpc';`

`export const t = initTRPC.create({`

  `transformer,`

`});`

#### 4\. Add to `httpLink()`, `wsLink()`, etc[​](#4-add-to-httplink-wslink-etc "Direct link to 4-add-to-httplink-wslink-etc")

> TypeScript will guide you to where you need to add `transformer` as soon as you've added it on the `initTRPC`\-object

`createTRPCClient()`:

src/app/\_trpc/client.ts

ts

`import { createTRPCClient, httpLink } from '@trpc/client';`

`import type { AppRouter } from './server/routers/_app';`

`import { transformer } from './utils/trpc';`

`export const client = createTRPCClient<AppRouter>({`

  `links: [`

    `httpLink({`

      `url: 'http://localhost:3000',`

      `transformer,`

    `}),`

  `],`

`});`

## Different transformers for upload and download[​](#different-transformers-for-upload-and-download "Direct link to Different transformers for upload and download")

If a transformer should only be used for one direction or different transformers should be used for upload and download (e.g., for performance reasons), you can provide individual transformers for upload and download. Make sure you use the same combined transformer everywhere.

## `DataTransformer` interface[​](#datatransformer-interface "Direct link to datatransformer-interface")

ts

`export interface DataTransformer {`

  `serialize(object: any): any;`

  `deserialize(object: any): any;`

`}`

`interface InputDataTransformer extends DataTransformer {`

  `/**`

   `* This function runs **on the client** before sending the data to the server.`

   `*/`

  `serialize(object: any): any;`

  `/**`

   `* This function runs **on the server** to transform the data before it is passed to the resolver`

   `*/`

  `deserialize(object: any): any;`

`}`

`interface OutputDataTransformer extends DataTransformer {`

  `/**`

   `* This function runs **on the server** before sending the data to the client.`

   `*/`

  `serialize(object: any): any;`

  `/**`

   `* This function runs **only on the client** to transform the data sent from the server.`

   `*/`

  `deserialize(object: any): any;`

`}`

`export interface CombinedDataTransformer {`

  `/**`

   `* Specify how the data sent from the client to the server should be transformed.`

   `*/`

  `input: InputDataTransformer;`

  `/**`

   `* Specify how the data sent from the server to the client should be transformed.`

   `*/`

  `output: OutputDataTransformer;`

`}`
