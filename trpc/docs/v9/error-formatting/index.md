---
title: "Error Formatting"
source: "https://trpc.io/docs/v9/error-formatting"
canonical_url: "https://trpc.io/docs/v9/error-formatting"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:45.072Z"
content_hash: "bfc40210aafb6762d310febe51f1a5e6735b958b31b3b1c20eeeeb80c3203b22"
menu_path: ["Error Formatting"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/data-transformers/index.md", "title": "Data Transformers"}
nav_next: {"path": "trpc/docs/v9/error-handling/index.md", "title": "Error Handling"}
---

The error formatting in your router will be inferred all the way to your client (& React components)

## Usage example highlighted[​](#usage-example-highlighted "Direct link to Usage example highlighted")

### Adding custom formatting[​](#adding-custom-formatting "Direct link to Adding custom formatting")

server.ts

ts

`const router = trpc.router<Context>().formatError(({ shape, error }) => {`

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

`});`

### Usage in React[​](#usage-in-react "Direct link to Usage in React")

components/MyComponent.tsx

tsx

`export function MyComponent() {`

  `const mutation = trpc.useMutation('addPost');`

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

## All properties sent to `formatError()`[​](#all-properties-sent-to-formaterror "Direct link to all-properties-sent-to-formaterror")

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

