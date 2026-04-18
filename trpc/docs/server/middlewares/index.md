---
title: "Middlewares"
source: "https://trpc.io/docs/server/middlewares"
canonical_url: "https://trpc.io/docs/server/middlewares"
docset: "trpc"
kind: "library"
adapter: "generic"
last_crawled_at: "2026-04-18T16:50:14.172Z"
content_hash: "8eb38615459671aa01d2a55952a4c18df80466cec0570abe407ed704d6e1a8d0"
menu_path: ["Middlewares"]
section_path: []
nav_prev: {"path": "trpc/docs/server/non-json-content-types/index.md", "title": "Content Types"}
nav_next: {"path": "trpc/docs/server/overview/index.md", "title": "Backend Usage"}
---

You can add middleware(s) to a procedure with the `t.procedure.use()` method. The middleware(s) will wrap the invocation of the procedure and must call `opts.next()` and return its result.

In the example below, any call to a `adminProcedure` will ensure that the user is an "admin" before executing.

In the example below timings for queries are logged automatically.

"Context Extension" enables middlewares to dynamically add and override keys on a base procedure's context in a typesafe manner.

Below we have an example of a middleware that changes properties of a context, the changes are then available to all chained consumers, such as other middlewares and procedures:

tRPC has an API called `.concat()` which allows you to independently define a partial procedure that can be used with any tRPC instance that matches the context and metadata of the plugin.

This helper primarily targets creating plugins and libraries with tRPC.

We have a powerful feature called `.pipe()` which allows you to extend middlewares in a typesafe manner.

Below we have an example of a middleware that extends a base middleware(foo). Like the context extension example above, piping middlewares will change properties of the context, and procedures will receive the new context value.

Beware that the order in which you pipe your middlewares matter and that the context must overlap. An example of a forbidden pipe is shown below. Here, the `fooMiddleware` overrides the `ctx.a` while `barMiddleware` still expects the root context from the initialization in `initTRPC` - so piping `fooMiddleware` with `barMiddleware` would not work, while piping `barMiddleware` with `fooMiddleware` does work.

ts

`import { initTRPC } from '@trpc/server';`

`const t = initTRPC`

  `.context<{`

    `a: {`

      `b: 'a';`

    `};`

  `}>()`

  `.create();`

`const fooMiddleware = t.middleware((opts) => {`

  `const { ctx } = opts;`

  ``ctx.a; // 👈 fooMiddleware expects `ctx.a` to be an object``

     `(property) a: {     b: "a"; }`

  `return opts.next({`

    `ctx: {`

      ``a: 'a' as const, // 👈 `ctx.a` is no longer an object``

    `},`

  `});`

`});`

`const barMiddleware = t.middleware((opts) => {`

  `const { ctx } = opts;`

  ``ctx.a; // 👈 barMiddleware expects `ctx.a` to be an object``

     `(property) a: {     b: "a"; }`

  `return opts.next({`

    `ctx: {`

      `foo: 'foo' as const,`

    `},`

  `});`

`});`

`` // ❌ `ctx.a` does not overlap from `fooMiddleware` to `barMiddleware` ``

`fooMiddleware.unstable_pipe(barMiddleware);`

