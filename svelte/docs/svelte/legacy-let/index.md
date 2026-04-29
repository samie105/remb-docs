---
title: "Reactive let/var declarations"
source: "https://svelte.dev/docs/svelte/legacy-let"
canonical_url: "https://svelte.dev/docs/svelte/legacy-let"
docset: "svelte"
kind: "framework"
adapter: "generic"
last_crawled_at: "2026-04-18T16:48:02.670Z"
content_hash: "042d474c91cecb73e9775295b485c43b2dcc58a3949b210e6c3bd0b775b6da4c"
menu_path: ["Reactive let/var declarations"]
section_path: []
nav_prev: {"path": "../legacy-overview/index.md", "title": "Overview"}
nav_next: {"path": "../legacy-reactive-assignments/index.md", "title": "Reactive $: statements"}
---

In runes mode, reactive state is explicitly declared with the [`$state` rune]($state).

In legacy mode, variables declared at the top level of a component are automatically considered _reactive_. Reassigning or mutating these variables (`count += 1` or `object.x = y`) will cause the UI to update.

```
<script>
	let count = 0;
</script>

<button on:click={() => count += 1}>
	clicks: {count}
</button>
```

Because Svelte's legacy mode reactivity is based on _assignments_, using array methods like `.push()` and `.splice()` won't automatically trigger updates. A subsequent assignment is required to 'tell' the compiler to update the UI:

```
<script>
	let numbers = [1, 2, 3, 4];

	function addNumber() {
		// this method call does not trigger an update
		numbers.push(numbers.length + 1);

		// this assignment will update anything
		// that depends on `numbers`
		numbers = numbers;
	}
</script>
```

[Edit this page on GitHub](https://github.com/sveltejs/svelte/edit/main/documentation/docs/99-legacy/01-legacy-let.md) [llms.txt](/docs/svelte/legacy-let/llms.txt)

previous next

[Overview](/docs/svelte/legacy-overview) [Reactive $: statements](/docs/svelte/legacy-reactive-assignments)
