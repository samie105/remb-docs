---
title: "Middleware API Reference"
source: "https://docs.astro.build/en/reference/modules/astro-middleware/"
canonical_url: "https://docs.astro.build/en/reference/modules/astro-middleware/"
docset: "astro"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:47:46.554Z"
content_hash: "30234128160addd4d992fb585d96a09f3572fa1fc8efe7433c0d60de3dbc8873"
menu_path: ["Middleware API Reference"]
section_path: []
---
# Middleware API Reference

**Added in:** `astro@2.6.0`

Middleware allows you to intercept requests and responses and inject behaviors dynamically every time a page or endpoint is about to be rendered. For features and usage examples, [see our middleware guide](/en/guides/middleware/).

## Imports from `astro:middleware`

[Section titled “Imports from astro:middleware”](#imports-from-astromiddleware)

The following helpers are imported from the virtual middleware module:

```
import {  defineMiddleware,  sequence,} from 'astro:middleware';
```

### `defineMiddleware()`

[Section titled “defineMiddleware()”](#definemiddleware)

**Type:** `(fn: [MiddlewareHandler](#middlewarehandler)) => MiddlewareHandler`

A function for defining a middleware function with type safety. When you use this utility, the [`context`](#context) and [`next()`](#next) arguments are automatically typed, and you will get a Typescript error if you try to return a [value not supported in your middleware](#middlewarehandler).

```
import { defineMiddleware } from "astro:middleware";
export const onRequest = defineMiddleware((context, next) => {  /* your middleware logic */});
```

### `sequence()`

[Section titled “sequence()”](#sequence)

**Type:** `(…handlers: [MiddlewareHandler](#middlewarehandler)[]) => MiddlewareHandler`

A function that accepts middleware functions as arguments, and will execute them in the order in which they are passed.

```
import { sequence } from "astro:middleware";
async function validation(context, next) {/* ... */}async function auth(context, next) {/* ... */}async function greeting(context, next) {/* ... */}
export const onRequest = sequence(validation, auth, greeting);
```

## Imports from `astro/middleware`

[Section titled “Imports from astro/middleware”](#imports-from-astromiddleware-1)

The following helpers can be imported from the regular middleware module when you build an [Astro Integration](/en/reference/integrations-reference/):

```
import {  createContext,  defineMiddleware,  sequence,  trySerializeLocals,} from "astro/middleware";
```

### `createContext()`

[Section titled “createContext()”](#createcontext)

**Type:** `(context: [CreateContext](#createcontext-1)) => [APIContext](/en/reference/api-reference/)`  

**Added in:** `astro@2.8.0`

A low-level API to create an [`APIContext`](/en/reference/api-reference/)to be passed to an Astro middleware [`onRequest()` function](#onrequest).

This function can be used by integrations/adapters to programmatically execute the Astro middleware.

### `defineMiddleware()`

[Section titled “defineMiddleware()”](#definemiddleware-1)

See [`defineMiddleware()`](#definemiddleware) from `astro:middleware`.

### `sequence()`

[Section titled “sequence()”](#sequence-1)

See [`sequence()`](#sequence) from `astro:middleware`.

### `trySerializeLocals()`

[Section titled “trySerializeLocals()”](#tryserializelocals)

**Type:** `(value: unknown) => string`  

**Added in:** `astro@2.8.0`

A low-level API that takes in any value and tries to return a serialized version (a string) of it. If the value cannot be serialized, the function will throw a runtime error.

## `astro/middleware` types

[Section titled “astro/middleware types”](#astromiddleware-types)

The following types are imported from the regular middleware module:

```
import type {  CreateContext,} from "astro/middleware";
```

### `CreateContext`

[Section titled “CreateContext”](#createcontext-1)

**Type:** `{ request: Request; params?: Params; userDefinedLocales?: string[]; defaultLocale: string; locals: App.Locals; clientAddress?: string }`  

**Added in:** `astro@2.8.0`

An object to [create a context](#createcontext) to be passed to an Astro middleware. This contains the following properties:

#### `CreateContext.request`

[Section titled “CreateContext.request”](#createcontextrequest)

**Type:** `Request`

The incoming [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) object.

#### `CreateContext.params`

[Section titled “CreateContext.params”](#createcontextparams)

**Type:** `Params`

An object containing the optional parameters to be passed to [`Astro.params`](/en/reference/api-reference/#params).

#### `CreateContext.userDefinedLocales`

[Section titled “CreateContext.userDefinedLocales”](#createcontextuserdefinedlocales)

**Type:** `string[]`  

**Added in:** `astro@3.5.0`

A list of supported locales defined in the [user’s `i18n` configuration](/en/reference/configuration-reference/#i18nlocales).

#### `CreateContext.defaultLocale`

[Section titled “CreateContext.defaultLocale”](#createcontextdefaultlocale)

**Type:** `string`  

**Added in:** `astro@4.16.0`

The default locale defined in the [user’s `i18n` configuration](/en/reference/configuration-reference/#i18ndefaultlocale).

#### `CreateContext.locals`

[Section titled “CreateContext.locals”](#createcontextlocals)

**Type:** `App.Locals`  

**Added in:** `astro@5.0.0`

An object for storing arbitrary information from a middleware, accessible to the user via [`Astro.locals`](/en/reference/api-reference/#locals).

Learn more about [storing data in `locals`](/en/guides/middleware/#storing-data-in-contextlocals) with example usage.

#### `CreateContext.clientAddress`

[Section titled “CreateContext.clientAddress”](#createcontextclientaddress)

**Type:** `string`  

**Added in:** `astro@6.0.0`

The [IP address](https://en.wikipedia.org/wiki/IP_address) of the request.

This must be provided by the adapter or platform from a trusted source (e.g. socket address, platform-provided header).

If not provided, accessing `clientAddress` will throw an error.

## `astro` types

[Section titled “astro types”](#astro-types)

```
import type {  MiddlewareHandler,  MiddlewareNext,  RewritePayload,} from "astro";
```

### `MiddlewareHandler`

[Section titled “MiddlewareHandler”](#middlewarehandler)

**Type:** `(context: [APIContext](/en/reference/api-reference/), next: [MiddlewareNext](#middlewarenext)) => Promise<Response> | Response | Promise<void> | void`

Represents an Astro middleware function. Middleware handlers receive two arguments and can either return a `Response` directly or call `next()` to invoke the next middleware in the chain. Alternatively, you can use [`defineMiddleware()`](#definemiddleware) to get type safety for your middleware.

The following example imports the `MiddlewareHandler` type to get type safety in the [`onRequest()`](#onrequest) function:

```
import type { MiddlewareHandler } from "astro";
export const onRequest: MiddlewareHandler = (context, next) => {  /* the middleware logic */};
```

A middleware handler receives the following properties:

#### `context`

[Section titled “context”](#context)

**Type:** [`APIContext`](/en/reference/api-reference/)

An [Astro context](/en/reference/api-reference/) object mirroring many of the `Astro` global properties.

#### `next()`

[Section titled “next()”](#next)

**Type:** [`MiddlewareNext`](#middlewarenext)  

A function that calls all the subsequent middleware in the chain and returns a `Response`. For example, other middleware could modify the HTML body of a response and awaiting the result of `next()` would allow your middleware to respond to those changes.

Since Astro v4.13.0, `next()` accepts an optional URL path parameter in the form of a string, `URL`, or `Request` to [rewrite](/en/guides/routing/#rewrites) the current request without retriggering a new rendering phase.

The following example uses `next()` to serve content from a different path when the current path matches `/old-path`:

```
import type { MiddlewareHandler } from "astro";
export const onRequest: MiddlewareHandler = (context, next) => {  if (context.url.pathname === '/old-path') {    return next('/new-path');  }  return next();};
```

### `MiddlewareNext`

[Section titled “MiddlewareNext”](#middlewarenext)

**Type:** `(rewritePayload?: [RewritePayload](#rewritepayload)) => Promise<Response>`  

Represents the [`next()` function](#next) passed to middleware handlers.

### `RewritePayload`

[Section titled “RewritePayload”](#rewritepayload)

**Type:** `string | URL | Request`  

**Added in:** `astro@4.13.0`

Represents the destination for a [rewrite](/en/guides/routing/#rewrites) when passed to the [`next()`](#next) function.

## Middleware exports

[Section titled “Middleware exports”](#middleware-exports)

When defining your project’s middleware in `src/middleware.js`, export the following user-defined functions:

### `onRequest()`

[Section titled “onRequest()”](#onrequest)

**Type:** [`MiddlewareHandler`](#middlewarehandler)

A required exported function from `src/middleware.js` that will be called before rendering every page or API route. It receives two arguments: [`context`](#context) and [`next()`](#next). `onRequest()` must return a `Response`: either directly, or by calling `next()`.

```
export function onRequest (context, next) {  // intercept response data from a request  // optionally, transform the response  // return a Response directly, or the result of calling `next()`  return next();};
```

[Contribute](/en/contribute/) [Community](https://astro.build/chat) [Sponsor](https://opencollective.com/astrodotbuild)
