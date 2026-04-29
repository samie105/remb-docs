---
title: "await"
source: "https://svelte.dev/docs/svelte/await-expressions"
canonical_url: "https://svelte.dev/docs/svelte/await-expressions"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:56.041Z"
content_hash: "9dadc7ef771e2f6ec9e2730176f095a97dddf41ed0eac9c02f64721b936f7ac9"
menu_path: ["await"]
section_path: []
nav_prev: {"path": "../class/index.md", "title": "class"}
nav_next: {"path": "../scoped-styles/index.md", "title": "Scoped styles"}
---

As of Svelte 5.36, you can use the `await` keyword inside your components in three places where it was previously unavailable:

*   at the top level of your component's `<script>`
*   inside `$derived(...)` declarations
*   inside your markup

This feature is currently experimental, and you must opt in by adding the `experimental.async` option wherever you [configure](/docs/kit/configuration) Svelte, usually `svelte.config.js`:

svelte.config

```
export default {
	compilerOptions: {
    experimental: {
        async: boolean;
    };
}compilerOptions: {
		experimental: {
    async: boolean;
}experimental: {
			async: booleanasync: true
		}
	}
};
```

The experimental flag will be removed in Svelte 6.

## Synchronized updates[](#Synchronized-updates)

When an `await` expression depends on a particular piece of state, changes to that state will not be reflected in the UI until the asynchronous work has completed, so that the UI is not left in an inconsistent state. In other words, in an example like this...

