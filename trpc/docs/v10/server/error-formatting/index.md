---
title: "Error Formatting"
source: "https://trpc.io/docs/v10/server/error-formatting"
canonical_url: "https://trpc.io/docs/v10/server/error-formatting"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:15.423Z"
content_hash: "2377d7dce3158d2f0ebc955c7995bea501cf7a8c024b22f36d60547cd9af44d5"
menu_path: ["Error Formatting"]
section_path: []
nav_prev: {"path": "../data-transformers/index.md", "title": "Data Transformers"}
nav_next: {"path": "../error-handling/index.md", "title": "Error Handling"}
---

The error formatting in your router will be inferred all the way to your client (& React components)

## Usage example highlighted[​](#usage-example-highlighted "Direct link to Usage example highlighted")

### Adding custom formatting[​](#adding-custom-formatting "Direct link to Adding custom formatting")

server.ts

ts

`import { initTRPC } from '@trpc/server';`

`export const t = initTRPC.context<Context>().create({`

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

> Since `v8.x` tRPC is compliant with [JSON-RPC 2.0](https://www.jsonrpc.org/specification)

ts

`{`

  `error: TRPCError;`

  `type: ProcedureType | 'unknown';`

  `path: string | undefined;`

  `input: unknown;`

  `ctx: undefined | TContext;`

  `shape: DefaultErrorShape; // the default error shape`

`}`

**`DefaultErrorShape`:**

ts

`interface DefaultErrorData {`

  `code: TRPC_ERROR_CODE_KEY;`

  `httpStatus: number;`

  `path?: string;`

  `stack?: string;`

`}`

`interface DefaultErrorShape`

  `extends TRPCErrorShape<TRPC_ERROR_CODE_NUMBER, DefaultErrorData> {`

  `message: string;`

  `code: TRPC_ERROR_CODE_NUMBER;`

`}`
