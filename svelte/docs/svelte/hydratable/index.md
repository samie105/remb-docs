---
title: "Hydratable data"
source: "https://svelte.dev/docs/svelte/hydratable"
canonical_url: "https://svelte.dev/docs/svelte/hydratable"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:42:24.815Z"
content_hash: "7edc2d13a9f5cf9b6ad794ef1c4f8c579ceb60ce9762bdb2c94fbed9814f2e60"
menu_path: ["Hydratable data"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/imperative-component-api/index.md", "title": "Imperative component API"}
nav_next: {"path": "svelte/docs/svelte/best-practices/index.md", "title": "Best practices"}
---

In Svelte, when you want to render asynchronous content data on the server, you can simply `await` it. This is great! However, it comes with a pitfall: when hydrating that content on the client, Svelte has to redo the asynchronous work, which blocks hydration for however long it takes:

```
<script>
  import { getUser } from 'my-database-library';

  // This will get the user on the server, render the user's name into the h1,
  // and then, during hydration on the client, it will get the user _again_,
  // blocking hydration until it's done.
  const user = await getUser();
</script>

<h1>{user.name}</h1>
```

That's silly, though. If we've already done the hard work of getting the data on the server, we don't want to get it again during hydration on the client. `hydratable` is a low-level API built to solve this problem. You probably won't need this very often — it will be used behind the scenes by whatever datafetching library you use. For example, it powers [remote functions in SvelteKit](/docs/kit/remote-functions).

To fix the example above:

```
<script>
  import { hydratable } from 'svelte';
  import { getUser } from 'my-database-library';

  // During server rendering, this will serialize and stash the result of `getUser`, associating
  // it with the provided key and baking it into the `head` content. During hydration, it will
  // look for the serialized version, returning it instead of running `getUser`. After hydration
  // is done, if it's called again, it'll simply invoke `getUser`.
  const user = await hydratable('user', () => getUser());
</script>

<h1>{user.name}</h1>
```

This API can also be used to provide access to random or time-based values that are stable between server rendering and hydration. For example, to get a random number that doesn't update on hydration:

```
import { function hydratable<T>(key: string, fn: () => T): Treferencehydratable } from 'svelte';
const const rand: numberrand = hydratable<number>(key: string, fn: () => number): numberreferencehydratable('random', () => var Math: MathAn intrinsic object that provides basic mathematics functionality and constants.
Math.Math.random(): numberReturns a pseudorandom number between 0 and 1.
random());
```

If you're a library author, be sure to prefix the keys of your `hydratable` values with the name of your library so that your keys don't conflict with other libraries.

## Serialization[](#Serialization)

All data returned from a `hydratable` function must be serializable. But this doesn't mean you're limited to JSON — Svelte uses [`devalue`](https://npmjs.com/package/devalue), which can serialize all sorts of things including `Map`, `Set`, `URL`, and `BigInt`. Check the documentation page for a full list. In addition to these, thanks to some Svelte magic, you can also fearlessly use promises:

```
<script>
  import { hydratable } from 'svelte';
  const promises = hydratable('random', () => {
	return {
	  one: Promise.resolve(1),
	  two: Promise.resolve(2)
	}
  });
</script>

{await promises.one}
{await promises.two}
```

## CSP[](#CSP)

`hydratable` adds an inline `<script>` block to the `head` returned from `render`. If you're using [Content Security Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Guides/CSP) (CSP), this script will likely fail to run. You can provide a `nonce` to `render`:

server

```
const const nonce: `${string}-${string}-${string}-${string}-${string}`nonce = var crypto: CryptoMDN Reference
crypto.Crypto.randomUUID(): `${string}-${string}-${string}-${string}-${string}`The randomUUID() method of the Crypto interface is used to generate a v4 UUID using a cryptographically secure random number generator.
Available only in secure contexts.
MDN Reference
randomUUID();

const { const head: stringHTML that goes into the <head>
head, const body: stringHTML that goes somewhere into the <body>
body } = await render<SvelteComponent<Record<string, any>, any, any>, Record<string, any>>(component: ComponentType<SvelteComponent<Record<string, any>, any, any>>, options?: {
    props?: Omit<Record<string, any>, "$$slots" | "$$events"> | undefined;
    context?: Map<any, any>;
    idPrefix?: string;
    csp?: Csp;
    transformError?: ((error: unknown) => unknown | Promise<unknown>) | undefined;
} | undefined): RenderOutputOnly available on the server and when compiling with the server option.
Takes a component and returns an object with body and head properties on it, which you can use to populate the HTML when server-rendering your app.
referencerender(const App: LegacyComponentTypeApp, {
	csp?: Csp | undefinedcsp: { nonce?: string | undefinednonce }
});
```

This will add the `nonce` to the script block, on the assumption that you will later add the same nonce to the CSP header of the document that contains it:

server

```
let response: Responseresponse.Response.headers: HeadersThe headers read-only property of the with the response.
MDN Reference
headers.Headers.set(name: string, value: string): voidThe set() method of the Headers interface sets a new value for an existing header inside a Headers object, or adds the header if it does not already exist.
MDN Reference
set(
  'Content-Security-Policy',
  `script-src 'nonce-${let nonce: stringnonce}'`
 );
```

It's essential that a `nonce` — which, British slang definition aside, means 'number used once' — is only used when dynamically server rendering an individual response.

If instead you are generating static HTML ahead of time, you must use hashes instead:

server

```
const { const head: stringHTML that goes into the <head>
head, const body: stringHTML that goes somewhere into the <body>
body, const hashes: {
    script: `sha256-${string}`[];
}hashes } = await render<SvelteComponent<Record<string, any>, any, any>, Record<string, any>>(component: ComponentType<SvelteComponent<Record<string, any>, any, any>>, options?: {
    props?: Omit<Record<string, any>, "$$slots" | "$$events"> | undefined;
    context?: Map<any, any>;
    idPrefix?: string;
    csp?: Csp;
    transformError?: ((error: unknown) => unknown | Promise<unknown>) | undefined;
} | undefined): RenderOutputOnly available on the server and when compiling with the server option.
Takes a component and returns an object with body and head properties on it, which you can use to populate the HTML when server-rendering your app.
referencerender(const App: LegacyComponentTypeApp, {
	csp?: Csp | undefinedcsp: { hash?: boolean | undefinedhash: true }
});
```

`hashes.script` will be an array of strings like `["sha256-abcd123"]`. As with `nonce`, the hashes should be used in your CSP header:

server

```
let response: Responseresponse.Response.headers: HeadersThe headers read-only property of the with the response.
MDN Reference
headers.Headers.set(name: string, value: string): voidThe set() method of the Headers interface sets a new value for an existing header inside a Headers object, or adds the header if it does not already exist.
MDN Reference
set(
  'Content-Security-Policy',
  `script-src ${let hashes: {
    script: string[];
}hashes.script: string[]script.Array<string>.map<string>(callbackfn: (value: string, index: number, array: string[]) => string, thisArg?: any): string[]Calls a defined callback function on each element of an array, and returns an array that contains the results.
@paramcallbackfn A function that accepts up to three arguments. The map method calls the callbackfn function one time for each element in the array.@paramthisArg An object to which the this keyword can refer in the callbackfn function. If thisArg is omitted, undefined is used as the this value.map((hash: stringhash) => `'${hash: stringhash}'`).Array<string>.join(separator?: string): stringAdds all the elements of an array into a string, separated by the specified separator string.
@paramseparator A string used to separate one element of the array from the next in the resulting string. If omitted, the array elements are separated with a comma.join(' ')}`
 );
```

We recommend using `nonce` over hash if you can, as `hash` will interfere with streaming SSR in the future.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/06-runtime/05-hydratable.md) [llms.txt](/docs/svelte/hydratable/llms.txt)

previous next

[Imperative component API](../imperative-component-api/index.md) [Best practices](../best-practices/index.md)
