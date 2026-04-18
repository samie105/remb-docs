---
title: "use:"
source: "https://svelte.dev/docs/svelte/use"
canonical_url: "https://svelte.dev/docs/svelte/use"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:37:31.228Z"
content_hash: "3c1c01f1e66107b3b4279a5c34de5e19813dd7eeba3f3d65dfdf6df065fb8520"
menu_path: ["use:"]
section_path: []
nav_prev: {"path": "svelte/docs/svelte/bind/index.md", "title": "bind:"}
nav_next: {"path": "svelte/docs/svelte/transition/index.md", "title": "transition:"}
---

> In Svelte 5.29 and newer, consider using [attachments](@attach) instead, as they are more flexible and composable.

Actions are functions that are called when an element is mounted. They are added with the `use:` directive, and will typically use an `$effect` so that they can reset any state when the element is unmounted:

App

```
<script>
	/** @type {import('svelte/action').Action} */
	function myaction(node) {
		// the node has been mounted in the DOM

		$effect(() => {
			// setup goes here

			return () => {
				// teardown goes here
			};
		});
	}
</script>

<div use:myaction>...</div>
```

```
<script lang="ts">
	import type { Action } from 'svelte/action';

	const myaction: Action = (node) => {
		// the node has been mounted in the DOM

		$effect(() => {
			// setup goes here

			return () => {
				// teardown goes here
			};
		});
	};
</script>

<div use:myaction>...</div>
```

An action can be called with an argument:

App

```
<script>
	/** @type {import('svelte/action').Action} */
	function myaction(node, data) {
		// ...
	}
</script>

<div use:myaction={data}>...</div>
```

```
<script lang="ts">
	import type { Action } from 'svelte/action';

	const myaction: Action = (node, data) => {
		// ...
	};
</script>

<div use:myaction={data}>...</div>
```

The action is only called once (but not during server-side rendering) — it will _not_ run again if the argument changes.

> Legacy mode
> 
> Prior to the `$effect` rune, actions could return an object with `update` and `destroy` methods, where `update` would be called with the latest value of the argument if it changed. Using effects is preferred.

## Typing[](#Typing)

The `Action` interface receives three optional type arguments — a node type (which can be `Element`, if the action applies to everything), a parameter, and any custom event handlers created by the action:

App

```
<script>
	/**
	 * @type {import('svelte/action').Action<
	 * 	HTMLDivElement,
	 * 	undefined,
	 * 	{
	 * 		onswiperight: (e: CustomEvent) => void;
	 * 		onswipeleft: (e: CustomEvent) => void;
	 * 		// ...
	 * 	}
	 * >}
	 */
	function gestures(node) {
		$effect(() => {
			// ...
			node.dispatchEvent(new CustomEvent('swipeleft'));

			// ...
			node.dispatchEvent(new CustomEvent('swiperight'));
		});
	}
</script>

<div
	use:gestures
	onswipeleft={next}
	onswiperight={prev}
>...</div>
```

```
<script lang="ts">
	import type { Action } from 'svelte/action';

	const gestures: Action<
		HTMLDivElement,
		undefined,
		{
			onswiperight: (e: CustomEvent) => void;
			onswipeleft: (e: CustomEvent) => void;
			// ...
		}
	> = (node) => {
		$effect(() => {
			// ...
			node.dispatchEvent(new CustomEvent('swipeleft'));

			// ...
			node.dispatchEvent(new CustomEvent('swiperight'));
		});
	};
</script>

<div
	use:gestures
	onswipeleft={next}
	onswiperight={prev}
>...</div>
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/03-template-syntax/13-use.md) [llms.txt](/docs/svelte/use/llms.txt)

previous next

[bind:](/docs/svelte/bind) [transition:](/docs/svelte/transition)


