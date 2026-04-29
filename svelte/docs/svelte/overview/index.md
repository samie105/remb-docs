---
title: "Overview"
source: "https://svelte.dev/docs/svelte/overview"
canonical_url: "https://svelte.dev/docs/svelte/overview"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:32:12.323Z"
content_hash: "2b7ba0b91ec70b16b139df142c570d02a4fe49401d21fa9433c661495d57b195"
menu_path: ["Overview"]
section_path: []
nav_next: {"path": "../getting-started/index.md", "title": "Getting started"}
---

Svelte is a framework for building user interfaces on the web. It uses a compiler to turn declarative components written in HTML, CSS and JavaScript...

App

```
<script>
	function greet() {
		alert('Welcome to Svelte!');
	}
</script>

<button onclick={greet}>click me</button>

<style>
	button {
		font-size: 2em;
	}
</style>
```

```
<script lang="ts">
	function greet() {
		alert('Welcome to Svelte!');
	}
</script>

<button onclick={greet}>click me</button>

<style>
	button {
		font-size: 2em;
	}
</style>
```

...into lean, tightly optimized JavaScript.

You can use it to build anything on the web, from standalone components to ambitious full stack apps (using Svelte's companion application framework, [SvelteKit](../kit)) and everything in between.

These pages serve as reference documentation. If you're new to Svelte, we recommend starting with the [interactive tutorial](/tutorial) and coming back here when you have questions.

You can also try Svelte online in the [playground](/playground) or, if you need a more fully-featured environment, on [StackBlitz](https://sveltekit.new).

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/01-introduction/01-overview.md) [llms.txt](/docs/svelte/overview/llms.txt)

previous next

[Getting started](/docs/svelte/getting-started)
