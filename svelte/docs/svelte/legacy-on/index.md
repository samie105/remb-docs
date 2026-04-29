---
title: "on:"
source: "https://svelte.dev/docs/svelte/legacy-on"
canonical_url: "https://svelte.dev/docs/svelte/legacy-on"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:44.225Z"
content_hash: "a418a30016a84f8a11c770847d9b6bdc3f151bb83344c8f7d33946e8bc055a02"
menu_path: ["on:"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/legacy-$$props-and-$$restProps/index.md", "title": "$$props and $$restProps"}
nav_next: {"path": "svelte/docs/svelte/legacy-slots/index.md", "title": "<slot>"}
---

In runes mode, event handlers are just like any other attribute or prop.

In legacy mode, we use the `on:` directive:

App

```
<script>
	let count = 0;

	/** @param {MouseEvent} event */
	function handleClick(event) {
		count += 1;
	}
</script>

<button on:click={handleClick}>
	count: {count}
</button>
```

```
<script lang="ts">
	let count = 0;

	function handleClick(event: MouseEvent) {
		count += 1;
	}
</script>

<button on:click={handleClick}>
	count: {count}
</button>
```

Handlers can be declared inline with no performance penalty:

```
<button on:click={() => (count += 1)}>
	count: {count}
</button>
```

Add _modifiers_ to element event handlers with the `|` character.

```
<form on:submit|preventDefault={handleSubmit}>
	<!-- the `submit` event's default is prevented,
	     so the page won't reload -->
</form>
```

The following modifiers are available:

*   `preventDefault` — calls `event.preventDefault()` before running the handler
*   `stopPropagation` — calls `event.stopPropagation()`, preventing the event reaching the next element
*   `stopImmediatePropagation` — calls `event.stopImmediatePropagation()`, preventing other listeners of the same event from being fired.
*   `passive` — improves scrolling performance on touch/wheel events (Svelte will add it automatically where it's safe to do so)
*   `nonpassive` — explicitly set `passive: false`
*   `capture` — fires the handler during the _capture_ phase instead of the _bubbling_ phase
*   `once` — remove the handler after the first time it runs
*   `self` — only trigger handler if `event.target` is the element itself
*   `trusted` — only trigger handler if `event.isTrusted` is `true`. I.e. if the event is triggered by a user action.

Modifiers can be chained together, e.g. `on:click|once|capture={...}`.

If the `on:` directive is used without a value, the component will _forward_ the event, meaning that a consumer of the component can listen for it.

```
<button on:click>
	The component itself will emit the click event
</button>
```

It's possible to have multiple event listeners for the same event:

App

```
<script>
	let count = 0;

	function increment() {
		count += 1;
	}

	/** @param {MouseEvent} event */
	function log(event) {
		console.log(event);
	}
</script>

<button on:click={increment} on:click={log}>
	clicks: {count}
</button>
```

```
<script lang="ts">
	let count = 0;

	function increment() {
		count += 1;
	}

	function log(event: MouseEvent) {
		console.log(event);
	}
</script>

<button on:click={increment} on:click={log}>
	clicks: {count}
</button>
```

## Component events[](#Component-events)

Components can dispatch events by creating a _dispatcher_ when they are initialised:

Stepper

```
<script>
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
</script>

<button on:click={() => dispatch('decrement')}>decrement</button>
<button on:click={() => dispatch('increment')}>increment</button>
```

```
<script lang="ts">
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
</script>

<button on:click={() => dispatch('decrement')}>decrement</button>
<button on:click={() => dispatch('increment')}>increment</button>
```

`dispatch` creates a [`CustomEvent`](https://developer.mozilla.org/en-US/docs/Web/API/CustomEvent). If a second argument is provided, it becomes the `detail` property of the event object.

A consumer of this component can listen for the dispatched events:

```
<script>
	import Stepper from './Stepper.svelte';

	let n = 0;
</script>

<Stepper
	on:decrement={() => n -= 1}
	on:increment={() => n += 1}
/>

<p>n: {n}</p>
```

Component events do not bubble — a parent component can only listen for events on its immediate children.

Other than `once`, modifiers are not valid on component event handlers.

> If you're planning an eventual migration to Svelte 5, use callback props instead. This will make upgrading easier as `createEventDispatcher` is deprecated:
> 
> Stepper
> 
> ```
> <script>
> 	export let decrement;
> 	export let increment;
> </script>
> 
> <button on:click={decrement}>decrement</button>
> <button on:click={increment}>increment</button>
> ```
> 
> ```
> <script lang="ts">
> 	export let decrement;
> 	export let increment;
> </script>
> 
> <button on:click={decrement}>decrement</button>
> <button on:click={increment}>increment</button>
> ```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/99-legacy/10-legacy-on.md) [llms.txt](/docs/svelte/legacy-on/llms.txt)

previous next

[$$props and $$restProps](/docs/svelte/legacy-$$props-and-$$restProps) [<slot>](../legacy-slots/index.md)
