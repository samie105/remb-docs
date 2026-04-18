---
title: "<svelte:boundary>"
source: "https://svelte.dev/docs/svelte/svelte-boundary"
canonical_url: "https://svelte.dev/docs/svelte/svelte-boundary"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:39:58.569Z"
content_hash: "4d0cc91d9b93580af590936350ddbf079a42f21391f84882db95e09f33b43829"
menu_path: ["<svelte:boundary>"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/nested-style-elements/index.md", "title": "Nested <style> elements"}
nav_next: {"path": "svelte/docs/svelte/svelte-window/index.md", "title": "<svelte:window>"}
---

```
<svelte:boundary onerror={handler}>...</svelte:boundary>
```

> This feature was added in 5.3.0

Boundaries allow you to 'wall off' parts of your app, so that you can:

*   provide UI that should be shown when [`await`](await-expressions) expressions are first resolving
*   handle errors that occur during rendering or while running effects, and provide UI that should be rendered when an error happens

If a boundary handles an error (with a `failed` snippet or `onerror` handler, or both) its existing content will be removed.

> Errors occurring outside the rendering process (for example, in event handlers or after a `setTimeout` or async work) are _not_ caught by error boundaries.

## Properties[](#Properties)

For the boundary to do anything, one or more of the following must be provided.

### pending[](#Properties-pending)

This snippet will be shown when the boundary is first created, and will remain visible until all the [`await`](await-expressions) expressions inside the boundary have resolved ([demo](/playground/untitled#H4sIAAAAAAAAE21QQW6DQAz8ytY9BKQVpFdKkPqDHnorPWzAaSwt3tWugUaIv1eE0KpKD5as8YxnNBOw6RAKKOOAVrA4up5bEy6VGknOyiO3xJ8qMnmPAhpOZDFC8T6BXPyiXADQ258X77P1FWg4moj_4Y1jQZZ49W0CealqruXUcyPkWLVozQXbZDC2R606spYiNo7bqA7qab_fp2paFLUElD6wYhzVa3AdRUySgNHZAVN1qDZaLRHljTp0vSTJ9XJjrSbpX5f0eZXN6zLXXOa_QfmurIVU-moyoyH5ib87o7XuYZfOZe6vnGWmx1uZW7lJOq9upa-sMwuUZdkmmfIbfQ1xZwwaBL8ECgk9zh8axJAdiVsoTsZGnL8Bg4tX_OMBAAA=)):

```
<svelte:boundary>
	<p>{await delayed('hello!')}</p>

	{#snippet pending()}
		<p>loading...</p>
	{/snippet}
</svelte:boundary>
```

The `pending` snippet will _not_ be shown for subsequent async updates — for these, you can use [`$effect.pending()`]($effect#$effect.pending).

> In the [playground](/playground), your app is rendered inside a boundary with an empty pending snippet, so that you can use `await` without having to create one.

### failed[](#Properties-failed)

If a `failed` snippet is provided, it will be rendered when an error is thrown inside the boundary, with the `error` and a `reset` function that recreates the contents ([demo](/playground/hello-world#H4sIAAAAAAAAE3VRy26DMBD8lS2tFCIh6JkAUlWp39Cq9EBg06CAbdlLArL87zWGKk8ORnhmd3ZnrD1WtOjFXqKO2BDGW96xqpBD5gXerm5QefG39mgQY9EIWHxueRMinLosti0UPsJLzggZKTeilLWgLGc51a3gkuCjKQ7DO7cXZotgJ3kLqzC6hmex1SZnSXTWYHcrj8LJjWTk0PHoZ8VqIdCOKayPykcpuQxAokJaG1dGybYj4gw4K5u6PKTasSbjXKgnIDlA8VvUdo-pzonraBY2bsH7HAl78mKSHZpgIcuHjq9jXSpZSLixRlveKYQUXhQVhL6GPobXAAb7BbNeyvNUs4qfRg3OnELLj5hqH9eQZqCnoBwR9lYcQxuVXeBzc8kMF8yXY4yNJ5oGiUzP_aaf_waTRGJib5_Ad3P_vbCuaYxzeNpbU0eUMPAOKh7Yw1YErgtoXyuYlPLzc10_xo_5A91zkQL_AgAA)):

```
<svelte:boundary>
	<FlakyComponent />

	{#snippet failed(error, reset)}
		<button onclick={reset}>oops! try again</button>
	{/snippet}
</svelte:boundary>
```

> As with [snippets passed to components](snippet#Passing-snippets-to-components), the `failed` snippet can be passed explicitly as a property...
> 
> ```
> <svelte:boundary {failed}>...</svelte:boundary>
> ```
> 
> ...or implicitly by declaring it directly inside the boundary, as in the example above.

### onerror[](#Properties-onerror)

If an `onerror` function is provided, it will be called with the same two `error` and `reset` arguments. This is useful for tracking the error with an error reporting service...

```
<svelte:boundary onerror={(e) => report(e)}>
	...
</svelte:boundary>
```

...or using `error` and `reset` outside the boundary itself:

```
<script>
	let error = $state(null);
	let reset = $state(() => {});

	function onerror(e, r) {
		error = e;
		reset = r;
	}
</script>

<svelte:boundary {onerror}>
	<FlakyComponent />
</svelte:boundary>

{#if error}
	<button onclick={() => {
		error = null;
		reset();
	}}>
		oops! try again
	</button>
{/if}
```

If an error occurs inside the `onerror` function (or if you rethrow the error), it will be handled by a parent boundary if such exists.

## Using transformError[](#Using-transformError)

By default, error boundaries have no effect on the server — if an error occurs during rendering, the render as a whole will fail.

Since 5.51 you can control this behaviour for boundaries with a `failed` snippet, by calling [`render(...)`](imperative-component-api#render) with a `transformError` function.

> If you're using Svelte via a framework such as SvelteKit, you most likely don't have direct access to the `render(...)` call — the framework must configure `transformError` on your behalf. SvelteKit will add support for this in the near future, via the [`handleError`](../kit/hooks#Shared-hooks-handleError) hook.

The `transformError` function must return a JSON-stringifiable object which will be used to render the `failed` snippet. This object will be serialized and used to hydrate the snippet in the browser:

```
import { function render<Comp extends SvelteComponent<any> | Component<any>, Props extends ComponentProps<Comp> = ComponentProps<Comp>>(...args: {} extends Props ? [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options?: {
    props?: Omit<Props, "$$slots" | "$$events">;
    context?: Map<any, any>;
    idPrefix?: string;
    csp?: Csp;
    transformError?: (error: unknown) => unknown | Promise<unknown>;
}] : [component: Comp extends SvelteComponent<any> ? ComponentType<Comp> : Comp, options: {
    props: Omit<Props, "$$slots" | "$$events">;
    context?: Map<any, any>;
    idPrefix?: string;
    csp?: Csp;
    transformError?: (error: unknown) => unknown | Promise<unknown>;
}]): RenderOutputOnly available on the server and when compiling with the server option.
Takes a component and returns an object with body and head properties on it, which you can use to populate the HTML when server-rendering your app.
referencerender } from 'svelte/server';
import type App = SvelteComponent<Record<string, any>, any, any>
const App: LegacyComponentTypeApp from './App.svelte';

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
	transformError?: ((error: unknown) => unknown | Promise<unknown>) | undefinedtransformError: (error: unknownerror) => {
		// log the original error, with the stack trace...
		var console: ConsoleThe console module provides a simple debugging console that is similar to the
JavaScript console mechanism provided by web browsers.
The module exports two specific components:

A Console class with methods such as console.log(), console.error() and console.warn() that can be used to write to any Node.js stream.
A global console instance configured to write to process.stdout and
process.stderr. The global console can be used without importing the node:console module.

Warning: The global console object's methods are neither consistently
synchronous like the browser APIs they resemble, nor are they consistently
asynchronous like all other Node.js streams. See the note on process I/O for
more information.
Example using the global console:
console.log('hello world');
// Prints: hello world, to stdout
console.log('hello %s', 'world');
// Prints: hello world, to stdout
console.error(new Error('Whoops, something bad happened'));
// Prints error message and stack trace to stderr:
//   Error: Whoops, something bad happened
//     at [eval]:5:15
//     at Script.runInThisContext (node:vm:132:18)
//     at Object.runInThisContext (node:vm:309:38)
//     at node:internal/process/execution:77:19
//     at [eval]-wrapper:6:22
//     at evalScript (node:internal/process/execution:76:60)
//     at node:internal/main/eval_string:23:3

const name = 'Will Robinson';
console.warn(`Danger ${name}! Danger!`);
// Prints: Danger Will Robinson! Danger!, to stderrExample using the Console class:
const out = getStreamSomehow();
const err = getStreamSomehow();
const myConsole = new console.Console(out, err);

myConsole.log('hello world');
// Prints: hello world, to out
myConsole.log('hello %s', 'world');
// Prints: hello world, to out
myConsole.error(new Error('Whoops, something bad happened'));
// Prints: [Error: Whoops, something bad happened], to err

const name = 'Will Robinson';
myConsole.warn(`Danger ${name}! Danger!`);
// Prints: Danger Will Robinson! Danger!, to err@seesourceconsole.Console.error(message?: any, ...optionalParams: any[]): void (+1 overload)Prints to stderr with newline. Multiple arguments can be passed, with the
first used as the primary message and all additional used as substitution
values similar to printf(3)
(the arguments are all passed to util.format()).
const code = 5;
console.error('error #%d', code);
// Prints: error #5, to stderr
console.error('error', code);
// Prints: error 5, to stderrIf formatting elements (e.g. %d) are not found in the first string then
util.inspect() is called on each argument and the
resulting string values are concatenated. See util.format()
for more information.
@sincev0.1.100error(error: unknownerror);

		// ...and return a sanitized user-friendly error
		// to display in the `failed` snippet
		return {
			message: stringmessage: 'An error occurred!'
		};
	};
});
```

If `transformError` throws (or rethrows) an error, `render(...)` as a whole will fail with that error.

> Errors that occur during server-side rendering can contain sensitive information in the `message` and `stack`. It's recommended to redact these rather than sending them unaltered to the browser.

If the boundary has an `onerror` handler, it will be called upon hydration with the deserialized error object.

The [`mount`](imperative-component-api#mount) and [`hydrate`](imperative-component-api#hydrate) functions also accept a `transformError` option, which defaults to the identity function. As with `render`, this function transforms a render-time error before it is passed to a `failed` snippet or `onerror` handler.

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/05-special-elements/01-svelte-boundary.md) [llms.txt](/docs/svelte/svelte-boundary/llms.txt)

previous next

[Nested <style> elements](/docs/svelte/nested-style-elements) [<svelte:window>](/docs/svelte/svelte-window)

