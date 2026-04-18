---
title: "Data Transformers"
source: "https://trpc.io/docs/v10/server/data-transformers"
canonical_url: "https://trpc.io/docs/v10/server/data-transformers"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:57.638Z"
content_hash: "70e6ac7fd38ff68bc5f017a7d125ae10900922752433c4c517252a3907da83ab"
menu_path: ["Data Transformers"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/server/caching/index.md", "title": "Response Caching"}
nav_next: {"path": "trpc/docs/v10/server/context/index.md", "title": "Context"}
---

You are able to serialize the response data & input args. The transformers need to be added both to the server and the client.

## Using [superjson](https://github.com/blitz-js/superjson)[​](#using-superjson "Direct link to using-superjson")

SuperJSON allows us to transparently use, e.g., standard `Date`/`Map`/`Set`s over the wire between the server and client. That is, you can return any of these types from your API-resolver and use them in the client without having to recreate the objects from JSON.

### How to[​](#how-to "Direct link to How to")

#### 1\. Install[​](#1-install "Direct link to 1. Install")

bash

`yarn add superjson`

#### 2\. Add to your `initTRPC`[​](#2-add-to-your-inittrpc "Direct link to 2-add-to-your-inittrpc")

routers/router/\_app.ts

ts

`import { initTRPC } from '@trpc/server';`

`import superjson from 'superjson';`

`export const t = initTRPC.create({`

  `transformer: superjson,`

`});`

#### 3\. Add to `createTRPCProxyClient()` or `createTRPCNext()`[​](#3-add-to-createtrpcproxyclient-or-createtrpcnext "Direct link to 3-add-to-createtrpcproxyclient-or-createtrpcnext")

ts

`import { createTRPCProxyClient } from '@trpc/client';`

`import type { AppRouter } from '~/server/routers/_app';`

`import superjson from 'superjson';`

`export const client = createTRPCProxyClient<AppRouter>({`

  `transformer: superjson, // <--`

  `// [...]`

`});`

utils/trpc.ts

ts

`import { createTRPCNext } from '@trpc/next';`

`import type { AppRouter } from '~/server/routers/_app';`

`import superjson from 'superjson';`

`// [...]`

`export const trpc = createTRPCNext<AppRouter>({`

  `config(config) {`

    `return {`

      `transformer: superjson, // <--`

    `};`

  `},`

  `// [...]`

`});`

## Different transformers for upload and download[​](#different-transformers-for-upload-and-download "Direct link to Different transformers for upload and download")

If a transformer should only be used for one direction or different transformers should be used for upload and download (e.g., for performance reasons), you can provide individual transformers for upload and download. Make sure you use the same combined transformer everywhere.

### How to[​](#how-to-1 "Direct link to How to")

Here [superjson](https://github.com/blitz-js/superjson) is used for uploading and [devalue](https://github.com/Rich-Harris/devalue) for downloading data because devalue is a lot faster but insecure to use on the server.

#### 1\. Install[​](#1-install-1 "Direct link to 1. Install")

bash

`yarn add superjson devalue`

#### 2\. Add to `utils/trpc.ts`[​](#2-add-to-utilstrpcts "Direct link to 2-add-to-utilstrpcts")

utils/trpc.ts

ts

`import { uneval } from 'devalue';`

`import superjson from 'superjson';`

`// [...]`

`export const transformer = {`

  `input: superjson,`

  `output: {`

    `serialize: (object) => uneval(object),`

    ``// This `eval` only ever happens on the **client**.``

    ``deserialize: (object) => (0, eval)(`(${object})`),``

  `},`

`};`

#### 3\. Add to your `AppRouter`[​](#3-add-to-your-approuter "Direct link to 3-add-to-your-approuter")

server/routers/\_app.ts

ts

`import { initTRPC } from '@trpc/server';`

`import { transformer } from '../../utils/trpc';`

`export const t = initTRPC.create({`

  `transformer,`

`});`

`export const appRouter = t.router({`

  `// [...]`

`});`

#### 4\. Add to `createTRPCProxyClient()`[​](#4-add-to-createtrpcproxyclient "Direct link to 4-add-to-createtrpcproxyclient")

client.ts

ts

`import { createTRPCProxyClient } from '@trpc/client';`

`import { transformer } from '../utils/trpc';`

`export const client = createTRPCProxyClient<AppRouter>({`

  `transformer, // <--`

  `// [...]`

`});`

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


