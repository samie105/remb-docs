---
title: "transition:"
source: "https://svelte.dev/docs/svelte/transition"
canonical_url: "https://svelte.dev/docs/svelte/transition"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:38:08.412Z"
content_hash: "dd4b59587761d53b454d46878dc2c90941639a66aa0033a8bfd99e9955202a02"
menu_path: ["transition:"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/use/index.md", "title": "use:"}
nav_next: {"path": "svelte/docs/svelte/in-and-out/index.md", "title": "in: and out:"}
---

A _transition_ is triggered by an element entering or leaving the DOM as a result of a state change.

When a block (such as an `{#if ...}` block) is transitioning out, all elements inside it, including those that do not have their own transitions, are kept in the DOM until every transition in the block has been completed.

The `transition:` directive indicates a _bidirectional_ transition, which means it can be smoothly reversed while the transition is in progress.

```
<script>
	import { fade } from 'svelte/transition';

	let visible = $state(false);
</script>

<button onclick={() => visible = !visible}>toggle</button>

{#if visible}
	<div transition:fade>fades in and out</div>
{/if}
```

## Local vs global[](#Local-vs-global)

Transitions are local by default. Local transitions only play when the block they belong to is created or destroyed, _not_ when parent blocks are created or destroyed.

```
{#if x}
	{#if y}
		<p transition:fade>fades in and out only when y changes</p>

		<p transition:fade|global>fades in and out when x or y change</p>
	{/if}
{/if}
```

## Built-in transitions[](#Built-in-transitions)

A selection of built-in transitions can be imported from the [`svelte/transition`](svelte-transition) module.

## Transition parameters[](#Transition-parameters)

Transitions can have parameters.

(The double `{{curlies}}` aren't a special syntax; this is an object literal inside an expression tag.)

```
{#if visible}
	<div transition:fade={{ duration: 2000 }}>fades in and out over two seconds</div>
{/if}
```

## Custom transition functions[](#Custom-transition-functions)

```
transition = (node: HTMLElementnode: HTMLElement, params: anyparams: any, options: {
    direction: "in" | "out" | "both";
}options: { direction: "in" | "out" | "both"direction: 'in' | 'out' | 'both' }) => {
	delay?: number,
	duration?: number,
	easing?: (t: numbert: number) => number,
	css?: (t: numbert: number, u: numberu: number) => string,
	tick?: (t: numbert: number, u: numberu: number) => void
}
```

Transitions can use custom functions. If the returned object has a `css` function, Svelte will generate keyframes for a [web animation](https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API).

The `t` argument passed to `css` is a value between `0` and `1` after the `easing` function has been applied. _In_ transitions run from `0` to `1`, _out_ transitions run from `1` to `0` — in other words, `1` is the element's natural state, as though no transition had been applied. The `u` argument is equal to `1 - t`.

The function is called repeatedly _before_ the transition begins, with different `t` and `u` arguments.

App

```
<script>
	import { elasticOut } from 'svelte/easing';

	/** @type {boolean} */
	export let visible;

	/**
	 * @param {HTMLElement} node
	 * @param {{ delay?: number, duration?: number, easing?: (t: number) => number }} params
	 */
	function whoosh(node, params) {
		const existingTransform = getComputedStyle(node).transform.replace('none', '');

		return {
			delay: params.delay || 0,
			duration: params.duration || 400,
			easing: params.easing || elasticOut,
			css: (t, u) => `transform: ${existingTransform} scale(${t})`
		};
	}
</script>

{#if visible}
	<div in:whoosh>whooshes in</div>
{/if}
```

```
<script lang="ts">
	import { elasticOut } from 'svelte/easing';
	export let visible: boolean;

	function whoosh(node: HTMLElement, params: { delay?: number, duration?: number, easing?: (t: number) => number }) {
		const existingTransform = getComputedStyle(node).transform.replace('none', '');

		return {
			delay: params.delay || 0,
			duration: params.duration || 400,
			easing: params.easing || elasticOut,
			css: (t, u) => `transform: ${existingTransform} scale(${t})`
		};
	}
</script>

{#if visible}
	<div in:whoosh>whooshes in</div>
{/if}
```

A custom transition function can also return a `tick` function, which is called _during_ the transition with the same `t` and `u` arguments.

> If it's possible to use `css` instead of `tick`, do so — web animations can run off the main thread, preventing jank on slower devices.

App

```
<script>
	export let visible = false;

	/**
	 * @param {HTMLElement} node
	 * @param {{ speed?: number }} params
	 */
	function typewriter(node, { speed = 1 }) {
		const valid = node.childNodes.length === 1 && node.childNodes[0].nodeType === Node.TEXT_NODE;

		if (!valid) {
			throw new Error(`This transition only works on elements with a single text node child`);
		}

		const text = node.textContent;
		const duration = text.length / (speed * 0.01);

		return {
			duration,
			tick: (t) => {
				const i = ~~(text.length * t);
				node.textContent = text.slice(0, i);
			}
		};
	}
</script>

{#if visible}
	<p in:typewriter={{ speed: 1 }}>The quick brown fox jumps over the lazy dog</p>
{/if}
```

```
<script lang="ts">
	export let visible = false;

	function typewriter(node: HTMLElement, { speed = 1 }: { speed?: number }) {
		const valid = node.childNodes.length === 1 && node.childNodes[0].nodeType === Node.TEXT_NODE;

		if (!valid) {
			throw new Error(`This transition only works on elements with a single text node child`);
		}

		const text = node.textContent;
		const duration = text.length / (speed * 0.01);

		return {
			duration,
			tick: (t) => {
				const i = ~~(text.length * t);
				node.textContent = text.slice(0, i);
			}
		};
	}
</script>

{#if visible}
	<p in:typewriter={{ speed: 1 }}>The quick brown fox jumps over the lazy dog</p>
{/if}
```

If a transition returns a function instead of a transition object, the function will be called in the next microtask. This allows multiple transitions to coordinate, making [crossfade effects](/tutorial/deferred-transitions) possible.

Transition functions also receive a third argument, `options`, which contains information about the transition.

Available values in the `options` object are:

*   `direction` - one of `in`, `out`, or `both` depending on the type of transition

## Transition events[](#Transition-events)

An element with transitions will dispatch the following events in addition to any standard DOM events:

*   `introstart`
*   `introend`
*   `outrostart`
*   `outroend`

```
{#if visible}
	<p
		transition:fly={{ y: 200, duration: 2000 }}
		onintrostart={() => (status = 'intro started')}
		onoutrostart={() => (status = 'outro started')}
		onintroend={() => (status = 'intro ended')}
		onoutroend={() => (status = 'outro ended')}
	>
		Flies in and out
	</p>
{/if}
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/14-transition.md) [llms.txt](/docs/svelte/transition/llms.txt)

previous next

[use:](/docs/svelte/use) [in: and out:](/docs/svelte/in-and-out)