``Argument of type 'MiddlewareBuilder<{ a: { b: "a"; }; }, object, { foo: "foo"; }, unknown>' is not assignable to parameter of type 'MiddlewareFunction<{ a: { b: "a"; }; }, object, { a: "a"; }, { foo: "foo"; }, unknown> | MiddlewareBuilder<{ a: "a"; }, object, { foo: "foo"; }, unknown>'.   Type 'MiddlewareBuilder<{ a: { b: "a"; }; }, object, { foo: "foo"; }, unknown>' is not assignable to type 'MiddlewareBuilder<{ a: "a"; }, object, { foo: "foo"; }, unknown>'.     Types of property 'unstable_pipe' are incompatible.       Type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ a: { b: "a"; }; }, object, { foo: "foo"; }, $ContextOverridesOut, unknown> | MiddlewareBuilder<{ a: { b: "a"; }; foo: "foo"; }, object, $ContextOverridesOut, unknown>) => MiddlewareBuilder<...>' is not assignable to type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ a: "a"; }, object, { foo: "foo"; }, $ContextOverridesOut, unknown> | MiddlewareBuilder<{ a: "a"; foo: "foo"; }, object, $ContextOverridesOut, unknown>) => MiddlewareBuilder<...>'.         Types of parameters 'fn' and 'fn' are incompatible.           Type 'MiddlewareFunction<{ a: "a"; }, object, { foo: "foo"; }, any, unknown> | MiddlewareBuilder<{ a: "a"; foo: "foo"; }, object, any, unknown>' is not assignable to type 'MiddlewareFunction<{ a: { b: "a"; }; }, object, { foo: "foo"; }, any, unknown> | MiddlewareBuilder<{ a: { b: "a"; }; foo: "foo"; }, object, any, unknown>'.             Type 'MiddlewareFunction<{ a: "a"; }, object, { foo: "foo"; }, any, unknown>' is not assignable to type 'MiddlewareFunction<{ a: { b: "a"; }; }, object, { foo: "foo"; }, any, unknown> | MiddlewareBuilder<{ a: { b: "a"; }; foo: "foo"; }, object, any, unknown>'.               Type 'MiddlewareFunction<{ a: "a"; }, object, { foo: "foo"; }, any, unknown>' is not assignable to type 'MiddlewareFunction<{ a: { b: "a"; }; }, object, { foo: "foo"; }, any, unknown>'.                 Types of parameters 'opts' and 'opts' are incompatible.                   Type '{ ctx: { a: { b: "a"; }; foo: "foo"; }; type: "query" | "mutation" | "subscription"; path: string; input: unknown; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }' is not assignable to type '{ ctx: { a: "a"; foo: "foo"; }; type: "query" | "mutation" | "subscription"; path: string; input: unknown; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }'.                     The types of 'ctx.a' are incompatible between these types.                       Type '{ b: "a"; }' is not assignable to type '"a"'.2345Argument of type 'MiddlewareBuilder<{ a: { b: "a"; }; }, object, { foo: "foo"; }, unknown>' is not assignable to parameter of type 'MiddlewareFunction<{ a: { b: "a"; }; }, object, { a: "a"; }, { foo: "foo"; }, unknown> | MiddlewareBuilder<{ a: "a"; }, object, { foo: "foo"; }, unknown>'.   Type 'MiddlewareBuilder<{ a: { b: "a"; }; }, object, { foo: "foo"; }, unknown>' is not assignable to type 'MiddlewareBuilder<{ a: "a"; }, object, { foo: "foo"; }, unknown>'.     Types of property 'unstable_pipe' are incompatible.       Type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ a: { b: "a"; }; }, object, { foo: "foo"; }, $ContextOverridesOut, unknown> | MiddlewareBuilder<{ a: { b: "a"; }; foo: "foo"; }, object, $ContextOverridesOut, unknown>) => MiddlewareBuilder<...>' is not assignable to type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ a: "a"; }, object, { foo: "foo"; }, $ContextOverridesOut, unknown> | MiddlewareBuilder<{ a: "a"; foo: "foo"; }, object, $ContextOverridesOut, unknown>) => MiddlewareBuilder<...>'.         Types of parameters 'fn' and 'fn' are incompatible.           Type 'MiddlewareFunction<{ a: "a"; }, object, { foo: "foo"; }, any, unknown> | MiddlewareBuilder<{ a: "a"; foo: "foo"; }, object, any, unknown>' is not assignable to type 'MiddlewareFunction<{ a: { b: "a"; }; }, object, { foo: "foo"; }, any, unknown> | MiddlewareBuilder<{ a: { b: "a"; }; foo: "foo"; }, object, any, unknown>'.             Type 'MiddlewareFunction<{ a: "a"; }, object, { foo: "foo"; }, any, unknown>' is not assignable to type 'MiddlewareFunction<{ a: { b: "a"; }; }, object, { foo: "foo"; }, any, unknown> | MiddlewareBuilder<{ a: { b: "a"; }; foo: "foo"; }, object, any, unknown>'.               Type 'MiddlewareFunction<{ a: "a"; }, object, { foo: "foo"; }, any, unknown>' is not assignable to type 'MiddlewareFunction<{ a: { b: "a"; }; }, object, { foo: "foo"; }, any, unknown>'.                 Types of parameters 'opts' and 'opts' are incompatible.                   Type '{ ctx: { a: { b: "a"; }; foo: "foo"; }; type: "query" | "mutation" | "subscription"; path: string; input: unknown; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }' is not assignable to type '{ ctx: { a: "a"; foo: "foo"; }; type: "query" | "mutation" | "subscription"; path: string; input: unknown; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }'.                     The types of 'ctx.a' are incompatible between these types.                       Type '{ b: "a"; }' is not assignable to type '"a"'.  // ✅ `ctx.a` overlaps from `barMiddleware` and `fooMiddleware`  barMiddleware.unstable_pipe(fooMiddleware);  ``

