---
title: "Error Handling"
source: "https://trpc.io/docs/v9/error-handling"
canonical_url: "https://trpc.io/docs/v9/error-handling"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:41:48.135Z"
content_hash: "00c12781100270571824f3ba73d1514bfa75eba54d2a4aaef6ec5f81b0512998"
menu_path: ["Error Handling"]
section_path: []
nav_prev: {"path": "trpc/docs/v9/error-formatting/index.md", "title": "Error Formatting"}
nav_next: {"path": "trpc/docs/v9/example-apps/index.md", "title": "Example Apps"}
---

Whenever an error occurs in a procedure, tRPC responds to the client with an object that includes an "error" property. This property contains all the information that you need to handle the error in the client.

Here's an example error response caused by a bad request input:

json

`{`

  `"id": null,`

  `"error": {`

    `"message": "\"password\" must be at least 4 characters",`

    `"code": -32600,`

    `"data": {`

      `"code": "BAD_REQUEST",`

      `"httpStatus": 400,`

      `"stack": "...",`

      `"path": "user.changepassword"`

    `}`

  `}`

`}`

## Error codes[​](#error-codes "Direct link to Error codes")

tRPC defines a list of error codes that each represent a different type of error and response with a different HTTP code.

Code

Description

HTTP code

BAD\_REQUEST

The server cannot or will not process the request due to something that is perceived to be a client error.

400

UNAUTHORIZED

The client request has not been completed because it lacks valid authentication credentials for the requested resource.

401

FORBIDDEN

The server was unauthorized to access a required data source, such as a REST API.

403

NOT\_FOUND

The server cannot find the requested resource.

404

TIMEOUT

The server would like to shut down this unused connection.

408

CONFLICT

The server request resource conflict with the current state of the target resource.

409

PRECONDITION\_FAILED

Access to the target resource has been denied.

412

PAYLOAD\_TOO\_LARGE

Request entity is larger than limits defined by server.

413

METHOD\_NOT\_SUPPORTED

The server knows the request method, but the target resource doesn't support this method.

405

CLIENT\_CLOSED\_REQUEST

Access to the resource has been denied.

499

INTERNAL\_SERVER\_ERROR

An unspecified error occurred.

500

## Throwing errors[​](#throwing-errors "Direct link to Throwing errors")

tRPC provides an error subclass, `TRPCError`, which you can use to represent an error that occurred inside a procedure.

For example, throwing this error:

server.ts

ts

`import * as trpc from '@trpc/server';`

`const appRouter = trpc.router().query('hello', {`

  `resolve: () => {`

    `throw new trpc.TRPCError({`

      `code: 'INTERNAL_SERVER_ERROR',`

      `message: 'An unexpected error occurred, please try again later.',`

      `// optional: pass the original error to retain stack trace`

      `cause: theError,`

    `});`

  `},`

`});`

`// [...]`

Results to the following response:

json

`{`

  `"id": null,`

  `"error": {`

    `"message": "An unexpected error occurred, please try again later.",`

    `"code": -32603,`

    `"data": {`

      `"code": "INTERNAL_SERVER_ERROR",`

      `"httpStatus": 500,`

      `"stack": "...",`

      `"path": "hello"`

    `}`

  `}`

`}`

## Handling errors[​](#handling-errors "Direct link to Handling errors")

All errors that occur in a procedure go through the `onError` method before being sent to the client. Here you can handle or change errors.

pages/api/trpc/\[trpc\].ts

ts

`export default trpcNext.createNextApiHandler({`

  `// ...`

  `onError({ error, type, path, input, ctx, req }) {`

    `console.error('Error:', error);`

    `if (error.code === 'INTERNAL_SERVER_ERROR') {`

      `// send to bug reporting`

    `}`

  `},`

`});`

The `onError` parameter is an object that contains all information about the error and the context it occurs in:

ts

`{`

  `error: TRPCError; // the original error`

  `type: 'query' | 'mutation' | 'subscription' | 'unknown';`

  `path: string | undefined; // path of the procedure that was triggered`

  `input: unknown;`

  `ctx: Context | undefined;`

  `req: BaseRequest; // request object`

`}`


