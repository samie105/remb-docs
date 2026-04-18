---
title: "Error Formatting"
source: "https://trpc.io/docs/server/error-formatting"
canonical_url: "https://trpc.io/docs/server/error-formatting"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:45.271Z"
content_hash: "505dd89e9c1358d799e116f900963c2b048a9d41d5e3c9aeabf28c48e9d97597"
menu_path: ["Error Formatting"]
section_path: []
nav_prev: {"path": "trpc/docs/server/context/index.md", "title": "Context"}
nav_next: {"path": "trpc/docs/server/data-transformers/index.md", "title": "Data Transformers"}
---

The error formatting in your router will be inferred all the way to your client.

## Usage example highlighted[​](#usage-example-highlighted "Direct link to Usage example highlighted")

### Adding custom formatting[​](#adding-custom-formatting "Direct link to Adding custom formatting")

server.ts

ts

`import { initTRPC } from '@trpc/server';`

`import { ZodError } from 'zod';`

`export const t = initTRPC.create({`

  `errorFormatter(opts) {`

    `const { shape, error } = opts;`

    `return {`

      `...shape,`

      `data: {`

        `...shape.data,`

        `zodError:`

          `error.code === 'BAD_REQUEST' && error.cause instanceof ZodError`

            `? error.cause.flatten()`

            `: null,`

      `},`

    `};`

  `},`

`});`

### Usage in React[​](#usage-in-react "Direct link to Usage in React")

components/MyComponent.tsx

tsx

`import { useEffect } from 'react';`

`import { trpc } from '../utils/trpc';`

`export function MyComponent() {`

  `const mutation = trpc.addPost.useMutation();`

  `useEffect(() => {`

    `mutation.mutate({ title: 'example' });`

  `}, []);`

  `if (mutation.error?.data?.zodError) {`

    `// zodError will be inferred`

    `return (`

      `<pre>Error: {JSON.stringify(mutation.error.data.zodError, null, 2)}</pre>`

    `);`

  `}`

  `return <>[...]</>;`

`}`

## All properties sent to `errorFormatter()`[​](#all-properties-sent-to-errorformatter "Direct link to all-properties-sent-to-errorformatter")

> tRPC is compliant with [JSON-RPC 2.0](https://www.jsonrpc.org/specification)

ts

`interface ErrorFormatterOpts {`

  `error: TRPCError;`

  `type: 'query' | 'mutation' | 'subscription' | 'unknown';`

  `path: string | undefined;`

  `input: unknown;`

  `ctx: unknown;`

  `shape: { message: string; code: number; data: unknown };`

`}`

**`DefaultErrorShape`:**

ts

`type DefaultErrorData = {`

  `code: TRPC_ERROR_CODE_KEY;`

  `httpStatus: number;`

  `/**`

   `* Path to the procedure that threw the error`

   `*/`

  `path?: string;`

  `/**`

   `* Stack trace of the error (only in development)`

   `*/`

  `stack?: string;`

`};`

`interface DefaultErrorShape {`

  `message: string;`

  `code: TRPC_ERROR_CODE_NUMBER;`

  `data: DefaultErrorData;`

`}`