tRPC has an experimental API called `experimental_standaloneMiddleware` which allows you to independently define a middleware that can be used with any tRPC instance. Creating middlewares using `t.middleware` has the limitation that the `Context` type is tied to the `Context` type of the tRPC instance. This means that you cannot use the same middleware with multiple tRPC instances that have different `Context` types.

Using `experimental_standaloneMiddleware` you can create a middleware that explicitly defines its requirements, i.e. the Context, Input and Meta types:

ts

`import {`

  `experimental_standaloneMiddleware,`

  `initTRPC,`

  `TRPCError,`

`} from '@trpc/server';`

`import * as z from 'zod';`

`const projectAccessMiddleware = experimental_standaloneMiddleware<{`

  `ctx: { allowedProjects: string[] }; // defaults to 'object' if not defined`

  `input: { projectId: string }; // defaults to 'unknown' if not defined`

  `// 'meta', not defined here, defaults to 'object | undefined'`

`}>().create((opts) => {`

  `if (!opts.ctx.allowedProjects.includes(opts.input.projectId)) {`

    `throw new TRPCError({`

      `code: 'FORBIDDEN',`

      `message: 'Not allowed',`

    `});`

  `}`

  `return opts.next();`

`});`

`const t1 = initTRPC`

  `.context<{`

    `allowedProjects: string[];`

  `}>()`

  `.create();`

``// ✅ `ctx.allowedProjects` satisfies "string[]" and `input.projectId` satisfies "string"``

`const accessControlledProcedure = t1.procedure`

  `.input(z.object({ projectId: z.string() }))`

  `.use(projectAccessMiddleware);`

``// ❌ `ctx.allowedProjects` satisfies "string[]" but `input.projectId` does not satisfy "string"``

`const accessControlledProcedure2 = t1.procedure`

  `.input(z.object({ projectId: z.number() }))`

  `.use(projectAccessMiddleware);`

