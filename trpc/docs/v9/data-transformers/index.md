---
title: "Data Transformers"
source: "https://trpc.io/docs/v9/data-transformers"
canonical_url: "https://trpc.io/docs/v9/data-transformers"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:41.945Z"
content_hash: "fb5b36fac612eab40eca03d9f8b00353f9920540a5610d1213d7c3e303e00ad9"
menu_path: ["Data Transformers"]
section_path: []
---
You are able to serialize the response data & input args. The transformers need to be added both to the server and the client.

## Using [superjson](https://github.com/blitz-js/superjson)[​](#using-superjson "Direct link to using-superjson")

SuperJSON allows us to transparently use e.g. standard `Date`/`Map`/`Set`s over the wire between the server and client. That means you can return any of these types in your API-resolver and use them in the client without recreating the objects from JSON.

### How to[​](#how-to "Direct link to How to")

#### 1\. Install[​](#1-install "Direct link to 1. Install")

bash

`yarn add superjson`

#### 2\. Add to `createTRPCCLient()` or `withTRPC()` config[​](#2-add-to-createtrpcclient-or-withtrpc-config "Direct link to 2-add-to-createtrpcclient-or-withtrpc-config")

client.ts

ts

`import superjson from 'superjson';`

`// [...]`

`export const client = createTRPCClient<AppRouter>({`

  `// [...]`

  `transformer: superjson,`

`});`

pages/\_app.tsx

ts

`import superjson from 'superjson';`

`// [...]`

`export default withTRPC<AppRouter>({`

  `config(config) {`

    `return {`

      `// [...]`

      `transformer: superjson,`

    `};`

  `},`

`})(MyApp);`

#### 3\. Add to your `AppRouter`[​](#3-add-to-your-approuter "Direct link to 3-add-to-your-approuter")

server/routers/\_app.ts

ts

`import * as trpc from '@trpc/server';`

`import superjson from 'superjson';`

`export const appRouter = trpc.router().transformer(superjson);`

`// .query(...)`

## Different transformers for upload and download[​](#different-transformers-for-upload-and-download "Direct link to Different transformers for upload and download")

If a transformer should only be used for one direction or different transformers should be used for upload and download (e.g. for performance reasons), you can provide individual transformers for upload and download. Make sure you use the same combined transformer everywhere.

### How to[​](#how-to-1 "Direct link to How to")

Here [superjson](https://github.com/blitz-js/superjson) is used for uploading and [devalue](https://github.com/Rich-Harris/devalue) for downloading data, because devalue is a lot faster but insecure to use on the server.

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

    ``deserialize: (object) => eval(`(${object})`),``

  `},`

`};`

#### 3\. Add to `createTRPCCLient()`[​](#3-add-to-createtrpcclient "Direct link to 3-add-to-createtrpcclient")

client.ts

ts

`import { transformer } from '../utils/trpc';`

`// [...]`

`export const client = createTRPCClient<AppRouter>({`

  `// [...]`

  `transformer: transformer,`

`});`

#### 4\. Add to your `AppRouter`[​](#4-add-to-your-approuter "Direct link to 4-add-to-your-approuter")

server/routers/\_app.ts

ts

`import * as trpc from '@trpc/server';`

`import { transformer } from '../../utils/trpc';`

`export const appRouter = trpc.router().transformer(transformer);`

`// .query(...)`

## `DataTransformer` interface[​](#datatransformer-interface "Direct link to datatransformer-interface")

ts

`type DataTransformer = {`

  `serialize(object: any): any;`

  `deserialize(object: any): any;`

`};`

`type CombinedDataTransformer = {`

  `input: DataTransformer;`

  `output: DataTransformer;`

`};`
