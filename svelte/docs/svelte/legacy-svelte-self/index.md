---
title: "<svelte:self>"
source: "https://svelte.dev/docs/svelte/legacy-svelte-self"
canonical_url: "https://svelte.dev/docs/svelte/legacy-svelte-self"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:49:45.880Z"
content_hash: "5d165f895b333c88abf17c7540e1efa7b7fb46cdac8c3c52d1e7ac1a9a4fdb45"
menu_path: ["<svelte:self>"]
section_path: []
nav_prev: {"path": "../legacy-svelte-component/index.md", "title": "<svelte:component>"}
nav_next: {"path": "../legacy-component-api/index.md", "title": "Imperative component API"}
---

The `<svelte:self>` element allows a component to include itself, recursively.

It cannot appear at the top level of your markup; it must be inside an if or each block or passed to a component's slot to prevent an infinite loop.

```
<script>
	export let count;
</script>

{#if count > 0}
	<p>counting down... {count}</p>
	<svelte:self count={count - 1} />
{:else}
	<p>lift-off!</p>
{/if}
```

> This concept is obsolete, as components can import themselves:
> 
> App
> 
> ```
> <script>
> 	import Self from './App.svelte'
> 	export let count;
> </script>
> 
> {#if count > 0}
> 	<p>counting down... {count}</p>
> 	<Self count={count - 1} />
> {:else}
> 	<p>lift-off!</p>
> {/if}
> ```
> 
> ```
> <script lang="ts">
> 	import Self from './App.svelte'
> 	export let count;
> </script>
> 
> {#if count > 0}
> 	<p>counting down... {count}</p>
> 	<Self count={count - 1} />
> {:else}
> 	<p>lift-off!</p>
> {/if}
> ```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/99-legacy/31-legacy-svelte-self.md) [llms.txt](/docs/svelte/legacy-svelte-self/llms.txt)

previous next

[<svelte:component>](/docs/svelte/legacy-svelte-component) [Imperative component API](/docs/svelte/legacy-component-api)