``Argument of type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: string; }>' is not assignable to parameter of type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: number; }> | MiddlewareFunction<{ allowedProjects: string[]; }, object, object, object, { projectId: number; }>'.   Type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: string; }>' is not assignable to type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: number; }>'.     Types of property 'unstable_pipe' are incompatible.       Type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ allowedProjects: string[]; }, object, object, $ContextOverridesOut, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, $ContextOverridesOut, { ...; }>) => MiddlewareBuilder<...>' is not assignable to type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ allowedProjects: string[]; }, object, object, $ContextOverridesOut, { projectId: number; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, $ContextOverridesOut, { ...; }>) => MiddlewareBuilder<...>'.         Types of parameters 'fn' and 'fn' are incompatible.           Type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: number; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, any, { projectId: number; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, any, { projectId: string; }>'.             Type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: number; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, any, { projectId: string; }>'.               Type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: number; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }>'.                 Types of parameters 'opts' and 'opts' are incompatible.                   Type '{ ctx: { allowedProjects: string[]; }; type: "query" | "mutation" | "subscription"; path: string; input: { projectId: string; }; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }' is not assignable to type '{ ctx: { allowedProjects: string[]; }; type: "query" | "mutation" | "subscription"; path: string; input: { projectId: number; }; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }'.                     The types of 'input.projectId' are incompatible between these types.                       Type 'string' is not assignable to type 'number'.2345Argument of type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: string; }>' is not assignable to parameter of type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: number; }> | MiddlewareFunction<{ allowedProjects: string[]; }, object, object, object, { projectId: number; }>'.   Type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: string; }>' is not assignable to type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: number; }>'.     Types of property 'unstable_pipe' are incompatible.       Type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ allowedProjects: string[]; }, object, object, $ContextOverridesOut, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, $ContextOverridesOut, { ...; }>) => MiddlewareBuilder<...>' is not assignable to type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ allowedProjects: string[]; }, object, object, $ContextOverridesOut, { projectId: number; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, $ContextOverridesOut, { ...; }>) => MiddlewareBuilder<...>'.         Types of parameters 'fn' and 'fn' are incompatible.           Type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: number; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, any, { projectId: number; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, any, { projectId: string; }>'.             Type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: number; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, any, { projectId: string; }>'.               Type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: number; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }>'.                 Types of parameters 'opts' and 'opts' are incompatible.                   Type '{ ctx: { allowedProjects: string[]; }; type: "query" | "mutation" | "subscription"; path: string; input: { projectId: string; }; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }' is not assignable to type '{ ctx: { allowedProjects: string[]; }; type: "query" | "mutation" | "subscription"; path: string; input: { projectId: number; }; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }'.                     The types of 'input.projectId' are incompatible between these types.                       Type 'string' is not assignable to type 'number'.  // ❌ `ctx.allowedProjects` does not satisfy "string[]" even though `input.projectId` satisfies "string"  const t2 = initTRPC    .context<{      allowedProjects: number[];    }>()    .create();  const accessControlledProcedure3 = t2.procedure    .input(z.object({ projectId: z.string() }))    .use(projectAccessMiddleware);  Argument of type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: string; }>' is not assignable to parameter of type 'MiddlewareBuilder<{ allowedProjects: number[]; }, object, object, { projectId: string; }> | MiddlewareFunction<{ allowedProjects: number[]; }, object, object, object, { projectId: string; }>'.   Type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: string; }>' is not assignable to type 'MiddlewareBuilder<{ allowedProjects: number[]; }, object, object, { projectId: string; }>'.     Types of property 'unstable_pipe' are incompatible.       Type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ allowedProjects: string[]; }, object, object, $ContextOverridesOut, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, $ContextOverridesOut, { ...; }>) => MiddlewareBuilder<...>' is not assignable to type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ allowedProjects: number[]; }, object, object, $ContextOverridesOut, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: number[]; }, object, $ContextOverridesOut, { ...; }>) => MiddlewareBuilder<...>'.         Types of parameters 'fn' and 'fn' are incompatible.           Type 'MiddlewareFunction<{ allowedProjects: number[]; }, object, object, any, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: number[]; }, object, any, { projectId: string; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, any, { projectId: string; }>'.             Type 'MiddlewareFunction<{ allowedProjects: number[]; }, object, object, any, { projectId: string; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, any, { projectId: string; }>'.               Type 'MiddlewareFunction<{ allowedProjects: number[]; }, object, object, any, { projectId: string; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }>'.                 Types of parameters 'opts' and 'opts' are incompatible.                   Type '{ ctx: { allowedProjects: string[]; }; type: "query" | "mutation" | "subscription"; path: string; input: { projectId: string; }; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }' is not assignable to type '{ ctx: { allowedProjects: number[]; }; type: "query" | "mutation" | "subscription"; path: string; input: { projectId: string; }; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }'.                     The types of 'ctx.allowedProjects' are incompatible between these types.                       Type 'string[]' is not assignable to type 'number[]'.                         Type 'string' is not assignable to type 'number'.2345Argument of type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: string; }>' is not assignable to parameter of type 'MiddlewareBuilder<{ allowedProjects: number[]; }, object, object, { projectId: string; }> | MiddlewareFunction<{ allowedProjects: number[]; }, object, object, object, { projectId: string; }>'.   Type 'MiddlewareBuilder<{ allowedProjects: string[]; }, object, object, { projectId: string; }>' is not assignable to type 'MiddlewareBuilder<{ allowedProjects: number[]; }, object, object, { projectId: string; }>'.     Types of property 'unstable_pipe' are incompatible.       Type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ allowedProjects: string[]; }, object, object, $ContextOverridesOut, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, $ContextOverridesOut, { ...; }>) => MiddlewareBuilder<...>' is not assignable to type '<$ContextOverridesOut>(fn: MiddlewareFunction<{ allowedProjects: number[]; }, object, object, $ContextOverridesOut, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: number[]; }, object, $ContextOverridesOut, { ...; }>) => MiddlewareBuilder<...>'.         Types of parameters 'fn' and 'fn' are incompatible.           Type 'MiddlewareFunction<{ allowedProjects: number[]; }, object, object, any, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: number[]; }, object, any, { projectId: string; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, any, { projectId: string; }>'.             Type 'MiddlewareFunction<{ allowedProjects: number[]; }, object, object, any, { projectId: string; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }> | MiddlewareBuilder<{ allowedProjects: string[]; }, object, any, { projectId: string; }>'.               Type 'MiddlewareFunction<{ allowedProjects: number[]; }, object, object, any, { projectId: string; }>' is not assignable to type 'MiddlewareFunction<{ allowedProjects: string[]; }, object, object, any, { projectId: string; }>'.                 Types of parameters 'opts' and 'opts' are incompatible.                   Type '{ ctx: { allowedProjects: string[]; }; type: "query" | "mutation" | "subscription"; path: string; input: { projectId: string; }; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }' is not assignable to type '{ ctx: { allowedProjects: number[]; }; type: "query" | "mutation" | "subscription"; path: string; input: { projectId: string; }; getRawInput: GetRawInputFn; meta: object | undefined; signal: AbortSignal | undefined; next: { ...; }; }'.                     The types of 'ctx.allowedProjects' are incompatible between these types.                       Type 'string[]' is not assignable to type 'number[]'.                         Type 'string' is not assignable to type 'number'.``