[Open in playground](/playground/untitled#H4sIAAAAAAAAA42RwU7DQAxEf8WyOCRqRAoSlzSJxB8gwY1wcBJHrLRxVrvelhLtv6O2QC8cuD6PxjP2ikIzY4XPRxne_SLmk0eIbiTlgAVOxnLA6nXFngJ_ax-duw17tspY4LCIsmjACusweOO07aRTywoEDdwEJeXsLt_90P5K789UOqVwlAGmKIOaRYDGMaMC-hzW07RTOpBRED7Ak19mEzjLphyaFgLri5l5iZpNBTxst3m-g7IE8momMxiyMLKl48XGs0YvQLCB_pwndVKX19RSG3FRQY-Omw4lzj37DqE3MlZ7spGblVL7L12fLo6uXSnBBtY-QQPrpclvwVSXrsUC_7qs8odipT5ygadNWJ3fgemtQCVjD0ZGrCaygdMXiHR87sgBAAA)

```
<script>
	let a = $state(1);
	let b = $state(2);

	async function add(a, b) {
		await new Promise((f) => setTimeout(f, 500)); // artificial delay
		return a + b;
	}
</script>

<input type="number" bind:value={a}>
<input type="number" bind:value={b}>

<p>{a} + {b} = {await add(a, b)}</p>
```

```
<script lang="ts">
	let a = $state(1);
	let b = $state(2);

	async function add(a, b) {
		await new Promise((f) => setTimeout(f, 500)); // artificial delay
		return a + b;
	}
</script>

<input type="number" bind:value={a}>
<input type="number" bind:value={b}>

<p>{a} + {b} = {await add(a, b)}</p>
```

...if you increment `a`, the contents of the `<p>` will _not_ immediately update to read this —

```
<p>2 + 2 = 3</p>
```

— instead, the text will update to `2 + 2 = 4` when `add(a, b)` resolves.

Updates can overlap — a fast update will be reflected in the UI while an earlier slow update is still ongoing.

## Concurrency[](#Concurrency)

Svelte will do as much asynchronous work as it can in parallel. For example if you have two `await` expressions in your markup...

```
<p>{await one(x)}</p>
<p>{await two(y)}</p>
```

...both functions will run at the same time, as they are independent expressions, even though they are _visually_ sequential.

This does not apply to sequential `await` expressions inside your `<script>` or inside async functions — these run like any other asynchronous JavaScript. An exception is that independent `$derived` expressions will update independently, even though they will run sequentially when they are first created:

```
// `b` will not be created until `a` has resolved,
// but once created they will update independently
// even if `x` and `y` update simultaneously
let let a: numbera = function $derived<number>(expression: number): number
namespace $derivedDeclares derived state, i.e. one that depends on other state variables.
The expression inside $derived(...) should be free of side-effects.
Example:
let double = $derived(count * 2);@see{@link https://svelte.dev/docs/svelte/$derived Documentation}@paramexpression The derived state expression$derived(await function one(x: number): Promise<number>@paramx one(let x: numberx));
let let b: numberb = function $derived<number>(expression: number): number
namespace $derivedDeclares derived state, i.e. one that depends on other state variables.
The expression inside $derived(...) should be free of side-effects.
Example:
let double = $derived(count * 2);@see{@link https://svelte.dev/docs/svelte/$derived Documentation}@paramexpression The derived state expression$derived(await function two(y: number): Promise<number>@paramy two(let y: numbery));
```

> If you write code like this, expect Svelte to give you an [`await_waterfall`](runtime-warnings#Client-warnings-await_waterfall) warning

## Indicating loading states[](#Indicating-loading-states)

To render placeholder UI, you can wrap content in a `<svelte:boundary>` with a [`pending`](svelte-boundary#Properties-pending) snippet. This will be shown when the boundary is first created, but not for subsequent updates, which are globally coordinated.

After the contents of a boundary have resolved for the first time and have replaced the `pending` snippet, you can detect subsequent async work with [`$effect.pending()`]($effect#$effect.pending). This is what you would use to display a "we're asynchronously validating your input" spinner next to a form field, for example.

You can also use [`settled()`](svelte#settled) to get a promise that resolves when the current update is complete:

```
import { function tick(): Promise<void>Returns a promise that resolves once any pending state changes have been applied.
referencetick, function settled(): Promise<void>Returns a promise that resolves once any state changes, and asynchronous work resulting from them,
have resolved and the DOM has been updated
@since5.36referencesettled } from 'svelte';

async function function onclick(): Promise<void>onclick() {
	let updating: booleanupdating = true;

	// without this, the change to `updating` will be
	// grouped with the other changes, meaning it
	// won't be reflected in the UI
	await function tick(): Promise<void>Returns a promise that resolves once any pending state changes have been applied.
referencetick();

	let color: stringcolor = 'octarine';
	let answer: numberanswer = 42;

	await function settled(): Promise<void>Returns a promise that resolves once any state changes, and asynchronous work resulting from them,
have resolved and the DOM has been updated
@since5.36referencesettled();

	// any updates affected by `color` or `answer`
	// have now been applied
	let updating: booleanupdating = false;
}
```

## Error handling[](#Error-handling)

Errors in `await` expressions will bubble to the nearest [error boundary](svelte-boundary).

## Server-side rendering[](#Server-side-rendering)

Svelte supports asynchronous server-side rendering (SSR) with the `render(...)` API. To use it, simply await the return value:

server

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
referencerender(const App: LegacyComponentTypeApp);
```

> If you're using a framework like SvelteKit, this is done on your behalf.

If a `<svelte:boundary>` with a `pending` snippet is encountered during SSR, that snippet will be rendered while the rest of the content is ignored. All `await` expressions encountered outside boundaries with `pending` snippets will resolve and render their contents prior to `await render(...)` returning.

> In the future, we plan to add a streaming implementation that renders the content in the background.

## Forking[](#Forking)

The [`fork(...)`](svelte#fork) API, added in 5.42, makes it possible to run `await` expressions that you _expect_ to happen in the near future. This is mainly intended for frameworks like SvelteKit to implement preloading when (for example) users signal an intent to navigate.

```
<script>
	import { fork } from 'svelte';
	import Menu from './Menu.svelte';

	let open = $state(false);

	/** @type {import('svelte').Fork | null} */
	let pending = null;

	function preload() {
		pending ??= fork(() => {
			open = true;
		});
	}

	function discard() {
		pending?.discard();
		pending = null;
	}
</script>

<button
	onfocusin={preload}
	onfocusout={discard}
	onpointerenter={preload}
	onpointerleave={discard}
	onclick={() => {
		pending?.commit();
		pending = null;

		// in case `pending` didn't exist
		// (if it did, this is a no-op)
		open = true;
	}}
>open menu</button>

{#if open}
	<!-- any async work inside this component will start
	     as soon as the fork is created -->
	<Menu onclose={() => open = false} />
{/if}
```

## Caveats[](#Caveats)

As an experimental feature, the details of how `await` is handled (and related APIs like `$effect.pending()`) are subject to breaking changes outside of a semver major release, though we intend to keep such changes to a bare minimum.

## Breaking changes[](#Breaking-changes)

Effects run in a slightly different order when the `experimental.async` option is `true`. Specifically, _block_ effects like `{#if ...}` and `{#each ...}` now run before an `$effect.pre` or `beforeUpdate` in the same component, which means that in [very rare situations](/playground/untitled?#H4sIAAAAAAAAE22R3VLDIBCFX2WLvUhnTHsf0zre-Q7WmfwtFV2BgU1rJ5N3F0jaOuoVcPbw7VkYhK4_URTiGYkMnIyjDjLsFGO3EvdCKkIvipdB8NlGXxSCPt96snbtj0gctab2-J_eGs2oOWBE6VunLO_2es-EDKZ5x5ZhC0vPNWM2gHXGouNzAex6hHH1cPHil_Lsb95YT9VQX6KUAbS2DrNsBdsdDFHe8_XSYjH1SrhELTe3MLpsemajweiWVPuxHSbKNd-8eQTdE0EBf4OOaSg2hwNhhE_ABB_ulJzjj9FULvIcqgm5vnAqUB7wWFMfhuugQWkcAr8hVD-mq8D12kOep24J_IszToOXdveGDsuNnZwbJUNlXsKnhJdhUcTo42s41YpOSneikDV5HL8BktM6yRcCAAA=) it is possible to update a block that should no longer exist, but only if you update state inside an effect, [which you should avoid]($effect#When-not-to-use-$effect).

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/19-await-expressions.md) [llms.txt](/docs/svelte/await-expressions/llms.txt)

previous next

[class](/docs/svelte/class) [Scoped styles](/docs/svelte/scoped-styles)
