---
title: "Set up a tRPC Client"
source: "https://trpc.io/docs/v10/client/vanilla/setup"
canonical_url: "https://trpc.io/docs/v10/client/vanilla/setup"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:34:56.112Z"
content_hash: "fac0ae57e4e54aa0cc08140812bb4b888e876969af353fbc62f8095ab0eb5d4c"
menu_path: ["Set up a tRPC Client"]
section_path: []
nav_prev: {"path": "trpc/docs/v10/client/vanilla/aborting-procedure-calls/index.md", "title": "Aborting Procedure Calls"}
nav_next: {"path": "trpc/docs/v10/client/vanilla/infer-types/index.md", "title": "Inferring Types"}
---

### 1\. Install the tRPC Client library[​](#1-install-the-trpc-client-library "Direct link to 1. Install the tRPC Client library")

Use your preferred package manager to install the `@trpc/client` library, and also install `@trpc/server` which contains some required types.

*   npm
*   yarn
*   pnpm
*   bun

bash

`npm install @trpc/client @trpc/server`

bash

`npm install @trpc/client @trpc/server`

### 2\. Import your App Router[​](#2-import-your-app-router "Direct link to 2. Import your App Router")

Import your `AppRouter` type into the client application. This type holds the shape of your entire API.

ts

`import type { AppRouter } from '../server/router';`

tip

By using `import type` you ensure that the reference will be stripped at compile-time, meaning you don't inadvertently import server-side code into your client. For more information, [see the Typescript docs](https://www.typescriptlang.org/docs/handbook/release-notes/typescript-3-8.html#type-only-imports-and-export).

### 3\. Initialize the tRPC client[​](#3-initialize-the-trpc-client "Direct link to 3. Initialize the tRPC client")

Create a tRPC client with the `createTRPCProxyClient` method, and add a `links` array with a [terminating link](trpc/docs/v10/client/links/index.md#the-terminating-link) pointing at your API. To learn more about tRPC links, [click here](trpc/docs/v10/client/links/index.md).

client.ts

ts

`import { createTRPCProxyClient, httpBatchLink } from '@trpc/client';`

`import type { AppRouter } from '../path/to/server/trpc';`

`const client = createTRPCProxyClient<AppRouter>({`

  `links: [`

    `httpBatchLink({`

      `url: 'http://localhost:3000/trpc',`

      `// You can pass any HTTP headers you wish here`

      `async headers() {`

        `return {`

          `authorization: getAuthCookie(),`

        `};`

      `},`

    `}),`

  `],`

`});`

### 4\. Use the tRPC Client[​](#4-use-the-trpc-client "Direct link to 4. Use the tRPC Client")

Under the hood this creates a typed [JavaScript Proxy](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Proxy) which allows you to interact with your tRPC API in a fully type-safe way:

client.ts

ts

`const bilbo = await client.getUser.query('id_bilbo');`

`// => { id: 'id_bilbo', name: 'Bilbo' };`

`const frodo = await client.createUser.mutate({ name: 'Frodo' });`

`// => { id: 'id_frodo', name: 'Frodo' };`

You're all set!

